label diana_cel_msg1_resposta:

    mc surpreso "Uma apresentação especial no Cassino só pra mim?!"

    "A [d] realmente parece bem agradecida pela pauta que eu entreguei para o chefe."

    mc charmoso "Não tenho por que não aproveitar uma noite especial no Cassino."

    "Caraca... vai ser incrível..."

    "O que eu respondo pra ela?"

    menu:
        "Estou louco pra ver você cantando ao vivo.":


            $ diana_seducao += 1

            "Quero muito poder ver ela cantando no Cassino. Tenho certeza que vai ser incrível."

            "..."

            $ diana_cel_msg1_r = "seducao"
        "Quero muito conhecer o Cassino.":


            "O Cassino deve ser incrível. Não vejo a hora de conhecer o lugar."

            "..."

            $ diana_cel_msg1_r = "amizade"

    "Pronto! Enviado."

    "..."

    "Ela já respondeu."

    show screen celular_diana

    "..."

    "Muito bom! Vou ver a [d] cantando amanhã. E pelo que eu entendi vai ser só pra mim."

    mc surpreso "Isso é incrível!"

    jump diana_evento2

label diana_evento4_pre:

    $ diana_e4 = "pre"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    mc surpreso "Opa! Alguém ligando."

    mc normal "Alô."

    d "[mc]?"

    mc "Oi, [d]. Tudo bem?"

    d "Sim. Você tá ocupado agora?"

    mc "Não, não. O que foi?"

    d "Eu queria muito sair com você."

    menu:
        "U-um encontro?!":


            mc surpreso "T-tipo um encontro?!"

            d "Isso. Mas não precisa ficar nervoso desse jeito {i}rsrs{/i}"

            mc envergonhado "Haha... Ok, eu topo."
        "Um encontro romântico?":


            $ diana_seducao += 1

            mc charmoso "Você diz um encontro só nos dois?"

            d "Isso mesmo. O que você acha?"

            mc "Seria incrível, [d]."

            d "Que bom."

    mc normal "Passo aí no cassino a noite então?"

    d "Não!"

    mc preocupado "..."

    d "Desculpa. É que eu preciso sair daqu- digo... eu quero poder falar com você em outro lugar."

    mc normal "Ok. Relaxa."

    menu:
        "Tenho um lugar que eu quero conhecer.":


            $ diana_seducao += 1

            mc normal "Ah! Tem um lugar que eu ouvi falar na redação da revista e queria conhecer."

            "Seria a hora perfeita pra ver aquele lugar..."

            d "Onde?"
        "Onde você gostaria de ir?":


            mc normal "Onde você gostaria de ir?"

            d "Eu? É... O que você sugere?"

            mc charmoso "Eu sou um cavalheiro. Prefiro que você escolha."

            d "..."

            d "E eu gostaria de ouvir sua sugestão."

            "Bom... se ela quer que eu escolha..."

    mc "Então. Eu ouvi falar de uma pizzaria tradicional lá no centro."

    mc "Escutei o povo falando que é a melhor pizza da capital. Eles tão lá há mais de 100 anos."

    d "..."

    mc desconfiado "[d]?"

    d "Alighieri?"

    mc surpreso "Isso mesmo!"

    d "Certeza que de todos os lugares, é lá que você quer se encontrar?"

    "Merda... será que é furreca demais? Mas falaram que é super tradicional!"

    if v27_fim:

        "Quando eu fui com o [n] lá, a gente ficou do lado de fora. Pareceu realmente um lugar incrível."

    mc desculpa "S-se você não gos-"

    d "Tudo bem. Qualquer lugar pra mim tá bom."

    d "Além do mais, tem até um certo tipo de poesia na sua escolha."

    mc desconfiado "Como?"

    d "Esquece. Ah! Eu vou te pedir uma coisa."

    mc normal "Claro."

    d "Eu queria que você chegasse lá e me avisasse. Eu me preparo e vou. Um motorista me deixa lá."

    d "Pode ser a noite que você quiser."

    mc desconfiado "O-ok. Mas-"

    d "Não se preocupe que não vou demorar. Só me avisar então. Beijos, [mc]."

    mc "Beijo..."

    "{i}Tu tu tu{/i}"

    "Que estranho. Será que aconteceu alguma coisa com ela?"

    "Bom... não importa. Só sei que por causa disso aí eu vou poder sair com a [d]."

    "Já é a quarta vez que eu vou poder falar com ela a sós. Talvez seja a hora de eu decidir o que eu quero com ela."

    if diana_e2 == "seducao":

        $ diana_quente = True

        "Aquele dia a gente se beijou no cassino."

        "Foi muito bom."

    if diana_e3 == "seducao":

        $ diana_quente = True

        "Aquela noite no quarto dela... eu tenho certeza que ia rolar alguma coisa."

        "Ela já tava abrindo o roupão e tudo."

    if diana_e2 != "seducao" and diana_e3 != "seducao":

        "Até agora eu tô sendo só um amigo pra ela. Não rolou nada mais quente entre a gente."

        "Será que eu só vou continuar assim?"

        "A [d] é um mulherão. Será que amizade é tudo o que eu realmente quero com ela?"
    else:


        "E a [d] é uma mulher bem decidida. Provavelmente ficar só no beijinho é pouco pra ela."

        "Eu preciso jogar ela na cama logo, antes que ela se canse de mim."

    "Só que agora eu tenho que focar no nosso encontro."

    "Tenho que ir na {b}pizzaria durante a noite{/b} e avisar ela."

    "Pra chegar lá, tenho que pegar o busão até o centro da cidade. A pizzaria fica no último bairro saindo daqui."

    "Quero me encontrar com ela o mais cedo possível."

    jump call_cidade

label diana_evento7_pre:











    $ diana_e7 = "pre"

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d7_save", extra_info="d7_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "{i}trr trr{/i}"

    mc "Oi?"

    if diana_namoro:

        d "Oi, querido. Como você tá?"
    else:


        d "[mc]. Como você tá?"

    scene black with dissolve

    scene ape_celular_falando with Dissolve(1.0)

    mc "Oi, Diana! Tô bem. Valeu. Saudades de você."

    d "Eu também. Tudo bem depois daquele dia no clube?"

    if diana_e6 == "barao":

        "Naquela noite eu acabei entrando na conversa do Barão e ele me mostrou aquela sala secreta no bar do Tony."

        "Aquele foi um passo importante pra eu ganhar a amizade desse grupo de poderosos. Se é que esse grupo existe mesmo desse jeito."

        "Mas acabei deixando a Diana de lado..."
    else:


        "Naquela noite o Barão quase atirou em mim."

        "O filho da puta não tava nem aí. Só mirou e tava pronto pra me balear."

        "Eu mantive a cabeça no lugar, pedi desculpa, e a Diana acabou me protegendo."

    menu:
        "Tá tudo certo. E com você?":


            mc "Tô mais preocupado em como as coisas tão aí."

            d "Tá tudo bem... na medida do possível."

        "Tudo bem entre a gente depois que eu conversei com o Barão?" if diana_e6 == "barao":

            d "Foi a coisa mais sensata a fazer. Depois eu fiquei pensando e você foi bem inteligente."

            d "fingir que tá jogando o jogo deles é o mais seguro."

            mc "Verdade..."

            "Eu vou jogar o jogo deles e pular fora ou realmente vou querer me juntar?"

        "Tirando o fato que quase fui peneirado pela carabina daquele fdp..." if diana_e6 != "barao":

            d "Sorte que tudo ficou bem. Peço desculpas por colocar você numa situação como essa."

            mc "Eu te perdoo. E vou te falar, tu não é a primeira a quase me matar num encontro."

            d "Espero que eu seja a sua preferida, então."

            mc "Hehe..."

    mc "E por que você tá ligando? Saudades?"

    d "Quero falar com você. Mas não pelo telefone."

    mc "Parece coisa importante. A gente pode se ver hoje."

    d "Eu ficaria muito agradecida. Você pode vir até o Cassino? Eu... não posso sair, você sabe."

    mc "Aí no território do Barão? Você... acha uma boa?"

    d "Você vai direto pro hotel e sobe no meu quarto."

    d "Só toma cuidado pra não dar bobeira. A gente não quer que ele saiba."

    if diana_e6 == "barao":

        "A Diana não faz ideia que eu tô no mesmo time do Barão... E acho bom não revelar pra ela."

        "Ela não precisa saber nada que aconteceu naquela sala."

        if diana_namoro:

            "Principalmente porque a gente tá namorando..."
    else:


        mc "Eita..."

    menu:
        "Eu passo aí então.":


            pass

    d "Se você puder vir à tarde... porque de noite pode ser que ele precise de mim."

    mc "Ok... sei como é."

    "Não é possível que o Barão realmente trate a Diana dessa forma."

    "Ela é obrigada a fazer o que ele quer. E tá presa nesse castelo que é o cassino."

    d "Espero você então."

    if diana_namoro:

        d "Eu tô pouco mais emocionada que o normal, então não sei se vai dar pra namorar."

        mc "Poxa... tô com saudades de sentir você na cama também."

        d "Não vai insistir... que você já é um adulto."

        mc "Mas e se eu quiser muito?"

        d "Eu vou acabar atendendo você assim. Te vejo daqui a pouco, amor."

        mc "Até, linda."

    d "Tenho medo de falar isso pelo celular e ele ouvir de alguma forma, mas um evento muito grande tá pra acontecer."

    d "Toma cuidado, tá bom?"

    mc "P-pode deixar."





    "Evento muito grande... do que ela tá falando?"

    "Não vai demorar muito pra eu matar a curiosidade. Daqui umas horinhas eu já passo lá."

    "Vou esperar na praça."

    scene black with dissolve

    scene mc parque_sentado with Dissolve(1.0)

    "O Tony, o Barão, o Prefeito, a Natasha... parece que todos eles trabalham juntos."

    "Eles são as sombras que encobrem a capital. Parece que alguém tinha falado desse jeito comigo uma vez."

    "Será que isso realmente é verdade? Será que existe um tipo de 'máfia' que atua nas sombras da cidade?"

    menu:
        "Acho que tá óbvio isso neste ponto":


            "Não tem como negar mais. Tem uma coisa orquestrada acontecendo aqui."
        "Isso aqui não é um filme":


            "Parece meio viajado pensar nisso. Mas que tem muita coisa errada aqui na cidade com certeza tem."

            "Não sei se é algo coordenado, mas em todo lugar que eu olho tem algum esquema terrível."

    "O Gustav com a Pri, a Cidade Chinesa, o Gevanni com a Nona, a Cássia e a Faux, a Blergh! de rolo com o Nathan..."

    "Todos os lugares que eu vou investigar tem maracutaia."

    "Graças a isso eu consegui várias pautas e continuo me mantendo no emprego por um fio."

    "Mas esta cidade... o que aconteceu com ela? Quem começou tudo isso?"

    "E melhor... quem tá no topo disso tudo?"

    scene black with dissolve

    scene cassino portas with Dissolve(1.0)

    "Não dá pra negar que o Cassino é a construção mais fodástica da ilha."

    "Será que o Barão é o 'dono da cidade'? O barão não só do cassino, mas da capital?"

    if diana_e6 == "barao":

        "Sorte que eu resolvi me aliar com ele."

        "Certo ou errado nunca são claros desse jeito. A Cássia me ensinou isso."

        "Eu vou fazer o que eu tiver que fazer pra conquistar meu lugar na mesa."
    else:


        "Droga... será que eu devia ter me aliado com ele?"

        "Mas deixar a Diana nas mãos do filha da puta? De jeito nenhum."

        "O certo é o certo e eu não sou um lixo. Eu vou conquistar meu sucesso de forma limpa."

    "Opa. Olha a hora. Melhor eu ir pra lá falar com ela."

    "Seja lá o que a Diana quer... eu sinto que vai ser um lance cabuloso."

    "O Cassino tá fechado essa hora, então eu preciso ir direto na área do hotel."

    scene black with dissolve

    scene cassino_ponte3 with Dissolve(1.0)

    "Aqui é o lobby que dá nos quartos. Agora só ir no quarto da Diana que eu fui da outra vez."

    if diana_e6 == "barao":

        "Hmm... será que o Barão vai querer saber que eu tô vindo aqui?"

        "A Diana disse que ele não podia saber de jeito nenhum..."

        "Mas eu tô tentando fazer a boa pra ele. E agora?"

        menu:
            "Vou avisar o Barão do encontro com a Diana":


                $ d7_avisa_barao = True

                "Vou ganhar uns pontos com ele. Mostrar lealdade. Sorte que a Ana tá por aqui."

                mc "Ei, Ana. Tudo bem?"

                "Ana" "Olá."

                mc "Tenho uma tarefa importante pra você."

                "Ana" "O-oi? Senhor?"

                mc "Você pode avisar o Barão que eu tô aqui pra falar com a Diana?"

                "Ana" "C-com a senhorita Diana? Tudo bem. Vou pedir pra entregarem sua mensagem pra ele."

                mc "Boa garota. Valeu."
            "Não vou falar nada por enquanto":


                "Deixa quieto. Vamos ver o que a Diana quer."
    else:


        menu:
            "Tomara que o lance da Diana não acabe me ferrando...":


                pass

    scene black with dissolve

    pause 2.0

    play sound som_15_campainha

    mc "Diana?"

    "???" "É você?"

    mc "O-oi? Quem é?"

    scene black with dissolve

    play sound som_porta

    pause 2.0

    scene diana7_img1 with Dissolve(1.0)

    d "Sou eu."

    menu:
        "Ufa. Sua voz tava diferente.":


            pass

    d "É. Tô tentando manter segredo sobre isso. Ninguém sabe que você tá aqui, né?"

    if d7_avisa_barao:

        "Provavelmente a Ana, o Barão e mais algumas pessoas..."

        "Mas não tenho como falar isso pra ela."

    mc "Não. Vim o mais rápido e quase certeza que ninguém conhecido me viu."

    d "Excelente."

    if diana_namoro:

        scene black with dissolve

        scene diana7_img2 with Dissolve(1.0)

        d "Tava com saudades de você, meu homem."

        mc "Achei que a gente não ia ter tempo pra namorar."

        d "Eu menti. Eu quero um pouco de você comigo esta noite."

        mc "Uma diversão... aqui no Cassino?"

        d "Sim... daquela vez não rolou, mas desta vez você é meu."



        d "Vamos tomar um banho comigo?"

        mc "Banho... hmm... na banheira?"

        d "Claro. Tudo do melhor no Cassino do Barão."

        label d7_premium1:

            pass

        menu:
            "Vem. Me mostra onde fica o banheiro.":


                if not premium:

                    call mensagem_premium

                    jump d7_premium1

                d "Tudo pra você, meu amor."

                scene black with dissolve

                scene diana7_premium1 with Dissolve(1.0)

                pause 2.0

                d "Nem acredito que a gente tá aqui numa hora dessas."

                mc "Você parece feliz."

                d "Você é meu pedacinho do céu no inferno."

                mc "E você é muito fofa. E um tantinho dramática como sempre."

                d "Tá na minha alma."

                mc "Essa alma sensível é seu charme."

                d "Não acho... tenho muitas outras coisas pra você que são muito mais charmosas..."

                scene black with dissolve

                scene diana7_premium2 with Dissolve(1.0)

                pause 2.0

                mc "Falando assim... tá me dando vontade de sentir esse charme todo."

                d "E não sentiu várias vezes já?"

                mc "Minha gata é deliciosa demais... eu preciso sentir de novo."

                d "Parece que ser cantora não é meu único talento pro meu homem..."

                mc "Vamos ligar a água?"

                d "Você tá limpinho demais pra tomar banho. Precisa se sujar um pouco."

                mc "Vou começar isso agora mesmo então."

                d "A é?"

                scene black with dissolve

                scene diana7_premium3 with Dissolve(1.0)

                pause 2.0

                d "Ai... é pra eu sentar aqui, é?"

                mc "Pra gente brincar um pouco. Se sujar, sabe..."

                d "Aprendi gostar desse tipo de brincadeira com você."

                mc "Comigo? Mentira... você sempre foi tão confiante, Diana."

                d "São coisas diferentes."

                d "Falando nisso... t-tem outra coisa que eu aprendi a gostar com você."

                mc "Sério? O quê?"

                d "D-deixa pra lá..."

                menu:
                    "Tá bom...":


                        d "Ficou interessado, né?"
                    "Você vai ter que me falar, hein.":


                        d "Vamos ver se você faz eu falar..."

                d "E o que você vai fazer agora, hein, gostoso?"

                mc "Deixa eu ver o que você tá merecendo..."

                menu:
                    "Esfregar o pau nela para provocar":


                        mc "O que você quer que eu faça, hein..."

                        scene black with dissolve

                        scene diana7_premium4 with Dissolve(1.0)

                        pause 2.0

                        d "Onde você tá esfregando isso, hein?"

                        mc "Você tava falando que aprendeu gostar de algo... vai me falar, é..."

                        d "Nnghh... tá judiando da sua garota?"

                        mc "Não..."

                        d "Só tá me dando vontade de sentir ele todo em mim."

                        mc "É o que você quer?"

                        d "É!"
                    "Enfiar de uma vez":


                        mc "Toma aqui, safada!"



                scene diana7_premium5 with vpunch

                d "Ah! Isso!"

                mc "Nngnhhh! Que delícia, Diana!"

                d "Ah... fazia tempo... hmmm... que eu não te sentia assim!"

                mc "Eu também tava com saudades da sua xotinha gostosa."

                d "Hmmm..."

                mc "Tá tão gostoso... assim a gente vai precisar do banho logo logo."

                d "E-eu também vou, safado... aaah..."

                menu:
                    "Sente ele melhor, delícia!":


                        pass

                scene diana7_premium6 with vpunch

                d "Nngnhhh!"

                d "Ah... Adoro como seu pau mne aperta tudo por dentro."

                mc "Se você falar assim você me deixa mais louco ainda!"

                d "Nnnghh! Tô vendo! Aahhnn! Tá metendo gostoso, é!?"

                mc "M-muito!"

                "Se eu continuar nesse ritmo vou acabar gozando!"

                "Por que a Diana é tão gostosa?!"

                d "Aahh! Aaahhnng!"

                mc "Já tá quase lá, é?!"

                d "N-não! Eu quero... eu quero mais... diferente..."

                menu:
                    "O que você quer fazer, hein? Para de segredo e me conta.":


                        pass

                d "T-tenho vergonha... mas... eu..."

                d "Quero sentir atrás..."

                mc "Hmm..."

                scene black with dissolve

                scene diana7_premium7 with Dissolve(1.0)

                pause 2.0

                mc "Era isso que você tava com vergonha?"

                d "S-sim... aah..."

                d "Essa boca no meu..."

                mc "Sim... vou preparar esse rabinho pro meu caralho."

                d "Aahh... desde aquele dia... aahnn... não consigo tirar isso da cabeça."

                d "Achei que fosse doer, ia ser horrível... mas eu senti tão gostoso..."

                mc "Sorte a nossa, safada."

                d "Aahhnnn... essa língua... só de pensar no seu... negócio entrando de novo... aah..."

                mc "Hmmm... você tá pronta."

                d "Tô... vem..."

                scene black with dissolve

                scene diana7_premium8 with Dissolve(1.0)

                pause 2.0

                mc "Vou enfiar."

                d "Vai com calma... aah..."

                mc "Do jeitinho que você gosta. Judiando desse cuzinho tarado."

                d "D-danado... hmmm..."

                d "Essa pressão... aaahhh..."

                mc "E eu deixei ele todo molhadinho, amor."

                d "Isso... hmmm..."

                scene black with dissolve

                scene diana7_premium9 with Dissolve(1.0)

                pause 2.0

                mc "Hmm... tá dentro, delícia."

                "Que delícia esse cuzinho apertado da Diana!"

                d "Hmmmm... tô sentindo, tesão. Pode mexer."

                mc "Toma, gata!"

                d "Aahh... hmmm..."

                d "Mete mais forte no rabinho do seu amor!"

                mc "Meto! Aahn!"

                d "Aahhnnn! Do jeito que ela gosta! Aainnn!"

                mc "Assim mesmo!"

                menu:
                    "Vou meter mais forte nesse buraquinho gostoso!":


                        pass



                scene diana7_premium10 with hpunch

                pause 2.0

                d "AAAHH!"

                mc "Tá gostoso, tá?!"

                d "Aainn! Delícia! Tá muito gostoso!"

                mc "Então vai, geme pra mim! Nngh!"

                d "Hmmnnhgg! Aaaiinnn!"

                mc "Vou gozar!"

                d "Eu que vou! Vou gozar pelo cu, amor! Aainn!"

                d "Tava com tanta vontade assim!"

                mc "Goza pra mim!"

                d "Aainnnn!"



                scene diana7_premium11 with hpunch

                pause 2.0

                d "Carambaaa! Aaainn, paixãããooo!"

                mc "Tô gozando também, amor! Aahhh!"

                mc "Vou te encher de porra! AAAAHHH!"

                d "AAAINN!"

                scene diana7_premium11 with hpunch

                mc "TOOMMAAA!!!"

                d "NNghhh!"

                scene black with dissolve

                scene diana7_premium12 with Dissolve(1.0)

                pause 2.0

                mc "Aahh... ahhh..."

                d "Hmmm... tô sentindo..."

                mc "Caramba... te enchi de leitinho..."

                d "Me encheu de tudo... de amor, de paixão..."

                d "Agora sim a gente merece um banho."

                mc "Opa."

                scene black with dissolve

                scene diana7_premium13 with Dissolve(1.0)

                pause 2.0

                d "Eu queria poder ficar assim pra sempre com você."

                d "Mas enquanto eu tiver aqui... esse futuro não existe pra gente."

                menu:
                    "Eu vou fazer dar certo. Você vai ver.":


                        d "Eu queria que fosse fácil assim."
                    "Vamos aproveitar enquanto temos tempo.":


                        d "Que já acabou..."

                mc "Então eu vou te ajudar! Me fala o que você tá pensando!"

                d "E-eu..."

                d "Deixa eu aproveitar você mais um pouco. E depois a gente conversa, tudo bem, lindo?"

                mc "Sim... eu também quero mais carinho na banheira."

                d "Fofo..."

                scene black with dissolve

                pause 2.0

                scene quarto_paris geral with Dissolve(1.0)

                mc "Nem acredito que a gente fez isso... assim..."

                d "Um momento do céu no inferno... voltar pra este quarto me lembra do que vai acontecer."

                mc "Diana... eu tô com você."
            "A gente pode fazer isso depois que resolver os problemas.":


                d "Que homem sério..."

                mc "É triste... mas é melhor."

                d "Eu sei... você é muito mais racional que eu."

        menu:
            "O que você precisava falar pra mim?":


                pass
    else:


        menu:
            "Antes do rolo, vamos curtir?":


                scene diana7_img2 with hpunch

                mc "Tô afim de você."

                d "Q-que que é isso, [mc]?"

                mc "Você, assim... vamos curtir um pouquinho?"



                d "Desde quando você tem esse interesse em mim? Devia ter colocado um anel se era essa sua ideia."

                mc "Poxa..."

                d "Nada de poxa, homem."

                "Talvez se a gente tivesse namorando ela aceitasse fazer um lance gostoso comigo agora... merda."
            "O que você precisava falar pra mim?":


                pass

    mc "Vamos pro assunto... o que tá rolando?"

    d "Deixa eu me ajeitar. Senta comigo."

    play sound som_roupas

    scene black with dissolve

    scene diana7_img3 with Dissolve(1.0)

    d "Esses dias eu tava lembrando de quando a gente se conheceu na praia."

    menu:
        "Quando eu tropecei em você tomando sol...":


            pass

    d "Era o destino. Os céus queriam unir nossas vidas de alguma forma."

    "Talvez fosse só eu sendo tarado, mas tudo bem..."

    d "Eu tinha visto seu nome na revista algumas vezes e pedi pra você entregar uma pauta."

    mc "Sim... sobre sua música, né?"

    d "É. Você lembra quando eu apresentei ela pra você no Cassino?"

    mc "Com certeza. Foi incrível, [d]. Ela tinha uma emoção diferente."

    d "Eu coloquei toda minha alma naquela música. Era uma história que me tocava de forma diferente."

    d "Aquela letra era tão real que eu podia sentí-la nas minhas mãos, como um diamante."

    mc "Só que... teve aquele lance com o Barão, né?"

    d "Sim... ele não permitiu que eu tocasse ela. Meu diamante se desfez como pó e escorreu pelos meus dedos."

    d "O mundo... nunca saberia quem era a verdadeira Diana, a jóia do Cassino do Barão."

    "Isso era tão importante pra Diana... eu vejo como ela tá triste."

    menu:
        "Você não pode desistir. Precisa mostrar pras pessoas quem é você.":


            mc "Nunca é tarde demais!"

            scene black with dissolve

            scene diana7_img4 with Dissolve(1.0)

            d "Esse é o [mc] que eu conheço. Um coração maior do que cabe no peito."

            if diana_namoro:

                d "Foi isso que fez eu me apaixonar perdidamente por você."

                mc "Verdade?"

            mc "Porque eu só tô falando a verdade. Nunca é tarde!"

            d "Eu queria ter esse seu otimismo."
        "Tem forças que são maiores do que nós. Não podemos ir contra.":


            scene black with dissolve

            scene diana7_img4 with Dissolve(1.0)

            d "Eles realmente tiraram seu espírito também?"

            mc "Eu quero ter uma boa vida pra mim. E às vezes a forma de atingir isso é respeitando a ordem das coisas."

            d "Exatamente..."

    d "O que parece pra mim é que certas pessoas têm todo o poder e outras só podem seguir o caminho que as primeiras decidiram."

    d "Dinheiro, influência, poder... quem tem pode viver. Aos outros, só resta jogar com as cartas que já foram colocadas na mesa."

    mc "Não gosto de ver você desanimada assim."

    d "Eu não estou desanimada. Apenas... reflexiva."

    mc "O que você pretende fazer então?"

    d "Eu tenho uma última carta guardada."

    mc "Então você não desistiu mesmo? Vai contra o Barão?"

    d "Se isso não funcionar, eu vou ser a escrava que ele sempre sonhou. Vou aceitar meu destino."

    d "Mas... se meu plano funcionar... bom... ai, ai..."

    menu:
        "Que foi, Diana? Tá pensando em desistir?":


            pass

    d "Talvez eu já tenha desistido..."

    d "Mas eu queria tentar uma última vez. O que você acha, [mc]?"

    mc "O que eu acho? Sobre o quê?"

    scene black with dissolve

    scene diana7_img6 with Dissolve(1.0)

    d "Eu tenho aqui dois envelopes. Um foi eu que escrevi."

    d "Tem tudo o que eu pensei, algo que eu venho matutando desde antes de nós nos encontrarmos na praia."

    d "O outro foi escrito pelo Barão."

    menu:
        "O que que tem nesses envelopes?":


            d "Os dois guardam uma pauta dentro. Pautas com os meus desejos ou os desejos do meu senhor."

            d "Apenas um desses desejos vai chegar na sua revista."
        "O que eu faço com eles?":


            d "Você vai levar um deles pra sua revista. Agora... qual?"

    mc "E-eu que vou escolher?"

    d "Sim. Quero que você me diga."

    d "Eu deveria aceitar meu destino e viver aqui, como uma rainha cativa em seu castelo?"

    d "Ou eu devo ser uma princesa guerreira, que desiste de tudo para viver livre?"

    d "Nenhuma das escolhas parece perfeita."

    d "Desde o começo eu te disse que confio na sua sensibilidade. No seu sexto sentido."

    d "Disse também que carregar o peso de todos nas suas costas pode te trazer problemas."

    d "Agora é minha vez de colocar o meu peso nas suas costas."

    if diana_namoro:

        d "Mais do que ajudar sua namorada. De olhar pra fecilidade dela."

    scene black with dissolve

    scene diana7_img5 with Dissolve(1.0)

    d "Quero que você pense em mim como uma pessoa, como um ser humano."

    d "Eu devo ir contra tudo o que me aprisiona e provavelmente acabar sem nada, talvez sem a vida, ou aceitar o que o destino me deu?"

    menu:
        "Mas eu que vou decidir algo assim importante pra você? E também... como eu fico?":


            pass

    d "Sei que não é fácil. Isso terá consequências pra você também. E por isso só posso pedir pra você."

    d "Não posso tomar esta decisão sozinha. Eu tentei. Fiz tudo o que podia."

    d "Eu não queria te colocar nesse lugar, mas é minha última saída. VOCÊ é minha saída agora, [mc]."

    mc "[d]..."

    scene black with dissolve

    scene diana7_img6 with Dissolve(1.0)

    "Essa não é uma pergunta fácil... mas ela realmente precisa de mim."

    "Isso pode mudar a vida da Diana pra sempre. E até a minha. Claro que terão consequências."

    if diana_e6 == "barao":

        "Eu decidi ficar do lado do Barão, então talvez o melhor seja seguir o plano dele."

        "Dissuadir ela de fazer uma cagada e bagunçar o coreto."
    else:


        "Eu não tô do lado do Barão. Eu tô com a Diana."

        "Mas desafiar ele... e perder tudo numa luta contra um cara poderoso desses... vale a pena?"

    if diana_namoro:

        "Com certeza o que eu decidir aqui vai afetar nosso namoro também."

        "Se eu quero ficar com ela, acho que é bem óbvio o caminho que eu tenho que seguir. Mas quais serão as consequências?"

    "[mc]... o que você vai fazer? O que você vai escolher neste momento crítico?"

    menu:
        "Me dá o envelope que você escreveu.":


            $ d7_envelope = 1

            mc "Claro que eu vou querer seu envelope. A gente não vai desistir."

            d "Tem certeza?"

            mc "Totalmente."

            scene black with dissolve

            scene diana7_img7 with Dissolve(1.0)

            d "Então a gente não vai desistir ainda. Meu plano vai continuar."

            mc "Do que depender de mim, você pode apostar que vai."

            mc "Eu não sei o que tá passando nessa cabeça aí, com certeza é uma coisa bem complicada."

            mc "Mas eu quero que você continue com ele em mente."

            d "Mesmo... que não seja o que você tá esperando?"

            menu:
                "Eu te apoio de qualquer jeito.":


                    d "Obrigada pela confiança."
                "O q-que você tá pensando?":


                    d "Desculpa, mas não posso contar. Você vai ter que confiar em mim."

                    mc "Diana..."

                    "O que ela tá pensando?"

            mc "Então é só levar pra redação esse envelope?"
        "Me dá o envelope que o Barão escreveu.":


            $ d7_envelope = 2

            mc "Não vamos arriscar."

            d "Então desisto de tudo mesmo..."

            mc "Se você quer saber minha opinião, é essa."

            scene black with dissolve

            scene diana7_img8 with Dissolve(1.0)

            d "É o que eu quero... pelo menos é o que eu acho que eu quero."

            mc "Não se arrisca, Diana. As coisas não vão ser tão ruins assim."

            d "É... era essa a conclusão que eu tinha chegado sozinha."

            d "Tudo bem..."
        "Vamos apostar na sorte. Que a Lady Luck decida.":


            $ d7_envelope = 3

            d "C-como?"

            mc "Heh... situações loucas exigem medidas mais loucas ainda."

            d "Não tô entendendo o que você quer dizer."

            mc "Você não consegue decidir. Nem eu."

            mc "Vamos deixar pra sorte. Que o acaso decida nosso destino."

            d "Você... tá falando sério?!"

            mc "Vamos embaralhar os envelopes e decidir que a Fortuna decida como tudo vai acabar."

            d "Isso é loucura... mas... se sua intuição diz isso, eu decido apostar nela."



            scene black with dissolve

            scene diana7_img9 with Dissolve(1.0)

            mc "Eu não sei qual é qual."

            d "E agora?"

            menu:
                "Pegar o envelope da esquerda":


                    pass
                "Pegar o envelope da direita":


                    pass

            mc "É este. Que ela esteja do nosso lado."

            d "De todos os cenários que eu envisionei pra este momento, nunca acontecia deste jeito."

            d "Sem dúvida, você é um sujeito diferente, [mc]."

    d "Entregue para o seu chefe. E vamos esperar o dia do show."

    mc "Então vai rolar um show mesmo..."

    d "Vai ser o show de uma nova era. Ah!"

    if diana_namoro:

        d "Independente de como nosso futuro juntos vai se desenvolver..."

        mc "Não fala assim. A gente vai ficar juntos."

        d "É o meu desejo, amor. Só que..."

    scene black with dissolve

    scene diana7_img10 with Dissolve(1.0)

    d "Indpendente dos nossos sentimentos, eu gostaria de te agradecer."

    d "Mas não aqui. Eu quero dizer 'obrigada' durante o show. Pra que todo mundo saiba."

    mc "C-como é?!"

    d "Teria problema pra você? Eu falar seu nome para todos os presentes?"

    mc "[d]... eu não sei se eu mereço uma honraria dessas. De verdade."

    mc "Você é a artista. É sua voz, sua interpretação. Eu não fiz nada."

    d "Eu sei que esse é seu jeito, [mc]. Você sempre acha que não fez nada."

    d "Não enxerga como muda a vida das pessoas que passam pelo seu caminho de forma irremediável."

    menu:
        "Eu mudei sua vida dessa forma?":


            pass

    d "Mudou. E ainda vai mudar."

    if diana_namoro:

        mc "Tenho certeza. Quando a gente finalmente puder ficar juntos de verdade. Sem esses problemas."

        d "Você tá descrevendo meu sonho."

        d "Mas não é apenas essa mudança."

    d "Vai mudar tudo de muitas formas."

    d "Talvez eu também tenha um sexto sentido. E eu sinto que você tem um potencial muito grande."

    d "Uma energia que atrai acontecimentos na sua vida. Uma espécie de... poder oculto, uma característica do espírito."

    menu:
        "Hmm... me explica melhor isso aí.":


            d "Não tem o que explicar. É mais sentir. Note como as coisas vão acontecendo na sua vida."

            mc "Você diz... como eu me meto em furada? Ah! Isso com certeza!"

            d "O destino às vezes é assim. Ele tem muitas curvas, subidas e descidas, mas ele chega no fim de um jeito ou de outro."
        "Desculpa, mas não acredito nessa história de 'oculto'.":


            d "O oculto não precisa da sua sanção para existir."

            d "Você acreditando ou não ele vai agir na sua vida. Se você vai perceber ele ou não, essa é sua escolha."

    mc "Tá falando igual uma verdadeira maga."

    scene black with dissolve

    scene diana7_img11 with Dissolve(1.0)

    d "Haha... pode ser. Posso tá exagerando um pouco. Mas é o momento, sabe?"

    mc "Claro... esse momento vai definir tudo pelo jeito."

    d "Tudo e mais um pouco. Mas você não me respondeu ainda. Posso te agradecer pra todo mundo? Eu adoraria."

    "Agradecer... ela vai falar pra todo mundo que eu tô nesse rolo."

    "O Barão vai saber mais quem vai ouvir o que tá rolando..."

    "Ela quer me agradecer. Pra Diana isso vai ser algo muito importante."

    "Mas será que é uma boa pra mim? Um pouco de fama não faz mal certo? Ou faz? Merda... e agora?"

    menu:
        "Eu ficaria muito feliz com seu agradecimento.":


            $ d7_agradece = True

            d "Que bom. Então todo mundo vai saber o que você fez por mim."

            mc "Ok! Eu fico muito agradecido."
        "Prefiro que você não fale nada. Você agradece aqui.":


            d "Desde quando você é tímido assim?"

            mc "Haha..."

            "Eu que não quero meu nome disso tudo. Perigoso demais."

    mc "Então entrego a pauta pro chefe e daí vemos o que acontece."

    d "Não queria... mas sinto que este vai ser meu último show, [mc]."

    mc "Vira essa boca pra lá, [d]."

    d "Não fique preocupado. Você fez tudo o que você podia."

    d "As coisas vão acontecer como têm que acontecer."

    mc "..."

    mc "Vou lá então."

    d "Tudo bem. Vamos nos ver em breve."

    if diana_namoro:

        d "[mc]... olha..."

        scene black with dissolve

        scene diana7_img12 with Dissolve(1.0)

        d "Será que tem uma chance pra gente? Pra gente viver nosso amor?"

        mc "A-ah... Diana... como você é perfeita..."

        d "Se tivesse uma oportunidade... um final feliz pra esta história, queria que fosse ao seu lado."

        mc "Com certeza, gata. Me escuta."

        mc "Quando tudo isso acabar, eu vou querer namorar muito com você."

        mc "Você é a mulher mais deliciosa que eu tive na vida. E não quero perder mais um segundo contigo."

        d "Eu vou ser sua. Do jeito que você merece, meu amor."

        mc "Me espera. Vai dar tudo certo."

        d "Vai, sim."

    d "Beijos."

    mc "Beijos..."

    scene black with dissolve

    scene cidade regiao2_noite with Dissolve(1.0)

    "Como que isso vai acabar?"

    if d7_envelope == 1:

        "Eu vou ajudar a Diana entregando pro chefe a pauta que ela escreveu."

        "O que será que ela tá tramando? Será que ela vai mesmo contra o Barão?"

        "A Diana é uma mulher forte. Ela parecia meio pra baixo, mas sei que ela não vai desistir."

        "Vou fazer minha parte e esperar que tudo acabe bem."

    "Vou {b}passar na redação e entregar a pauta pro chefe{/b}."

    "E ver o que vai sair disso tudo."

    "O meu destino, o destino da Diana e até da capital... eu acho que este é o momento mais crucial que eu já vivi aqui na ilha."

    "Eu PRECISO ver como isso acaba."

    $ tempo = 4

    jump call_cidade

label diana_evento7:

    $ estou_na_cidade = False

    $ diana_e7 = "evento"

    $ cassino_roupa = "blacktie"

    mc "Vou pegar meu black tie, deixar tudo no esquema e esperar o dia do show dela."

    "Diana... o que que vai acontecer?"

    if diana_namoro:

        "Desde que a gente começou a namorar, eu quero que você se livre desse destino de escravidão."

        "Eu quero que você seja feliz. E eu quero que seja do meu lado. Quero ser feliz com você."

    "O chefe não me disse quem que tanto vai tá nesse evento, mas parece que é gente graúda."

    "Do jeito que o Barão é, aposto que vai ter gente daquele grupo lá."

    "Eu tenho que tá pronto pro pior."

    scene black with Dissolve(1.0)

    "{b}Alguns dias depois{/b}"

    scene black with Dissolve(1.0)

    scene ape_chuveiro with Dissolve(1.0)

    "Chegou o grande dia."

    "Não consegui falar com a Diana desde a última vez lá no quarto dela."

    if d7_envelope == 1:

        "Se ela tá aprontando alguma com aquele envelope, agora eu faço parte disso também."

        "Eu entreguei a pauta dela pro chefe. E tudo isso deve fazer parte do plano dela."

    elif d7_envelope == 2:

        "Eu decidi entregar o envelope do Barão, então ela não deve tá planejando nada."

        "Ele vai gostar de saber que eu ajudei a parar as loucuras da Diana."
    else:


        "Eu deixei a história do envelope nas mãos de Deus."

        "O que vai sair disso aí... eu nem sei de qual dos dois lados tudo vai acontecer."

        "Que a sorte esteja do nosso lado."

    scene black with dissolve

    scene cassino_ponte2 with Dissolve(1.0)

    "Muito foda ver que eu tô trajado como o pessoal mais chique daqui."

    "Devo tá parecendo um milionário."

    mc "Com licença, vallet, por favor estacione minha Ferrari. Tome aqui C$ 200 de gorjeta."

    "Pff... quem vê, pensa."

    menu:
        "O show deve ser no Jazz Corner. É o único palco exclusivo que tem aqui.":


            pass

    mc "Só deixa eu en-"

    show ana c_ola with dissolve

    ana "Com licença, senhor."

    mc "Oi, Ana."

    ana "Oi... peço desculpas, senhor, mas hoje o Jazz Corner está fechado para um evento especial."

    menu:
        "Eu fui convidado. Pode olhar na lista. Meu nome é [mcc].":


            pass

    ana "Hmm..."

    ana "Tem razão, senhor. Me perdoe."

    menu:
        "Tudo bem. Você tá perdoada. Mas só porque é linda.":


            ana "Ai, senhor... eu não mereço toda essa gentileza."

            mc "Claro que merece. Olha pra esse rostinho perfeito."
        "Tem gente muito chique aí, Ana?":


            ana "Os convidados ainda estão chegando, mas o senhor Barão já está aqui."

            mc "Ah. Ele já chegou..."

            ana "Sim. E outras personalidades de renome aqui na capital."

            mc "Valeu."

    mc "Agora deixa eu entrar. Que logo logo já deve começar, né?"

    show ana c_preocupada with dissolve

    ana "Sim. M-mas, [mc]... posso te falar uma coisa? Sem querer me intrometer, claro."

    menu:
        "Agora não tenho tempo. A gente se fala depois do evento.":


            ana "Tudo bem... aproveite a festa, senhor."
        "Claro. Que que foi?":


            "Acho que eu posso perder um tempinho falando com ela."

            ana "Você me parece ser um homem direito. Assim, uma pessoa bacana."

            mc "Valeu, [ana]..."

            ana "Eu já vi o que o Barão e... esses convidados podem fazer."

            ana "Você e eles... não parecem do mesmo lugar, sabe?"

            ana "N-não quero ser intrometida! Só queria te falar isso..."

            ana "Essas pessoas podem ter dinheiro, ter poder, mas elas são... você sabe..."

            ana "D-desculpa."

            menu:
                "Eu entendo... mas eu ainda vou fazer parte deste grupo também.":


                    ana "Ah! Ok..."

                    mc "Algumas pessoas podem ter medo desse mundo, mas ninguém deixa de ser humano por causa do poder."

                    mc "E eu quero fazer parte do topo. Então..."
                "Eu nunca vou ser igual a essas pessoas.":


                    mc "Eu sei do que você tá falando. E meu interior nunca vai ser igual eles."

                    mc "Eu prefiro morrer, acabar sem nada, do que me corromper dessa forma."

                    ana "Eu fico feliz de ouvir isso..."

                    mc "A gente conversa mais outro dia, tá? Fica bem."

                    "A Ana, que trabalha pro Barão, sabe melhor que eu como esse povo não presta."

    mc "Até mais."

    ana "A-até..."

    scene black with dissolve

    scene jazz_corner_novo with Dissolve(1.0)

    "Tô aqui. Tem umas pessoas, mas não sei se reconheço alguém."

    "Talvez procurar a Diana e ver como tão as coisas com ela... ou falar com o Barão..."

    "O chefe também quer que eu descubra algum furo antes da FAUX. Não posso esquecer isso."

    "Eu posso abordar essa festa de várias formas. E agora?"

    menu:
        "Tenho que achar a Diana.":


            $ renpy.block_rollback()

            "Acho que vou falar com a Diana. Ver se consigo descobrir alguma coisa."

            "???" "[mc]!"

            mc "Barão!"

            ba "Garoto! Vem cá!"
        "Vou falar com o Barão.":


            $ renpy.block_rollback()

            mc "Ah! Acho que tô vendo ele ali."

            mc "Oi, Barão."
        "Vou procurar outras pessoas que eu conheço":


            $ renpy.block_rollback()

            "Será que alguma celebridade que eu conheço veio?"

            "???" "[mc]!"

            mc "Barão!"

            ba "Garoto! Vem cá!"

    scene black with dissolve

    scene diana7_img13 with Dissolve(1.0)

    ba "Como você tá? Aproveitando a noite?"

    mc "Acabei de chegar. Ainda tô dando uma olhada em tudo. Nem bebi ainda."

    ba "Haha! Que anfitrião eu seria se deixasse meu amigo de boca seca?"

    ba "EI! GAROTA! Traz algo bom aqui pro [mc]! E vai logo!"

    "???" "S-sim, senhor!"

    ba "Aposto que você não achou que eu ia te chamar, né?"

    mc "Sendo sincero... parece uma festa meio fora da minha realidade."

    ba "Deixa disso!"

    if diana_e6 == "barao":

        ba "Depois que você prometeu pra mim lá no bar que ia deixar a Diana em paz e ficaria do meu lado, nós somos parceiros."

        ba "A gente não pode deixar mulher entrar no meio de amizade de verdade. Amizade entre homens, entende?"

        mc "Claro."

        ba "Disso que tô falando!"
    else:


        ba "Mesmo você dando uma de zé mané aquela noite no bar, eu não podia deixar de te chamar."

        "Até parece que eu ia deixar a Diana, idiota..."

        mc "Por quê?"

    ba "Você foi fundamental pra isso aqui."

    ba "Sem você, esta festança não estaria acontecendo, [mc]!"

    menu:
        "Eu? Tá me zoando agora? Eu não tive nada a ver com isso.":


            pass

    scene black with dissolve

    scene diana7_img14 with Dissolve(1.0)

    ba "Você teve TUDO a ver com isso."

    ba "Sua revista e suas pautas que transformaram a Diana no fenômeno que ela é hoje."

    ba "Que a garota tem talento isso ninguém vai negar. Além de um corpinho delicioso."

    ba "Mas foi sua revista que fez todo mundo querer vir assistir a performance dela."

    menu:
        "Eu sempre quis ajudar o Cassino. E você, Barão.":


            ba "Você sabe onde o poder da cidade está. E você não quer perder um pedaço, certo?"

            mc "Eu sou um cara humilde. Quero seguir as ordens de quem manda."

            ba "Tô gostando bastante desse paparazzo que tô vendo hoje."
        "Não sabia disso. Só fiz o que a Diana me pediu.":


            ba "Você tem essa síndrome de herói, né?"

            ba "Mas saiba que desde o começo tudo tava dentro dos meus planos."

            ba "A própria Diana... daquele jeito rebelde dela... ela sempre soube o lugar dela."

            ba "E ela sempre fez o que eu queria."

            "Não é possível que as pautas, minha ajuda... acabou favorecendo esse desgramado."

    if diana_e6 == "barao":

        ba "E no nosso último encontro, quando eu te levei pra 'sala da verdade'. Ali nós fechamos nosso acordo."

        ba "Eu vi verdade no que você disse."

        mc "Que eu realmente queria fazer parte do grupo."

        ba "Exatamente."
    else:


        ba "Mesmo você fazendo graça lá com a Diana no bar do Tony, sua ajuda foi fundamental."

        ba "Tu sabe qual é seu lugar nisso tudo."

        "Mesmo eu não tendo desafiado ele desde o começo... ele fala desse jeito, amigável."

        "Qual é a desse cara? Ele me acha tanto um zé ninguém que eu nem mereço a preocupação dele?"

        "Ou ele tá tentando me convencer a ser um dos aliados dele?"

    ba "Por isso sua presença era essencial aqui hoje."

    ba "Vamos brindar ao [mc]!"

    ba "E antes de eu te apresentar a algumas pessoas, queria confirmar algo contigo."

    ba "A Diana parece mais resignada com a situação dela esses últimos tempos."

    ba "A rebeldia da rapariga finalmente acabou."

    menu:
        "Vai ser melhor pra todo mundo se ela só obedecer.":


            pass
        "Se eu fosse você tomava cuidado. Pode tá quieto demais.":


            pass

    if d7_avisa_barao:





        mc "Lembra que eu tive aqui uns dias atrás? Eu pedi pra Ana te avisar."

        ba "Sim. Chegou até mim. Então ela tava aprontando alguma mesmo."

        mc "Estava."

        menu:
            "Mas ela parecia meio sem vontade. Nem sei se ela vai fazer algo.":


                pass

        ba "É o que eu tô vendo também. Finalmente ela pode ter sossegado."

    ba "Olha, [mc]! Tem gente chegando aí!"

    if sayuri_final3:

        scene black with dissolve

        scene diana7_img15 with Dissolve(1.0)

        ba "Senhorita, Ai Fen. A nova Mestra da Cidade Chinesa. Seja bem-vinda."

        s "Agradecida pelo convite, Barão."

        mc "S-sayuri?!"

        s "Eu tenho compromissos no bairro, então não pretendo ficar muito, mas não podia deixar de prestigiar seu convite."

        ba "Eu entendo perfeitamente, Mestra. E como tão indo as coisas lá?"

        s "Perfeitas. O senhor está convidado para nos visitar."

        ba "Vou fazer isso! Fiquei sabendo que você é muito mais eficiente que a sua predecessora Jidao."

        s "Muitas coisas estão mudando na Cidade Chinesa."

        ba "É o que o Tony me disse. Seus punhos podem não ter o peso da Jidao, mas são mais eficientes e ágeis."

        s "A antiga mestra deveria saber que peso demais compromete. Muitas vezes só precisamos fluir como um rio."

        ba "Com certeza vocês orientais têm grandes metáforas."

        menu:
            "Oi, Sayuri...":


                mc "Tudo bem?"

                s "A-ah... [mc]... estou bem. E você?"

                mc "Também. Saudades de você."

                scene black with dissolve

                scene diana7_img16 with Dissolve(1.0)

                s "Você foi peça importante para toda estas transformações que estão acontecendo na Cidade Chinesa."

                s "Sempre... será bem-vindo em nossa cidade. Por tudo... o que aconteceu entre a ge... digo... por tudo o que você fez."

                ba "Hmm... tô sentindo uma tensão sexual aqui?"

                s "Senhor, Barão!"

                ba "C-com todo o respeito, claro."

                menu:
                    "Eu quis que a Sayuri fosse a nova Mestra. Achei que ela faria um trabalho melhor.":


                        pass

                ba "Não sabia que você tava envolvido dessa forma com os chineses, garoto."

                s "É verdade, Barão. O [mc] garantiu que as coisas pudessem continuar como estavam, sem uma ruptura total."

                s "Não fosse por ele... eu nunca teria a força necessária para assumir as rédeas do meu destino e assumir o posto que sempre foi meu."

                mc "[s]... você realmente é uma mulher incrível."

                s "O-obrigada... mas terminei o que tinha pra falar."

                s "V-vou me sentar."
            "...":


                "Essa é a nova Sayuri? Ou melhor... Ai Fen."

                s "Foi um prazer ver vocês. Vou me sentar."

                scene black with dissolve

                scene diana7_img16 with Dissolve(1.0)

        ba "Ai Fen... espero que nossa relação continue tão frutífera quanto foi com a mestra Jidao."

        s "Não poderia ser diferente, Barão."

        mc "!"

        s "Nossa parceria é fundamental para o bem-estar da Capital."

        s "Assim como nossos antepassados dividiram a cidade entre chineses e italianos na fundação, vamos continuar progredindo, juntos."

        ba "Concordo totalmente. É nossa responsabilidade manter a cidade funcionando."

        s "Certas coisas são mais importantes do que nós. Começaram antes e terminarão depois. É nossa responsabilidade manter o fluxo como os escolhidos da vez."

        ba "Uma última coisa... e sobre a sacerdotisa?"

        s "Melhor falarmos sobre isso em sua visita."

        "Sacerdotisa?"

        if sacerdotisas >= 2:

            "Eu falei sobre elas com a Carol."

            "Aquelas três garotas orientais que tavam na foto que eu achei na pasta do Gevanni."

            "Eles também se referiam a elas como 'sacerdotisas'."

            "Será que essa merda é mais importante do que eu tô dando moral?"

        ba "Entendido. E aproveite a festa, Mestra."

        s "Agradecida. Até mais, rapazes."

        scene black with dissolve

        scene diana7_img14 with Dissolve(1.0)

        menu:
            "Então a Sayuri também está com o grupo.":


                pass

        ba "A Mestra Ai Fen."

        mc "D-desculpe."

        ba "Todos aqui têm um ego maior do que você imagina, [mc]. Aprenda a se dirigir a todos como deve."

        ba "Eu acho isso uma grande merda, mas fazer política é essencial pra todos."

        "Sayuri... então você tá com eles?"

        "Será que eu devia ter tirado ela e a Jidao da Cidade Chinesa?"

        ba "Falando em política."

    mc "A-ah..."

    scene black with dissolve

    scene diana7_img17 with Dissolve(1.0)

    pause 2.0

    ba "Senhor, prefeito! Não acredito que o senhor realmente está aqui!"

    pr "Contenha-se, Marcos."

    ba "Você sabe que aqui eu sou Barão. Para um político profissional, você esqueceu a política em casa."

    pr "Perdão, Barão. Estou um tanto desconfortável de estar aqui."

    ba "Não pensei que o maior cassino do país não atenderia seus elevados padrões, Basílio."

    pr "Não seja bobo. Não fica bem para um prefeito estar em um cassino. Se tiver um paparazzo aqui, isso pode ser um problema."

    menu:
        "E-epa... será que ele tá falando de mim?":


            pass

    na "Não tema, senhor. Eu fiz questão de garantir que temos apenas amigos."

    pr "Só você mesmo para me deixar em paz, Natasha. Eu confio na sua eficiência."

    ba "Viu só? Você se preocupa demais. Além da FAUX, apenas nosso garoto [mc] tá aqui."

    pr "O garoto da revista, [mcc]."

    menu:
        "É uma honra, prefeito.":


            pr "Honra? Não exagere, jovem."

            ba "Ele sabe com quem está falando."

            pr "Será que sabe? Isso é preocupante."
        "Boa noite.":


            pr "..."

    pr "O Tony não vê esse garoto com bons olhos."

    na "O Barão garantiu pessoalmente que o senhor [mc] não vai causar problemas."

    ba "Tá vendo, garoto? Tô colocando minha mão por você."

    mc "Obrigado..."

    na "Além de que o [mc] é um dos pupilos da Cássia. Ela está de olho nele."

    pr "Hmm..."

    "O que eu tô fazendo aqui? Eu me sinto um peixe beta no meio de tubarões."

    "Se eu relaxar um pouco minha perna ela vai começar a tremer igual uma vara verde."

    pr "Você sabe que eu nunca faria a desfeita de perder o seu show, amigo, mas você deve agradar a Natasha aqui."

    pr "Não fosse a insistência dela, provavelmente eu teria ficado te devendo."

    ba "Natasha... sei muito bem..."

    na "..."

    pr "Enfim..."

    scene black with dissolve

    scene diana7_img18 with Dissolve(1.0)

    if not sayuri_final3:

        pr "Por que a mesa reservada para a mestra da Cidade Chinesa está vazia?"

        pr "Espero que ela esteja chegando... não podemos perder nossa mão no maior bairro da cidade."

        ba "Bem... sendo sincero... ainda não sei quem está no comando lá."

        pr "O que você quer dizer com isso?"

        "M-merda! Tô fodido! Eu acabei com o reinado da Jidao e chutei ela do poder!"

        "E tirei a própria Sayuri também... s-se eles descobrirem..."

        menu:
            "S-senhor... eu vou me sentar.":


                ba "Espere. Tem mais pessoas que você deve conhecer."

                pr "Então?"
            "Vou rezar pra eles não me matarem.":


                pass

        "Puta que pariu..."

        na "Senhor, eu lhe escrevi um memorando. Houve uma espécie de coup d'état na Cidade Chinesa."

        na "Não temos informações exatas, mas parece que duas seguidoras se aliaram a um agente externo..."

        pr "Ah... tem razão. Precisamos de alguém lá imediatamente. Cuide disso, [na]."

        na "Sim, senhor."

        pr "Entre em contato com a mestra Jidao. Ela vai nos explicar o que aconteceu."

        "Parece que eles ainda não sabem que EU sou o 'agente externo'."

        "Mas se a Jidao contar..."

        pr "Vamos cuidar para que esses rebeldes sofram as consequências de seus atos."

        "Morri."
    else:


        pr "Estou vendo a substituta da Jidao sentada ali. O que você achou dela?"

        ba "Ela pode ser uma mulher maus suave que a velha, mas vem da mesma linha."

        ba "Mesmo sendo uma mulher... eu não teria coragem de brincar com ela."

        pr "Eu não me importo com seu machismo, Barão. Você sabe o que eu estou perguntando."

        ba "Não se preocupe. Ela está conosco."

        pr "Excelente. Marque uma reunião com ela, Natasha."

        na "Sim, senhor."

    if julia_final2:

        pr "E você viu o que aconteceu com o Gevanni?"

        ba "O idiota do filho dele, né?"

        pr "Como é possível? Tudo por causa da sacerdotisa."

        ba "Você sabe como são os jovens... hormônios demais."

        pr "Você entende a gravidade da situação?"

        pr "A garota está desaparecida, pelo amor de Deus!"

        ba "E a polícia? Você declarou ela como desaparecida?"

        pr "Claro que não. A família Ai já foi avisada para não fazer nada. Mas eu não sei nada sobre isso."

        na "O Tony que está movimentando as cartas dele. Mas até agora nada. Provavelmente... devemos esperar o pior."

        pr "Isso estragaria todo o ri-"
    else:


        pr "Pelo menos parece que o Gevanni tá conseguindo manter as coisas com a outra sacerdotisa."

        ba "É... parece que o filho dele tava atrapalhando, mas tudo acabou dando certo."

        pr "Excelente."

    na "Com todo o respeito, senhor prefeito, Barão, mas não acho que devemos falar sobre isso aqui. Agora."

    pr "Ela tem razão."

    if diana_e6 == "barao":

        ba "O garoto sabe de tudo, senhor prefeito!"

        na "Como é?"

        pr "O que você quer dizer com 'tudo'?"

        ba "Eu mostrei a sala do Tony pra ele. O garoto já disse que ficaria do nosso lado. Não é, jovem?"

        menu:
            "Sim. E-eu deixei isso claro aquela noite no bar.":


                pass

        ba "Tá vendo?"

        na "Mesmo assim..."

        "Por que a Natasha tá me ferrando? Eu quero saber sobre essa história de 'sacerdotisa'!"

        "E, principalmente, que eles me aceitem no grupo! Eu sinto que eu tô tão perto!"

        pr "Não quero saber sobre essa história de sala, não faço ideia do que você está falando."

        pr "Mas se o Barão realmente confia, eu gostaria de confirmar se está tudo certo com a outra."

        ba "Com certeza. Você sabe que ela está muito bem protegida."

        pr "Você ainda lembra das especificações do contrato, não lembra? Vida boa."

        ba "Você se preocupa demais com essas raparigas."

        pr "E o seu jeito de falar me dá nojo."

        ba "A política tá comendo seu cérebro. Tá tudo certo. Ela tá vivendo bem e muito feliz."

        pr "Toda essa história de cantar... você podia só deixar ela ter uma vida normal."

        ba "De novo esse papo? Já disse que eu faço o que eu quero com ela. Ela é minha."

        pr "Pelo contrário, ela não é sua. Você só está protegendo ela até a hora certa."

        pr "Veja o que aconteceu com o Gevanni, caramba! A gente perdeu nosso homem no banco!"

        pr "Você sabe quanta preparação foi necessária pra isso? Isso vem desde meu avô! E a batata caiu na minha mão!"

        ba "Diga o que quiser, ela é minha."

        pr "Você não tem salvação..."

        pr "Não se esqueça o que aconteceu com o Gustav. Ele quis demais, e veja onde estamos agora."
    else:


        ba "Depois do que ele fez naquela noite, querendo proteger a Diana, melhor esperarmos um pouco."

        "Talvez se eu tivesse ficado do lado do Barão..."

        pr "Só quero que você se lembre do Gustav e do que está acontecendo com ele, por querer demais."

    menu:
        "Aquele velho nojento... não vejo a hora que saia o resultado do julgamento.":


            pass

    "???" "É bom que vocês estejam vendo a realidade."

    ba "Veja se não é a senhora Verônica Zaza! Dona da Blergh!"

    scene black with dissolve

    scene diana7_img19 with Dissolve(1.0)

    na "Senhora Zaza."

    pr "Como vai, [ve]?"

    za "Sem o velho, quem vai oferecer uma vitrine para suas garotas, hein, prefeito?"

    na "Senhora, Zaza. O prefeito não tem nada a ver com isso."

    za "Perdão, claro que não."

    pr "Isso é coisa do Tony."

    za "Claro... e esse dinheiro não rega sua campanha, claro que não."

    ba "Buahahaha! Essa mulher não tem papas na língua. Sua mãe não te educou não, senhora?"

    za "Imagine se algo viesse a acontecer com o Cassino do Barão. E sem o Gustav..."

    if julia_final2:

        za "E também sem o Gevanni..."

    za "De onde viria a grana, prefeito?"

    ba "O que pode acontecer com o meu cassino?! Você comeu merda, velha?!"

    na "Nós temos tudo sob controle, senhora."

    scene black with dissolve

    scene diana7_img20 with Dissolve(1.0)

    za "A Blergh! pode se tornar a salvação de tudo, prefeito."

    pr "As coisas não vão chegar neste ponto, senhora Zaza. Mesmo assim, é bom poder contar com a Blergh!"

    za "Eu quero um pedaço maior dessa torta. Acho bom vocês repensarem a posição de vocês antes que seja tarde."

    ba "Não gosto do tom de voz dessa mulher..."

    za "Eu vejo como vocês tratam as mulheres nesta cidade. Até mesmo as sacerdotisas, sendo submetidas a certas coisas."

    ba "Você é muito saidinha..."

    pr "Eu concordo com você. Os guardiães podiam fazer um trabalho melhor. Era justamente isso que eu estava falando."

    ba "Bah..."

    scene black with dissolve

    scene diana7_img21 with Dissolve(1.0)

    za "E esse garoto aqui? Ele pode escutar isto tudo? Hmm... eu já te vi?"

    menu:
        "Sim, eu sou amigo do Nathan.":


            za "Ah, sim... então nos encontramos, é isso?"

            mc "Aquela vez onde foi o desfile."
        "Não, acho que não nos encontramos.":


            za "É possível."

            na "Ele é o jornalista da revista, senhora."

    za "Ah, sim. Parece que eu te devo meus agradecimentos, jovem."

    if n3_gravou:

        za "Este jovem gravou a conversa com o Nathan que foi a base pra matéria."

        za "Você... desde aquele momento você já tinha olhos no grupo, garoto?"

        mc "Eu sabia que a Cássia seria uma boa parceira."
    else:


        "Eu não gravei a conversa com o Nathan no bar como a Cássia tinha pedido."

        "Mas não dá pra negar que eu participei de cabeça nesse rolo todo. Até acabei discutindo com o Nathan por causa disso."

    za "A matéria sobre a vida do Nathan colocou a Blergh! no radar. Seu trabalho foi muito importante."

    za "Claro que tudo conduzido pela Cássia, mas pelo que ela disse seu apoio foi fundamental."

    menu:
        "Obrigado, senhora.":


            mc "Fico feliz de ajudar."

            ba "Esse é o meu garoto."

            za "Este é um aliado interessante, mas a Cássia não é suficiente?"

            na "O máximo de apoio que pudermos melhor, não concorda, senhora?"

            ba "Além de que aquela víbora não faz parte de nada por enquanto. Vamos ver como ela vai se sair no momento final."

            za "Vamos ver... tomara que ela possa contar com o apoio deste jovem inteligente."

            mc "Sobre a compra, você diz?"

            za "Você tem um olhar penetrante, jovem. Um olhar que nos convida a falar de nossas vidas."

            za "Eu... adoraria conversar com você a sós em breve."

            mc "S-senhora..."

            ba "Essa mulher é um perigo, [mc]! Hahaha! Deve trepar como ninguém."

            za "Não que você saiba, Marcos. Eu nunca me deitaria com um estrupício como você."

            ba "Do que você me tá me xingando?!"

            za "Exatamente."

            mc "Pff..."

            za "Com certeza o garoto seria um amante muito melhor do que você. Ele não vê as mulheres como seus objetos."

            ba "Não se preocupe que eu ensino ele. E você, vê se xispa, senhora. Que tu tá amargando minha bebida."
        "Todos vocês me enganaram!":


            mc "Eu achei que o Nathan tava em dificuldades, mas ele também tava envolvido!"

            za "E quem não está? Você também está, paparazzo."

            za "Todos tentando ter uma cadeira nesta mesa. Você deveria culpar menos a vida e mais suas próprias ações. Você não é uma vítima aqui."

            mc "Ugh..."

    scene black with dissolve

    scene diana7_img22 with Dissolve(1.0)

    za "Enfim, vocês sabem como a Blergh! está crescendo e ela está se tornando uma das bases desta pirâmide."

    za "Acho bom vocês começarem a dar o valor que eu mereço. E tratem melhor suas mulheres."

    za "Adeus."

    ba "Velha mais atrevida..."

    pr "Primeiro o Gustav, Barão, Gevanni... agora a senhora Zaza. Por que tenho que lidar com tantos egos inflados?"

    ba "Ela nunca vai fazer um pingo de diferença pra você, Basílio. O Cassino é uma rocha."

    scene black with dissolve

    scene diana7_img23 with Dissolve(1.0)

    na "Uma rocha que pode quebrar a qualquer momento se você colocar uma arma na mão da sua inimiga."

    ba "Tá falando da Diana?"

    na "Pra quê dar palco pra ela? D-digo... com todo o respeito, senhor Barão."

    pr "Ela tem razão, Marcos."

    ba "Vocês são medrosos demais. Eu estou dizendo. A garota sabe o lugar dela."

    ba "Aliás, ela já devia ter descido."

    scene black with dissolve

    scene diana7_img14 with Dissolve(1.0)

    ba "[mc]. Vai no quarto dela e traz essa mulher. Espero que ela não faça graça."

    ba "Hoje é o dia que ela vai dobrar os joelhos pra mim e cantar na frente de todos vocês."

    ba "Não vou tolerar nenhuma desobediência. E vou provar pra vocês que ela aceitou o destino dela."

    menu:
        "Sim, senhor.":


            pass
        "E se ela não quiser descer?":


            ba "Traga ela pelos cabelos, [mc]."

            pr "Marcos!"

            ba "Só tome cuidado para não estragar o penteado. Quero minha garota linda para meus convidados."

    mc "Deixa comigo."

    scene black with dissolve

    scene diana7_img23 with Dissolve(1.0)

    na "[mc]... quer uma dica?"

    menu:
        "Não preciso. Eu sei me virar, assistente.":


            na "O-ok..."

            ba "Buahahahaha! Esse garoto tem fibra!"
        "Diga. Que dica?":


            na "A Diana é uma mulher sensível. Mas ao mesmo tempo ela não tem medo."

            na "Usar força demais pode não ser o melhor caminho."

            ba "Bah... mulheres são muito frescas. Ele vai trazer ela, vocês vão ver."

            mc "V-valeu, Natasha."

    mc "Tô subindo lá."

    scene black with dissolve

    scene cassino_ponte3 with Dissolve(1.0)

    "Por que ela não desceu ainda?"

    "{i}toc toc{/i}"

    mc "Diana. É o [mc]. Abre pra mim?"

    "..."

    "{i}toc toc{/i}"

    mc "Diana?!"

    "..."

    "Ué?"

    "O que a Diana tá fazendo? O Barão tá esperando ela."

    "Tá TODO MUNDO chique esperando ela..."

    "E agora o Barão ainda coloca na minha mão pra iniciar o show. Que caramba, viu?"

    "{i}toc toc{/i}"

    mc "DIANA!"

    "..."

    "Não é possível! E agora?"

    menu:
        "Tentar abrir a porta":


            pass

    play sound som_porta

    mc "O-opa... tá aberto."

    play sound som_porta

    scene black with dissolve

    scene diana7_img24 with Dissolve(1.0)

    mc "Diana?"

    "Ela não tá aqui?"

    mc "Hm?"

    scene diana7_img25 with vpunch

    "Q-que merda é essa?!"

    "Não vai me dizer que é esse o plano dela?! Não, Diana..."

    play sound som_16_chuveiro

    "{i}sshhhh{/i}"

    mc "O chuveiro..."

    "Não... não pode ser."

    mc "DIANA!"

    play sound som_hit

    scene diana7_img26 with hpunch

    mc "DIANA!!!"

    d "..."

    "Não! O q-que eu fiz?!"

    mc "DIANA! ME RESPONDE!!!"

    d "[mc]..."

    mc "Diana, você tá bem?!"

    d "T-tô aqui... você... pode entrar..."

    scene diana7_img27 with vpunch

    mc "O-oi... você tá..."

    d "Estou me aprontando pro show."

    menu:
        "Você tá bem? Tá machucada?":


            d "Não... tá tudo ok."
        "O que é aquela faca no quarto?!":


            d "Ah... a faca... Era pro Barão. Mas eu desisti."

            mc "C-como é?"

            d "Eu tava esperando ele. Mas nada aconteceu, relaxa."

            mc "O-ok..."

    mc "Não queria invadir assim... só fiquei preocupado. Desculpa."

    if diana_namoro:

        d "Nós tamo namorando, [mc]... não tem nada aqui que você não tenha visto."

        mc "Isso é, mas... mesmo assim..."
    else:


        d "Não tem problema."

    mc "Tô me sentindo bobo agora... você me assustou."

    d "Eu desisti, [mc]..."

    mc "Desistiu?"

    d "Tô me sentindo envergonhada... por ter feito tudo isso e agora tudo acabar assim."

    d "O Barão... ia ser fácil me livrar das minhas amarras."

    menu:
        "Você... planejava mesmo... com a faca?":


            pass

    d "Ele é a causa de tudo. Se eu acabo com ele, todo o martírio acaba."

    d "O desgraçado não me vê como uma pessoa, mas como um objeto pessoal dele."

    d "Acabando com ele... eu teria uma chance..."

    d "Mas não tenho força pra fazer isso com alguém. Eu posso cantar, mas não matar."

    mc "Diana..."

    scene black with dissolve

    scene diana7_img28 with Dissolve(1.0)

    mc "Você é uma mulher de espírito. Você tem criatividade, emoção, sensibilidade."

    mc "Não é tua cara fazer isso."

    d "Mas se essa é a única chance de escapar, e eu não consigo... então estou fadada a ser escrava dele."

    d "Este show. Tudo isso aqui é pra esfregar na minha cara que eu sou dele."

    d "Proibiu minha música, e agora chamou todo mundo. Ele quer provar pra todos que eu fui dominada."

    mc "Ele é um homem horrível..."

    if diana_e6 == "barao":

        d "Você fala isso mesmo tendo ido naquela sala secreta com ele na outra noite?"

        mc "Sim. Mesmo que eu ficasse do lado desse grupo, não dá pra eu negar que o Barão é um cretino."
    else:


        mc "Ele tentou me matar lembra?"

        d "Ele mataria qualquer um. O homem é um desequilibrado."

        mc "Sim. Um cretino."

    mc "Mas o que eu tava pensando é se não tem outra forma?"

    if d7_envelope == 1:

        mc "Você me deu aquele envelope. Eu achei que você tivesse um plano."

        d "Eu tinha um plano... mas... não dá."
    else:


        "Se eu tivesse escolhido o envelope dela... talvez a gente tivesse um plano agora."

    d "Não adianta a gente se enganar, [mc]."

    d "A gente é pequeno demais."

    if diana_e6 == "barao":

        d "Certo você que foi na sala com ele lá no bar."

    d "Eu vou aceitar meu destino e ser uma escrava desse escroto pra sempre."

    "O Barão tava certo... ele destruiu o coração da Diana."

    "Aquela mulher cheia de energia, cheia de poder que eu encontrei, reduzida a isso que sobrou."

    "Como uma pessoa pode foder a cabeça de outra desse jeito?"

    if diana_e6 == "barao":

        "É com esse tipo de gente que eu vou me aliar?"

    "Esse é o momento da verdade."

    if diana_namoro:

        "Ver minha namorada desse jeito... tá fodendo minha cabeça, mano."

    "A Diana tá estilhaçada. E eu sou a única pessoa que pode dá uma força pra ela nesse momento."

    "O que eu disser aqui vai mudar nossa vida juntos pra sempre."

    label diana7_menu1:

        pass

    menu:
        "Aceite seu destino. Encontre a felicidade aqui no Cassino.":


            $ d7_escolha = 1

            "Eu vou confirmar que a Diana vai ficar na mão do Barão pra sempre?"

            "Isso vai ajudar ele e pode me aproximar ainda mais do grupo. Mas a Diana... ela vai se ferrar pra sempre."
        "E daí que você não pode matar ele? Use o SEU ponto forte pra se rebelar.":


            $ d7_escolha = 2

            "Vou reanimar ela pra ela se rebelar contra o Barão do jeito dela. Com a arte dela."
        "Você não pode matar ele, mas eu posso. Deixa comigo. Eu sumo com esse cara pra você.":


            $ d7_escolha = 3

            "Eu vou mesmo fazer isso? EU vou matar o Barão pra ela?"

            "O que vai ser da minha vida depois de ser acusado de matar uma pessoa?"

    menu:
        "É isso mesmo que eu quero.":


            pass
        "Calma... tenho que pensar nisso melhor.":


            jump diana7_menu1

    $ renpy.block_rollback()

    if d7_escolha == 1:

        mc "Você tá certa. Tem coisas que são grandes demais pra gente."

        scene black with dissolve

        scene diana7_img30 with Dissolve(1.0)

        d "Parece que não foi só meu coração que eles despedaçaram."

        mc "Heh... tem razão... parece que eu também me rendi."

        d "Foi muito bom enquanto durou, [mc]. A esperança, eu digo."

        d "As coisas vão continuar assim. Como sempre foram."

        mc "É... acho que é o melhor."

    elif d7_escolha == 2:

        mc "Talvez você não seja uma pessoa com força pra esfaquear alguém. E isso é ruim?"

        mc "Agora, você tem sua sensibilidade, sua arte. Será que você não pode fazer isso dessa forma?"

        scene black with dissolve

        scene diana7_img29 with Dissolve(1.0)

        d "M-minha arte?"

        mc "Você colocou sua verdade naquela música que o Barão proibiu. Será que não tem uma forma de usar isso?"

        d "[mc]... como você consegue enxergar luz onde só existe trevas?"

        mc "Você tá num buraco agora. Você só vê escuridão. Deixa alguém que tá do lado de fora te dizer o que tem em volta."

        d "Palavras tão bonitas... e tão reais."

        d "Quem sabe um dia eu não consiga, certo?"

        mc "É... se você não tem forças hoje, talvez amanhã."

        d "Tem razão... obrigada."

        if diana_namoro:

            d "O senhor é o amor que eu precisava, mas não mereço."

            mc "Claro que merece. Uma mulher igual você merece qualquer cara."

        scene black with dissolve

        scene diana7_img30 with Dissolve(1.0)
    else:


        mc "Deixa comigo. Eu dou um jeito nele. Eu vou fazer o que você não conseguiu."

        d "E-enlouqueceu?!"

        mc "Talvez... mas é o que eu decidi."

        scene black with dissolve

        scene diana7_img30 with Dissolve(1.0)

        d "M-mesmo que por um milagre você consiga! Você vai acabar com tua vida! De jeito nenhum!"

        mc "Minha vida pela sua. E se eu quiser fazer isso?"

        d "Não. De jeito nenhum. Eu não conseguiria viver sabendo que você tá apodrecendo numa prisão."

        d "Por favor... prometa que você não fará isso. Eu imploro!"

        menu:
            "Tudo bem... eu prometo.":


                pass

        d "Obrigada... as coisas vão dar certo. Não precisamos perder nossas vidas por causa do cretino."

        mc "Combinado..."

    d "Então vou me arrumar e descer."

    mc "Tem bastante gente te esperando."

    d "Você... pode ver esse show?"

    mc "Claro. Nunca que eu perderia uma apresentação sua."

    d "Obrigada... quem sabe você não consegue algo pra sua revista?"

    d "Ficaria feliz se de toda essa desgraça surgisse pelo menos alguma coisa boa."

    "Verdade... o chefe quer que eu consiga um furo pra publicar..."

    "E até agora eu não consegui nada publicável. Nada que eu possa comprovar."

    mc "Então vou descer e me preparar pra sua apresentação."

    d "Tudo bem. Nos vemos lá embaixo em breve."

    mc "Até daqui a pouco."

    if d7_escolha == 3:

        scene black with dissolve

        scene diana7_img25 with Dissolve(1.0)

        "A Diana pode não querer que eu faça isso... mas EU QUERO."

        "Ela não precisa saber. Mas o Barão VAI parar de encher o saco dela. Mesmo que eu me foda por isso."

        "Vou pegar essa faca e levar ele pra um lugar com só nós dois."

    scene black with dissolve

    pause 2.0

    scene diana7_img31 with Dissolve(1.0)

    mc "Ufa... voltei."

    "Parece que o pessoal tá ficando impaciente. Melhor eu avisar o Barão."

    mc "Barão."

    ba "[mc]! Cadê ela?! Me fala que ela tá descendo AGORA!"

    mc "Sim. Ela tá. Só tava terminando de se arrumar."

    ba "Perfeito. E o que você achou?"

    menu:
        "Tá tudo sob controle. Ela não vai tentar nada.":


            ba "Excelente trabalho!"

    ba "Então agora podemos sentar e só aproveitar a música dela."

    ba "Opa! E olha ela aí!"

    ba "Chegou a hora, pessoal! Uma salva de palmas pra Jóia do Cassino! Dianaaa!"

    scene black with dissolve

    scene diana7_img32 with Dissolve(1.0)

    d "Boa noite, senhoras e senhores. É um prazer ter figuras tão ilustres para ouvir minha música esta noite."

    d "Vocês sabem como o Cassino é o coração do entretenimento da ilha e da capital como um todo."

    d "É uma honra para mim ser a face de um local de tamanha importância econômica e até social."

    ba "Isso aí! Viva o Cassino do Barão!"

    menu:
        "Bater palmas":


            mc "{i}clap clap clap{/i}"

        "Barão. Preciso falar com você algo em particular" if d7_escolha == 3:

            "É minha chance de pegar ele. Quando todo mundo tá olhando pra Diana."

            ba "Tá doido, garoto? Agora na hora do show? Não pode ser depois?"

            mc "Pode... mas é sobre a Diana. O senhor vai querer saber."

            ba "Depois. Você não sabe como eu queria ver este momento."

            mc "Ok... o senhor manda."

            "Depois do show... você pega ele."
        "...":


            pass

    d "Antes de iniciar a performance da noite, gostaria de fazer um agradecimento."

    d "Primeiro, mais uma espécie de congratulações, a todas as mulheres que vivem aqui."

    d "A capital não é o melhor lugar para nós. Não somos valorizadas e se quer respeitadas nesta cidade."

    d "Pelos trabalham que nos colocam à forma como lidam conosco. Poucas mulheres chegaram em posição de poder aqui."

    d "A maioria acaba em posição de subserviência, ou como verdadeiros troféus para serem apreciadas pelos olhos masculinos."

    za "Disse tudo, Diana."

    if sayuri_final3:

        s "Penso o mesmo. Não é simples."

    d "Mas nós sabemos nosso valor. E um dia eles terão que "

    ba "Bah! Canta logo!"

    if d7_agradece:

        d "E, em segundo lugar, para uma pessoa muito importante na minha vida."

        d "Quando nos conhecemos eu fiz um pedido a essa pessoa e ele aceitou de bom grado nossa parceria."

        d "De lá pra cá, nossa relação de trabalho virou amizade, das maiores que eu desenvolvi na vida."

        if diana_namoro:

            d "E, essa amizade acabou se tornando amor."

            ba "Amor? Que história é essa?"

            "E-epa..."

            if sayuri_final3:

                scene black with dissolve

                scene diana7_img33 with Dissolve(1.0)

                s "Amor?"

                "Eita... agora só falta a Diana falar meu nome..."

                scene black with dissolve

                scene diana7_img32 with Dissolve(1.0)

        d "Um agradecimento especial para o paparazzo [mcc]."

        d "Sem você, esta noite não aconteceria."

        ba "Aí eu concordo! Salva de palmas!"

        menu:
            "Valeu, gente. Pra mim também foi muito bom.":


                pass

        pr "..."

    d "E agora. Vamos para a apresentação da noite."

    d "Uma música especial que preparei para que você entendam como é a vida no Cassino."

    d "Aos interessados... eu acho que vocês deveriam gravar um show como este."

    "E-ela falou isso olhando pra mim? É um sinal?"

    "Eu só tenho meu celular, mas vai ter que ser com ele."

    menu:
        "Começar a filmar a apresentação da Diana.":


            pass

    $ renpy.choice_for_skipping()

    $ proibido_salvar = True
    $ show_quick_menu = False

    d "Minha mais nova música. A qual coloquei todo meu coração e minha verdade."

    play music "audio/musica_6_diana.mp3" loop

    $ renpy.pause(delay=10, hard=True)

    scene diana7_img34 with Dissolve(3.0)

    d "{cps=6}{i}Na esquina da rua fim com o começo...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Cruzando aquela avenida cujo nome sempre esqueço...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Ela olhava com os olhos frios de quem entende...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}As dificuldades que só o escravo sente.{/i}{/cps}{w=2.0}{nw}"

    scene diana7_img34 at diana_esquerda with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana7_img35 with Dissolve(3.0)

    d "{cps=6}{i}As luzes dos carros e as luzes das ruas...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Tudo lembrava dos dias mais turbulentos...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Quando suas palavras não eram suas...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}E o desespero preenchia todos os momentos.{/i}{/cps}{w=2.0}{nw}"

    scene diana7_img35 at diana_direita with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana7_img36 with Dissolve(3.0)

    d "{cps=6}{i}As luzes então apagaram como um eclipse...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Os olhos carregados ela chorou e disse...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}O fim enfim o momento mais aguardado...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Dessa forma seu espírito seria libertado.{/i}{/cps}{w=2.0}{nw}"

    scene diana7_img36 at diana_esquerda with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana7_img37 with Dissolve(3.0)

    d "{cps=6}{i}No momento de fortúnio o eclipse chegou para sua alegria...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Pois no fim da noite vinha outra vez o dia...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}E a amarra da vida novamente a prendia...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}A jovem garota, a escrava da ilha.{/i}{/cps}{w=1.0}{nw}"

    scene diana7_img37 at diana_direita with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    stop music fadeout 3.0

    $ proibido_salvar = False
    $ show_quick_menu = True

    "E-essa música! Não é a música que o Barão proibiu?"

    scene black with dissolve

    scene diana7_img38 with Dissolve(1.0)

    za "Essa letra... essa é a verdade, Diana?"

    pr "Natasha... acho melhor nós irmos..."

    ba "E-essa é uma música inventada! Pra passar emoção, não é, Diana?!"

    d "Eu disse tudo o que tinha pra dizer... o que vocês vão fazer com isso depende de vocês."

    if d7_escolha == 1:

        d "Me disseram que eu devia aceitar meu destino. Mas eu não farei isso."

        d "Seria outro homem tentando dizer pra eu aceitar a vida que me colocaram."

    elif d7_escolha == 2:

        d "Mas a pessoa mais importante pra mim neste momento me lembrou de algo."

        d "Que eu tenho a MINHA força. O MEU poder. O poder da arte e da emoção."

        d "E ele foi meu apoio para poder cantar esta música para vocês hoje."

    d "Eu tenho a capacidade de mudar minha vida. E tomar as decisões que EU quero pra mim."

    d "Pro inferno as mãos que me oprimem e me escravizam! Eu vou lutar pela minha liberdade!"

    scene diana7_img39 with hpunch

    ba "Cala a boca, mulher! Você tem tudo de bom aqui!"

    ba "Eu te garanto uma vida de rainha! Que merda você tá falando?!"

    d "Eu terei o que EU QUERO. E não o que você acha que eu mereço."

    d "VOCÊS QUE TÃO AQUI! AGORA VOCÊS SABEM COMO AS COISAS ACONTECEM!"

    d "VOCÊS VÃO PERMITIR QUE ALGO ASSIM CONTINUE?! VÃO FAZER PARTE DE UM ESCÂNDALO COMO ESTE?!"

    if sayuri_final3:

        scene black with dissolve

        scene diana7_img33 with Dissolve(1.0)

        s "Me desculpe... isso... está fora do meu poder."

    d "Alguém?!"

    scene black with dissolve

    scene diana7_img40 with Dissolve(1.0)

    za "Você apostou garota, e eu te dou os parabéns pela coragem."

    za "Mas não quer dizer que realmente vai dar em algo. É uma pena."

    za "Infelizmente... quando você atenta contra o rei, tenha certeza de matar ele."

    d "Não é possível! Vocês tão vendo o que tá acontecendo!"

    scene black with dissolve

    scene diana7_img41 with Dissolve(1.0)

    na "Nós vimos tudo o que precisávamos. O prefeito está se retirando."

    pr "..."

    pr "Ligue para o Tony. É bom que ele venha pra cá."

    na "Sim, senhor."

    d "Vocês vão ignorar mesmo?! O prefeito da cidade?!"

    scene black with dissolve

    scene diana7_img39 with Dissolve(1.0)

    ba "HAHAHAHA! O que você achou?! Que eles iam ficar com peninha de você?!"

    ba "Todo mundo sabe que você é minha escrava e ninguém vai fazer porra nenhuma!"

    d "Vai todo mundo saber! Alguém vai fazer!"

    ba "Ninguém vai saber, sua puta! A FAUX é a única cobrindo o evento e eles nunca vão publicar isso!"

    d "UUGHH! Todos vocês?! Ninguém aqui tem um pingo de ética!?"

    "..."

    d "Não é possível... ninguém... vai fazer nada..."

    d "Tudo isso... vai sumir pra sempre... e ninguém vai saber..."

    ba "E você vai sofrer as consequências! Ah, se vai, sua puta ingrata!"



    scene diana7_img42 with hpunch

    "Eu gravei tudo!"

    "E a Sofia tá na redação pronta pra publicar o que eu mandar!"

    "Se isso aparecer no site da revista, em minutos todo mundo vai tá falando isso nas redes sociais!"



    "Todo mundo aqui faz parte do grupo. Talvez ninguém levante o dedo pra ajudar a Diana."

    "Mas eu posso..."

    "Se eu divulgar este vídeo, eu vou acabar com o Barão. Talvez até com o Cassino."

    "Todo mundo vai saber o que ele fazia com a Diana. Eu gravei ele falando tudo."

    "Mas daí... todo mundo vai saber que vai ter sido eu."

    "O grupo vai me foder de todas as formas possíveis. Até eu acabar a sete palmos abaixo da terra."

    "E não sou só eu. Se eles descobrirem que a Sofia que publicou, ela tá fodida também!"

    "Eu posso não ter a grana deles, ou a força deles, ou a influência ou as armas... mas eu tenho a revista."

    "Meu coração tá saindo pela boca! Minha perna tá tremendo! Eu tô suando frio!"

    "O que eu faço agora?!"

    label diana7_menu2:

        pass

    menu:
        "Mandar a Sofia publicar o vídeo no site da revista!":


            "O Tony... o prefeito, o Barão... todo mundo vai saber que fui eu."

            "Certeza que minha vida vai tá na reta depois dessa. E eu já vi o que eles fazem com quem vai contra eles."

            "E dessa vez não vai ser só eu... o vídeo provavelmente vai sair no nome da Sofia."

            "Por que raios o chefe colocou a filha dele pra fazer isso?!"

            "Com certeza isso vai dar MUITA merda."

            "Mas não dá."

            "Não tem como deixar a Diana assim."

            "Viver essa vida na mão do Barão pra sempre. Ela teve força pra vir aqui e jogar a merda no ventilador."

            "Ela acreditou que alguém faria alguma coisa. Que pelo menos alguém faria a coisa certa e sentiria nojo disso tudo."

            "Mas todo mundo virou a cara pra ela."

            "Eu não vou."

            "Eu vou te ajudar, [d]. Eu vou fazer sua mensagem chegar até as pessoas."

            "Esses filhos da puta não vão te calar!"
        "Fazer como os outros, ficar calado e ignorar o apelo da Diana":


            jump diana_final3



















            p "Este caminho ainda não está disponível nesta atualização."

            p "Para caprichar bastante em cada final, o RB preferiu se dedicar totalmente a um caminho antes de fazer os outros."

            p "Mês que vem você poderá escolher esta opção e ver os outros finais da [d]!"

            p "Veja todos os finais para juntar os pedaços do grande mistério e descobrir todos os caminhos!"

            p "Não esqueça de ver quais finais você já conseguiu olhando no menu e no ícone do personagem"

            jump diana7_menu2

    "Só tenho que mandar a mensagem pra Sofia."

    "{i}Tec tec tec{/i}"

    "{i}Sofia, tô mandando um vídeo que é o maior furo de reportagem que vai sair da festa.{/i}"

    "{i}Publica antes da Faux!{/i}"

    menu:
        "{i}E toma cuidado... você sabe quem são estas pessoas.{/i}":


            pass
        "Não vou escrever nada":


            pass

    play sound acerto

    "Pronto."

    "Agora é com a Sofia."

    "A matéria vai tá no ar logo logo. É impossível que esses corruptos não façam alguma coisa quando o país inteiro cair matando."

    "Agora sou eu... tenho que pensar na minha própria pele."

    "Dar o fora daqui antes que eles vejam o que eu fiz."

    scene diana7_img43 with vpunch

    pause

    d "Então é isso..."

    ba "'Isso'? Você acha que esse seu show vai acabar nisso?!"

    ba "Eu vou te mostrar o que acontece com quem desafia."

    d "A-ah..."

    if sayuri_final3:

        s "Senhor Barão... você sabe nosso compromisso com as sacerdotisas."

        ba "Não se preocupe... daqui um tempo essa puta vai estar novinha em folha."

        s "..."

    "Ele vai acabar com a Diana."

    ba "E eu vou começar aqui mesmo."

    d "N-não! Não vem pra cima de mim, seu monstro!"

    ba "Você vai ver o que é ser um monstro de verdade!"

    "Ele tá indo pra cima da Diana na frente de todo mundo!"

    if d7_escolha == 3:

        scene black with dissolve

        scene diana7_img46 with Dissolve(1.0)

        "É a hora perfeita pra eu usar a faca que eu peguei."

        "É só pegar ele e meter a peixeira no desgramado."

        "Ou... esse é um plano terrível. Que vai me custar a liberdade."

        "Talvez o melhor seja dar o fora daqui. E agora?"

    "Eu tenho que dar o fora antes que eles vejam o resultado do vídeo."

    "Mas se eu não fizer nada... a Diana..."

    "O que eu faço?!"

    menu:
        "Segurar o Barão":


            $ d7_faca = 1

            mc "Barão! Não faz isso!"

            scene diana7_img44 with hpunch

            pause

            ba "Que é isso, moleque?!"

            mc "Você não pode bater nela!"

            ba "Como é?! Quem você pensa que é pra me falar isso?!"

            menu:
                "Isso não tá certo! Eu não vou deixar!":


                    ba "Era só o que me faltava. Você ficando com dó dessa filha da puta?!"
                "Isso não vai ficar bom pro senhor. Se controle.":


                    mc "Você é um homem de prestígio. Não deixa ela estragar tua moral com todo mundo. A TV tá aqui."

                    ba "Você escutou o que ela falou. Se eu não fizer nada, daí que minha moral vai cair."

                    ba "Eu sou um homem e não posso deixar uma mulher levantar a voz pra mim assim."

                    ba "Eu vou colocar ela no lugar dela."

                    mc "Senhor... me escuta..."

            ba "Me solta, idiota!"

            if mc_fisico > 250:

                scene diana7_img44 with hpunch

                mc "Você não vai pra lugar nenhum!"

                "Finalmente aqueles treinos serviram pra alguma coisa!"

                ba "Desde quando um franguinho igual você consegue me imobilizar, assim!? Desgraçado!"

                mc "Você não vai bater nela!"

                ba "Quem você pensa que é pra falar assim comigo?!"
            else:


                scene diana7_img42 with hpunch

                "Merda! Não tenho força pra segurar ele!"

                "Se eu tivesse treinado mais! DROGA!"

                if d7_escolha == 3:

                    "Mas... eu tenho outro jeito de segurar ele."
                else:


                    "Desculpa, Diana."

                    ba "Sua, cadela!"

                    d "Aahhh!"

                    ba "Toma, vadia!"

                    d "Aaiii!!!"

                    "Merda..."

                    play sound som_hit

                    scene diana7_img47 with vpunch

                    mar "Vamos parar com isso."

                    ba "Me solta, idiota! Eu ainda não acabei!"

                    mar "Meu chefe mandou eu te segurar. É só meu trabalho."

                    ba "Eu vou acabar com você também!"

            if d7_escolha == 3:

                "Eu tô com a faca aqui."

                "Se eu quiser, eu mato esse filho da puta agora!"

                "Provavelmente eu vou pra cadeia. Matando ele ou não, isso vai ser tentativa de homicício."

                "Isso se esses fdp não me matarem antes de eu chegar na prisão."

                "Com certeza vai dar merda. Mas eu tô com a faca e o queijo na mão."

                "O Barão se acha a última bolacha do pacote. Você pode fazer ele provar o sabor do próprio veneno agora, [mc]."

                menu:
                    "Esfaquear o Barão":


                        $ d7_faca = 2

                        "Foda-se tudo! Mesmo que minha vida acabe aqui, ele vai cair comigo!"

                        mc "FILHO DA PUTA!!!"

                        scene diana7_img45 with hpunch

                        pause

                        ba "A-AAGHH!"

                        mc "Essa é pela Diana!"

                        scene diana7_img45 with hpunch

                        ba "F-FILH-"

                        mc "E ESSA É POR MIM, DESGRAÇADO!"

                        scene diana7_img45 with hpunch

                        ba "AAAAGHHH!"

                        "Que delícia! Esse cara que se acha o rei do mundo com essa carabina!"

                        "Apontando ela pros outros! Achando que é intocável!"

                        mc "Que é intocável agora, seu FILHO DA PUTA?!"

                        ba "AAIIINNGHHH!!!"

                        play sound som_hit

                        scene diana7_img47 with vpunch

                        mar "Vamos parar com isso."

                        mc "Marco!"

                        ba "S-socorroo..."

                        mar "O que você pensa que tá fazendo, maninho?!"

                        mc "Ele ia bater na Diana! Esse filha da puta mereceu!"

                        mar "Você tá perdido, maninho!"
                    "Esquecer essa ideia maluca":


                        "Não! Não posso jogar minha vida no lixo desse jeito."

                        "Por pior que seja... nem a Diana ia querer isso."
            else:


                play sound som_hit

                scene diana7_img47 with vpunch

                mar "Vamos parar com isso."

                mc "Marco!"

                ba "Me solta, idiota! Eu ainda não acabei!"

                mar "Meu chefe mandou eu te segurar. É só meu trabalho."

                ba "Eu vou acabar com você também!"
        "Apenas olhar pro lado":


            "Eu... não posso fazer nada agora... minha vida tá em jogo aqui."

            scene diana7_img42 with hpunch

            "Desculpa, Diana."

            ba "Sua, cadela!"

            d "Aahhh!"

            ba "Toma, vadia!"

            d "Aaiii!!!"

            "Merda..."

            play sound som_hit

            scene diana7_img47 with vpunch

            mar "Vamos parar com isso."

            ba "Me solta, idiota! Eu ainda não acabei!"

            mar "Meu chefe mandou eu te segurar. É só meu trabalho."

            ba "Eu vou acabar com você também!"

    mar "Barão. Você precisa de ajuda."

    "Aproveitar que o Marco tá com ele. É minha chance de ajudar a Diana!"

    scene black with dissolve

    scene diana7_img48 with Dissolve(1.0)

    mc "Você tá bem?!"

    d "Tô..."

    mc "Que bom..."

    d "Você postou?"

    mc "E-eu?"

    menu:
        "Sim. Eu mandei o vídeo pra redação. Já deve tá no ar.":


            pass

    d "Obrigada..."

    mc "Não tem o que agradecer. Eu fiz o certo. Só isso."

    d "Olha como eu sou hipócrita."

    mc "Hm?"

    d "No fim... eu também te dei meu peso pra você carregar."

    d "Eu disse... desde aquele dia no quarto... que você ia acabar se ferrando por carregar o peso dos outros."

    mc "Diana..."

    d "Quem ia imaginar... que seria meu peso que ia te derrubar."

    if diana_namoro:

        d "Você... quis ser meu príncipe."

        mc "Você é meu amor. Eu nunca ia te deixar desse jeito."

    mc "Para de pensar besteira. Todo mundo vai saber a verdade."

    mc "Eu só não sei... qual é a próxima parte do plano. Você pensou no que acontece agora?"

    d "Não... desculpa."

    if diana_namoro:

        d "Eu sou guiada pela emoção, meu amor."
    else:


        d "Eu sou guiada pela emoção."

    d "Eu só torço... pra que ela leve a gente pra segurança agora."

    mc "Ela? A gente precisa sair daqui antes que eles desc-"

    scene black with dissolve

    scene diana7_img49 with Dissolve(1.0)

    to "Que que tá acontecendo aqui?!"

    to "Senhor prefeito, o senhor está aqui ainda?"

    pr "Sim... temos que ir Natasha..."

    na "S-sim. Já estávamos de saída..."

    to "Você já devia ter tirado ele daquí faz tempo, secretária."

    pr "O Barão... ele... passou um pouco do limite."

    to "O Barão está acabado, senhor."

    pr "Como é?!"

    to "Todos sabem o que aconteceu aqui."

    "N-não! Não é possível! Ainda não por favor!"

    pr "Impossível. Só a Faux está cobrindo."

    to "A revista..."

    "NÃO!!!"

    pr "O garoto!"

    to "Senhor..."

    na "Isso é muito pior do que a gente tinha imaginado, prefeito."

    na "Tony, por favor, tira ele do cassino."

    to "..."

    na "Eu vou lidar com o Barão e com a sacerdotisa. E com o paparazzo..."

    to "É melhor que e-"

    pr "Deixe com ela, Tony. A Natasha vai saber cuidar disso."

    to "Sim, senhor. Vamos. Eu te levo."

    to "Marco! Fique de olho em tudo! E leve o Barão para um lugar seguro."

    if d7_faca == 2:

        to "Por que raios ele tá sangrando?!"

        to "Não acredito que foi esse fedelho!"

        mar "Eu fiz a atadura, mas ele desmaiou. Não sei se aguenta, chefe."

        pr "Isso é um absurdo."

        to "Não acredito... você sabe o que fazer."

    mar "Pode deixar, chefe."

    na "Marco, depois ligue para o Luca. A Faux precisa controlar a narrativa!"

    mar "Você..."

    pr "Marco, obedeça a Natasha."

    mar "Sim, prefeito."

    pr "Depos nos falamos. Cuide de tudo aqui."

    na "Pode deixar."

    pr "Vamos, Tony. Me explica tudo e eu vou bolar o que fazer."

    na "Agora deixa eu ver..."



    scene black with dissolve

    scene diana7_img50 with Dissolve(1.0)

    na "Você tá bem, Diana?"

    mc "Natasha..."

    d "Você veio..."

    na "Que show todo foi esse? Você tinha me dito que..."

    d "Desculpa... mas eu não podia continuar daquele jeito."

    na "Vivendo uma vida de rainha no Cassino? Era tão difícil assim?"

    na "Você entende que essa vida é melhor que a grande maioria das pessoas?"

    menu:
        "Sendo escrava daquele idiota?":


            na "Todos nós temos que sacrificar algo por uma vida melhor."

            d "Ele tem razão. Eu prefiro morrer do que continuar com ele."
        "Não vou me intrometer":


            d "Eu não consegui. Me perdoa."

    na "Que coisa... você sempre foi emotiva demais."

    menu:
        "O que você tá fazendo aqui, secretária?":


            na "Resolvendo o que vocês complicaram."
        "Por que você não ajudou a Diana?":


            na "Eu ajudei ela a desistir dessa ideia absurda."

            mc "Você?"

            na "Mas parece que ela preferiu seguir o conselho de outra pessoa."

    d "Não. Fui eu. Eu decidi fazer isso."

    na "Você entende que as coisas nunca mais serão as mesmas?"

    d "Você tem razão. Esquece o passado. Tudo mudou. Me tira daqui."

    na "O que você quer dizer?"

    d "Faz o que eu sempre te pedi. Me tira desta prisão."

    na "Você... você tá pensando com o coração, não com a cabeça!"

    d "O [mc] também precisa de ajuda. Ele publicou o vídeo."

    na "Ele tá com a corda no pescoço."

    if d7_faca == 2:

        na "Ele fez muito mais que publicar um vídeo. Ele pode ter matado o Barão."

        mc "Ele mereceu!"

        d "Ele fez por mim."

    na "Não consigo ver uma forma do [mc] sobreviver a isso."

    na "Esse foi o maior golpe que nosso grupo tomou desde..."



    scene black with dissolve

    scene diana7_img51 with Dissolve(1.0)

    d "'Nosso'? Você realmente virou uma deles?"

    na "Graças a você."

    d "Por que você prometeu que nunca perderia seu espírito. Sempre seria a Natasha que eu conheci."

    na "Você não entende..."

    menu:
        "Natasha. Eu, a Diana e... quem publicou o vídeo... todos nós não temos pra onde ir.":


            pass

    d "Você é nossa única chance agora, minha amiga."

    na "Minhas mãos estão atadas. Vocês não sabem o que eu tive que fazer pra virar a secretária do Donatello."

    na "Eu sofri muito pra chegar onde eu cheguei. Eu não quero jogar isso fora agora."

    d "Eu imagino. Não quero que você perca o que você conquistou."

    d "Mas você é a única. Sem você..."

    na "Droga..."

    if natasha_e2 == "positivo":

        "Eu falei pra Natasha sobre o Barão aquela vez. Pode ser uma boa lembrar isso agora."

        menu:
            "Cobrar ela da informação do Barão":


                $ natasha_cobrou = True

                mc "Natasha, lembra do que aconteceu quando você pediu pra eu ir atrás do Barão?"

                na "Sei..."

                d "Que história é essa?"

                na "Era algo do prefeito. Desde o começo ele sabia que o Barão tava saindo da linha."

                na "Ele me colocou aqui, lembra? Pra encontrar algo sobre ele."

                d "Sim! A gente se falou algumas vezes naquela época."

                d "Foi lá que tudo isso aqui começou."

                na "Sabia... você realmente tava planejando algo assim."

                d "E como o [mc] ajudou?"

                na "Ele que me passou as informações do Barão. E onde ele se encontrava com o Tony."

                menu:
                    "Tive que falar com várias pessoas.":


                        pass

                d "Incrível, [mc]. Nem eu sabia sobre essas reuniões com o Tony."

                na "Aquilo foi muito importante pra mim. Eu ganhei vários pontos."

                na "Então... eu sei o que você quer dizer."

                mc "Faz essa pela gente."

                na "Tudo bem. Vou fazer isso por você, [mc]."

                na "E vou lembrar disso. Pois vai chegar um dia que isso vai ser importante."

                mc "Hm?"

                d "Você conseguiu, [mc]!"

                mc "Sim... mas..."
            "Não tocar no assunto":


                "Não, deixa isso de lado. Melhor deixar elas duas se entenderem."

                "Vou ter que confiar na Diana."

                d "Amiga... eu não quero te cobrar... mas... um sonho pelo outro."

                "Do que ela tá falando?"

                na "O que eu posso falar depois dessa? Não imaginei que você iria usar essa cartada."

                d "É minha última chance."

                na "Ok, ok... eu tiro você daqui. Mas vai ser por você, Diana. Pelo que você conseguiu pra mim."

                d "Eu sabia que você não ia me deixar aqui, amiga."

                na "Sabia, né?"
    else:


        "Talvez se eu tivesse ajudado mais a Natasha... eu poderia ter algo pra trocar com ela agora."

        "Vou ter que confiar na Diana."

        d "Amiga... eu não quero te cobrar... mas... um sonho pelo outro."

        "Do que ela tá falando?"

        na "O que eu posso falar depois dessa? Não imaginei que você iria usar essa cartada."

        d "É minha última chance."

        na "Ok, ok... eu tiro você daqui. Mas vai ser por você, Diana. Pelo que você conseguiu pra mim."

        d "Eu sabia que você não ia me deixar aqui, amiga."

        na "Sabia, né?"

    menu:
        "Como ela vai tirar a gente da cidade assim? O Tony vai atrás da gente até no inferno.":


            pass

    na "Eu vou usar o avião do prefeito."

    mc "Como é?!"

    na "Eu sou a secretária dele. Eu faço isso todo o tempo. Ninguém vai suspeitar logo de cara."

    d "[na]... como você vai explicar isso pra eles depois?"

    mc "Verdade! Quando eles perceberem que a Diana sumiu!"

    na "Não se preocupem comigo. Se preocupem com vocês."

    na "Se vocês não derem o fora agora, o Barão vai acabar com os dois. E nem o prefeito vai poder ajudar."

    d "Eu sei. Nossa única chance é muito longe deste lugar. Mas também não quero te prejudicar."

    na "Eu decidi que eu vou te ajudar. Quer que eu volte atrás?"

    menu:
        "Ela tá certa, Diana. A gente precisa dessa ajuda.":


            d "Eu sei..."
        "Fico preocupado com você, Natasha.":


            na "Já falei que vocês precisam mais do que eu."

            mc "Mas o que eles vão fazer com você se eles descobrirem?"

            na "Descobrir o quê? Que eu ajudei uma sacerdotisa? Esse é meu trabalho também."

            d "Sacerdotisa... do que você tá falando?"

            na "Esquece."

    na "Então vem. O carro que eu uso com o Donatello deve tá no estacionamento. Temos que sair correndo."

    "Eu vou pegar um avião pra longe da cidade?"

    "É o único jeito agora?"

    d "Natasha... espera."

    na "Que foi? A gente não tem tempo."

    d "Eu preciso falar com o [mc]."

    na "Eu vou preparar o carro. Não demorem."

    d "Obrigada."

    scene black with dissolve

    scene diana7_img52 with Dissolve(1.0)

    pause

    if diana_namoro:

        mc "O que foi, amor? A gente não tem tempo."

        d "Eu sei, lindo."
    else:


        mc "Que foi, Diana? O tempo."

        d "Eu sei..."

    d "Mas eu não posso decidir isso por você."

    d "Eu quero você em segurança, mas não quero mudar sua vida."

    d "Você sabe do que eu tô falando, né?"

    menu:
        "Sobre a gente pegar o avião e sumir daqui...":


            pass

    d "Sim..."

    d "Se você não tivesse publicado o vídeo, nada disso taria acontecendo."

    d "Foi seu vídeo que tirou eles daqui. Que abriu essa porta pra mim."

    d "Mas agora você é um alvo. Eles vão querer se vingar de você."

    mc "Eu sei... na hora eu só consegui pensar que não era certo todo mundo virando as costas pra você."

    mc "No fundo eu sabia que podia dar uma merda muito grande pra mim, mas eu decidi fazer isso do mesmo jeito."

    d "Meu peso foi grande demais pra você, [mc]."

    d "Eu tô arriscando tudo pela minha liberdade. Só que você não ganha nada aqui."

    d "Além de mim, é claro."

    mc "[d]..."

    d "Meu sonho é que você venha comigo. Pegue o avião para outro lugar do meu lado. Uma nova vida. Longe de tudo isso."

    mc "Deixar tudo pra trás..."

    d "Sei que não é justo pedir isso pra você. Mas existe outra alternativa agora?"

    d "Você vai ficar aqui e lidar com esses malditos? Com esses inescrupulosos? Imagina o que eles podem fazer com você?"

    if diana_namoro:

        d "Você é meu namorado. O amor da minha vida."

        d "E depois de hoje eu tenho certeza disso. E eu quero viver do seu lado pra sempre."

        d "Não quero te perder pra eles."
    else:


        d "Nós vivemos tantas coisas juntos, [mc]..."

        d "E não tenho como esconder isso agora de você."

        mc "Do que você tá falando?"

        d "Quando você resolveu mandar aquele vídeo e arriscar tudo por mim..."

        d "É alguém assim que eu quero do meu lado."

        mc "Diana... você tá falando..."

        "Até agora eu a Diana fomos amigos... mas sempre achei ela uma mulher incrível."

        "Requintada, adulta, sensual, elegante, educada... talvez a mulher mais completa que eu encontrei aqui."

        "Ela disse que quer alguém assim do lado dela. É minha chance."

        "É minha última chance de ficar com ela."

        menu:
            "Eu também quero você do meu lado. Namora comigo.":


                $ diana_namoro = True

                d "Sério, [mc]? Você também me quer?"

                mc "Eu te quero. Você é a mulher mais incrível que eu convivi aqui."

                mc "Quero viver tudo com você. Ser seu homem."

                d "E eu vou ser sua mulher."

                d "Então você vai vir comigo mesmo? A gente vai ser um casal londe daqui?"

                d "Uma nova vida! Só eu e você!"
            "Nossa amizade sempre foi o que eu mais gostei.":


                d "Você realmente não sente algo mais por mim, né?"

                mc "Não. Você é incrível. Mas sempre vai ser uma grande amiga."

                d "Eu só me apaixono por quem não quer nada comigo. As duas vezes."

                mc "Diana... você sempre vai ter minha amizade. Ainda mais se a gente acabar dando o fora daqui juntos."

        d "Vai ser muito importante pra mim ter você comigo."

        mc "Pra mim também. A gente vai ter que confiar um no outro pra sobreviver lá fora."

        d "E então? Você vai comigo?"

    "Viajar pra fora... ficar um tempo em outra cidade, talvez outro país..."

    "Abandonar tudo o que eu tenho aqui e ir com a Diana?"

    "Ou ficar aqui e encarar esses malditos? Se eu ficar... a morte é praticamente certa."

    "Mas... como eu vou viver deixando tudo pra trás também? E agora?"

    "Preciso de mais tempo pra pensar."

    menu:
        "A Natasha tá esprando a gente. Vamos.":


            pass

    d "Tudo bem. Mas, querido..."

    mc "Vou decidir o que fazer no carro. Preciso de mais um tempo."

    d "Eu entendo. Então vamos."

    mc "Vamos!"

    if sayuri_final3:

        scene diana7_img53 with vpunch

        s "Onde vocês estão indo?!"

        mc "S-sayuri?!"

        s "O Barão tá com o Marco. O prefeito foi com o Tony. E eu não vejo a Zaza... Só tem eu aqui agora."

        s "Repito. Pra onde vocês estão indo?"

        d "Por favor! Nós temos que sair daqui!"

        s "Senhorita Diana, sei que não nos conhecemos, por isso entendo se você tiver dúvidas sobre mim."

        s "Entretanto, eu tenho que lhe dizer: você significa muito para todos nós."

        s "Infelizmente, não posso deixar que a senhorita vá assim."

        mc "[s]!"

        s "Me desculpe, [mc]. Eu... não posso..."

        "Por que a Sayuri tá falando assim?!"

        s "Veja, não concordo nem um pouco com a forma que o Barão lida com você."

        s "Quando assumi a Cidade Chinesa, uma das coisas que eu me propuz foi aliviar as relações."

        s "E ele, pelo contrário, acha que é seu dono. O que não é verdade."

        menu:
            "Eu sabia que você tinha um bom coração, Sayuri.":


                s "O certo é o certo."
            "O Barão nunca vai mudar! A gente tem que sair daquí!":


                s "Não estamos falando do Barão. Eu sei que ele é desnecessário."

        s "Mesmo assim, a Diana é importante demais. Eu estaria sendo negligente se deixasse ela sair assim."

        mc "Sayuri... você não entende..."

        s "Vocês que não entendem. Existem coisas maiores do que todos nós acontecendo aqui."

        "Ela não vai deixar a gente passar assim..."

        "Será que ela não vê que a Diana tá sofrendo?!"

        "Sayuri... aquela garota meiga que eu conheci não existe mais?"

        d "Você tem razão, senhorita. Eu não entendo."

        d "O que eu sei é que nós estamos falando da MINHA vida aqui. E, pra mim, minha vida vem em primeiro lugar."

        d "Não importa o quão grande vocês acham que qualquer coisa é. Pra mim, MINHA VIDA é o que importa."

        s "Às vezes precisamos nos sacrificar pelo bem dos outros, senhorita Diana."

        d "Droga! Você não entende?! Eu não quero! Eu quero minha liberdade!"

        mc "Sayuri..."

        "Do que ela tá falando? Por que a Diana continuar aqui é tão importante assim?"

        if sacerdotisas >= 2:

            "Tem a ver com o que eu li sobre aquelas sacerdotisas?"

            "Quando eu tava falando com a Carol na Biblioteca..."

            "Aquela foto das garotas de quimôno... por que tudo isso parece tão suspeito?"

            "Parece que alguém chamou a Diana assim uma hora. Ou tô inventando oisso?"

        "A Sayuri sempre foi uma mulher muito inteligente. Se ela tá falando... talvez ela tenha razão."

        "Não... eu vou abandonar a Diana agora?"

        "Merda... o que eu faço?"

        label diana7_menu3:

            pass

        menu:
            "Não! Vocês não podem arruinar a vida da Diana pelos seus planos!":


                pass
            "A Sayuri tem razão, Diana. Vamos cancelar tudo.":


                p "Este caminho ainda não está disponível nesta atualização."

                p "Para caprichar bastante em cada final, o RB preferiu se dedicar totalmente a um caminho antes de fazer os outros."

                p "Mês que vem você poderá escolher esta opção e ver os outros finais da [d]!"

                p "Veja todos os finais para juntar os pedaços do grande mistério e descobrir todos os caminhos!"

                p "Não esqueça de ver quais finais você já conseguiu olhando no menu e no ícone do personagem."

                jump diana7_menu3

        mc "Sayuri... você lembra quando tudo começou? Quando a gente se conheceu?"

        scene black with dissolve

        scene diana7_img54 with Dissolve(1.0)

        s "S-sim... lá no... templo."

        mc "Sim. Você era outra pessoa lá."

        s "Eu era."

        mc "Você mudou, você cresceu. Hoje você é uma mulher muito mais segura, muito mais firme."

        s "Obrigada."

        mc "Mas você não é só isso. Pelo menos não foi assim que eu te via."

        s "O que você quer dizer?"

        mc "Você sempre foi uma mulher preocupada com a irmã, com sua comunidade."

        mc "Com um grande senso de dever, mas com uma gentileza honesta também."

        s "Eu sempre senti que você me via de verdade, [mc]. Me via e me ouvia."

        s "Eu te disse. Você foi tão importante pra minha mudança. Eu sou muito agradecida."

        menu:
            "Se você se sente assim, então faça uma por mim. Deixa a gente ir sem falar pra ninguém.":


                pass

        s "Você... quer que eu abandone minha responsabilidade por você?"

        mc "Você lembra o que aconteceu na Cidade Chinesa. A Mestra me atacou no rio."

        s "Sim..."

        mc "Eu poderia ter ido atrás de mudar tudo naquele lugar. Mas eu resolvi confiar em vocês."

        mc "Que você deixaria tudo diferente. O próprio Bao disse isso pra mim. Pra aceitar vocês."

        mc "Se eu tivesse acabado com você e a Mestra você não taria aqui."

        s "Tem toda razão. Você quer cobrar lealdade de mim agora?"

        menu:
            "Sim. Eu deixei você lá. Agora você me deixa sair também.":


                $ renpy.block_rollback()

                $ sayuri_cobrou = True

                s "Entendo. Então considere minha dívida paga."

                mc "Você vai deixar a gente sair sem avisar eles?"
            "Não. Só quero que confie em mim.":


                $ renpy.block_rollback()

                s "Você continua com esse jeito, [mc]... você acredita na gente..."

                mc "Eu sei que você vai fazer o certo."

                s "O certo nem sempre é o que você acha. Não vou fazer pelo que você acha 'certo'. Mas por você..."

                mc "Não só por mim. Pensa na Diana. Ela é uma mulher presa nesse destino igual você."

                mc "Mas ela não quer seguir o caminho que você seguiu. O sonho dela é outro."

                s "..."

        s "Vão."

        d "É verdade?!"

        s "Se você quer fugir das suas responsabilidades, e ele quer ser indulgente com isso, eu posso fechar os olhos."

        s "O [mc] tinha poder para mudar tudo na Cidade Chinesa e acabar com nosso poder. Mas ele ficou do nosso lado."

        s "Eu vou usar o meu poder pra ajudar vocês agora."

        d "Obrigada, senhorita. Minha responsabilidade é com meu sonho. Talvez eu não tenha sua força, mas este é o caminho que escolhi."

        s "Desejo que seja feliz."

        if diana_namoro:

            s "Mesmo que seja do lado dele."

            mc "E-eu..."

            d "Só posso agradecer."

        d "Vamos, [mc]?"

        mc "S-sim. Muito obrigado, [s]."

        s "Vamos ver se nosso destino ainda vai se cruzar."

        s "Algo me diz que você ainda tem algo a fazer nesta cidade, [mc]."

        mc "O-ok! Talvez não seja um adeus. Seja um até logo!"

    scene diana7_img55 with vpunch

    pause

    d "Me segue, [mc]. Eu sei onde é o estacionamento!"

    mc "Tá legal!"

    mc "A Natasha vai tá esperando a gente?!"

    d "Ela tem um carro que é dela!"

    d "A gente tem que sair sem ninguém ver a gente!"

    if d7_faca == 2:

        mc "O Barão não vai poder fazer mais nada. Não depois do que eu fiz com ele."

        d "Aquela faca. Era a que eu tinha pego..."

        mc "Você desistiu... mas eu fiz o que você não conseguiu."

        d "Você pode ter jogado sua vida fora por isso. Tudo isso foi por mim?"

        menu:
            "Sim. Você merecia vingança.":


                pass
            "Não. Ele mereceu pelo que ele fez.":


                mc "Não carregue essa culpa. Esse era um assunto que EU tinha que resolver com ele."

        d "Não imaginei que você tinha esse tipo de..."

        mc "Sei do que você tá falando. Mas quando a gente vê certas coisas... passa por certas coisas... a gente muda."

        d "Eu vou cuidar de você, [mc]."

        mc "..."

        d "E obrigada. Obrigada por tudo o que tá fazendo."
    else:


        mc "Se o Marco ou o Tony pegar a gente!"

    scene black with dissolve

    d "Tamo chegando!"

    mc "Ela tá ali!"

    d "A gente vai conseguir!"

    na "Subam!"

    play sound som_carro

    pause 2.0

    scene diana7_img56 with Dissolve(1.0)

    mc "Tamo no centro! Você tirou a gente da ilha!"

    d "Obrigada amiga! E agora?"

    na "Tá tudo certo. Vou levar vocês pro aeroporto da prefeitura e o avião vai tá esperando."

    mc "No meio da cidade?!"

    na "Sim. É especial para assuntos... especiais."

    "Será que é aquele que eu fui com a Pri?"

    na "Vocês vão dar o fora daqui. Depois de pousar, vocês pegam um Uber, um ônibus, sei lá, e vão pra um lugar que ninguém saiba."

    menu:
        "E você, Natasha? Como vai ficar?":


            pass

    na "Já falei pra não se preocupar comigo. Eu vou segurar as pontas aqui com o chefe."

    d "Vou te dever essa por toda a vida, querida. Mas sinto que não poderei pagar nunca."

    na "Pague sendo feliz. E nunca mais voltando pra capital. Se você voltar, eles vão te prender pior do que agora."

    menu:
        "Natasha... por que você tá fazendo isso? Você não trabalha pro prefeito?":


            na "Sim. Eu trabalho."

            mc "Então... por que... aposto que ele não vai gostar muito de ver a Diana fugindo."

            na "Eu tenho uma dívida com a Diana. Só quero pagar o que eu devo de uma vez por todas."

            d "Você faz porque eu te dei o que você tem hoje ou por que no fundo você ainda me ama?"

            na "Eu nunca te amei."

            d "Infelizmente... eu acredito nisso."

            mc "Vocês..."

            d "Sim. Nós tivemos um caso."

            if diana_namoro:

                d "Mas foi antes de começarmos nosso relacionamento, querido. São coisas do passado."

                menu:
                    "Tudo bem.":


                        mc "Eu só... nunca ia imaginar isso."
                    "Você podia ter me contado.":


                        d "Não queria reviver fantasmas do passado."

                if na1_beijo or na3_beijo or na3_banheira or natasha_e4 == "seducao":

                    "B-bom... eu e a Natasha também tivemos nosso rolo..."

                    "Mas seria melhor se ela não falasse nada... principalmente porque eu e a Diana... ai ai..."

                    na "Bom... tem algo que a Diana precisa saber também."

                    d "Hm?"

                    mc "É..."

                    menu:
                        "A gente não tem cabeça pra falar disso agora!":


                            pass

                    na "Verdade."

                    "Ufa..."

                    na "A verdade é que eu e o [mc] também tivemos nosso caso."

                    d "Não creio! Vocês?!"

                    mc "S-sim!"

                    d "Quero saber dessa história!"

                    menu:
                        "Bom....":


                            pass

                    na "Nossos casos também também foram no passado... não foi?"

                    mc "É..."

                    "Acho que eu já tava com a Diana quando eu fiquei com a Natasha..."

                    "Ela podia foder tudo comigo agora. Graças a Deus ela fez a boa..."

            na "Enfim... é isso. Essa daí vai acabar me matando, mas é o mínimo que eu podia fazer."

            d "Você fez muito mais do que eu podia esperar."
        "Vamos deixar o papo de lado e correr!":


            na "Excelente ideia!"

    d "Esta é a última vez que eu vejo as luzes da ilha. Adeus, capital!"

    mc "..."

    d "Você tá pronto, [mc]? Pra dar adeus?"

    "É agora ou nunca."

    "Eu vou com a Diana pra fora. Deixo tudo pra trás e vou ter uma vida nova."

    "Ou fico aqui e enfrento as consequências de ter desafiado o grupo do Tony."

    "Se eu quiser ficar com a Diana, eu tenho que ir com ela. Ela nunca mais vai poder voltar aqui."

    "Eu posso ser feliz com ela lá. E descobrir uma nova vida."

    "Ou damos adeus aqui. E eu torço pra que ela seja feliz e continuo lutando sendo um paparazzo."

    "Seja qual for minha escolha... eu sei que minha vida não será mais a mesma quando o sol nascer de novo."

    na "Estamos chegando! Você tem que decidir, [mc]!"

    label diana_menu4:

        pass

    menu:

        "Eu quero continuar namorando a Diana. Vamos viver longe deste inferno." if diana_namoro:

            mc "Eu não quero continuar aqui sem a Diana. Eu vou com ela."

            scene black with dissolve

            scene diana7_img57 with Dissolve(1.0)

            d "Você tá falando sério, meu amor?"

            mc "Claro que eu tô. Eu quero viver com você. Pra sempre."

            d "Você sabe que a gente vai ter que ralar, né? Recomeçar nossas vidas do zero em outro lugar."

            mc "Eu sei. Mas eu tô pronto. E dessa vez eu vou ter você do meu lado."

            d "Eu prometo que eu vou tá com você em tudo."

            mc "E eu com você."

            na "Lindas juras de amor. Quero ver na prática."

            mc "Parece que alguém tá com ciúmes."

            d "De mim ou de você?"

            mc "Haha..."

            na "Pelo amor..."

            jump diana_final1

        "Eu vou fugir com a Diana. É a única forma de eu viver." if not diana_namoro:

            mc "Não tem mais nada nesta cidade pra mim."

            scene black with dissolve

            scene diana7_img57 with Dissolve(1.0)

            mc "Vamos escapar dessa juntos."

            d "Amigos de viagem?"

            na "Parem de brincar. Vocês tão correndo risco de verdade."

            d "Mas nós temos você."

            na "Mimados."

            mc "Haha..."

            na "Pelo amor..."

            jump diana_final1
        "Eu vou ficar. Eu ainda tenho coisas pra fazer na cidade.":


            jump diana_final2





label diana_final1:

    $ diana_final1 = True


    scene black with dissolve

    scene diana7_img58 with Dissolve(1.0)

    na "O avião vai decolar assim que vocês entrarem."

    d "A gente nunca mais vai se ver, né, querida?"

    na "Não."

    d "Você tem certeza do que você tá fazendo? Não prefere fugir conosco?"

    na "Diana... você já me falou isso outras vezes. E o que eu respondo?"

    d "Que você tá onde sempre quis..."

    na "Exatamente."

    d "Do lado desses idiotas."

    na "Os idiotas que transformaram a cidade no que ela é hoje. Uma das capitais econômicas do mundo."

    na "Eu sei que o Barão não te tratou como devia. E eu nunca vou perdoar ele por isso."

    d "Eu sei. Não precisa se justificar."

    na "Mas o prefeito... ele não é assim. Ele é um homem sério."

    na "E eu vou ajudar ele a manter a cidade no caminho certo. E se desfazer dessas pessoas ruins, iguais ao Barão."

    d "Querida... eu não sei se você sonha demais ou só tá se enganando."

    menu:
        "A Diana tem razão. Fruta podre não dá pra ficar saudável de novo.":


            na "Vocês não entendem..."
        "A Natasha tá certa. Ela vai dar um jeito de acabar com isso.":


            mc "Isso não nos diz respeito mais, Diana."

            d "Você tá certo... é que ela... tudo bem..."

    mc "Nós temos que ir. O avião tá esperando."

    d "Adeus, amiga."

    na "Adeus. Viva seu sonho de liberdade."

    d "Eu vou. Aproveitar cada dia."

    if diana_namoro:

        d "Do lado do meu homem."
    else:


        d "E eu vou ter meu amigo pra me ajudar."

    mc "Pode contar comigo. Eu vou cuidar dela, Natasha."

    na "Agora vão. Adeus!"

    d "Tchau!"

    scene black with dissolve

    scene diana7_img59 with Dissolve(1.0)

    d "Ainda não acredito que eu consegui. Que eu tô livre."

    menu:
        "Também acho! A gente conseguiu!":


            d "Né?! Não foi fácil! Mas agora eles não pegam mais a gente!"
        "Este avião é deles. Quem garante que...":


            d "Você acha?"

            mc "Melhor a gente comemorar só quando a gente tiver longe daqui."

            d "Tem razão... mas não consigo deixar de sentir uma pontada de liberdade."

    mc "Eu nunca imaginei que esta noite eu ia deixar tudo pra trás."

    mc "Minha carreira de paparazzo, a ilha das celebridades, a capital... todas as pessoas que conheci..."

    d "Está triste?"

    mc "Triste? Acho que não. Nostálgico."

    d "Você foi a rocha em que eu me escorei para conseguir me libertar, [mc]."

    if diana_namoro:

        d "Se não fosse seu amor. Se você não tivesse comigo, eu nunca faria isso."

        mc "De todas as mulheres que eu conheci. Seu amor foi o mais sincero, Diana."

        mc "Eu nunca poderia deixar você lá, sofrendo daquele jeito."

    mc "Se eu voltasse pra aquele momento 100 vezes, eu mandaria o vídeo 100 vezes."

    mc "Essa ilha me ensinou que muitas vezes não existe certo ou errado. Que as coisas são mais complexas do que a gente pensa."

    mc "Mas ainda existem decisões nas nossas vidas que, no fundo, temos certeza do que temos que fazer. E essa era uma delas."

    mc "Virar o rosto pra você igual os outros... como eu ia conseguir dormir à noite?"

    d "Esse é o homem que você é, [mc]. O homem como poucos no mundo."

    mc "Valeu."

    menu:
        "Adeus, ilha. Adeus, capital. Eu nunca vou esquecer o que eu vivi aqui. Mas agora é hora de uma nova vida!":


            pass

    play sound som_aviao

    scene black with Dissolve(3.0)

    pause

    "Agora sou eu e a Diana numa nova vida."

    window hide

    pause

    scene diana7_img60 with Dissolve(1.0)

    "Eu e a Diana aterrisamos em outro estado. Ficamos lá por um dia e pegamos outro avião. Dessa vez pra outro continente."

    "Seria impossível alguém nos encontrar."

    "Mesmo com o poder do prefeito e da polícia corrupta da capital, eles não teriam poder em outro país."

    "Não éramos procurados, nosso passaporte tava legalizado. Não tinha razão pra termos problemas."

    "E assim... com tranquilidade... nossos dias passaram."

    "Chega daquela loucura. Daquele sofrimento. Agora era curtir a vida ao lado de alguém que gostava de mim."

    scene black with Dissolve(3.0)

    pause







    play sound som_4_fadolandia

    pause 1.0

    scene diana7_img61 with Dissolve(1.0)

    d "O que você tá achando?"

    mc "É diferente. Sair de todo aquele rolo pra viver uma vida tranquila."

    d "Melhor ou pior?"

    if not diana_namoro:

        "Eu e a Diana não tá namorando, mas a gente tá cada vez mais próximos."

        "Acho que pode rolar alguma coisa logo logo..."

    menu:
        "Eu sempre quis uma vida tranquilo do lado de alguém especial.":


            d "Eu sinto o mesmo."

            d "E vô tá sempre do teu lado, contanto que você me queira."

            mc "Eu sempre vou querer."
        "Acho que eu preferia o inferno da capital.":


            d "Hm..."

            mc "Mas não se sinta culpada. Eu sou adulto. Fiz a escolha que eu queria fazer."

            d "Obrigada por falar isso."

            d "E quem sabe... a gente pode voltar?"

            mc "Você gostaria?"

    d "Talvez daqui um tempo... quando a poeira abaixar, a gente podia tentar voltar."

    mc "Depois do que aconteceu no Cassino não acho que é uma boa."

    d "Mesmo que demore uns anos... mas o Basílio não vai ser prefeito pra sempre."

    mc "Isso é..."

    d "Não me entenda errado. Eu me sinto tão bem longe daquilo."

    mc "Você tá sorrindo bem mais aqui. Sorriu mais vezes nesses meses que em tudo o que eu vi lá na capital."

    d "Você tá reparando bastante em mim então..."

    mc "Eu tô."

    d "É... talvez eu realmente esteja sorrindo de verdade."

    d "Mas eu falo por você."

    d "Você gostaria de voltar? Daqui uns anos?"

    menu:
        "Eu... acho que sim.":


            mc "Por pior que a capital fosse, eu curtia a loucura."

            d "A nossa capital era o coração do mundo, como algumas pessoas falaram."

            mc "É... não é à toa."
        "Não. Nossa vida é aqui agora. Daqui pra frente!":


            d "Verdade?"

            mc "Você gostaria?"

            d "Eu gostaria de ser uma grande cantora. Atingir o mundo."

            d "E com certeza as ligações da capital iam me ajudar nisso."

    d "Eu vou fazer minha carreira de uma forma ou de outra."

    mc "Tenho que falar que você tá fazendo um bom trabalho nos barzinhos daqui. Eu tô adorando ver você cantar."

    d "Às vezes você é meu único público."

    mc "Isso é..."

    d "Mas é todo o público que conta."

    mc "Com esse sorriso, e trabalho duro, você vai chegar no topo sem precisar daquelas pessoas."

    mc "E eu vou aproveitar da vida boa com teu dinheiro."

    d "Tudo é nosso. A voz é minha, mas o espírito é seu."

    d "Aliás, vou me preparar pro show de hoje. O que quer dizer que provavelmente vou me preparar pra você."

    mc "Haha... tô ansioso."

    menu:
        "Eu vou andar mais um pouco. Logo logo tô em casa.":


            pass

    d "Tá bom."

    if diana_namoro:

        d "E depois do show a comemoração?"

        mc "Daquele jeitinho que o pai gosta."

        d "Hmm..."

    d "Beijo."

    mc "Beijo."

    scene black with dissolve

    play sound som_4_fadolandia

    pause 1.0

    scene diana7_img61 with Dissolve(1.0)

    "Minha vida aqui vai ser bem diferente. Mas com a Diana, tenho certeza que cada dia vai ser incrível."

    "Espero que dê tudo certo com a Sofia."

    "Ela acabou ficando lá com bomba nas mãos. Devia ter pedido pra Natasha proteger ela."

    "Se bem que eu que gravei, eu que mandei. Talvez eles nem saibam que foi ela que postou. Tomara."

    "Apesar que as coisas que eu tinha lá não interferem mais. Fico pensando a cara do chefe com a minha demissão."

    "Tomara que a revista sobreviva sem as minhas pautas."

    "Adeus, pessoal. Foi muito bom tudo o que a gente viveu juntos!"

    "Eu nunca vou esquecer vocês! De verdade!{nw}"

    play sound som_17_tiro

    scene red with vpunch

    mc "AI!"

    "???" "Calado!"

    "Tá me puxando. Que merda é essa! O que tá acontecendo?!"

    mc "Eu vou gritar!"

    play sound som_hit

    scene black with hpunch

    mc "AAHHH!!!"

    "???" "Dá mais um pio e eu acabo contigo, maninho."

    "Essa voz!"

    play sound som_hit

    scene diana7_img62 with vpunch

    pause

    mc "Akh!"

    mc "MARCO!"

    mar "E aí?"

    "Não! Aqui?!"

    "A gente tá em outro país, em outro continente, cara!"

    "Como esse filha da puta me achou!"

    menu:
        "Não é possível! Como encontraram a gente aqui!?":


            mar "O chefe me mandou ir atrás de você."

            mc "Não é tão fácil assim!"

            mar "Nada que umas ligações do prefeito junto aos órgãos públicos de transporte não resolvessem."

            mar "E você usar nosso avião... não ajudou."

            mc "Merda!"

            "Foi ideia da Natasha!"
        "O que você vai fazer comigo?!":


            mc "Você não veio aqui matar a saudades, né?"

    mc "Eu tô fodido!"

    mar "Com certeza, maninho. Você mexeu com as pessoas erradas."

    mc "Você viu o que eles fizeram com a Diana! Eu só salvei ela!"

    mc "Era pra esse ser o final bom!"

    mar "Não tem final bom pra você nessa história, amigo."

    mc "Marco..."

    mar "O Tony foi bem claro. A gente precisa manter a mensagem de que se você mexe com o esquema, o esquema mexe contigo de volta."

    menu:
        "Vai me matar aqui? A sangue frio?":


            pass

    mar "Foi pra isso que eu vim."

    mc "Filho da puta... você é igual eles!"

    mar "Lembra do viaduto?"

    mc "Viaduto?"

    mar "É. Quando você conheceu a Priscila Fontinelli. O Gustav me mandou apagar tu. Ele devia tá com ciúmes."

    mc "Você não me matou aquela vez..."

    mar "Aquela vez eu te disse que eu não tinha nada contra você. Eu apenas sigo ordens. É o meu trabalho."

    mc "Você não precisa fazer a coisa errada por causa deles! Você também tem uma cabeça!"

    mar "Errado?"

    mc "É! Tirar uma vida não é certo!"

    mar "Sabe, maninho... acho que não parece olhando pra mim, mas eu acredito em Deus."

    menu:
        "Você religioso? Tá brincando?":


            pass

    mar "O chefe disse que tudo tem um motivo no mundo. Cada coisa tem o seu lugar."

    mar "Ele contou uma passagem da Bíblia. Os italianos adoram esse livro. Ele falou para eu decorar."

    mar "Ezequiel 25:17."

    mar "'O caminho do justo está cercado por todos os lados pelas iniquidades dos egoístas e pela tirania dos perversos.'"

    mar "'Bendito é aquele que, em nome da caridade, pastoreia os fracos pelo vale das trevas, pois ele é o protetor de seus irmãos e o salvador dos filhos perdidos.'"

    mar "'E Eu atacarei com vingança e raiva furiosa aqueles que tentam envenenar e destruir meus irmãos.'"

    mar "'E você saberá: meu nome é o Senhor quando minha vingança cair sobre ti.'"

    mc "Você pastoreia os fracos pelo vale das trevas? Você acha que mata em nome de Deus? Nem você acredita nisso!"

    mar "O chefe que disse. Que eu poderia matar por algo melhor."

    mar "Eu nem queria te matar, maninho. Mas você zoou os cabeça e agora o chefe quer sua cabeça de exemplo."

    mar "Adeus."

    menu:
        "Vai logo! Senta o dedo nessa porra, pau mandado!":


            jump diana7_final_morre
        "Ele só quer que eu morra! Não preciso morrer de verdade! Por favor!":


            mar "Que papinho é esse, hein?"

            scene black with dissolve

            scene diana7_img63 with Dissolve(1.0)

            mc "O Tony nunca vai vir aqui! Nem o prefeito!"

            mc "É só você falar que eu morri! Eu prometo que eu NUNCA mais apareço na ilha!"

            mar "Hmm..."

            mc "Marco! Eu nunca fiz nada pra você! Por favor!"

    mar "Faz sentido, maninho."

    mar "Eu não preciso deixar pistas. E você desaparece de qualquer forma."

    mar "Talvez seja até melhor."

    mc "Eu disse!"

    mar "Mas se você voltar... ele vai saber que eu menti. E daí ele me mata. Nada feito."

    mar "Adeus."

    mc "Não!"

    menu:
        "Eu juro que não volto! Eu morreria também!":


            pass

    mar "Isso é... se você voltar lá, com certeza o Tony te passa."

    mc "Eu não tenho nada mais lá. Vou viver aqui com a Diana. Podemos até sumir daqui também."

    mar "Não. Pelo contrário. Vocês vão ficar aqui. Você vai garantir que a Diana vai ficar aqui."

    mc "C-combinado."

    mar "Na hora certa nós vamos chamar ela. E é bom que ela não suma."

    mc "Que hora certa?"

    mar "Não sei também, maninho. Mas é o que o chefe me falou. Ele mandou eu levar a Diana."

    mar "Mas a gente sabe que ela vai dar trabalho. Ela vai viver muito melhor aqui, achando que tá livre."

    mc "Com certeza."

    mar "Então você vai garantir que ela não desapareça. Você vai trabalhar pra gente."

    mc "Mesmo depois de tudo... eu ainda vou acabar me juntando a vocês?"

    mar "Você quer viver? É sua única escolha."

    "Vigiar a Diana pra eles... em troca da minha vida. É como se a Diana nunca fosse livre de verdade."

    "E dessa vez eu que vou tá prendendo ela."

    "Ou digo não a tudo isso. E pago com a minha vida?"

    menu:
        "Pode contar comigo. Eu vou vigiar ela pra vocês.":


            mar "Isso aí. Te deixar vivo vai acabar ajudando."

            mc "Merda..."
        "Eu não vou fazer parte dessa merda! Se quiser me mata!":


            mar "Eu sabia que você era um rato."

            mc "MARCO! NÃO!"

            jump diana7_final_morre
        "Mas como você vai saber que a gente tá aqui?":


            mar "Será que é melhor eu te matar e arrastar ela pelo cabelo?"

            mc "N-NÃO!!!"

            mar "Ok. Além de que o prefeito desta cidade já tá sabendo de tudo."

            mc "C-como..."

            mar "Política, dinheiro... eles sempre tão de mãos dadas, maninho."

            mc "É o que parece."

            menu:
                "Pode contar comigo. Eu vou vigiar ela pra vocês.":


                    mar "Isso aí. Te deixar vivo vai acabar ajudando."

                    mc "Merda..."

    scene black with dissolve

    scene diana7_img64 with Dissolve(1.0)

    mar "Então tá. Ficamos assim. Você fica de olho nela pra mim. E você NUNCA mais volta pra capital."

    mar "Se a Diana quiser voltar, você pode deixar ela. Mas você... nah nah... nunca mais, entendeu?"

    menu:
        "Entendi. Vocês nunca mais vão me ver.":


            pass

    mar "Legal. Até mais, maninho."

    "Eu nunca mais vou voltar... será que eu pergunto o que aconteceu com o pessoal?"

    "Pode ser minha última chance. Mas também... eu posso acabar sabendo o que eu não quero."

    menu:
        "Até mais, Marco. E valeu por me deixar viver.":


            pass
        "Marco... você só tá atrás de mim, né?":


            mar "Não. Tem a maninha da sua revista. Ela é a próxima da lista."

            mc "QUÊ?!"

            mar "Ela publicou o vídeo da Diana. E agora tá fazendo pergunta demais sobre você."

            mc "Não é possível..."

            mar "Isso não tem mais nada a ver com você, lembra? Cortar TODAS as relações com a capital."

            mar "Escuta aqui, maninho. Agora você é um de nós. Não quero ouvir um 'piu', entendeu?"

            mar "Se eu chegar lá e ela souber de algo..."

            mc "U-ugh..."

            "A Sofia... ela vai acabar morrendo pra ele. E ela só tem a mim."

            "Essa é uma escolha sem volta pra mim."

            menu:
                "Desculpa, Sofia. Mas entre minha vida e a sua, eu escolho a minha":


                    $ renpy.block_rollback()

                    mc "Eu decidi que vou viver."

                    mar "Excelente escolha."
                "Eu tenho que avisar a Sofia, não importa o que aconteça comigo":


                    $ renpy.block_rollback()

                    mar "Esse olhar. Eu sabia."

                    mc "NÃO! MARCO!"

                    jump diana7_final_morre

            mar "E a secretária... ela que arranjou o avião, não foi?"

            "O que adianta mentir agora?"

            menu:
                "Sim.":


                    pass

            mar "Muito bem. Nós já sabíamos."

            mar "Ela quis salvar a amiga. E acabou conseguindo. Mas pagou."

            mc "A Natasha também..."

    if d7_faca == 2:

        mar "Ah... e o Barão provavelmente não vai sobreviver. Você fez um estrago nele."

        mc "Filho da puta. Mereceu. Espero que agonize bastante antes de morrer."

        mar "Haha... não parecia que você tinha esse sangue frio."

        mc "Esse tipo de pessoa merece o que tá vindo pra eles."

        mar "Você vingou a cantora. Isso é certo. Bom..."

    mar "Aproveite a nova vida que você ganhou, maninho. Você e a cantora."

    mar "Porque era pra você ter morrido aqui e agora. E ela encarcerada novamente."

    mar "Alguns sacrifícios são necessários. Uma vida pela outra. Adeus."

    mc "Adeus..."

    "Desgraçados..."

    scene black with Dissolve(3.0)

    pause

    pause

    scene diana7_img65 with Dissolve(1.0)

    mc "Nós conquistamos nossa liberdade."

    mc "Talvez... talvez eu também tivesse preso. Pautas... fazendo coisas erradas... passando medo todo dia."

    mc "Fugimos daquela cidade maldita. Você... nem eu... precisamos mais daquilo tudo."

    d "Nós conseguimos, querido."

    if diana_namoro:

        d "Nosso amor nos salvou."

        mc "Sim, linda."
    else:


        d "Nossa amizade nos salvou."

        mc "Sim."

    "E o sacrifício daquelas pessoas..."

    "Sofia... eu tô aqui por sua causa."

    "Mesma coisa a Natasha. Que se sacrificou pela Diana."

    "Uma vida pela outra."

    mc "O que me resta é aproveitar essa vida que compraram pra gente."

    d "A gente que comprou, [mc]."

    mc "Sim. Vamos esquecer o passado e olhar pra frente."

    mc "Só eu e você."

    d "Sim."

    scene black with Dissolve(3.0)

    pause

    $ persistent.diana_final1 = True

    "{i}FIM{/i}"

    pause

    p rindo "Parabéns por chegar ao final... mas que finalzinho... hein?"

    p lecionando "Uma vida normal? Ao lado de uma única garota? Eu sei que ela é perfeita, mas uma só mesmo?"

    p "A vida é cheia de possibilidades. Por que você se colocaria em uma gaiola como essa?"

    p "Pensa em todas as mulheres e homens que você pode conhecer, todas as intensas emoções que te esperam."

    p "Quais outras dezenas de finais diferentes existem no seu futuro?"

    p rindo "Eu permito que você volte e tente outros destinos. Destinos que serão muito interessantes para você."

    p "Mas principalmente para mim."

    p "Aqui mesmo na sua relação com a Diana... existem tantas possibilidades. Não aceite qualquer uma!"

    p "Será que é possível salvar todas? Existe algo escondido?"

    p "Eu não posso te contar, mas talvez você possa encontrar."

    p "Vou continuar de olho em você, gato!"

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Parabéns! Você conquistou o Final 1 da Diana!{/b}"

    "{b}Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    scene white with dissolve

    $ renpy.full_restart()

label diana7_final_morre:

    $ renpy.block_rollback()

    play sound som_17_tiro

    scene red with hpunch

    "E-eu... vou morrer assim?!"

    scene black with Dissolve(2.0)

    p "Sério que você matou ele assim?"

    p "Essa morte vagabunda nem merece um final. Que decepção."

    p "E de raiva não vou te deixar voltar. Espero que você tenha salvado antes."

    p "Vamos ver quantas mais vezes você vai ter que escutar eu te falando isto."

    $ renpy.full_restart()

label diana_final2:

    $ diana_final2_pre = True

    if diana_namoro:

        d "Tá falando sério, amor?"

    scene black with dissolve

    scene diana7_img66 with Dissolve(1.0)

    if diana_namoro:

        mc "Sim, linda."

        mc "Não tem coisa que eu queria mais nessa vida que tá do seu lado. Você é meu amor."
    else:


        mc "Eu queria ser seu amigo nessa hora que você precisa."

    d "Então!"

    mc "Mas eu não posso só deixar tudo pra trás. Alguma coisa me impede."

    d "Você acha que seu destino tá ligado a este lugar imundo?"

    mc "Não sei se eu acredito em destino... mas tem coisa demais na minha mão aqui."

    mc "Não falo só de coisas..."

    d "..."

    na "..."

    menu:
        "Você me entende? Tenho que cuidar de outras pessoas.":


            pass

    d "Claro que eu entendo."

    d "Seria egoísmo demais querer que você carregue só o meu peso."

    d "Existem outras pessoas aqui que precisam de você tanto quanto eu."

    d "A Natasha é uma delas."

    na "Hmf... mais fácil ele vir chorando pro meu colo."

    d "Se vocês gostam de mim, não quero ver os dois brigando."

    na "O que você quiser, princesa."

    d "E você, [mc]? Promete que vai cuidar da Natasha pra mim? Promete que não vai deixar nada acontecer com ela?"

    "Meu Deus... prometer uma coisa dessas pra Diana assim?"

    "Mas dá pra negar um pedido assim numa hora dessas?"

    "Com certeza eu ganharia uns pontos com a Natasha... e poderia rolar algo depois..."

    "Imagina ficar com a Natasha?"

    if diana_namoro:

        "A Diana nem foi ainda e já tô pensando em trocar ela... qual seu problema, [mc]?"

    "Talvez valha a pena... o q-que eu tô pensando?"

    menu:
        "Claro. Vou proteger a Natasha. Pode ir tranquila. Pensa nas suas coisas.":


            $ d7_nat_prometeu = True

            d "Não tenho como agradecer."

            na "Hmm... querendo se fazer de homem, é?"

            mc "Haha... para com isso. Só quero que ela vá tranquila. E eu nunca ia deixar nada acontecer com você mesmo."

            na "O-obrigada..."
        "Isso é demais pra mim, Diana. Eu sou só um paparazzo.":


            d "Um paparazzo que me salvou do meu cativeiro."

            mc "Eu só segui seu plano. Você fez tudo."

    d "Por favor, faça o que tiver ao seu alcance."

    na "É hora de você pensar em você, sua boba. Não em mim. Eu vou ficar bem."

    na "O prefeito vai entender."

    d "Eu não teria tanta certeza, minha querida. Não passamos de peças descartáveis pra eles."

    menu:
        "Eu vi o que eles podem fazer com quem desafia eles...":


            pass

    na "Eu não sou como os outros. Eu conquistei meu lugar. Eu sou peça fundamental. Eles querendo ou não."

    d "Se você acha, amiga... fico mais tranquila."

    mc "..."

    na "Olhem lá!"

    scene black with dissolve

    scene diana7_img58 with Dissolve(1.0)

    na "O avião vai decolar assim que você entrar."

    mc "Cuidado, Natasha! A gente tá indo na contra mão!"

    na "Não temos tempo pra se preocupar com isso!"

    d "A gente nunca mais vai se ver, né, querida?"

    na "Não."

    d "Você tem certeza do que você tá fazendo? Não prefere fugir comigo? E você, [mc]? Tenho medo do que eles podem fazer."

    menu:
        "Eu vou dar meu jeito. Eu dei até hoje.":


            d "Incrível. Sua resiliência é de outro mundo, [mc]."

            na "Ou ele é só louco mesmo."

            mc "Provavelmente haha..."
        "Talvez desta vez eu precise de uma ajuda.":


            na "Com certeza. Você vai tá na lista deles."

            mc "Só não sei pra quem pedir ajuda..."

            d "Que perigo! Venha comigo, [mc]!"

            mc "Mesmo assim... correndo risco, minha vida tá aqui."

            d "Você é louco."

    d "E você, amiga?"

    na "Diana... você já me falou isso outras vezes. E o que eu respondo?"

    d "Que você tá onde sempre quis..."

    na "Exatamente."

    d "Do lado desses idiotas."

    na "Os idiotas que transformaram a cidade no que ela é hoje. Uma das capitais econômicas do mundo."

    na "Eu sei que o Barão não te tratou como devia. E eu nunca vou perdoar o cretino por isso."

    d "Eu sei. Não precisa se justificar."

    na "Mas o prefeito... ele não é assim. Ele é um homem sério."

    na "E eu vou ajudar ele a manter a cidade no caminho certo. E se desfazer dessas pessoas ruins, iguais ao Barão."

    d "Querida... eu não sei se você sonha demais ou só tá se enganando."

    menu:
        "A Diana tem razão. Fruta podre não dá pra ficar saudável de novo.":


            na "Vocês não entendem..."
        "A Natasha tá certa. Ela vai dar um jeito de acabar com isso.":


            mc "Você precisa pensar em como VOCÊ vai fugir."

            d "Você tá certo... é que ela... tudo bem..."

    mc "Você tem que ir, Diana. O avião tá esperando."

    if diana_namoro:

        d "Adeus, meu amor. Você é o namorado que eu sempre sonhei."

        mc "E se esse não for o fim? Eu ainda quero você, delícia."

        d "Essa esperança enche meu coração."
    else:


        d "Adeus, amigo. Nada disso teria acontecido sem sua ajuda."

    mc "Conta comigo. Sempre."

    d "Adeus, amiga."

    na "Adeus. Viva seu sonho de liberdade."

    d "Eu vou. Aproveitar cada dia."

    na "Agora vai. Adeus!"

    d "Tchau!"

    play sound som_aviao

    scene black with dissolve

    scene diana7_img67 with Dissolve(1.0)

    na "Lá vai ela... voa, passarinho."

    mc "Ela merece."

    na "Com certeza. A Diana tem um coração que é muito difícil de achar."

    mc "Sim..."

    na "Até parece alguém que eu conheço."

    mc "Hm?"

    na "Deixa pra lá."

    menu:
        "Eu queria saber como ela acabou no Cassino, nas mãos do Barão.":


            pass

    na "É uma história complicada. Se você tivesse do nosso lado você saberia provavelmente."

    mc "Você sabe?"

    na "Sim. Mas não tenho tempo pra te contar agora."

    scene black with dissolve

    scene diana7_img68 with Dissolve(1.0)

    na "Nós temos que pensar no que a gente vai fazer."

    na "Afinal, nós ajudamos ela a escapar das mãos do Barão."

    menu:
        "E eu que ainda divulguei o vídeo? Eu tô morto já.":


            pass

    na "Provavelmente."

    na "Você comprou briga com quem não podia, [mc]. Você é louco."

    menu:
        "Você ficou quietinha vendo ela se ferrar.":


            na "Eu sei que não é o que ela queria, mas ela o melhor pra ela só aceitar."

            mc "É o que você fiz. Eu não ia deixar a Diana lá."
        "Eu devia ter ficado quieto... ia envolver menos pessoas...":


            na "Agora é tarde demais."

    na "E no fim eu acabei entrando nesse rolo também."

    mc "Por quê?"

    na "Eu não podia ignorar tudo o que ela fez por mim."

    na "Sem ela, eu não estaria onde estou hoje."

    mc "E você gosta mesmo disso?"

    na "Enfim. A questão é que agora nós estamos na mira deles."

    na "E a sua situação é ainda muito pior. O Barão é um dos cabeças. Além de ser um maníaco desgraçado."

    na "Com certeza ele vem atrás de você."

    menu:

        "Se ele sobreviver à facada que eu dei nele." if d7_faca >= 2:

            na "Ainda tem isso... meu Deus..."

            na "O Marco levou ele pro hospital da ilha que é ali do lado."

            mc "Espero que ele nunca saia de lá."

            na "Você vai acabar na prisão assim."

            mc "Depois eu penso nisso."

        "Eu devia ter metido a peixeira nele." if d7_faca < 2:

            na "Tá louco?! Atentar contra a vida de um deles?!"

            mc "Não teria que me preocupar agora."

            na "Eu não contaria com isso."

    na "E eu consegui o avião pra ela... quando eles se derem conta disso..."

    na "Heh... que loucura que a gente se meteu hoje."

    if not d7_nat_prometeu:

        "Tô sentindo que tá rolando um clima..."

        "Se eu tivesse prometido que ia proteger ela... acho que conseguia mandar uma cantada bem barata agora."

        "Fazer o quê..."

        menu:
            "Melhor a gente voltar logo.":


                pass
    else:


        scene black with dissolve

        scene diana7_img69 with Dissolve(1.0)

        na "Você ainda disse que ia me proteger... como você vai fazer isso?"

        mc "Não sei... mas vou cumprir minha promessa."

        na "Rsrs..."

        mc "Pode rir, é verdade."

        na "Você é fofo. Sempre foi."

        if natasha_e4 == "seducao":

            na "Tá me lembrando de quando a gente trepou na prefeitura."

            mc "N-natasha?"

            na "Não lembra?"

            mc "Claro que lembro... Foi gostoso transar lá na sala do chefe?"

            na "Muito. Foi quente pra caralho."

        elif na1_beijo:

            mc "Lembra quando a gente se beijou no Cassino?"

            na "Lembro... veio na minha cabeça bem agora..."

        elif na3_beijo:

            mc "Lembra do nosso beijo lá no Distrito? Pra despistar o Montanha?"

            na "Lembro... veio na minha cabeça bem agora..."

        na "E agora a gente tá jurado de morte. Os dois."

        mc "Pois é... os dois..."

        na "Dá um certo tesão, né?"

        mc "T-tesão?"

        "Ela tá me provocando? Sério mesmo? Numa hora dessas?"

        menu:
            "Dá um tesão, sim...":


                scene black with dissolve

                scene diana7_img70 with Dissolve(1.0)

                na "Esse perigo... ele me lembra do meu país, sabe?"

                na "E não sei porque... ele me deixa muito excitada."

                mc "C-caralho..."

                "Ainda não acredito que eu tenho a chance de ficar com uma mulher dessas."

                "A Natasha parece que caiu do céu. Que mulher mais perfeita."

                "E ela tem uma vibe... perigosa... sei lá... um tipo diferente de tesão."

                na "Você também sente isso?"

                mc "Eu..."

                "Transar numa hora dessas... com o Tony e o Marco na nossa cola?"

                "E se isso diminuir nossa chance de sobreviver?"

                "E no meio da rua ainda!"

                "O que eu faço?!"

                menu:
                    "Tá afim de trepar uma última vez?":


                        $ d7_natasha_sexo = True

                        na "Você sabe que eu tô. Me pega aqui no capô mesmo."

                        mc "Hmmm!"



                        label d7_premium2:

                            pass

                        menu:
                            "Se é nossa última trepada. Bora aproveitar.":


                                if not premium:

                                    call mensagem_premium

                                    jump d7_premium2

                                na "O que você vai querer fazer comigo?"

                                mc "Se for nossa último sexo mesmo, é bom valer a pena."

                                na "No meio da rua ainda... o que você acha de me deixar toda molhada?"

                                mc "Eu adoro chupar essa buceta docinha."

                                mc "Desce do capô e levanta essa bunda pra mim."

                                na "Que homem mandão... mas se é por uma chupada..."

                                scene black with dissolve

                                scene diana7_premium14 with Dissolve(1.0)

                                pause 2.0

                                na "Assim que você quer?"

                                mc "Hmmm... que delícia..."

                                na "Toda sua pra você cair de boca."

                                mc "Ah! Se eu caio..."

                                "Que xotinha mais rosadinha que a Natasha tem."

                                "É perfeita... parece que nunca foi usada, só esperando pra ficar toda molhada."

                                "Vou deixar ela ensopada pra depois entrar nela deslizando."

                                mc "Hmm... tô ficando duro só de olhar pra você, safada."

                                na "Vai logo... tô ansiosa com a buceta na sua cara, homem..."

                                mc "Safada."

                                scene black with dissolve

                                scene diana7_premium15 with Dissolve(1.0)

                                pause 2.0

                                na "Hmmm... é disso que eu preciso!"

                                mc "Que delícia que você é. Essa bucetona é tão gostosa quanto é linda."

                                na "Ah... falando assim e me lambendo toda... hmmm..."

                                menu:
                                    "Chupar ela até ela gozar":


                                        mc "Se nós dois vamo morrer logo, é bom os dois aproveitarem ao máximo."

                                        na "Eu aproveito assim com esse bocão."

                                        mc "Assim que você gosta, né, cachorra."

                                        na "Ah... [mc]..."

                                        mc "Tá gostando, é?"

                                        na "Muito!"

                                        scene black with dissolve

                                        scene diana7_premium16 with Dissolve(1.0)

                                        pause 2.0

                                        na "Aaiinnn..."

                                        mc "Parece que tá bom mesmo."

                                        na "Uma bocada dessa no meio da rua... hmmm..."

                                        mc "Sei. Eu também tô morrendo de tesão."

                                        mc "Mas agora quero você aproveite."

                                        na "Tô aproveitando! Nnnghh! Tá uma delícia! Aahh!"

                                        mc "Vai melar toda minha boca, vai?"

                                        na "Voooouuu!"

                                        mc "Me tá todo esse suquinho agora."

                                        scene diana7_premium17 with hpunch

                                        pause 2.0

                                        na "Hammmnmnnnnngghhhaaa!"

                                        mc "Hmmm..."

                                        na "Ai, que delícia... hmmm..."

                                        mc "Tá tremendo..."

                                        na "Ah... essa boca... essa língua..."

                                        na "Eu tô toda molhada..."

                                        mc "Perfeito! Que agora é minha vez."
                                    "Meter logo que o tesão tá demais":


                                        mc "Você já tá molhada o suficiente!"

                                        na "M-mas!"

                                        mc "Vem cá, gostosa!"

                                na "E-ei!"

                                scene diana7_new18 with hpunch

                                pause 2.0

                                mc "Você me deixou louco, Natasha!"

                                na "Nnghhh!"

                                na "A-achar que vai morrer te deixou com tesão?!"

                                menu:
                                    "Essa pode ser minha última trepada!":


                                        pass

                                na "Aahh!"

                                na "Ahnnn!"

                                na "Não sabia que você tinha isso dentro de você assim!"

                                mc "Nem eu!"

                                scene diana7_premium19 with hpunch

                                pause 2.0

                                mc "Não importa o que eu faça seus chefes continuam me fodendo!"

                                na "Aaiinn! M-mas não sou eu!"

                                mc "Você também faz parte deles!"

                                na "Aahhh! Que pauzão!"

                                mc "Tá gostando, é?! Você é uma safada! Sua puta!"

                                na "Nnghhh! Aaahnnn! É só meu trabalho!"

                                mc "Cala a boca!"

                                na "Aaahnnnn! Quer se divertir na última trepada, né?! Aahhn!"

                                mc "Nnghhh! Você é gostosa demais!"

                                menu:
                                    "Meter mais forte":


                                        pass

                                mc "TOMA!"

                                scene diana7_premium20 with hpunch

                                pause 2.0

                                na "Aaiiighhh!"

                                na "Que gostoso! Agghnn! Que tesão danado!"

                                mc "Eu sei! Eu também! Nghh!"

                                mc "Vou gozarrr!"

                                mc "GOZARRRR!!!"

                                scene diana7_premium20 with hpunch

                                na "AAAAAHHH!"

                                mc "Nngnhhhhh!"

                                na "Caralhooo..."

                                scene black with dissolve

                                scene diana7_premium21 with Dissolve(1.0)

                                pause 2.0

                                mc "Aahh... gozei tudo..."

                                na "Tô vendo... não poupou nada..."

                                mc "Você é deliciosa demais."

                                na "Seu pau também... ah..."

                                mc "Agora pelo menos... eu vou morrer satisfeito..."
                            "A gente não tem muito tempo. Vem rápido.":


                                na "Safado!"

                                scene diana7_new18 with hpunch

                                pause 2.0

                                mc "Você me deixou louco, Natasha!"

                                na "Nnghhh!"

                                na "A-achar que vai morrer te deixou com tesão?!"

                                menu:
                                    "Essa pode ser minha última trepada!":


                                        pass

                                na "Aahh!"

                                na "Ahnnn!"

                                na "Não sabia que você tinha isso dentro de você assim!"

                                mc "Nem eu!"

                                mc "Não importa o que eu faça seus chefes continuam me fodendo!"

                                na "Aaiinn! M-mas não sou eu!"

                                mc "Você também faz parte deles!"

                                na "Aahhh! Que pauzão!"

                                mc "Tá gostando, é?! Você é uma safada! Sua puta!"

                                na "Nnghhh! Aaahnnn! É só meu trabalho!"

                                mc "Cala a boca!"

                                na "Aaahnnnn! Quer se divertir na última trepada, né?! Aahhn!"

                                mc "Nnghhh! Você é gostosa demais!"

                                menu:
                                    "Meter mais forte":


                                        pass

                                mc "TOMA!"

                                scene diana7_new18 with hpunch

                                mc "AAAGHH!"

                                na "Nnnghhh...."

                                mc "Aahh... delícia..."

                        scene black with dissolve

                        scene diana7_new19 with Dissolve(1.0)

                        pause 2.0

                        na "Hehe..."

                        na "Nem acredito que eu tô trepando com você no meio da cidade assim."

                        na "E tão perto da prefeitura ainda."

                        mc "Nem acredito que você ficou afim de transar comigo assim."

                        na "Você merece um agrado..."

                        mc "Certo... por quê?"

                        na "Fiquei com pena de você. Por tudo o que vai acontecer."

                        mc "Haha... engraçadinha."

                        na "Hah..."

                        mc "Caralho... depois dessa o Tony pode até me furar."

                        na "Não brinca com isso. A gente tem que ir."

                        mc "Claro."
                    "Melhor a gente voltar logo.":


                        na "Hmf... então vamos."

                        "Ela não gostou nem um pouco... mas não vai admitir nunca."

                        "E eu perdi a chance de ficar com uma deusa dessas... o que eu tenho na cabeça?!"
            "A gente não tem tempo pra isso":


                na "Hmf... então vamos."

                "Ela não gostou nem um pouco... mas não vai admitir nunca."

                "E eu perdi a chance de ficar com uma deusa dessas... o que eu tenho na cabeça?!"

    na "Ah. Só deixa eu fazer uma ligação antes. Pode me dar uma licença?"

    mc "Hmm... tá."

    if d7_natasha_sexo:

        scene black with dissolve

        scene diana7_img71 with Dissolve(1.0)
    else:


        scene black with dissolve

        scene diana7_img72 with Dissolve(1.0)

    "Pra quem ela tá ligando?"

    "Não posso esquecer que a Natasha continua sendo uma deles."

    "Ela ajudou a Diana, ela vai com a minha cara. Mas mesmo assim, ela é uma deles."

    na "Pronta."

    mc "Opa."

    play sound carro_porta

    scene black with dissolve

    scene diana7_img73 with Dissolve(1.0)

    mc "Então..."

    menu:
        "Pra quem você ligou?":


            na "Tenho que garantir que eles não vão me pegar."

            mc "E você tem alguém pra resolvir isso pra você?"

            na "Quem eu melhor que eu mesma pra me garantir."

            mc "Queria ter essa confiança sua..."

            na "Cada um dá seus pulos, [mc]."
        "Qual é seu plano agora?":


            na "Tive que dá meu jeito aqui. Só posso contar comigo agora."

    na "Vou te levar até a ilha e vou rodar por aí até ficar de manhã."

    na "Daí vou falar com o prefeito o mais rápido possível. Se o Tony me achar antes eu tô fodida."

    if d7_nat_prometeu:

        mc "Eu prometi pra Diana que ia te ajudar, então conta comigo também."

        na "Você é fofo, mas tem pouca coisa que um paparazzo pode fazer agora."

        na "Sua parte você já fez. Que foi causar tudo isso."

        mc "Haha... ok..."
    else:


        "Sorte que eu não prometi que ia ajudar ela. Agora ela se vira com ele."

    mc "Então o Donatello vai te salvar mesmo."

    na "Eu conquistei isso. Eu torno a vida dele muito mais fácil."

    mc "Você não tem medo dessas pessoas?"

    na "Claro que eu tenho. Mas as coisas não eram diferentes do meu país."

    mc "Sempre suspeitei que você não é daqui. Seu sotaque, e sua aparência também."

    na "As coisas não eram fáceis lá. Mas desta vez eu tô do lado das pessoas certas."

    menu:
        "Sei não, Natasha... quem escravizou a Diana tá do lado certo?":


            pass

    na "Vamos deixar essas conversas pra depois que a gente tiver passado por isso."

    mc "Não faço ideia do que eu vou fazer ainda..."

    na "Chegou a hora de você acionar amigos. Pessoas poderosas que possam te proteger agora."

    na "Você conhece vários famosos. Alguém precisa segurar a barra pra você."

    "A Natasha tem razão. A pessoa certa pode me salvar dessa bosta que eu me meti."

    "Com quem eu poderia contar agora..."

    "Se eu pudesse escolher UMA pessoa. Quem eu chamaria?"

    menu:
        "Ok... amanhã cedo vou fazer umas ligações. Tenho que ver em quem contar agora.":


            pass

    na "Se eu puder fazer algo, pode deixar comigo."

    mc "Você aliviaria minha barra com o prefeito?"

    na "Claro. Eu te falei que o Basílio é um homem sério. Você acha que ele vai querer coagir ou até matar alguém por isso?"

    mc "Tomara que não."

    "Será que o prefeito é diferente do Tony e do Barão? Será que ele é um cara certo mesmo?"

    "Parece que a Natasha coloca a mão no fogo por ele."

    scene black with dissolve

    scene diana7_img77 with Dissolve(1.0)

    "A Natasha deve ser uma das mulheres mais lindas que existem no mundo."

    "Será que o prefeito tem esse tipo de interesse com ela também?"

    "Ela é secretária dele. Se ele for um nojento, provavelmente pode fazer ela aceitar o que ele quiser."

    "Mas a Natasha é sexy pra caralho também. A voz, o jeito que ela fala, a confiança."

    "Fico pensando se ela não usaria tudo isso pra conseguir o que ela quer."

    "Quem tá na mão de quem?"

    na "[mc]? Derrubou algo aqui?"

    mc "N-não!"

    play sound som_carro

    scene black with dissolve

    pause 1.0

    scene diana7_img74 with Dissolve(1.0)

    na "Esse ponto de ônibus é o mais perto da sua casa?"

    mc "Hm? É."

    na "Posso te deixar aqui? Vou fazer o retorno ali pro centro."

    mc "Claro. Tá excelente aqui pra mim."

    na "Ok... perfeito..."

    mc "?"

    na "B-boa sorte, [mc]. Não esquece de ligar pra alguém. Você precisa de ajuda."

    mc "Pode deixar. E você também, Natasha. Toma cuidado."

    if d7_natasha_sexo:

        na "Se a gente morrer esses dias... pelo menos a gente transou uma última vez."

        mc "Foi um prazer transar contigo hoje, delícia. Mas a gente vai repetir."

        na "Espero que sim... você faz gostoso, viu?"

        mc "Eu? Não sou nada perto de você."

        na "É um prazer agradar meu homem."

    na "Até, gato."

    play sound carro_porta

    scene black with dissolve

    scene cidade onibus_noite with Dissolve(1.0)

    "Parece que aqui termina minha noite... que loucura."

    "Quem ia imaginar que aquele evento com a Diana ia acabar assim?"

    "Diana... Tomara que a Diana consiga escapar. E finalmente seja livre."

    "Esses filhos da puta não podem continuar fazendo isso. Acabando com a vida de alguém assim."

    "E eu tenho que ficar esperto. Cedo ou tarde eles vão vir atrás de mim por eu ter vazado aquele vídeo."

    "Pode não ser hoje, nem amanhã... mas eu sinto que em algum momento vai acontecer."

    "Eu ajudei a Diana publicando o vídeo. Agora eu tô na mira deles. Até a Natasha sabe disso."

    "Sinto que tô me metendo em buracos cada vezes mais fundos."

    "Hoje só quero me trancar em casa e torcer pra eles não venham atrás de mim por um tempo."

    "Qual vai ser a próxima desgraça que eu vou me meter?"

    scene black with dissolve

    $ tempo = 3

    jump call_cidade

label diana_final2_parte2:

    $ diana_final2 = True

    $ renpy.vibrate(1)

    play sound smash

    scene diana7_img75 with vpunch

    mc "ARGH!!"

    "???" "Previsível."

    menu:
        "Caralho! Quem me tacou no chão, porra?!":


            pass

    "???" "Quem mais?"

    mc "Você tem ideia quanto custou isso aqui, hein?!"

    "???" "Garoto, outros problemas mais urgentes chamam sua atenção."

    mc "Q-quem..."

    scene diana7_img76 with vpunch

    mc "Vocês!"

    "C-como?! Como eles me acharam tão rápido assim?!"

    "Eu nem cheguei em casa ainda!"

    to "Quem ia imaginar..."

    to "Um paparazzo qualquer, causando esse tipo de dor de cabeça."

    menu:
        "Eu só fiz meu trabalho.":


            mc "Foi pra isso que eu fui!"

            to "Claro! Óbvio que foi pra isso!"
        "Não tinha como deixar a Diana daquele jeito.":


            to "Não tinha, né?"

    to "Ou você é muito inteligente, ou é muito idiota."

    to "Acha que pode contra nós ou é burro pra entender contra quem você tá indo contra."

    mc "Tony... eu..."

    if d7_faca >= 2:

        to "Você esfaqueou o Barão, porra!"

        to "Um dos caras mais ricos dessa merda toda! Você entende, caralho?!"

        mc "Ele ia bater na Diana!"

        to "E não foi só isso..."

    to "Aquele vídeo... a vida dele acabou."

    mc "Não podia deixar a Diana lá ignorada... ela ia ficar lá? Presa pra sempre?"

    to "Foda-se, idiota! Não se faz isso com alguém como ele!"

    to "Existem pessoas que tão acima da lei, do certo e do errado!"

    to "Se a polícia ou a justiça não podem fazer nada contra eles, não é um otário como você que vai!"

    menu:
        "Eu já fiz. Você mesmo disse.":


            pass

    mar "Chefe..."

    to "O garoto tá pilhado, Marco. Ele não sabe o que tá falando."

    "Não sei porque tô provocando esse cara. Provavelmente eu já tô morto mesmo. Foda-se!"

    to "Eu tô vendo nos seus olhos. Você já sabe o que vai acontecer com você, né?"

    to "Por que você não fugiu com a cantora? Você teria uma chance."

    mc "Eu ainda tenho coisas pra resolver aqui na ilha."

    to "Ah, tem sim, com certeza."

    to "Coloca ele de pé."

    mar "Sim, senhor."

    mc "NÃO! POR FAVOR!"

    play sound som_hit

    scene diana7_img78 with hpunch

    mc "AAAGHH!"

    "Para! Por favor!"

    to "Se você acha que você tem alguma chance contra mim, você não entende."

    to "Filho da puta!"

    play sound som_hit

    scene diana7_img78 with hpunch

    mc "IAAAHGGH!"

    "Tá doendo! Tá doendo tanto, caralho!"

    to "Nem a garota gritou igual você, seu fraco."

    play sound som_hit

    scene diana7_img79 with vpunch

    mc "AAGNHH!"

    "Eu tô sangrando! Eu vou morrer!"

    to "Vamos ver quantos socos você aguenta até ter uma hemorragia."

    menu:
        "Por favor...":


            to "Devia ter pensado nisso antes de ir contra quem é maior que você."

            mc "NÃO!"
        "...":


            to "Já morreu?"

            to "Acorda, cretino!"

    play sound som_hit

    scene diana7_img80 with vpunch

    mc "UUGHH!"

    "Por que tá acontecendo isso comigo?!"

    mar "Mais um pouco e ele vai apagar, chefe."

    to "Tenho certeza que a hacker durou mais que isso, Marco."

    if mc_fisico > 250:

        mar "Dá pra ver que ele treina na academia. Talvez ele aguente mais um pouco."

        to "Excelente. Que eu ainda tô longe de terminar com esse pilantra."

        play sound som_hit

        scene diana7_img80 with vpunch

        mc "AAAII!"
    else:


        mar "Ele não tem treino suficiente. Dá pra ver que ele tá quebrando."

        to "IDIOTA!"

        play sound som_hit

        scene diana7_img80 with vpunch

        mc "AAAIII!!!"

    to "Joga esse puto no chão."

    "Só acaba logo... me mata..."

    play sound som_grito

    scene diana7_img81 with vpunch

    pause 3.0

    mc "Aahh... aahh..."

    "..."

    to "O que você fez hoje vai ter implicações muito maiores do que essa cabecinha sua pode compreender."

    to "A queda do Barão derruba várias outras peças."

    mc "D-do que você tá falando?"

    "Eu não consigo enxergar direito... minha respiração... meu corpo... tá tudo estranho."

    to "Esse é o fim do Barão."

    if d7_faca >= 2:

        to "Mesmo que ele sobreviva à facada que você deu. O que já vai ser difícil pelo jeito."

    to "O vídeo acabou com ele."

    menu:
        "Só com ele?":


            to "Não vou falar sobre isso com você."

            to "Mas o idiota se ferrou."
        "Espero que você não tenha se ferrado também.":


            to "Eu não. Não estava lá. Não apareço no vídeo."

            mc "Que bom..."

            to "Pelo contrário."

    to "Com a queda do Barão, resolveram passar o Cassino pra eu gerenciar."

    mar "Parabéns, chefe."

    to "Não sou o dono, a grana não é minha, mas nunca pensei que eu fosse subir rápido dessa forma."

    menu:
        "Graças a mim...":


            pass

    to "Tem razão. Graças em parte a você e à Diana também."

    to "O pequeno golpe de vocês deram acelerou muito meus planos."

    scene black with dissolve

    scene diana7_img82 with Dissolve(1.0)

    to "A família Alighieri é só um adereço dos Donatello a tempo demais."

    to "O Luca pode estar satisfeito, mas eu não estou."

    to "Eu vou assumir o comando da família cedo ou tarde. Que Deus tenha minha querida falecida."

    to "E quando isso acontecer, muita coisa vai mudar. O velho vai ter que aceitar as MINHAS decisões."

    to "E é incrível como você acabou me ajudando. Mesmo sem ter a intenção."

    menu:
        "Isso quer dizer que você vai me deixar viver?":


            pass

    to "Claro que não."

    to "Como eu posso deixar um maluco como você vivo?"

    to "Eu cheguei onde eu cheguei me livrando de ratos como você pra eles."

    mc "Tony... eu só queria ajudar a Diana... eu não tenho nada contra 'eles'. Nem sei quem eles são."

    to "Não se faça de burro. Até mesmo um inocente como você sabe de quem estamos falando."

    to "Com certeza você não sabe tudo, não conhece todos, mas tem uma ideia de quem manda na ilha de verdade."

    to "Desde o velho abusador que estupra a Priscila, até membros de órgãos públicos de relevância na capital."

    mc "Eu não quero escutar isso... eu não quero nada com essas pessoas..."

    to "Dá até dó... como você entrou nesse rolo todo só procurando pautas pra se manter na revista."

    scene black with dissolve

    scene diana7_img83 with Dissolve(1.0)

    mar "As vezes parece o destino, chefe."

    to "Você sabe que eu não acredito nesse tipo de bobagem, Marco. Calado."

    mar "Desculpa, chefe. Mas pense. Ele é só um paparazzo. Um jornalista recém-formado."

    to "Isso é... falando assim, é impossível que você realmente faça algo."

    mar "E ele acabou ajudando, né?"

    to "Talvez sua maluquice, se tiver uma cabeça por trás, pode ser útil na hora certa. Você pensou o mesmo que eu, Marco?"

    mar "Acho que não, senhor... mas a revista..."

    to "É... é sobre isso mesmo que tô pensando."

    to "É a única coisa que o Luca ainda não conseguiu."

    "Eles querem a revista. Mas não posso falar nada. Eu tô com o pé na cova aqui."

    "Agora é torcer por um milagre! De cima ou de baixo! Por favor! Alguém me salve! Pixie!"

    to "A Cássia falou que a filha do editor que tá causando. Você sabe quem é ela?"

    "A Sofia... não... se eles souberem que ela publicou o vídeo..."

    "E ainda por cima tá tentando fazer a cabeça do pai dela pra não vender..."

    "Mas se eu mentir pra ele... eu tô em condições de tentar salvar alguém agora?"

    "É MINHA vida que tá na reta aqui."

    menu:
        "Eu sei quem é a filha dele. Nós somos... amigos.":


            pass
        "Eu não sei de quem você tá falando.":


            mar "Maninho..."

            to "Não tem jeito. Ele nunca vai se dobrar."

            mar "E agora, chefe?"

            to "Você sabe."

            mc "Marco! Me escuta!{nw}"

            jump diana7_final_morre

    to "Excelente."

    to "Me fala... foi ela quem publicou o vídeo, não foi?"

    "Não! Essa pergunta, não!"

    menu:
        "Sim...":


            pass
        "Não sei. Só mandei o vídeo.":


            to "Não tem jeito. Ele nunca vai se dobrar."

            mar "E agora, chefe?"

            to "Você sabe."

            mc "Marco! Me escuta!{nw}"

            jump diana7_final_morre

    mc "Mas foi o chefe que deixou ela de plantão. Ela não sabia nada sobre a Diana."

    to "Sei... mesmo assim, ela devia ter tido um pouco mais de cabeça."

    mar "Ela parece corajosa. E pra irritar a Cássia daquele jeito."

    to "Hah... sem medo de publicar um vídeo como aquele, não querendo a revista na mão da Faux."

    to "E eu ainda lembro que o Luca não foi com a cara dela."

    menu:
        "O senhor Luca era o ídolo da Sofia!":


            pass

    to "Hahaha... e ela deve ter mudado de opinião quando viu ele."

    "Como ele sabe disso?"

    "Lembro que a Sofia ficou super chateada depois do jeito que ele falou sobre as notícias."

    to "Aquele velho..."

    to "Enfim, estou aqui há mais tempo do que eu devo. Mas graças a você eu vejo uma luz aqui."

    to "Nós vamos fazer um acordo. E talvez você possa viver mais um dia."

    "Tô vendo uma luz no fim do túnel! Isso!"

    "Eu tenho que falar qualquer merda pra esse cara. Qualquer coisa que me tire daqui com vida!"

    "Depois eu falo com a Sofia, com a polícia, sei lá."

    menu:
        "Por favor... o que você quiser, Tony. Juro que não vou atrapalhar.":


            pass

    mar "Assim que se fala, maninho."

    to "Até que você não é tão idiota, garoto. Ser herói é para os lunáticos. A vida não é assim."

    to "Mantenha os pés no chão e você vai chegar longe."

    scene black with dissolve

    scene diana7_img84 with Dissolve(1.0)

    mc "O que eu posso fazer por você?"

    to "Te darei três opções. A sua vida, a vida da sua amiga de trabalho ou algo a mais que você tenha pra mim."

    to "Em breve meu sogro vai fazer uma proposta para a mesa de diretores da sua revista."

    to "Vai ser uma proposta agressiva, e eles provavelmente irão aceitar. A não ser que o editor e a filha atrapalhem."

    to "Você vai garantir que ela não será um problema. Mas você precisa fazer isso ANTES da proposta."

    to "Pois se não eu vou garantir que ela pague pelo vídeo publicado e pelo trabalho que ela tá dando na aquisição."

    to "Estamos entendidos? Ou tem outra razão pra eu te deixar vivo?"

    "Se eu não tivesse ajudado a Diana eu não taria nesta situação."

    "Não ia precisar vender a revista... ou colocar a vida da Sofia em risco."

    "Uma vida pela outra. É o que parece aqui."

    "Ou tem uma terceira chance? Sacrificar outra pessoa?"

    "[mcc]... o que você vai fazer?"

    label diana_final2_menu:

        pass

    menu:
        "Sim, senhor. Eu vou te dar o sinal verde assim que ela tiver pronta.":


            $ sofia_entregou = True

            to "É isso que eu gosto de ouvir."

            to "Claro que as coisas não vão acontecer no seu tempo. Vou te dar um período pra fazer isso. E é menor do que você imagina."

            mc "Mas eu preciso de tempo pra fazer isso... a Sofia é terrível."

            to "Esse é seu problema. Não meu. Assim que tudo estiver pronto, você me diz."

            to "Você tem ideia que o dono da Faux, Luca Alighieri, é meu sogro. O marido da minha falecida esposa."

            to "Eu ainda vou tomar o lugar dele como o patriarca da família."

            to "Se eu disser pra ele que a compra da revista vai acontecer, é essencial que ACONTEÇA."

            to "Ou a sua morte não vai ser suficiente para saciar minha vingança."

            scene diana7_img84 with hpunch

            to "ESTAMOS ENTENDIDOS?!"

            menu:
                "S-sim, senhor.":


                    pass

            to "Muito bem."
        "Eu não posso fazer isso. Não posso estragar a vida dela pela minha.":


            mar "Essa é sua resposta, maninho?"

            to "Não tem jeito. Ele nunca vai se dobrar."

            mar "E agora, chefe?"

            to "Você sabe."

            mc "Marco! Me escuta!{nw}"

            jump diana7_final_morre
        "Eu tenho algo a mais. É sobre a Natasha.":


            if d7_nat_prometeu:

                "Não... eu prometi pra Diana que ia proteger a Natasha. Não posso voltar atrás agora."

                "Não seria justo com ela. Eu sou um homem de palavra."

                jump diana_final2_menu

            $ natasha_entregou = True

            to "Natasha? A secretária do prefeito?"

            mc "Sim."

            to "Hmm..."

            mar "Chefe... você sabe como el-"

            to "Quieto, Marco!"

            mar "Sim, senhor."

            to "Eu sei o que ela representa pra nós."

            mar "Por isso mesmo..."

            mc "Você vai pegar ela, não vai?"

            "O que eu tô fazendo? Vou entregar a Natasha por causa da revista?"

            "Eu tô falando da vida de uma pessoa aqui."

            to "Eu não confio nessa mulher. Ela parece inteligente demais."

            "O Tony tem medo da Natasha? É isso mesmo?"

            to "Ela possuiu o prefeito como uma alma penada. Ele não quer enxergar o que está acontecendo."

            "Essa é minha chance de sair daqui vivo sem envolver a Sofia e a revista."

            menu:
                "A Diana só fugiu por causa dela. Ela conseguiu o avião do prefeito e levou ela.":


                    pass

            mar "Olha só... um contra o outro."

            to "Você tem certeza?"

            mc "Sim. Eu tava lá."

            to "Isso é melhor pra mim do que você imagina."

            mc "Só não... por favor... não mata ela, Tony. A Natasha tá do lado de vocês."

            to "Cala a boca."

    to "Obrigado por me tornar o novo chefe do cassino."

    to "Espero que você sobreviva."

    to "Marco, vamos."

    mar "Posso levar ele no hospital, chefe?"

    to "Não. Ele que sobreviva sozinho. É perigoso."

    to "Você sabe quem está lá, não sabe?"

    mar "Sim, senhor. Boa sorte, Maninho."

    play sound som_hit

    scene diana7_img85 with vpunch



    mc "ARGH!"

    to "Incrível como você continua vivo. Você é uma barata."

    play sound som_35_passos

    mar "É verdade, maninho. Você se mete em cada uma, mas continua vivo."

    mar "Pra mim isso é destino. Talvez o Senhor tenha algo pra você. Ou o Inimigo."

    mc "Marco... como eu vou chegar no hospital assim?"

    mar "Dá seus corres, maninho. Você ouviu o chefe. Boa sorte."

    play sound som_35_passos

    "Eles vão mesmo... me deixar pra morrer aqui..."

    mc "Alguém me escuta..."

    show black with dissolve

    hide black with dissolve

    "N-não..."

    "A adrenalina tá acabando... eu vou..."

    show black with dissolve

    hide black with dissolve

    mc "Marco... alguém..."

    mc "Por favor..."

    "Por que as coisas tinham que acabar assim?"

    show black with Dissolve(1.0)

    hide black with Dissolve(1.0)

    "Se eu tivesse feito uma amizade diferente... um amor diferente..."

    "Será que ela poderia me salvar agora?"

    "Como é ruim... tá sozinho..."

    show black with Dissolve(2.0)

    pause










    pause

    scene black with dissolve

    scene diana7_img86 with Dissolve(1.0)

    pause

    mc "Eu tô vivo?"

    mc "Eu vivi! Eu tô vivo!"

    mc "CARALHO EU TÔ VIVO!!!"

    "Fico imaginando quantas escolhas eu podia ter tomado ontem a noite que me levariam pra desgraça total."

    mc "Tô pouco me fodendo!"

    mc "Eu consegui... o Tony e o Marco me deixaram viver!"

    "Só que... como eu vim parar no hospital?"

    "Será que o Marco me ouviu chamando ele?"

    "???" "Acordou, bro?"

    mc "!!!"

    scene black with dissolve

    scene diana7_img87 with Dissolve(1.0)

    mc "[us]!"

    us "Quem mais? Como você tá, amigo?"

    menu:
        "Você que me salvou?":


            pass

    us "Eu que te trouxe aqui. Tu tava fodido, bro."

    mc "Mano... como..."

    "Destino? Pixie?"

    us "Não lembra? Foi naquele mesmo ponto que a gente se reencontrou."

    mc "Verdade... quando você me tacou no chão, filho da puta."

    us "Eu tava indo pro cassino. Tinha ouvido umas coisas."

    mc "É... a noite foi quente no Cassino do Barão."

    us "Daí eu vi uma mina em cima do ponto de ônibus, tu acredita?"

    mc "Uma m-mulher?"

    us "Isso aí, mano. Coisa doida. Quando desci do carro e fui lá ver, cadê a mina? Tinha sumido."

    us "Daí te vi caídão lá. Nem te reconheci de tão inchado."

    menu:

        "A Selena?!" if quincy_e1:

            us "Sei não, cara. Ela sumiu."

            mc "Foi lá que eu vi ela a primeira vez... em cima do ponto."

            "A Selena que chamou o [us]?"

            "Mas ela..."
        "Uma moça em cima do ponto...":


            us "Sei não, cara. Ela sumiu."

            mc "Não sei quem pode ser... que doideira..."

    us "Daí claro que eu te trouxe aqui, né?"

    mc "Como vou te agradecer, irmão? Sem você eu ia tá morto. Certeza."

    us "Com certeza hahaha! A não ser que a mina do ponto te trouxesse. Mas, sei lá, deu até um arrepio olhar pra ela."

    us "Ei! Foi bom eu ter te visto, sabia?"

    mc "Sério? Que que foi?"

    if xiang_escape >= 5:

        mc "Pensei que eu era persona não grata no Distrito depois que eu tirei a Xiang de lá."

        us "A Madame não pode te ver nem pintado de ouro, amigo."

        mc "Eu não piso lá nem que me paguem."

        us "É melhor mesmo."

        us "Mas agora as coisas podem mudar."

        mc "Por quê?"

    us "Tu fez a boa pra gente, cara."

    mc "Eu?"

    scene black with dissolve

    scene diana7_img88 with Dissolve(1.0)

    us "Claro."

    us "Tu ajudou a mana Diana, irmão. Eu descobri tudo."

    menu:
        "Mana? Diana? Como assim? O que ela é pra você, cara?":


            pass

    us "Bateu a cabeça, é? A Diana a cantora."

    mc "Eu sei! Mas o que tu tem com ela?!"

    us "A mana Diana é cria do Distrito, ué."

    us "E tu salvou ela, cara. Tu tirou ela das garras daquele filho da puta do Barão."

    if xiang_escape >= 5:

        us "Tu tirou a nossa da gente, mas tirou a deles também."

        us "Tu reestabeleceu o equilíbrio."

    mc "Cara... não sei se eu tô grogue, mas tu vai ter que me explicar melhor isso."

    us "Tu é jornalista, cara! Envolvido nos trâmites aí, bro. Era pra tu saber dessas paradas."

    us "Das {b}sacerdotisas{/b}, pô!"

    mc "O estranho é que essa é uma palavra rara demais pra eu tá ouvindo toda hora desse jeito."

    us "Tô falando. Tu sabe desse lance problemático aí, caralho."

    if sacerdotisas > 0:

        "Eu vi um lance desses lá no NBC."
    else:


        "Sinto que eu podia saber mais sobre isso neste ponto, viu..."

        "Não sei porque, mas lembrei da Júlia agora. Que estranho."

    mc "Uma hora você vai ter que me contar esse lance direito, cara."

    us "Depois do que tu fez pela mana Diana, tu vai ser um herói lá no Distrito, cara."

    us "Tu abriu um caminho e tanto pra nós. Tu não compreende a parada."

    menu:
        "Se você tá falando, eu não vou ligar de ser herói.":


            pass

    us "Hahaha! Tu é foda, irmão."

    us "As coisas vão acontecer. Ainda mais agora."

    if xiang_escape >= 5:

        us "Vou falar com a velha. Tentar limpar sua barra, beleza?"

        mc "Seria massa, cara. Tô com saudades de ir lá."

        us "A Celeste vive falando de ti. Até hoje."

    us "Vou fazer a boa pra você lá então. Você vai ver. Vai ficar tudo certo."

    mc "Espera, [us]..."

    us "Que foi?"

    "O que a Natasha falou sobre amigos poderosos."

    "A Madame Nora e o Distrito podem me ajudar."

    if natasha_entregou:

        "E não só eu... Eu entreguei a Natasha pro Tony. Talvez ele pudesse me ajudar."

    elif sofia_entregou:

        "Eu entreguei a revista pra ele. Talvez com a ajuda do Distrito eu pudesse reverter isso."

    "O que é mais negócio pra mim?"

    if xiang_escape >= 5:

        "Se ele limpar minha barra com a Madame Nora por causa da Xiang, nossa, vai ser bom ter amizade com eles de novo."
    else:


        "Se eu ganhar moral no Distrito, talvez me ajude no futuro, caso eu bagunce lá em algum momento."

    menu:
        "Nada. Faz minha moral lá no Distrito. Vai ser bom.":


            $ black_salva = 1

            us "Vai ser bom pra tu, você vai ver."

            us "Ter nossa amizade vai ser útil... ô se vai."

            mc "Isso tenho certeza. Vou contar com vocês."

        "Preciso da ajuda do Distrito pra salvar uma amiga chamada Natasha." if natasha_entregou:

            $ black_salva = 2

            mc "Tenho uma amiga chamada Natasha. Ela trabalha com o prefeito."

            mc "Fala com ele, por favor. Não deixa nada de ruim acontecer com ela."

            us "Hmm... é um pedido complicado. Vou ter que falar com a Madame."

            mc "Ela tem contato com ele?"

            us "Claro. Se ela topar, acho que consigo ajeitar pra tu. Essa... Natasha vai ficar bem."

            mc "Você é o cara."

        "Preciso da ajuda do Distrito pra evitar a compra da revista." if sofia_entregou:

            $ black_salva = 3

            mc "Os filhos da puta querem me obrigar a fazer a cabeça de uma mina."

            mc "Se eu não fizer, eles vão me passar. Vou precisar de um help com isso."

            us "Ninguém vai tocar no meu parça."

            us "Se a coisa esquentar, me avisa e eu deixo o Montanha contigo um tempo."

            mc "Tá falando sério?"

            us "Eles têm aquele gorila deles, mas o Montanha dá um pega bom. Pode apostar."

            mc "Nem sei como agradecer."

    "Não sei se isso resolve... mas é algo já."

    us "Então fica assim."

    us "Não esquenta que tá tudo acertado com o hospital. Presente do seu amigo de infância."

    mc "Você é o cara, [us]. Obrigado de novo. Tu é muito firmeza, irmão."

    us "Pode contar. Tamo aí pra isso. Vamos torcer agora pela mana Diana."

    mc "Vamos torcer pra ela ter a vida que ela queria. Longe do Barão. Ela tá livre agora."

    us "Graças ao meu irmão [mc]. Tu é foda. Agora deixa eu ir que tem mais gente querendo te ver."

    mc "Sério?"

    us "Ela tá toda feliz que você acordou e não morreu."

    mc "Ué. Quem?"

    if priscila_namoro:

        us "Disse que é sua namorada."

        mc "!!!"

    us "Você vai ver. Tu tá bem, hein, cara."

    us "Saindo com uma mina dessas, mano. Se contar não dá pra acreditar."

    us "Agora vou lá. Antes que ela tenha um treco."

    mc "Até."

    play sound som_35_passos

    scene black with dissolve

    scene diana7_img86 with Dissolve(1.0)

    "Tô vivo... e agora o [us] tá do meu lado."

    "Talvez eu tenha uma chance."

    "Queria tanto que desse certo pra todo mundo no final."

    "Sei que vai ser difícil, que se eu não tomar cuidado eu vou pra vala também."

    "Só que me salvar sozinho vai ser um cocô também. Quero ver todo mundo livre desses filhos da puta. Se der."

    "E quem raios tá aí?"

    "???" "Licença..."

    scene black with dissolve

    scene d7_pri1 with Dissolve(1.0)

    pause

    c "Oi..."

    mc "PRI!!!"

    c "Você parece melhor mesmo... ufa... tô tão feliz!"

    mc "É você mesmo? O que você tá fazendo aqui?"

    c "Vim te vê, né!"

    c "Fiquei sabendo que você tinha se envolvido num rolo lá no cassino!"

    menu:
        "Como assim? Quem te falou?":


            pass

    c "A Miranda ouviu alguma coisa de alguém e me falou. Daí eu vim correndo!"

    if priscila_namoro:

        c "Não tinha como deixar meu gato jogado aqui sozinho!"

        mc "Você é fofa demais... a melhor namorada do mundo."
    else:


        c "Não tinha como deixar meu meu melhor amigo jogado aqui sozinho!"

        mc "Você é fofa..."

    "Uau... como ela tá gata..."

    menu:
        "Deixa eu ver essa roupa melhor":


            scene black with dissolve

            scene d7_pri2 with Dissolve(1.0)

            pause

            "Hmm... caraca..."

            "Ela tá quase pelada! Esse vestido é transparente, e parece que ela não tá usando nada por baixo!"

            "Se eu forçar um pouco a vista acho que consigo ver tudo! Quase consigo! Falta pouco!"

            c "Gostou?"

            menu:
                "Claro! Olha pra você, que delícia!":


                    c "Gostou, né?"

                    if priscila_namoro:

                        c "E é tudo seu. Tudo pro meu príncipe."

                        mc "Assim que eu gosto. Essa delícia só pra mim."

                "Não gosto da minha namorada andando assim." if priscila_namoro:

                    c "Não fica assim, fofo."

            if priscila_namoro:

                c "Eles podem ver, mas só você pode pegar."

                c "Eles ficam desejando o que só você pode ter."

                mc "Só eu?"

                c "Claro."

                c "Enquanto você tiver só comigo, eu vou tá só com você também."

                c "Eu sou uma garota apaixonada. Quero meu príncipe. Desde o começo!"

                mc "Eu sou ele."
            else:


                c "Se você tivesse comigo... podia fazer mais que só olhar."

                mc "Não me provoque..."

                c "Claro que provoco. Você sabe que eu quero você desde o começo."

                mc "Pri..."

                "Será que eu tô sendo MUITO idiota de não ficar com ela?"

            c "Mas agora não quero dar em cima de você. Você tem que descansar."

            mc "Eu não tô tão ruim assim."
        "Melhor não dar uma de tarado":


            pass

    c "Nao se mexe... eu vou aí."

    mc "O-opa."

    scene black with dissolve

    scene d7_pri3 with Dissolve(1.0)

    pause

    c "Cheguei."

    mc "Como tão as coisas? Faz tempo que eu não via você, gata."

    c "Meu filme tá quase lançando. Eu tô viajando o mundo todo dando entrevista."

    c "Já fui nuns 100 Talk Shows diferentes pra anunciar o filme."

    mc "Caraca! E você voltou... só pra me ver?"

    c "Como SÓ pra te ver?"

    if priscila_namoro:

        c "Você entende que você é a coisa MAIS importante pra mim."

        mc "Se você diz."
    else:


        c "Se eu não vier te xavecar, como que eu te seduzo?"

        mc "Haha..."

    c "Comprei este vestido só pra você. Pra você não conseguir tirar os olhos do meu corpo."

    mc "Tá quase funcionando..."

    c "Não funcionou?!"

    mc "É que seu rosto é bonito demais, sabe."

    c "Bobo..."

    c "É sério. Se eu tô aqui hoje, sorrindo desse jeito, é por sua causa, [mc]."

    c "Você sabe como as coisas tavam no começo."

    c "Mas você me ajudou a sair do buraco. E ainda foi até o fim."

    menu:
        "Como o idiota do Gustav tá?":


            pass

    c "Desaparecido."

    mc "Verdade?"

    c "Desde aquela audiência lá com a juíza ele tá quieto. Tramando alguma, provavelmente."

    c "Por isso que eu vim também. Tenho medo que ele faça alguma coisa terrível com você."

    mc "Ele não seria o único..."

    c "Quem ia imaginar que você também ia arranjar briga com o Barão."

    mc "Esses caras... eles são terríveis."

    c "Sim... e você parece mais cabeça dura que eu..."

    menu:
        "Não vou deixar eles fazerem mal pra você e nem pra ninguém.":


            pass

    scene black with dissolve

    scene d7_pri4 with Dissolve(1.0)

    c "Parece um herói falando. Então eu vou te ajudar nisso."

    mc "Você não vai querer entrar nessa."

    c "Se você não puder contar comigo mesmo depois de tudo o que fez pra mim, eu seria uma babaca."

    c "Claro que eu quero. Eu não sou de porcelana."

    menu:
        "Eu sei. Você tem muita força aí dentro.":


            c "Não quero acabar no hospital igual meu herói, mas eu vou fazer minha parte."

            mc "Alguma coisa em mente?"

            c "Sim. Eu descobri algo... na prática..."
        "Pri... mas e o filme? Você vai continuar com eles.":


            c "Você não sabe como as coisas funcionam. O contrato..."

            mc "Que que tem?"

    c "Eles enganam todas. Mas eu vou dar um jeito."

    mc "Eu preciso de pautas. Se quiser me falar."

    c "Vou falar. Só que na hora certa."

    c "Vou falar com a Ágata e com a Tatá. E você vai ver."

    mc "Boa sorte, linda."

    if priscila_namoro:

        c "Assim que isso acabar, a gente viver felizes."

        c "Me espera só mais um pouquinho."

        c "E não me trai, hein! Ou eu me vingo saindo com outro cara!"

        menu:
            "Claro que não... jamais.":


                pass

        c "Rum... ok..."

    c "Eu não vou sair de mãos abanando. Mas quando chegar a hora, você vai ver. Eu vou acabar com eles, [mc]."

    if priscila_namoro:

        mc "Escutar você falando assim me deu vontade de te beijar."

        c "E por que não beija logo?"

        menu:
            "Posso te beijar?":


                c "Você pode tudo, meu homem."

                scene black with dissolve

                scene d7_pri5 with Dissolve(1.0)

                c "Hmm..."

                mc "Hmmm..."

                c "Que saudades dessa boca."

                "Essa mina é MUITO gostosa, caralho. Essa boca, essa pele, esse cheiro. Tudo."

                "Não é à toa que ela é esse fenômeno. O corpo, a boca, ela foi feita pra dar tesão."

                "Imagino quantas milhões de pessoas não iam querer experimentar essa delícia que tá nos meus braços."

                c "Pode pegar em mim... mata a saudades do seu amor..."

                scene black with dissolve

                scene d7_pri6 with Dissolve(1.0)

                c "Ahh..."

                mc "Com esse vestidinho só pra me dar tesão, né?"

                c "Sim! Só pra deixar meu gato louco pra me pegar."

                mc "Vou pegar em tudo. Esse rabão, esses peitos."

                c "Isso! É tudo seu! Pega neles!"

                c "Pode pegar em tudo... aperta... apalpa... pega no meu pescoço, faz o que quiser."

                mc "Nnnghh..."

                menu:
                    "Tirar o vestido dela":


                        pass

                mc "Vem!"

                scene black with dissolve

                scene d7_pri7 with Dissolve(1.0)

                c "Ainn..."

                c "Vai me deixá sem roupa no meio do hospital, é?"

                mc "Lingua gostosa. Corpo safado."

                c "Sou safada pra você, amor."

                mc "Quero fazer tudo com você hoje!"

                c "Faz, sim. Faz!"

                mc "Eu vo- AAAGH!"

                c "[mc]?!"

                mc "M-meu... ai que dor!"

                c "C-calma!"

                scene black with dissolve

                scene diana7_img86 with Dissolve(1.0)

                mc "Caralho... que dor..."

                c "Quer que eu chame a enfermeira?! Aqui!"

                mc "N-não... tá tudo bem. Já passou..."

                mc "Só é melhor eu não sentar de novo."

                mc "Que merda! Só por que tava uma delícia!"

                c "Hehe... eu adorei..."

                mc "Mas eu queria te dar mais carinho."

                c "Você ainda vai dar. Vai me deixar doida!"
            "Ainda tô meio dolorido.":


                c "E-entendi..."

                c "Bom... vou esperar mais um pouquinho..."

    c "Mas vou cuidar de você todo agora!"

    mc "Vai, é?"

    c "Dá licença! Upa!"

    mc "E-ei! Argh!"

    scene black with dissolve

    scene d7_pri8 with Dissolve(1.0)

    c "Vou ficar aqui até você dormir. Depois tenho que ir viajar."

    mc "Foi muito pouco."

    c "Eu sei! Foi mesmo!"

    c "Mas se você não morrer nos próximos meses, logo logo o filme sai."

    c "E o resto vai ser resolvido. Você vai ver."

    menu:
        "E quando sair o resultado se eles vão investigar...":


            pass

    c "Se eles investigarem ele... mesmo que ele não seja julgado culpado, vai acabar tudo."

    c "Hollywood vai dar um chute bem gostoso no velho asqueroso filho da puta."

    mc "Que delícia. Eu ia gostar tanto, Pri."

    mc "Mas e você? Você também ia ficar sem o filme."

    c "A gente vai falar mais sobre isso depois!"

    c "Me espera só mais um pouquinho! Continua vivo, gostoso!"

    mc "Hahaha... pode deixar, vou tentar."

    c "Agora fecha o olhinho... vou fazer um cafuné bem delícia."

    mc "Tá..."

    "A Pri é tão fofa..."

    c "Carinho... carinho..."

    "Força, [mc]... você vai conseguir."

    "Eles te menosprezam, mas você vai mostrar pra eles."

    "Diana... boa sorte na sua nova vida."

    "Será que eu devia ter ido contigo? Viver feliz do seu lado em algum lugar normal por aí?"

    "Não... esse não sou eu. Minha vida tá aqui."

    "Às vezes a gente toma soco na cara, às vezes a modelo mais conhecida do mundo te faz cafuné."

    "É uma loucura que não dá pra explicar."

    "Aproveita sua vida. Que eu vou tentar aproveitar a minha também. Aqui neste buraco entre o céu e o inferno."

    scene black with Dissolve(2.0)

    $ persistent.diana_final2 = True

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 2 da Diana! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    $ diana_terminou = True

    scene white with dissolve

    jump call_cidade

label diana_final3:

    $ diana_final3 = True

    "Se eu falar algo agora, eu coloco minha vida, a vida da Diana e da Sofia em risco."

    "Além de que eu ia perder todos os pontos que eu conquistei com os poderosos."

    "Desculpa, Diana, mas não dá pra fazer nada..."

    ba "Tá vendo, vadia?! Você não é ninguém! Ninguém vai mexer o dedo por você!"

    d "P-por favor!"

    mc "..."

    ba "Agora você vai ver o que acontece com quem me desobedece."

    d "Nããão!"

    play sound som_hit

    scene diana7_img39 with vpunch

    ba "Sua, cadela!"

    d "Aahhh!"

    play sound som_hit

    ba "Toma, vadia!"

    d "Aaiii!!!"

    "Merda... Ele vai acabar com ela..."

    play sound som_hit

    scene diana7_img48 with vpunch

    d "Ai... nnnggg... nnnghh..."

    "Mas eu não vou fazer nada. Aguenta, Diana..."

    ba "Chora, não, vadia! Eu ainda não acabei!"

    play sound som_hit

    scene diana7_img39 with vpunch

    d "AAAAHHHH!!!"

    scene diana7_img50 with vpunch

    na "PARE! SEU MONSTRO!"

    "Natasha!"

    ba "Você é outra cadela sem valor!"

    pr "Natasha! Não se intrometa..."

    ba "Nenhuma mulher vai me falar o que fazer!"

    ba "Eu MANDO nessa porra! Eu MANDO EM TODAS VOCÊS!"

    scene diana7_img39 with vpunch

    ba "Quando o homem fala, a mulher abaixa a cabeça, entendeu?!"

    ba "Vocês só servem pra serem putas no meu Cassino!"

    mc "..."

    ba "E agora deixa eu continuar... ensinar algo pra vocês duas."

    d "NÃÃÃÃÃOOOO!!!!"

    play sound som_hit

    scene red with vpunch

    pause

    play sound som_hit

    scene diana7_img47 with vpunch

    ba "EII!!!"

    mar "Vamos com cuidado, Barão. Por favor, senhor."

    ba "Marco! Me solta, segurança do caralho! Não me toca!"

    mar "Só tô seguindo ordens do chefe, senhor."

    scene diana7_img49 with hpunch

    to "Eu mandei ele segurar."

    ba "E quem você pensa que é, Tony?! Manda ele me soltar agora!"

    to "Peço desculpas, senhor... mas você sabe o que está em jogo aqui."

    "O Tony... e o Marco..."

    pr "Finalmente, Tony."

    to "Desculpa a demora, senhor. Eu devia ter chegado mais rápido."

    pr "Eu sabia que essa não era uma boa ideia. Você errou, Natasha."

    na "S-senhor..."

    pr "Vamos parar com isso agora. Esta festa foi um erro."

    ba "Por causa desta vadia!"

    to "Vamos todos nos acalmar."

    ba "Foda-se, Tony. Seu sogro nunca vai publicar isso."

    to "Mesmo assim, senhor."

    ba "Tudo bem. Eu parei. Pode me soltar, Marco."

    scene black with dissolve

    scene diana7_img52 with Dissolve(1.0)

    ba "O show acabou! Todo mundo circulando!"

    na "Eu vou levar a Diana pro quarto dela."

    pr "Isso. Cuide dela."

    menu:
        "Eu vou nessa também. Obrigado pelo convite.":


            pass

    ba "Você não, [mc]. Nem você, nem o Tony."

    to "Hm?"

    ba "Eu quero ir com vocês em um lugar. Se o prefeito também quiser."

    pr "De forma alguma. Eu fiquei tempo demais aqui."

    na "Assim que eu deixar ela lá, eu já pego nosso carro, senhor."

    pr "Ficarei no aguardo."

    scene black with dissolve

    scene diana7_img89 with Dissolve(1.0)

    pr "E você? O que tá planejando com o Tony e o garoto?"

    ba "Quero falar sobre a situação da idiota."

    pr "Ela não é idiota. Ela é a chave."

    to "O prefeito [pr] tem razão, senhor Barão. Tudo estava explicado no contrato."

    ba "Contratos, contratos... eu não sou um homem que lê as letras minúsculas."

    ba "Pra mim, um aperto de mão é o suficiente."

    pr "..."

    to "Talvez fosse bom eu revisar o contrato com ele, prefeito."

    pr "Essa é uma boa ideia. E ele já está afim de um encontro com vocês pra falar sobre a Diana."

    ba "Você vem, Basílio?"

    pr "Não. Acho bom vocês irem até o bar do Tony."

    to "Mas levar o paparazzo?"

    ba "Ele já conhece."

    to "Mas..."

    if diana_e6 == "barao":

        ba "Inclusive levei ele na sala."

        to "Você é louco, Marcos?! Sem minha presença?!"

        ba "O que você disse?"

        to "Aquela sala... você sabe que ela tem uma cópia de tudo!"

        ba "Você tá alterado demais."
    else:


        ba "Ele não entrou na sala, mas não vejo problema."



    to "Eu não concordo... apesar que agora estarei junto..."

    to "Eu já levei o [mc] lá. Mas... agora é diferente."

    pr "Escute o Tony."

    ba "O Tony é o cara da limpeza. Eu já tenho que ter cuidado com o Luca, não vou ter com ele."

    to "..."

    pr "Não quero me intrometer nisso. Vocês se entendam. Só não façam mais bagunça esta noite."

    ba "E você não seja tão medroso."

    scene black with dissolve

    scene diana7_img90 with Dissolve(1.0)

    pr "Medroso?! Eu?!"

    ba "Calma aí."

    pr "Sou eu que mantenho essa porra toda funcionando!"

    pr "Sem mim, todos vocês já teriam se comido! E tudo teria ido pro saco!"

    ba "F-foi uma brincadeira. Não fique assim."

    pr "Você não entende, né, Marcos?!"

    pr "Não entende que se eu não vencer as eleições, tudo acaba!"

    to "Senhor..."

    menu:
        "{i}Eles tão olhando pra mim...{/i}":


            pass

    pr "Ok... eu entendi... falamos sobre isso outro dia."

    pr "Vão pro bar e discutam o que precisam discutir. O que aconteceu com a sacerdotisa hoje não pode ocorrer novamente."

    ba "Bah..."

    to "Vamos. O Marco vai nos levar."

    ba "Você vem, não vem, [mc]?"

    mc "E-eu..."

    "Eu vou me envolver mais com esses caras?"

    "Quero fazer ainda mais parte desse grupo que comanda a ilha?"

    "Ou é melhor eu só fazer minhas coisas e dar o fora?"

    menu:
        "Sim. Eu vou com vocês, amigos.":


            $ diana_grupo = True

            scene black with dissolve

            scene diana7_img14 with Dissolve(1.0)

            ba "Esse é meu garoto. Você vai ser grande, [mc]."

            ba "Tony, chama o Marco. Estamos saindo."

            to "Sim... senhor..."

            scene black with dissolve

            pause 2.0

            scene bar_tony1 with Dissolve(1.0)

            "De novo eu tô aqui."

            "No lugar que eu conversei com o Barão pela primeira vez."

            "No lugar em que o Tony trouxe a Nona."

            "E se aqui for o coração da operação deles?"

            to "Vamos conversar aqui? Querem um drink?"

            ba "Deixamos pra depois. Vamos pra sala."

            to "Barão!"

            ba "Eu confio nele, Tony."



            if diana_e6 == "barao":

                ba "E eu te disse que ele já viu."

                to "Eu sei... Eu e ele já conversamos lá. Mas agora é diferente."

                ba "Que seja. Vamos logo."

            to "Ok... mas olha, só, garoto. É pra ficar de bico calado, ouviu?"

            menu:
                "Pode deixar.":


                    pass

            to "E não olhe demais nas coisas."

            ba "Não trate assim nosso convidado. Vamos."

            scene black with dissolve

            scene diana7_img91 with Dissolve(1.0)

            "Esta sala..."

            "Não acredito que eu tô com dois figurão da capital no lugar de trabalho deles."

            "Eu tô cada vez mais perto deles. Do grupo que comanda a ilha."

            "Mas isso... essa é uma boa pra mim?"

            "Eu sei como eles tratam as pessoas. Nem eles mesmo se toleram às vezes."

            "Me sinto numa selva. E quem der mole primeiro é devorado."

            "Se eu for por esse caminho... preciso ser tão forte, frio e calculista quanto eles."

            menu:
                "Essa sala realmente tá diferente...":


                    pass

            scene black with dissolve

            scene diana7_img92 with Dissolve(1.0)

            "Das outras vezes não tinha esse negócio aqui."

            "S-será que é droga?! Nessa quantidade?!"

            to "O que foi garoto?"

            menu:
                "O que... o que é isso aqui?":


                    ba "Haha... esse é nosso segredo."

                    mc "Parece... droga."

                    to "É droga. Mas nenhuma que você ouviu falar."

                    to "Coisa nova. O pessoal tá apelidando de Pó Mágico."

                    ba "Pó Mágico é foda hahahaha!"

                    to "Coisa pesada. Mas tão prometendo que isso não faz mal no longo prazo. Só se exagerar na dose."

                    mc "Eita..."

                    to "Quer experimentar?"

                    menu:
                        "Manda.":


                            to "Tem 10 pau aí?"

                            if cash >= 10000:

                                mc "Tenho... mas não vou gastar com isso."
                            else:


                                mc "Tá louco?"

                            to "Então nada feito. Sem produto pra você."
                        "Melhor eu passar...":


                            to "Homem esperto. Produto é pra vender, não pra usar."
                "N-nada, não...":


                    to "É apenas um produto. Não se preocupe."

            ba "Falando em produto... Ele ainda tá de olho?"

            to "Sim..."

            ba "Ainda não conseguiu comprar o sujeito?"

            to "Não. E tenho quase certeza que foi esse detetive que trouxe o cara da Interpol."

            ba "Não acredito! O sujeito ainda tá aqui?"

            to "Sim."

            ba "Caralho, Tony. Isso vai dar merda."

            to "Eu ainda pego ele na hora certa. O homem é esperto. E não quero sujar as mãos erradas de sangue."

            ba "Já falei pra você dar seus pulos!"

            to "Enfim... se acomodem."

            menu:
                "Opa... vou sentar aqui. Igual da outra vez.":


                    pass

            scene black with dissolve

            scene diana7_img93 with Dissolve(1.0)

            to "Eu te trouxe aqui, Barão, pra te lembrar do contrato. Uma das vias está aqui."

            ba "Certeza que você quer me tratar assim, Tony?"

            ba "Você pode ser um Alighieri, mas você está muito abaixo. Você é um estranho no ninho, um outsider."

            to "EU!!! Eu... eu não sou de fora. Eu sou um Alighieri real. Em nome da minha falecida esposa."

            ba "Você pode ter chego aqui com esse charme, talvez você seja bom de cama, mas o sangue da família não está em suas veias."

            ba "É por isso que o Luca te colocou pra cuidar do lixo."

            to "..."

            "Ele tá furioso. O Barão não tem medo desse cara mesmo."

            to "Apenas releia o contrato. Tá aqui."

            ba "Eu não vou ler nada. [mc]. Leia pra mim."

            menu:
                "Agora mesmo, Barão. Me passa aqui, Tony.":


                    to "..."

            to "Tome."

            mc "Vamos lá."

            "Hm? Tem uma foto junto com o contrato."

            scene black with dissolve

            scene sacerdotisas1 with Dissolve(1.0)

            "Que foto é essa?!"

            to "Pode começar."

            mc "S-sim!"

            "{i}Contrato de entrega de Diana *REMOVIDO* à custódia de Marcos *REMOVIDO* no processo do ritual *REMOVIDO*.{/i}"

            ba "Esses caras são cheios de segredinho. Não dá moral."

            to "É importante. Continua lendo."

            "{i}Todos os dados foram removidos de ambientes digitais. Apenas duas versões impressas do contrato ficaram disponíveis.{/i}"

            "{i}Uma para cada parte do acordo.{/i}"

            "{i}As partes se comprometem a manter sigilo absoluto quanto à transação, sob pena de sanções em caso de vazamento.{/i}"

            "{i}As partes reconhecem que este contrato não tem e não pode ter qualquer respaldo legal devido à natureza da transação.{/i}"

            "{i}O passado da garota também foi apagado para evitar que a mesma tenha qualquer chance de vazar o ocorrido.{/i}"

            "{i}Marcos ficará responsável por fazer a proteção da sacerdotiza.{/i}"

            "{i}O acordo firmado entre o Distrito e o Grupo estabelece que ambas as partes deverão receber uma promessa de fidelidade.{/i}"

            "{i}Dessa forma, a Cidade Chinesa funcionará como mediadora da transação.{/i}"

            "{i}A família *REMOVIDO* já entregou sua parte para os cuidados do mediador, que repassará assim que receber a contrapartida.{/i}"

            "{i}No caso da família *REMOVIDO*, suas dívidas para com o Grupo foram totalmente apagadas como contrapartida.{/i}"

            "{i}Parte do acordo estabelece que a família deverá deixar a capital e ir para local não descriminado.{/i}"

            "{i}A família também renega qualquer direito de contato com a parte a partir da assinatura deste instrumento.{/i}"

            "{i}A parte do Grupo do contrato ficará protegida no cofre de um banco de segurança máxima.{/i}"

            "{i}Uma pessoa de confiança será designada para fazer a segurança pessoal e deverá responder caso o documento seja perdido.{/i}"

            "{i}Por fim, Marcos deverá fazer relatórios periódicos do desenvolvimento da sacerdotiza.{/i}"

            "{i}Ela deve apresentar plena saúde e desenvolvimento físico, mental e psicológico.{/i}"

            "{i}Falha em atender qualquer um dos parâmetros acordados acarretará em sanções extra judiciais.{/i}"

            "{i}E, por estarem assim justos e contratados, firmam o presente contrato em duas vias de igual teor e forma.{/i}"

            "{i}E na presença das testemunhas, que subscrevem, obrigam-se, por si e seus sucessores, a cumprir o aqui disposto.{/i}"

            menu:
                "Acaba aqui.":


                    pass

            to "Obrigado, [mc]."

            "Um contrato que diz que a Diana foi... vendida?"

            if sacerdotisas > 0:

                "É o mesmo contrato que eu li na sala do Gevanni."

                "Tipo, exatamente o mesmo contrato que colocou a Júlia na casa da Sayuri!"
            else:


                "Fico pensando se isso aconteceu com outra das garotas..."

                "Se envolve a Cidade Chinesa, o Grupo e o Distrito, então talvez outras tenham entrado nesse rolo também."

            scene black with dissolve

            scene diana7_img93 with Dissolve(1.0)

            ba "E daí? O que eu tenho a ver com isso?"

            to "Você prestou atenção nesta parte?"

            to "'Marcos ficará responsável por fazer a proteção da sacerdotiza.'"

            ba "Ela vai ficar bem, Tony! Eu garanto!"

            to "Você não tem cabeça. Você se irrita. Deixa as emoções tomarem conta, quanto tá irritado, frustrado, contrariado."

            to "Você viu o que você fez com ela?"

            ba "Para com isso. Ela não é de vidro."

            ba "Fala aí, [mc]. Você acha que eu fui severo demais com ela? Seja sincero, rapaz!"

            menu:
                "Não, Barão. Você só deu o que ela mereceu.":


                    ba "Tá vendo?!"
                "Pra quem deveria proteger ela... você foi bem severo.":


                    ba "Garoto! Eu que te trouxe aqui!"

                    to "Não desconte nele."

            to "Você é um perigo pra tudo o que estamos tentando fazer."

            to "Seu temperamento precisa estar sob controle. A sacerdotisa PRECISA estar bem, para que tudo aconteça como precisa."

            ba "Eu já disse que ela vai ficar bem."

            scene black with dissolve

            scene diana7_img94 with Dissolve(1.0)

            to "Não, Marcos... você não está entendendo."

            ba "Hm?"

            to "Você nunca mais vai encostar um dedo nela. Não importa como."

            ba "Ela é minha, entendeu?!"

            to "Se eu descobrir que essa garota tem uma cicatriz, uma marca, uma ferida, no corpo ou na cabeça dela."

            to "Eu e o Marco vamos aparecer na sua sala com uma serra. E ele vai te segurar igual ele segurou hoje."

            to "E eu vou cortar todos os seus dedos, um por um, depois todos os seus membros, um por um."

            to "E vou colocar uma das suas putas do Cassino pra te deixar de pau duro, pra eu poder cortar ele direito."

            ba "Seu filho da puta! Eu te pago! Você não é nada sem mim!"

            to "Você esqueceu o que você mesmo disse?"

            ba "Hm?"

            to "Vocês me pagam pra limpar o lixo. E, hoje, você tá sendo o lixo que eu tenho que limpar."

            to "Então... diga que estamos entendendo, antes que eu seja obrigado a te atirar no rio por estar FEDENDO DEMAIS."

            ba "Eu vou explodir seus m... q-quer saber? Foda-se."

            ba "Posso ter a mulher que eu quiser. Eu sou o homem mais rico desta cidade!"

            to "Exatamente, senhor."

            ba "Heh... mesmo me dando vontade de meter chumbo nessa sua cabeça oca, eu sei que contratamos o homem certo."

            to "Vocês são espertos, Barão. Encontraram alguém que precisa lutar pelo lugar dele."

            to "Não nasci com o sangue, como o senhor mesmo disse."

            to "E se algo der errado, imagina quem vai ser o primeiro a se foder."

            ba "É bom que você saiba seu lugar."

            to "Só estou defendendo seus interesses. Então estamos entendidos?"

            ba "Sim. Eu precisava de um pouco de senso. Não quero perder o que eu tenho."

            scene black with dissolve

            scene diana7_img95 with Dissolve(1.0)

            ba "E qual é o próximo passo?"

            menu:
                "Próximo passo? Eles vão me falar o que tão planejando?!":


                    pass

            to "Eu gostaria de falar, mas com ele aqui."

            ba "Te falei que o moleque tá comigo, porra. Fala aí, pô!"

            menu:
                "Também quero fazer parte disso. Podem contar comigo.":


                    ba "Esse garoto tem gana, Tony."

                    to "Esse paparazzo tá envolvido em muita coisa."

                    mc "Eu?"

                    to "Se ele tiver falando a verdade, talvez seja útil."

                    mc "Claro que eu tô!"

                    mc "Eu quero fazer parte dos esquemas também!"

                    ba "Olha o jeito que ele fala! Hahaha!"

                    ba "Confia nele. O que tá rolando?"

                    to "Bom... ainda tenho que afinar tudo com o prefeito, mas provavelmente nosso foco será a Zaza."

                    ba "Não vou com a cara da velha. Ela é feminista demais pro meu gosto."

                    to "O Gustav tá com a corda no pescoço."

                    ba "Tony, a gente gasta milhões pra molhar a mão desses vagabundos! Essa juíza não tá na folha?!"

                    to "Não."

                    ba "Mas e o outro jeito?"

                    to "Também não adianta. Ela tem segurança particular. Seria arriscado demais."

                    ba "Filha da puta!"

                    ba "Se a gente perder a grana do Gustav... entendi... por isso vocês levantaram a Zaza."

                    to "Ela já é um investimento antigo. Mas sem o Gustav, a gente precisa de outra vitrini pra nossas garotas."

                    scene black with dissolve

                    scene diana7_img96 with Dissolve(1.0)

                    "Eles querem que a Zaza dê certo... e o Nathan é peça fundamental disso."

                    "Se ele continuar com eles, a Blergh! vai explodir. Mas se ele não continuar..."

                    "Será que eu entro nessa?"

                    menu:
                        "Eu sou amigo do Nathan. Posso ajudar.":


                            $ grupo_nathan = 1

                            ba "Quem é esse? O modelo?"

                            to "Sim. A Zaza tá na mão dele."

                            ba "Como?"

                            mc "A matéria que a Cássia fez, com todo o rolo dele ser deportado."

                            to "Exatamente. Ele ganhou projeção nacional."

                            mc "Só que ele tá em dúvida se ele continua nessa vida ou não."

                            to "E você pode soprar algo no ouvido dele, pelo que entendi."

                            mc "Sim. Deixa comigo. Vou fazer ele continuar com a Blergh! e vocês vão ter a grana, e a vitrine."

                            ba "HAHAHA! Olha esse doido, Tony!"

                            to "Muito bem. Se você conseguir, vou te considerar como um amigo."

                            ba "É sua chance, garoto! Não desperdiça!"

                            mc "Vou fazer meu melhor e provar que eu tô no nível de vocês."

                            to "Heh... vamos ver."

                            "É isso! Essa é minha chance! Tenho que fazer o Nathan continuar na Blergh!"

                            "E se eu conseguir... eles vão me olhar com outros olhos. Tenho que aproveitar essa oportunidade."
                        "Vou ficar quieto.":


                            "Não vou colocar o do Nathan na reta assim."

                            mc "..."
                "Já me intrometi demais. Melhor vocês falarem sozinhos.":


                    to "Ele tem razão. Depois conversamos o resto. Depois que eu falar com o Basílio."

                    ba "Aprovo."

            to "Então encerramos aqui."

            ba "E aí, garoto. Gostou de tá com gente grande?"

            menu:
                "Me senti parte da cúpula.":


                    pass

            ba "Isso aí, porra!"

            to "E que fique claro, [mc], se qualquer coisa aqui vazar... vou saber que é você."

            mc "P-pode deixar. Ninguém vai saber nada."

            to "Muito bom."

            to "Agora vamos. Vou fechar o bar."

            ba "A gente se fala em breve."

            mc "Falou."
        "Acho melhor eu deixar vocês.":


            scene black with dissolve

            scene diana7_img31 with Dissolve(1.0)

            "Eu não vou me meter nessa."

            mc "Eu só não queria me intrometer no negócio de vocês."

            mc "Acho que eu não tenho cacife pra me juntar. Vou nessa."

            ba "Do que você tá falando, caralho?! Eu que tô te chamando!"

            pr "Se ele não quer, é melhor, Barão."

            ba "Bah... falou, fedelho."

            mc "Até mais a todos."

            to "Até..."

    "Ufa... tô saindo dessa..."

    "Ainda tô vivo... e acho que ninguém tá correndo risco."

    scene black with dissolve

    pause 2.0

    scene capital_final with Dissolve(1.0)

    "Então assim que a festa no Cassino acabou."

    "O plano da Diana não deu certo. E ela vai viver pra sempre nas mãos do Barão pelo jeito."

    if diana_grupo:

        "Ou até que aquele ritual que tava no contrato aconteça."

        "Esses caras são malucos... eu vou querer participar disso mesmo?"

    "Ela tava contando que eu ia publicar aquele vídeo e implodir o Cassino com o escândalo."

    "Mas eu não entrei no jogo dela."

    "Eu mudei a vida dela pra sempre. Pro bem ou pro mal."

    "E nessa eu me salvei e salvei a Sofia também. Que não publicou o vídeo."

    "E a própria Diana pode ter evitado um final pior. Não é o que ela queria, mas ela tá viva e vai ter uma boa vida no Cassino."

    "Uma vida por duas, possivelmente três. O saldo parece positivo."

    "Nem sempre o caminho certo é o mais heróico. Às vezes, a gente tem que ser pé no chão."

    "Agora é ir pra casa e continuar indo por esse caminho.{nw}"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    mc "Hm? Diana?"

    "{i}Me encontra aqui no meu apê por favor{/i}"

    "Que história é essa? Por que ela ia querer falar comigo?"

    "Depois do que eu fiz... sei lá... isso não tá me cheirando bem."

    "Não tô me sentindo bem depois de ter deixado ela pra trás."

    "O que eu faço?"

    menu:
        "Ir até o apartamento falar com a Diana":


            "Eu não posso deixar a Diana sozinha agora. Ela precisa de mim."

            mc "{i}Tô chegando.{/i}"

            "Mas o que eu vou falar pra ela?"

            scene black with dissolve

            pause 1.0

            play sound som_porta

            pause 1.0

            scene diana7_img97 with Dissolve(1.0)

            mc "Oi... como você tá?"

            d "..."

            mc "Não precisa falar. Eu sei..."

            menu:
                "Você contava comigo, né? E eu te decepcionei.":


                    pass

            d "É muito mais que decepção."

            d "Eu pensei que você estivesse comigo. Que você estivesse do meu lado."

            menu:
                "Eu tava. Essa foi a forma que eu achei de te salvar. De você mesma.":


                    pass
                "Preferi ficar do lado deles. É melhor pra mim.":


                    pass

            d "[mc]..."

            d "Eu nunca escolhi estar aqui. Alguém decidiu que eu seria a boneca de um pedaço de bosta."

            d "Quem decidiu isso? Meus pais? Deus?"

            "Será que a Diana sabe do contrato?"

            "Será que ela sabe que ela é uma 'sacerdotisa'?"

            menu:
                "Não sei quem escolheu. Mas temos que fazer o melhor com o que nós temos.":


                    pass

            mc "Você é uma mulher sensacional. Talentosa, artística, sensível."

            mc "Faça a melhor jogada que você puder com a mão que você recebeu."

            d "É fácil falar, quando você tem o mundo todo pra ir."

            mc "Tenho mesmo?"

            mc "Trabalho no único lugar que me aceitou. No bico do corvo. A uma pauta de perder tudo."

            mc "Você acha que tá presa é só sua condição?"

            mc "Nós que temos que ralar todos os dias pra pagar os boleto no fim do mês tamo livre de verdade?"

            mc "Será que a gente faz o que a gente quer? Que a gente tá livre de verdade?"

            d "Estamos todos fodidos?"

            mc "Sabe quem não tá?"

            d "Os filhos da puta que nos controlam."

            mc "É o que eu acho. Esses caras, sim, estão acima de tudo."

            menu:
                "E é por isso que eu vou acabar com eles.":


                    mc "Não posso morrer aqui."

                    d "Eu acho que você perdeu a chance de acabar com o Barão hoje."

                    mc "Pode ser... mas pelo menos vou ver o dia nascer mais uma vez."
                "E é por isso que eu vou me unir a eles.":


                    d "Vai? Você quer ser um desses filhos da puta?"

                    mc "E você não quer? Não prefere ver a cidade de cima pra baixo? Igual eles?"

            d "Eu não quero nada com essas pessoas. Eu só quero minha vida. MINHA."

            d "Longe desse falso glamour, das mãos desses cretinos. Quero só poder ir pra outro lugar."

            mc "Infelizmente isso não vai acontecer hoje. Mas e amanhã?"

            d "Não sei se tenho força pra continuar..."

            menu:
                "Enquanto a gente viver, a gente tem chance.":


                    pass

            mc "Acabar com tudo tira todas minhas oportunidades. E isso eu não vou fazer."

            mc "Prefiro lutar até minha última gota de sangue. E ver o que a vida tem pra mim."

            d "Falando assim, parece que pode ter uma chance, algum dia."

            mc "É o que eu espero pra mim também."

            d "Se as coisas melhorarem pra você, você me avisa?"

            mc "Digo o mesmo."

            scene black with dissolve

            scene diana7_img98 with Dissolve(1.0)

            d "Eu vou ficar um tempo sozinha agora."

            if diana_namoro:

                $ diana_rompeu = True

                mc "E nosso relacionamento?"

                d "Eu não tenho força pra outra pessoa agora, [mc]. Mal tenho pra mim."

                menu:
                    "Então tá tudo acabado entre nós?":


                        pass

                d "Sim..."

                mc "Você foi a mulher mais incrível que eu tive algo neste inferno."

                d "E você o único homem pelo qual eu senti algo neste inferno."

            d "Te desejo o melhor, [mc]. Que você chegue onde você deseja."

            mc "Digo o mesmo. Recupere seu brilho. O mesmo que você tinha quando te vi na praia a primeira vez."

            d "A estrela morreu. A luz que você vê, é apenas um passado distante."

            mc "Diana... fica bem."

            d "..."

            mc "Até mais."
        "Agora sou do Grupo. Encerrar tudo aqui e nunca mais falar com ela":


            $ diana_negou = True

            "Não. Meus assuntos com a Diana estão encerrados."

            "Agora eu tô com o grupo."

            mc "{i}Não podemos mais nos ver. Desejo tudo de melhor pra você.{/i}"

            "{i}Contato bloqueado{/i}"

    "A Capital é um lugar repleto de possibilidades, mas cheio de buracos."

    "Um pote de ouro no final de um caminho cheio de abismos."

    "Será que eu ainda tô no caminho? Ou eu já caí e não sei?"

    "Vamos pra casa..."

    scene black with Dissolve(2.0)

    $ persistent.diana_final3 = True

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 3 da Diana! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    scene white with dissolve

    jump call_cidade

label diana_evento6:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d6_save", extra_info="d6_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ diana_e6 = "evento"

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você deverá ser corajoso e ficar do lado de quem precisa mais de você."

        p "Só que... é preciso saber a hora de parar. Deixe seu orgulho de lado e aceite seu lugar."

        p rindo "E aí? Você vai preferir a pauta ou ficar do lado dos poderosos? Aqui, você decide! Boa sorte!"

    "Eu sinto que eu tô conseguindo me manter bem aqui na cidade levando em consideração as circunstâncias."

    "Só que parece que cada vez mais as coisas tão mais tensas. Tem muita coisa errada nessa cidade."

    "Eu sempre lembro da [d]. Aquela vez ela tava tão triste no bar. É claro que tem alguma coisa acontecendo com ela."

    if diana_namoro:

        "Mesmo naquela vibe eu acabei me declarando pra ela e ela aceitou namorar comigo. Foi incrível."
    else:


        "Acho que eu consegui ajudar ela um pouco, mas mesmo assim foi muito pouco."

    "O que será que eu posso fazer que realmente vai livrar disso tudo?"

    "Com certeza esse rolo passa pelo Barão. Do jeito que a [d] fala dele, e também aquela vez no apartamento dela..."

    "Trrr"

    mc desconfiado "Hm? Uma mensagem de voz da [d]..."

    "{i}Oi. Desculpa falar em cima da hora, mas você poderia ir a um bar comigo? Fica do lado da pizzaria que a gente saiu aquela vez.{/i}"

    "{i}Não queria sair sozinha esta noite. Você poderia me acompanhar? Estarei te esperando lá. É do lado da pizzaria.{/i}"

    "Ela quer se encontrar comigo nesse bar. É perto da pizzaria que a gente saiu aquela vez."

    scene ape_chuveiro with Dissolve(1.0)

    "Eu que não vou negar o pedido de uma mulher dessas."

    if diana_namoro:

        "Agora que a gente tá namorando, eu tenho que fazer alguma coisa pra tirar ela dessa."

    "A [d] é uma das únicas pessoas que eu conheço que realmente se preocupou comigo."

    "Além de que ela tá envolvida em um lance com pessoas poderosas. Certeza que tem uma pauta pra mim aí."

    "Eu preciso de algo novo pra revista ou o chefe vai me demitir logo."

    "Tá bom de banho... Bora pra lá."

    scene black with dissolve

    call locomocao from _call_locomocao_19

    scene cidade pizzaria with Dissolve(1.0)

    pause

    "Ela disse que ficava aqui do lado. Hmm..."



    "O duro é que eu não tô vendo nada que se pareça com um bar. Parece tudo casa..."

    scene pizzaria_out_italiano with Dissolve(1.0)

    "Esse é o tal do [to]..."

    if v31_fim:

        "Ele tá todo enrolado no esquema do [gus]. Mesmo ele não tendo feito nada comigo, não dá pra confiar nele."

    "Mas talvez ele saiba onde fica esse bar aí."

    mc "Boa noite."

    to "Jovem... nos vemos aqui novamente."

    mc "Eu precisava da sua ajuda com uma coisa."

    to "Claro. Sente-se."

    menu:
        "É só uma pergunta rápida.":


            mc "Não tem necessidade. Só quero fazer uma pergunta rápida."

            to "Pois então pergunte."
        "Ok... Com licença.":


            mc "Beleza. Vou sentar aqui então."

            scene tony_pizzaria_mesa with Dissolve(1.0)

            mc "Eu não queria te alugar muito."

            to "Você fala como se eu estivesse atarefado. Estou apenas aproveitando a lua e uma boa bebida."

            mc "Você... costuma vir bastante pra cá?"

            to "Acredito que mais do que eu deveria. Mas... é que este lugar me lembra da minha esposa."

            mc "Ah. Faz tempo que você não vê ela?"

            to "Sim, algum tempo. Ela faleceu."

            mc "Meus pêsames."

            to "A única certeza da vida é a morte, não é mesmo?"

            mc desculpa "Tem razão..."

            to "Mesmo assim, sempre achamos que ela está longe. Fazemos planos para o futuro e perdemos tempo com mesquinharia."

            to "Imagino como seria nossa vida se soubessemos que teríamos apenas mais um ou dois anos antes do fim."

            mc preocupado "Seria um pouco desesperador."

            to "Mas será que não aproveitaríamos melhor nosso tempo? O ser humano tende a dar mais valor ao que é escasso."

            mc "Talvez... mas mesmo assim prefiro pensar que ainda tenho muitos anos pela frente."

            to "Eu também torço para isso. Mas, mesmo assim, tente aproveitar sempre o tempo que você tem."

            to "Se bem que... eu falando em você aproveitar o tempo e eu roubando ele de você. Que incoerência."

            to "Você disse que queria me perguntar algo."

            mc surpreso "S-sim! É..."

    mc normal "Uma amiga disse que tem um bar aqui ao lado, só que não achei a entrada. Você sabe que bar pode ser?"

    to "Ora... será que é o pub que estou pensando? Seria uma coincidência e tanto."

    mc "..."

    to "Que amiga seria essa?"

    "Será que é bom eu falar o nome da [d] assim?"

    menu:
        "Minha amiga é a cantora do cassino.":


            mc "O nome dela é [d], a cantora do cassino."

            to "Foi o que eu imaginei. Eu vi vocês juntos da outra vez."

            to "Então ele realmente trouxe ela para cá. Que desperdício..."

            mc "Como assim?"

            to "Não se preocupe. Estou falando sozinho. Eu tenho essa mania inconveniente."

            mc "Hm..."

            to "Mas se ela te chamou pra cá, então com certeza é o pub que eu tinha em mente."
        "Não é alguém que você conhece.":


            mc "Certeza que você não conheça ela. Mas ela disse que era aqui do lado."

            mc "Acho que vou mandar uma mensagem pra ela pra confirmar."

            to "Bom... o único bar dessas redondezas é esse pub que estou pensando. Só estou realmente surpreso que seja ele."

            to "Mas deve ser."

    to "Eu posso te ajudar a chegar lá. É bem aqui ao lado da pizzaria."

    mc "Mas não tem nenhuma porta ou algo assim..."

    to "É um bar um tanto quanto desconhecido. Por isso minha descrença quando você comentou."

    to "virando a sua direita, é a primeira porta. Ela está aberta."

    mc desconfiado "Certeza que é ali? Não tem nenhuma placa..."

    to "Pode confiar em mim. Caso ela não esteja lá, você pode apenas sair."

    mc concentrando "Faz sentido. Obrigado."

    to "Tenha uma boa noite."

    mc "Boa noite."

    scene black with dissolve

    "Ainda não sei qual é a desse cara."

    "Mas isso realmente não parece um bar. Espero que eu não esteja invadindo a casa de alguém..."

    "..."

    scene bar_tony1 with Dissolve(2.0)

    pause

    mc surpreso "..."

    "Que lugar chique. Quem diria..."

    "Por que alguém iria investir mó grana pra levantar isso aqui e depois esconder?"

    "E a porta ainda tava aberta... que loucura..."

    "A [d] tem que tá por aqui."

    scene d6_imagem1 with Dissolve(1.0)

    pause

    "Ela não ouviu eu entrando? Deve tá super concentrada com alguma coisa..."

    "Ela tava tão mal da outra vez. Espero que as coisas estejam melhor pra ela agora."

    "Acho que depende de mim também. Eu preciso ser uma boa companhia pra ela hoje."

    "Falando em companhia... parece que não tem mais ninguém aqui além da gente."

    if diana_namoro:

        "Agora que a gente tá namorando, pode ser a chance que eu preciso pra poder levar ela pra cama."

        "Ou pode ser aqui nos sofás mesmo. Não tem problema nenhum pra mim."

    elif diana_quente:

        "Eu e a [d] já se pegou, mas até agora nada oficial. Se pá, hoje é o dia de chegar nela."

        "Se eu perder essa chance... vou subir as escadas do prédio de joelho."
    else:


        "Talvez seja uma boa chance de eu e ela ter uma conversa mais íntima."

    if not nathan_namoro:

        "Agora, que a [d] tem um corpo do caralho... olha pra essas coxas..."

        "Ela é bem magrinha, mas na bunda e nas pernas, cristo..."

    "Deixa eu parar de viajar."

    mc charmoso "Boa noite, senhorita."

    d "O-oi!"

    scene d6_imagem2 with Dissolve(1.0)

    pause

    d "Ah. É você, [mc]."

    menu:
        "Como assim 'ah'? Decepcionada?":


            mc zerado "O que você quer dizer com 'ah'? Ficou decepcionada que era eu?"

            d "Não é isso..."
        "Tava esperando outra pessoa?":


            $ diana_seducao += 1

            mc desconfiado "Que foi? Parece que você achou que era outra pessoa."

            d "Sim, eu pensei."

            mc "Quem?"

            d "Ninguém interessante."

    d "Fiquei muito feliz de você vir. Desculpa pedir assim em cima da hora."

    mc normal "Tudo bem. Contanto que eu possa vir, nunca vai ser problema pra mim."

    d "Você é um verdadeiro cavalheiro. Sempre colocando as damas sobre seus próprios desejos."

    mc envergonhado "Alguns diriam que eu sou 'gado', isso sim."

    d "Como se as crianças de hoje soubessem como ser um homem de verdade. Idiota quem dá atenção a elas."

    if diana_namoro:

        mc charmoso "Olha... você aceitou namorar comigo, então alguma coisa de certo eu fiz."

        d "Você fez mais coisas certas do que você imagina."

        d "Eu queria muito te beijar agora, mas é melhor deixarmos pra depois, tudo bem?"

        mc desculpa "Tudo bem. Aconteceu alguma coisa?"

        d "Não é nada. Mas eu não conheço esse lugar, então não fico à vontade aqui."
    else:


        mc envergonhado "Acho que você tem razão..."

    d "Você é um pouco influenciado demais às vezes, [mc]. Eu fico preocupada com isso."

    mc envergonhado "Você fica? Por quê?"

    d "Porque pessoas boas acabam se ferrando muitas vezes."

    d "E é um pouco hipócrita da minha parte, porque eu faço o mesmo com você. Sempre te chamo pra me fazer companhia."

    menu:
        "Eu vim porque eu quis.":


            mc charmoso "Não pensa demais nisso, não. Eu vim aqui porque eu quis. Não é só por sua causa."

            d "Quer dizer que você também tem seus interesses comigo."

            mc "Claro."

            d "Mas é só comigo ou talvez tenha outros interesses?"

            mc "Eu sou um paparazzo... ficando do lado de famosos, eu sei que uma hora ou outra eu vou descobrir alguma coisa."

            d "Eu entendo perfeitamente. Inclusive, a gente se conheceu por causa disso, né?"

            mc "É verdade. Você tava incrível lá na praia."

            d "E você adora elogiar..."
        "Eu não ligo se for uma mulher gata.":


            $ diana_seducao += 2

            mc charmoso "Pode ser hipócrita. A gente nunca nega um pedido de uma mulher bonita."

            d "E você, como sempre, não perde a chance de tentar ganhar uns pontos."

            mc "Se tem uma coisa que eu aprendi, é que a gente precisa aceitar a verdade. Você devia fazer a mesma coisa."

            d "Aceitar que você é um womanizer?"

            mc envergonhado "Não sei o que é isso... mas parece negativo."

            d "Não sei se você é ingênuo mesmo ou se faz de bobo pra sair de enrascadas."

            mc "..."

    mc normal "Enfim, o que tá rolando aqui? Por que você não tá no cassino?"

    scene d6_imagem3 with Dissolve(1.0)

    pause

    d "Bem... o Barão não gostou muito do meu comportamento nos últimos dias."

    mc preocupado "Como assim?"

    d "Nas palavras dele, eu tenho saído muito e desrespeitado nosso acordo."

    mc "..."

    d "Então ele disse que queria que eu viesse pra cá um tempo."

    mc "O que isso quer dizer? Quero dizer, o que vir pra cá significa?"

    d "Ainda não sei. Eu não conhecia esse lugar até hoje. Inclusive é bem estranho um bar desses tá escondido aqui."

    mc envergonhado "Foi a mesma coisa que eu pensei. A fachada é de uma casa simples, e dentro um bar luxuoso desses?"

    d "E você? O que você acha que isso significa?"

    menu:
        "Eu acho que é uma coisa positiva.":


            $ diana_seducao += 1

            mc "Olha, esse bar aqui parece uma coisa bem exclusiva. Eu acho que pode ser uma boa coisa."

            mc "Talvez ele esteja querendo impressionar uma pessoa importante. E o cassino seria demais, talvez."

            d "É... isso já aconteceu antes. O Barão não tá sozinho. Eu já vi ele com várias figuras importantes."

            mc desculpa "É. Ele é dono do maior empreendimento da ilha."

            d "Se não for da cidade como um todo. É imposível saber quanto dinheiro rola naquele antro de desavisados."

            mc envergonhado "Verdade..."
        "Provavelmente ele quer punir você.":


            mc desculpa "Sendo sincero, acho que ele quer punir você mesmo. Até pelo que você disse que ele não gostou de algumas coisas aí."

            d "Sim... é o que parece."

            d "Ele não pode prejudicar um bem valioso de qualquer forma."

            mc desconfiado "Hm?"

            d "Nada..."

    mc "E ele? Ele não disse nada?"

    d "Praticamente. Só disse que eu ia parar com os shows no cassino e ser realocada para outro lugar por um tempo."

    mc desculpa "Parece coisa séria."

    d "Esse homem não brinca, [mc]. Tenha cuidado com ele."

    mc envergonhado "Ele é um homem famoso e bem ocupado. Acho difícil eu ter uma chance de falar com ele."

    d "É. Ele não costuma perder o tempo dele onde ele não vê valor."

    mc envergonhado "Você parece conhecer bastante o Barão, [d]. Mas você nunca contou como você acabou trabalhando no cassino."

    d "Senta comigo."

    scene d6_imagem4 with Dissolve(1.0)

    pause

    d "Não é uma história assim tão interessante. Não sei se você teria interesse."

    menu:
        "Com certeza é uma história que vale à pena.":


            mc normal "Essa história vale muito, [d]. Você é uma celebridade, caramba."

            d "Acho que você enxerga muito onde não tem, [mc]. Mas não vou reclamar."
        "Tudo o que tem a ver com você me interessa.":


            $ diana_seducao += 2

            mc charmoso "Eu quero saber tudo o que tem a ver com você."

            d "Você é muito cara de pau...{w} mas eu gosto mesmo assim."

            mc "Você acha que tudo o que eu falo é porque eu quero te impressionar. Você se acha muito."

            d "E eu tô errada?"

            mc "Prefiro não responder isso."

            d "Haha..."

    d "Já que você faz questão, eu vou contar."

    d "Essa é uma história que eu nunca contaria, se não fosse você me perguntando."

    mc charmoso "Informação exclusiva, então?"

    d "Se é assim que você quer pensar, mas não tem nada que você possa usar na sua revista eu acredito."

    mc "Não dá pra saber. Cada coisa que já foi parar naquela revista..."

    d "Eu conheço o Barão desde minha adolescência. Ela era bem jovem na época também."

    mc normal "Nossa."

    d "Pode não parecer, mas o Barão é bem novo. Quem olha pro cassino que ele levantou deve achar que ele é um velho."

    d "Mas você se surpreenderia se visse ele. O homem é totalmente diferente do que alguém que ouviu dele acharia."

    mc desconfiado "Sério? Ele não é um gordão de terno cheio de pompa?"

    d "Haha... de forma alguma. Se você visse ele como eu já vi algumas vezes, ele parece um personagem de um filme."

    d "As roupas que ele usa são no mínimo questionáveis. E ele tem uma mania idiota de andar armado."

    mc surpreso "Armado?!"

    scene d6_imagem5 with Dissolve(1.0)

    pause

    d "O que eu posso dizer? Ele é um idiota. Extremamente desnecessário. Várias coisas que ele faz são incoerentes."

    mc desconfiado "Eu imaginaria que um cara grande como esse seria mais... sei lá... experiente."

    d "Experiente? Isso é uma coisa que ele não é. Ele parece um sortudo burro que ganhou uma bolada na Mega Sena."

    d "A diferença é que ao invés de ganhar uma vez, ele ganha esse valor todos os dias."

    mc envergonhado "Praticamente dinheiro infinito..."

    d "Com o passar dos anos... duvido que alguém consiga usar tudo o que ele acumulou nesse tempo."

    d "Ele sabe que ele tá no topo da cadeia alimentar. E ele não faz nada pra esconder isso. Ele quer é que saibam."

    d "Todas as chances que ele tiver de demonstrar isso, ele vai mostrar. Mesmo que seja pra uma pessoa qualquer na rua."

    mc desculpa "Talvez tenha subido na cabeça dele..."

    d "Esse é o perigo. Nunca se sabe o que uma pessoa assim vai fazer, entende?"

    menu:
        "O que você acha disso?":


            mc "E o que você acha disse jeito dele?"

            d "Não é óbvio? Quem gostaria de depender de uma pessoa assim?"
        "Você não curte esse jeito dele...":


            $ diana_seducao += 1

            mc serio "Você não gosta desse jeito dele, né?"

            d "De forma alguma. É extremamente desnecessário e só causa transtornos para as pessoas."

    mc envergonhado "Mas ele pode... essa é a diferença dessas pessoas pra gente... eles tão em outro nível."

    d "Então você acha que pessoas que têm dinheiro e influência podem fazer o que eles querem?"

    mc serio "N-não é isso. Mas muitas pessoas assim são excêntricas pelo que eu vejo. E se ele não tá prejudicando ninguém..."

    scene d6_imagem6 with Dissolve(1.0)

    pause

    d "..."

    mc "Que foi? Falei merda?"

    d "Não é isso... é o contrário, inclusive... você tá certo..."

    d "Será que as pessoas enxergam o quanto essas pessoas prejudicam os outros?"

    mc "[d]... como assim?"

    d "Essas pessoas ricas e poderosas aparecem na televisão quando fazem doações e participam de eventos de caridade."

    d "Eles fazem propagandas de como eles ajudam a sociedade... é esse lado que todo mundo consegue ver."

    d "Mas e o que está na sombra, [mc]?"

    mc "As pessoas não podem julgar o que elas não conseguem ver..."

    d "Você tem razão. São poucos que sabem o que acontece por trás da cortina."

    mc "É... o Barão... você tá falando isso por causa dele?"

    d "Não só ele, [mc]. Mas ele também. O Barão prejudicou muita gente pra chegar onde ele tá. E continua fazendo isso até hoje."

    mc "Você também, [d]? Ele te prejudicou?"

    mc "Quando a gente se encontrou, você disse que precisava de alguém que levasse seu trabalho pra além do cassino..."

    mc "Desde aquela época... o que você quer fazer é sair de perto do cassino e do Barão?"

    d "É o que eu queria... mas eu já não sonho mais com isso."

    d "Os meus sonhos não trazem nenhum benefício pro Barão. Por isso ele os ignora."

    mc "[d]... ele não é só seu chefe? Por que ele teria tanta influencia na sua vida?"

    scene d6_imagem7 with Dissolve(1.0)

    d "Heh... quem dera fosse só isso, [mc]..."

    d "O Barão é dono da minha voz. Eu só posso cantar pra quem ele permite."

    mc "Como assim?! Isso tá certo?!"

    d "Nós temos um contrato. Eu só posso cantar nessas condições."

    d "Foi esse homem que trouxe minha voz pro mundo e ele pode levar ela pra onde quiser agora."

    mc desculpa "Isso não pode ser legal, [d]... ele deve tá infringindo alguma lei nisso."

    d "Mesmo que ele estivesse, [mc]. O que isso mudaria?"

    mc preocupado "Como assim? Você pode ir pra Justiça contra ele."

    d "Haha... e você acha que eu ganharia alguma com isso? Qual seria minha chance contra ele no tribunal?"

    mc desculpa "..."

    d "Mesmo que eu vencesse... qual seria minha chance no mundo? Quem contrataria uma cantora que processa seu patrocinador?"

    d "Tirando que o Barão tem muito mais influência do que eu. Ele me esmagaria ou... simplesmente... se chegasse nesse ponto..."

    mc "Hm?"

    d "Deixa pra lá."

    menu:
        "Sempre tem um jeito de sair de um problema.":


            mc serio "Tem que ter um jeito. Sempre tem um jeito da gente sair de um buraco."

            d "Isso pode funcionar nos filmes, [mc], mas não na vida real."

            d "Na vida, existe um limite real e bem definido do que uma pessoa pode fazer."

            mc desculpa "Merda... então eu não posso fazer nada?"

            if diana_namoro:

                mc preocupado "Um namorado que vê sua garota assim e não faz nada?!"
        "Desculpa se eu não posso ajudar...":


            $ diana_seducao += 2

            mc desculpa "Droga... só você o que tá passando. Desculpa se eu não posso ajudar... Eu me sinto um merda."

            if diana_namoro:

                mc "Mesmo sendo seu namorado... é muito frustrante não poder fazer nada!"

            d "Não seja bobo, [mc]. Você tem feito muito por mim."

            d "Você é a segunda pessoa pra quem eu conto isso. É como tirar um peso das costas poder falar."

            d "Às vezes... ouvir... mesmo parecendo pouco, é tudo o que a gente precisa."

            mc "Entendo... mas mesmo assim... eu queria poder fazer mais."

    scene d6_imagem8 with Dissolve(1.0)

    pause

    d "Por favor. Continue do meu lado. É tudo o que eu preciso agora."

    mc "..."

    "Se a [d] acha que eu vou ficar só esperando, ela tá muito enganada."

    "Não sei ainda se eu faria algo contra o Barão. Talvez isso seja perigoso demais pra um cara normal igual eu."

    "Mas eu não vou ficar só olhando. Com certeza eu não vou."

    "Eu tenho que tirar o máximo de cada oportunidade. E eu não vou deixar um escândalo desse passar assim."

    "A [d] é com certeza uma cantora talentosa. O Barão deve ter feito um contrato que vale por muitos anos."

    "Mas será que é só isso? Do jeito que ela fal-"

    d "[mc]? Tudo bem?"

    mc surpreso "Desculpa! Eu tava viajando..."

    d "Por favor, tente não pensar demais nisso. Se eu te contei, é porque eu julguei que você tinha maturidade suficiente."

    mc desculpa "Ok..."

    d "Obrigada. Agora, e se a gente aprovei-"

    "{i}clack clock{/i}"

    d "Hm?"

    mc desconfiado "Tem alguém abrindo a porta."

    scene d6_imagem9 with Dissolve(1.0)

    pause

    ba "Minha menina! Demorei?"

    if v29_fim:

        "Esse homem! Eu lembro dele!"

        "Quando eu tava investigando o Barão pra [na]... ele tava aqui do lado na pizzaria falando com o [to]."

        "Então ele realmente é o Barão?"

    d "Boa noite, Barão."

    $ ba_nome = "Barão"

    ba "O que foi? Você parece assustada. Não esperava que eu viria?"

    d "Você fala alto demais. Só isso."

    ba "HAHAHA!"

    ba "Você é toda delicadinha, menina. Parece de porcelana."

    d "..."

    ba "Deixa eu tirar meus óculos."

    scene d6_imagem10 with Dissolve(1.0)

    ba "E quem é esse sujeito aí? Ele trabalha aqui?"

    menu:
        "...":


            mc serio "..."

            d "Não. Ele é um amigo que veio a meu pedido. Eu não me senti confortável vindo aqui sozinha."

            ba "Então esse é o tal do [mc]. O paparazzo."

            d "Isso."
        "Meu nome é [mc]. Prazer.":


            mc normal "Com licença. Meu nome é [mc]. Prazer em conhecer você."

            ba "HAH! Então você é o [mc]."

            d "..."

            ba "Não acredito que vamos ter a chance de conversarmos."

    mc "Você... já me conhecia?"

    ba "A [d] já falou uma vez de você. Depois de eu insistir muito, é claro..."

    ba "Ela não gosta de falar da vida dela pra mim. Eu também não sei por que ela faz isso."

    ba "Eu considero ela minha melhor amiga. Será que o sentimento não é mútuo, querida?"

    d "..."

    ba "Tá vendo? Só tomo gelo."

    "Qual é a desse cara?"

    ba "Ei, [d]."

    d "Que foi?"

    scene d6_imagem11 with Dissolve(1.0)

    pause

    d "Q-que é isso?!"

    ba "Você tem um rabo incrível, sabia?"

    d "Você enlouqueceu?"

    "O que esse cara acha que tá fazendo?!"

    if diana_namoro:

        "Ela é minha, cara!"

        "Será que eu falo alguma coisa pra ele parar?"

        "E essa arma na cintura dele? Será que é uma boa confrontar esse cara aqui agora?"

        menu:
            "Melhor eu deixar a [d] resolver.":


                "Melhor eu deixar ela resolver. Eu preciso confiar na [d]."
            "Não posso deixar ele fazer o que quer.":


                "Eu não posso deixar ele fazer o que quiser com a [d]. A gente tá num lance sério agora."

                mc bravo "Ei!"

                ba "Hm?"

                d "Por favor! Deixa eu!"

                mc preocupado "[d]..."

                ba "Não precisa ficar assim, menina. Calma..."

                "Eu acho que isso que ela falou foi pra mim. Eu vou ter que me segurar por enquanto..."

    ba "Eu achei que só nós dois estaríamos aqui hoje."

    d "Eu não sabia que você viria."

    ba "Por que você achou que ia te chamar pra cá?"

    scene d6_imagem12 with Dissolve(1.0)

    pause

    ba "Eu queria aproveitar minha garota..."

    "!"

    d "C-como assim? Você... nunca olhou pra mim desse jeito."

    d "Inclusive, foi você quem disse que nunca ninguém poderia mexer no seu bem mais precioso, n-não foi?"

    ba "Isso era antes... quando você era a estrela do cassino."

    d "Você tá brincando comigo?"

    ba "De jeito nenhum. Eu disse pra você que as coisas iam mudar, não disse?"

    ba "Você atraiu muita gente pro cassino com sua voz. Realmente, nunca teria crescido como eu cresci sem você."

    d "Eu sei. Eu sei m-muito bem o meu valor."

    ba "Só que... eu acho que a fama subiu um pouco sua cabeça, não acha?"

    d "Por que você está falando isso?"

    ba "Suas 'saidinhas'... suas conversinhas com esse... [mc]... e outras pessoas. Você não era assim, querida."

    ba "Alguma coisa fez você achar que pode me desobedecer. Acho que você entendeu 'seu valor', e isso te deu coragem."

    d "N-não é nada disso..."

    ba "Mas eu vou fazer você entender rapidinho que no Cassino do Barão a única peça imutável é o Barão."

    d "V-você tá sendo r-rídulo."

    ba "Calma... não precisa ficar nervosa desse jeito. Esse sorriso nervoso não combina com você."

    ba "Vai lá pra trás, do lado do piano e se prepara pra cantar. Você vai entreter eu e o [mc] esta noite."

    d "E-eu-"

    ba "Vai logo!"

    ba "E você senta comigo, [mc]."

    scene black with dissolve

    scene d6_imagem13 with Dissolve(1.0)

    pause

    ba "Então você é o amiguinho dela. Vocês ficam de segredinho sempre?"

    "O que tá acontecendo aqui? O que passa na cabeça desse cara?"

    "Pelo que a [d] falou, ele é meio explosivo. É bom eu tomar muito cuidado com o que eu vou falar se eu não quiser acabar com um buraco no peito."

    menu:
        "Eu sou só um paparazzo.":


            mc "Eu sou um paparazzo que trabalha pra revista da ilha, só isso."

            ba "Você tá de olho em podres dela para publicar então?"

            mc "Não é só 'podres', mas qualquer informação relevante sobre ela. As pessoas têm interesse na [d]."

            ba "Eu imagino que tenham mesmo. {w}Mas então a relação de vocês é apenas profissional. Eu achei que fosse totalmente outra coisa."

            mc "Sério?"
        "Nós somos bons amigos.":


            mc "Nós somos bons amigos."

            ba "Bons amigos? Quão 'bons'?"

            mc "Sei lá. Ela conta as coisas dela pra mim e eu pra ela. Não tem muito segredo. É uma amizade comum."

            ba "{i}Hmf{/i}"

    ba "A [d] é uma garota fechada. Se ela te contou alguma coisa mais pessoal, isso já é coisa demais pra um cara igual você."

    mc "Igual eu?"

    ba "É. Uma pessoa normal. Sem muitos benefícios, captou? A garota está em um mundo diferente do seu."

    ba "Já teve gente que ofereceu seis dígitos pra passar uma noite com ela. Esse é o tipo de ambiente que ela cresceu."

    ba "Um homem que trabalha pra comer e pagar, sei lá, aluguel e ônibus nunca vai entender o que é isso."

    mc "Haha... com certeza."

    ba "Hmm... e isso não te incomoda? Eu me sentiria super deslocado se eu fosse você."

    mc "Pior que não. Se fosse um tempo atrás, provavelmente eu me sentiria, mas hoje em dia, não."

    mc "Meu trabalho fez eu ficar perto de bastante gente grande aqui na cidade."

    ba "E o que você achou dessa vida?"

    menu:
        "Hoje eu me sinto uma pessoa grande também.":


            mc "A verdade é que eu me sinto poderoso também hoje. Eu sei do meu valor."

            ba "Hah! Por que você acha isso?"

            mc "Olha... eu sei da minha influência na opinião das pessoas com a revista. Eu não sou o dono, mas eu posso publicar verdades lá."

            mc "Eu também tô do lado de várias pessoas importantes. E muitas até já me pediram favores."

            mc "Outros já me chamaram pra fazer parte também. Então por tudo isso eu acho que eu não sou mais o pobre coitado que chegou aqui."

            ba "Parece um jeito conveniente de pensar. Mas talvez você tenha razão, quem sabe..."
        "Eu percebi que os poderosos são idiotas.":


            mc "Hehe... não vai me levar à mal, ok? Mas o que eu concluí é que os poderosos são bem idiotas."

            ba "Haha! Como é?"

            mc "Acho que todas pessoas com algum poder que eu encontrei nesta ilha eram perturbadas."

            mc "Eram egoístas, muitas eram maldosas mesmo. Acho que ninguém usava seu poder pensando nos outros, sabe?"

            mc "Pra mim isso é a mesma coisa que ser um babaca ou uma babaca mesmo."

            ba "Você é puritano, [mc]. Essa sim é uma forma idiota de ver o mundo. Essa coisa de bonzinho e ajudar os necessitados é meio fraca."

            mc "Sei..."

    scene d6_imagem14 with Dissolve(1.0)

    ba "Sua visão sobre o que é poder tá limitada pela sua vida. Quem olha algo de baixo pra cima é diferente de quem olha de cima pra baixo."

    ba "Você só vai poder sentir o que é poder de verdade quando você tiver ele em suas mãos. Quando você sentir o cheiro dele."

    ba "Antes disso, você não passa de um otário falando sobre o que não sabe."

    mc "Será mesmo?"

    ba "Óbvio."

    mc "Será que eu preciso ser rico pra achar que um rico tá fodendo a vida das pessoas? Eu não posso só ver o que tá acontecendo?"

    ba "E você acha que é fácil assim?"

    ba "Responde essa aqui, [mc]. Se você visse um talento como o da minha menina. Você não faria de tudo pra ter ele?"

    ba "Presta atenção. Se você tivesse como assegurar esse talento pra você. Você não garantiria?"

    ba "Você ajuda ela e em troca garante ela pra você pra sempre. Você acha isso errado?"

    "Ele tá falando da relação dele com a [d]... eu tenho que tomar cuidado com o que eu vou responder."

    menu:
        "Eu garantiria o talento dela pra mim.":


            mc charmoso "Eu iria querer esse talento dela pra mim. Seria o melhor negócio."

            ba "Exatamente. É isso que tô falando, [mc]."

            ba "Quando a gente tem poder, a gente pode fazer as escolhas que são melhor pra gente."

            ba "Ficar pensando nos outros é jogar sua vantagem fora. O que você quer é garantir sua posição de dominância."

            mc envergonhado "Acho que eu entendo..."
        "Eu faria algo justo pros dois. Sem ferrar ela.":


            mc normal "Se fosse eu nessa situação, eu tentar ver o que era melhor pros dois. Sem querer ferrar ela também."

            ba "Ela quem?"

            mc "Essa pessoa que você tá falando, n-nessa situação hipotética, claro."

            ba "Você tá falando que mesmo tendo a chance de garantir o melhor negócio, você ainda ia pensar nela?"

            ba "Mesmo que isso trouxesse problemas pra você depois? E se ela estourasse e te deixasse pra trás?"

            ba "Você teria investido em alguém que depois te daria uma rasteira."

            mc charmoso "Se eu mantivesse um negócio bom com ela, ela nunca teria porque me deixar."

            ba "Mas ela teria mais força pra negociar quando tivesse mais poder."

            mc envergonhado "Isso é... mas as coisas são assim."

            ba "Não seriam se você tivesse calculado melhor no começo."

    ba "Assim... Dá pra ver que você tem uma cabeça boa. Só precisa de mais contato com as pessoas certas."

    ba "Só que eu não vou ser seu pai. O [to] bebeu muito vinho se ele achou o contrário?"

    mc desconfiado "Hm?"

    d "Garotos. Posso interromper vocês um pouco?"

    scene d6_imagem15 with Dissolve(1.0)

    pause

    d "Eu vim aqui para cantar, não foi?"

    ba "Claro, minha linda. Eu preciso ouvir uma voz bonita. Por favor, me ajude."

    mc "..."

    d "Você vai me acompanhar no piano?"

    ba "Desculpa, mas hoje não, menina. Sua voz será mais do que suficiente."

    d "Então, deixe-me começar."

    d "..."

    d "{i}O sol nasceu, mas meus olhos continuavam negros.{/i}"

    d "{i}Eu queria ver o que o passado me trouxe...{/i}"

    ba "Não sei o que o [to] viu em você. Mas se ele acha que vale à pena investir... talvez você tenha algum valor."

    mc "O que você quer dizer?"

    ba "Eu posso dar uma colher de chá pra você. Foi um pedido pessoal dele. Mas uma coisa precisa ficar clara."

    ba "Tá vendo essa menina cantando? Ela é minha. Eu paguei por ela. E ninguém vai tirar ela de mim."

    scene d6_imagem16 with Dissolve(1.0)

    pause

    ba "Mesmo que eu tenha que acorrentar ela em uma sala. Ela será minha pra sempre."

    ba "Ela é tudo o que eu tenho de mais precioso... {w}tirando meu cassino é óbvio."

    ba "Eu tenho vontade de rir só de olhar pra ela. Tão preciosa... talentosa... e tão barata..."

    "Como ele pode falar desse jeito da [d]? Ela é uma pessoa, não uma coisa..."

    "Mas será que vale à pena eu só ignorar isso? Parece que eles querem me dar uma chance."

    "O Barão... o [to]... eles são grandes. Será que eles também tão de olho no que eu posso publicar na revista?"

    "Ser aliado desses caras..."

    scene d6_imagem17 with Dissolve(1.0)

    ba "[mc]."

    mc "O-oi!"

    ba "Ela vai parar daqui a pouco. Então eu preciso da sua resposta agora."

    ba "Se você quer ter alguma chance de andar com as pessoas certas. Você vai ter que escolher a opção certa."

    mc "E quais são minhas escolhas?"

    ba "Eu não quero saber você de conversa estranha com a minha menina."

    ba "Eu não ligo se você quer conversar com ela. Mas pare de colocar ideias na cabeça dela."

    ba "Você entendeu? E aí? O que vai ser?"

    "Que pergunta é essa..."

    "Decidir entre me aliar com essas pessoas... mas em troca abandonar a [d] nesse inferno que ela tá passando..."

    "Acho que eu entendo um pouco ela agora... porque ela tá sempre tensa... sempre meio 'sombria'..."

    "Ter esse cara na sua cola. Deve ser uma sensação horrível."

    if diana_namoro:

        "Por isso que foi tão difícil ela aceitar namorar comigo. Eu não fazia ideia, mas ela sabia o problema que ia dar..."

    "Será que eu posso só abandonar ela desse jeito?"

    scene d6_imagem18 with Dissolve(1.0)

    pause

    mc "Eu..."

    menu:
        "Eu não vou deixar você tratar a [d] assim.":


            $ renpy.block_rollback()

            "Talvez eu me arrependa do que eu vou falar agora, mas eu não aguento mais essas pessoas que se acham donas do mundo."

            mc "Não importa o quanto você é rico e cheio de pompa, nada justifica você se achar dono da [d]."

            mc "Ela é uma pessoa e tem o direito de ser livre. De ter a vida dela longe de você. Você não é dono dela, por mais que você ache que é."

            mc "Enquanto eu estiver aqui, eu vou ajudar ela a conquistar o que ela quer."

            if diana_namoro:

                mc "Eu sou namorado dela e pretendo continuar firme do lado dela até o fim."

            ba "Você tá louco?!"

            mc "Eu não. Você tá louco. Você acha que pode conseguir o que quer igual um garoto mimado só porque anda com essa arminha na cintura?"

            mc "Será que isso funciona mesmo? Eu duvido."

            scene d6_imagem19 with vpunch

            pause

            ba "Você tá maluco, moleque?!"

            mc "Eu precisava ser sincero com você. Não aguento mais essa nossa conversa mole."

            ba "Você é corajoso. Ah se é! Eu não imaginava que você teria bolas pra falar desse jeito!"

            ba "Mas agora o showzinho acabou! Tu vai sair daqui deitado com um buraco no meio desse peito magrela!"

            "Merda! Ele vai mesmo matar uma pessoa assim!? E a vida dele?!"

            ba "Eu vou te dar três segundos pra se despedir, lazarento!"

            ba "3...{w} 2...{w} 1..."

            scene black with dissolve

            "MERDA!"

            ba "HAHAHA!"

            d "PARA!!!{nw}"

            scene d6_imagem20 with hpunch

            pause

            d "Para! Por favor!"

            ba "O que você acha que tá fazendo, garota!? Sai daí!"

            d "É culpa minha! Não atire nele, por favor!"

            ba "Idiota! Você vai tomar uma bala por causa desse cretino?!"

            d "Ele não te conhece! Ele não sabia! Dá uma chance pra ele!"

            ba "Você escutou o que esse lazarento falou?!"

            d "Por mim! Por favor! Dá uma chance pra ele! Ele aprendeu a lição!"

            mc "[d]! Cuidado!"

            d "Ele vai se desculpar!"

            ba "Você sabe que eu não faço isso, menina..."

            d "Por mim... eu prometo que fico te devendo..."

            ba "..."

            ba "Caralho! Ok! Mas eu quero ouvir o pedido de desculpas da boca dele!"

            d "Vai, [mc]. P-por favor."

            "Pedir desculpas pra esse idiota? Por ter falado a verdade? E as minhas bolas?"

            "Mas... se eu não falar... ele vai atirar em mim. Ou será que não?"

            "O que eu faço?!"

            menu:
                "Eu não vou me desculpar.":


                    $ renpy.block_rollback()

                    mc "..."

                    d "[mc]! Por favor!"

                    mc "Desculpa, [d]. Mas não dá. Seria a mesma coisa que falar que ele tá certo."

                    d "Nããão! Idiota!"

                    ba "Sai da frente, garota!"

                    scene d6_imagem19 with hpunch

                    ba "Vai com sua verdade pro inferno, garoto do caralho!"

                    play sound "audio/som_17_tiro.mp3"

                    scene black

                    "{i}BANG{/i}"

                    mc "KH!!"

                    d "IDIOTAAA!"

                    $ persistent.mc_morreu2 = True

                    scene red with Dissolve(3.0)

                    pause

                    show pixie b_preocupada with Dissolve(1.0)

                    p "Merda, você matou ele."

                    if persistent.mc_morreu:

                        p "E não foi a primeira vez, né? Eu lembro daquela vez no viaduto. Você é idiota?"

                    p "Eu sabia que eu não devia ter deixado qualquer criatura ficar no comando..."

                    p "Eu vou te dar uma chance. Vê se aproveita..."

                    menu:
                        "Voltar para o último ponto salvo":


                            p "Acho bom."

                            $ renpy.load("None-continue")
                        "Desistir de tudo":


                            p "Você não passa de uma pessoa fraca."

                            $ renpy.full_restart()
                "Por favor... me perdoe...":


                    $ renpy.block_rollback()

                    mc "Por favor, me desculpa! Eu... me descontrolei..."

                    ba "Fala de novo, moleque!"

                    mc "M-me desculpa!"

                    ba "Haha! Assim, sim. Isso é saber seu lugar."

                    d "V-você vai deixar ele em paz?"

                    ba "Dessa vez, sim. A cara dele quase chorando foi prazer suficiente pra uma noite."

                    ba "Agora eu vou pro cassino. Ver se alguém quer me fazer companhia!"

                    ba "Minha linda... não demore muito. Tem gente aqui fora te esperando pra te levar."

                    ba "Mais tarde, depois que eu curtir um pouco, eu passo no seu quarto pra ver como você tá."

                    d "T-tá. Pode ir."

                    scene black with dissolve

                    ba "Até mais, [mc]! Se cuida!"

                    ba "HAHAHA!"

                    scene d6_imagem21 with Dissolve(2.0)

                    pause

                    d "..."

                    mc "[d]... desculpa..."

                    d "Isso foi horrível... e-eu pensei que ele fosse te matar..."

                    mc "Ele seria louco de matar uma pessoa aqui? Arriscar a vida dele por minha causa?"

                    d "V-você não entende, [mc]? Ele é louco! Ele acha que pode fazer o que quiser."

                    mc "Desculpa causar isso com você... mas... eu não podia deixar ele continuar falando aquelas coisas horríveis..."

                    d "Você só precisava aguentar..."

                    mc "Eu não consegui. Desculpa... eu queria fazer alguma coisa, mas no fim foi você quem me salvou."

                    if diana_namoro:

                        d "[mc]... é isso que a gente vai passar se você quiser continuar namorando comigo. Você entende?"

                        mc "Sim... agora eu entendo o que você queria dizer."

                        d "É melhor encerrarmos isso aqui. Vai ser melhor para nós dois."

                        mc "Aqui? Assim?"

                        d "É."

                        mc "De jeito nenhum."

                        d "M-mas!"

                        mc "Eu quero ficar do seu lado, [d]."

                    elif diana_quente:

                        d "Por isso que... mesmo a gente tendo ficando antes, a gente nunca vai poder ter algo sério."

                        d "Ele nunca deixaria..."

                        "Eu e a [d] já ficamos... e eu sei o quão incrível ela é. Mas sempre terá esse perigo."

                        "Essa é minha {b}última chance de ter algo sério com ela{/b}. Se eu negar ela aqui, não vou ter coragem de falar de novo."

                        "O que eu quero fazer?"

                        menu:
                            "Mesmo assim... eu quero você.":


                                mc "Não importa o Barão. Eu quero você, [d]. E eu quero algo sério."

                                d "Você tá falando sério?"

                                mc "Como eu nunca falei antes."

                                d "[mc]..."

                                if diana_seducao >= 35:

                                    $ diana_namoro = True

                                    d "É o que você quer? De verdade? Mesmo com todos os riscos?"

                                    mc "Sim. É o que eu quero."

                                    mc "Eu quero ficar do seu lado, [d]."
                                else:


                                    d "Não vale à pena. Não vale à pena a gente arriscar tudo por isso. Me perdoe."

                                    "Droga... será que eu não conquistei ela o suficiente? Que ela não quer arriscar?"

                                    mc "Se é sua decisão. Eu entendo..."

                                    d "É a decisão mais adulta, independente do que a gente deseja."

                                    mc "Pode ser... mas isso não muda o que eu sinto."

                                    jump diana_e6_amizade
                            "É melhor sermos amigos.":


                                mc "Sim. Essa não é a hora certa. O melhor é sermos amigos."

                                d "É a decisão mais adulta, independente do que a gente deseja."

                                mc "Mas isso não muda o que eu sinto."

                                jump diana_e6_amizade
                    else:


                        label diana_e6_amizade:

                            pass

                        $ diana_e6 = "amizade"

                        mc "Você é uma pessoa que eu realmente me importo. Eu nunca vou deixar você sozinha."

                        d "Você... arriscaria sua vida de novo por mim? É isso?"

                        mc "Bom... arriscar a vida... talvez seja um pouco demais. Acho que eu aprendi minha lição."

                        d "Garoto esperto..."

                        mc "Mas isso não quer dizer que eu vou deixar você na mão dele."

                        mc "Eu vou salvar você, [d]. De um jeito ou de outro."

                        jump diana_e6_pauta



            $ diana_e6 = "seducao"

            d "Vem aqui... deita comigo..."

            mc "Claro."

            scene d6_imagem22 with Dissolve(1.0)

            pause

            d "Você realmente acredita que a gente vai ficar bem?"

            mc "Eu acredito que depende da gente. A gente precisa tomar cuidado e jogar as próximas cartas da melhor forma."

            d "Um passo em falso e a gente pode morrer... os dois..."

            mc "Eu sei. Mas eu prefiro ficar com você e arriscar do que toda noite pensar que você tá presa naquele lugar sozinha."

            d "Você me salvar então?"

            mc "Eu vou. Eu prometo."

            d "Então me beija, [mc]."

            mc "Com todo o prazer."

            scene d6_imagem23 with Dissolve(1.0)

            pause

            d "Sua boca é tudo o que eu preciso pra superar essa noite."

            mc "..."

            "Eu não me importo de arriscar tudo... se eu puder ficar com a [d]."

            "Ela é uma mulher que vale o esforço e o perigo."

            window hide

            pause

            mc "Posso tirar seus óculos?"

            d "Hm? P-por quê?"

            mc "Hoje eu quero fazer algo a mais do que beijar."

            scene d6_imagem24 with Dissolve(1.0)

            pause

            d "A-ah!"

            mc "A gente precisa de algo bom pra aguentar o que vai vir..."

            d "M-mas nosso tempo... ah! Onde você tá indo?"

            mc "Eu vou fazer você esquecer o Barão."

            d "Ah... ah..."

            window hide

            pause

            scene d6_imagem25 with Dissolve(1.0)

            pause

            mc "É bom?"

            d "É muito bom! Continua!"

            d "Ah! Aaah!"

            mc "Você tá tremendo..."

            d "Cala a boca e continua!"

            d "Ah! Aai!"

            d "Aaahh!"

            window hide

            pause



            label diana6_premium1:

                pass

            menu:
                "Oferecer sexo anal":


                    if not premium:

                        call mensagem_premium

                        jump diana6_premium1

                    mc "Diana..."

                    d "Ai... que é?"

                    mc "Tá gostando, né?"

                    d "Muito... gostei... quer dizer... gozei... ah..."

                    d "Mas eu não vou parar aqui... desde aquela noite no seu quarto eu não parei de pensar no sexo com você."

                    d "Tá afim?"

                    mc "Com certeza. Mas deixa eu falar um lance antes."

                    mc "Você sabe que eu sou apaixonado pela sua bunda desde o começo, né?"

                    d "Eu provoquei você lá na praia... e no cassino... e no meu apartamento... é culpa minha também."

                    mc "Que bom que você falou isso porque... eu tava pensando em tentar algo novo com você hoje."

                    d "Envolvendo minha bunda?"

                    mc "É. Esse bundão delicioso. O que você acha?"

                    d "Eu achei que você ia esperar uns meses antes de começar a pedir coisas assim..."

                    menu:
                        "Tem razão.":


                            mc "Você tá certa. A gente vai ter tempo."

                            d "Deixa eu sentir você mais um pouco então."

                            mc "Tá."

                            scene black with Dissolve(1.0)

                            "..."
                        "E se for gostoso?":


                            mc "Mas e se for gostoso pra nós dois? Se não for, a gente não precisa fazer. Você tem a palavra final."

                            d "Hmm..."

                            d "Não imaginei que chegaria nisso nessa velocidade, mas não posso negar que tá me deixando excitada."

                            mc "E eu nem comecei ainda... vem aqui."

                            scene black with dissolve

                            d "Olha bem..."

                            scene d6_premium1 with Dissolve(1.0)

                            pause

                            d "Minha nossa... ah... você vai começar aí mesmo?"

                            mc "É tudo pra você se sentir bem, linda."

                            d "Hmm... é estranho..."

                            mc "Você tá sensível já... só curte..."

                            d "[mc]... cuidado..."

                            d "Hmmm..."

                            d "Isso é quente, não posso negar..."

                            mc "Uhumm..."

                            d "Ahmm..."

                            mc "Eu vou chupar tudo. Na frente e atrás."

                            d "Aahnn... calmammm!"

                            scene d6_premium2 with Dissolve(1.0)

                            pause

                            d "Ai... quando você passa em tudo assim...!"

                            mc "É bom, né?"

                            d "É! Aahn! Lambe tudo! Assim!"

                            mc "Uhum!"

                            d "É melhor do que eu pensei! NNNGH!"

                            d "Continua... tô me sentindo bem..."

                            mc "E só vai melhorar."

                            d "Assim! Passa em tudo! HNNG!"

                            d "Atrás é bom também... pode lamber... nngh.... tô gostando..."

                            mc "Agora você tá pronta."

                            d "O que acontece agora?"

                            mc "Agora eu vou estimular mais você. Deita aqui."

                            d "Ai, [mc]..."

                            scene black with dissolve

                            scene d6_premium3 with Dissolve(1.0)

                            pause

                            mc "Só mexer um pouquinho aqui."

                            d "Aii... mmm..."

                            mc "É uma área gostosa. Só na portinha assim..."

                            d "Ah... assim..."

                            mc "Isso. Me fala o que você tá sentindo."

                            d "É diferente... mas não é ruim."

                            mc "Só relaxa... vai ficar melhor agora."

                            scene d6_premium4 with Dissolve(1.0)

                            pause

                            d "Nnnnghh!"

                            d "O que você tá fazendo aí?! NNGH!"

                            mc "Só na portinha... e chupada."

                            d "Ahnn... isso é intenso..."

                            mc "A é?"

                            d "Na frente e atrás... Nnnghhh! Isso é muito tarado!"

                            mc "Uhum!"

                            d "Sentir gostoso nos dois!"

                            d "Acho que eu vou gozar de novo... ah..."

                            mc "Pode gozar."

                            d "Ai... nnghh... e vai ser grande... [mc]..."

                            mc "É bom, né?!"

                            d "É bom! Hmm! Tá vindo! NNGHH!"

                            d "Não para! Tá vindo! VAAII!"

                            d "AAAGHGH!"

                            scene d6_premium5 with vpunch

                            pause

                            d "MINHA NOSSAA!!!"

                            d "NNNNGHHHH!"

                            "Uau... ela tá tremendo..."

                            d "Tá vindo ainda... aah...."

                            d "Isso... ai... que delícia..."

                            mc "Gostou?"

                            d "Não sabia... nnghh... que podia ser tão bom..."

                            mc "Tá afim do prato principal agora?"

                            d "Você quer me matar de prazer?"

                            mc "Eu também quero sentir... esse buraquinho."

                            d "Deixa eu descansar... fica pra próxima... eu tô tremendo..."

                            "Acho que ela merece um descanso... mas quando a gente vai ter outra chance dessas?"

                            "Será que eu paro aqui?"

                            menu:
                                "Você merece um descanso.":


                                    mc "Tudo bem. Você merece um descanso. Foi bom por uma noite, né?"

                                    d "Gozei duas vezes... desculpa não te agradar, mas a culpa foi sua. Você fez gostoso demais."

                                    mc "Haha..."
                                "Você aguenta mais um pouco.":


                                    mc "Eu sei que você aguenta mais um pouco. Vai ser a melhor parte."

                                    d "Minha nossa... eu vou acordar toda dolorida amanhã... certeza..."

                                    mc "Vem."

                                    scene black with dissolve

                                    scene d6_premium6 with Dissolve(1.0)

                                    pause

                                    mc "Se ajeita."

                                    d "Você fica quietinho. Deixa eu fazer no meu tempo, ouviu?"

                                    mc "Claro... só deixa eu sentir seu buraquinho, Diana..."

                                    d "Você quer isso faze tempo pelo jeito."

                                    mc "Desde que você começou a me provocar com essa raba."

                                    d "Que vulgar... eu esperava mais requinte do meu parceiro."

                                    mc "Eu nem sei mais o que eu tô pensando!"

                                    d "Vou te dar essa colher de chá... você tá excitado demais."

                                    mc "Pra cacete."

                                    d "Então tá... deixa eu sentar..."

                                    mc "Isso..."

                                    scene d6_premium7 with Dissolve(1.0)

                                    pause

                                    d "Hmmm..."

                                    mc "Tô sentindo.... tá entrando..."

                                    d "Eu sei... nnnghh..."

                                    mc "Dói?"

                                    d "Dói... mas eu tô molhada... vai devagar..."

                                    mc "Eu só vou esperar você."

                                    d "Nngh... vou mexer..."

                                    mc "Tá escorregando."

                                    d "Você me deixou toda melada... olha como vai... mmnnh..."

                                    mc "A sensação é incrível, Diana..."

                                    d "É mesmo? Tão bom assim?"

                                    mc "Você nem imagina! Mmnnh! Seu cuzinho é uma delícia!"

                                    d "Cala a boca... aah... não fala assim..."

                                    mc "Eu amo seu cuzinho."

                                    d "Mandei.. mnnh... parar... se você fala assim, eu tô ficando exctada DE NOVO!"

                                    mc "Quer gozar pela bunda agora, é?"

                                    d "Ai... mmnnh..."

                                    d "Não tá doendo mais. Deixa eu me ajeitar."

                                    mc "Opa."

                                    d "Mela mais seu pau. Deixa ele bem molhado."

                                    mc "Tá. Vem aqui."

                                    scene black with dissolve

                                    scene d6_premium8 with Dissolve(1.0)

                                    pause

                                    d "Ainn! Minha nossa!"

                                    mc "Diana... aah... eu vou enfiar tudo!"

                                    d "AI! Que caralho grosso!"

                                    mc "Aah..."

                                    d "Minha bunda tá muito sensível. Tá comendo ela inteira!"

                                    mc "Então vai. Pula em mim!"

                                    d "Eu vou! NNGH!"

                                    mc "Ah! Aghh!"

                                    mc "Que delícia, Diana! Você tá me apertando muito!"

                                    d "Ai! Aiin!"

                                    mc "Ahhh!"

                                    scene d6_premium9 with Dissolve(1.0)

                                    pause

                                    d "Ai, que delícia... aaannngh... aah..."

                                    mc "Aaah!"

                                    d "Tá arrombando minha bunda! NNGHHH!"

                                    d "Eu tô sentindo nos dois! ANGH!"

                                    scene d6_premium9 with vpunch

                                    d "Assim! AAIN!"

                                    mc "Que delícia!!!"

                                    mc "Eu vou gozar, Diana!"

                                    d "Não!!! Ainda não!"

                                    mc "E-eu não aguento! Você é delícia demais!"

                                    d "Não! Eu quero gozar de novo... tá vindo, [mc]... eu preciso sentir na buceta e na bunda."

                                    mc "Não fala assim que é pior!"

                                    d "Aguenta mais..."

                                    menu:
                                        "Tá bom. Vamos trocar de posição.":


                                            mc "T-tá... eu preciso de um segundo então."

                                            d "Hmmm... mas..."

                                            mc "N-nada de 'mas'! Se você continuar se esfregando nele assim, é impossível!"

                                            d "Ok..."

                                            scene black with dissolve

                                            d "Vai logo... eu preciso sentar em você..."

                                            pause 0.5

                                            scene d6_premium10 with Dissolve(1.0)

                                            pause

                                            mc "Quem que não tá aguentando agora, hm?"

                                            d "Cala a boca e mete... você quer ou não meu cuzinho? Aahnn..."

                                            mc "Parece que alguém tá excitada demais."

                                            d "Vain... vaiin..."

                                            mc "Onde você quer?"

                                            d "Na bunda. Enfia na bunda."

                                            mc "Quem que negaria um pedido desses?!"

                                            d "VAII!"

                                            mc "ENTÃO TOMA!"

                                            scene d6_premium11 with vpunch

                                            pause

                                            d "AAIINN!"

                                            mc "Tá inteiro em você!"

                                            d "SSHKIMMM! AANNGH!!"

                                            d "FODE!"

                                            mc "Diana! Eu não consigo muito!"

                                            d "Continua!!! Eu vou gozar DE NOVOO!!"

                                            mc "Eu tambémm!!"

                                            d "AAHH! Assim é bom demais! Na frente e atrás!! É muita coisaaa!!"

                                            mc "Então vai! Rebola no meu caralho!!!"

                                            d "Tá vindo! Não para! Por favor não PARAAA!!!"

                                            d "Mais!!! MAISS!"

                                            scene d6_premium12 with vpunch

                                            d "AAAAAAHHHHHNNN!!"

                                            mc "TÕ GOZANDOOOO!!!!"

                                            d "AAAIKJNN!!"

                                            d "Tô gozando pela bunda!!! Pela buceta e pela bundaaaa!!! AAAGGHH!!!"

                                            mc "Caraalhooo!!!"

                                            scene d6_premium12 with vpunch

                                            d "Ainda tá saindo! Aah... ah..."

                                            d "Minha nossa... que delícia..."

                                            mc "Essa foi a melhor transa que eu tive... eu acho..."

                                            d "Eu também... foi a gozada mais intensa..."

                                            d "você tava certo... eu... adorei a brincadeira na bunda..."

                                            scene black with Dissolve(2.0)
                                        "EU VOU GOZAARR!!":


                                            mc "Não aguento! Vou gozaAaArRRR!!!!"

                                            scene d6_premium8 with vpunch

                                            mc "AAAHH!!"

                                            scene d6_premium8 with vpunch

                                            d "Ah..."

                                            mc "Desculpa... não aguentei..."

                                            d "Ah... ok..."

                                            d "Ufa..."

                                            scene black with Dissolve(2.0)

                                            mc "Essa foi a melhor transa que eu tive... eu acho..."

                                            d "Que bom..."
                "Vamos parar aqui":


                    "Tá bom por hoje..."

            scene black with dissolve

            mc "Gostou?"

            d "Amei... você deve conhecer muito bem o corpo de uma mulher..."

            scene d6_imagem26 with Dissolve(1.0)

            pause

            d "Isso foi incrível, [mc]..."

            mc charmoso "Agora você pode ir tranquila pra casa."

            d "Mas eu tenho algo pra você também. Não é tão gostoso, mas acho que pode te ajudar."

            label diana_e6_pauta:

                d "Se você realmente vai ficar do meu lado. Eu tenho uma coisa pra você."

                mc "O quê?"

                d "Uma pauta pra sua revista. Uma informação que pode nos dar alguma vantagem."

                mc "S-sério?"

                d "Preste atenção, [mc]. O Cassino tá envolvido em um esquema de {b}tráfico de pessoas{/b}."

                mc "Como assim?!"

                d "É isso mesmo. Eu tenho o depoimento de uma trabalhadora do cassino que foi negociada como mercadoria."

                d "Ela foi vendida para o Barão. Este é o depoimento dela. Eu não posso te dar o nome, e claro que vai ser preciso investigar."

                d "Mas... eu acho que é o suficiente pra você convencer seu editor que é algo que vale à pena correr atrás. Que tem fundamento."

                $ pautas += 1
                $ diana_p2 = True

                "{b}Você recebeu uma nova pauta{/b}"

                mc "Muito obrigado, [d]. Eu vou falar com o chefe na hora certa e vamos colocar a boca no trombone."

                d "É nossa única chance, [mc]. Mas saiba que você vai tá arriscando muita coisa. Toma cuidado."

                mc "Eu vou tomar."

                d "Agora é melhor eu ir. Tem alguém aí fora me esperando."

                mc "Você vai ficar bem?"

                d "Sim... eu vou..."

                mc "Até mais, [d]."

                d "Até..."

                scene black with dissolve

                "Eu decidi ficar do lado da [d] contra o Barão... eu sinto que isso ainda vai voltar..."

                "O incrível é que eu ganhei uma pauta. Isso vai me mandar mais um tempo aqui na cidade. Incrível!"
        "Eu quero ficar do seu lado.":


            $ renpy.block_rollback()

            $ diana_e6 = "barao"

            mc "Eu aceito. Eu não vou me meter na sua vida com a [d]. Isso só diz respeito a vocês."

            ba "Sábia decisão, [mc]. Talvez o [to] tenha razão sobre você."

            mc "Eu quero ficar do lado de vocês. Das pessoas que podem realmente me trazer algo de bom nessa cidade."

            ba "Disse tudo. Incrível."

            ba "E eu quero te mostrar uma coisa. Isso é algo que ninguém viu. E vai ser como um acordo de homens entre nós."

            ba "Será... um pacto de sangue, vamos dizer assim."

            mc "Pacto... de sangue... Q-quê?!"

            scene d6_imagem17 with Dissolve(1.0)

            ba "Meu amor, pode parar por agora."

            d "?!"

            ba "Beba algo no bar. Eu vou mostrar algo pro [mc] rapidinho e depois vamos embora."

            d "O quê?"

            ba "É algo que apenas nós homens podemos ver. Você vai ter que esperar. Me obedeça. Venha pra cá, venha."

            d "[mc]? Você..."

            mc desconfiado "Ok..."

            scene black with dissolve

            "..."

            ba "Veja."

            scene d6_imagem27 with Dissolve(1.0)

            pause

            mc surpreso "Que lugar é este aqui?!"

            ba "Haha... incrível, não?"

            ba "Quase ninguém imagina... mas é aqui que a banda toca."

            mc desconfiado "Dinheiro... computadores... baralho?"

            ba "É aqui onde as principais decisões são tomadas."

            mc "Decisões? De que tipo?"

            ba "É nesta sala onde é decidido o futuro da nossa cidade."

            mc "..."

            ba "Você pode pensar que a Prefeitura ou a câmara dos vereadores pode mandar alguma coisa... não passam de fantoches, amigo."

            ba "É aqui que tudo o que importa acontece."

            mc "E de quem... de quem é essa sala?"

            ba "É melhor eu não te responder. Não estamos nessa etapa da relação ainda. Mas veja."

            scene d6_imagem28 with Dissolve(1.0)

            pause

            mc "Caralho... é muito dinheiro... e muitas... coisas..."

            ba "Nem eu entendo o que é tudo isso. Mas tem informação pra caramba aqui."

            ba "Aposto que daria pra você encher uma revista inteira só com o que tem nessa sala."

            mc envergonhado "Seria... bem interessante..."

            ba "Haha! Mas é um sonho de uma noite de verão. Nada do que tá aqui pode sair da sala."

            ba "Uma porrada de gente iria pra cadeia, entende?"

            mc "E-entendo..."

            ba "Bom. É isso. Se alguém pegar a gente aqui, você vai morrer com certeza."

            mc preocupado "T-tá..."

            ba "Então, não se esqueça do que você me prometeu. Não quero mais saber de você se metendo na vida da [d]."

            ba "Ela é minha. E vai ficar pra sempre comigo. Até mais."

            mc "Até..."

            scene black with dissolve

            ba "Venha. Preciso fechar a sala."

            ba "Venha, querida. Vamos."

            d "Já?"

            ba "Sim. O [mc] vai ficar bem. Vamos pro cassino, pra nossa casa."

            d "..."

            "..."

            "Desculpa, [d]. Mas ele são poderosos demais. Essa é a melhor decisão."

            "Eu espero..."

    "Mas olha a hora. É melhor eu voltar direto pro apê."



    label diana_e6_final:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v43_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v43_fim","final","local")

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    call checa_final from _call_checa_final_16

    jump call_cidade

label diana_evento5:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d5_save", extra_info="d5_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ diana_e5 = "evento"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "{i}Trr trrr{/i}"

    mc surpreso "Opa!"

    "A [d] me ligando..."

    menu:
        "Boa noite, linda. Tudo bem?":


            $ diana_seducao += 1

            mc charmoso "Boa noite, linda. Que bom que você ligou."

            d "Linda? As coisas já estão nesse nível?"

            mc "Se depender de mim, sim. O que você acha?"

            d "Vamos ver hoje à noite."

            mc desconfiado "Hoje?"
        "E aí, [d]? Tudo bem?":


            mc normal "Boa noite, [d]. Tudo legal?"

            d "Tudo sim. Queria te chamar pra fazer algo comigo hoje. Topa?"

            mc normal "Fazer o que?"

    d "O que você acha de sair comigo agora? Um encontro eu quero dizer."

    mc charmoso "Com certeza. Eu v-"

    d "Mas precisa ser agora. Você tem 15 minutos pra chegar no centro."

    mc desconfiado "Como assim? Eu preciso tomar um banho, me t-"

    d "É agora ou nunca, [mc]. Topa ou não?"

    menu:
        "Assim? Eu não sei...":


            $ diana_seducao += 1

            mc desculpa "Eu não sei, [d]. Não queria sair com você de qualquer jeito. Você é tão requintada..."

            d "Eu vou entender, [mc]. Eu sei que não é normal, mas é só hoje. O que você diz?"

            mc normal "Se é o jeito, tô saindo agora."
        "Eu não vou perder a chance de te ver.":


            $ diana_seducao += 2

            mc charmoso "Olha, não é do jeito que eu esperava, mas não vou perder uma chance de ver você."

            d "Era isso que eu queria ouvir de você."

            mc "Todas as vezes que a gente saiu eu achei incrível, então pode apostar."
        "Por que assim na correria?":


            mc preocupado "Mas assim? Nessa correria?"

            d "Se você preferir não sair, eu vou entender."

            mc desculpa "Não, não é isso. Eu vou, tá bom?"

    d "Perfeito! Você sabe o bairro dos ricos?"

    mc zerado "Bairro dos ricos... no continente, né? Sei..."

    if v18_fim:

        "É onde o bosta do [caio] mora."

    mc "É naqueles prédios altos de vidro. Onde geralmente tem bastante polícia."

    d "Isso. Chegando nos prédios, você verá na rua principal um bar chamado Atlantis, com uma fachada diferente."

    d "Ele é todo de vidro azul e a frente dele tem um led com uns peixes. Não tem como se perder."

    d "Vou estar esperando você lá."

    mc charmoso "Tá bom. Tô saindo já porque chegar aí em 15 minutos vai ser incrível."

    d "Se esforça que vai valer à pena. Até daqui a pouquinho."

    "{i}Tchk{/i}"

    "Melhor eu ir de Uber, que de busão não tem nem como."

    scene black with Dissolve(1.0)

    "..."

    mc normal "Ela disse bar Aquarium."

    "Motorista" "Não sei onde é, mas os barzinhos ficam aqui."

    mc "Beleza. Pode parar aí."

    "Motorista" "Boa noite."

    mc "Valeu."

    scene cidade centro10 with Dissolve(2.0)

    pause

    if v18_fim:

        "Só de ver estes prédios, já me dá um treco ruim."

    "A rua principal é aqui. Tem vários barzinhos e talz."

    "A sorte é que ela é bem mais movimentada e iluminada que o resto do bairro. Então só pode ser aqui."

    "Atlantis... Atlantis... acho que é este aqui. Opa... olha os peixes que a [d] falou."

    "Vou entrar."

    scene bar_atlantis geral with Dissolve(1.0)

    pause

    "Caraca. Que lugar massa."

    mc zerado "E eu com essa roupa aqui."

    d "[mc]. Aqui."

    scene d5_diana_ola with Dissolve(1.0)

    pause

    mc surpreso "..."

    d "Você chegou rápido."

    mc charmoso "Fiz o possível."

    menu:
        "Vale à pena se matar por uma mulher destas.":


            mc charmoso "Vale à pena se matar por uma mulher como você. Com certeza."

            d "Não exagere, [mc]. Não é como se eu tivesse pedido o mundo para você também."

            mc envergonhado "Verdade. Mas quero ganhar meus pontos contigo."

            d "Isto não é um jogo, homem. Não é como você fosse me conquistar se tivesse pontos de sedução suficientes."

            mc "Verdade..."
        "Não foi nada. Só queria uma roupa melhor.":


            $ diana_seducao += 1

            mc concentrando "Não foi nada. Só queria um pouquinho mais de tempo pra tomar um banho e me vestir."

            d "Sei que foi meio em cima da hora. Desculpa."

            mc charmoso "Isso é o de menos. Não precisa se desculpar."

            d "Vamos fazer a noite valer à pena, o que me diz?"

            mc "Com certeza."

    d "Eu reservei uma mesa pra gente. Um lugar separado do bar."

    mc normal "Só a cara da riqueza, hein?"

    d "Quando eu chamo alguém para me encontrar, pode apostar que eu preparo o melhor. Venha, senta aqui."

    mc charmoso "Claro."

    scene d5_diana_mc_sentados with Dissolve(1.0)

    pause

    d "Pode ficar à vontade. O dono do bar é um fã meu. Ele prometeu que não vai deixar ninguém vir para este lado do bar enquanto estivermos aqui."

    mc "Uou. Às vezes até esqueço que você é conhecida assim na capital."

    d "Só por quem tem algum dinheiro. Não sou igual a [cc] que é conhecida por todos."

    mc "Haha... mas com a [c] é só a jovenzada."

    d "Não sei, não. Claro que a maioria são adolescentes, mas deve ter muito marmanjo que compra revista dela também."

    mc "S-será?"

    d "A [c] é linda, além do corpo dela ser perfeito, ela é super nova e tá sempre de roupa que mostra bem tudo isso. Isso não é por coincidência."

    d "Aliás, eu estava vendo o trailer do filme dela e aquela roupa? Você viu? Você acha que aquilo é só pra adolescente?"

    mc "Haha... acho que você tem razão."

    d "Falando em [c]... eu sei que você conhece ela."

    if priscila_namoro:

        "Um pouco mais do que conhecer, mas ela não precisa saber disso."

    if diana_e3 != "horrivel":

        mc "Verdade. A gente conversou sobre isso lá no seu quarto aquela noite."

        if diana3_segredo:

            $ diana_seducao += 1

            d "Sim... lembra que você falou que foi fuçando no celular dela que conseguiu esse emprego?"

            mc "Sshhh! Você não vai esquecer nunca isso pelo jeito..."

            d "Quem sabe."

            d "Mas não é sobre isso que eu quero falar."

    mc "O que você quer saber?"

    d "Eu- opa! Acho que derrubei meu brinco. Nossa, que indelicada."

    mc "Que isso. Acontece."

    d "Será que você pode pegar pra mim por favor? Deve estar embaixo da mesa."

    mc "Tá. Opa..."

    scene d5_sob_mesa with Dissolve(1.0)

    pause

    mc surpreso "O-opa..."

    d "Que foi? Tá vendo?"

    mc "E-eu... É... vou olhar melhor..."

    "S-sério isso?! Será que ela tá fazendo de propósito? Eu consigo ver a... a..."

    d "Ops. Achei."

    menu:
        "Voltar para o banco":


            mc "Ufa. Deixa eu sentar."

            scene d5_diana_mc_sentados with Dissolve(1.0)

            mc "Então achou?"
        "Continuar sob a mesa":


            $ diana_seducao += 1

            mc "V-verdade?!"

    d "Sim. Estava aqui do meu lado."

    mc "Ufa. Que bom."

    d "Obrigada pela ajuda."

    scene d5_diana_mc_sentados with Dissolve(0.5)

    mc "Hehe... o que você tava falando mesmo?"

    d "Eu... ia te fazer uma pergunta."

    mc "S-sim. Claro."

    d "Quero que você seja sincero comigo. Qual das duas é mais bonita? Eu ou a [c]?"

    "Oxi... que pergunta... assim na lata?"

    menu:
        "Que pergunta é essa?":


            $ diana_seducao += 1

            mc "Que pergunta é essa?"

            scene d5_diana_seria with Dissolve(1.0)

            pause

            d "Eu sabia que você não ia responder."

            mc "Ei. O que foi?"

            d "Não é nada, [mc]. Você não precisa saber de tudo só pra responder uma pergunta."

            mc "..."

            d "..."

            mc "Não é sua cara fazer esse tipo de pergunta. Por isso que eu falei."

            d "Será que você me conhece tão bem assim pra falar isso?"

            mc "Acho que sim. Eu sei que você é uma mulher bem confiante. Não combina com esse tipo de pergunta."

            d "As pessoas não são isso ou aquilo. Não é como se a gente sempre se sentisse da mesma forma."

            mc "Verdade..."
        "A [c].":


            mc "Vou ser sincero. Pros meu padrão pessoal de beleza, a [c]."

            scene d5_diana_seria with Dissolve(1.0)

            pause

            d "..."

            mc "O que não quer dizer que você não seja fantástica. Você sabe que você é linda, [d]."

            d "Não precisa tentar remediar, [mc]. Eu pedi sua sinceridade."

            mc "Não tô remediando. Só quero que você saiba que uma coisa não anula a outra."

            mc "A beleza de uma pessoa não anula a outra. É isso que quero dizer."

            d "Eu entendi... não é isso... Bom, deixa pra lá."

            mc "[d]... essa pergunta..."
        "Você.":


            $ diana_seducao += 2

            mc "Você vai falar que eu não tô sendo sincero, mas eu realmente acho você mais bonita."

            scene d5_diana_sexy2 with Dissolve(1.0)

            pause

            d "Eu pedi sinceridade, lembra?"

            mc "Sim. Tô sendo sincero. Eu acho você muito mais bonita, sensual, elegante."

            mc "Não é que a [c] não seja linda também, mas pra mim você ganhou o duelo da minha preferência pessoal."

            d "Eu acredito... fico feliz de saber isso. Obrigada, [mc]."

            mc "Não precisa agradecer. Só que essa pergunta não tem sua cara."

    mc "É... aconteceu alguma coisa?"

    d "Ah..."

    scene d5_diana_seria with Dissolve(1.0)

    d "Nada que seja do seu interesse. E nem tem nada a ver com nossa noite."

    mc charmoso "[d]... se tem alguma coisa incomodando você eu quero saber. Isso tem tudo a ver com a nossa noite."

    mc desculpa "Aliás, é por causa disso que você me chamou desse jeito hoje, né?"

    d "Como assim? Não posso só querer passar um tempo com você?"

    mc "Quero dizer... Você ter me chamado assim sem nem dar um tempo pra eu me trocar."

    d "..."

    d "Eu sabia que ia ficar na cara se eu te chamasse desse jeito. Me desculpa."

    mc charmoso "Não precisa se desculpar. Eu só quero saber o que tá pegando."

    scene d5_diana_sexy with Dissolve(1.0)

    d "[mc]... você leva jeito mesmo pra ser jornalista. É bem curioso e intrometido."

    mc envergonhado "Que bom que você me conhece..."

    d "E cara de pau também pelo jeito..."

    d "Eu já falei isso, mas essa sua mania de se meter em tudo ainda vai voltar pra te pegar. Cedo ou tarde."

    mc charmoso "Acho que eu aguento."

    d "Mas se tem alguém que eu teria coragem de contar é pra você."

    d "Eu tô cansada de guardar tudo pra mim, sabe? Mas eu não sei se é bom pra você saber o que eu sei. Pode ser perigoso."

    mc preocupado "Perigoso?"

    d "Com certeza. Fazer parte de um círculo restrito te dá acesso a informações que deixam certos poderosos vulneráveis."

    scene d5_diana_seria with Dissolve(1.0)

    d "Só que isso coloca um alvo nas suas costas. Informação é tudo nesse mundo. Ela pode mudar a vida de um ricaço do dia pra noite."

    mc "Entendi..."

    "Já me falaram sobre o poder da minha revista antes. Será que é sobre isso que eles tão falando? O poder de saber das coisas e tornar público?"

    "A [d] com certeza sabe das coisas... será que eu quero entrar nesse buraco?"

    menu:
        "Eu quero ouvir o que você tem a falar.":


            mc charmoso "Eu quero ouvir sua história com certeza."

            d "Mas você entende os riscos, né? Eu tô falando de gente grande, [mc]."

            mc desculpa "Não sei se eu entendo perfeitamente, mas eu pensei no pior e tô pronto mesmo assim."

            d "Só você mesmo..."
        "Acho melhor não me intrometer nessa história.":


            $ diana_e5 = "horrivel"

            mc desculpa "[d]... acho que você tem razão. Eu... tem tanta coisa acontecendo na minha vida. Eu não sei se eu quero mais problema."

            mc "Eu queria muito te ajudar, de verdade. Mas eu acho melhor não desse jeito."

            scene d5_diana_seria2 with Dissolve(1.0)

            d "Eu sei... o pior é que eu sei. Desculpa fazer você passar por isso."

            mc preocupado "Eu que peço desculpas. Eu queria que você pudesse confiar e se apoiar em mim. Porque você já me ajudou também."

            d "Vamos esquecer isso, [mc]. Eu vou continuar sendo quem eu sempre fui. Minha vida não é tão ruim quanto eu posso fazer parecer."

            d "Além disso, como você falou, você tem seus problemas também. E eu não quero ser mais um fardo."

            mc desculpa "..."

            mc "E agora?"

            d "Acho que acabou o clima."

            mc "Pois é..."

            d "Vamos encerrar por aqui. A gente vai ter outras chances de se ver eu acredito."

            mc preocupado "Com certeza. Você me liga?"

            d "Farei o possível."

            scene d5_diana_mc_mesa with Dissolve(1.0)

            d "[mc]..."

            mc "O-oi."

            d "Até mais."

            mc "Até..."

            scene black with Dissolve(1.0)

            "..."

            scene cidade centro10 with Dissolve(2.0)

            "Eu não queria decepcionar a [d]... e talvez até tivesse uma pauta nessa história toda. Mas eu não quero isso agora."

            "Passar por um risco agora e perder tudo o que eu conquistei aqui. Tô fora."

            "Bora pra casa. Amanhã é um outro dia."

            jump diana_e5_final

    scene d5_diana_seria2 with Dissolve(1.0)

    d "Tudo isso começou por sua causa, [mc]. Quando a gente se encontrou na praia e você aceitou nossa parceria."

    mc charmoso "Era uma parceria e tanto pra mim. E tem sido excelente."

    d "Eu coloquei certas coisas na cabeça por conta disso. Expectativas de como minha vida seguiria a partir de lá."

    d "Só que o tempo só mostrou que ter ou não sua ajuda não mudaria em nada minha vida."

    mc preocupado "Nada?"

    d "Nada... A engrenagem é muito maior que eu e você. Ela esmaga pessoas como nós, [mc]."

    mc "[d]... você é uma peça importante do Cassino. Você não é tão fácil de ser esmagada."

    d "Aí que você se engana. O meu poder é tão grande quanto ao de qualquer outra pessoa pra eles."

    d "[mc]... eu fiz tudo que eu podia. Eu trabalhei na minha música com meu coração, com minha alma e com tudo."

    d "Eu fui uma boa garota, eu obedeci, mesmo odiando o que me pediam. Eu me preparei, eu esperei, fui paciente."

    d "Eu não pisei na bola e nem avancei o sinal. Eu fui... perfeita. O máximo que era possível pra mim."

    d "Mas nada disso funcionou. Nada disso surtiu qualquer efeito."

    d "Eu trouxe você pra esse problema, mesmo sem falar das consequências, e também não resolveu nada."

    d "No fim, eu voltei pra estaca zero. Foi tudo em vão."

    d "Isso não é... desesperador? Sentir que não importa o que você faça, é impossível mudar sua vida?"

    menu:
        "A gente ainda pode fazer isso funcionar, [d].":


            $ diana_seducao += 1

            mc "Mas ainda pode dar certo! Não é como se todas as nossas fichas tivessem acabado!"

            d "Como não?! Você não ouviu o que eu disse?! Eu fui perfeita e não mudou nada!"

            mc "Calma. Eu sei. Só que essa foi só uma tentativa. Isso não é o fim."

            d "[mc], olha. Não existem 'chances'. Existe uma chance. Agora acabou! Você não entendeu?!"
        "Eu não sei se eu entendi o que você quer dizer.":


            mc desculpa "[d]... Eu... não sei se eu entendi tudo o que você quer dizer."

            d "[mc]... o Cassino, o Barão, o grupo do qual ele faz parte. Tudo isso é grande demais pra mim, pra você ou pra qualquer pessoa."

            d "A gente pode se debater, chorar, espernear o quanto quiser, eles nos olham como se fôssemos formigas."

            d "Eu não tenho escapatória, entende?"

            "O grupo do qual o Barão faz parte... esse grupo..."

    mc desculpa "Sim. Eu entendo. Eu só acho de verdade que é possível a gente fazer alguma coisa. Sempre tem um jeito."

    scene d5_diana_sexy with Dissolve(1.0)

    d "Por que você fala isso ainda? Você é uma criança?"

    mc desculpa "Olha... eu sinto daqui seu desespero. E acho que hoje não é o melhor dia pra gente bater o martelo."

    mc charmoso "Tentar decidir coisas com a cabeça quente só vai afundar a gente na merda."

    d "Seu otimismo é comovente e irritante ao mesmo tempo. Parece que você não tá na mesma realidade das outras pessoas."

    mc envergonhado "Isso doeu um pouco... mas olha. Eu era um zé ninguém, prestes a perder o trabalho, sem casa e sem nunca ter falado com uma mulher direito."

    mc "Como que qualquer pessoa ia imaginar que alguns meses depois eu estaria falando com uma mulher incrível como você."

    mc charmoso "Minha vida deu uma virada de 180 em um tempo que dá pra contar nos dedos de algumas mãos. Talvez muitas mãos... mas você entendeu."

    mc "Não dá pra falar que sua vida acabou. A gente é jovem e tem muita coisa pela frente. Nunca se sabe o dia de amanhã."

    mc "Enquanto a gente tiver energia, a gente pode tentar novamente. E a energia vem da gente mesmo e não dos outros. Então, se você topar, eu topo."

    d "Que absurdo... a vida parece tão fácil na sua cabeça. Você fala como se não tivessem correntes te segurando."

    mc envergonhado "Não sei..."

    d "Olha..."

    scene d5_diana_mc_mesa with Dissolve(1.0)

    pause

    d "Acho que é isso que torna você tão especial."

    mc "S-sério?"

    d "Conversar com alguém que não vê limites é cansativo... às vezes é simplesmente enervante."

    d "Mas... se você passa pelo asco inicial e se entrega... é incrivelmente viciante."

    d "Uma pessoa que não cansa, que não abaixa a bola não importa o que aconteça... isso é inspirador, [mc]."

    d "Eu sei que sua vida não é fácil."

    mc "Sabe?"

    d "Com certeza. Essas celebridades tão sempre colocando você em situações sufocantes... O trabalho de entregar quem você ama pro seu chefe..."

    d "Eu nem consigo imaginar como é viver constantemente com medo de ser pego, demitido ou fazer uma escolha errada quando a gente anda sobre vidro."

    d "Como você fez pra chegar até aqui?"

    menu:
        "Não sei... acho que só fui vivendo...":


            mc "Pra ser extremamente sincero com você, acho que eu só fui vivendo mesmo."

            mc "Nunca parei pra pensar se eu tava certo ou errado. Ou se esse caminho era ruim ou bom."

            d "Simples assim?"

            mc "Bom... você perguntou o meu segredo. Não era nada incrível eu acho..."

            d "Talvez seja. Talvez o mais certo seja o mais simples e a gente que tem vergonha de admitir."

            d "Será que a gente realmente sabe pra onde estamos indo?"

            mc "Eu acho que nem sempre."

            d "Talvez nunca..."
        "O sofrimento faz da gente mais forte.":


            $ diana_seducao += 2

            mc "Eu sinto que as dificuldades que eu passo não são por nada. Elas me deixam mais cascudo."

            mc "Viver com tudo dando certo pode ser bom, mas e quando algo der errado? Será que alguém que viveu no bem bom vai saber como lidar?"

            mc "Talvez sofrer só faça parte do que o ser humano tenha que viver na Terra. Quanto mais cedo a gente entender isso, mais fácil superar."

            d "Sem dúvida é um argumento bem corajoso. Mas você precisa estar pronto pra sofrer."

            mc "Sofrer nunca é fácil... e às vezes ninguém tá pronto pra quando algo ruim acontece. Mas se a gente se der um tempo, dá pra virar."

            d "Você tá parecendo um livro de auto ajuda agora."

            mc "Haha... acho que sim. Me empolguei um pouco."

            d "Mas foi bonito mesmo assim."

            mc "Obrigado."
        "Talvez eu queira ver o tesouro no fim do arco irís.":


            $ diana_seducao += 1

            mc "Eu penso que talvez eu esteja esperando pra ver o tesouro que tem no fim do arco irís. Aguentar o agora pra colher depois."

            d "Homem resignado..."

            mc "Exatamente. Aguentar algo terrível aqui e ali agora e depois finalmente poder viver o bom que tem depois."

            d "Mas e se não tiver nada de bom 'no fim'. E se no fim só existir o fim mesmo."

            mc "Daí vai ser meio triste... mas é essa esperança que eu acho que me dá força."

            mc "Pensar que depois de subir essa montanha, tem algo incrível no cume me esperando. Isso me dá energia pra aguentar."

            d "Talvez seja isso que falte pra mim. Um alvo no fim do caminho que me permita sonhar e passar pelo que eu estou passando."

    scene d5_diana_apoiada with Dissolve(1.0)

    pause

    d "[mc]... talvez nem você saiba seu segredo exatamente, mas eu quero mais disso."

    d "Eu preciso disso agora."

    d "Se você tiver razão e realmente o melhor seja só tentar de novo, então provavelmente eu vou continuar sendo um fardo pra você."

    d "Porque sozinha eu tenho certeza que eu nunca vou conseguir."

    mc charmoso "Pode contar comigo, [d]. Eu vou tá aqui pra você."

    d "Não precisa me responder isso hoje. Pensa com calma. Se você ficar do meu lado, você vai virar inimigo de gente muito grande."

    d "O Barão é só um deles. Mas tem mais gente nessa roda. Gente do mundo do dinheiro, que tem influência na polícia, no entretenimento e até na política."

    d "Eles são grandes desse jeito. E a gente é só duas formigas."

    mc "A gente pode até ser só formigas, mas a gente faz uma boa dupla, fala aí."

    d "..."

    d "Como é fofo..."

    mc "Tô falando sério!"

    d "Acho que... com licença."

    scene d5_diana_mc_posando with Dissolve(1.0)

    pause

    mc "T-toda!"

    d "Acho que vou gostar muito de fazer uma dupla com você, [mc]."

    if diana_e4 == "seducao":

        $ diana_quente = True

    if diana_quente:

        mc "E-eu também..."

        d "Falando nisso, eu já experimentei como é fazer uma dupla com você. Eu gostei bastante."

        mc "E-eu também..."

    d "No começo eu pensei que você fosse criança demais pra mim, [mc]."

    mc "S-sério?!"

    d "Mas com o tempo eu aprendi a admirar isso em você. Essa sua capacidade de ser leve perante a vida."

    d "Essas suas caretas e seu jeito de ficar com vergonha de tudo... isso é, talvez, encantador..."

    mc "Mas eu não sou sempre assim... ou sou?"

    d "Você tem um jeito só seu. Talvez não seja o tipo de pessoa que impressiona logo de primeira."

    mc "S-senti uma leve crítica nesse comentário..."

    d "Mas com certeza me impressionou com o tempo. E eu tenho certeza que impressionou muitas outras garotas e garotos."

    mc "Agora você só tá tentando fazer com que eu não me sinta mal."

    d "Para, bobo... me escuta."

    scene d5_diana_mc_posando2 with Dissolve(1.0)

    pause

    "Uou! Hoje a [d] tá bem direta... olha pra essas pernas e pra esse decote..."

    if diana_quente:

        "Tô com uma sensação muito boa de que hoje vai rolar algo muito bom se eu não acabar com o clima."

    d "Existe essa coisa da primeira impressão, sabe?. Às vezes uma mulher sabe se quer ou não ficar com um homem no primeiro minuto."

    d "Segurança, confiança, cheiro, aparência, a voz, tudo isso faz a gente querer ou não transar com alguém."

    d "Não dá pra explicar. É físico, animal. E também é uma porcaria."

    mc "Porcaria? Por que?"

    d "Às vezes, a gente acaba perdendo o cara certo porque a voz do outro é mais sexy ou ele tem um olhar que mexe com você."

    d "O coitado do amigo que não tinha essa energia sexual nunca teve uma chance. Mas sabe? Às vezes ele seria a melhor escolha."

    d "O ser humano é um animal, mas a gente tem razão, a gente tem consciência. E essa atração animal nem sempre é suficiente."

    d "Claro, você transa e pode até ficar satisfeita. Mas e depois? É daí que vem o vazio do dia seguinte."

    mc "E o sertanejo da fulana lá..."

    d "Sim. Se a gente fosse um pouco menos animal nessa hora e olhasse de verdade pra quem realmente pode adicionar algo na nossa vida..."

    d "... talvez a gente chorasse menos e sofresse menos de amor. Menos decepção e menos noites pensando em quem não merece atenção."

    d "Dizem que o ser humano no fundo gosta de sofrer. Mas eu acho que é só desculpa pra gente continuar fazendo coisa errada."

    mc "Eu acho que isso não é só com a mulher. A gente também sempre vai na mina mais sexy e que dá mais bola."

    mc "E claro que transar é bom, mas homem também escuta sertanejo, né? Então já viu..."

    scene d5_diana_mc_posando_close with Dissolve(1.0)

    d "É isso que eu quis dizer. Talvez quando a gente se viu na praia eu não ficaria de jeito nenhum."

    d "Mas com o tempo eu vi que talvez você não fosse a escolha mais óbvia, mas a mais certa."

    if diana_quente:

        $ diana_seducao += 1

        d "Tanto que a gente acabou ficando."

        mc safado "E aposto que não se arrependeu."

        d "Acho que eu criei um monstro. A auto estima subiu demais."

        mc envergonhado "Tô brincando."

        mc charmoso "Claro que não posso falar por você, mas eu gostei muito."

        d "Isso é bom."
    else:


        d "Às vezes eu fico chateada de nada ter rolado entre a gente."

        mc "Eu também ficou pensando nisso..."

        d "Mas quem sabe não é para o melhor? A gente também precisa de amigos."

        mc normal "Com toda a certeza."

    d "Ah! Infelizmente eu vou ter que ir logo."

    mc preocupado "Mas já?!"

    d "É... mas antes eu queria te mostrar uma coisa."

    mc desconfiado "Onde?"

    d "Aqui no bar mesmo. Quero que você veja porque o nome do bar é Atlantis."

    mc normal "Legal."

    scene bar_atlantis geral2 with Dissolve(2.0)

    "O bar já tá bem mais vazio. Pra onde será que a galera foi?"

    d "Olha que interessante aqui."

    mc normal "Opa, tô indo."

    scene d5_diana_mc_olhando with Dissolve(1.0)

    pause

    mc "Uou... que legal. Como eles fazem isso? Não é de verdade, né?"

    d "Não... o dono me explicou que eles usam um telão de led 4k pra simular um aquário."

    mc "Caraca... é muito real. É tão bonito que é mais bonito que o de verdade. Muito interessante mesmo."

    d "É sim... eu achei que você ia gostar mesmo."

    mc "Valeu mesmo por ter me chamado, [d]."

    d "Eu que agradeço. Você não sabe o quanto você me ajudou hoje. Eu me sinto outra pessoa."

    "A [d] é uma mulher tão diferenciada. Ela é sincera, ela não tem medo de falar o que tá sentindo."

    "Mesmo assim ela tem esse ar misterioso. Esse jeito de que tá sempre acima da gente. Só que também fala do que tem medo..."

    "É duro de explicar o que eu sinto quando eu tô com ela."

    if diana_quente:

        "A gente já ficou e não tem como falar que eu não curti. Ela é linda, gostosa, cheirosa."

        "E hoje eu sinto que ela tá me provocando muito. Se eu não fizer nada, vou perder uma chance de ouro."
    else:


        "Até hoje eu e a [d] ficamos só na amizade. Mas hoje ela tá me provocando mais do que o normal."

        "Talvez ela queira algo a mais comigo. Todo aquele papo sobre casais e talz... dá pra ver isso."

    "E agora? Se eu realmente for fazer alguma coisa precisa ser agora, antes que ela puxe o carro."

    "Mas e se eu tiver entendendo tudo errado e ela não quiser nada? Ela tava tão triste antes..."

    "Que frio na barriga! O que eu faço?!"

    d "Então acho que é isso..."

    mc "É. Nossa... deixa eu só ver mais um pouquinho. Ainda tô impressionado hehe..."

    d "Tudo bem..."

    label diana_e5_escolha:

        "Que merda eu tô falando?!"

        "Se eu voltar agora a gente vai ficar na amizade! O que eu faço?!"

    menu:
        "L-legal. Acho que podemos voltar, [d].":


            "A [d] é uma garota incrível e eu quero ela como amiga. Nada mais do que isso."

            "Eu sei que talvez ela quisesse outra coisa, mas tenho que ser sincero com ela."

            label diana_e5_amizade:

                $ diana_e5 = "amizade"

            mc "Tá bom. Você já tem que voltar mesmo?"

            d "Sim. O Barão não sabe que eu tô aqui."

            mc "Qual é o problema nisso?"

            scene d5_diana_mc_olhando2 with Dissolve(1.0)

            d "Você ainda não entendeu isso, [mc]?"

            mc "Desculpa, acho que não."

            d "Você não lembra da minha música ou do nosso encontro na pizzaria? Tudo o que eu falei... é verdade. Literalmente."

            mc "[d]..."

            d "Pense muito bem, [mc]. Se você realmente quiser me ajudar, você vai virar inimigo do Barão e daqueles que estão com ele."

            d "Essas pessoas são perigosas. Não esquece isso."

            d "Eu vou entender se você não quiser. Vou mesmo. Você já é um amigo muito maior do que eu podia esperar."

            d "Agora eu preciso ir. Ela já tá aqui me esperando."

            d "Obrigada mais uma vez por hoje. Foi incrível. E boa noite."

            mc "B-boa noite..."
        "Eu tava pensando naquele negócio de formigas...":


            "Das outras vezes eu só segui a deixa da [d]. Mas hoje ela não tá legal. Se eu não tomar a dianteira, ela vai se decepcionar."

            "Mas agora não é hora de se aproveitar dela. Eu só vou dar em cima se eu tiver certeza que eu {b}quero algo sério com ela{/b}."

            "Eu quero mesmo namorar a [d]?"

            menu:
                "Sim. Eu quero namorar ela sério.":


                    "Eu quero algo mais com a [d]. Eu sei disso."
                "Não. Preciso pensar melhor.":


                    "Calma... essa é uma decisão importante. Pensa pensa pensa!"

                    d "[mc]?"

                    mc "Ah! É..."

                    jump diana_e5_escolha

            "Força, [mc]. O máximo que ela vai fazer é dizer 'não'. Respira..."

            scene d5_diana_mc_olhando2 with Dissolve(1.0)

            mc "Sabe, [d]..."

            d "Oi?"

            mc "Hoje a gente tava falando sobre formigas... "

            d "Não foi das minhas melhores analogias..."

            mc "Foi boa, sim. Deu pra entender bem. Mas o que eu queria dizer é que... eu acho que a gente forma uma bela dupla."

            d "Hm?"

            mc "Assim..."

            if diana_quente:

                mc "Quando a gente se beijou antes, eu senti algo mais do que só um lance físico. Eu não queria parar só nisso."

            mc "Depois de hoje, de ver você quase desesperada com essa situação, sem saber como reagir... eu senti uma angústia tão grande."

            mc "Eu fiquei muito triste de ver você assim. De verdade. E eu... não quero que você se sinta assim nunca mais."

            d "[mc], isso é algo que infelizmente não está no seu controle. Eu agra-"

            scene d5_diana_mc_abracados with Dissolve(1.0)

            pause

            mc "Calma..."

            d "[mc]..."

            mc "É sobre isso que eu quero falar. Eu não quero mais só olhar você passando por isso de longe."

            mc "Tudo isso só me mostrou que eu me importo com você, mais do que eu imaginava."

            d "..."

            mc "Eu... quero ser mais do que um amigo ou um peguete. Eu quero namorar você, [d]."

            d "!"

            mc "Eu falo sério."

            if diana_seducao >= 35:

                $ diana_e5 = "seducao"
                $ diana_namoro = True

                d "[mc]... você realmente pensa isso?"

                mc "Sim. É o que eu quero [d]... se você quiser também."

                d "..."

                d "Hoje eu vim pronta pra ter algo com você. Mas depois da nossa conversa eu entrei em outro clima."

                d "Eu nunca esperei que você chegaria com um pedido desses..."

                mc "..."

                d "Eu..."

                d "Eu não sei o que dizer."

                mc "Não sabe?"

                d "Calma... não me solta por favor."

                scene d5_diana_mc_abracados_frente with Dissolve(1.0)

                pause

                mc "T-tá..."

                d "Acho que eu nunca... nunca... não sei como te falar."

                mc "Pode falar como você quiser."

                d "Eu nunca... tive que decidir alguma coisa assim."

                mc "Nunca?"

                d "Não... essa é a primeira vez que eu tenho que decidir algo assim..."

                mc "Voc-"

                d "Para. Só me dá um tempo..."

                "Como assim nunca teve que decidir? A [d] nunca namorou alguém ou nunca ficou tão em dúvida assim?"

                "Essa demora tá me matando... se ela demorar mais eu vou morrer de vergonha."

                "Se bem que abraçar ela assim não tá ruim, não. A [d] tá cheirosa e eu tô sentindo a bun-"

                d "[mc]..."

                mc "O-oi..."

                d "Você entende no que você vai se meter? Você entende que eu não sou responsável pela minha vida?"

                "Como assim não é responsável?"

                mc "[d]... eu-"

                d "Se você entende isso e está pronto para encarar isso comigo. Então eu aceito. Eu aceito namorar você, [mc]."

                "Isso! Boa! Depois eu penso no que ela quer dizer. O que importa é que ela aceitou!"

                mc "Eu aceito, claro. O que eu disse é sério, [d]. Eu não quero ver você passar mais por isso sozinha."

                d "Então vai."

                mc "Vai?"

                d "Me beija."

                scene d5_diana_mc_beijo with Dissolve(1.0)

                pause

                "Nossa. A [d] tá ofegante. Eu nunca vi ela tão vulnerável assim."

                "Eu acho que essa é a primeira vez que eu beijo a [d] de verdade."

                d "Eu... nunca senti um beijo assim, [mc]."

                mc "Vai se acostumando que ainda vai ter muito."

                scene d5_diana_mc_abracados_encarando with Dissolve(1.0)

                pause

                d "Eu nunca imaginei que essa noite acabaria nisso."

                mc "Muito menos eu que nem tomei banho."

                d "O que é isso perto do que você fez por mim hoje, [mc]?"

                d "Eu tinha desistido de tudo. Estava pronta para continuar sendo aquilo que o Barão quer que eu seja."

                d "Você me salvou. E fico até um pouco triste de saber que você nunca vai realmente entender o peso dessas palavras."

                mc "Eu n-"

                d "Chega de falar e me beija mais."

                scene d5_diana_mc_beijo2 with Dissolve(1.0)

                pause

                "A gente se beijou por minutos... deu pra ver todo mundo no bar olhando."

                window hide

                pause

                scene d5_diana_mc_abracados_encarando with Dissolve(1.0)

                d "Acho que eu não vou enjoar de te beijar tão cedo."

                mc "Ei... quer dizer que alguma hora vai?"

                d "Talvez. Mas agora tenho que ir. Já passou muito da hora. Ela deve estar preocupada."

                mc "El-"

                d "Ah. Se você me encontrar no Cassino, por favor não me trate de forma diferente."

                mc "Por que?"

                d "Ninguém pode saber de nós lá. Ninguém, ouviu?"

                mc "Tudo bem. Mas po-"

                d "Boa noite, [mc]. Fica bem."



                "Que história é essa de 'ela'? E a gente acabou de oficializar. A gente podia fazer mais..."

                "Eu quero ela pra mim esta noite. Mas está certo eu forçar ela assim?"

                label diana5_premium1:

                    pass

                menu:
                    "Puxar ela pra você":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_53

                            jump diana5_premium1

                        mc "Diana!"

                        d "?!"

                        scene d5_premium1 with hpunch

                        pause

                        d "A-ah! [mc]?!"

                        mc "Eu quero ficar com você essa noite."

                        d "Você sabe que eu não posso... hm-hm... é perigoso..."

                        mc "Desculpa se eu tô sendo egoísta, mas eu quero você pra mim agora que a gente tá namorando."

                        d "Mesmo que... isso dê problema?"

                        menu:
                            "Tem razão... melhor parar.":


                                mc "Não. Eu não quero arranjar problemas pra você."

                                d "Obrigada por entender. Eu acredito que teremos outras oportunidades..."

                                mc "Sim. Com certeza. Eu não tenho pressa."

                                d "Boa noite."

                                mc "Boa noite..."

                                "Eu sinto que perdi muita coisa deixando ela ir assim..."
                            "Mesmo que dê problema.":


                                mc "Você não acha que a gente aguenta?"

                                d "Ah..."

                                mc "Se você não falar nada, eu vou continuar te apertando e te beijando."

                                d "Tô vendo... mas eu..."

                                mc "Hm?"

                                scene d5_premium2 with Dissolve(1.0)

                                pause

                                d "Aahh... meu vestido..."

                                mc "Não tem ninguém aqui, lembra?"

                                d "Eu sei, mas... hmm..."

                                mc "Seu corpo é incrível, Diana. Eu adoro olhar pra você, sentir você..."

                                mc "Desde aquele dia eu não esqueci que a gente chegou muito perto... hoje você vai ser minha."

                                d "Mas e o ba... e a nnn.... nnnghhh..."

                                mc "Você quer ficar comigo, não quer?"

                                d "Eu quero."

                                mc "Eu faço você se sentir bem?"

                                d "Muito."

                                mc "Então fica comigo. E depois a gente vê o que a gente faz."

                                d "Ah... eu..."

                                d "[mc]..."

                                d "Tá. Eu aceito sua proposta. Eu vou brincar com você aqui."

                                mc "Você faz de mim o homem mais feliz do mundo."

                                d "Não exagere... e tem uma coisa... a gente não pode transar aqui, mesmo sendo tranquilo."

                                mc "Tudo bem. Vamos ver onde as coisas vão levar."

                                d "Mas eu quero brincar com você... e aposto que você vai adorar..."

                                mc "Já tô adorando..."

                                d "Sente aqui."

                                scene black with dissolve

                                scene d5_premium3 with Dissolve(1.0)

                                pause

                                mc "Ah..."

                                d "Eu sei o quanto você ama minha bunda. Então sente bem ela."

                                mc "Sua bunda é incrível, Diana."

                                d "Eu sei. É gostosa de apertar e de sentir aí na virilha, né?"

                                mc "C-com certeza... ah..."

                                d "Parece que tem alguém aqui gostando aqui atrás."

                                mc "Não consigo controlar. Você é gostosa demais."

                                d "Não controla nada. Deixa eu sentir você aqui atrás também."

                                mc "Sente ele na sua bunda então."

                                d "Vamos dançar juntos... ninguém vai poder falar nada."

                                mc "Tá... dançar..."

                                d "Huhu... delícia..."

                                menu:
                                    "Continuar dançando":


                                        mc "Continua assim, Diana. Tá bom demais."
                                    "Levantar mais o vestido":


                                        mc "Deixa eu ver você melhor."

                                        d "Como assim?"

                                        mc "Aqui ó."

                                        scene d5_premium4 with Dissolve(1.0)

                                        pause

                                        d "Ah..."

                                        mc "Eu gosto assim, mais safado."

                                d "Eu gosto assim também. Tá começando a mexer comigo, [mc]."

                                mc "E se você continuar desse jeito, eu não vou conseguir me segurar, Diana."

                                d "Quem disse que é pra você se segurar?"

                                d "Não esquece que a gente tá em público... mas se você olhar pro meu vestido agora... o que que falta?"

                                mc "Eu quero sentir mais que sua bunda."

                                d "Você quer o resto?"

                                mc "Não para de mexer e vem aqui."

                                scene d5_premium5 with Dissolve(1.0)

                                pause

                                d "Aiii!"

                                d "Como eu vou dançar assim?"

                                mc "Dá seu jeito, mulher."

                                d "Ah... eu preciso me esfregar em você... me solta..."

                                mc "Continua mexendo."

                                d "É pra isso que eu tô aqui!"

                                mc "Ah, Diana. Você é muito sexy. E você tá me fazendo me sentir muito bem."

                                d "Não esquece que isso aqui é só uma dança, tá?"

                                mc "Aha. Continua."

                                d "O que você tá pensando agora?"

                                mc "Nada não."

                                d "Eu tô percebendo uma intenção na sua voz..."

                                "A Diana tá acabando comigo aqui. Eu não consigo pensar em outra coisa que não seja meter nela agora."

                                "Não sei se isso é demais, mas eu podia abaixar a calcinha dela e fazer tudo agora mesmo."

                                "Lá no banheiro eu consegui entrar, mas não consegui comer ela de verdade."

                                "E a gente tá aqui no agarro forte. Ela tá se esfregando no meu pau sem vestido... é só colocar esse paninho pro lado e..."

                                menu:
                                    "Tirar a calcinha dela":


                                        mc "Licença, Diana."

                                        scene black with dissolve

                                        scene d5_premium6 with Dissolve(1.0)

                                        pause

                                        d "Ah... o que é isso, [mc]?"

                                        mc "Tô dançando mais pertinho."

                                        d "Hmm... isso é muito quente."

                                        mc "Com certeza. Mas vai ser divertido."

                                        d "Se você continuar se esfregando assim, pode entrar."

                                        mc "Então continua rebolando em mim, Diana."

                                        d "Tá... aah..."

                                        mc "Hmm..."

                                        d "Eu tô sentindo muito você."

                                        mc "Vem mais."

                                        scene d5_premium7 with Dissolve(1.0)

                                        pause

                                        d "Ahn... vai entrar..."

                                        mc "Vem, esfrega."

                                        "Se continuar assim eu vou comer ela no meio do bar."

                                        "Que loucura."

                                        mc "Quem te viu, quem te vê, Diana. Toda chique, se esfregando no meio do bar assim."

                                        d "Hmm... E você?"

                                        mc "Eu?"

                                        d "Vai só ficar olhando ou vai comer?"

                                        mc "Ah... claro que eu vou!"

                                        d "Então vem, gato. Eu tô pronta."

                                        mc "Toma, Diana!"

                                        scene d5_premium8 with hpunch

                                        pause

                                        d "AAAHNN!"

                                        mc "AGH!"

                                        mc "Eu tô dentro de novo, gata."

                                        d "Hmmm... melhor que da outra vez ainda."

                                        "Não acredito que eu tô comendo a Diana. Uma mulher dessas dando pra mim assim."

                                        d "Ahn..."

                                        mc "Dança. Continua dançando pra mim."

                                        d "Aahnn... ah..."

                                        scene d5_premium9 with vpunch

                                        pause

                                        mc "Assim mesmo! Vai!"

                                        d "Ah! Tá dentro mesmo!"

                                        mc "Finalmente eu vou te comer decente, Diana!"

                                        d "Come direito, gostoso!"

                                        mc "Vem mais perto! Deixa eu te apertar!"

                                        d "Nnnghh!"

                                        mc "Ah!"

                                        scene d5_premium10 with vpunch

                                        pause

                                        d "Minha nossa!"

                                        mc "Diana! Continua assim!"

                                        d "Agnn!"

                                        mc "Você tá tão molhada!"

                                        d "Porque você é uma delícia!"
                                    "Continuar dançando":


                                        mc "Vamo continuar assim mais um pouco, Diana."

                                        d "Claro. Até você cansar."

                                mc "Desse jeito.. eu tô quase lá, Diana!"

                                d "[mc]... eu quero gozar... ah... com você hoje."

                                mc "A-ah?"

                                d "O que você acha... hm... quer transar comigo de verdade?"

                                mc "Claro. É o que eu mais quero."

                                scene black with dissolve

                                mc "Q-quê? Por que parar?"

                                scene d5_premium11 with Dissolve(1.0)

                                pause

                                d "Já que a gente tá desafiando tudo e todos esta noite..."

                                mc "O que passou por essa cabecinha aí?"

                                d "Tava pensando que a gente podia fazer um bis do nosso show."

                                mc "Quer dançar de novo, é?"

                                d "E se a gente fizer isso na sua casa?"

                                mc "S-sério?"

                                d "Aqui é perigoso. A gente podia se divertir bem mais tranquilos lá."

                                "Passar a noite com a Diana no meu apê... não acredito..."



                                if casa:

                                    "Agora que eu tô com o apê novo, dá pra chamar ela."

                                    "Imagina levar uma mulher requintada igual a Diana pro muquifo que eu vivia antes? Até parece."

                                    if xiang_casa:

                                        "O problema é que a Xiang tá lá... como que eu vou explicar isso pra Diana?"

                                    if karli_casa:

                                        "O problema é que a Karli tá lá... como que eu vou explicar isso pra Diana?"

                                    "Será que é uma boa levar ela lá?"

                                    menu:
                                        "Bora pra casa.":


                                            mc "Com certeza. Eu ia adorar ter você lá."

                                            d "Eu tô me sentindo muito viva de tá fazendo um negócio desses, [mc]."

                                            mc "E eu tô muito empolgado de poder passar a noite toda com você."

                                            d "Então vamos."

                                            if xiang_casa or karli_casa:

                                                mc "Só pra te avisar... eu tô... ajudando uma amiga... ela tá ficando em casa um tempo."

                                                d "Amiga? Eu tô namorando um homem comprometido?"

                                                mc "Claro que não! É só amizade mesmo."

                                                d "Hm... isso é estranho, [mc]."

                                                mc "Desculpa... eu não consigo falar não pras pessoas..."

                                                d "Faz sentido... eu sei como você é. Tudo bem... mas isso não me deixa totalmente confortável."

                                                d "Se eu descobrir qualquer coisa... que você me enganou... eu não teria como olhar nos seus olhos de novo."

                                                mc "Não se preocupe. É só amizade mesmo."

                                                d "Tá... Vamos."

                                                mc "Bora!"

                                            scene black with dissolve

                                            pause 1.0

                                            jump diana5_ape
                                        "Vamo no seu apê.":


                                            "Melhor não arriscar. Se ela achar que eu sou um tarado, daí que nunca vai rolar nada mesmo."

                                            mc "Então..."
                                else:


                                    "Impossível. Não naquele muquifo que eu vivo. Ela nunca ia ter coragem de pisar lá."

                                    "Uma mulher igual a Diana? De jeito nenhum. Não tenho coragem nem de convidar ela."

                                mc "Eu tô muito afim de ir até o fim com você, Diana. Muito mesmo."

                                d "Mas?"

                                mc "M-mas não dá pra ser no meu apê."

                                d "Huh? Não pode ser tão ruim assim. Eu não ligo, [mc]. Eu faço isso por você."

                                mc "Sem chances. Eu que não tenho coragem."

                                mc "O que você acha da gente ir pro seu?"

                                d "Isso sim é impossível. Se pegarem a gente entrando juntos... não... mesmo que a gente pense em algo. É arriscado demais."

                                mc "Ok... e agora?"

                                d "A gente vai ter outras oportunidades."

                                d "Eu me diverti bastante esta noite, [mc]. Muito mais do que eu tinha imaginado. Boa noite."

                                mc "B-boa noite."
                    "Melhor não forçar":


                        mc "Ok... boa noite pra você também..."
            else:


                d "[mc]... você realmente pensa isso?"

                mc "Sim. É o que eu quero [d]... se você quiser também."

                d "..."

                d "Eu não quero."

                mc "Não?"

                d "Não. Pelo menos não agora."

                mc "Eu pensei que... você também me via assim."

                d "Eu te disse. Você é uma pessoa única, o cara mais interessante que eu encontrei em muito tempo."

                d "Mas eu não senti que você queria algo comigo. Pelo menos hoje eu não senti isso."

                "Droga... por que a rejeição dói tanto? O que eu podia ter feito de diferente?"

                scene d5_diana_mc_olhando2 with Dissolve(1.0)

                mc "..."

                if diana_quente:

                    d "Eu sei que a gente já ficou antes. Mas as coisas não chegaram nesse ponto pra mim."

                d "Eu ainda não acredito como você acabou me ajudando hoje. Mas isso não é a mesma coisa de gostar de alguém nesse ponto."

                d "Isso não muda admiração que eu sinto por você. E não digo que é impossível no futuro. Mas não hoje."

                mc "Tudo bem..."

                d "Não fi-"

                mc "Você pode escapar de mim hoje. Mas a gente ainda vai sair de novo."

                d "Sim, vamos... E parece que nem isso te deixa pra baixo, hein?"

                mc "Não é fácil ser rejeitado, mas eu sei que ainda vou ter outra chance de conquistar esse coração."

                d "Vou estar esperando."

                jump diana_e5_amizade

    scene black with dissolve

    scene bar_atlantis geral2 with Dissolve(2.0)

    "Ela foi mesmo..."

    if diana_namoro:

        "Nem acredito que a gente começou a namorar."

        "Até um tempo atrás parecia que seria impossível. Ela sempre pareceu ligas acima, mesmo sendo uma das únicas que realmente perguntavam sobre mim."

        "Mas agora a gente tá junto e eu quero proteger ela do Barão e de todo o resto."

    "A [d] falou de coisas importantes hoje. Eu preciso de um tempo com calma pra processar tudo isso."

    "Tenho que colocar as coisas em ordem pra entender o que acontece com ela se realmente eu quero ajudar."

    "Eu sinto que a situação dela não morre com ela ou até com o Cassino. O Barão faz parte de algo maior, muito maior."

    "A [d] sabe muito mais do que ela me falou. Mas ela quer me proteger. Eu sinto isso."

    "Eu vou investigar tudo isso e escrever uma matéria pra revista. Quanto mais o tempo passa, mas eu vejo como tem matérias incríveis nesta ilha."

    "Eu preciso ficar de olho aberto e fazer as escolhas certas. Não dá pra deixar certas coisas passarem batidas."

    "E o pior, dá pra ver que em algum momento eu vou ter que fazer uma escolha que vai fazer eu me confrontar com quem realmente importa na capital."

    "Tenho que me preparar o máximo possível."



    label diana_e5_final:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v34_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v34_fim","final","local")

    scene black with Dissolve(3.0)

    call checa_final from _call_checa_final_17

    jump call_cidade

    label diana5_ape:

        "Eita que a gente vai ter que ir de busão..."

        pause 1.0

        scene ilha_vista_noite with Dissolve(1.0)

        pause 1.0

        mc "É aqui. Desculpa por fazer você pegar o busão..."

        d "Foi uma experiência... inédita."

        d "Mudando de assunto, não imaginei que você teria cacife para viver em um prédio como este."

        mc "Haha... as coisas acontecem, né?"

        d "Fico imaginando como você conseguiu isso."

        "Eita... se ela soubesse da minha relação com a velha Gina..."

        mc "Mistérios do jornalismo... não tente pensar muito nisso."

        mc "Ah!"

        mc "Diana... só me dá um segundo pra eu ver se tá tudo ok."

        d "Haha... tudo bem."

        scene black with dissolve

        if xiang_casa:

            scene xiang_ape3 with Dissolve(1.0)

            mc "Oi, Xiang."

            "Xiang" "Olá. Onde [mc] tava?"

            mc "Passeando... olha... eu trouxe uma amiga comigo. A gente vai ficar um tempo no quarto."

            "Xiang" "Hm?"

            mc "Fica quietinha, ok? Faz esse favor pro [mc]."

            "Xiang" "Tá..."

            mc "Valeu!"

        if karli_casa:

            scene ap_karli cama with Dissolve(1.0)

            mc "Fala aí, mina."

            "Karli" "Qual a boa?"

            mc "Por que você já tá aqui?"

            "Karli" "Você tava demorando, achei que você ia passar a noite fora, daí né..."

            mc "Eu preciso que você fique de boa hoje. Trouxe uma amiga aí."

            "Karli" "Amiga, né? Bom... ela é gata?"

            mc "Super gata."

            "Karli" "Hmm... então..."

            mc "Só dá o fora e deixa eu usar o quarto."

            "Karli" "Ok... ok..."

        scene black with dissolve

        mc "Pode vir, Diana. A barra tá limpa. Vamo pro quarto."

        d "Tudo bem..."

        pause 1.0

        scene ap quarto with Dissolve(1.0)

        mc "Pronto."

        if xiang_casa or karli_casa:

            d "Aquela na sala era sua amiga?"

            mc "Sim."

            d "Ela vai deixar a gente... em paz?"

            mc "Com certeza."

        d "Ok... e agora?"

        mc "Agora você vem aqui."

        scene d5_premium12 with vpunch

        pause

        d "HMM!"

        d "A-assim, é?"

        mc "Você me provocou demais, [d]. Todas as vezes que a gente quase chegou lá."

        mc "Hoje sou só você e eu..."

        d "É..."

        mc "Hoje eu quero ir até o fim não importa o que aconteça. Você quer também, né?"

        d "Claro. Eu tô louca pra isso, [mc]."

        d "Amanhã a gente pessa nas consequências."

        mc "Exatamente."

        d "Tá bom. A gente não precisa perder tempo com preliminares. Eu tô pronta."

        scene black with dissolve

        scene d5_premium13 with Dissolve(1.0)

        pause

        d "Eu não preciso usar vestido aqui."

        mc "D-diana!?"

        d "Vem logo. Não precisa dessa cara de espanto. Eu sou uma mulher excitada, só isso."

        mc "Ah... eu vou aproveitar muito você."

        d "Eu falei que não precisa de preliminar. Eu tô pronta desde o bar."

        d "Deixa eu preparar você pra você se lambuzar em mim."

        mc "T-tá."

        scene black with dissolve

        scene d5_premium14 with Dissolve(1.0)

        pause

        mc "Ah... sua boca..."

        d "Deixa eu molhar bem ele."

        mc "É bom demais..."

        d "Calma, não vai se empolgar demais, [mc]. Você não quer perder o prato principal da noite."

        mc "Não fala assim que só piora."

        d "Tá bom ou quer mais?"

        "Se ela continuar assim... pode ser que eu chegue lá rápido demais... ou será que eu aguento."

        menu:
            "Continua mamando.":


                mc "Pode continuar mamando... você é boa demais nisso."

                d "Eu posso fazer melhor. Olha aqui."

                scene d5_premium15 with Dissolve(1.0)

                pause

                mc "A-ah..."

                d "Delíxia!"

                d "{i}Slhup slip{/i}"

                mc "Que boca incrível..."

                d "Obrrigadxa."

                "M-melhor eu parar aqui antes que eu acabe na boca dela."

                mc "T-tá bom, Diana."
            "Hora da verdade.":


                mc "Eu não aguento esperar."

        mc "Eu quero comer você agora."

        d "Não via a hora."

        scene black with dissolve

        scene d5_premium16 with Dissolve(1.0)

        pause

        mc "Eu vou colocar."

        d "Vai... enfia..."

        mc "Vai ser a primeira vez que eu vou comer você direito, Diana."

        d "Ah... verdade... agora não tem pressa nem perigo. Pode fazer como você quiser."

        mc "Desde que a gente se conheceu lá na praia... eu não via a hora disso, sabia?"

        d "Não minta."

        mc "É verdade. Você é uma mulher incrível. A mulher mais requintada que eu já conheci."

        d "E agora ela tá de perna aberta esperando seu caralho..."

        mc "Não precisa esperar mais!"

        scene d5_premium17 with hpunch

        pause

        d "Aannh!"

        mc "Agh!"

        d "T-tá dentro..."

        mc "E entrou tão fácil, Diana."

        d "Eu falei que eu tava pronta... eu quero muito você, [mc]."

        mc "Hoje eu vou fazer você minha."

        d "Faz! Pode começar!"

        mc "Toma, Diana! Sente meu amor!"

        scene d5_premium18 with hpunch

        pause

        d "Ah! Ahnn!"

        mc "Gostosa!"

        d "Assim que eu esperava! Ahnng!"

        mc "É bom?!"

        d "Melhor que eu imaginava! Annngh!"

        d "Nunca pensei que isso ia ser tão bom!"

        mc "Meu pau é uma delícia?!"

        d "Sim! Annh! Aanh!!"

        d "Você é uma delícia, [mc]!"

        mc "AAgh!"

        d "Faz gostoso em mim!"

        mc "Faço!"

        d "ANNGH! ANNNGH!"

        mc "Vai gozar, já?!"

        d "V-vou! N-não para por favor!"

        "Será que eu deixo ela gozar ou mudo de posição?"

        menu:
            "Então goza!":


                mc "Então goza, Diana! Goza no meu caralho!"

                d "Vou gozar! Tô gozando!!!"

                scene d5_premium19 with vpunch

                pause

                d "AAAHHHHH!"

                scene d5_premium19 with vpunch

                d "I-incrível!"

                mc "Uau... foi bom, hein?"

                d "A-ainda tô... aah..."

                mc "Agora é minha vez."
            "Segura aí.":


                mc "Nada disso... ainda tá muito cedo pra você."

                d "Não... não para por favor!"

                mc "Eu quero que a gente goze juntos."

                d "Então vai... vai logo..."

        d "Eu tô muito sensível..."

        mc "Mas eu não vou parar agora."

        mc "Vira aqui pra mim."

        d "A-ah..."

        scene black with dissolve

        scene d5_premium20 with Dissolve(1.0)

        pause

        d "Eu não sei como vai ser... eu tô tão... ah..."

        mc "Eu acho que você vai gostar."

        d "Eu tô toda... nnghh..."

        "A Diana tá tão sexual agora. Eu quero muito gozar nela..."

        mc "Se prepara, Diana."

        d "Vem... vem em mim."

        scene d5_premium22 with vpunch

        pause

        d "AAIINN!"

        mc "Você tá mais apertada, Diana!"

        d "T-tá! T-tá demais, [mc]!"

        mc "Eu vou ficar louco comendo você assim!"

        d "Fica! Sente minha bunda batendo em você!"

        mc "Ahh! Impossível não sentir! Olha pra essa raba gorda!"

        d "Ainn! É pra você comer!"

        mc "Diana! Eu vou acelerar!"

        d "C-cuidado!"

        scene d5_premium21 with hpunch

        pause

        d "AANNGH! AANNNHH!"

        mc "Eu vou gozar!"

        d "Goza! Eu vou gozar também!"

        mc "Goza comigo, Diana!"

        d "Vem, [mc]! AANNH!! Come!!! ANNGHH!!"

        d "Mais um pouco! VAII!!"

        mc "Tá vindo, gostosa!!!"

        d "Joga tudo em mim! AANNNNGHHH!"

        scene d5_premium23 with hpunch

        pause

        mc "GOZAAANDDOOOO! AAAGHH!"

        d "AAAANNNGHH!"

        scene d5_premium23 with hpunch

        d "MINHA NOSSA!"

        mc "Aaagh... agh..."

        d "Aah..."

        mc "Tá saindo tudo..."

        d "Eu tô sentindo... escorrendo..."

        d "Eu preciso... uff..."

        scene black with Dissolve(2.0)

        pause 2.0

        d "Ufa..."

        scene d5_premium24 with Dissolve(1.0)

        pause

        d "Ah... o que foi isso, [mc]? Foi... demais."

        mc "Eu também achei. Você foi incrível, Diana."

        d "Obrigada..."

        mc "E você parece radiante."

        d "Você tá se elogiando às minhas custas. Isso não é romântico."

        mc "Deixa eu aproveitar um pouco. Parece que você gostou bastante."

        d "Adorei..."

        mc "Eu também amei."

        menu:
            "Deixa eu me ajeitar em você?":


                mc "Posso me ajeitar em você um pouquinho?"

                d "Hm? Claro."

                scene black with dissolve

                scene d5_premium25 with Dissolve(1.0)

                pause

                d "Esse tipo de carinho também é bom, né?"

                mc "Com certeza."

                d "Agora que a gente tá junto, a gente pode ficar assim sempre que tiver a chance."

                mc "Eu já tô ansioso."

                d "Eu só espero poder resolver meus problemas. E que você consiga os seus também."

                mc "Nem fala. Mas pode contar comigo, tá?"

                d "Não sei o quanto você pode me ajudar nisso."

                mc "Eu sei que o dono do Cassino tá envolvido em tramóia. Se eu puder, eu vou te salvar dele."

                d "Ah... Essas pessoas são grande demais pra nós, seres humanos, [mc]."

                d "Precisamos ser adultos e aceitar nosso lugar. Não desistir, mas reconhecer quando são apenas fantasias."

                mc "Hmm... não sei... eu tenho vivido coisas que talvez eu possa... sei lá..."

                d "Não faça promessas que você não pode cumprir."

                mc "Ok... eu vou ficar quieto e aproveitar meu carinho."

                d "É a melhor coisa que você faz."

                mc "Você não é fácil, Diana..."

                d "Não. Eu sou eu."

                mc "..."

                pause 1.0

                show black with dissolve

                hide black with dissolve

                mc "Acho que eu dei uma pescada."

                d "Tudo bem. É gostoso mexer em você."
            "E agora?":


                pass

        mc "E agora? Quer passar a noite aqui?"

        d "Se você quiser que o Barão apareça aqui e dê um tiro no meio da sua cara."

        mc "E-ei..."

        d "Esse homem não é brincadeira, [mc]."

        mc "Ele que é o tal ciumento, né?"

        d "Sim..."

        d "Eu preciso voltar e ele não pode me ver com você. E eu vou ter que aguentar por ter ficado a noite toda fora."

        mc "Diana, se eu soubesse..."

        d "Não precisa ficar assim. Eu sou adulta e escolhi o que eu quis. A vida é assim."

        d "Agora, eu só preciso que você não tenha medo de ficar comigo de novo."

        mc "C-claro que não. Eu entendo."

        d "Muito bem. Na próxima vez... eu quero que seja mais intenso que a noite de hoje."

        d "Tem uma coisa que eu gostaria de tentar... com meu corpo."

        mc "Hm?"

        d "Eu quero que você use outra parte do meu corpo. Eu acho que pode ser muito... prazerosa."

        mc "A-ah... não me deixa excitado de novo."

        d "Agora eu vou me arrumar e sair. Até a próxima, [mc]."

        mc "Eu te acompanho."

        d "Não. O Cassino fica cruzando a praça. Não se preocupe."

        mc "M-mas."

        d "[mc]... por favor."

        mc "Ok..."

        d "A gente vai se ver de novo..."

        scene black with Dissolve(1.0)

        scene ilha_vista_noite with Dissolve(1.0)

        "Ela foi mesmo..."

        if diana_namoro:

            "Nem acredito que a gente começou a namorar."

            "Até um tempo atrás parecia que seria impossível. Ela sempre pareceu ligas acima, mesmo sendo uma das únicas que realmente perguntavam sobre mim."

            "Mas agora a gente tá junto e eu quero proteger ela do Barão e de todo o resto."

        "A [d] falou de coisas importantes hoje. Eu preciso de um tempo com calma pra processar tudo isso."

        "Tenho que colocar as coisas em ordem pra entender o que acontece com ela se realmente eu quero ajudar."

        "Eu sinto que a situação dela não morre com ela ou até com o Cassino. O Barão faz parte de algo maior, muito maior."

        "A [d] sabe muito mais do que ela me falou. Mas ela quer me proteger. Eu sinto isso."

        "Eu vou investigar tudo isso e escrever uma matéria pra revista. Quanto mais o tempo passa, mas eu vejo como tem matérias incríveis nesta ilha."

        "Eu preciso ficar de olho aberto e fazer as escolhas certas. Não dá pra deixar certas coisas passarem batidas."

        "E o pior, dá pra ver que em algum momento eu vou ter que fazer uma escolha que vai fazer eu me confrontar com quem realmente importa na capital."

        "Tenho que me preparar o máximo possível."

        if xiang_casa and xiang_casa_evento > 11:

            scene black with dissolve

            scene xiang_casa3 with Dissolve(1.0)



            "Xiang" "Acabou as coisas com ela?"

            mc "Sim..."

            scene xiang_ape8 with vpunch

            "Xiang" "A Xiang sabe o que tava acontecendo alí! A gritaria!"

            mc "X-xiang!"

            "Xiang" "Você vai ter que comer a Xiang também agora!"

            mc "Q-quê?!"

            "Xiang" "Agora!"

            "Agora? E agora?"

            menu:
                "Tá bom. Vem aqui.":


                    mc "Tá bom! Vem aqui que eu cuido de você!"

                    scene xiang_ape12 with vpunch

                    mc "Ficou com ciúmes, é?"

                    "Xiang" "Xiang quer o [mc] com ela..."

                    mc "Eu tô aqui..."

                    "Xiang" "Xiang quer mais!"

                    mc "Você vai ter mais, sua putinha!"

                    scene xiang_ape14 with vpunch

                    "Xiang" "Ahhhn!"

                    mc "Isso que você queria?!"

                    "Xiang" "É! Ahnn!"

                    "Xiang" "Xiang quer pau do [mc] dentro!"

                    mc "Caralho! Como você é gostosa!"

                    scene xiang_ape15 with vpunch

                    mc "Acabei de comer minha namorada e agora tô trepando com você aqui!"

                    "Xiang" "Ai! Aiinn! Assim!"

                    mc "Que merda eu tô fazendo!?"

                    "Xiang" "A Xiang vai gozar!"

                    mc "Eu também, Xiang! Eu vou engravidar todas vocês!!!"

                    scene xiang_ape15 with vpunch

                    mc "AAAHHH!"

                    "Xiang" "AAAAIIIHH!"

                    mc "Vocês são todas gostosas demais!"

                    scene black with Dissolve(1.0)

                    "Eu sou um otário mesmo..."
                "Eu não posso.":


                    mc "Eu e a Diana tamo namorando! Eu não posso, Xiang."

                    mc "Eu gosto de você, mas não posso fazer isso."

                    "Xiang" "Xiang não gosta assim..."

                    mc "Desculpa, linda..."

                    "Xiang" "Tá..."



        scene black with Dissolve(3.0)

        $ tempo = 4

        $ v34_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v34_fim","final","local")

        call checa_final from _call_checa_final_18

        jump call_cidade

label diana_evento4:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d4_save", extra_info="d4_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ diana_e4 = "evento"

    scene pizzaria_out_italiano with Dissolve(2.0)

    pause

    "Ufa. Cheguei."

    "Agora tenho que avisar a [d]."

    "{i}Tuuu Tuuu{/i}"

    d "Oi, [mc]."

    mc "[d]. Fiz o que você pediu. Tô aqui na pizzaria."

    d "Ótimo! Muito obrigada! Hoje é um dia perfeito pra mim!"

    d "Vou me preparar e chego logo. Espera por mim aí na frente, moço."

    mc charmoso "Pode deixar, moça."

    d "Até daqui a pouquinho."

    "..."

    "Já faz um tempinho..."

    "Ok. Deixa eu ver... tô usando a roupa de sempre, mas tô bem vestido, tô cheiroso... separei uma graninha pra pagar."

    mc zerado "Já tô vendo eles cobrarem os ol-"

    "???" "Ei. Jovem."

    mc desconfiado "Hm?"

    if v31_fim:

        "Ei! Esse não é o chefe do [mar]? O que ele quer comigo?"

        to "Esta noite eu sou só um homem tomando vinho. Tente não pensar demais."

        mc "O-ok..."

    to "Esperando sua mulher?"

    mc envergonhado "Não sei se eu poderia chamar ela de 'minha mulher'."

    to "Isso é uma pena. Hoje em dia só existe... como vocês jovens falam... 'pegação'."

    mc envergonhado "Pra falar a verdade eu não sei se eu sou tão jovem assim, então não sei qual é a palavra do momento."

    mc normal "Mas eu não falei nesse sentido. É que... a gente ainda tá nos primeiros encontros."

    to "Ah! Trazendo uma garota para um encontro aqui na pizzaria para tentar conquistá-la! Você tem garra, garoto. Muito bem!"

    mc envergonhado "Haha..."

    to "Venha. Sente aqui. Tome algo comigo enquanto ela não chega."

    mc "Não sei se e-"

    to "Pare de pensar e sente logo."

    menu:
        "Ok. Até ela chegar.":


            $ tony1 = True

            mc normal "Tudo bem. Acho que dá pra conversar até ela chegar."

            to "Isso!"

            mc "Com licença."

            to "Toda."

            scene tony_pizzaria_mesa with Dissolve(1.0)

            to "Fique à vontade. Tome uma taça de vinho. Isso vai ajudar a noite."

            mc "Obrigado."

            to "Veja, jovem. Os tempos mudaram, mas nem todos precisam mudar com ele."

            mc "O que o senhor quer dizer?"

            to "Antigamente, nós dávamos muito mais valor aos rituais. Veja no caso da conquista, por exemplo."

            to "Existiam uma série de etapas que todo casal de enamorados devia cumprir antes de realmente iniciar uma relação."

            to "Quando eu conheci minha esposa, eu a via somente no quintal da casa dela, que inclusive é aqui perto."

            to "Eu ficava de fora do portão e ela do lado de dentro. E podíamos conversar por no máximo 15 minutos."

            to "A mãe dela, claro, ficava na porta da casa, olhando e ouvindo tudo o que estávamos fazendo."

            mc envergonhado "A mãe dela realmente era preocupada."

            to "A senhora Alighieri não ligava para o que estávamos fazendo."

            mc desconfiado "Mas-"

            to "Era o pai de minha esposa que não confiava em mim. Mas, obviamente, ele não podia demonstrar isso na época."

            mc envergonhado "Acho que eu entendo."

            to "Por que dessa história? É apenas um exemplo de como as coisas eram antigamente. Os rituais, o simbolismo."

            to "Hoje não existe mais isso. Não existe mais razão intrínsica. Não existe mais valor ou significado no contato."

            to "O objetivo é a sensação física, o ósculo, o coito, o agora. Não importa com quem seja."

            to "Não existe conquista, não existe romance. Os rituais não são mais necessários, pois o que importa é a sensação e não o significado."

            to "Mas então eu te pergunto... Se o que importa é só a sensação do momento, o que os outros são para nós? Só uma ferramenta de prazer?"

            to "Quando o ser humano ficou tão egoísta? Transformar outro ser humano em não mais que um objeto de prazer..."

            mc envergonhado "É... Não sei se eu estou acompanhando tudo o que o senhor quer dizer."

            to "Não importa. Você me parece das antigas. Trazer uma mulher para um encontro em uma pizzaria familiar antes mesmo de namorar é um excelente sinal sobre seu caráter."

            to "Você é um homem de verdade, como não existe mais hoje em dia."

            mc normal "Obrigado."

            to "Perdão por me alongar demais. Ver você esperando pela sua namorada aqui deve ter despertado alguma memória minha."

            d "[mc]?"

            mc surpreso "D-diana!"

            to "Quando quiser conversar, estou sempre aqui na pizzaria pela noite. Boa sorte."

            mc charmoso "Valeu!"

            scene pizzaria_out_italiano with Dissolve(1.0)

            mc charmoso "O-oi."
        "Valeu, mas vou esperar ela aqui mesmo.":


            mc envergonhado "O-obrigado pelo convite, mas acho melhor esperar ela aqui mesmo."

            to "Você quem perde."

            mc "Haha..."

            to "Boa sorte em seu encontro."

            mc normal "Obrigado."

            scene black with dissolve

            "..."

            scene pizzaria_out_noite with Dissolve(1.0)

            "Quem será que era esse cara?"

            "..."

            "Cadê a [d]?"

            "..."

            "Será que ela deu um bolo em mim?"

            "..."

            "Ah! Tá chegando."

            d "Boa noite, [mc]."

            mc normal "Oi. Boa noite."

    show diana_vp triste with dissolve

    d "Demorei muito?"

    menu:
        "Um pouco, mas tudo bem.":


            $ diana_seducao += 1

            mc charmoso "Um pouquinho, mas não tem problema nenhum."

            d "Eu pensei que demoraria menos, perdão."

            mc "Já falei que não foi nada."

            if tony1:

                mc "Além de que eu estava conversando com esse homem aqui atrás."

                d "..."

                mc "Oi?"

                d "Ah, sim. Que bom."
        "Não, não! Chegou bem rapidinho.":


            mc surpreso "Não! Foi rapidinho!"

            d "Você pode ser sincero comigo. Eu aguento."

            mc envergonhado "Eu tô falando sério."

            d "Tá."

    mc "Vamos entrar?"

    d "Claro."

    mc "A senhorita primeiro."

    d "Obrigada."

    play sound "audio/som_6_bar.mp3"

    scene cidade pizzaria_interior with Dissolve(1.0)

    show diana_vp pose with dissolve

    d "Ora, ora."

    mc normal "Que foi?"

    d "Este restaurante não é qualquer um... parece que alguém realmente quer me impressionar."

    menu:
        "Não é nada de mais...":


            mc envergonhado "Não é nada. Eu só queria conhecer este lugar e..."

            d "Entendo... eu também não conhecia, só tinha ouvido falar. Vamos ver se a fama tem base."

            mc normal "Espero que sim."
        "Você é uma mulher requintada.":


            $ diana_seducao += 2

            mc charmoso "Você é uma mulher requintada, não posso te levar pra qualquer lugar."

            d "Claro que você não podia perder a chance de ganhar uns pontos, né?"

            mc "Com certeza. Mas falando sério, eu acredito que isso é o mínimo que eu teria coragem de levar você."

            d "Você não vai conseguir me deixar sem jeito... mesmo com essa fala mansa."

            mc "Você realmente é difícil."

            d "Eu sou só uma mulher que viu muita coisa nessa vida."

            mc "Justo."
        "Tô esbanjando!":


            $ diana_seducao += 1

            mc normal "Hoje tô esbanjando! Aproveita!"

            d "Haha! Aconteceu alguma coisa que a gente está pra comemorar?"

            mc "Você precisa de motivo pra esbanjar? Eu não."

            d "Estou vendo. Vou aproveitar então."

            mc "Só vem comigo."

    show diana_vp falando with dissolve

    d "Mas pensando aqui... você realmente tem cacife pra comer neste lugar?"

    if roupa_blacktie:

        $ diana_seducao += 1

        mc charmoso "Eu tenho um Black Tie, [d]. Eu posso comer onde eu quiser."

        d "Parece que alguém tá melhorando de vida."

        mc "Eu só paro no topo."

        d "Excelente frase."
    else:


        mc envergonhado "Eu espero que sim."

        d "Pelo lado bom, eu não vou deixar você pagar pra mim."

        mc normal "Não, não, não. De jeito nenhum."

        mc charmoso "Hoje eu tô pagando tudo. Nem pense nisso."

        d "Você quer mesmo deixar uma marca, né?"

    mc normal "Vamos pegar uma mesa?"

    show diana_vp pose with dissolve

    d "Claro."

    mc normal "Deixa eu chamar o garçom."

    mc "Com licença!"

    "Garçom" "Opa. Estou chegando!"

    show diana_vp pose at esquerda with move

    show teo_restaurante ola at entra_direita with dissolve

    "Garçom" "Boa noite."

    if v25_fim:

        "Epa. Esse é o [teo], não é?"

        teo "Ei. Você é o... [mc], amigo da [g], né?"

        mc normal "Isso. Não sabia que você trabalhava aqui."

        teo "O [caio] arranjou esse bico pra mim. Tinha que pagar a faculdade. Mas eu trabalho só de fim de semana."

        mc "Tem as aulas."

        teo "Isso."

        teo "O que vocês gostariam de pedir?"

        mc normal "A gente quer senta-"

        d "Eu gostaria de uma vegetariana. Me surpreenda."

        teo "O-ok!"

        mc normal "Pode fazer uma inteira para nós."

        teo "Combinado. Vou ver o que o chefe recomenda."

        d "Perfeito."

        teo "Vou preparar uma mesa pra vocês e já chamo o casal."

        hide teo_restaurante with dissolve

        hide diana_vp with dissolve

        show diana_vp falando with dissolve

        d "[g]..."

        mc normal "O que você disse?"

        d "Nada, não."

        mc desconfiado "?"

        teo "Podem vir e se ajeitar. A pizza chega em 5 minutos."
    else:


        mc "Boa noite."

        d "Boa noite."

        "Garçom" "O que vocês gostariam de pedir?"

        mc normal "A gente quer senta-"

        d "Eu gostaria de uma vegetariana. Me surpreenda."

        "Garçom" "O-ok!"

        mc normal "Pode fazer uma inteira para nós."

        "Garçom" "Combinado. Vou ver o que o chefe recomenda."

        d "Perfeito."

        "Garçom" "Vou preparar uma mesa pra vocês e já chamo o casal."

        mc "Obrigado."

        hide teo_restaurante with dissolve

        "..."

        "Garçom" "Podem se sentar. A pizza chega em 5 minutos."

    mc "Valeu."

    mc charmoso "Você primeiro, [d]."

    d "Com licença."

    scene diana_pizzaria_close1 with Dissolve(1.0)

    pause

    d "Qual sua primeira impressão sobre o lugar?"

    mc normal "Não sei... eu sinto uma coisa diferente neste lugar."

    d "Diferente como?"

    mc "Não sei explicar. Como se não fosse só uma pizzaria. Não sei se é a formalidade, ou a entrada que parecia tão diferente dos outros prédios."

    mc "Talvez seja esse ar meio antigo que o lugar tem. Ou toda essa decoração italiana, que parece que eu não tô mais na mesma cidade."

    d "Sem dúvidas você tem uma grande sensibilidade. Eu já te falei isso antes."

    mc envergonhado "Acho que sim."

    d "A maioria das pessoas conseguem sentir as coisas, tem essa capacidade, mas elas não querem."

    menu:
        "Como assim?":


            mc desconfiado "O que você quer dizer?"
        "Sentir não é uma questão de querer ou não.":


            mc normal "Bom... se você bota a mão no fogo, sentir dor não é lá uma questão de querer."

            d "Não viaja, [mc]. Eu não me refiro a ação e reação."

    d "Eu estou falando sobre captar energias... sobre conseguir perceber sinais."

    mc desconfiado "Tipo... você é esotérica?"

    d "Haha! Não sei se eu me encaixaria exatamente em um rótulo assim, mas eu acredito em um mundo além."

    mc normal "Entendi."

    d "Você não?"

    menu:
        "Sim. Eu acredito.":


            mc charmoso "Eu acredito, sim, que tenha algo além do que a gente vê. Não sei explicar, mas a vida tem que ser mais do que só isso."

            d "Exatamente. É isso que eu penso também."

            d "Não é possível que tudo seja acaso. Pense nas particularidades da Terra. Os animais que aprendem coisas específicas."

            d "Ou como se nosso mundo estivesse um pouco pra lá ou pra cá do Sol a vida já não seria possível."

            d "Pra mim, é impossível que tudo isso seja apenas sorte. Como tanta gente vive junta sem se matar. Existe uma ordem no universo."

            mc "Concordo com você."
        "Não. Eu só acredito na ciência.":


            mc charmoso "Não... eu só consigo acreditar na ciência, no que está comprovado por estudos sérios."

            mc "Nada contra, claro. Cada um acredita no que quer, mas, pra mim, o 'além' não existe."

            d "Mas pense comigo."

            d "Não é possível que tudo seja acaso. Pense nas particularidades da Terra. Os animais que aprendem coisas específicas sozinhos."

            d "Ou como se nosso mundo estivesse um pouco pra lá ou pra cá do Sol a vida já não seria possível."

            d "Pra mim, é impossível que tudo isso seja apenas sorte. Como tanta gente vive junta sem se matar. Existe uma ordem no universo."

            mc envergonhado "Entendo... mas talvez essa ordem não venha de algo superior, mas do simples acaso."

            d "Não consigo pensar assim..."

    mc feliz "Opa! Olha a pizza aí! Valeu!"

    scene diana_pizzaria_cena with Dissolve(1.0)

    mc "Eita. Ele colocou a pizza direto na mesa."

    d "Sim, parece que é uma tradição do lugar."

    mc "Eles tão aí há centenas de anos, né. Eles devem saber o que tão fazendo."

    d "Centenas não sei, mas é bastante tempo."

    mc "Mas você tava falando sobre o lance espiritual."

    d "Não é um 'lance espiritual'..."

    scene diana_pizzaria_mc2 with Dissolve(1.0)

    d "Esse assunto te chateia?"

    mc "Claro que não. Eu acho bem interessante."

    d "Então ok..."

    scene diana_pizzaria_cena with Dissolve(1.0)

    d "Eu não sou religiosa. Nem lembro se eu já fui em igreja antes na vida."

    mc "Sorte sua que sua família não te obrigava."

    d "É... não passei por essa fase."

    d "Mas, mesmo assim, eu sinto que existe algo mais que vai além do que a gente vê."

    d "Pode chamar de mundo espiritual, de mundo das ideias, de reino de Deus, ou o poder das fases da lua."

    "Esse vestido da [d] tem um decotão... E ela não tá usando sutiã..."

    "Caraca..."

    menu:
        "Uma olhadinha não vai matar ninguém":


            show diana_pizzaria_busto with dissolve

            pause

            "Uou!"
        "Claro que não! Por que eu tô pensando nisso?":


            $ diana_seducao += 2

            "De jeito nenhum! Se controle, [mc]!"

    d "Eu não sei explicar. Eu não estudei isso. Mas eu sinto isso."

    d "Quando eu estou compondo, eu sinto essa energia em mim. Quando eu canto também."

    d "E até quando eu escuto música, bem concentrada... eu sinto a arte em mim, algo que transcende o físico e o material."

    d "Esse sentimento, essa energia... isso pra mim não são só neurônios ou algo assim. É algo maior e mais profundo dentro de mim."

    hide diana_pizzaria_busto with dissolve

    menu:
        "Uou. Isso foi bonito, [d].":


            $ diana_seducao += 1

            mc "Uou... isso foi bem incrível."

            d "Só estou desabafando com você. Obrigada por me ouvir."

            mc "Que nada. Dá pra ver que você é uma pessoa com conteúdo."

            d "Haha... espero que isso seja um elogio."

            mc "Claro que é!"
        "Que doideira...":


            mc "Que doideira, [d]..."

            d "Você acha?"

            mc "Assim... eu não consigo entender exatamente o que você tá falando. Eu não consigo sentir muito isso."

            d "Sério? Tem certeza? Eu sempre achei você uma pessoa sensível."

            mc "Bom... agora que você falou assim, não tenho mais tanta certeza!"

            d "Hahaha! Perdão."

            mc "Haha... tudo bem."

    scene diana_pizzaria_mc3 with Dissolve(1.0)

    d "Hmmm... tô me sentindo melhor depois de ter falado sobre isso."

    d "Às vezes eu me acho louca por pensar nisso. Parece que as pessoas ou não acreditam em nada ou são fanáticas."

    mc "Não existe mais meio termo?"

    d "Algo assim. Mas deixa eu falar. Essa noite tá me fazendo muito bem."

    mc "Sério? Que bom. Eu não sei se eu sou a melhor companhia às vezes."

    d "O que você quer dizer com 'ser a melhor companhia'?"

    mc "Quero dizer, tipo assim... se eu sei conversar, se eu sei ouvir. Ué. Uma companhia agradável."

    d "Então você realmente é um garotinho inseguro..."

    mc "Ei. Vai usar o que eu falo contra mim agora?"

    d "Desculpa."

    d "Na minha opinião pessoal, você é uma excelente companhia."

    d "Você é atencioso, você sabe ouvir, não faz brincadeira idiota, não fala merda demais. E como um adicional, ainda é engraçado e fofo de vez em quando."

    mc "Uou..."

    d "Uou digo eu."

    if diana_quente:

        d "Por que você acha que rolaram as coisas que rolaram com a gente lá no Cassino?"

        mc "É... você também é uma mulher incrível."

        d "Eu sei. Muitos diriam que eu sou areia demais pro seu caminhãozinho."

        mc "Metida!"

        d "Mas não é verdade. Você realmente despertou esse desejo em mim."

        mc "Você também."
    else:


        d "Pena que você não quer nada comigo, né?"

        mc "C-como assim?!"

        d "Já podia ter rolado algo entre a gente faz tempo, mas você se faz de bobo."

        mc "D-Diana..."

        d "Se você quer algo comigo, hoje é o último dia que vou te esperar antes de te colocar friendzone. Acho bom você pensar bem."

        mc "O-ok."

    mc "Já que você falou sobre isso, deixa eu te perguntar. Como é sua vida amorosa? Tá vendo alguém?"

    "Merda... não sei se eu devia ter puxado esse assunto."

    d "Isso é ciúmes?"

    mc "Você também não perde uma chance de me azucrinar..."

    d "Por que você está tão sensível, [mc]?"

    mc "Tá viajando..."

    scene diana_pizzaria_mc2 with Dissolve(1.0)

    d "Pode falar pra mim. Aconteceu alguma coisa?"

    mc "Não aconteceu nada."

    d "Você tá se metendo muito no problema dos outros?"

    mc "..."

    d "Eu sabia."

    mc "Não é só isso. É que às vezes eu não sei como agir."

    d "O que você não está sabendo como agir?"

    "Será que eu devo falar sobre minhas coisas pra [d]?"

    if diana_e3 != "horrivel":

        "Quando a gente foi pro quarto dela na outra noite, ela realmente se interessou pela minha história."

        "Acho que ela foi a única garota até hoje que realmente perguntou algo sobre mim."

    menu:
        "Não é nada. Só coisa da minha cabeça.":


            mc "Relaxa, não é nada."

            d "Claro que é!"

            mc "Não quero falar sobre isso com você."

            d "Mas eu quero te ajudar."

            mc "Você me ajuda vindo comigo e passando um tempo incrível comigo."

            d "[mc]..."
        "É que estão acontecendo tantas coisas...":


            $ d4_desabafou = True

            $ diana_seducao += 3

            mc "Tudo... de uns tempos pra cá tem acontecido tanta coisa na minha vida."

            if diana3_segredo:

                d "Desde que você xeretou o celular da [cc] quando ela foi no banheiro?"

                mc "Ei... você ainda não esqueceu isso?"

                d "Não... mas eu te disse que seu segredo tá seguro comigo."

                mc "Valeu."

            d "Mas me fale melhor."

            mc "Eu não quero encher você com as minhas coisas."

            d "Não seja medroso. Fale o que você tem que falar. Pode confiar em mim, [mc]."

            mc "Igual esse negócio de ser paparazzo. Entregar confidências de pessoas que são minhas amigas pelo meu trabalho."

            mc "Isso realmente tá certo, [d]?"

            mc "Eu fico dizendo que eu tenho que fazer isso pra poder viver aqui na capital, mas será que é verdade? Esse é o único jeito?"

            mc "E se eu continuo fazendo isso por que é mais fácil?"

            d "Eu te entendendo. Não é uma questão simples."

            mc "Tem uma jornalista lá na redação que faz tudo o que precisa pelo sucesso. Ela não tá nem aí pra nada. E só se dá bem."

            mc "Será que esse é meu destino também?"

            scene diana_pizzaria_close2 with Dissolve(1.0)

            d "Olha, [mc]. Você falou uma coisa agora que... tem muito a ver comigo também. Por isso eu posso falar que te entendo."

            d "Às vezes, viramos escravos de uma situação que nos colocamos ou que alguém nos colocou."

            d "A gente meio que se acostuma com a situação e não consegue mudar, não consegue sair dela."

            d "Trabalhar e ganhar dinheiro... quase ninguém pode fugir dessas algemas."

            d "A rotina de acordar, trabalhar, voltar e se divertir no tempo que sobra. Um ciclo que a maioria de nós vivemos."

            d "Uma roda que dá uma volta a cada 24 horas e não temos como parar. Vamos morrer de fome? Viver na rua? É nossa responsabilidade continuar rodando."

            mc "Então os fins justificam os meios? Pelo dinheiro eu posso fazer tudo?"

            d "Eu não acho que a resposta seja um ou outro. Ser ou não ser paparazzo. Eu sinto que você pode ser bom ou ruim, não importa o que você faça."

            d "Você pode ser um paparazzo ético ou antiético. Depende de você."

            d "Eu sei que estou parecendo um livro de autoajuda, mas não tem como ser mais sincera do que isso sem dar uma palestra."

            mc "Eu entendo..."

            mc "Obrigado. É bom poder falar sobre isso com alguém."

            d "Não precisa agradecer."





    scene diana_pizzaria_falando with Dissolve(1.0)

    d "Você já me ajudou muito, [mc]. Desde quando você publicou a pauta sobre meu single."

    mc charmoso "Você que me ajudou com a pauta."

    d "Eu queria ter mais novidades pra falar pra você, mas acho que o show não vai acontecer."

    mc angustiado "Sério?! Por que?!"

    d "O Barão não gostou da música..."

    mc preocupado "É o Barão que decide sobre suas músicas?"

    d "É o Barão que decide sobre tudo..."

    mc desconfiado "Como assim tudo?"

    d "..."

    mc preocupado "O que aconteceu, [d]?"

    if diana_e3 != "horrivel":

        d "Você já deve ter uma ideia depois do que aconteceu lá no meu quarto aquele dia."

        mc desculpa "..."

    d "Não é fácil falar sobre isso, [mc]. Eu... acho que nunca falei pra ninguém."

    mc "Pode falar pra mim. Eu quero te ajudar."

    d "..."

    scene diana_pizzaria_close2 with Dissolve(1.0)

    d "Eu... Você já se sentiu preso? Como se sua vida te prendesse."

    d "Sentir que ninguém em volta de você dá a mínima pro que você quer, pro que você gosta!"

    d "As pessoas querem que você faça isso, faça aquilo, e não tão nem aí pro que você tá sentindo?"

    d "Você tenta fazer algo! Você fala, você chora... você briga... mas nada muda."

    d "É assim que eu me sinto... todos os dias..."

    mc preocupado "[d]... sempre tem um jeito da gen-"

    d "Não tem... Nem tudo tem solução. Tem vez que a gente se enterrou fundo demais."

    mc desculpa "Eu não acho que seja pra semp-"

    scene diana_pizzaria_chorando with vpunch

    d "Não, [mc]! Não tem! Não fala merda!"

    d "Tem gente que se mete no buraco porque quis! Porque o filho da puta tinha que comprar a porra do carro e não consegue pagar!"

    d "Só que tem gente que foi enfiada no buraco sem ter escolha!"

    mc preocupado "Calma, [d]. As pessoas t-"

    d "O que importa?! Eu nunca mais vou ver ninguém aqui! A porra do garçom! Nem ninguém!"

    mc angustiado "Por que não iria?! Cal-"

    d "Eu não posso! Não posso! [mc]! Me escuta pelo amor de Deus!"

    "Caralho... tá todo mundo olhando pra gente. O que eu faço?"

    "A [d] tá completamente fora de controle."

    d "Eu..."

    mc angustiado "Respira, [d]."

    d "{i}puuuuuuuf{/i}"

    mc preocupado "Vai ficar tudo bem."

    d "[mc]..."

    mc "Isso. Calma..."

    "Ufa. Ela tá melhorando."

    d "Desculpa... eu não queria..."

    mc "Tudo bem. Tá tudo bem."

    d "Eu sou uma..."

    mc "..."

    d "Não consigo falar. Desculpa."

    mc "Tudo bem. Tudo bem. Não precisa falar."

    d "Não importa o que eu quero. O que importa é o que o Barão quer."

    mc "Entendi."

    d "Ele... pode fazer o que quiser comigo."

    mc preocupado "[d]..."

    scene diana_pizzaria_mc2 with Dissolve(1.0)

    d "..."

    d "Desculpa. Eu não queria-"

    d "{i}snif{/i}"

    d "Não queria estragar tudo."

    d "{i}shiuf{/i}"

    d "Não estou me sentindo bem. Vou ao toalete."

    mc "Certeza que você quer ficar sozinha? Não quer andar por aqui?"

    d "Não. Eu já volto."

    mc "O-ok."

    scene pizzaria_interior2 with Dissolve(1.0)

    "O que aconteceu aqui?"

    "Por que ela surtou desse jeito? Justo ela que é tão... adulta, sei lá."

    "A gente acabou nem encostando na comida..."

    "Eu queria poder fazer alguma coisa por ela."

    "Será que foi culpa minha?"

    "Porra... Eu tô pensando em um milhão de coisas ao mesmo tempo."

    "Se eu não manter a calma, não tem como eu ajudar ela."

    "{i}catraak{/i}"

    "Ela tá saindo. Deixa eu ver ela."

    mc envergonhado "O-oi. Tudo bem?"

    show diana_vp triste with dissolve

    d "Mais ou menos. Estou com muita vergonha de ter gritado aquela hora. Sorte que não colocaram a gente pra fora."

    mc "Tudo bem. Foi coisa rápida."

    d "Desculpa, [mc]. De verdade. Eu estraguei tudo. Eu devia ter ficado quieta."

    d "A única noite que eu... e eu estraguei tudo... com o cara mais legal que eu conheço."

    mc preocupado "Calma. Não estragou nada. Você precisava disso."

    d "Para de ser legal comigo, [mc]. Isso só me deixa mais triste."

    mc angustiado "!"

    mc desculpa "Eu..."

    d "Eu vou chamar meu motorista."

    hide diana_vp triste with dissolve

    "Não! Eu não quero que ela vá assim!"

    scene diana_pizzaria_saindo with Dissolve(2.0)

    pause

    mc "[d]! Por favor!"

    d "Me deixa, [mc]! Você tentou, mas não dá."

    d "Eu sou fodida demais pra você."

    mc "[d]!!"

    d "..."

    menu:
        "Deixar ela ir":


            $ diana_e4 = "horrivel"

            "É triste... mas não posso decidir por ela."

            mc "Fica bem, [d]..."

            d "..."

            scene black with Dissolve(1.0)
        "Segurar o braço e dar um beijo nela":


            "O que eu faço?! Como eu paro ela!?"

            "Desculpa, [d]. Mas eu não posso deixar você ir assim!"

            mc "Vem aqui!"

            scene black with hpunch

            d "Ei!"

            scene diana_pizzaria_beijo with hpunch

            pause

            d "Hhmmmm!!"

            "Desculpa! Desculpa! Mas é a única coisa que veio na minha cabeça!"

            d "Hmm..."

            mc "Desculpa, eu-"

            if diana_seducao >= 27:

                $ diana_e4 = "seducao"

                d "Não para. Me beija mais."

                d "Me beija toda."

                mc "..."

                d "Vem. Beija aqui."

                scene diana_pizzaria_beijo2 with Dissolve(2.0)

                pause

                d "Hmmm... isso, com vontade."

                mc "Você é deliciosa, [d]."

                d "[mc], você me deixa doida. Faz assim. Me aperta."

                window hide

                pause



                d "O que você acha da gente continuar o que a gente não conseguiu aquele dia?"

                mc "Aqui?!"

                d "Qual o problema? Eles têm um banheiro bem bonito..."

                mc "S-sério?"

                d "Pare de gaguejar e me responda, homem. Você quer transar ou não?"

                label diana4_premium1:

                    pass

                menu:
                    "Claro!":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_54

                            jump diana4_premium1

                        mc "Claro. Onde é o banheiro?"

                        d "Vem comigo."

                        scene black with Dissolve(1.0)

                        scene d4_premium2 with Dissolve(1.0)

                        pause

                        d "Pronto! Agora a gente tá sozinhos aqui!"

                        mc "E você tá incrível, igual sempre."

                        d "Você acha demais?"

                        mc "Você é demais..."

                        d "Obrigada, mas não é isso... eu digo... transar no banheiro..."

                        mc "Nunca imaginei que você toparia fazer algo assim em um banheiro público."

                        d "Você acha que eu não gosto de me divertir? De ser um pouco... suja de vez em quando?"

                        mc "Você sempre foi tão requintada... agora um banheiro."

                        d "Esse banheiro... não sei... tem alguma coisa nele que tá mexendo comigo."

                        mc "S-sério?"

                        d "Transar com você aqui... hmm... tá me deixando quente pra caramba, [mc]."

                        "O que tem de diferente aqui? Será que é por causa do dono?"

                        d "Mas não é só um banheiro italiano que me deixou assim... foi você. Do jeito que você me pegou quando eu tava saindo."

                        d "Então vem logo aqui e continua o que você começou lá, garotão."

                        mc "Vem logo então."

                        scene black with dissolve

                        scene d4_premium3 with Dissolve(1.0)

                        pause

                        d "Hnnng! É isso que eu queria."

                        mc "Eu tô aqui pra você, gata."

                        d "Isso. Eu não quero que você se segure. Eu quero gemer muito alto aqui."

                        mc "Só não esquece que a gente tá no banheiro da pizzaria, sua louca."

                        d "Por isso mesmo!"

                        d "Me agarra mais forte. Me joga na parede, gostoso."

                        d "Tira essa roupa. Vem aqui!"

                        mc "Então toma!"

                        scene d4_premium4 with hpunch

                        pause

                        d "Ai!"

                        mc "Gostou?!"

                        d "Isso! Me segura assim! Na parede!"

                        d "Annh!"

                        mc "Você quer que todo mundo escute, é?!"

                        d "Que eu tô dando no banheiro?!"

                        mc "É!"

                        d "Nnnnghh!"

                        "Ela tá fazendo barulho mesmo. Se pegarem a gente de verdade..."

                        d "Que foi? Já tá cansando?!"

                        d "A gente não tem mais 12 anos, [mc]. A gente não precisa parar no beijo."

                        mc "Diana, mas as pessoas..."

                        d "Esquece os outros e só me pega! Se eles processarem a gente, valeu a pena me pegar, não valeu?!"

                        mc "E se a gente fosse na minha casa continuar lá?"

                        d "De jeito nenhum! Eu não aguento! Só vai logo!"

                        "Será que eu continuo com essa loucura da Diana? Ainda mais no restaurante do..."

                        menu:
                            "É perigoso!":


                                mc "Diana, eu quero muito ficar com você, mas esse aqui não é o lugar."

                                d "Tudo isso é medo deles?"

                                mc "A gente pode continuar lá em casa."

                                d "[mc]... você tá certo... desculpa... não sei o que deu em mim..."

                                mc "Vamos?"

                                d "Tá. Me coloca no chão..."
                            "Foda-se! Eu quero ela!":


                                mc "Eu vou fazer você implorar pra eu parar."

                                d "Faz mesmo!"

                                mc "Mas antes eu vou preparar você."

                                scene black with dissolve

                                scene d4_premium5 with Dissolve(1.0)

                                pause

                                d "Ai, minha nossa!"

                                mc "Hmmm!"

                                d "Isso é bom demais, [mc]!"

                                d "Aainnn! AAHNNN!"

                                "Não, ela tá começando a gemer demais!"

                                d "AANMNGH! ME LAMBE!"

                                d "AAGNN! AANNGH!!!"

                                mc "D-diana!"

                                d "Não para! VAII! AAAHHHH!"

                                scene d4_premium6 with vpunch

                                pause

                                d "OOHHH!"

                                d "AAAH! AAANNGHH!"

                                "Já que eu vou me ferrar quando eles nos arrancarem daquí dando tiro, melhor morrer dando prazer pra ela."

                                d "AANGH! AAAGHHH! ASSIM!!!"

                                d "Essa é a melhor língua do mundo! E você sabe usar ela!"
                                scene dnew_ani13 with Dissolve(1.0)
                                mc "NNGH!"

                                d "ASSIM! VAIII! EU VOOOUUU!"

                                mc "..."

                                d "Que foi?! Falta pouco, [mc]... não desiste agora, por favor..."

                                mc "Quem tá desistindo?"

                                d "Você! Move essa língua pelo amor de tudo que é mai-"

                                mc "Não não... você não vai gozar aqui."

                                scene black with dissolve

                                scene d4_premium1 with Dissolve(1.0)

                                d "Por que?!"

                                menu:
                                    "Eu vou te comer aqui.":


                                        mc "Hoje a gente vai até o fim."

                                        mc "Se você tá afim de dar aqui nesse banheiro, eu não vou negar. Vem aqui."

                                        scene black with dissolve

                                        scene d4_premium7 with Dissolve(1.0)

                                        pause

                                        d "A-ai!"

                                        mc "Assim que você queria?"

                                        d "Ai, [mc]... o que você vai fazer comigo?"

                                        mc "Eu quero te comer de quatro. Dessa vez eu não vou parar até aproveitar você inteirinha."

                                        d "Eu... eu vou berrar se você meter esse pau gostoso em mim..."
                                        scene dnew_ani12 with Dissolve(1.0)
                                        mc "Tô nem aí. Eu adoro escutar você gemendo."

                                        d "Mas nesse lugar..."

                                        mc "Que foi?! Agora você tá dando pra trás?!"

                                        d "!"

                                        d "..."

                                        d "Hmmm... pode me comer como você quiser. Só faz eu gemer e gozar gostoso."

                                        mc "Era isso que eu queria ouvir, Diana."

                                        d "Mmnnn..."

                                        scene d4_premium8 with Dissolve(1.0)

                                        pause

                                        d "Nnnnghhh... ah... para de roçar ele assim..."

                                        mc "Deixa eu curtir bastante..."

                                        d "Eu preciso logo... faz eu gritar, [mc]!"

                                        "Por que a Diana tá assim?"
                                        scene dnew_ani14 with Dissolve(1.0)
                                        "Não é ela que sempre curtiu uma provocação... uma sensualidade... e agora tá implorando pelo meu pau?"

                                        d "Vai... não aguento mais..."

                                        "Será que aconteceu alguma coisa? Alguma coisa que deixou ela assim?"

                                        "Talvez fosse melhor eu parar..."

                                        d "Vaiinn..."

                                        menu:
                                            "Temos que conversar.":


                                                mc "Calma, Diana... tem alguma coisa errada acontecendo aqui. A gente precisa conversar."

                                                d "Conversar?! Agora?! Eu tô molhada pronta pra você!"

                                                mc "Você não tá parecendo você. Vem aqui..."

                                                d "[mc]!"

                                                scene black with dissolve

                                                scene d4_premium1 with Dissolve(1.0)

                                                mc preocupado "O que aconteceu?"

                                                d "Nada..."

                                                mc "Você pode confiar em mim. Pode me falar."

                                                d "Droga... Quem mandou eu me apaixonar por um homem igual você..."

                                                mc "..."

                                                d "[mc]... você tá certo... desculpa... não sei o que deu em mim..."

                                                d "Obrigada por perceber isso... e me ajudar a colocar a cabeça no lugar."
                                            "Fazer o que ela quer":


                                                mc "Calma... você já vai perder a cabeça..."

                                                scene d4_premium9 with Dissolve(1.0)

                                                pause

                                                mc "Olha pra essa raba..."

                                                d "Você gosta mesmo do meu bumbum, né?"

                                                mc "É a bunda mais bonita que eu já vi na minha vida..."

                                                d "Quantas bundas você já viu assim?"

                                                mc "Por esse ângulo... desse jeito... acho que só a sua."

                                                d "Hmmm... eu me sinto tirando sua virgindade... agora vai... enfia."
                                                scene dnew_ani18 with Dissolve(1.0)
                                                d "Era isso que você queria desde aquela outra vez. Agora voce tem a chance."

                                                mc "Tem razão..."

                                                d "Eu prometo que você vai ter muitas chances de olhar pra minha... raba... desse jeito."

                                                mc "Ah..."

                                                mc "Então agora... não assusta..."

                                                "{i}BLANG{/i}"

                                                mc "A p-porta!"

                                                d "!!!"

                                                "..."

                                                d "Ufa... acho que só bateram na porta..."

                                                mc "Foi sem querer provavelmente... eu achei que ia ter que parar bem agora..."

                                                d "Huhum... então vai, gato... aproveita e se esbalda! Você me deixou tão molhada..."

                                                mc "Você sabe mesmo me provocar, Diana! Toma!"

                                                scene d4_premium10 with vpunch

                                                pause

                                                d "AAAAGH!"

                                                mc "Tô dentro! Não acredito!"

                                                d "HNNG! Eu tô sentindo!"

                                                mc "Ah... eu tô no céu..."
                                                scene dnew_ani16 with Dissolve(1.0)
                                                d "Aproveita, que depois dessa a gente vai pro... hmm... inferno!"

                                                mc "Tudo bem?"

                                                d "Tudo. Você é do tamanho certo, e você deixou ela pronta pra você."

                                                d "Pode começar... eu não aguento mais esperar!"

                                                mc "Finalmente você vai ter o que você queria desde o começo. Vai gritar como você nunca gritou na vida!"

                                                d "Veemmm!"
                                    "A gente vai lá pra casa.":


                                        mc "Diana, eu quero muito ficar com você, mas esse aqui não é o lugar."

                                        d "Tudo isso é medo deles?"

                                        mc "A gente pode continuar lá em casa."

                                        d "[mc]... você tá certo... desculpa... não sei o que deu em mim..."

                                        scene black with dissolve

                                        scene d4_premium1 with Dissolve(1.0)

                                        mc preocupado "O que aconteceu?"

                                        d "Nada..."

                                        mc "Você pode confiar em mim. Pode me falar."

                                        d "Droga... Quem mandou eu me apaixonar por um homem igual você..."

                                        mc "..."

                                        d "[mc]... você tá certo... desculpa... não sei o que deu em mim..."

                                        d "Obrigada por perceber isso... e me ajudar a colocar a cabeça no lugar."

                        "{i}Nnnheeecc{/i}"

                        "???" "O que é isso?!"

                        mc "HMM!?"

                        scene black with vpunch

                        d "Você!"

                        mc "!!!"

                        scene d4_premium1 with vpunch

                        "???" "Se ajeitem e vamos conversar lá fora."

                        d "Minha nossa..."

                        "???" "Estou esperando vocês... pelo amor..."

                        d "Sim..."

                        mc angustiado "..."
                    "Melhor não.":


                        mc "Diana... é melhor a gente não exagerar.{nw}"

                        "Homem" "Ei! O que os dois pensam que tão fazendo aqui?!"

                        mc "!"

                        "Homem" "Saiam já do estabelecimento vocês dois!"

                        mc "[d]!"

                        d "Sai correndo!"

                        scene pizzaria_interior2 with vpunch
            else:




                $ diana_e4 = "amizade"

                scene pizzaria_interior2 with Dissolve(1.0)

                show diana_vp irritada with dissolve

                d "Que merda foi essa?!"

                mc desculpa "Desculpa. Eu não queria que você fosse embora. Daí foi a primeira coisa que veio na minha cabeça."

                d "Sério!?"

                "Homem" "Ei! Saiam já do estabelecimento vocês dois!"

                mc surpreso "Aquele homem tá putasso!"

                hide diana_vp with moveoutright

                d "Vem, [mc]!"

                mc surpreso "!!"

            show black with moveinleft

            scene pizzaria_out_noite with Dissolve(1.0)

            mc angustiado "{i}puf puf{/i}"

            d "Hahaha!"

            mc desconfiado "Hm?"

            show diana_vp feliz with dissolve

            d "Que que foi aquilo, [mc]?! Loucura!"

            mc desculpa "E-eu não sei o que deu em mim. Acho que eu fiquei nervoso e- não sei!"

            d "Hahaha!"

            mc envergonhado "Haha...?"

            "Será que ela surtou? Ela vai me matar?"

            d "Então quer dizer que uma pessoa abandona um encontro com você. A primeira coisa que vem na sua cabeça é dar um beijo nela?"

            mc envergonhado "Bem..."

            d "Qualquer outro dia eu daria um belo tabefe nessa cara de pau!"

            mc "Que bom que hoje é hoje então..."

            d "Que... hoje é hoje?"

            d "Hahahaha!"

            "???" "[d]?"

            show diana_vp falando with dissolve

            d "Você? Já?"

            show diana_vp falando at esquerda with move

            show natasha normal at entra_direita with dissolve

            na "Boa noite."

            if v22_fim:

                mc surpreso "!!!"

                "É a [na]! O que eu faço?!"

                mc envergonhado "B-boa noite."
            else:


                mc normal "Boa noite."

            d "Por que você já tá aqui?"

            na "Bateram na sua porta e como você não respondeu, estão pensando até em arrombar. Eu vim o mais rápido que pude."

            show diana_vp irritada with dissolve

            d "Que droga..."

            d "Vamos!"

            na "Vou ligando o carro."

            hide natasha with dissolve

            hide diana_vp with dissolve

            show diana_vp pose with dissolve

            d "As coisas não aconteceram como a gente planejou."

            mc envergonhado "Não..."

            if diana_e4 == "seducao":

                if premium:

                    d "Primeiro, peço desculpas pelo que aconteceu no banheiro... eu tava fora de mim..."

                    mc safado "Aquilo no banheiro..."

                    d "Foi frustrante no final, né? Mas não se preocupa, que a gente vai ter outras chances."

                    mc zerado "Foi incrível... mas eu queria ter..."

                    d "Epa... não tenha pressa. Você vai fazer o que você tá querendo... eu também quero."

                    mc charmoso "Fico feliz de saber. Da próxima você não escapa... e vamos finalmente sacramentar isso aí."

                    d "Sacramentar... haha..."
                else:


                    mc safado "Mas aquele beijo."

                    d "Eu gostei muito. Ele me salvou, [mc]."

                    mc charmoso "A gente vai se ver de novo?"

                d "Vamos. Eu te ligo, ok?"

                mc charmoso "Ok."
            else:


                d "Muito obrigada, [mc]. Você foi um verdadeiro cavalheiro, esta noite."

                mc charmoso "Eu não fiz nada. Desculpa qualquer coisa."

                d "Sem dúvidas você é um cara como nenhum outro."

                d "A gente vai se ver ainda. Até."

                mc normal "Até, [d]."

            hide diana_vp with dissolve

            "..."

            scene black with Dissolve(1.0)

    scene mc onibus_noite with Dissolve(1.0)

    "A gente tava conversando de boassa..."

    "O que será que deu nela? O que ela quis dizer com tudo aquilo?"

    "'O Barão manda em tudo'. Em tudo o que? O Barão é dono do Cassino, mas isso não quer dizer que ele pode mandar em TUDO."

    "Que tipo de contrato será que a [d] tem com o Barão? Ele pode mandar ela cantar naquelas condições... e proibir uma música."

    "Ela ia me contar alguma coisa, mas ela não conseguiu."

    "Mano! A gente não comeu e nem pagou a pizza!"

    if diana_e4 == "horrivel":

        "Eu saí andando e ninguém me parou e eu nem falei nada! Como assim?!"

        "Droga..."

        "Nosso encontro não deu nada certo."

        "Será que eu devia ter parado ela? O que será que ia acontecer se eu tivesse feito isso?"

        "Ficou mó climão agora. Bom... espero que as coisas melhorem."
    else:


        "A gente saiu chutado e eu não paguei nada!"

        mc "Que sorte!"

        "Mas e aquele beijo? Da onde eu tirei aquilo?"

        "Acho que esses últimos tempos tão me dando mais coragem, sei lá."

        "Até parece que um ano atrás eu ia ter coragem de fazer isso."

        if diana_e4 == "seducao":

            "E ela mandou eu continuar beijando ainda por cima. Caralho, aquilo foi quente."

            "Ela tá na minha. A [d] é posuda, mas eu sei que ela tá me curtindo."

            "E eu tô na dela também hehe... que mulherão."
        else:


            "Quando eu beijei ela... talvez se ela tivesse mais na minha ela não ia ligar."

            "Mas ficou na cara que ela não curtiu meu beijo. Talvez ela me veja só como amigo."

            "Isso não é ruim. Ser amigo dela não seria ruim, não."

        "Ter uma cantora do meu lado seria demais pra ter material pra revista. O chefe que ia ficar feliz."

        mc "Por que eu tô pensando nesse velho desgraçado? Isso não importa..."

    "A [d] é uma garota incrível. Eu quero poder ver ela de novo."

    "Eu quero ajudar ela do jeito que eu puder. E eu tenho certeza que pra ajudar ela eu vou ter que passar por cima do Barão."

    mc "Barão... eu não te conheço, mas eu tenho certeza que você é um idiota... Me espere..."

    scene black with Dissolve(3.0)

    "Eita. Eu falei igual um super herói hehe..."



    "Mas e a Diana? Como será que ela tá?"

    menu:
        "Eu queria saber...":


            pause 1.0

            scene d4_premium11 with Dissolve(1.0)

            pause

            $ na_nome = "Natasha"

            d "Me deixa, [na]..."

            if diana_e4 == "seducao":

                na "Que loucura foi aquela no banheiro com aquele homem?"

                d "Não sei... nem me pergunte... alguma coisa me deixou com vontade de dar."

                na "Você falando desse jeito..."

                d "Fazia tempo que eu não me sentia viva daquele jeito."

            na "Eu não sei o que deu na sua cabeça, mas foi perigoso demais sair do Cassino pra se encontrar com ele."

            d "Eu tinha você pra me cobrir..."

            na "Eu não posso te cobrir. Você entende que a gente tá do lado contrário na história?"

            d "..."

            d "Eu sei... me desculpa. Eu não queria abusar do carinho que você tem por mim."

            na "Não precisa pedir desculpas também... eu só quero que você tome cuidado."

            d "Por que você precisa trabalhar pra eles, Natasha?"

            na "Existem poucas formas de se dar bem na capital. Nem todo mundo tem seu talento pra música."

            na "Eles são a porta pra eu me tornar alguém um dia. Mas não é fácil entrar pro grupo. Você precisa se provar."

            d "E te colocaram pra me olhar?"

            na "Não adianta tentar mudar o rumo da conversa, senhorita. O problema esta noite é você."

            d "Você tá certa... pra variar..."

            na "..."

            scene d4_premium12 with Dissolve(1.0)

            na "Mudando de assunto... Então você vai ficar com ele?"

            d "Quem sabe..."

            na "Ainda não é oficial?"

            d "Não. Ainda não tem nada certo."

            na "Bom saber."

            d "Haha... mas na próxima..."

            na "A coisa tá indo rápido desse jeito?"

            d "Não sei o que ele tem... mas é contagiante... eu falo as coisas pra ele, e tudo fica melhor depois."

            d "Além de que ele sabe falar muito bem na hora certa."

            d "É fácil ver ele como um idiota sem graça, mas passe um tempo com ele e você vai entender."

            na "Falando desse jeito... talvez eu acabe me interessando também."

            d "Se ele te escolher, não vejo nenhum problema. Eu não vou brigar por causa de homem."

            na "E eu nunca brigaria com você por causa de qualquer um."

            d "A é?"

            na "É..."

            scene d4_premium13 with Dissolve(1.0)

            pause

            na "Se logo vão colocar um anel no seu dedo, acho bom eu não perder tempo."

            d "Você nunca perdeu tempo, desde o começo..."

            na "Mas eu quero aproveitar mais um pouco antes do fim."

            d "É por isso que você pegou esse trabalho de babá? Pra ficar mais perto?"

            na "E se for? E se eu não gostar de ser babá de um italiano boa pinta o dia inteiro e quiser outro tipo de bebê?"

            d "Não sei..."

            na "A gente tá chegando. Posso subir com você?"

            d "Pra me acompanhar até a porta?"

            label diana4_premium2:

                pass

            na "Claro..."

            menu:
                "Vem. Eu quero companhia.":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_55

                        jump diana4_premium2

                    d "Vai ser bom ter companhia. Sobe pro meu quarto."

                    na "Eu gosto quando você aceita minhas propostas."

                    d "As coisas pararam na metade esta noite... e você sabe ser bem convincente..."

                    na "Essa frustração não faz bem. Eu vou te ajudar com isso."

                    d "..."

                    scene black with Dissolve(1.0)

                    scene quarto_paris geral with Dissolve(1.0)

                    pause 1.0

                    d "De volta à gaiola."

                    na "Uma gaiola linda e bem chique."

                    scene black with dissolve

                    scene d4_premium14 with Dissolve(1.0)

                    pause

                    d "Não vou disctutir com você hoje. Eu tô me sentindo muito bem."

                    na "Esse vestido caiu bem em você."

                    d "É um daqueles que só ele pode comprar."

                    na "Alguns milhares?"

                    d "Muitos milhares. Você sabe que ele não economiza nessas coisas."

                    na "Dá pra ver... ele tá perfeito no seu corpo. Mostrando exatamente o que eu quero ver."

                    d "Tenho certeza que ele ficaria perfeito em você também."

                    d "Ah! Melhor ainda! Fica com ele."

                    na "Sério?"

                    d "Eu sei que a prefeitura não paga muito... e se você gostou tanto. Ele vai me dar outro logo mesmo."

                    na "Mesmo que a prefeitura pagasse um monte, seria impossível comprar um vestido desse."

                    d "Tá vendo? Mais uma razão pra você aceitar."

                    na "Então tá... posso pegar ele mesmo?"

                    d "Claro. Eu tô te dando."

                    na "Então vou pegar."

                    scene black with dissolve

                    d "Hm?"

                    scene d4_premium15 with Dissolve(1.0)

                    pause

                    d "O que você tá fazendo?"

                    na "Pegando meu vestido."

                    d "Que absurdo... não dá pra esperar eu tirar, não?"

                    na "Eu pego o que é meu. Não perco tempo."

                    d "A gente ainda tá falando do vestido?"

                    na "Do que você quer falar?"

                    d "Não sei, Natasha... hoje o dia realmente... mas, não sei..."

                    na "Não é possível que você ficou satisfeita com aquilo. Você sabe que eu faço muito melhor."

                    d "Isso não é uma competição."

                    na "Eu não vou me desculpar por querer fazer você se sentir bem melhor que os outros."

                    na "Se você não deixar eu puxar o vestido com as mãos, eu vou ter que usar a boca."

                    d "Boca?"

                    scene d4_premium16 with Dissolve(1.0)

                    pause

                    d "A-ah..."

                    na "Será que assim eu consigo?"

                    d "N-natasha... n-não..."

                    na "Pode falar 'não' o quanto quiser, nós duas sabemos que seu corpo quer."

                    d "Você abusa do meu jeito..."

                    na "Não vou mentir... seu jeito meigo e carinhoso é uma porta de entrada."

                    d "Mas eu..."

                    "Eu vou me entregar pra ela desse jeito?"

                    menu:
                        "Pode tirar o vestido.":


                            d "Por que eu não consigo dizer 'não' pra você?"

                            na "Porque você gosta."

                            d "Tira logo seu vestido."

                            na "Aleluia."

                            scene black with dissolve

                            scene d4_premium17 with Dissolve(1.0)

                            pause

                            na "Ele fica perfeito em você, mas seu corpo nu é ainda melhor."

                            d "Pode parar com essa fala mansa, eu vou ser sua hoje."

                            na "Parece que alguém tá começando a esquentar."

                            d "Você sabe como eu gosto."
                            scene dnew_ani17 with Dissolve(1.0)
                            na "Gentil, mas com força."

                            d "Ah... você me conhece tão bem..."

                            na "Mais do que você imagina."

                            d "Mnnhh..."

                            na "Agora vira aqui. Deixa eu sentir sua boca."

                            d "Sim. Eu também quero sentir a sua."

                            scene black with dissolve

                            scene d4_premium18 with Dissolve(1.0)

                            pause

                            d "Nnnghh..."

                            na "Ah..."

                            d "Por que tanta força?"

                            na "Porque você me deixa louca. Por isso."

                            d "Ahhn..."

                            d "E só eu vou ficar pelada?"

                            na "Claro que não."

                            d "Eu quero sentir sua pele roçando em mim."

                            na "Assim você me deixa mais louca!"

                            d "E eu não sei?"

                            na "Parece que alguém aqui me conhece também."

                            d "Se você vai demorar, deixa eu tirar pra você."

                            scene d4_premium19 with Dissolve(1.0)

                            pause

                            d "Agora sim, seu peito apertando o meu desse jeito."

                            na "Você é uma delícia, Diana."

                            d "Aaahn!"

                            na "Seu gemido é uma delícia também."

                            d "Ah... eu tô tremendo, Natasha."

                            na "E isso é só o começo. Hoje eu vou quebrar sua cama."

                            d "A gente não pode. E se ele descobrir?"

                            na "Você sabe que ele não liga pra mim. Parece que nunca passou pela cabeça dele que você curte mulheres."

                            d "Eu curto você. É diferente."

                            na "Ah... você também tem uma fala mansa que... qualquer um cairia por você."

                            d "Talvez... cantar também é seduzir..."

                            na "Depois dessa você merece um presente. Senta na cama."

                            d "Natasha... eu falei sério sobre ele. Acho que a gente devia parar."

                            na "Nem pense nisso. Senta na cama."

                            menu:
                                "Sentar na cama":


                                    scene black with dissolve

                                    scene d4_premium20 with Dissolve(1.0)

                                    pause

                                    d "Ah!"

                                    na "Foi aqui que ele te lambeu, é?!"

                                    d "P-para de graça... nnnghhh..."

                                    na "Eu não ligo. Eu tô aqui pra sentir prazer."

                                    d "Você é uma idiota... hmmm... falando assim... enquanto me chupa..."

                                    na "Tá ficando excitada, né? Eu vejo só pelo jeito que você fala."

                                    d "Claro! Com essa língua me lambuzando, sua gostosa!"

                                    na "Eu tô só começando, Diana."

                                    window hide

                                    pause

                                    scene d4_premium21 with Dissolve(1.0)

                                    pause

                                    d "Ahn! AAhnn!"

                                    na "Eu adoro sentir você."

                                    d "Então sente! Eu tô gostando, [na]!"

                                    na "Hmm!"

                                    d "Assim! HNNG!"

                                    na "Vai gozar?!"

                                    d "Mais um pouco! Vai!"

                                    na "Mhmmm!"

                                    d "Assim! VAII!"

                                    na "..."

                                    d "Por que parou?!"

                                    na "Aguenta um pouco... é uma técnica."

                                    d "Técnica?"

                                    na "Confia em mim que você vai ter a maior gozada da sua vida."

                                    na "Mas agora é minha vez. Se ajeita na cama."

                                    d "Ah... ok..."

                                    scene black with dissolve

                                    scene d4_premium22 with Dissolve(1.0)

                                    pause

                                    d "Hnng!"

                                    na "Isso! Enfia a boca em mim!"

                                    d "Hmmm!"

                                    na "Você é tão carinhosa, Diana. Vai com força!"

                                    d "NNNGH!"

                                    na "Melhorou, mas faz mais! Você é uma flor, eu quero a Diana nervosa agora."

                                    na "Ah... ahnnn... que delícia..."

                                    na "Vem mais pra cá. É nesse ponto aqui."

                                    d "T-tchá."

                                    scene d4_premium23 with Dissolve(1.0)

                                    pause

                                    na "Aí! Agora sim, Diana!"

                                    d "Nnngnghhh..."

                                    na "Eu tô quase lá! Não para! Vai!"

                                    d "Nghhh!"

                                    na "Isso! Tá muito gostoso! Vai! Forte!"

                                    d "Ahnnng!"

                                    na "Isso! Ah! Aahhnn! Asssimmm!"

                                    d "Ahnn... aah..."

                                    na "Como é que é? Você tá se masturbando enquanto me lambe? Que absurdo!"

                                    d "Aahnn..."

                                    na "Tudo bem. Eu vou te ajudar. Vou apalpar aqui bem forte."

                                    d "?!"

                                    scene d4_premium24 with vpunch

                                    pause

                                    d "NNGH!"

                                    na "Isso, querida! Continua enfiando essa boca em mim!"

                                    d "AAhhnn..."

                                    na "E pode se tocar. Só não vale gozar ainda."

                                    d "Eu quero gozar, Na!"

                                    na "Ainda não... eu tô quase lá também... mas vamos gozar juntas."

                                    d "Vai logo, por favor... não aguento mais."

                                    na "Tá bom. Tá bom. Eu não aguento mais esperar também."

                                    na "Pula pra lá. Eu vou por cima."

                                    d "Vem logo."

                                    scene black with dissolve

                                    scene d4_premium25 with Dissolve(1.0)

                                    pause

                                    na "Ah!Eu adoro terminar assim!"

                                    d "Parece que a gente tá transando de verdade! AHN!"

                                    na "Se isso não é transar, meu amor, não sei o que é!"

                                    d "Então vai! Esfrega em mim!"

                                    na "Esfrego! Sente minha buceta na sua!"

                                    d "Eu tô tão molhada, Natasha!"

                                    na "Ai! Eu também! Anngh!"

                                    d "Não para agora! Acelera!"

                                    na "Tá!"

                                    scene d4_premium26 with vpunch

                                    pause

                                    d "Assim! Desse jeito!"

                                    na "Tá vindo, Diana! Eu vou gozar!"

                                    d "Eu também! Goza comigo!"

                                    na "Isso! Tô sentindo!"

                                    d "AANNH! AANNN!"

                                    na "AAAGH! AAAAHH!"

                                    scene d4_premium27 with vpunch

                                    pause

                                    d "Aaiiiin!"

                                    na "AAAHHH!"

                                    scene d4_premium27 with vpunch

                                    d "De novo!"

                                    d "AAhhhh!"

                                    scene d4_premium27 with vpunch

                                    d "M-mais uma! AAANNNGH!"

                                    na "Aaahhhh... ah..."

                                    d "Minha nossa... ahnnn..."

                                    na "Eu disse que ia ser o melhor orgasmo da sua vida."

                                    d "Segurar assim... foi incrível mesmo..."

                                    na "Se os homens soubessem dar prazer pras mulheres..."

                                    d "... o mundo seria muito melhor..."

                                    scene black with Dissolve(1.0)

                                    pause 1.0

                                    scene d4_premium28 with Dissolve(1.0)

                                    pause

                                    d "Foi demais..."

                                    na "Eu disse que você não ia se arrepender."

                                    d "Falou mesmo..."

                                    d "Se você é... tão boa na cama... por que você quer alguém inexperiente como eu?"

                                    na "Hmm..."

                                    na "Sendo sincera, eu não sei. Talvez por causa disso mesmo?"

                                    d "Não acredito... provavelmente você poderia ter a mulher ou o homem que você quisesse."

                                    d "Porque além de boa no sexo, você é linda, charmosa e tem um ar misterioso que qualquer um gostaria de resolver."

                                    na "Você tá exagerando. Mas, sim... eu tenho certa facilidade pra subir na cama dos outros."

                                    d "Eu sinto que... seu mistério ainda tá muito longe de acabar."

                                    na "Eu sou só a secretária de um prefeito tentando entrar para um grupo de criminosos e resolver minha vida."

                                    d "Haha... só? Você quer mais?"

                                    na "Falando assim parece grande mesmo, mas o dia é bem monótono."

                                    d "Agora... deixa eu te perguntar uma coisa..."

                                    na "Fala, linda."

                                    scene d4_premium29 with Dissolve(1.0)

                                    pause

                                    d "Depois que você fizer tudo o que tem que fazer... e eu me livrar das minhas amarras..."

                                    d "O que você acha da gente... assumir isso aqui."

                                    na "Tá brincando? Você não tá se engraçando com aquele rapaz?"

                                    d "Sim, o [mc] é muito especial, mas hoje eu ainda preferiria ficar com você."

                                    na "Você tá assim porque eu dei um bom trato em você."

                                    d "Não seja estúpida. Eu falo sério, Natasha."

                                    na "Mesmo que não fosse o sexo... você sabe que eu não tenho interesse em nada sério. Eu fui bem clara desde o começo."

                                    d "Você não mudou de ideia depois de hoje?"

                                    na "Não. Eu tô aqui por causa do sexo e é isso."

                                    d "Você é impossível."

                                    d "Bom... eu sinto que tá muito perto de alguma coisa acontecer com o [mc]. A cada novo contato, mais eu me apaixono. Essa pode ser sua última chance."

                                    na "Passo. Espero que vocês sejam felizes."

                                    d "Você é você mesmo... sem tirar nem por."

                                    na "E eu sei que você gosta."

                                    d "Hmm..."

                                    na "Agora eu vou me arrumar. E tomar cuidado com o Barão."

                                    d "A gente se vê a noite?"
                                "Parar por aqui":


                                    d "Ah... eu sei o quanto você é persuasiva... ainda mais com esses beijos..."

                                    na "É disso que eu tô falando... deixa tudo comigo."

                                    d "Mas eu quero parar aqui. É perigoso demais."

                                    na "Não. Por favor."

                                    d "Com licença. É sério."

                                    na "Tá... eu conheço sua voz..."

                                    scene black with Dissolve(1.0)

                                    scene quarto_paris geral with Dissolve(1.0)

                                    na "É por causa dele?"

                                    d "É."

                                    na "E se eu fosse sua alma gêmea? Você vai me perder?"

                                    d "A gente poderia ficar juntas... mas eu sei que você não quer nada sério."

                                    na "Tem razão. Você sabe que é só sexo casual."

                                    d "Infelizmente..."

                                    na "É... mas é bom assim também, não é?"

                                    na "Acho que é melhor eu ir nessa então."

                                    d "Eu também acho. Você sabe onde me encontrar."
                        "Eu não quero hoje.":


                            d "Eu sei o quanto você é persuasiva... ainda mais com esses beijos..."

                            na "É disso que eu tô falando... deixa tudo comigo."

                            d "Mas eu não quero nada com você hoje."

                            na "Ouch... assim mesmo?"

                            d "Com licença. É sério."

                            na "Tá... eu conheço sua voz..."

                            scene black with dissolve

                            scene d4_premium15 with Dissolve(1.0)

                            na "É por causa dele?"

                            d "É. Eu sinto que é um caminho sem volta agora."

                            na "E por que não pode ser eu?"

                            d "Poderia... mas eu sei que você não quer nada sério."

                            na "Tem razão. Vou perder meu sexo casual..."

                            d "Linda e charmosa desse jeito, logo logo você encontra outro."

                            na "É..."

                            scene black with Dissolve(1.0)

                            scene quarto_paris geral with Dissolve(1.0)

                            na "Acho que é melhor eu ir nessa então."

                            d "Eu também acho. Mas você sabe onde me encontrar."
                "Hoje não. Tô cansada.":


                    d "Na próxima, tá? Eu tive emoção demais pra um dia."

                    na "Certeza? Eu posso te fazer uma massagem."

                    d "Eu sei muito bem das suas massagens... elas são incríveis, mas eu termino mais cansada."

                    na "Certeza que você vai perder? Eu prometo que vai ser uma delícia."

                    d "Você é bem convincente, mas hoje, não."

            na "Tudo bem. Te vejo em breve, se tudo der certo."

            d "Tá. Até uma noite dessas."
        "Deixa pra lá":


            "Ela deve tá legal."

    scene black with Dissolve(1.0)

    pause 1.0



    $ tempo = 4

    $ v26_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v26_fim","final","local")

    jump call_cidade

label diana_evento3:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d3_save", extra_info="d3_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "Aqui é onde eu vi a apresentação da [d] na outra vez."

    if diana_e2 == "seducao":

        "Aquele dia as coisas entre a gente esquentaram rápido."

        "A gente tava conversando e logo depois a gente já foi pra um beijo..."

        mc safado "Foi incrível..."
    else:


        "Eu e a [d] trocamos uma ideia. Ela com certeza é uma mulher diferenciada."

        "Muito talentosa, requintada..."

        "Infelizmente não consegui nada mais quente com ela. Se eu quiser ir pra esse caminho com ela, tenho que fazer meu movimento da próxima vez."

    "Tá na cara que a [d] é uma mulher que sabe o que quer."

    stop music fadeout 2.0

    "Ela tem seus objetivos com a música e não tá satisfeita só com os shows aqui no cassino. Acho que ela quer conquistar o país, até o mundo se pá."

    "Pensando bem... aquela música que ela cantou pra mim..."

    "Eu lembro que terminava com alguma coisa tipo 'a escrava da ilha'."

    "Tava meio disfarçada, mais tinha alguma coisa ali. Não sei explicar..."

    "A forma que ela cantou. Aquela emoção toda. Parece até que ela tava falando d-"

    "???" "[mc]?"

    mc desconfiado "Âh?"

    mc surpreso "[d]!"

    d "Xiu. Vem comigo."

    mc envergonhado "Tá"

    scene black with Dissolve(1.0)

    "..."

    scene jazz_bar angulo2 with Dissolve(2.0)

    d "Não tem ninguém aqui."

    show diana ola with dissolve

    d "Boa noite, [mc]. Tudo bem?"

    mc charmoso "Boa noite."

    menu:
        "Tudo bem. E você?":


            mc normal "Tudo legal. E você? Como tá?"

            d "Levando. Mais apresentações do que eu gostaria aqui no cassino."

            mc preocupado "Sério? Tão forçando a barra?"

            d "Não precisa fazer essa cara. Sempre foi assim por aqui."

            mc desculpa "Entendo..."

        "Ainda tô pensando no nosso beijo." if diana_e2 == "seducao":

            mc charmoso "Ainda tô pensando no nosso beijo. E você?"

            show diana exibida with dissolve

            d "..."

            d "Foi só um beijo, [mc]. Você tem o que... 15 anos?"

            mc envergonhado "Ei..."

            d "Não deixa de ser um pouco fofo, mas você quer ser um homem charmoso e não fofo, certo?"

            mc "Não sei como responder essa pergunta. Não posso ser os dois?"

            d "Tá querendo demais..."
        "Você fica incrível com esse vestido.":


            $ diana_seducao += 1

            mc charmoso "Uou. Esse vestido... você fica demais nele."

            show diana provocando with dissolve

            d "Você lembrou? Foi o que eu usei na outra noite."

            mc "Certas coisas não dá pra gente esquecer, [d]."

            d "Cuidado pra não exagerar no tom..."

            mc "Só falo a verdade."

    show diana ola with dissolve

    d "Que curioso ver você aqui."

    mc desconfiado "Por que?"

    d "Não imaginei que você fosse de jogar dinheiro fora em cassino."

    if cassino_roupa == "normal":

        d "Bom... a sorte não parece estar do seu lado ultimamente..."

        mc zerado "Tá falando da minha roupa, né?"

        d "Não disse nada..."

        mc "..."

    elif cassino_roupa == "blazer":

        $ diana_seducao += 1

        d "Inclusive dá pra ver que você tá entrando no clima mesmo. Tá até vestido à caráter."

        mc "Este é um dos únicos lugares que dá pra gente se vestir melhor."

        d "Não discordo."

    elif cassino_roupa == "blacktie":

        $ diana_seducao += 2

        d "E vestido assim... deve estar aproveitando mesmo a casa do Barão."

        mc "Não é nada."

        d "Nada? Isso é costura fina. Um Black Tie desses não se vê todos os dias. Nem aqui no cassino."

    mc normal "Todo mundo tem o direito a se divertir de vez em quando. Eu também mereço."

    d "Se você acha perder dinheiro divertido..."

    mc desconfiado "Você tá sendo até bem crítica pra quem ganha a vida às custas do cassino."

    show diana exibida with dissolve

    d "..."

    "O que foi? Será que eu disse algo errado?"

    d "Nem sempre a gente avalia a situação com todas as informações. Nosso conhecimento limitado faz a gente conjecturar de forma leviana."

    mc desconfiado "Como é?"

    d "Eu não devo nada ao Barão. Ele, sim, me deve por contar comigo nesse muquifo que ele acha que é cinco estrelas."

    menu:
        "Com certeza. Você merece mais que isso.":


            $ diana_seducao += 1

            mc charmoso "Concordo. Você tem talento pra sair deste lugar e conquistar muito mais."

            show diana ola with dissolve

            d "Eu tenho certeza. Mas obrigada por pontuar isso."
        "Você parece bem crítica quanto ao cassino.":


            mc desconfiado "Você tá sendo bem crítica com relação ao cassino. Você não curte trabalhar aqui?"

            d "Trabalhar?"

            d "O Barão não merece nada. Eu não devo nada a ele. Não vou falar bem deste lugar só porque estou aqui."

            d "Acho inescrupuloso o que eles fazem com as pessoas."

            d "Abusam do vício das pessoas pra ganhar dinheiro que muitas vezes elas nem têm."

            d "Nunca concordarei com isso."

            mc desculpa "Você tem um ponto aí..."

    d "Eu pretendo sair daqui o mais rápido possível."

    d "E claro que você vai me ajudar com sua revista, [mc]. Estou contando com isso."

    mc charmoso "Eu prometi e pretendo cumprir com minha parte. Pode confiar em mim."

    d "Perfeito."

    scene jazz_bar angulo1 with Dissolve(2.0)

    show jazz_bar_diana angulo1_diana_explicando with dissolve

    d "Inclusive..."

    d "Eu vou aproveitar que você está aqui e te passar por cima o que eu planejo para o futuro."

    if cassino_roupa == "blacktie":

        show jazz_bar_mc angulo1_blacktie_normal with dissolve

    elif cassino_roupa == "blazer":

        show jazz_bar_mc angulo1_blazer_normal with dissolve

    elif cassino_roupa == "normal":

        show jazz_bar_mc angulo1_normal_normal with dissolve

    mc "Certo. O que você pretende?"

    d "Eu te disse que eu não quero continuar cantando no cassino lá na praia, lembra?"

    mc "Sim. Pelo que eu entendi, você quer tipo almejar voos mais altos, vamos dizer assim..."

    d "Podemos dizer isso."

    d "Eu quero que isso aconteça o quanto antes."

    d "A matéria que você publicou foi um bom começo. Muitas pessoas viram a notícia e vieram me perguntar do single."

    menu:
        "Não foi nada de mais.":


            mc "Não foi nada. É só nosso acordo."

            d "Eu sei. Só queria que soubesse que ele está sendo benéfico para mim."

            mc "E pra mim também. Eu só tive acesso ao cassino graças a você. Além de ganhar uns pontos na revista."

            d "É bom para nossa parceria que os benefícios sejam mútuos."
        "Tudo pra ajudar você.":


            mc "Fico feliz de ajudar você. Quero que você conquiste o que quer."

            d "Obrigada..."

            d "Espero que você também esteja tirando proveito do nosso acordo."

            mc "Com certeza. Eu só tive acesso ao cassino graças a você. Além de ganhar uns pontos na revista."

            d "Que bom."
        "Você merece. É muito talentosa.":


            $ diana_seducao += 1

            mc "Pra falar a verdade, depois de ouvir você cantar, eu acho que eu fiz a escolha natural ao aceitar nosso acordo."

            mc "Você é super talentosa e acredito que merece sair daqui."

            show jazz_bar_diana angulo1_diana_excitada with dissolve

            d "[mc]..."

            d "Você sabe exatamente o que falar às vezes."

            mc "Só às vezes?"

            d "Só..."

    mc "Mas... agora que a matéria começou a dar resultado. O que você pretende fazer?"

    show jazz_bar_diana angulo1_diana_seduzida with dissolve

    d "Agora vou preparar tudo para o lançamento do single."

    d "Falta pouco para o show de lançamento. Preciso ter certeza que as maiores autoridades da música estejam aqui."

    d "Esse show tem que ser incrível, [mc]. Todos precisam estar aqui."

    mc "Entendi."

    d "Não. Não é tão simples. Isso é realmente muito importante pra mim."

    if cassino_roupa == "normal":

        show jazz_bar_mc angulo1_normal_encostado with dissolve

    elif cassino_roupa == "blazer":

        show jazz_bar_mc angulo1_blazer_encostado with dissolve

    elif cassino_roupa == "blacktie":

        show jazz_bar_mc angulo1_blacktie_encostado with dissolve

    "Isso parece realmente algo grande pra [d]."

    "Mas ela já é uma cantora tão conhecida na capital. Por que ela tá colocando tanta expectativa em uma única música?"

    mc "Por que essa música é tão especial?"

    d "Você lembra dela? Daquele dia que cantei pra você?"

    mc "Claro."

    d "Então é autoexplicativo."

    "Não sei se é tão fácil de entender assim igual ela acha."

    d "Não quero que você me ache uma esnobe. Mas é que não é fácil explicar, [mc]. Ainda mais com palavras."

    "A [d] realmente parece estar colocando todas as fichas nesse lançamento."

    "Se ela precisa de pessoas importantes pro show, talvez eu possa ajudar."

    mc "Eu entendo. Relaxe. E sobre o show..."

    mc "Olha... eu conheço pessoas. Meu trabalho de paparazzo faz eu ter acesso a celebridades."

    mc "Algumas são realmente minhas amigas. O que você acha de eu conversar com elas e pedir pra elas virem?"

    d "Você faria isso por mim?"

    hide jazz_bar_diana with dissolve

    if cassino_roupa == "normal":

        show jazz_bar_mc angulo1_diana_mc_normal with dissolve

    elif cassino_roupa == "blazer":

        show jazz_bar_mc angulo1_diana_mc_blazer with dissolve

    elif cassino_roupa == "blacktie":

        show jazz_bar_mc angulo1_diana_mc_blacktie with dissolve

    mc "Claro, [d]."

    mc "Eu quero te ajudar."

    d "..."

    d "Entretanto, isso não tá no nosso acordo."

    mc "Eu sei. Foda-se o acordo. Não quero fazer isso por causa de acordo."

    d "Então por que? Por que você vai fazer isso por alguém que você mal conhece?"

    menu:
        "Preciso de um motivo? Só quero que você tenha sucesso.":


            mc "Haha. Não precisa ficar desconfiada. Desde quando a gente precisa de um motivo pra isso?"

            d "..."

            mc "Eu só quero que você se dê bem. Tenha sucesso no que tá propondo pra sua vida."

            d "..."

            mc "É sério!"

            d "..."

            d "Sabe, [mc]... você é meio estranho."

            mc "Você também dizendo isso?"

            d "Você escuta muito isso?"

            mc "Mais do que eu gostaria..."

            d "Talvez seja verdade então. Já parou pra pensar?"

            mc "Prefiro achar que estão todos só querendo me zoar por algum motivo desconhecido."
        "Talvez eu só queira te conquistar...":


            $ diana_seducao += 2

            mc "Não sei... quem sabe eu só queira ganhar alguns pontos com você..."

            d "Então é isso?"

            mc "Talvez..."

            d "Você tem algo de diferente. Uma energia que eu sinto quando eu olho nos seus olhos."

            d "Não sei se é seu cheiro, ou a sua voz."

            d "Tem alguma coisa em você que me faz querer prestar atenção em você. Como se estivesse me atraindo."

            d "Parece loucura falando assim... mas é como se eu ouvisse uma voz me chamando de dentro de uma caverna."

            d "Uma vontade de me aproximar e descobrir o que tem lá dentro."

            mc "[d]..."

    if diana_e2 != "horrivel":

        d "Lembra o que eu disse da outra vez?"

        scene jazz_bar angulo2 with Dissolve(1.0)

        mc "Opa."

        if cassino_roupa == "normal":

            show jazz_bar_mc angulo2_diana_mc_normal_juntos with dissolve

        elif cassino_roupa == "blazer":

            show jazz_bar_mc angulo2_diana_mc_blazer_juntos with dissolve

        elif cassino_roupa == "blacktie":

            show jazz_bar_mc angulo2_diana_mc_blacktie_juntos with dissolve

        mc "E-eu..."

        d "Eu disse que você vai acabar se dando mal se continuar carregando todo mundo nas costas."

        mc "Você... falou alguma coisa assim mesmo..."

        if diana_e2 == "seducao":

            d "Aquela noite eu falei outra coisa também."

            mc "O que?"

            d "Me beija."

            mc "E-eu..."

            menu:
                "Beijar ela":


                    $ diana_seducao += 2
                    $ diana3_beijo = True

                    if cassino_roupa == "normal":

                        show jazz_bar_mc angulo2_beijo_normal with dissolve

                    elif cassino_roupa == "blazer":

                        show jazz_bar_mc angulo2_beijo_blazer with dissolve

                    elif cassino_roupa == "blacktie":

                        show jazz_bar_mc angulo2_beijo_blacktie with dissolve

                    pause

                    d "Atitude. Eu gosto disso."

                    window hide

                    pause

                    if cassino_roupa == "normal":

                        show jazz_bar_mc angulo2_diana_mc_normal_juntos with dissolve

                    elif cassino_roupa == "blazer":

                        show jazz_bar_mc angulo2_diana_mc_blazer_juntos with dissolve

                    elif cassino_roupa == "blacktie":

                        show jazz_bar_mc angulo2_diana_mc_blacktie_juntos with dissolve

                    mc "Já é a segunda vez que a gente se beija aqui."

                    d "Já cansou?"

                    mc "Claro que não..."

                    d "Mas você está certo em uma coisa. O que acha da gente variar um pouco?"

                    mc "Como assim?"

                    d "Quer continuar lá em cima, no meu quarto?"

                    mc "Si-sim."

                    d "Perfeito."

                    hide jazz_bar_mc with dissolve

                    d "Vem comigo."

                    mc charmoso "Claro."

                    jump diana_e3_subir
                "Não beijar":


                    mc "Não agora. A gente já se beijou aqui."

                    mc "E se a gente for... sei lá... pro seu quarto?"

                    d "Sério mesmo, mocinho?"

                    mc "Eu tô acelerando as coisas?"

                    d "Você que tem cabeça de 15 anos, não eu."

                    d "Não tenho nada contra."

                    hide jazz_bar_mc with dissolve

                    d "Pode vir comigo."
        else:


            d "É bom que você lembre. Eu não falo isso brincando."

            d "O fato de você querer me ajudar só por ajudar. E todas as outras pessoas na sua vida."

            d "Eu tenho certeza que elas já trouxeram riscos pra você. Estou certa?"

            "Parece que ela tá lendo minha mente..."

            d "Não precisa responder. Eu sei que eu estou certa."

            d "Eu não me importo de ser sua amiga, [mc]. Você é um cara legal, mas tome cuidado para não exagerar."

            mc "O-ok."

            d "Talvez seja isso que me atrai. Hoje as pessoas são tão egoístas, egocêntricas. Cada um só pensa em si mesmo."

            d "E quando eu olho pra você, parece que você realmente se importa comigo. Mesmo a gente se conhecendo tão pouco."

            d "Essa é uma característica linda. E você devia ter orgulho dela."

            mc "Obrigado..."

    d "Olha... eu tenho uma proposta. O que acha de você subir até meu quarto?"

    mc "Quêê?!"

    d "Assim a gente pode conversar e se conhecer melhor. O que me diz?"

    "Ir pro quarto com ela?!"

    "Isso é quase um convite pra... Será que eu aceito?"

    menu:
        "Tudo bem.":


            mc "Tudo bem. Vai ser legal ter sua companhia hoje."

            d "Digo o mesmo."
        "Sozinho com você no quarto? Com certeza.":


            $ diana_seducao += 2

            mc "Uma noite sozinho com você no quarto? Impossível negar."

            d "Mesmo faltando classe, um comentário desses vai deixar qualquer mulher lisongeada."
        "Infelizmente hoje não vou poder.":


            $ diana_e3 = "horrivel"

            mc "Pra mim hoje não vai dar. Desculpa."

            d "Não tem o que se desculpar."

            d "Então eu conto com sua ajuda."

            mc "Pode deixar. Eu vou conversar com quem eu conheço."

            d "Obrigada de novo, [mc]."

            mc "Não tem o que agradecer."

            d "Boa noite."

            mc "Boa noite."

            scene jazz geral with Dissolve(1.0)

            "Esse negócio de ir pro quarto é perigoso demais."

            "Não quero levar as coisas pra esse lado com a [d]. E não quero que ela fique tendo impressões erradas."

            "Eu vou ajudar ela, mas é isso."

            jump diana_e3_final

    label diana_e3_subir:

        d "Então vamos subir."

    hide jazz_bar_mc with dissolve

    d "Pode vir comigo."

    mc charmoso "Claro."

    scene black with Dissolve(1.0)

    "..."

    scene cassino_ponte3 with Dissolve(1.0)

    d "Nosso elevador é aqui subindo este lance de escadas."

    mc normal "Eu acho este hall incrível."

    d "Se tem uma coisa que o Barão sabe fazer é impressionar."

    mc envergonhado "..."

    scene black with Dissolve(1.0)

    "..."

    d "Aqui estamos."

    scene quarto_paris geral with Dissolve(2.0)

    pause

    mc surpreso "!"

    d "Gostou?"

    mc normal "Muito. Parece o quarto de um filme..."

    d "..."

    d "Vou deixar você só um segundo, ok?"

    mc "Claro. Sinta-se em casa."

    d "..."

    mc zerado "Parece que ela não gostou da minha piadinha."

    "Agora que eu tô aqui tá meio que me dando um nervoso."

    "Só nós dois aqui. Claro que vai rolar alguma coisa entre a gente."

    "Não! Não posso achar que o jogo tá ganho ainda. Tudo vai depender do meu desempenho."

    if diana_e2 == "seducao":

        "Eu fui muito bem beijando ela, mas agora é outra história."

        "Tenho que manter o clima rolando e garantir que ela tá na minha."
    else:


        "Eu não consegui avançar tanto com ela na parte de sedução ainda."

        "Se eu realmente quero uma chance com essa mulher incrível, eu preciso melhorar meu jogo."

    "Seja como for, sozinho com ela aqui no quarto, é a hora perfeita pra rolar alguma coisa entre a gente."

    "Se eu deixar essa chance escapar, talvez seja adeus pra sempre."

    "..."

    d "Pronto."

    mc charmoso "Opa."

    scene quarto_partis visao1 with Dissolve(2.0)

    mc surpreso "!"

    show diana r_ola with dissolve

    d "O que foi, [mc]?"

    menu:
        "Você não tá à vontade demais?":


            $ diana_seducao += 1

            mc charmoso "Você não tá muito à vontade pra quem tá com visita?"

            show diana r_interessada with dissolve

            d "Algum problema?"

            mc "Não. Por mim, claro que não."

            d "Eu achei que após me ver com o mesmo vestido duas vezes, você ia querer me ver usando outra coisa."

            mc charmoso "Está linda com certeza."

            d "Obrigada."
        "Não é nada.":


            mc envergonhado "Não é nada, não."

            show diana r_desconfiada with dissolve

            d "Se você não estiver se sentindo à vontade aqui, pode falar."

            mc normal "Nada disso. Tá tudo ok."

            d "Que bom."

    show diana r_ola with dissolve

    d "Eu quero que você relaxe. Somos apenas companheiros curtindo a noite. E não precisa pensar demais. Não tem nada rolando aqui."

    "Nada? Por que ela tá falando isso? Será que eu já ferrei tudo?"

    d "Deixa eu começar com uma pergunta."

    d "Desde quando você mora aqui na ilha?"

    mc normal "Não muito. Eu fiz faculdade aqui na capital e depois de terminar o curso eu tava pronto pra voltar pra casa dos meus pais."

    mc "Só que minha mãe arranjou um emprego pra mim na revista."

    mc "Os primeiros meses foram terríveis, mas de uma hora pra outra tudo mudou."

    show diana r_desconfiada with dissolve

    d "De uma hora pra outra? O que aconteceu?"

    mc normal "Na verdade foi tudo graças à [cc]. Ela foi a primeira celebridade que eu consegui qualquer informação."

    show diana r_interessada with dissolve

    d "Hmm... parece uma história interessante. Quer me contar?"

    menu:
        "Pode ser. Se você realmente tá interessada.":


            mc envergonhado "Você realmente quer ouvir isso?"

            d "Sim. Você sabe que a [cc] é uma das principais celebridades do ano, não sabe?"

            mc "Engraçado... falando assim é até um pouco intimidador."

            jump diana_e3_historia
        "Agora é sua vez de falar algo de você. Depois eu conto.":


            mc charmoso "Você já perguntou. Agora é sua vez de contar algo. Depois eu conto minha história."

            show diana r_meudeus with dissolve

            d "Ok. O que você quer saber?"

            mc concentrando "Hmm..."

            mc normal "A mesma pergunta que você me fez. Como você veio parar aqui na ilha?"

            d "Sério?"

            d "Não é uma história tão interessante quanto a sua."

            mc normal "Haha. Certeza que é muito melhor."

            show diana r_desconfiada with dissolve

            d "..."

            mc charmoso "Ficou com vergonha?"

            d "Não é isso..."

            d "Digamos que eu vim pra cá pra me tornar famosa. Eu cheguei com um contrato assinado com o Barão para trabalhar no cassino."

            d "Estou aqui desde então."

            mc desconfiado "Faz pouco tempo isso?"

            d "Eu respondi minha pergunta. Agora quero saber do seu rolo com a [cc]."

            mc envergonhado "Justo."

    label diana_e3_historia:

        mc normal "Bom... tudo começou lá na redação."

        mc "Eu escutei ela brigando com o chefe."

        if orelha_porta:

            mc envergonhado "Eu acabei não aguentando e xeretei a conversa."

            mc "Quando ela terminou de gritar ela abriu a porta com tudo e a gente trombou."

        mc "Ela disse alguma coisa assim... 'um paparazzo como você eu até ia gostar que me seguisse'. Não lembro exatamente."

        mc envergonhado "Por conta disso o chefe me deu mais alguns dias pra conseguir algo sobre ela."

        mc desculpa "Eu fiquei mega nervoso. Precisava de alguma coisa que desse pra publicar."

        show diana r_interessada with dissolve

        mc desconfiado "Aquele dia me deu uma dor de cabeça do cão. O que é bem raro. Acho que nem tive dor de cabeça depois daquilo."

        d "Nem figurada?"

        mc zerado "Dor de cabeça nesse sentido é o que não falta."

        d "É fácil de ver no seu rosto o quanto você sofre por conta dessas celebridades."

        mc envergonhado "Tá tão na cara assim?"

        d "Mas desculpe. Continua com a história."

        mc normal "Ah. Sim. Eu acabei indo no bar aquela noite."

        mc "Pelo incrível que pareça a [c] tava lá no bar sozinha. Eu esperei ela terminar de falar com o garçom... que é uma peça também."

        mc "A gente passou a noite conversando."

        if priscila_e1 == "seducao":

            mc envergonhado "Daí o clima foi esquentando e... aconteceu um lance louco lá."
        else:


            mc desculpa "Ela tava bem pra baixo aquela noite. Bem vulnerável mesmo. E eu acabei sendo o único amigo que ela tinha."

        mc normal "Depois disso eu-"

        show diana r_desconfiada with dissolve

        d "O que aconteceu? Não vai terminar?"

        menu:
            "Falar que você fuçou o celular da [c]":


                $ diana_seducao += 2
                $ diana3_segredo = True

                mc envergonhado "Vou. Calma."

                mc "É que ela acabou dormindo no meu colo e eu aproveitei pra... fuçar o celular dela."

                show diana r_meudeus with dissolve

                d "Não creio!"

                mc "Pois é. Não me orgulho disso, mas, né? O que eu ia fazer? Era isso ou ser despedido."

                d "Incrível. Ter essa coragem é realmente impressionante."

                show diana r_interessada with dissolve

                d "E ainda ter coragem de contar isso pra mim..."

                d "Isso é coisa de homem de verdade, [mc]."

                mc charmoso "Obrigado. Mas é que eu confio em você. E sinceramente, mesmo sendo algo questionável, era minha única alternativa."

                d "Concordo plenamente com você. Pensar demais em ética aquela hora teria acabado com sua vida na capital."

                mc "Tem razão."
            "Pular essa parte da história":


                mc envergonhado "Bom... enfim... depois desse nosso tempo juntos no bar, ela acabou me revelando sobre o filme que ia gravar."

                mc normal "E isso acabou me salvando do destino de ter que voltar pra casa dos meus pais."

        d "Realmente incrível."

    mc desculpa "Não é nada de mais..."

    show diana r_ola with dissolve

    d "Acho que você está se dando pouco crédito."

    d "Quero te falar um negócio, mas cansei de conversar de pé. Vem sentar comigo na cama."

    mc surpreso "Ca-cama..."

    d "Aqui. Vem."

    hide diana with dissolve

    mc envergonhado "Cama..."

    scene quarto_paris geral with Dissolve(1.0)

    "Eu tenho a impressão que a [d] tá dando em cima de mim."

    "Devagar... de forma muito sútil... Será que é isso mesmo?"

    d "[mc]?"

    mc surpreso "Oi!"

    d "Pode sentar aqui comigo."

    mc "Tá."

    scene diana_e3_cama1 with Dissolve(2.0)

    pause

    d "Não precisa ficar tão tenso, bobinho."

    mc envergonhado "Eu tô bem."

    d "Você não tá costumado a ir pra cama com garotas bonitas?"

    mc surpreso "I-ir pra cama?!"

    mc envergonhado "Quero dizer..."

    d "Não precisa falar nada."

    d "Aliás, você não parece tão velho. Quantos anos você tem?"

    mc envergonhado "..."

    d "Não gosta de falar a idade?"

    mc "Isso não importa."

    d "Eu tenho 23. Viu? Não dói."

    mc "Engraçadinha..."

    mc desconfiado "Nossa. Você parece mais velha."

    scene diana_e3_cama2 with Dissolve(2.0)

    pause

    d "?"

    mc surpreso "Não! Digo! Não pela aparência."

    mc charmoso "Você parece tão... sofisticada. E passa uma segurança."

    d "..."

    mc desculpa "Desculpa. Não era pra ser algo negativo..."

    d "Não se preocupe. Não é por sua causa... É que eu lembrei de uma coisa."

    menu:
        "O que você lembrou?":


            mc desculpa "O que foi que você lembrou?"

            d "..."

            d "Coisas que aconteceram no passado."

            mc "..."

            d "O que eu te disse sobre não carregar os problemas das pessoas?"

            mc "Eu sei... mas-"

            d "Eu não vou colocar esse peso em você ainda, [mc]. Eu agradeço, mas não farei isso com você. Não ainda, pelo menos."

            mc "Ok..."
        "Tem um cara na sua cama. Não é hora de pensar em outra coisa.":


            $ diana_seducao += 1

            mc desconfiado "Ei. Tem um cara aqui na sua cama. Não é hora de ficar viajando."

            d "Haha... você tem razão, [mc]."

            d "Não seria educado ficar de cara virada agora por outras coisas."

            mc charmoso "É o que eu penso."

            d "Obrigada..."

    d "..."

    mc desculpa "..."

    d "O clima ficou horrível por minha causa..."

    mc "Tudo bem."

    if diana_seducao >= 19:

        $ diana_e3 = "seducao"

        d "Só tem um jeito da gente resolver isso."

        mc desconfiado "Hm?"

        d "O que você acha da gente ter um pouco de diversão adulta?"

        mc surpreso "..."

        scene diana_e3_cama3 with Dissolve(2.0)

        pause

        d "Dois adultos... sozinhos na cama..."

        d "Não posso negar que você tem sido um verdadeiro sedutor no tempo que passamos juntos."

        d "Falando as coisas certas, na medida certa."

        d "Eu também sei seduzir..."

        window hide

        pause

        mc charmoso "Com certeza."

        if diana3_beijo:

            d "Aquele beijo no bar realmente me deixou com vontade de continuar."

        d "Deita do meu lado? Vem se divertir comigo."

        menu:
            "Com certeza.":


                mc charmoso "Com certeza."

                d "Então vem aqui."

                d "Eu vou tirar tudo pra você."

                scene black with dissolve

                scene diana3_img1 with Dissolve(1.0)

                pause

                "Eita lasqueira!"

                d "O que você acha?"

                mc "Melhor do que eu imaginava. Você é perfeita."

                d "Obrigada..."

                d "Desde nossa 'conversa' no Cassino eu queria te encontrar aqui."

                mc "Eu também não via a hora."

                d "Agora fica a pergunta... você aprendeu a ser um homem de verdade?"

                mc "Ah... se eu vou conseguir me segurar?"

                d "É."

                label diana3_premium1:

                    pass

                menu:
                    "Sim. Vou só olhar.":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_56

                            jump diana3_premium1

                        mc "Eu prometo que eu vou só olhar."

                        d "Eu duvido um pouco, mas é essa incerteza que deixa a coisa ainda mais interessante pra mim."

                        mc "Eu tô resistindo, não tô?"

                        d "Sim, mas estamos só começando, certo? Até quando você vai conseguir?"

                        mc "Pode mandar. Eu vou respeitar você. E vou colher meus frutos no final."

                        d "Hmmm... esse já não é um fruto bom o suficiente?"

                        mc "C-claro que é."

                        d "Vamos ver onde nossa brincadeira vai levar a gente. Quem sabe..."

                        d "Pode trocar de lugar na cama... por onde você quer me ver?"

                        mc "Ali embaixo..."

                        d "Claro... no meio das minhas pernas."

                        mc "Isso mesmo."

                        d "Então vai. Você que escolhe."

                        scene black with dissolve

                        scene diana3_img2 with Dissolve(1.0)

                        pause

                        d "Aí que você queria?"

                        mc "É..."

                        d "Hmhmm... então... o que você vai fazer agora?"

                        "Isso é um teste? Ou é um sinal pra eu escolher o que eu quero?"

                        "Droga... eu quero acertar. O que eu faço?"

                        menu:
                            "Ir pra cima sem encostar":


                                "Bora ver o que ela vai fazer..."

                                mc "Eu vou..."

                                scene black with dissolve

                                scene diana3_img3 with Dissolve(1.0)

                                pause

                                d "Ei!"

                                mc "Que foi? Só tô olhando."

                                d "Ah... safado."
                                scene dnew_ani04 with Dissolve(1.0)
                                mc "Você disse que eu posso ir onde eu quiser. Só não posso encostar."

                                d "Você ganhou essa. E agora?"
                            "Continuar olhando":


                                "Eu tenho que ficar de boa. Ganhar a confiança dela."

                        d "Vai ficar aí mesmo? Não vai fazer nada?"

                        mc "Eu disse que tinha aprendido minha lição."

                        d "Hmm... vamos ver..."

                        d "Se você aguentar essa próxima... eu admito que você conseguiu..."

                        mc "Você gosta do jogo da sedução? Eu posso jogar esse jogo também."

                        d "Quero ver... 3... 2... 1..."

                        scene black with dissolve

                        scene diana3_img4 with Dissolve(1.0)

                        pause

                        d "Ahn... eu tô todinha na sua frente..."

                        mc "{i}gulp{/i}"

                        d "Você não vai fazer nada?"

                        "É agora ou nunca. Ou eu ataco essa mulher agora ou ele vai escapar. Eu sei disso."

                        "Não! A Diana sabe o que ela quer. Ela tá jogando com você."
                        scene dnew_ani06 with Dissolve(1.0)
                        "Ela quer um homem de verdade, que sabe respeitar uma mulher."

                        "Claro que não! Que homem de verdade deixaria uma mulher fazer isso e ficaria só olhando!?"

                        "E agora?! O que é ser um homem de verdade?!"

                        "Aaahhhh! O que eu faço?!"

                        d "E aí? O que vai ser, [mc]?"

                        menu:
                            "Fazer sexo oral":


                                python:
                                    if renpy.android:
                                        renpy.block_rollback()

                                "Ser um homem é agir como homem não importa o que a mulher diga!"

                                mc "Vem aqui!"

                                scene diana3_img7 with vpunch

                                d "[mc]!"

                                mc "Nunca que eu vou ficar quieto numa condição dessas!"

                                d "Você prometeu que ia só olhar!"

                                mc "É culpa sua!"

                                scene black with vpunch

                                d "TOMA!"

                                "{i}TUDUMP!!!{/i}"

                                mc angustiado "AARGH!"

                                d "Idiota..."

                                scene diana3_img16 with Dissolve(1.0)

                                d "Você acha que ser um homem é voltar com sua palavra por que uma mulher te 'provocou demais'?"

                                d "Acha que pode colocar a culpa da sua infantil falta de auto controle em outra pessoa?"

                                mc "Que homem aguentaria ficar parado nessas condições, [d]? Você ia me achar um bundão!"

                                d "Bundão é não cumprir com sua palavra e ainda colocar a culpa nos outros."

                                d "Bundão é não saber respeitar o espaço dos outros."

                                d "Ser adulto é assumir responsabilidade pelos seus atos. Me fazer te dar uma bronca dessas igual sua professora é ser um bundão."
                                scene dnew_ani08 with Dissolve(1.0)
                                mc "Eu..."

                                d "Você é um homem diferente, que ainda tem um coração, mas precisa amadurecer muito se você quer ficar com uma mulher como eu."

                                mc "Eu vou pensar nisso tudo."

                                d "Isso mesmo. Pense bem antes{w=0.3}"
                            "Ficar olhando":


                                python:
                                    if renpy.android:
                                        renpy.block_rollback()

                                "Ser homem é respeitar a mulher e cumprir com a minha palavra."

                                "Mesmo que ela me ache um bundão, eu vou fazer o que eu acho que é certo."

                                mc "Eu vou fazer o que eu disse que eu ia fazer."

                                d "Hmm... não acredito... uma mulher abre as pernas assim pra você e você só olha? Você não tem bolas?"

                                mc "Por isso mesmo."

                                d "Ah... você... você é o homem de verdade. Você é o homem que eu tava esperando."

                                mc "Agora, que eu quero muito poder fazer você gozar, com certeza eu quero."

                                d "Faz eu gozar então. Ela é toda sua."

                                "Finalmente a recompensa."

                                scene black with dissolve

                                scene diana3_img5 with Dissolve(1.0)

                                pause

                                d "Ahn... você não sabe como eu queria isso."

                                mc "Devia ter deixado eu fazer isso antes."

                                d "Esperar a hora certa deixa tudo melhor... aahn!"

                                mc "Você vai ver o que tava perdendo."

                                d "Nhhgggg.... eu já to vendo."

                                scene diana3_img6 with Dissolve(1.0)

                                pause

                                d "Ah... aah..."

                                mc "Então você queria desde o começo! Eu até pensei que você tava só brincando comigo."

                                d "Esse jogo da sedução... nnnh... eu adoro... eu fico excitada de pensar que você me quer."

                                mc "Eu nunca vou entender a cabeça de vocês, celebridades."

                                d "Anng... aannnhggg!"

                                scene diana3_img9 with Dissolve(1.0)

                                pause

                                d "Tá muito bom... nnng..."

                                mc "..."

                                d "Se você continuar assim... eu vou... aaahnn..."

                                mc "Escutar você gemendo é muito bom."

                                d "É porque tá muito bom, [mc]. Nngg!"

                                mc "Se você tá chegando lá, é bom eu acelerar."

                                d "S-se você- AAANNGH!"

                                scene diana3_img7 with vpunch

                                pause

                                d "Annngh! NNNGHH!"

                                mc "Pode gozar!"

                                d "Continua! NNGH! Mais um pouco! AAANNN!"

                                d "Vai! NNGH! LAMBEEE!! NNGHH!!"

                                d "AH! AAHH!! AAAHHHH!!!"

                                scene diana3_img8 with vpunch

                                pause 1.0

                                scene diana3_img8 with vpunch

                                pause

                                d "Aaaiii... minha nossa..."

                                d "E-eu ainda tô tremendo..."

                                mc "Poxa... esse foi intenso..."

                                d "É pra isso que... serve a sedução... ufa..."
                                scene dnew_ani07 with Dissolve(1.0)
                                mc "Deixa eu me ajeitar. Não é fácil fazer uma mulher gozar assim."

                                d "Haha..."

                                scene black with Dissolve(2.0)

                                d "E quem deixou você deitar?"

                                mc "Hm?"

                                d "Vem aqui."

                                mc surpreso "D-diana?!"

                                scene diana3_img11 with Dissolve(1.0)

                                pause

                                d "Se tem alguém que merece gozar hoje é você."

                                mc "A-ah..."

                                d "Você pode ser bom com a boca... mas eu também sou."

                                "É hoje que eu tenho um infarto."

                                mc "Só de olhar pra você assim eu já fico todo duro."

                                d "Aproveita, que hoje eu existo só pra você, [mc]."

                                "A Diana é perfeita. Olha esse traseiro, essas pernas... o que eu fiz pra merecer tá com uma mulher dessas?"

                                d "Hmmm..."

                                mc "Aahn..."

                                "E ela sabe mesmo usar a boca..."

                                scene diana3_img10 with Dissolve(1.0)

                                pause

                                mc "C-com a mão também?!"

                                d "Quanto tempo você vai durar assim, hm?"

                                mc "O m-máximo que eu aguentar! Isso tá bom demais!"

                                d "Quero ver quanto... {i}slhup{/i}"

                                mc "Ah!"

                                d "Seu pau é gostoso."

                                mc "Aahnn..."

                                d "Eu quero sentir mais ele."

                                mc "Sente ele inteiro!"

                                scene diana3_img12 with Dissolve(1.0)

                                pause

                                d "{i}gulp{/i}"

                                mc "D-diana! Você vai engolir ele inteiro!"

                                d "HmHmmm!"

                                "Isso tá bom demais!"

                                "Eu tenho que..."

                                mc "Ah!"

                                window hide

                                pause

                                scene diana3_img13 with Dissolve(1.0)

                                pause

                                d "Hora de finalizar você."

                                mc "Aí é golpe b- aahn!"

                                d "Goza! Pode gozar!"

                                mc "Eu tô quase lá, [d]!"

                                d "Pode jogar tudo em mim!"

                                mc "Minha nossa! T-tá muito bom! Você é muito gata, Diana!"

                                d "Hmmm!"

                                mc "Ah! Aaahh! AAAGHH!"

                                scene diana3_img14 with vpunch

                                pause

                                mc "AAAAKH!"

                                d "Isso! Jorra tudo, meu bem..."

                                mc "Aah... aahhn..."

                                d "Gostou?"

                                mc "Gostei? Eu quase infartei gozando tanto..."

                                d "Eu vou considerar isso um elogio..."

                                mc "D-desculpa a sujeira."

                                d "Que sujeira?"

                                scene diana3_img15 with Dissolve(1.0)

                                pause

                                d "Eu adorei seu sabor..."

                                mc "U-uau..."

                                d "Nesta noite eu estou aqui pra você. Inteira."

                                mc "Eu também tô aqui pra você."

                                d "A gente pode se divertir assim outro dia. Eu vou adorar sentir você de novo."

                                mc "N-nem fala uma coisa dessas... você quer ir de novo hoje ainda?"

                                d "Está bom pra mim por uma noite..."

                                mc "Então é bom você parar de lamber assim..."

                                d "Huhu..."

                                scene black with dissolve

                                scene diana3_img16 with Dissolve(1.0)

                                d "Você lembra o que eu te falei da outra vez?"

                                mc "O quê?"

                                d "O problema desse nosso... arranjo."

                                mc "A tal pessoa ciumenta?"
                                scene dnew_ani08 with Dissolve(1.0)
                                d "É. Isso continua, tudo bem? Ela não se preocupa com pessoas como você."

                                mc "Como eu? Tipo, baixo clero?"

                                d "É. E essa é nossa vantagem. Mas tente não falar demais."

                                mc "Entendi... eu sou um paparazzo mas só vou colocar no jornal o que a gente combinar."

                                d "Obrigada. Isso é bom pra mim, mas é bom pra você também. Você não quer chamar a atenção das pessoas erradas."

                                mc "Ok. Vou ficar de olho, [d].{w=0.3}"
                    "Se você me provocar eu te ataco.":


                        mc "Não. Se você continuar me provocando eu vou te atacar. Igual das outras vezes."

                        d "Você não tem jeito mesmo. Eu quero te mimar, mas como desse jeito?{w=1.0}"
            "Desculpa. Não tô no clima agora.":


                $ diana3_negou = True

                "Eu não quero dar esse passo com a [d]."

                "Ela é linda, mas com tudo o que tá acontecendo ultimamente, não acho uma boa ideia."

                mc desculpa "Desculpa. Eu não quero isso agora."

                d "Quê? Sé-"
    else:


        $ diana_e3 = "amizade"

        d "Olha..."

        d "Eu te chamei aqui pra gente poder se divertir como adultos."

        mc envergonhado "A-adultos?"

        d "Mas eu realmente não tô me sentindo no clima."

        d "Quando a gente conversa, eu sinto que você é muito mais um amigo do que um parceiro de cama."

        mc desculpa "Um amigo?"

        d "Sim. Eu sinto que é fácil conversar com você. Contar as coisas que eu quero sem me preocupar."

        d "É uma sensação diferente... como se você tivesse um genuíno interesse em mim."

        mc normal "Claro que eu tenho."

        d "?"

        mc desconfiado "Que foi?"

        scene diana_e3_cama1 with Dissolve(1.0)

        d "E ainda fala isso de forma tão natural..."

        d "Você com certeza é estranho."

        mc zerado "De novo?"

        d "Não consigo evitar. É culpa sua, bobo..."

        mc "Me chama de estranho e a culpa ainda é minha..."

        d "Vo-"

    scene quarto_paris geral with hpunch

    "{i}TOC TOC{/i}"

    d "Hm?"

    "Homem" "[d]!"

    "{i}TOC TOC{/i}"

    "Homem" "Abre a porta!"

    mc serio "Quem é esse cara?"

    d "Meu Deus! [mc], por favor entra no meu closet."

    mc desconfiado "Que? Po-"

    d "Entra logo. Aqui. Vai!"

    "Homem" "[d]!"

    scene black with hpunch

    mc desconfiado "Ai!"

    d "Fica quieto, por favor."

    "..."

    "Que porra foi essa agora?"

    "..."

    "Pera. Acho que eu consigo escutar."

    "Homem" "{size=17}Por que demorou?{/size}"

    d "{size=17}Estava deitada. O que foi?{/size}"

    "Homem" "{size=17}É assim que é para falar comigo?{/size}"

    d "{size=17}Desculpa, Barão.{/size}"

    mc surpreso "Ba-"

    "Opa."

    "Barão! É ele?! O dono do cassino?!"

    "Homem" "{size=17}Enfim... tenho um cliente importante e ele quer lhe ouvir cantar.{/size}"

    d "{size=17}Agora? Eu já me apresentei hoje. Estava pronta pra dormir.{/size}"

    "Homem" "{size=17}O que está acontecendo com você hoje?{/size}"

    d "{size=17}O que o senhor quer dizer?{/size}"

    "Homem" "{size=17}Você se esqueceu de como as coisas funcionam por aqui?{/size}"

    "Homem" "{size=17}Se eu mandar você descer lá e cantar. Você canta.{/size}"

    d "{size=17}...{/size}"

    "Homem" "{size=17}Não entendeu? Vou te dar outro exemplo.{/size}"

    "Homem" "{size=17}Se eu mandar você ir lá e cantar nua para ele ficar de pau duro vendo você. VOCÊ FAZ!{/size}"

    "Homem" "{size=17}Agora você entendeu?{/size}"

    d "{size=17}Sim, senhor...{/size}"

    "Homem" "{size=17}Acho bom. Estou te esperando no Jazz Corner. Você tem cinco minutos.{/size}"

    d "{size=17}Sim, senhor...{/size}"

    "..."

    "Que merda foi essa? Esse cara tava falando sério? Quem ele acha que a [d] é?"

    d "[mc]..."

    scene quarto_partis visao1 with Dissolve(1.0)

    mc desculpa "..."

    show diana r_desconfiada with dissolve

    d "..."

    d "Eu tenho que resolver uma coisa. Posso te chamar um outro dia?"

    mc preocupado "Claro... Mas voc-"

    d "Não fale nada, por favor."

    d "Quando quiser me ver, eu me apresento alguns dias da semana no Jazz Corner."

    d "Sempre que vier ao cassino dê uma passadinha lá."

    mc "Tá. Mas Di-"

    d "Boa noite, [mc]. Obrigada pela companhia."

    mc "Boa noite..."

    scene black with Dissolve(1.0)

    label diana_e3_final:

        scene cassino geral with Dissolve(1.0)

        if diana_e3 != "horrivel":

            "..."

            "Por que o Barão falou daquele jeito com a [d]?"

            "E ela ainda não fez nada. Ela não parece o tipo de mulher que iria ouvir algo assim e ficar quieta."

            "Seja lá o que acontece entre a [d] e o Barão, é mais complicado do que parece."

            "Quero muito poder entender isso e ajudar ela no que eu puder."

            "Foda-se se ela me acha estranho ou se eu vou me ferrar por me meter na vida das pessoas."

            "O que adianta viver com medo e não ser útil pras pessoas que a gente se importa?"

            "Legal... agora eu tô me achando o super herói."

            mc zerado "Talvez eu realmente seja estranho."
        else:


            "Eu não quis subir com ela."

            "Melhor eu voltar pra casa e focar em outras coisas."

            "Espero que a [d] fique bem e que a gente possa conversar em outra oportunidade."

        scene cassino_roleta with Dissolve(1.0)

        show pessoas_roleta2 with dissolve

        "Garota" "Você viu aquela garota estranha? Uma menina pálida que tava hoje no Jazz Corner? Dizem que é uma maga."

        "Amiga" "Sim! Eu vi... fiquei até meio com medo dela..."

        mc desconfiado "Hm?"

        "Garota" "Eu ouvi uma história que se você desagradar ela e ficar sozinho até o final do show, ela aparece pra você."

        "Amiga" "Ai, que medo! Você sabe o que desagrada ela?!"

        "Garota" "Ela é bem misteriosa, então se você conseguir descobrir algo dela e contar pros outros, provavelmente ela não vai gostar."

        "Amiga" "Não quero nem saber disso..."

        "Maga? Pálida? Será que o Fabrício sabe alguma coisa sobre ela? Talvez eu podia {b}comprar alguma informação dele{/b}."

        "Enfim... tá tarde. Deixa eu voltar pra casa."

        scene black with Dissolve(2.0)



        menu:
            "E o que aconteceu com a Diana?":


                d "Boa noite a todos. Gostaria de cantar hoje uma nova canção."

                scene diana3_img17 with Dissolve(1.0)

                pause

                d "{cps=6}{i}Na esquina da rua fim com o começo...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Cruzando aquela avenida cujo nome sempre esqueço...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Ela olhava com os olhos frios de quem entende...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}As dificuldades que só o escravo sente.{/i}{/cps}{w=2.0}{nw}"



                "Homem" "Se você vai cantar essa merda, pelo menos dá algo pra gente!"

                d "..."

                scene diana3_img18 with Dissolve(1.0)

                d "{cps=6}{i}As luzes dos carros e as luzes das ruas...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Tudo lembrava dos dias mais turbulentos...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Quando suas palavras não eram suas...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}E o desespero preenchia todos os momentos.{/i}{/cps}{w=2.0}{nw}"

                "Homem" "Eu prefero as músicas antigas..."
                scene dnew_ani09 with Dissolve(1.0)
                "???" "Deixa ela cantar."

                "Homem" "Tira mais um pouco então!"

                d "Droga..."

                "Homem" "Que foi?!"

                "Ele vai continuar me humilhando... e na frente desse cara."

                "Acho que é melhor eu só subir de uma vez e depois sofrer as consequências..."

                "Ou só aceitar tudo o que esse maldito pedir e acabar logo com isso?"

                menu:
                    "Encerrar tudo agora":


                        d "Chega desse absurdo! Seus porcos imundos!"

                        d "Estou me retirando para o meu quarto!"

                        scene black with vpunch

                        "Homem" "Volte aqui! Agora!"

                        "..."

                        jump diana3_premium_final
                    "Continuar cantando":


                        "Só vai ser mais sofrimento se eu parar agora."

                d "Nada."

                scene diana3_img19 with Dissolve(1.0)

                d "{cps=6}{i}As luzes então apagaram como um eclipse...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Os olhos carregados ela chorou e disse...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}O fim enfim o momento mais aguardado...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Dessa forma seu espírito seria libertado.{/i}{/cps}{w=2.0}{nw}"

                "Homem" "O Gustav aqui quer ver algo diferente! Artista normal ele já conhece um monte!"
                scene dnew_ani15 with Dissolve(1.0)
                "Homem" "Coloca a linguinha pra fora!"

                d "!!!"

                "Homem" "Vai logo!"

                scene black with dissolve

                scene diana3_img20 with Dissolve(1.0)

                pause

                gus "Por que fazer ela cantar assim?"

                "Homem" "Alguns homens sentem prazer quando estão humilhando as mulheres."

                gus "Isso é um absurdo. São verdadeiros animais."

                "Homem" "Eu também acho... mas sabe como é... tem cada louco por aí."

                gus "Continue, minha filha."

                scene black with dissolve

                scene diana3_img21 with Dissolve(1.0)

                d "{cps=6}{i}No momento de fortúnio o eclipse chegou para sua alegria...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}Pois no fim da noite vinha outra vez o dia...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}E a amarra da vida novamente a prendia...{/i}{/cps}{w=1.0}{nw}"

                d "{cps=6}{i}A jovem garota, a escrava da ilha.{/i}{/cps}{w=1.0}{nw}"

                "Homem" "Excelente! Agora eu gostei! A letra é horrível, mas a performance! Magnífica!"
                scene dnew_ani10 with Dissolve(1.0)
                gus "É uma linda canção."

                d "Obrigada. Agora se me permit-"

                "Homem" "Não não. Você vai ficar aí enquanto conversamos. Para... melhorar a vista. Você não concorda?"

                gus "Você é terrível. Mas não tem chamam de Barão à toa, não é mesmo?"

                "Homem" "Hah."

                scene black with dissolve

                scene diana3_img22 with Dissolve(1.0)

                "Barão" "Fazia tempo que você não vinha pra cá."

                gus "É o trabalho. Sempre o trabalho. E outras coisas."

                "Barão" "Trabalho e outras coisas. É sempre o trabalho e outras coisas... você tem toda razão."

                gus "Não quero que pense que eu fiz desfeita do seu convite."

                "Barão" "Claro que não. Você é um homem ocupado. Trabalho e outras coisas... é uma honra ter você aqui."

                gus "Não precisa ser humilde. Você é tão importante quanto eu pra tudo continuar acontecendo."

                "Barão" "Somos a galinha dos ovos de ouro. Sem querer faltar com humildade, sem nós o que sobraria?"

                gus "Concordo, amigo. O dinheiro move o mundo."

                "Barão" "Move o mundo. Exatamente."

                scene diana3_img23 with Dissolve(1.0)

                "Barão" "Mudando de assunto, como andam as outras coisas? O trabalho eu sei que vai bem."

                gus "Não me sinto à vontade de falar sobre isso com ela aqui."

                "Barão" "Pode confiar em mim, a Diana sabe como se comportar."

                gus "Hmm... bom, tem uma nova garota."

                "Barão" "Uma nova garota... excelente. Aquela... como é o nome dela mesmo? Priscila? Ela é uma jóia."

                gus "Com certeza. Dificilmente aparecerá outra como essa. Mas sabe como é... tudo o que a gente usa demais acaba enjoando."

                "Barão" "Haha... nem me fala. Estou ansioso para ver essa nova aquisição."

                gus "É... vamos ver..."

                if v54_fim:

                    "Barão" "Eu escutei sobre uma audiência..."

                    scene diana3_img24 with Dissolve(1.0)

                    gus "..."

                    "Barão" "Em que pé tá isso?"

                    gus "Tudo vai acontecer como sempre aconteceu. Não se preocupe."

                    if julgamento_sucesso > 0:

                        "Barão" "Parece que teve gente que deu com a língua nos dentes."

                        gus "É o que parece..."

                        "Barão" "Nós precisamos fazer nossa parte, amigo. Isso foi desleixo."
                    else:


                        "Barão" "Parece que ninguém falou nada contra você. Você fez um bom trabalho."

                        gus "Mas é claro."

                    gus "Eu já disse para não se preocupar. Está tudo sob controle."

                    "Barão" "A Richter não tá na nossa lista de pagamentos. Isso muda muita coisa."

                    "Barão" "Se ela realmente decidir abrir uma investigação, imagina o que ela pode encontrar!"

                    gus "Vocês vão me jogar ao mar?"

                    "Barão" "Essa é a decisão que ninguém quer tomar. Nisso eu aposto meu dinheiro."

                    gus "..."

                    gus "E por que ela não tá com a gente?! Não era pra ele resolver isso?!"

                    "Barão" "Nisso eu concordo com você. Era pra ele cuidar dessa parte."

                    gus "A gente dá a grana, o Tony cuida da sujeira e ele garante o poder do nosso lado!"

                    gus "Eu tô fazendo minha parte!"

                    "Barão" "Parece que tem pessoas de fora olhando pra gente. Eu sinto que essa juíza tem as costas quentes."

                    gus "Claro! Quem recusaria entrar na roda? Mas não tem nada que a gente possa fazer?!"

                    gus "Ele nem me recebe!"

                    "Barão" "Ele nunca quis nada comigo também. Você sabe o quanto ele valoriza as aparências."

                    gus "Idiota... se ele acha que eu vou cair sozinho, tá muito enganado!"

                    "Barão" "Ei ei! Calma lá, amigo. Vamos com calma."

                    gus "É verdade..."

                    "Barão" "Parece que você precisa de uma mudança no clima."

                "Barão" "Vem. Deixa eu te mostrar a minha garota."

                gus "Você... ela não é só sua estrela, é?"

                "Barão" "Ela é minha estrela, mas muito mais que isso. A Diana já me ajudou a conquistar muita coisa!"

                "Barão" "Venha. Venha conferir."

                scene black with dissolve

                scene diana3_img25 with Dissolve(1.0)

                pause

                d "Ei! Eu já me apresentei!"

                "Barão" "Pare de besteira e deixe o senhor Gustav apreciar meu material."
                scene dnew_ani11 with Dissolve(1.0)
                "Esse filho da puta... tudo o que eu fiz não foi suficiente?!"

                label diana3_premium2:

                    pass

                "Eu vou deixar ele fazer o que quiser comigo?!"

                menu:
                    "Correr para o quarto":


                        d "Chega desse absurdo! Seus porcos imundos!"

                        d "Estou me retirando para o meu quarto!"

                        scene black with vpunch

                        "Barão" "Diana! Volte aqui! Agora!"

                        "..."

                        jump diana3_premium_final
                    "Ficar parada":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_57

                            jump diana3_premium2

                        "Só quero acabar logo com isso."

                        "Aguentar esses nojentos mais alguns minutos e continuar com a minha vida."

                        d "..."

                        "Barão" "Melhor assim."

                "Barão" "E aí? O que você acha?"

                gus "Você tem uma mulher e tanto aqui."

                "Barão" "É um tesouro. Não sei quem venceria num duelo com a Priscila, mas... acho que daria uma boa briga."

                gus "Ela é um pouco mais velha..."

                "Barão" "..."

                gus "Mas com certeza é uma mulher e tanto."

                scene diana3_img26 with Dissolve(1.0)

                gus "Principalmente aqui atrás. Abençoada."

                "Barão" "Foi um achado e tanto. Abençoada mesmo."

                "Barão" "Aproveite um pouco. Ela está aqui pra você, amigo."

                gus "Obrigado, amigo. Não tem como não melhorar o humor com isso aqui."

                "Barão" "Com certeza."

                gus "Eu posso fazer o que eu quiser?"

                "Barão" "Claro! Eu trouxe ela para ela divertir você."

                gus "Com licença, bebê. Eu quero sentir você aqui."

                d "?!"

                scene diana3_img28 with vpunch

                gus "Eu aposto que você vai gostar! É minha arte dar prazer para as mulheres!"

                d "!!!"

                gus "Ela não consegue nem falar! Que delícia!"

                gus "Ela tá gostando, não tá?!"

                "Barão" "Vamos tomar o silêncio dela como um 'sim'."

                d "Nng!"

                gus "Ela nunca vai admitir... mas ela adorou."

                gus "É o suficiente pra mim."

                "Barão" "Vamos. Eu vou te levar."

                gus "Obrigado. E obrigado pelo prazer de sentir essa incrível garota."

                "Barão" "O prazer é todo nosso."

                scene black with Dissolve(1.0)

                "..."

                scene diana3_img30 with Dissolve(1.0)

                "Barão" "Obrigado. Você foi muito bem. Ele ficou satisfeito."

                d "Seu animal... qual a necessidade de chegar nesse ponto?!"

                "Barão" "Nem vem. Você até gostou."

                d "Cretino! Você queria que eu chutasse ele na cara?!"

                "Barão" "Ok... perdão... eu sei que você se esforçou por mim. Eu não vou brincar com isso."

                d "Você ainda vai ser preso. E vai pagar por tudo o que você tá fazendo eu passar!"

                "Barão" "Se você sente melhor fazendo ameaças... eu não ligo."

                d "Maldito!"

                "Barão" "Se você continuar fazendo o que eu mando, você continua com sua vida de rainha."

                d "Me deixa ir embora!"

                "Barão" "Ainda não... você ainda precisa de mais."

                d "Eu vou conseguir! Você vai ver!"

                "Barão" "Eu aposto que sim. Você é muito competente."

                "Barão" "Mas está bom hoje. Vá para o quarto e descanse."

                d "..."

                "Barão" "Ah... e Diana... não se esqueça que você é minha."

                "Barão" "Não é porque eu te empresto para um amigo, que você pode ser de outra pessoa."

                "Barão" "Se eu descobrir qualquer coisa assim... essa pessoa está morta."

                d "Não tem ninguém..."

                "Barão" "Que bom. Boa noite."

                scene black with Dissolve(2.0)

                jump diana3_premium_final
            "Eu não quero saber":




                "Deixa pra lá. Ela é grandinha e vai saber se cuidar."

                "Aposto que ela ia preferir se eu não me preocupasse com ela."

        label diana3_premium_final:

            pass

        $ tempo = 4

        $ v19_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v19_fim","final","local")





    jump call_cidade

label diana_evento2:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d2_save", extra_info="d2_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    if tempo < 3:

        scene mc parque_sentado with Dissolve(1.0)
    else:


        scene mc parque_sentado_noite with Dissolve(1.0)

    "Eu e a [d] fizemos um acordo... eu tenho que entregar pautas sobre as músicas dela."

    "É um acordo excelente pra mim. E pelo que parece ela também sai ganhando com a visibilidade da revista."

    "Agora ela quer fazer um show só pra mim."

    "Será que é algo somente profissional? Ou talvez ela quer fazer algo mais intimista pra gente poder ficar sozinhos?"

    menu:
        "Eu gostaria de ter algo a mais com a [d]":


            "A [d] parece ser uma garota extremamente requintada, além de ser linda."

            "Só um idiota não iria querer algo com ela."
        "Não quero nada com ela":


            "A [d] parece uma garota incrível, mas não quero nada com ela."

            if priscila_namoro:

                "Ainda mais agora que eu tenho algo sério com a [c]. Não seria certo com ela."

    "O problema é essa roupa que eu tô usando. Não sei se é uma boa ideia ir assim no Cassino."

    "O Cassino é o lugar mais top da ilha. Que tipo de impressão eu vou passar vestido assim."

    "Preciso ver o que eu tenho lá em casa..."

    scene black with dissolve

    "..."

    if casa:

        scene ap mc_banheira with Dissolve(1.0)
    else:


        scene mc ap_pronto with Dissolve(1.0)

    mc "Pelo que eu vi aqui..."

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()
            roupa_blacktie = PythonSDLActivity.pegaBlacktie()
            roupa_blazer = PythonSDLActivity.pegaBlazer()

    if not roupa_blazer and not roupa_blacktie:

        "Droga... não encontrei nada que eu possa usar que seja chique o suficiente pra ir no Cassino."

        "Talvez seja uma boa eu passar na boutique lá no centro da cidade e tentar comprar algo."

        if tempo < 3:

            mc "Não tô afim de ir na loja agora."
        else:


            mc "Essa hora a loja já tá fechada."

        "Vou dá aquela hibernada e amanhã dou um pulo lá."

        "..."

        if casa:

            scene ap mc_dormindo1 with Dissolve(1.0)
        else:


            scene mc dormindo with Dissolve(2.0)

        "Delícia dormir..."

        "{i}zZzZzzzZZZZzzzZzZZz{/i}"

        scene black with Dissolve(1.0)

        $ dia += 1
        $ tempo = 1

        mc "Uaaaahhhh!"

        if casa:

            scene ap sala with Dissolve(1.0)
        else:


            scene mc ap_pronto with Dissolve(1.0)

        mc "Tô pronto."

        mc "Deixa eu pegar a merda do busão e ir dar uma olhada no que a boutique tem por uma grana que eu possa pagar."

        if cash < 250:

            "Que deve ser nada..."
        else:


            "Se bem que eu tô com uma graninha aqui. Talvez dê pra comprar algo bacana."

        scene black with Dissolve(1.0)

        "..."

        $ diana_e2_roupa = True

        jump boutique
    else:


        if roupa_blacktie:

            "Eu tenho meu Black Tie. Ele é perfeito pro Cassino."

            "Um traje de muita classe. Tenho certeza que a [d] vai achar incrível."

        if roupa_blazer:

            "Eu tenho meu Blazer. Ele é um traje esportivo chique segundo a moça da boutique."

            "É uma roupa chique mais casual. Ele pode não ser tão fino, mas vai ser muito bom ir com ele."

        mc "Eu tô tranquilo. Vai dar pra ir bem massa no Cassino amanhã."

        "Vou dá aquela hibernada e amanhã bora pro Cassino!"

        "..."

        if casa:

            scene ap mc_tv_quarto with Dissolve(1.0)
        else:


            scene ap mc_dormindo2 with Dissolve(2.0)

        "Delícia dormir..."

        "{i}zZzZzzzZZZZzzzZzZZz{/i}"

        scene black with Dissolve(1.0)

        $ dia += 1
        $ tempo = 1

        mc "Uaaaahhhh!"

        jump diana_e2_cassino

label diana_e2_cassino:

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    "Tudo resolvido... vou matar o tempo."

    "Ela disse oito da noite, então dá pra ver alguma coisa enquanto isso."

    "..."

    "Pera! Que porra é essa?!"

    "Uma policial lutando contra clones de uma mulher ninja pelada?!"

    "E cada um desses clones custa milhões de dólares?!"

    "Que desperdício..."

    "..."

    $ tempo = 3

    if casa:

        scene ap mc_dormindo3 with Dissolve(1.0)
    else:


        scene apartamento noite with Dissolve(1.0)

    "Opa. Já passou das sete. Melhor eu me arrumar."

    play sound "audio/som_16_chuveiro.mp3"

    if casa:

        scene ap mc_chuveiro with Dissolve(1.0)
    else:


        scene mc banho with Dissolve(1.0)

    $ renpy.pause(5)

    "O Cassino é o principal ponto da ilha. Quase todo o dinheiro que roda por aqui passa por lá de alguma forma."

    "Interessante que eu nunca ouvi muito sobre o dono do lugar. Só sei que ele é chamado de {b}Barão{/b}."

    "Dizem que a família do Barão foi uma das primeiras a habitar a capital."

    "Desde então eles apoiam o grupo do prefeito. Aliás, o prefeito da nossa cidade tá mais pra um monarca."

    "Pelo que eu sei, o grupo político dele está no poder da capital há mais de cem anos."

    "Isso não pode ser verdade... Enfim... melhor eu terminar."

    "..."

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()
            roupa_blacktie = PythonSDLActivity.pegaBlacktie()
            roupa_blazer = PythonSDLActivity.pegaBlazer()

    stop sound

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento noite with Dissolve(1.0)

    "Beleza... Com qual roupa eu devo ir?"

    menu:

        "Vestir o {b}Black Tie{/b}" if roupa_blacktie:

            $ d2_blacktie = True
            $ cassino_roupa = "blacktie"

            show mc blacktie with dissolve

            "Óbvio que eu vou com o meu traje mais fino. O Cassino é o único lugar aqui na ilha que o Black Tie cai como uma luva."

            "Estou mais do que preparado pra ver todo mundo pagando pau pra mim."

        "Vestir o {b}Blazer{/b}" if roupa_blazer:

            $ d2_blazer = True
            $ cassino_roupa = "blazer"

            show mc blazer with dissolve

            "Meu blazer é top pra usar no Cassino. Ele não é o traje mais fino, mas é chique e casual."

            "Eu vou me sentir muito bem usando ele. E a [d] vai adorar me ver usando uma roupa diferente."
        "Vestir a roupa de sempre":


            $ cassino_roupa = "normal"

            "Merda... ser pobre é complicado. Usar essa mesma roupa de sempre em um lugar tão chique vai ser triste."

            "Mas também foda-se. Não é a roupa que vai fazer de mim ou cara legal ou não."

            "Eu posso ser uma boa companhia independente da roupa que eu uso."

    "..."

    "Estou pronto."

    mc "Essa noite vai ser demais."

    mc "Alguém me segure!"

    "..."

    scene cidade regiao2_noite with Dissolve(2.0)

    "O Cassino fica bem perto de casa."

    "É só cruzar o parque e fazer a volta ali perto daquele prédio gigante."

    "Quando eu paro pra pensar como tem tanta coisa diferenciada nessa ilha, até dá um orgulho de conseguir pagar o aluguel pra morar aqui."

    "Bom, aqui estamos."

    scene cassino fachada with Dissolve(2.0)

    pause

    "Uou... o Barão realmente sabe como chamar a atenção pro Cassino."

    "Agora que tô aqui tá até dando um frio na barriga."



    menu:
        "Respira fundo e entra, [mc]...":


            "Preciso em concentrar e fazer isso."

            "É pela [d] e pelo meu emprego como paparazzo."
        "Para de ser um bundão e entra logo, [mc]!":


            mc preocupado "..."

    "Ok! Vamos nessa!"

    scene cassino portas with Dissolve(1.0)

    "O lugar é foda demais. Olha todo esse ouro e cristal..."

    "As portas refletem o fundo da cidade como se fossem um espelho de cristal. E os adornos de ouro fazem o mesmo."

    "Eles sem dúvida não pouparam na hora de decorar isso aqui."

    "Se bem que a quantidade de grana que eles devem ganhar aqui não é brincadeira."

    mc desconfiado "Hmmm..."

    "Parece que qualquer um pode entrar."

    "Vamos lá."

    "..."

    scene cassino hall with Dissolve(2.0)

    pause

    "Uou... é maior do que eu imaginava. E é só o hall de entrada. Muito espaço, muito luxo."

    "Será que esses detalhes são só imitação de ouro ou é tudo de verdade?"

    "Como que pode alguém ter tanto dinheiro pra levantar algo assim? Nesse nível?"

    if d2_blacktie or d2_blazer:

        "Sorte que eu vim com uma roupa massa. Se eu tivesse com aquela calça jeans ia passar vergonha."
    else:


        "A merda é que eu tô de jeans com esta camiseta..."

        "Olha... ser pobre não é fácil."

    if not cassino_1vez:



        call atendente_cena from _call_atendente_cena_1

    scene cassino geral with Dissolve(2.0)

    pause

    if not cassino_1vez:

        $ cassino_1vez = True

        call cassino_ana_cena from _call_cassino_ana_cena_1

    "Bom... ainda tenho uns minutos antes de começar o show da [d]."

    "Chegar adiantado vai parecer desespero. E além do mais, tô doido pra conhecer o restante do Cassino."

    "Vamos dar uma olhada."

    "..."

    scene cassino angulo with Dissolve(2.0)

    pause

    "O cassino tem vários jogos diferentes. Esse aqui na mesa eu nem sei o que é."

    "As pessoas devem gastar absurdos aqui."

    scene cassino_roleta with Dissolve(2.0)

    pause

    "A {b}roleta{/b} eu conheço."

    "Ainda não joguei, mas sempre tá cheio de gente andando por aqui."

    "Não lembro exatamente as regras, mas parece que você escolhe um número ou uma cor e se cair a que você escolheu você ganha."

    "Se eu conseguir juntar uma grana bacana, pelo menos vou querer tentar algumas vezes."

    mc tarado "Vai que eu fico rico..."

    if not cassino_1vez:

        $ cassino_1vez = True

        scene cassino_slots with Dissolve(2.0)

        pause

        "A {b}máquina de slots{/b} é muito massa também. Só colocar a moeda e torcer pra cair a combinação certa."

        "Fazer um JACKPOT e ficar milionário... Esse é o sonho de qualquer um!"

        "Com certeza vou querer jogar aqui também se eu tiver uma verba sobrando."

        "..."

    scene cassino geral with Dissolve(2.0)

    "Ainda tem a mesa de cartas, outro tipo de caça níqueis e várias outras coisas que eu ainda não joguei, mas já deu oito horas."

    "Vou ter que voltar aqui outra hora."

    "Bora pro Jazz Corner."

    "..."

    scene jazz geral with Dissolve(2.0)

    pause

    "Que lugar massa..."

    "Tão requintado..."

    mc surpreso "E tá vazio!"

    "Será que ela realmente vai cantar só pra mim?"

    "A [d] é a principal atração da principal atração da ilha. Por que ela tem interesse em mim?"

    "E se ela-"

    d "Oi, senhor [mc]."

    show diana ola with Dissolve(1.0)

    mc surpreso "[d]!"

    menu:
        "Que susto, mulher!":


            mc angustiado "Que susto, mulher! Quer me matar do coração?"

            mc concentrando "..."



            d "{i}Rsrs{/i}"

            d "Não seja exagerado."

            mc envergonhado "Ok, talvez eu tenha gritado mais do que eu devia mesmo..."

            d "Foi engraçado."
        "Você está incrível.":


            $ diana_seducao += 1

            mc charmoso "Uou... você está incrível."



            d "Obrigada."
        "Que surpresa encontrar você.":


            mc charmoso "Que surpresa encontrar você."



            d "Surpresa? Não marcamos justamente esta hora?"

            mc envergonhado "Tem razão... não é assim tão surpreendente."

            d "Você é engraçado, [mc]."

    d "Fiquei muito feliz de você ter aceitado meu convite."

    mc charmoso "Não tem como perder uma apresentação particular de uma estrela como você."

    d "Fico lisongeada."

    if d2_blacktie:

        $ diana_seducao += 2

        d "E deixa eu te dizer. Esse black tie caiu muito bem em você."

        mc charmoso "Obrigado. Uma roupa especial para uma ocasião especial."

        d "Preciso ser sincera. Não achei que você tinha cacife pra bancar algo assim."

        mc "O importante é investir no que realmente importa."

        d "Você tem toda razão."

    elif d2_blazer:

        $ diana_seducao += 1

        d "Agora que estou reparando, você ficou muito bem de blazer."

        d "Por um instante achei que você poderia querer vir com aquela roupa branca que te vi na praia."

        mc charmoso "De forma alguma. A ocasião e lugar pedem no mínimo um blazer."

        d "Concordo plenamente."
    else:


        show diana exibida with Dissolve(1.0)

        d "Eu agradeço muito por você ter vindo, mas esperava que você fosse se vestir um pouco mais-"

        mc envergonhado "Entendo. Sua pauta me ajudou no trabalho, mas a grana ainda tá curta."

        d "Entendo..."

        d "Sabe, como dizem, aparência não é tudo, certo?"

        mc "Certo..."

        "Ela tá querendo ser legal, mas obviamente ela teria preferido que eu tivesse trajado mais adequadamente para um lugar requintado como o cassino."

        "Mas não se deve julgar um livro pela capa. Ela vai ver que mesmo de roupa branca, [mc] é uma incrível companhia."

    mc desculpa "Mas... é sério que só estarei eu aqui?"

    d "Sim."

    show diana exibida with dissolve

    d "O que eu vou cantar pra você é meu novo single. Ninguém fora da produção ouviu ainda. Você será o primeiro."

    menu:
        "Isso é incrível, [d]!":


            mc surpreso "Isso é incrível, [d]! Vai ser demais!"

            d "Tenha calma {i}rsrs{/i}"

            mc envergonhado "É que parece algo tão exclusivo."

            d "E é mesmo. Eu me empenhei bastante nessa música."
        "Estou um pouco nervoso com isso.":


            mc envergonhado "Pensar nisso me deixa um pouco nervoso. É tão coisa de VIP."

            d "Não se estresse demais com isso."

            d "Realmente é algo exclusivo, mas fui eu que te convidei."

            mc "Tem razão, mas mesmo assim..."
        "Vai ser incrível ver você cantando pra mim.":


            $ diana_seducao += 1

            mc charmoso "Seu convite foi perfeito. Vai ser incrível ver você cantando só pra mim."

            show diana provocando with dissolve

            d "Hmm... Espero que você não esteja vendo mais do que existe."

            mc "O que eu vejo é uma cantora linda e talentosa que vai fazer uma apresentação só pra mim."

            d "Você merece por ter cumprido sua palavra e ter publicado a matéria."

            mc charmoso "Eu sempre cumpro. Pode confiar."

    show diana ola with dissolve

    d "Se você está pronto, pode sentar em algum daqueles lugares na frente."

    d "Eu vou me preparar e subir. Fique à vontade."

    mc normal "Ok."

    hide diana with dissolve

    "Ela vai começar. Melhor eu sentar em algum lugar."

    scene jazz corner with Dissolve(2.0)

    "Deixa eu sentar."

    if d2_blacktie:

        show mc jazz_corner_blacktie with dissolve

    elif d2_blazer:

        show mc jazz_corner_blazer with dissolve
    else:


        show mc jazz_corner_normal with dissolve

    pause

    "Aqui é igual o resto cassino. Os caras não economizaram na decoração."

    "Então quer dizer que é aqui que a [d] se apresenta."

    "Imagino o tipo de magnata que acompanha o trabalho dela."

    "E agora ter a chance de ver ela, só eu..."

    d "Pronto, [mc]?"

    mc "Si-sim."

    show diana jazz_corner_cantando with dissolve

    d "Espero que você não se importe do instrumental ser gravado."

    mc "Que isso! Claro que não."

    d "Não quis incomodar toda a banda. Além de que nem todos ouviram ainda."

    mc "Está tudo incrível, [d]. Relaxe."

    d "..."

    $ renpy.choice_for_skipping()

    $ proibido_salvar = True
    $ show_quick_menu = False

    d "Pode soltar!"

    play music "audio/musica_6_diana.mp3" loop

    $ renpy.pause(delay=10, hard=True)

    scene diana cantando1 with Dissolve(3.0)

    d "{cps=6}{i}Na esquina da rua fim com o começo...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Cruzando aquela avenida cujo nome sempre esqueço...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Ela olhava com os olhos frios de quem entende...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}As dificuldades que só o escravo sente.{/i}{/cps}{w=2.0}{nw}"

    scene diana cantando1 at diana_esquerda with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana cantando2 with Dissolve(3.0)

    d "{cps=6}{i}As luzes dos carros e as luzes das ruas...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Tudo lembrava dos dias mais turbulentos...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Quando suas palavras não eram suas...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}E o desespero preenchia todos os momentos.{/i}{/cps}{w=2.0}{nw}"

    scene diana cantando2 at diana_direita with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana cantando3 with Dissolve(3.0)

    d "{cps=6}{i}As luzes então apagaram como um eclipse...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Os olhos carregados ela chorou e disse...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}O fim enfim o momento mais aguardado...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Dessa forma seu espírito seria libertado.{/i}{/cps}{w=2.0}{nw}"

    scene diana cantando3 at diana_esquerda with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    scene diana cantando4 with Dissolve(3.0)

    d "{cps=6}{i}No momento de fortúnio o eclipse chegou para sua alegria...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}Pois no fim da noite vinha outra vez o dia...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}E a amarra da vida novamente a prendia...{/i}{/cps}{w=1.0}{nw}"

    d "{cps=6}{i}A jovem garota, a escrava da ilha.{/i}{/cps}{w=1.0}{nw}"

    scene diana cantando4 at diana_direita with Dissolve(3.0)

    $ renpy.pause(delay=15, hard=True)

    stop music fadeout 3.0

    $ proibido_salvar = False
    $ show_quick_menu = True

    scene jazz corner with Dissolve(2.0)

    if d2_blacktie:

        show mc jazz_corner_blacktie with dissolve

    elif d2_blazer:

        show mc jazz_corner_blazer with dissolve
    else:


        show mc jazz_corner_normal with dissolve

    mc "..."

    show diana jazz_corner_cantando with dissolve

    d "..."

    d "E então? O que achou?"

    menu:
        "Foi muito massa!":


            mc "Foi demais! Simplesmente demais! Meus parabéns!"

            d "Obrigada..."
        "[d]...":


            $ diana_seducao += 2

            "[d]..."

            d "O que foi, [mc]?"

            mc "Sua música..."

            d "Não se preocupe. Eu... estou bem."

            mc "Mas..."
        "Foi uma experiência incrível.":


            $ diana_seducao += 1

            mc "Foi uma experiência, sei lá... única."

            mc "Acho que eu nunca senti algo assim antes."

            d "Isso me deixa feliz, [mc]. Obrigada."

    mc "Realmente, uma das experiências mais marcantes que eu já tive na vida eu acho."

    d "Obrigada, [mc]... Eu... acho que preciso usar o toilet. Com licença..."

    hide diana with dissolve

    mc "Ah?"

    mc "O que será que aconteceu?"

    mc "Bom... deve ser coisa de cantor..."

    "..."

    "..."

    "Caraca, cadê ela?"

    "Será que eu fiz algo de errado?"

    menu:
        "Sair procurar por ela":


            "Hmmm..."

            "Ela tá demorando. Vou dar uma procurada por ela."

            "Acho que os banheiros ficam pra lá."

            jump diana_e2_depois
        "Ficar e esperar":


            "Provavelmente ela só precisa de um tempo. Não vou causar."

            "..."

            "..."

            "Caraca... nada ainda?"

            menu:
                "Agora é melhor eu ir atrás dela":


                    mc "Ela tá demorando demais. Deixa eu ver o que aconteceu."

                    jump diana_e2_depois
                "Vou ficar aqui. Não quero parecer desesperado":


                    $ diana_e2 = "horrivel"

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("diana_e2_horrivel","diana","personagem")

                    "Vai saber o que tá rolando. Se eu for atrás dela vou ficar parecendo um sujeitinho desesperado."

                    "Acho que vou ficar aqui e só esperar..."

                    "..."

                    "..."

                    d "[mc]! Aqui!"

                    mc "Ufa."

                    scene jazz geral with Dissolve(1.0)

                    mc normal "Oi. Tudo legal?"

                    show diana ola with dissolve

                    d "Tudo. Obrigada por me esperar."

                    d "Era isso que eu pretendia te mostrar. Uma forma de celebrar nossa parceria."

                    mc charmoso "Eu achei simplesmente incrível. Tenho certeza que vai ser um sucesso."

                    show diana provocando with dissolve

                    d "Eu estou um pouco cansada. Vou subir pro meu quarto."

                    mc normal "Acho que eu vou pra casa também. Gostei muito da noite."

                    d "Vamos conversar mais no futuro."

                    mc charmoso "Com certeza. Boa noite, [d]."

                    d "Boa noite."

                    hide diana with dissolve

                    jump diana_e2_final_nal

label diana_e2_depois:

    "..."

    scene jazz_bar angulo1 with Dissolve(2.0)

    "Os banheiros ficam pra lá. Acho que vou esperar ela aqui no bar."

    if d2_blacktie:

        show jazz_bar_mc angulo1_blacktie_normal with dissolve

    elif d2_blazer:

        show jazz_bar_mc angulo1_blazer_normal with dissolve
    else:


        show jazz_bar_mc angulo1_normal_normal with dissolve

    "Vou dar um tempinho aqui."

    "Que estranho... o bar tá fechado. Será que eles fecharam tudo por que a [d] pediu?"

    "E aquela música dela? O que-"

    d "[mc]? Por que está aqui?"

    show jazz_bar_diana angulo1_diana_explicando with dissolve

    mc "Oi."

    mc "É..."

    menu:
        "Fiquei preocupado com você.":


            $ diana_seducao += 1

            mc "Fiquei preocupado com você e vim ver se você tava legal."

            d "Obrigada, [mc]. Você é fofo às vezes, sabia?"

            mc "Haha..."
        "Queria pegar uns drinks pra gente beber.":


            $ diana_seducao += 2

            mc "Queria pegar uns drinks pra gente beber enquanto você se aprontava."

            show jazz_bar_diana angulo1_diana_excitada with dissolve

            d "Hmm..."

            d "Tá querendo me embebedar?"

            mc "Talvez..."

            d "E com qual propósito?"

            mc "Nada como um drink após um show."

            d "Incrível como você acertou. Eu realmente adoro tomar vodka depois de me apresentar."
        "Só tava dando uma olhada no lugar.":


            mc "Tava só me ocupando enquanto você se arrumava."

            d "Desculpa deixar você esperando."

            mc "Relaxa. Coisa de artista, né?"

            d "É..."

    d "Mas me fala. Como é a vida de paparazzo?"

    d "Imagino que nem todas as celebridades te recompensam quando você conta segredos sobre elas."

    if d2_blacktie:

        show jazz_bar_mc angulo1_blacktie_encostado with dissolve

    elif d2_blazer:

        show jazz_bar_mc angulo1_blazer_encostado with dissolve
    else:


        show jazz_bar_mc angulo1_normal_encostado with dissolve

    mc "Olha..."

    menu:
        "Eu adoro trabalhar com isso.":


            $ diana_seducao += 1

            mc "Eu curto muito ser paparazzo."

            mc "Claro que tem seu lado ruim também, mas poder conhecer celebridades e influenciar as pessoas é incrível."

            d "Não imaginei que você fosse do tipo obstinado."
        "Eu vejo como um mal necessário.":


            $ diana_seducao += 2

            mc "Na verdade eu vejo como um mal necessário."

            mc "Não é uma profissão incrível, mas tem quem goste das matérias e eu preciso do dinheiro."

            d "É como se você um escravo da situação, não concorda?"

            mc "Pior que falando assim, é como eu vejo. Sou obrigado pela situação."

            d "Consigo entender sua situação..."
        "Odeio essa profissão.":


            mc "Tá doida?! Eu odeio isso."

            mc "Ter que entregar as pessoas que eu gosto porque um velho precisa de assunto pra revista dele..."

            mc "Se eu tivesse outra forma de viver na ilha, eu sairia dessa na hora."

            d "Entendo..."

    d "Mesmo com o lado ruim e sem gostar de tudo, você continua se esforçando."

    show jazz_bar_diana angulo1_diana_seduzida with dissolve

    d "Não posso negar que seja um pouco incrível..."

    mc "Incrível é você com tudo isso aqui."

    d "É o que parece, não é?"

    d "Todo esse luxo, o glamour, as roupas chiques. É quase como uma outra realidade."

    mc "Com certeza..."

    show jazz_bar_diana angulo1_diana_explicando with dissolve

    d "Emprestando um dizer da minha avó, por fora desta bela viola, existe um pão bolorento."

    mc "O que você quer dizer?"

    d "Não é nada... não vamos deixar isso estragar nossa noite."

    d "..."

    "Preciso falar alguma coisa."

    menu:
        "Como é viver em um lugar como este?":


            mc "Mas como é viver aqui no cassino? Parece ser muito bom."

            d "Tem seus pontos fortes e fracos como tudo na vida, eu penso."

            d "Todo esse glamour que atrai tantas pessoas nem sempre é tão incrível como parece."

            mc "Entendo..."
        "Você parece ser apaixonada pela sua música.":


            $ diana_seducao += 1

            mc "Se tem algo que eu percebi sobre você, é que você ama sua música."

            mc "Deu pra ver isso claramente quando você tava cantando hoje."

            show jazz_bar_diana angulo1_diana_excitada with dissolve

            d "Nâo posso negar. A música realmente mexe comigo."

            d "Acho que é a coisa mais importante que eu tenho na vida. Minha voz, minha técnica, minha banda."

            d "Quero alcançar grandes coisas com minha música."

            mc "Tenho certeza que você vai."

    show jazz_bar_diana angulo1_diana_seduzida with dissolve

    d "Mas eu ainda pretendo sair deste lugar e tornar minha música famosa pelo mundo."

    mc "Certeza que você vai conseguir."

    d "Eu não consigo ter essa confiança."

    mc "Por que?"

    d "Isso é mais complicado do que você imagina..."

    mc "[d]..."

    menu:
        "Segurar a mão dela.":


            hide jazz_bar_diana

            $ diana_seducao += 2

            if d2_blacktie:

                show jazz_bar_mc angulo1_diana_mc_blacktie with dissolve

            elif d2_blazer:

                show jazz_bar_mc angulo1_diana_mc_blazer with dissolve
            else:


                show jazz_bar_mc angulo1_diana_mc_normal with dissolve

            d "[mc]."

            mc "Presta atenção."
        "Se manter afastado.":


            "..."

    mc "Não adianta eu querer falar sobre suas coisas, porque eu não sei o que tá rolando."

    mc "Você só ia me achar um besta."

    menu:
        "Mas você vai conseguir. Eu sei disso.":


            $ diana_seducao += 1

            mc "Só que eu sei que você vai conseguir. Você é uma garota inteligente, uma mulher incrível."

            mc "Eu sei que você vai conseguir."

            d "Eu agradeço por você querer me animar, [mc]. Obrigada."

            d "Mas não é assim. Não é uma coisa que envolve só a mim, entende?"

            d "Tem muita coisa em jogo aqui."

            d "Eu gostaria de poder te falar mais sobre isso, mas eu não posso."

            mc "Tudo bem. Tá tudo legal..."
        "Mas pode contar comigo. Eu vou estar aqui pra você.":


            $ diana_seducao += 2

            mc "Mas eu quero que você saiba que eu vou estar aqui pra você. Pode confiar em mim e contar comigo."

            mc "Mesmo não sabendo o que tá pegando, eu vou estar aqui pro que você precisar."

            mc "Eu quero ser alguém importante pra você."

            d "[mc]... Você..."
        "A gente precisa focar no lado bom da vida.":


            mc "Não adianta ficar quebrando a cabeça. Vamos focar no lado bom das coisas. A vida é muito boa."

            d "Essa forma simples de ver as coisas até me deixa mais alegre."

            mc "Claro. Não adianta ficar sofrendo! Vamos curtir!"

            d "Ok, vou tentar..."

    d "Sabe, [mc]... Você foi um cavalheiro esta noite."

    d "Eu tenho só mais um pedido pra você."

    mc "Cla-claro..."

    d "Eu posso olhar nos seus olhos?"

    mc "Ah?"

    d "Você me permite? Olhar bem seus olhos?"

    "Ixi... tô sentindo o clima entre a gente esquentando. Minha próxima resposta pode ser mais importante do que parece..."

    "O que eu respondo?"

    menu:
        "Sim.":


            mc "Sim, pode olhar."

            scene jazz_bar angulo2 with Dissolve(1.0)

            d "Com licença..."

            if d2_blacktie:

                show jazz_bar_mc angulo2_diana_mc_blacktie_juntos with Dissolve(1.0)

            elif d2_blazer:

                show jazz_bar_mc angulo2_diana_mc_blazer_juntos with Dissolve(1.0)
            else:


                show jazz_bar_mc angulo2_diana_mc_normal_juntos with Dissolve(1.0)

            d "..."

            mc "Di-Diana..."

            d "Você... tem olhos de uma pessoa boa, [mc]."

            d "Eu não sei se é uma coisa de outro mundo, ou só da minha cabeça. Mas eu consigo conhecer uma pessoa pelos olhos."

            mc "Sério?"

            d "Sim... eu consigo te entender. Você sofre pelos outros, só que não é só isso. Você ainda vai sofrer muito, [mc]."

            mc "Como assim?"

            d "Você carrega o fardo das pessoas..."

            d "Será que você aguenta carregar o meu também?"

            mc "[d], eu nã-"

            if diana_seducao >= 11:

                d "Eu quero te beijar."

                "Meu Deus! Ela tá se aproximando! O que eu faço?!"

                if priscila_namoro:

                    "Eu estou em um relacionamento sério com a [c]. Não seria certo... mas..."

                if sayuri_e4 == "namoro":

                    "Tem o beijo que eu dei na [s]. Eu sinto que ela arriscou tanto pra ficar comigo. E agora?"

                if julia_namoro:

                    "Eu escolhi ter algo sério com a [g] também."

                menu:
                    "Beijar ela":


                        $ diana_e2 = "seducao"

                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("diana_e2_seducao","diana","personagem")

                        "Eu quero beijar ela. Não importa o resto."

                        if d2_blacktie:

                            show jazz_bar_mc angulo2_beijo_blacktie with Dissolve(2.0)

                        elif d2_blazer:

                            show jazz_bar_mc angulo2_beijo_blazer with Dissolve(2.0)
                        else:


                            show jazz_bar_mc angulo2_beijo_normal with Dissolve(2.0)

                        pause

                        "..."

                        "O beijo dela é tão confiante. Como se ela tivesse certeza do que tá fazendo."

                        "A [d] parece uma garota tão forte, mas algo nela também me deixa triste..."

                        window hide

                        pause

                        if d2_blacktie:

                            show jazz_bar_mc angulo2_diana_mc_blacktie_juntos with Dissolve(1.0)

                        elif d2_blazer:

                            show jazz_bar_mc angulo2_diana_mc_blazer_juntos with Dissolve(1.0)
                        else:


                            show jazz_bar_mc angulo2_diana_mc_normal_juntos with Dissolve(1.0)

                        d "Você beija igual um adolescente, [mc]."

                        mc "Isso é bom ou-"

                        d "Não é nada."

                        mc "..."

                        d "Fazia muito tempo que eu não beijava alguém."

                        mc "Eu..."

                        d "Alguma coisa que eu não sei explicar me fez ter essa vontade."

                        d "[mc]..."

                        mc "Oi."

                        d "Tenha cuidado, tá?"

                        mc "Mas-"

                        d "Só me prometa que você vai tomar cuidado."

                        mc "Eu prometo."

                        d "Não carregue mais peso do que você aguenta. Não pense mais nos outros do que em você."

                        mc "[d]..."

                        d "Quero outro."



                        "Outro, é? E se eu apimentar um pouco as coisas?"

                        label diana2_premium1:

                            pass

                        menu:
                            "Tirar a blusa e agarrar ela":








                                "A Diana é uma mulher que sabe o que quer. Se eu mostrar confiança, tenho certeza que ela vai curtir."

                                scene black with dissolve

                                mc "E se eu tiver mais que um beijo pra você?"

                                d "Hm?"

                                scene diana2_img1 with Dissolve(1.0)

                                pause

                                d "Hmmm..."

                                mc "Só tá a gente aqui mesmo, né?"

                                d "É... mas deixa eu te falar um negócio antes de você continuar tirando as peças..."

                                mc "Fala."

                                d "Eu tô gostando de onde as coisas tão indo. Você parece saber o que você quer."

                                d "Só que tem um problema."

                                menu:
                                    "Você é casada?!":


                                        mc "Não vai me falar que você é casada!"

                                        d "Bom..."

                                        d "Não é casada, mas é um tanto parecido."
                                    "Qual o problema?":


                                        mc "Que problema?"

                                        d "Não é tão fácil de explicar."

                                d "Eu tenho uma relação com alguém aqui no Cassino."

                                mc "Ah... 'relação'? Tá de rolo?"

                                d "Não é amor e nem prazer. Mas é uma relação de qualquer forma."

                                d "Eu gostaria de poder encerrar tudo de uma vez, mas eu ainda não posso."

                                d "Não é que eu estou traindo ela. Você também não tá fazendo nada de errado ficando comigo."

                                mc "É só isso que importa. Você aceitou ficar comigo."

                                d "É... a questão é que essa pessoa pode ser um pouco ciumenta. As coisas podem complicar."

                                mc "Se essa pessoa descobrir que a gente ficou, é isso?"

                                d "Isso mesmo. E eu não quero trazer ainda mais problema para sua vida."

                                d "Eu não me sentiria bem se eu puxasse você pra esse rolo sem te dizer tudo antes."

                                d "E se você quiser parar aqui, eu vou entender completamente."

                                "Então a Diana tem alguém enrolado com ela... mas não é amor e nem prazer. O que ela quer dizer?"

                                "Se eu continuar com ela pode ser perigoso. Será que eu desisto?"

                                menu:
                                    "Eu não tenho medo":


                                        "Eu não vou desistir da [d] por causa de um ciúme idiota. E eu sei exatamente como responder."

                                        mc "Bom... eu acho que é melhor eu..."

                                        d "Eu sabi-"

                                        scene diana2_img2 with hpunch

                                        pause

                                        mc "Eu não vou deixar você escapar por causa de um ciúme."

                                        mc "Se você me escolher, eu sempre vou tá com você."

                                        d "[mc]..."

                                        d "Hmmm..."

                                        d "Você não faz ideia do que tá fazendo, mas eu vou aproveitar."

                                        d "Pega em mim. Vamos aproveitar esta noite."

                                        mc "É pra isso que eu tô aqui."

                                        scene diana2_img3 with Dissolve(1.0)

                                        pause

                                        d "Isso. Eu gosto quando você é decidido. O que você quer fazer?"

                                        mc "Eu vou passar a mão em tudo, Diana."

                                        d "Eu sei que você quer sentir minha bunda. Você não parava de olhar pra ela na praia."

                                        mc "Sua bunda, suas coxas... você é perfeita."

                                        d "Ahn... que bom que você gosta."

                                        "A Diana parece que tá no clima. Será que ela tá me dando o sinal verde pra continuar?"

                                        "Eu quero tanto pegar na bunda dela. Desde a praia... e agora... será? Ou é melhor não exagerar?"

                                        menu:
                                            "Eu preciso sentir ela":


                                                "Eu não vou perder essa chance."

                                                scene diana2_img4 with Dissolve(1.0)

                                                pause

                                                mc "Diana, é nosso primeiro beijo, mas eu não consigo me segurar."

                                                mc "Eu tenho que sentir sua bunda."

                                                d "Ahnng... quanta vontade..."

                                                mc "Você é muito gostosa. Deixa eu continuar pegando."

                                                d "Você tá animado demais pra nossa primeira vez. Tenha calma."

                                                mc "Não. Eu quero que você seja minha hoje."

                                                d "Que garoto mimado."

                                                scene black with dissolve

                                                mc surpreso "Diana!"

                                                scene diana2_img5 with Dissolve(1.0)

                                                pause

                                                d "Você já brincou demais por um dia."

                                                mc "N-não diga isso! A noite é uma criança!"

                                                d "Nós somos adultos, [mc]. Não precisamos ter pressa. Podemos continuar na próxima vez."

                                                mc "Você tá assim porque eu peguei em você?"

                                                d "Será que eu estou?"

                                                mc "Mas foi você quem disse que eu podia!"

                                                d "Eu não disse nada. Você entendeu o que queria pelo jeito."

                                                d "Eu vou deixar você ver, mas não pode tocar. O que você acha?"

                                                menu:
                                                    "Eu topo.":


                                                        mc "Ok... se é esse o jeito, eu topo."

                                                        d "Você quer olhar o que eu tenho por debaixo do vestido?"

                                                        mc "Eu quero!"

                                                        d "Hmm... então vem... pode olhar. Pode agachar e ver tudo o que tá escondido."

                                                        "Ela tá me provocando..."

                                                        scene diana2_img6 with Dissolve(1.0)

                                                        pause

                                                        mc "A-ah!"

                                                        d "Que foi? Viu algo que não esperava?"

                                                        mc "V-você tá sem calci-"

                                                        d "Xi... não precisa falar nada. O que você achou?"

                                                        "Caraca, que atrevida..."

                                                        mc "Eu acho que você tá brincando demais comigo. Eu não sei se eu vou aguentar."

                                                        d "Você não tem controle?"

                                                        mc "Você tá abusando."

                                                        d "Então tá bom. Chega."

                                                        scene black with dissolve

                                                        scene diana2_img7 with Dissolve(1.0)

                                                        pause

                                                        d "Eu pensei que você fosse um homem de verdade. Mas se você não consegue se controlar, então não adianta."

                                                        mc "Por que você tá fazendo isso comigo?"

                                                        d "Eu tô me divertindo. Só isso."

                                                        mc "Aah... se divertindo às minhas custas?!"

                                                        d "Mas você não tá gostando?"

                                                        mc "Tô, mas é que... você sabe..."

                                                        d "O problema é que você tá pensando demais no que você não tem ao invés de curtir o que você tem."

                                                        d "As pessoas costumam ser infelizes porque elas só conseguem ver o que elas queriam e não têm."

                                                        d "Ao invés de aproveitar tudo o que elas têm à disposição. Querer mais não é ruim, mas será que a gente não quer demais?"

                                                        mc "Você tem razão."

                                                        d "Será que você entendeu mesmo?"

                                                        mc "Eu entendi. Eu vou aproveitar."

                                                        d "Então vamos tentar... Ah... vem aqui, vem."

                                                        scene diana2_img8 with Dissolve(1.0)

                                                        pause

                                                        "Ah..."

                                                        d "Gostou?"

                                                        mc "Adorei."

                                                        d "Tá aproveitando?"
                                                        scene dnew_ani02 with Dissolve(1.0)
                                                        mc "Tô..."

                                                        "Eu vou acabar explodindo assim."

                                                        d "Parece que você entendeu mesmo... eu fiquei com vontade de te recompensar. Você quer?"

                                                        mc "Claro."

                                                        d "Então olha aqui..."

                                                        scene diana2_img9 with Dissolve(1.0)

                                                        pause

                                                        d "Tá vendo melhor?"

                                                        mc "Eu tô vendo tudo!"

                                                        d "Aah... que bom... pode olhar..."

                                                        mc "Só olhar?"

                                                        d "Só olhar... ahnn... você não pode... mais que isso... hmm..."

                                                        window hide

                                                        pause
                                                        scene dnew_ani05 with Dissolve(1.0)
                                                        "Caralho eu tô durasso demais! Por que ela tá fazendo isso?!"

                                                        "Eu não sei se eu vou aguentar! Eu preciso! Eu tô perdendo a cabeça!"

                                                        menu:
                                                            "Pegar nela":


                                                                mc "Diana! Perdão! Eu não consigo!"

                                                                d "Hm?!"

                                                                scene diana2_img10 with vpunch

                                                                pause

                                                                d "Aaii!"

                                                                mc "Eu preciso sentir você!"
                                                                scene dnew_ani03 with Dissolve(1.0)
                                                                d "[mc]!"

                                                                mc "Eu recompenso você com o melhor sexo oral da sua vida!"

                                                                d "Ah! Me solta!"

                                                                show black with vpunch

                                                                mc surpreso "Diana! Desculpa!"

                                                                scene diana2_img11 with Dissolve(1.0)

                                                                pause

                                                                d "Um homem de verdade é aquele que mantém sua palavra."

                                                                mc "Eu tentei! Só que voc-"

                                                                d "Não conseguir se controlar e depois colocar a culpa nos outros é infantil. E eu não quero me relacionar com uma criança."

                                                                d "Se você quer ver isso indo pra frente... acho bom você aprender a cumprir com suas promessas."

                                                                mc "E-eu vou fazer isso. Você vai ver."

                                                                d "Você é um cara especial, [mc]. Não deixe a luxúria destruir o que você tem de melhor."

                                                                mc "Ok. Mas me dá uma chance!"

                                                                d "Só se você prometer que vai fazer melhor da próxima."

                                                                mc "Com certeza. Você é incrível, [d]. Só que da próxima vez deixa eu fazer alguma coisa pelamor!"

                                                                d "Se da próxima vez a gente estiver no meu quarto, só nós dois, e você mostrar que melhorou... é possível."
                                                            "Fechar os olhos":


                                                                "Se continuar assim eu vou pular nela!"

                                                                show black with vpunch

                                                                mc "É demais pra mim! Eu não consigo!"

                                                                d "Ah... eu sou gostosa demais, é isso?"

                                                                mc "É! Se eu continuar olhando, eu vou!"

                                                                d "Parece que você aprendeu mesmo. Se você não consegue se controlar, faça o que tem que fazer."

                                                                mc "Eu tô fazendo!"

                                                                d "Hm-hmm... Agora pode abrir."

                                                                mc "Sério?!"

                                                                scene diana2_img11 with Dissolve(1.0)

                                                                pause

                                                                d "Um homem de verdade é aquele que mantém sua palavra. Eu gostei de ver isso em você."

                                                                d "Não conseguir se controlar e depois colocar a culpa nos outros é infantil. E eu não quero me relacionar com uma criança."

                                                                d "A gente vai ter futuro assim, [mc]. Espero que você tenha se divertido também."

                                                                mc "Com certeza. Você é incrível, [d]. Só que da próxima vez deixa eu fazer alguma coisa pelamor!"

                                                                d "Huhu... se da próxima vez a gente estiver no meu quarto, só nós dois, e você continuar sendo esse homem... eu acho que pode rolar, sim."

                                                        mc "Não vejo a hora!"

                                                        menu:
                                                            "Agachar e ver ela indo":


                                                                "Só uma última olhadinha..."

                                                                scene diana2_img12 with Dissolve(1.0)

                                                                pause

                                                                d "Você não tem dignidade mesmo, hm?"

                                                                mc "Deixa eu ver essa delícia..."

                                                                d "Hmm..."
                                                            "Manter a postura":


                                                                "Eu tenho que me segurar."
                                                    "Melhor a gente parar.":


                                                        mc "Se as coisas tão indo rápido demais melhor a gente parar aqui."

                                                        d "Excelente decisão, [mc]."

                                                        mc "Você disse... a gente vai ter tempo."

                                                        d "Concordo."
                                            "Não quero exagerar":


                                                "Tá bom onde a gente chegou..."

                                                d "Hmm... delícia..."

                                                mc "Você que é."
                                    "Melhor pular fora":


                                        mc "Eu... não tá na hora de entrar num tipo de problema desses."

                                        d "E é um problema grande. Isso eu sei."

                                        mc "Mas não vai ser sempre assim. Eu quero lutar por você."

                                        d "Vamos ver o que o futuro reserva para nós."

                                        mc "Com certeza."

                                d "Eu gostei muito da nossa noite."

                                mc "Eu também."

                                d "Eu vou te escrever de novo. Nossa parceria está só começando."

                                mc "Ela vai ser de grande proveito pra nós dois."

                                d "Com certeza."

                                d "Boa noite, [mc]."

                                mc "Até, [d]."

                                d "Não esquece do meu beijo... e de outras coisas..."

                                mc "Não vou..."

                                scene black with dissolve

                                jump diana_e2_final_nal
                            "Melhor ir devagar":


                                "Um beijo pra hoje é mais que suficiente..."

                                mc "Vem aqui."

                                if d2_blacktie:

                                    show jazz_bar_mc angulo2_beijo_blacktie with Dissolve(2.0)

                                elif d2_blazer:

                                    show jazz_bar_mc angulo2_beijo_blazer with Dissolve(2.0)
                                else:


                                    show jazz_bar_mc angulo2_beijo_normal with Dissolve(2.0)

                                pause

                        jump diana_e2_final
                    "Se afastar":


                        scene jazz_bar angulo1 with hpunch

                        if d2_blacktie:

                            show jazz_bar_mc angulo1_blacktie_normal with dissolve

                        elif d2_blazer:

                            show jazz_bar_mc angulo1_blazer_normal with dissolve
                        else:


                            show jazz_bar_mc angulo1_normal_normal with dissolve

                        mc "De-desculpa, [d]..."

                        d "..."

                        show jazz_bar_diana angulo1_diana_explicando with dissolve

                        d "Não tem o que se desculpar, [mc]."

                        d "Se você não se sente atraído por mim, não adianta forçar nada."

                        d "Nosso acordo não envolve sentimentos. Não se preocupe..."

                        mc desculpa "..."

                        jump diana_e2_amizade
            else:


                label diana_e2_amizade:

                    $ diana_e2 = "amizade"

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("diana_e2_amizade","diana","personagem")

                scene jazz_bar angulo1 with Dissolve(1.0)

                show diana exibida with dissolve

                d "..."

                d "Eu sinto que a gente é parecido, [mc]."

                mc desconfiado "Parecido como?"

                d "Nós dois somos forçados a fazer algo que não queremos."

                d "A gente não aguenta o que temos que fazer, mas odiamos ainda mais o que faríamos se não tivéssemos isso."

                mc "Não sei se-"

                d "Digo, somos amaldiçoados pelas circunstâncias, mas seríamos ainda mais sem elas."

                mc concentrando "Não sei se eu tô acompanhando."

                show diana ola with dissolve

                d "Talvez um dia você entenda o que eu quero dizer."

                d "Espero que mais cedo do que tarde."

                mc zerado "Tenho a impressão que as pessoas vivem me ameaçando de alguma forma..."

                d "Não estou te ameaçando {i}rsrs{/i}"

                d "Não seja bobo."

                d "Eu adorei sua companhia hoje. Obrigada mesmo por me ouvir cantar."

                mc normal "Foi um prazer. De verdade."

                d "Um dia... talvez um dia eu te conte sobre essa música."

                mc "Estou ansioso."

                jump diana_e2_final
        "Não.":


            mc "Me desculpe, [d]. Mas eu não me sinto confortável."

            d "Não esquente. Eu te entendo..."

            jump diana_e2_amizade

label diana_e2_final:

    scene jazz_bar angulo1 with Dissolve(1.0)

    if diana_e2 == "seducao":

        show diana provocando with dissolve
    else:


        show diana ola with dissolve

    d "Eu gostei muito da nossa noite."

    mc charmoso "Eu também."

    d "Eu vou te escrever de novo. Nossa parceria está só começando."

    mc normal "Ela vai ser de grande proveito pra nós dois."

    d "Com certeza."

    d "Boa noite, [mc]."

    mc "Até, [d]."

    hide diana with dissolve

    if diana_e2 == "seducao":

        d "Não esquece do meu beijo."

        mc envergonhado "Não vou..."

    label diana_e2_final_nal:

        "Hora de voltar pra casa. Já tá tarde."

    scene black with dissolve

    scene cidade angulo_1_noite with Dissolve(1.0)

    "Hoje foi um dia e tanto."

    "O cassino, o lance com a [d]."

    "A música dela. Foi tão bonita, mas algo nela me deixou apreensivo. Foi emocionante, foi forte."

    "E aquela letra? Eu queria poder ouvir de novo pra entender melhor..."

    "Ela sem dúvidas é o que chamam de guerreira. Ela parece tão certa do que tá fazendo..."

    if diana_e2 != "horrivel":

        mc desculpa "Mas lá no bar... Ela pareceu outra pessoa uma hora."

        "Sorte que eu fui atrás dela."

        if diana_e2 == "seducao":

            "E aquele beijo?"

            mc envergonhado "..."

            "Como as coisas vão avançar entre a gente?"

            "A [d] é uma garota incrível. Ela é linda, e o corpo..."

            mc tarado "Só de pensar..."

    "Hora de continuar. Ainda tem muita coisa pra acontecer."

    "Meu trabalho como paparazzo tá só começando. Fico imaginando as novas celebridades que vou conhecer."

    "E como vai evoluir minha relação com todas essas pessoas incríveis que eu já conheço?"

    mc charmoso "Fico empolgado só de pensar."

    $ tempo = 4
    $ v13_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v13_fim","diana","personagem")

    jump call_cidade

label diana_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("d1_save", extra_info="d1_save")

    $ estou_na_cidade = False

    $ diana_conheceu = True

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você só precisa não ser um idiota. Por que você recusaria, certo?."



        p rindo "E aí? Você vai preferir a pauta ou só vai ser um babaca mesmo? Aqui, você decide! Boa sorte!"

    "..."

    "É muito bom morar perto da praia."

    "Se eu pudesse, acho que vinha aqui todo dia."

    if v6_fim:

        "Sempre que eu ando por este trecho da praia eu me lembro daquele dia com a [c]."

        "Caraca. Deve ter sido o dia mais intenso da minha vida."

    "Todos na redação vivem falando que esta ilha tá cheia de celebridade."

    "Por enquanto eu não encontrei tantas assim como eu esperava."

    if not sayuri_evento1_check:

        "Eu conheci a [s] que é a principal atleta do país."

    "Conheci a [c], obviamente. Que é a grande modelo teen da atualidade."

    if not nathan_e1 == "nada":

        "Tem o [n] também. Eu acabei conhecendo ele por causa da [j]."

        "Mas ele ainda não é tão famoso. Mas se a [j] tá de olho nele, com certeza ele tem potencial."

    "Que outras celebridades será que eu..."

    scene praia dia with hpunch

    mc surpreso "Ai!"

    "Chutei alguma coisa..."

    scene diana tomando_sol with Dissolve(3.0)

    pause

    "Mulher" "..."

    "Caraca... Eu chutei a cadeira dessa mina..."

    "Caralho! Que mina gata!"



    label diana1_premium1:

        pass

    menu:
        "Secar ela":








            "Uma olhadinha rápida não vai dar nada..."

            scene black with dissolve

            scene diana1_img1 with Dissolve(1.0)

            pause

            "Minha nossa..."

            "Se é esse o tipo de gente que vem nessa praia, ter vido pra ilha vai ser a melhor decisão da minha vida."

            "Qual minha chance com uma mulher dessa? Deve ser perto de zero. Talvez negativo..."

            "Pelo menos eu posso olhar..."

            window hide

            pause

            "Ok... será que é demais querer ver mais um poquinho?"

            "Se ela acordar ela vai gritar e eu vou ser um tarado pra sempre..."

            menu:
                "Chegar mais perto":


                    "Eu vou dar uma olhadinha... se for pra morrer por secar essa gata, eu morro feliz."

                    scene diana1_img2 with Dissolve(1.0)

                    pause

                    "Amigo..."

                    "Eu tô tão perto... se ela tivesse o sono mais leve com certeza ela ia acordar."

                    "Certeza que eu tô abusando... mas será que eu sou um doido que sente prazer no perigo?"

                    "Sei lá, mas ficar olhando pra ela assim tá me deixando excitado pra caralho..."

                    "Certeza que ela tá sentindo o calor do meu corpo... eu tô colado nela."

                    "E se alguém passar por aqui e me ver assim?{w=0.5}"

                    scene black with vpunch

                    "A-ah!!!"

                    "Ela acordou!"

                    scene diana1_img3 with Dissolve(1.0)

                    pause

                    mc "D-des..."

                    mc "Hm? Ela só se ajeitou..."

                    "M-mas que é isso?! Que pose é essa?!"

                    "Ela abriu as pernas pra mim assim?!"

                    "Agora eu tô viajando... por que ela ia abrir as pernas pra mim?"

                    "Mas ia ser muito quente pensar que ela tá brincando comigo..."

                    "Tô ficando duro pra caralho de pensar nessa possibilidade... e se ela for uma exibicionista?"

                    "Ela pode sentir prazer de ter alguém olhando pra ela assim."

                    "???" "Hm-hmmm..."

                    "A-ah!!!"

                    scene diana1_img4 with Dissolve(1.0)

                    pause

                    mc "!!!"

                    "A-a-a-...."

                    "Ela se mexeu tanto que o biquíni..."

                    "Isso é demais pra mim... parece que ela tá me provocando de verdade!"

                    "O que eu posso fazer por você, moça? Vou ficar olhando bastante... pra você se divertir também."
                    scene dnew_ani01 with Dissolve(1.0)
                    "Se ela fosse famosa eu podia tirar uma foto com o celular... e vender pra revista. Podia até ser uma pauta!"

                    "Eu tô viajando demais."

                    "Só vou curtir um peitinho e dar o fora daqui o mais rápido possível."

                    window hide

                    pause 1.0

                    scene diana1_img5 with vpunch



                    "Mulher" "Oi?"

                    mc surpreso "!!!"

                    "Mulher" "Que foi?"

                    mc "E-eu..."

                    menu:
                        "Melhor eu não falar nada e só continuar andando":


                            "Melhor eu ficar na minha e só continuar andando... talvez ela não saiba que eu... sei lá..."

                            "Mas o biquíni... e agora?"

                            "Mulher" "Não vai pedir desculpas?"

                            mc surpreso "Ah ah!"

                            mc envergonhado "Desculpa, foi sem querer."

                            mc "Pensei que você estivesse dormindo."

                            "Mulher" "E se eu tivesse? Você ficou... olhando?"

                            mc "C-claro que não!"

                            "Mulher" "Hmmm..."

                            mc "Algum problema?"
                        "Desculpa por chutar sua cadeira.":


                            mc desculpa "Desculpa por chutar a cadeira. Foi sem querer."

                            "Mulher" "Você não olha por..."

                            "Mulher" "Hmmm..."

                            mc desconfiado "Algum problema?"
                        "Desculpa incomodar, mas você é muito linda.":


                            mc charmoso "Desculpa interromper seu momento sozinha, mas só queria falar que você é muito linda."

                            "Mulher" "Nem aqui eu consigo paz?"

                            "Mulher" "Entendi, entendi. Você é um fã blá blá."

                            mc desconfiado "Fã?"

                            "Mulher" "Você não..."

                            "Mulher" "Hmmm..."

                            mc desconfiado "Algum problema?"

                    jump diana1_premium_continua
                "Melhor parar aqui":


                    "Nah. Tá bom. Eu já pude ver uma das mulheres mais lindas da minha vida."
        "Não sou um cuzão":


            "Nem. Isso seria muita sacanagem com ela."

            "Imagina o povo do Twitter como ia ficar."

    "Mas o que eu faço então?"



    menu:
        "Melhor eu não falar nada e só continuar andando":


            "Talvez ela esteja só dormindo."

            "Melhor eu ficar na minha e só continuar andando..."

            "Mulher" "Não vai pedir desculpas?"

            mc surpreso "Ah ah!"

            mc envergonhado "Desculpa, foi sem querer."

            mc "Pensei que você estivesse dormindo."

            "Mulher" "Hmmm..."

            mc desconfiado "Algum problema?"
        "Desculpa por chutar sua cadeira.":


            mc desculpa "Desculpa por chutar a cadeira. Foi sem querer."

            "Mulher" "Você não olha por..."

            "Mulher" "Hmmm..."

            mc desconfiado "Algum problema?"
        "Desculpa incomodar, mas você é muito linda.":


            mc charmoso "Desculpa interromper seu momento sozinha, mas só queria falar que você é muito linda."

            "Mulher" "Nem aqui eu consigo paz?"

            "Mulher" "Entendi, entendi. Você é um fã blá blá."

            mc desconfiado "Fã?"

            "Mulher" "Você não..."

            "Mulher" "Hmmm..."

            mc desconfiado "Algum problema?"

    label diana1_premium_continua:

        pass

    "Mulher" "Eu não, e você?"

    mc "Eu?"

    "Mulher" "Sim. Você que chutou minha cadeira."

    mc desculpa "Ah, sim. Tô legal. Só tava pensando aqui, distraído."

    "Mulher" "No que você tava pensando?"

    menu:
        "Estava pensando nas celebridades que eu conheço.":


            mc normal "Não é nada de mais. Coisa boba."

            "Mulher" "Que tipo de coisa boba?"

            mc "Você realmente tá interessada?"
        "...":


            mc envergonhado "..."

            "Mulher" "Que foi? É algum segredo?"

            mc normal "Não. Nada disso. Só achei estranho você perguntar isso pra um estranho."

    "Mulher" "Se não quiser falar, tudo bem. Pode continuar pensando na sua vida sozinho."

    "Mulher" "Ou você pode se sentar e conversar comigo."

    mc "Sentar e conversar parece mais interessante com certeza."

    "Mulher" "Pois então."

    "Essa moça parece interessada em conversar comigo."

    "Aconteceu a mesma coisa quando conheci a [c]. Ela até me chamou de 'gato'."

    "Só que eu nunca tive sorte com as garotas... Será que eu fiquei atraente de uma hora pra outra?"

    "Mulher" "Então?"

    mc charmoso "Opa. Deixa eu sentar na areia aqui do seu lado."

    "Mulher" "Perfeito."

    scene diana protetor with Dissolve(3.0)

    pause

    "Caraca, que mina linda."

    "Mulher" "Você disse que ia pensando..."

    mc envergonhado "Ah, sim. Não sei se isso vai te interessar. Não quer falar de outra coisa?"

    "Mulher" "Deixa eu decidir se é interessante ou não."

    "Mulher" "Você vende drogas ou alguma coisa assim? Não é o fim do mundo."

    mc surpreso "Não, nada disso!"

    mc desculpa "Ok. Eu só tô um pouco preocupado porque eu achei que ia encontrar mais celebridades."

    "Mulher" "Quê? Que tipo de preocupação é essa?"

    mc "Parece estranho, mas é que isso é muito importante pra mim especificamente. É que eu trabalho como paparazzo."

    mc "Se eu não conseguir informações quentes sobre celebridades não vou conseguir me manter no emprego."

    "Mulher" "Espera..."

    scene praia dia with Dissolve(1.0)

    mc desconfiado "Opa."

    show diana b_analisando with dissolve

    "Mulher" "Você é um paparazzo?"

    mc "Isso mesmo. Que que tem?"

    "Mulher" "Você trabalha na revista de fofoca que tem aqui na ilha?"

    mc normal "Isso mesmo."

    "Mulher" "Como é seu nome?"

    mc "[mc]."

    "Mulher" "Não. Seu nome completo."

    label diana_e1_analise:

        mc "[mcc]."

    "Mulher" "Hmmm..."

    if priscila_atencao > 0:

        "Mulher" "Eu já li esse nome em alguma das edições. Pera..."

        "Mulher" "Foi você quem descobriu que a [cc] iria estrelar um filme, não foi?"

        jump diana_e1_final

    elif sayuri_atencao > 0:

        "Mulher" "Eu já li esse nome em alguma das edições. Pera..."

        "Mulher" "Foi você quem descobriu que a [sc] treinava no templo, não foi?"

        jump diana_e1_final

    elif nathan_atencao > 0:

        "Mulher" "Eu já li esse nome em alguma das edições. Pera..."

        "Mulher" "Foi você quem descobriu o modelo [nc], não foi?"

        jump diana_e1_final
    else:


        show diana b_discorda with dissolve

        "Mulher" "Não. Achei que tinha, mas nunca li nada que você tenha escrito."

        "Mulher" "Quando você publicar alguma coisa venha falar comigo. Talvez eu tenha algo pra você."

        "Mulher" "Até."

        hide diana with dissolve

        "Eita. O que será que ela quis dizer?"

        "Ela quer que eu publique alguma coisa na revista... E agora?"

        "Será que eu devo entregar a [s] ou a [c] pra poder continuar falando com essa garota?"

        "Bom... De uma forma ou de outra vou ter que entregar alguém pro chefe não me despedir."

        "Assim que eu entregar algo pra ele eu volto a falar com ela."

        "..."

        "Caraca. Andei pra caramba. Melhor voltar pra cidade."

        scene black with Dissolve(1.0)

        "Minhas pernas tão me matando..."

        $ tempo += 1
        $ diana_conheceu = True

        jump call_cidade

    label diana_e1_final_pre:

        scene praia dia with Dissolve(1.0)

        "Opa! Aquela mulher está tomando sol aqui de novo. Que sorte!"

        "Vamos ver se eu consigo algo com ela desta vez."

        mc normal "Bom dia."

        "Mulher" "Ah. É você..."

        show diana b_analisando with dissolve

        "Mulher" "Como é seu nome mesmo?"

        jump diana_e1_analise

    label diana_e1_final:

        $ iconchefe += 1

        mc surpreso "Co-como você sabe?!"

        "Mulher" "Eu sou uma leitora antiga da sua revista."

        mc desconfiado "Mas a ponto de decorar o nome dos paparazzi? Ainda mais o meu que tô começando agora."

        show diana b_discorda with dissolve

        "Mulher" "Você me pegou."

        "Mulher" "Digamos que eu tenha um interesse no trabalho que você e seus amigos paparazzi desenvolvem."

        mc "Interesse?"

        "Mulher" "Sim. É algo bem simples de entender na verdade."

        show diana b_analisando with dissolve

        "Mulher" "Aparentemente você não me conhece, mas eu sou uma celebridade também."

        mc surpreso "Quê?!"

        "Mulher" "Sim. Eu sou uma cantora que se apresenta no Cassino da ilha. Você já foi lá?"

        mc normal "Ainda não."

        "Mulher" "Bom, você precisa ter algum dinheiro pra ver meus shows... e aparentemente você não tem."

        mc zerado "Tá tão na cara assim?"

        "Mulher" "Sim."

        mc "..."

        "Mulher" "Mas você é atraente, preciso dizer. Alguma coisa em você me chamou a atenção."

        mc envergonhado "A é?"

        "Mulher" "Não precisa ficar com vergonha. Estou sendo sincera."

        "Mulher" "Mas não vamos fugir do assunto."

        mc normal "Verdade."

        "Mulher" "Bom... O que eu quero é expandir meus shows para outros lugares. Não quero ficar no Cassino pra sempre."

        "Mulher" "E pra conseguir isso vou precisar de alguma mídia. Preciso ficar conhecida fora da ilha."

        mc charmoso "E aparecer na revista seria perfeito pra você."

        "Mulher" "Exatamente."

        "Mulher" "Então temos um acordo?"

        mc desconfiado "Acordo?"

        show diana b_discorda with dissolve

        "Mulher" "Agora que eu comecei a achar você mais espertinho..."

        mc serio "Espera. Você quer dizer que quer que eu publique algo sobre você na revista?"

        "Mulher" "Exatamente."

        "Mulher" "Será benéfico para ambos. Eu terei a mídia que eu preciso e você terá pautas para publicar."

        "Mulher" "Não era justamente por isso que você estava preocupado?"

        mc "Espera..."

        "Ela tem razão."

        "Se eu concordar com ela eu vou ter pautas pra entregar pro chefe, e ainda vou poder continuar vendo ela."

        "Se eu recusar, provavelmente ela não vai querer nada comigo."

        "Não vejo por que não aceitar."

        "Só que a escolha parece fácil demais... Eu sinto um calafrio estranho quando minhas decisões parecem fáceis demais."

        "Mulher" "E então? Já pensou?"

        "Mulher" "Temos um acordo?"

        menu:
            "Não vou aceitar o acordo.":


                mc desculpa "Desculpa, mas não vou aceitar o acordo."

                show diana b_discorda with dissolve

                "Mulher" "Como assim? Por quê?"

                mc "As pautas que eu publico sou em quem escolhe. Não quero garantir nada pra você."

                "Mulher" "Tudo bem. A escolha é sua, mas parece que você está fazendo isso por ser cabeça dura."

                "Mulher" "Tem certeza?"

                "Será que estou deixando de aceitar um acordo bom por medo?"

                "E agora?"

                show black with dissolve

                p lecionando "Recusar o convite da [d] vai impedir que você veja os próximos eventos dela."

                p "Você também poderá ficar sem encontrar outros personagens que estão ligados à história dela."

                p "Se esta é sua primeira vez jogando, não recomendo deixar essa oportunidade passar."

                hide black with dissolve

                p rindo "Mas no fim é você quem escolhe."

                menu:
                    "Não vou aceitar. Não insista.":


                        $ diana_e1 = "recusou"

                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("diana_e1_recusou","diana","personagem")

                        mc serio "Eu tomei minha decisão. Por favor, não insista."

                        "Mulher" "Certo."

                        "Mulher" "Desejo sorte na carreira e se tiver dinheiro pra visitar o Cassino, veja um de meus shows."

                        mc normal "Combinado. Irei sim."

                        "Mulher" "Tenha um bom dia."

                        mc "Você também."

                        hide diana with dissolve

                        "Não sei se fiz o melhor, mas continuo mantendo minha integridade como paparazzo. Vou publicar o que quiser apenas."

                        "Bom. Minhas pernas tão cansadas de novo. Hora de voltar pro centro."

                        scene black with Dissolve(1.0)

                        $ tempo += 1

                        jump call_cidade
                    "Você tem razão. Não tenho nada a perder. Vou aceitar o acordo.":


                        mc serio "Você tem razão."

                        jump diana_e1_aceitou
            "Ok. Vou aceitar o acordo.":


                label diana_e1_aceitou:

                    $ diana_e1 = "aceitou"

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("diana_e1_aceitou","diana","personagem")

                    mc charmoso "Não tenho por que negar. Vou aceitar o acordo."

                    show diana b_divertida with dissolve

                    "Mulher" "Perfeito. Tenho certeza que nós dois vamos nos dar muito bem."

                    d "Meu nome é [dc]. Você pode me chamar só de [d]."

                    mc charmoso "Muito prazer."

                    d "Pra que a gente possa começar nossa parceria, tenho uma novidade quentíssima pra você."

                    mc surpreso "Legal!"

                    d "Meu novo single já está gravado e eu terei um show de lançamento daqui alguns dias."

                    d "Inclusive celebridades virão participar do show. Será um dos maiores concertos que já aconteceram na ilha."

                    d "A música ainda não vazou, então não vou te falar nada sobre ela ainda. Mas prometo te mandar mensagem."

                    mc normal "Isso realmente pode agradar o chefe. Pode deixar que vou passar pra ele."

                    d "É isso que eu espero do nosso acordo."

                    mc "Tá parecendo que nossa parceria vai ser muito boa."

                    d "E pra você ter certeza disso, tenho um presente pra você."

                    mc "Hm?"

                    scene black with dissolve

                    scene diana1_img6 with Dissolve(1.0)

                    pause

                    mc "Q-quê?! E-esse é meu presente?"

                    d "Você quer que seja?"

                    label diana1_premium2:

                        pass

                    menu:
                        "Eu quero.":








                            mc "Ah! É o t-tipo de presente que eu mais gosto."

                            d "Bom saber que você tem a mesma cabeça simples dos outros homens."

                            mc "Você acha?"

                            d "Eu ainda não conheci um homem que não fizesse qualquer coisa por uma mulher."

                            mc "Eu não sou assim. Só não vou deixar passar a oportunidade."

                            d "Haha... é isso que você diz pra você?"

                            mc "É sério."

                            scene diana1_img7 with Dissolve(1.0)

                            d "Então quer dizer que você não aceitaria atender um pedido meu pra pegar em mim?"

                            menu:
                                "Só pra isso, não.":


                                    mc "De jeito nenhum. Eu não aceitaria."

                                    d "Hmm... interessante..."

                                    mc "Não tá acreditando?"

                                    d "Se você diz eu acredito."
                                "Depende do pedido.":


                                    mc "Bom... depende do pedido, claro."

                                    d "Agora parece que você tá falando a verdade."

                                    mc "Mas é bem diferente."

                                    d "Minha teoria é que não importa o pedido, você aceitaria."

                            mc "Não, não. Você tá duvidando de mim."

                            d "Eu sei que você tava me olhando."

                            menu:
                                "De jeito nenhum.":


                                    mc "Não. Você tirou isso da sua cabeça. Eu tô olhando normal."

                                    d "Você não aproveitou que eu tô de biquíni pra ficar me secando, não, né?"

                                    mc "Nego veementemente."
                                "Você tá de biquíni!":


                                    mc "Você tava de biquíni! É pra olhar, né?!"

                                    d "Não seja ridículo. Qualquer mulher com um pingo de cabeça te daria um tapa por falar assim."

                                    mc "M-mas-"

                                    d "Eu não sou qualquer mulher. Ser olhada não me irrita. Não é esse o problema."

                                    mc "O que é então?"

                            d "Você continua fugindo da verdade."

                            mc "N-não."

                            scene diana1_img8 with Dissolve(1.0)

                            pause

                            mc "E-ei!"

                            d "Você quer dizer que se eu quisesse ficar com você aqui..."

                            d "Assim... agora... nessa praia deserta..."

                            mc "É... é..."

                            d "Você não ia me querer?"

                            mc "N-não é isso que eu falei."

                            d "Então você aceitaria qualquer coisa?"

                            mc "Q-qualquer coisa, não."

                            d "Hmmm..."

                            scene diana1_img9 with Dissolve(1.0)

                            pause

                            d "Será que você precisa de um pouquinho mais?"

                            d "Será que você vai conseguir deixar de curtir o que eu tenho pra você por que é cabeça dura?"

                            mc "O que que é?"

                            d "Tá ansioso pra saber?"

                            mc "Fala... n-não chega tão perto."

                            d "É segredo. Posso falar no seu ouvido?"

                            mc "Fala logo."

                            d "Primeiro você vai ter que me responder se você faria qualquer coisa ou não."

                            d "Se você aceitar... você vai sentir algo que você nem imagina. Hm?"

                            menu:
                                "Ok! Eu faço!":


                                    python:
                                        if renpy.android:
                                            renpy.block_rollback()

                                    mc "Eu faço!"

                                    d "A gente sempre soube disso, não é?"

                                    d "Você precisa ser mais verdadeiro com o que você sente, [mc]."

                                    mc "Beleza. agora fala."

                                    d "Seu presente..."

                                    scene black with dissolve

                                    pause

                                    scene diana1_img10 with Dissolve(1.0)

                                    pause

                                    mc "A-ahn!"

                                    d "Hmmm..."

                                    mc "A-ah..."

                                    d "Gostou?"

                                    mc "..."
                                "Para tudo!":






                                    python:
                                        if renpy.android:
                                            renpy.block_rollback()

                                    mc "N-não! Eu disse que não!"

                                    d "Interessante... e surpreendente."

                            d "Mas não é esse seu presente."

                            mc "N-não?"

                            d "Vou te dar um {b}Cartão Silver{/b} do Cassino. Toma."

                            mc "Opa."

                            scene black with dissolve

                            scene diana1_img11 with Dissolve(1.0)

                            pause

                            "Ela tá sem a parte de baixo?!"

                            "E o que é isso que ela me deu?!"

                            mc "Silver?!"



                            d "Você nem sabe o que é isso, sabe?"

                            mc "Não..."

                            d "Cartão Silver é o terceiro melhor cartão que você pode ter como jogador do Cassino do Barão."

                            d "Você precisa ganhar mais de C$ 250 mil jogando pra receber um desses."

                            mc "QuêêÊ!?"

                            d "Pois é. Acima desses só existem os cartões {b}Gold{/b} e {b}Platinum{/b}."

                            d "Esse cartão vai te dar direito a usar as instalações do cassino, além de alguns outros benefícios..."

                            d "Se você jogar o suficente e conseguir um Gold Card, você terá ainda mais vantagens no Cassino do Barão."

                            mc "..."

                            mc "I-isso é incrível..."

                            d "Agora eu tenho que ir. Foi um prazer fazer negócio com você, [mc]."

                            d "Já estou ansiosa para ver minha matéria na sua revista. Espero que você cumpra sua parte."

                            mc "Pode deixar."

                            d "Certo. Até outra oportunidade."

                            mc "Até."

                            menu:
                                "Olhar por baixo da canga":


                                    "Só uma olhadinha..."

                                    scene diana1_img12 with Dissolve(1.0)

                                    pause

                                    "Mas que bunda... e coxa... e tudo..."

                                    d "Todos nós sabíamos que você não tinha mais dignadade sobrando, não é verdade?"

                                    mc "E-ei!"
                                "Deixar ela ir":


                                    "Melhor não correr esse risco dela ver e depois jogar na minha cara."

                                    window hide

                                    pause
                        "N-não.":


                            mc "N-não... eu não posso."

                            d "Que pena. Então eu tenho outra coisa aqui pra você."





                            d "Vou te dar um {b}Cartão Silver{/b} do Cassino."

                            mc surpreso "Silver?!"



                            d "Você nem sabe o que é isso, sabe?"

                            mc envergonhado "Não..."

                            d "Cartão Silver é o terceiro melhor cartão que você pode ter como jogador do Cassino."

                            d "Você precisa ganhar mais de C$ 250 mil jogando pra receber um desses."

                            mc surpreso "QuêêÊ!?"

                            d "Pois é. Acima desses só existem os cartões {b}Gold{/b} e {b}Platinum{/b}."

                            d "Esse cartão vai te dar direito a usar as instalações do cassino, além de alguns outros benefícios..."

                            d "Se você jogar o suficente e conseguir um Gold Card, você terá ainda mais vantagens no Cassino do Barão."

                            mc "..."

                            mc "I-isso é incrível..."

                            d "Agora eu tenho que ir. Foi um prazer fazer negócio com você, [mc]."

                            d "Já estou ansiosa para ver minha matéria na sua revista. Espero que você cumpra sua parte."

                            mc charmoso "Pode deixar."

                            d "Certo. Até outra oportunidade."

                            mc "Até."



                    scene black with dissolve

                    scene praia dia with Dissolve(1.0)

                    "Uou. Essa [d] parece uma mulher ambiciosa."

                    "Eu posso me dar muito bem na revista se eu conseguir me tornar um parceiro dela."

                    "E esse {b}Cartão Silver{/b} vai me dar acesso ao Cassino. Não vejo a hora de poder usar ele."

                    "Também tenho que pensar na melhor hora de usar a pauta que ela me deu."

                    "O melhor é sempre entregar pautas quando o chefe for me despedir."

                    "Mas se eu quiser entregar antes eu posso sempre visitar ele na redação e entregar de uma vez."

                    "Nossa, passei tempo demais no sol. Melhor voltar logo pro centro da ilha."

                    $ pautas += 1
                    $ diana_p1 = True

                    scene black with Dissolve(1.0)

                    "Tô parecendo um camarão..."

                    $ tempo += 1

                    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
