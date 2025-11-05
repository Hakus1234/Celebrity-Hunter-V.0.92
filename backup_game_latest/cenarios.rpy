label cenario_mercado:

    $ estou_na_cidade = False

    scene mercado geral with Dissolve(1.0)

    if tempo < 3:

        if mercado_1vez:

            jump thaynara_menu
        else:


            $ mercado_1vez = True

            "Este mercado 24 horas é bem legal."

            "Normalmente, eu só como pizza. Tanto no almoço como na janta é só pizza."

            "Por algum motivo pizza é muito barata aqui na ilha."

            python:
                if renpy.android:
                    cash = PythonSDLActivity.pegaCash()

            if cash == 0:

                "Infelizmente eu não tenho grana nenhuma pra poder comprar coisas saudáveis aqui."

                "Preciso arranjar outro trabalho pra complementar o que eu ganho na revista."

                "Onde será que tão precisando de alguém? Tô aceitando qualquer negócio..."
            else:


                "Agora que eu tô ganhando uma grana ajudando o [gar] vou poder vir aqui comprar coisas mais saudáveis."

                "Sair dessa vida de pizza vai ser muito bom."

            "Bom. Deixa eu ver se tem algo bacana aqui."

            scene mercado mesas with dissolve

            "Puxa, um lugar pra consumir no próprio mercado. Muito massa."

            "Quem sabe posso trazer alguém aqui no futuro."

            "..."

            "Bem legal mesmo."

            "Bom... Vou dar o fora. Não adianta ficar só olhando."

            "..."

            scene mercado caixa with Dissolve(1.0)

            "Vou sair antes que achem que eu roubei algu-"

            mc surpreso "!"

            show thaynara incerta with Dissolve(1.0)

            pause

            "Que-que-quem é essa garota?!"

            "Que roupa sexy. E o corpo dela é perfeito. Ela nem deve ter notado que tá mostrando a alça da calcinha..."

            "Ou será que é de propósito?"

            menu:
                "Não tenho nada pra falar com ela. Vou embora.":


                    "Não tenho nada pra falar com ela. Deixa eu dar o fora daqui."

                    jump call_cidade
                "Vou tentar puxar assunto.":


                    $ thaynara_conheceu = True

                    mc envergonhado "Olá. Tá calor, né?"

                    "Garota" "Sim! Calor pra caramba!"

                    mc "..."

                    show thaynara desconfiada with hpunch

                    "Garota" "Ei! Você tava olhando pra minha calcinha?!"

                    menu:
                        "Claro que não. Eu não faria algo assim.":


                            mc envergonhado "Não não. Eu não faria algo assim."

                            "Garota" "Hmmm... Ok, acredito em você, moço."

                            show thaynara bemvindo with Dissolve(1.0)

                            "Garota" "É que meu shorts fica caindo, e às vezes esqueço de arrumar."

                            mc "Entendi..."
                        "Você fica mais bonita com a calcinha aparecendo.":


                            $ thaynara_seducao += 1

                            mc charmoso "É que você fica muito mais linda com a calcinha aparecendo, muito mais sexy."

                            "Garota" "Você acha?"

                            mc "Com certeza. Eu adorei seu estilo."

                            show thaynara bemvindo with Dissolve(1.0)

                            "Garota" "Então tá. Vou parar de arrumar então. Obrigada, moço."

                            mc "Não tem por onde."

                            "Será que ela realmente comprou isso que eu falei?"

                    mc normal "Bom, vou indo nessa."

                    "Garota" "Tenha um bom dia, moço."

                    hide thaynara with dissolve

                    "Garota estranha... Eu tenho a impressão que ela é diferente de outras mulheres que eu tenho encontrado recentemente."

                    "Ela parece tão... pura e verdadeira..."

                    "Preciso juntar uma grana e voltar aqui fazer uma comprinha e tentar encontrar ela outras vezes."

                    scene black with Dissolve(1.0)

                    p lecionando "Essa garota é especial realmente. Algo nela não me cheira bem."

                    python:
                        if renpy.android:
                            cash = PythonSDLActivity.pegaCash()

                    p rindo "Para poder conhecer ela melhor, você precisa juntar {b}R$ 30{/b} para fazer uma compra no mercado."

                    if v10_fim:

                        if cash > 0:

                            p "Continue ajudando o [gar] a limpar o bar e logo você vai ter dinheiro para saber mais sobre essa garota estranha."

                            p "Para trabalhar no bar, é só ir até lá nos períodos da manhã e da noite."
                        else:


                            p "Você pode juntar grana ajudando o [gar] no bar. Fale com ele quando tiver a chance e trabalhe no bar."

                            p "O bar fica aberto de tarde ou de noite."
                    else:


                        p "Continue a história da [c] até o final e depois você poderá trabalhar no bar."

                        p "Continue sua jornada como paparazzo e muitas loucuras ainda vão acontecer enquanto você joga."

                    jump call_cidade
    else:


        "Aquela [t] não trabalha aqui essa hora. Melhor eu deixar pra fazer compra quando ela estiver aqui."

        "Normalmente ela tá aqui de {b}manhã{/b} e à {b}tarde{/b}."

        jump call_cidade

label cenario_praia:

    $ estou_na_cidade = False

    if tempo > 3:

        "A praia é fechada durante a noite. Não adianta ir até lá essa hora."

        mc zerado "Onde já se viu uma praia 'fechar'?"

        "Talvez eu devesse perguntar sobre isso pra alguém que manje mais da ilha do que eu."

        jump call_cidade

    "Ir para a praia vai usar um período do meu dia."

    "Será que eu vou lá?"

    menu:
        "Andar até a praia":


            "Vamos lá. É uma boa pernada até a praia."

            scene black with dissolve

            play music "audio/som_12_gaivota.mp3" noloop

            jump praia1
        "Vou deixar pra outra hora":


            jump call_cidade

    label praia:

        "..."

        if tempo == 1:

            play sound "audio/som_13_praia2.mp3"

            scene praia dia with Dissolve(1.0)

            "O som das ondas tem algum efeito terapêutico."
        else:


            play sound "audio/som_13_praia.mp3"

            scene praia tarde with Dissolve(1.0)

            "Toda vez que eu olho para o por do sol aqui eu sinto uma tranquilidade..."

        label praia_loop:

            "Hmmm... deixa eu pensar o que vou fazer."

            menu:
                "Andar pela praia":


                    if tempo == 1:

                        play sound "audio/som_13_praia.mp3"

                        scene mc praia_dia with Dissolve(1.0)

                        "Nesta hora o sol ainda tá fraquinho. É a hora ideal pra dar um passeio."

                        "Quem sabe não encontro algo interessante?"

                    elif tempo >= 2:

                        play sound "audio/som_13_praia2.mp3"

                        scene mc praia_tarde with Dissolve(1.0)

                        "Eu tenho muita sorte de poder morar nesta ilha."

                        "Olha só pra esta vista!"

                    "..."

                    "{b}Uma hora depois{/b}"



                    if tempo > 1 and (not diana_conheceu or diana_e1 == "nada"):

                        "..."

                        "Parece que tem dois homens conversando ali..."

                        "Homem empolgado" "Você ouviu o boato?"

                        "Homem negativo" "Boato? Isso é coisa de fofoqueiro..."

                        "Homem empolgado" "O pessoal do Robson tá falando que tem uma moça muito gata que vem tomar sol aqui de {b}manhã{/b}."

                        "Amigo negativo" "E eu com isso?"

                        "Homem empolgado" "É aquela cantora que tá fazendo mó sucesso no {b}Cassino{/b}."

                        "Amigo negativo" "Isso não muda em nada minha vida..."

                        "Amigo empolgado" "Mano! Tu é muito mala!"

                        "..."

                        "Então tem uma cantora de sucesso que vem aqui tomar banho de sol na parte da {b}manhã{/b}..."

                        "Eu preciso checar isso."

                        "..."

                        "Opa. Já tô de volta onde eu comecei."



                    elif tempo == 1 and not diana_conheceu and diana_e1 == "nada":

                        jump diana_evento1

                    elif tempo == 1 and diana_conheceu and diana_e1 == "nada":

                        jump diana_e1_final_pre



                    "Caraca. Andei pra caramba. Melhor voltar pra cidade."

                    scene black with Dissolve(1.0)

                    "Minhas pernas tão em matando..."

                    $ tempo += 1

                    jump call_cidade
                "Voltar para o centro da ilha":


                    "Não tenho mais nada pra fazer aqui."

                    $ tempo += 1

                    jump call_cidade

    label cenario_salao:

        stop sound

        $ estou_na_cidade = False

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cenario_salao","salao","cenario")

        if gina_bunda:

            "A [m] disse que nunca mais queria me ver..."

            "Eu ferrei tudo comendo a [gina]. Que bosta..."

            "Agora ela vai ser despejada e nunca mais vou poder ver ela."

            "Adeus, [m]..."

            jump call_cidade

        if tempo > 1:

            if mc_massagem == 6 and not compra_casa_evento:

                scene black with Dissolve(1.0)

                if not karli_p_tadaima:

                    "Ué... A porta tá fechada... Mas nessa hora era pra [m] ter aberto o salão."

                    "Será que aconteceu alguma coisa?"

                    "Melhor eu procurar por ela no Tadaima no período da manhã e ver o que aconteceu."
                else:


                    $ compra_casa_evento = True

                    "Continua fechado..."

                    "Ela não tá trabalhando no Tadaima também."

                    mc surpreso "Será que ela foi despejada?!"

                    scene black with Dissolve(1.0)

                    jump massagem_curso









                jump call_cidade

            elif mc_massagem == 6:

                scene black with Dissolve(1.0)

                if k7_continua and not k7_poscasa:

                    python:
                        if renpy.android:
                            casa = PythonSDLActivity.pegaCasa()

                    "Eu fiquei de ver o lance da casa e depois retornar pra [m]."

                    if casa:

                        "Agora que eu tô com meu apê novo. Finalmente vou poder deixar ela ficar um tempo comigo."

                        "Vou ligar pra ela e avisar."

                        "Smartphone" "Tuu... Tuuu..."

                        m "Funerária."

                        mc desconfiado "Quê?"

                        m "Sou eu, bobo. Que foi?"

                        mc zerado "..."

                        mc normal "É. Tenho uma surpresa pra você. Tem como você me encontrar na praça daqui a pouco?"

                        m "Uma meia hora. Pode ser?"

                        mc "Claro. Vou te esperar lá."

                        m "Até."

                        "Bora lá."

                        "..."

                        scene ilha parque with Dissolve(1.0)

                        "..."

                        "..."

                        "Faz mais de meia hora. Ela deve tá chegando."

                        show karli normal with dissolve

                        m "Fala aí, tranqueira."

                        mc normal "Opa."

                        m "Espero que seja algo muito bom, porque pra me fazer vir até aqui..."

                        mc "Você vai curtir. Bora."

                        jump k7_mostra_ap
                    else:


                        "Eu ainda não consegui pegar o apê novo com a [gina]. Não tenho um lugar que ela possa ficar."

                        "Eu bem que podia arranjar uma grana e pagar o lance da [gina] pra ela me passar o apê."

                        "Não é tão caro assim. Algum tempo trabalhando no bar e eu dou um jeito nisso. Vai ser massa demais ter a [m] um tempo em casa."

                        "Será que é melhor eu esperar um pouco mais antes de ligar pra [m] e a gente ficar juntos no novo apartamento."

                        "Ou será que é melhor desistir dessa ideia dela ficar em casa e deixar a [m] resolver o problema sozinha?"

                        "E agora?"

                        menu:
                            "Esperar um tempo antes de continuar vendo a [m]":


                                "Eu acho que vou pensar melhor nesse lance da casa antes de continuar a ver a [m]."

                                "A [m] tá contando comigo. Quando eu conseguir a grana, preciso ligar pra [gina] e fechar com ela o lance do apê."

                                "Bora continuar o dia agora."

                                jump call_cidade
                            "Deixar a [m] resolver o problema sozinha e continuar":


                                "Não tem como eu ajudar ela. Não vou conseguir a grana da [gina] mesmo."

                                "É uma pena, mas ela é grande. Não adianta eu ficar chorando por ela."

                                "Vou ligar pra ela e avisar."

                                "Smartphone" "Tuu... Tuuu..."

                                m "Funerária."

                                mc desconfiado "Quê?"

                                m "Sou eu, bobo. Que foi?"

                                mc zerado "..."

                                mc normal "É... eu tava querendo fazer um lance pra te ajudar, mas não vai rolar."

                                m "Relaxa, [mc]."

                                m "Mesmo assim, eu queria te encontrar na praça em uma meia hora. Pode ser?"

                                mc "Claro. Vou te esperar lá."

                                m "Até."

                                "Bora lá."

                                "..."

                                scene ilha parque with Dissolve(1.0)

                                "..."

                                "..."

                                "Faz mais de meia hora. Ela deve tá chegando."

                                show karli normal with dissolve

                                m "Fala aí, tranqueira."

                                mc normal "Opa."

                                jump k7_sem_ap

                elif k7_continua and k7_poscasa:

                    if dia >= dia_karli:

                        jump k7_final

                    mc desculpa "A [m] ainda não tá pronta pra voltar a dar aulas."

                jump call_cidade

            scene salao geral with Dissolve(1.0)

            if mc_massagem <= 3:

                "Este lugar tem um cheiro muito bom..."

            elif mc_massagem <= 6:

                "Mesmo vindo aqui várias vezes para as aulas, o cheiro do salão da [m] continua muito bom."
            else:


                "Tava com saudades do cheirinho deste lugar."

            if cenario_salao_1vez:

                $ m_nome = "Atendente"

            menu:
                "Chamar a [m]":


                    mc normal "Olá?"
                "Voltar outra hora":


                    "Melhor voltar uma outra hora."

                    jump call_cidade

            if massagista_parque and not priscila_cel_msg2_resposta_check:

                if not cenario_salao_1vez:

                    $ m_nome = "Karli"

                    call checa_logado from _call_checa_logado_8

                    python:
                        if renpy.android:
                            PythonSDLActivity.tempoAgora()

                    mc normal "Ei! [m]! Tá aí?!"

                    "..."

                    call anuncio from _call_anuncio_9





                    label karli_curso:

                        python:
                            if renpy.android:
                                mc_massagem_db = PythonSDLActivity.pegaMpontos()

                        scene salao geral with dissolve

                        show karli feliz with dissolve

                        m "Oi, [mc]. Já tá com saudades?"

                        m "O que manda?"

                        menu:

                            "Estou pronto pra continuar meu curso." if mc_massagem < 10:

                                if dia >= dia_karli:

                                    if mc_massagem >= 9:

                                        show karli preocupada with dissolve

                                        m "Temos que dar um jeito de pagar pelo salão."

                                        mc desculpa "Verdade..."

                                        mc normal "Mas eu vou ter uma ideia. Pode confiar."









                                        show karli normal with dissolve

                                        m "Claro que vai. Você vai me salvar, enquanto eu fico tomando banho na banheira. Meu herói!"

                                        mc zerado "..."

                                        mc desconfiado "Quando eu pensar em algo eu volto. Vou ficar pensando em coisas."









                                        m "É pra ficar mesmo. Xau, juvenal."

                                        hide karli with dissolve

                                        mc zerado "Juvenal..."

                                        scene black with Dissolve(1.0)

                                        p lecionando "A história da [m] continua em alguma das próximas atualizações."

                                        p "Fique de olho em nosso Facebook e Instagram @celebrityhuntergame para acompanhar as novidades."

                                        p "Ei! Não me olhe assim! É tudo culpa do cara que faz o jogo! Reclama com o RB!"

                                        jump call_cidade

                                    if mc_massagem < mc_massagem_db:

                                        "{b}Você já esperou pela aula de massagem [mc_massagem_db] vezes. Mas neste gameplay você teve apenas [mc_massagem] aulas.{/b}"

                                        "{b}Como não é preciso esperar duas vezes pela mesma atividade, você pode continuar a história sem esperar novamente.{/b}"

                                        jump massagem_curso

                                    call checa_tempo from _call_checa_tempo_10

                                    m "Certo..."

                                    python:
                                        if renpy.android:
                                            mtempo = PythonSDLActivity.checkMtempoNext()

                                    if mtempo:

                                        m "Então fechou."

                                        python:
                                            if renpy.android:
                                                PythonSDLActivity.setMtempoNext()

                                        jump massagem_curso
                                    else:


                                        show karli satisfeita with dissolve

                                        m "Eu ainda não estou pronta. Você sabe que apressar a arte pode ter resultados horríveis para o mundo."

                                        mc zerado "Ok. Entendi. Não precisa inventar moda."

                                        scene black with dissolve

                                        p lecionando "Oi. Você só poderá continuar o curso {b}8 horas reais{/b} depois da sua aula anterior."

                                        p "Use o app Relógio no celular do [mc] para ver que horas você poderá fazer sua próxima aula."

                                        p "Ah! Você também pode liberar a próxima aula usando {b}Celebrity Coins{/b}."

                                        python:
                                            if renpy.android:
                                                persistent.coins = PythonSDLActivity.pegaMoedas(0)

                                        if persistent.coins >= 300:

                                            "{b}Liberar a próxima aula de massagem usará 300 Celebrity Coins{/b}"

                                            menu:
                                                "Liberar aula de massagem":


                                                    python:
                                                        if renpy.android:
                                                            PythonSDLActivity.avancaMasTempo()

                                                    $ renpy.block_rollback()

                                                    play sound "extra/carta.mp3"

                                                    "{b}Você usou 300 Celebrity Coins para liberar a próxima aula de massagem{/b}"

                                                    p rindo "Agora eu vou levar o [mc] para o começo da conversa para você inciar sua aula com a [m]."

                                                    $ renpy.block_rollback()

                                                    jump karli_curso
                                                "Agora não. Vou esperar o tempo":


                                                    p rindo "Você escolheu não liberar a próxima aula de massagem agora, né? Sem problemas!"
                                        else:


                                            p "Você precisa de ao menos {b}300 Celebrity Coins{/b} para liberar a exploração."

                                            p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja. Acesse o Menu para saber mais."

                                        p "Xau xau!"

                                        jump karli_curso





                                        p "Você pode conseguir moedas facilmente vendo vídeos na {b}Loja de Cartas{/b} ou comprando na nossa {b}Loja{/b}."

                                        show seta with vpunch

                                        p "Só clicar no botão {b}Menu{/b} aqui no canto inferior direito."

                                        p "Você também pode esperar as {b}8 horas{/b} terminarem. Ainda estaremos por aqui!"

                                        jump karli_curso
                                else:


                                    show karli meudeus with dissolve

                                    m "Eu disse que é uma vez por dia. Você não ouviu nada?"

                                    mc envergonhado "É que eu tava ansioso."

                                    m "Não me interessa. Agora tchau tchau."

                                    hide karli with dissolve

                                    mc surpreso "Ei! Não precisa me empurrar!"

                                    jump call_cidade
                            "Eu volto mais tarde.":








                                mc normal "Lembrei que tenho outras coisas pra resolver. Volto depois."

                                m "Tá. Até depois."

                                jump call_cidade
                else:


                    jump karli_1vez
            else:


                mc normal "Tem alguém aí?"

                "..."

                mc serio "Oiii! Tem cliente!"

                "..."

                $ m_nome = "Voz Feminina"

                m "Tô ocupada agora! Volta outra hora!"

                mc desconfiado "..."

                if massagista_negado == 0:

                    "Bom. Vou voltar outra hora..."

                    "Mas que tipo de atendente fala desse jeito?"

                    $ massagista_negado += 1

                elif massagista_negado == 1:

                    "De novo isso?"

                    mc serio "É a segunda vez que você fala isso pra mim!"

                    m "E daí? Volta outra hora!"

                    mc bravo "..."

                    "Eu tenho a impressão que ela não quer me atender de propósito..."

                    "Vou ter que voltar outra hora..."

                    $ massagista_negado += 1

                elif massagista_negado == 2:

                    mc bravo "Tá brincando?! É a terceira vez que eu venho aqui e você fala a mesma coisa!"

                    m "Você quer que eu fale o quê se eu tô ocupada?"

                    mc "..."

                    m "Eu tô semi nua aqui. Quem sabe você não tem mais chance de falar comigo em outro lugar?"

                    mc surpreso "Se-semi nua?!"

                    "Falar com ela em outro lugar? O que ela quer dizer com isso?"

                    "Talvez ela esteja em outros lugares em outros períodos do dia. Talvez eu devesse procurar por ela..."

                    $ massagista_negado += 1
                else:


                    mc zerado "Não sei porque eu continuo vindo aqui..."

                    m "Agora você tá entendendo a mensagem..."

                    mc "..."

                    m "Você vai ter mais chance de falar comigo no parque durante a noite e no restaurante japonês de manhã."

                    mc desconfiado "Ok... Vou me lembrar disso."

            jump call_cidade
        else:


            scene black with Dissolve(1.0)

            if cenario_salao_1vez:

                "Parece que não tem ninguém aqui agora. Que estranho..."

                "Mas já tá tudo aberto."

                mc zerado "Parece que o pessoal daqui não gosta de acordar cedo..."
            else:


                if mc_massagem == 6:

                    "A [m] precisa de um tempo pra ajeitar as coisas. Espero que ela volte com as aulas logo."

                elif mc_massagem >= 7:

                    "Agora que a [m] não trabalha mais no Tadaima, por que ela não abre o salão de manhã?"
                else:


                    "Esqueci que a [m] trabalha cedo no Tadaima."

                    mc desculpa "Ela é uma garota bem esforçada."

            jump call_cidade

    label cenario_fadolandia:

        if pixel_evento == 5:

            jump pixie_evento2

        scene fadolandia geral with Dissolve(1.0)

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cenario_fadolandia","fadolandia","cenario")

        $ nandom = random.randint(1,15)

        if nandom == 1:

            "De novo esse sonho?"

        elif nandom == 2:

            "Estou de volta no mundo dos meus sonhos."

        elif nandom == 3:

            "De novo? O que será que esse sonho quer me contar?"

        elif nandom == 4:

            "Acho que eu vou continuar sonhando com isso até descobrir o que ele significa..."

        elif nandom == 5:

            "Por que esse lugar de novo?"

        elif nandom == 6:

            "O que será que esse mesmo sonho quer dizer?"

        elif nandom == 7:

            "Acho que eu preciso parar de dormir com a TV ligada... só sonho estranho..."

        elif nandom == 8:

            "Mano, comer miojo duas da manhã da nisso... de novo esse lugar?"
        else:


            pass

        if cenario_fadolandia_1vez:

            show pixie sorrindo with dissolve

            p "Olá!"

            p "Então você realmente veio..."

            p "Tudo joinha, [mc]!?"

            mc normal "Oi, [p]. Tudo certo. E você?"

            p "Eu também! Que bom que você veio me visitar por conta própria. Mesmo eu sendo irresistível, não tinha certeza se você realmente viria."

            mc envergonhado "É que eu queria falar com você."

            show pixie provocando with dissolve

            p "Hmm... Você quer fazer o que eu estou pensando?"

            menu:
                "Exatamente.":


                    mc tarado "Exatamente o que você tá pensando."

                    p "Você sabe que eu adoraria..."

                    show pixie bonitinha with dissolve

                    p "Só que infelizmente você ainda não tá pronto pra isso aqui."

                    mc safado "Claro que eu tô."

                    p "Eu ainda sou areia demais pro seu caminhãozinho."

                    mc serio "..."

                    p "Mas não se preocupe. Continue fazendo o que você tá fazendo lá no seu mundo que cedo ou tarde eu vou te procurar."

                    mc charmoso "Ok. Vou me esforçar."

                    p "Assim que se fala."
                "Não. Pare de ser oferecida.":


                    mc zerado "Não. Você só pensa nisso?"

                    show pixie bonitinha with dissolve

                    p "Basicamente..."

                    mc "..."

            p "Mas o que você queria falar comigo?"

            mc normal "Ah! Eu queria pedir sua ajuda pra entender melhor o que tá acontecendo comigo nos últimos dias."

            p "Certo. Muito bom você ter vindo aqui procurar ajuda."

            p "Sua vida vai mudar rapidamente e é preciso entender o que está havendo pra você tirar o máximo de proveito disso tudo."

            mc "Certo. E como você pode me ajudar?"

            p "No momento eu posso fazer duas coisas por você. Ajudar com os encontros e te explicar melhor sua situação."

            mc surpreso "Você pode me ajudar com os encontros?!"

            show pixie sorrindo with dissolve

            p "Muito mais do que você imagina!"

            p "Eu te expliquei isso na primeira vez que conversamos. Tenho acesso a todos seus pensamentos."

            p "E eu posso dizer para você o que você fez de certo e o que você fez de errado em cada encontro."

            mc "Isso é incrível! Me ajudaria muito!"

            p "Obviamente. Mas pra fazer isso preciso de {b}Celebrity Coins{/b}, que são moedas especiais."

            mc desconfiado "Moedas especiais?"

            show pixie explanando with dissolve

            p "Sim. Essas moedas foram criadas por uma antiga civilização que já está extinta."

            mc zerado "E como eu consigo isso?"

            p "Não é possível. Elas são extremamente raras e apenas pessoas fora do jogo podem pegar."

            mc "Fora do jogo?"

            p "Sim. Não se preocupe com elas. Quando {size=10}quem estiver jogando{/size} tiver moedas suficientes você vai saber."

            mc desconfiado "Quem o que?"

            p "Não perca tempo tentando entender coisas que não lhe dizem respeito."

            mc zerado "..."

            show pixie animada with dissolve

            p "Agora. A segunda coisa que eu posso te ajudar é te explicar melhor sobre como sua vida está mudando."

            mc "Tenho que pagar por isso também?"

            p "Não. Isso eu faço de graça para você, porque você é muito gatinho."

            mc desconfiado "Ok..."

            p "Então é isso. Sempre que precisar de ajuda com um encontro ou tiver alguma dúvida sobre tudo isso, venha me visitar, ok?"

            mc normal "Beleza. Obrigado pela ajuda, [p]."

            show pixie provocando with dissolve

            p "Não precisa agradecer, bobinho. Seu sucesso com as celebridades é tudo o que eu quero."

            p "Quero ver você se deliciando com todas elas. E eles também."

            mc envergonhado "Vamos ver..."

            $ cenario_fadolandia_1vez = False

            "..."

        elif not cenario_fadolandia_1vez and pixie_e1 == "nada":

            jump pixie_evento1

        elif pixie_e1 != "nada" and not pixie_e3:

            jump pixie_evento3
        else:


            if tempo < 2:

                jump fadolandia_exploracao
            else:


                show pixie sorrindo with dissolve

            p "Oi!"

        p "Que bom que você voltou! Eu gosto de te ver, [mc]."

        p "E como eu posso servir meu querido [mcc] hoje?"

        label pixie_sonho_menu:

            show pixie animada with dissolve

            menu:

                "Vamos passear pelo sonho." if pixie_e3:

                    if pixie_historia >= 8:

                        mc charmoso "Bora continuar nossos passeios?"

                        p "Ainda não, [mc]."

                        mc preocupado "Por quê?!"

                        p "Você ainda não está pronto para o próximo passo. Continue vivendo e em breve continuaremos."

                        mc concentrando "Ok..."

                        "Droga... quando vai rolar alguma coisa com ela? Não aguento mais esperar!"

                        jump pixie_sonho_menu

                    jump fadolandia_pixie
                "Eu quero ajuda com um encontro.":


                    p "Claro! A cada nova atualização eu terei novas análises."

                    p "Não se esqueça que eu preciso de {b}Celebrity Coins{/b} para poder fazer isso."

                    label pixie_ajuda_encontro:

                        python:
                            if renpy.android:
                                persistent.guia1 = PythonSDLActivity.pegaGuia1()

                        scene fadolandia geral with dissolve

                        show pixie explicando with dissolve

                        if persistent.guia1:

                            menu:
                                "Priscila: Primeiro Encontro ({b}Liberado{/b})":


                                    show pixie animada with dissolve

                                    p "Muito bem! Vamos começar. Preste muita atenção!"

                                    call guia_priscila_e1 from _call_guia_priscila_e1

                                    "..."

                                    jump pixie_sonho_menu
                                "Agora não quero analisar encontros.":


                                    jump pixie_sonho_menu
                        else:


                            menu:
                                "Priscila: Primeiro Encontro ({b}300 Celebrity Coins{/b})":


                                    python:
                                        if renpy.android:
                                            persistent.coins = PythonSDLActivity.pegaMoedas(0)

                                    if persistent.coins >= 300:

                                        python:
                                            if renpy.android:
                                                PythonSDLActivity.compraGuia1()
                                                persistent.coins = PythonSDLActivity.usaMoedas(300)
                                                PythonSDLActivity.registraEvento("guia1_liberado","guia1","guias")

                                        play sound "extra/carta.mp3"

                                        "{b}Você usou 300 Celebrity Coins{/b}"

                                        p "Obrigadinha! Agora você pode ver minha análise quantas vezes quiser."

                                        p "Você não precisa gastar outras vezes."

                                        mc zerado "Era só o que faltava ter que pagar toda vez que eu quisesse ver."

                                        show pixie desconfiada with dissolve

                                        p "Tá me chamando de mercenária?"

                                        mc envergonhado "Claro que não..."

                                        p "..."

                                        jump pixie_ajuda_encontro
                                    else:


                                        show pixie bonitinha with dissolve

                                        p "Infelizmente você não tem {b}Celebrity Coins{/b} suficientes para liberar minha análise para este encontro."

                                        p "Você pode conseguir moedas facilmente vendo vídeos na {b}Loja de Cartas{/b} ou comprando na nossa {b}Loja{/b}."

                                        show seta with vpunch

                                        p "Só clicar no botão {b}Menu{/b} aqui no canto inferior direito."

                                        hide seta







                                        jump pixie_sonho_menu
                                "Agora não quero analisar encontros.":


                                    jump pixie_sonho_menu







                    jump pixie_sonho_menu
                "Tenho uma pergunta.":


                    jump pixie_sonho_perguntas

                "Quero ver você com aquela roupa de novo." if f1_poder and not pixie_e3:

                    mc tarado "O que acha de fazer aquele showzinho de novo pra mim?"

                    show pixie provocando with dissolve

                    p "Você gostou mesmo, hein?"

                    mc safado "Muito."

                    p "Dá 5 minutos e entra no meu quarto."

                    mc tarado "Ok."

                    hide pixie with dissolve

                    "..."

                    "Pronto. Bora lá."

                    "..."

                    scene fadolandia interior with Dissolve(1.0)

                    mc safado "Estou aqui."

                    show pixie b_provocando with dissolve

                    p "Pronto?"

                    mc "Nasci pronto."

                    show pixie b1 with dissolve

                    pause

                    p "Assim?"

                    mc "Delícia..."

                    show pixie b2 with dissolve

                    pause

                    mc "Gostosa..."

                    p "Isso, fala mais."

                    show pixie b3 with dissolve

                    pause

                    mc "Não aguento mais."

                    p "Melhor parar então."

                    hide pixie with dissolve

                    mc bravo "De novo não vamos poder fazer nada?"

                    show pixie b_provocando with dissolve

                    p "[mc], toda vez que você quiser vir me ver, você pode vir."

                    p "Seu tesão é como se fosse alimento para mim. Eu quero isso sempre que quiser."

                    p "Mas você ainda não está pronto para o prato principal."

                    mc preocupado "Mas por quê?"

                    p "Não posso te explicar isso. Mas você vai saber quando acontecer."

                    p "Vai ser o maior paradoxo da sua vida."

                    mc desconfiado "..."

                    p "Agora pode acordar. Xau xau!"

                    mc "Ei... Eu..."

                    scene black with Dissolve(1.0)

                    return
                "Está tudo certo. Vou acordar.":


                    mc normal "Acho que já tá na hora de acordar."

                    p "Ahh... Que pena. Eu gosto de te ver."

                    p "Mas eu sei que você virá mais vezes."

                    mc "Com certeza."

                    p "Xau xau!"

                    return

        label pixie_sonho_perguntas:

            show pixie bonitinha with dissolve

            p "O que você quer saber?"

            menu:
                "Qual é meu objetivo?":


                    show pixie explanando with dissolve

                    p "Cada pessoa pode ter um objetivo específico próprio. O seu pode ser levar a [c] pra cama ou namorar a [s] ou se dar bem como paparazzo."

                    p "É você quem vai decidir qual será seu objetivo. Esta é uma aventura muito pessoal e cada pessoa pode ter um final diferente."

                    p "Entretanto, no geral, o objetivo é se relacionar com o máximo de pessoas possível e viver a história que você quer com elas."

                    p "Cada celebridade ou pessoa que você conhecer aqui tem uma história própria. Seu objetivo é ver as histórias que você quer até o final."

                    p "Para atingir seu objetivo, você deverá prestar atenção em como vai se relacionar com elas."

                    p "Continue se encontrando com os personagens e crie sua própria história com eles!"

                    jump pixie_sonho_perguntas
                "Como minhas escolhas influenciam o que acontece?":


                    show pixie explanando with dissolve

                    p "Suas escolhas são o elemento mais importante de tudo!"

                    p "Suas respostas é que vão decidir como a história vai acontecer. Pode parecer exagero, mas é a verdade!"

                    p "Assim como na vida real, aqui nós temos DIVERSOS caminhos. Tudo vai depender de como você vai se relacionar com os outros."

                    p "As decisões possuem resultados de curto e longo prazo. No curto prazo, elas mudam como um encontro vai acabar."

                    p "Quero dizer, no curto prazo elas decidem se você vai ver uma cena ou outra. Alguns encontros possuem diversas {b}cenas especiais{/b}."

                    p "Não existe respostas certas. Normalmente existem pelo menos duas cenas especiais que você pode ver seguindo caminhos opostos."

                    p "Caso você queira ver todas as cenas, é preciso viver cada encontro mais de uma vez."

                    p "Preste atenção nos diálogos e tome as decisões que você acha certas para atingir o objetivo que você escolheu."

                    show pixie explicando with dissolve

                    p "Agora, no longo prazo, suas escolhas vão determinar como um personagem específico vai lidar com você."

                    p "Se você seduzir a [c], por exemplo, ela vai agir de forma diferente no futuro do que se você virar um amigo."

                    p "É por isso que logo no começo eu fiz você confirmar que é o único responsável por suas escolhas."

                    p "Se tudo vai acabar bem ou mal só depende de você."

                    jump pixie_sonho_perguntas
                "Como que eu sei se tô seduzindo ou virando amigo?":


                    show pixie explanando with dissolve

                    p "A melhor forma de saber isso DURANTE um encontro é observar as reações do seu parceiro."

                    p "Preste atenção na fisionomia e em como ele tá respondendo aos seus avanços."

                    p "Os seres humanos são uma caixinha de surpresas. E aqui a gente tenta ser o mais real possível."

                    p "Por isso é impossível saber com certeza. Mas quanto mais você conhecer um personagem, mais fácil vai ser perceber isso."

                    p "Também preste atenção na mensagem 'Fulana está analisando suas ações no encontro...'."

                    p "Esse é o momento em que o personagem vai decidir se você seduziu ou conquistou a amizade dele."

                    p "DEPOIS do encontro você poderá ver sua pontuação e então poderá saber melhor como você se saiu."

                    p "Se o resultado não foi o que você esperava, você pode usar meus poderes pra voltar no tempo e tentar novamente."

                    show pixie provocando with dissolve

                    p "Por isso sempre {b}Salve{/b} antes dos encontros, para que depois você possa {b}Carregar{/b} e fazer escolhas diferentes."

                    p "Essa é a vantagem de ter a fada mais sexy e poderosa do mundo te ajudando."

                    p "Só que meu poder vai fazer você se esquecer de tudo o que você viveu. É diferente do Harry Potter, por exemplo, que eles se lembram."

                    p "Como cada encontro possui vários resultados diferentes, você terá que viver eles mais de uma vez para ver todos."

                    show pixie animada with dissolve

                    p "Ah! Outra coisa importante! Os pontos que você ganha são cumulativos. Isso quer dizer que os pontos passam de um encontro para outro."

                    p "Dessa forma, se você seguiu o caminho da amizade no primeiro encontro, será mais fácil ser amigo no segundo."

                    p "Igualmente, se você seguiu o caminho da amizade nos dois primeiros, será impossível juntar pontos de sedução em um terceiro."

                    p "É o que chamamos de cair na {i}friendzone{/i}. É uma pena, mas a vida é assim."

                    jump pixie_sonho_perguntas
                "Tem como eu estragar tudo?":


                    show pixie desconfiada with dissolve

                    p "Com certeza!"

                    p "Existem duas formas de você se ferrar."

                    p "Primeiro é se você não entregar uma pauta para seu chefe a cada {b}5 encontros{/b}. Você vai ser despedido e vai ter que ir morar com seus pais."

                    p "Vai deixar para trás tudo o que conquistou aqui e vai morrer de solidão. É um final terrível."

                    p "Ou seja, você só precisa entregar pautas quando está avançando nas histórias principais. Você pode dormir à vontade que ele nunca vai te chamar."

                    p "Para evitar ser despedido, você deve descobrir coisas interessantes sobre as celebridades."

                    p "A melhor forma de conseguir isso, geralmente, é seguindo o caminho da amizade. Quanto mais elas confiarem em você, mais elas vão se abrir."

                    p "Se você só seduzir todo mundo, provavelmente eles nunca vão confiar em você o suficiente para revelar seus segredos."

                    p "Saber equilibrar sedução e amizade é o segredo para se dar bem aqui."

                    show pixie explanando with dissolve

                    p "A segunda forma de se ferrar é caso você perca a confiança de uma celebridade específica."

                    p "Se você for um idiota com a [c], por exemplo, ela pode não querer mais falar com você. E daí você não vai mais poder continuar a história dela."

                    p "Se você entregar muitas pautas de uma mesma celebridade pode acontecer a mesma coisa. Seja cuidadoso."

                    show pixie sorrindo with dissolve

                    p "Se você for bacana e tomar cuidado, tem tudo pra dar certo!"

                    p "Boa sorte não fodendo com tudo!"

                    jump pixie_sonho_perguntas
                "Por hora é isso.":


                    jump pixie_sonho_menu

                    show pixie sorrindo with dissolve

                    p "Ok!"

                    p "Quando precisar de mim de novo é só tirar uma soneca e vir pra cá."

                    p "Xau xau!"

        return

    label cenario_parque:

        $ estou_na_cidade = False

        play sound "audio/som_1_parque.mp3"









        scene ilha parque with Dissolve(1.0)

        if tempo == 1:

            if maria_evento == 0 and dia >= dia_maria and v4_fim:

                jump maria_evento1

            if maria_evento == 1 and dia >= dia_maria:

                jump maria_evento2

            elif maria_evento == 2 and dia >= dia_maria:

                jump maria_evento3

            elif maria_evento == 3 and dia >= dia_maria:

                jump maria_evento4

            elif maria_evento == 4 and dia >= dia_maria:

                jump maria_evento5

            elif maria_evento == 5 and dia >= dia_maria:

                jump maria_treino

            elif maria_evento == 6 and dia >= dia_maria:

                jump maria_evento6

            elif maria_evento == 7 and dia >= dia_maria:

                "Opa. A [ma] tá aqui."

                mc charmoso "Oi oi."

                show maria excitada with dissolve

                if maria_namoro:

                    ma "Oi, lindo. Tudo bem?"
                else:


                    ma "Oi, [mc]. Tudo bem?"

                mc "Tudo sim. E você?"

                ma "Meio corrido, mas tudo bacana."

                mc normal "Legal."

                ma "Eu queria falar sobre nossos treinos. Minha academia abriu e eu quero muito que você vá pra lá."

                mc "Com certeza."

                jump maria_evento7



                "A [ma] está preparando tudo para eu começar a frequentar a academia dela."

                "Não vejo a hora de continuar nossos treinos."

                p rindo "A história da [ma] continua nas próximas atualizações."

                p "Fique de olho nas nossas redes sociais @celebrityhuntergame e atualize nos dias 1 e 15 de cada mês!"

            elif maria_evento == 8:

                "Eu tenho que ir lá no centro, na parte da manhã, na academia da [ma]."

                "A gente só vai treinar por lá agora."

                "Bora."

                jump call_cidade

        if tempo > 2:

            if not massagista_parque:

                mc serio "Ei. Parece que tem uma moça sentada sozinha ali."

                "Será que eu devia chegar nela? Mas olha a hora... Ela pode achar que eu sou um bandido..."

                menu:
                    "Deixar para outra hora do dia":


                        mc desculpa "Agora tá muito tarde. Seria meio complicado."

                        mc "Melhor eu deixar para outra hora."

                        jump call_cidade
                    "Chegar perto dela":


                        $ m_nome = "Garota"

                        mc tarado "Quem não arrisca não petisca."

                        "..."

                        scene parque banco_noite with Dissolve(1.0)

                        mc desculpa "Boa noite..."

                        show karli feliz with dissolve

                        m "Ah?"

                        m "O-oi. Boa noite."

                        if massagista_bonita:

                            mc surpreso "Eu lembro de você!"

                            mc normal "Você é a garota do Tadaima. A garçonete da manhã."

                            m "Ah? Ah, sim..."

                            m "Acho que eu me lembro de você..."

                            mc desculpa "Eu apareci um dia lá, mas acabei não comendo nada."

                            m "As coisas são caras lá mesmo."

                            mc "Não sei se você lembra, mas meu nome é [mc]."

                            m "Verdade..."
                        else:


                            mc charmoso "Meu nome é [mcc] e eu moro naquele prédio logo ali."

                            m "Ok..."

                        mc desculpa "Desculpa a intromissão, mas o que você tá fazendo aqui sozinha essa hora?"

                        m "Por um acaso eu te devo satisfação agora?"

                        mc envergonhado "Nã-não... Claro que não... É só que eu..."

                        "Droga! Um estranho chega falando isso no meio da noite. O que eu esperava que ela falasse?"

                        m "Tô só brincando com você. Calma."

                        mc "A é? Ufa... Que bom..."

                        m "Mas que é suspeito um cara chegar em você assim no meio da noite..."

                        mc "Verdade..."

                        mc normal "É que eu fiquei um pouco preocupado com você sozinha aqui."

                        mc "A ilha não é violenta, mas a ocasião faz o ladrão o pessoal diz."

                        m "Quem diz isso? Nunca ouvi..."

                        mc desculpa "Acho que tô ficando velho."

                        m "Calma... Tô brincando com você de novo."

                        mc desconfiado "Você tem um senso de humor meio..."

                        show karli satisfeita with dissolve

                        $ m_nome = "Karli"

                        m "O nome é [m]. E eu sou mestra em piadas com senso de humor questionável."

                        mc desconfiado "Hmm..."

                        m "Eu gosto de sair durante a noite e andar pela ilha."

                        m "A gente encontra pessoas estranhas como você."

                        mc zerado "Estranho?"

                        m "E dessa vez não é piada."

                        mc "..."

                        show karli feliz with dissolve

                        m "Minha cota diária de conversa com desconhecidos tá preenchida. Melhor eu ir pra casa."

                        m "Boa noite, [mc]."

                        mc "Boa noite, [m]."

                        hide karli with dissolve

                        mc normal "Bom... É uma garota estranha, mas conhecer novas pessoas nunca é ruim."

                        m "{size=15}Eu ouvi isso!{/size}"

                        mc surpreso "!"

                        mc desculpa "Eu tenho que parar com essa mania de pensar em voz alta..."

                $ massagista_parque = True

            if massagista_parque and not stifler_conheceu:

                jump stifler_evento1

        mc concentrando "..."

        mc feliz "Esse parque é massa."

        mc zerado "Mas ultimamente não tô com tempo pra ficar andando sozinho..."

        mc normal "Preciso conseguir pautas e conhecer novas pessoas. Não vou perder essa chance."

        jump call_cidade

    label cenario_casa:

        $ estou_na_cidade = False

        stop sound

        if diana_final2_pre and not diana_final2:

            jump diana_final2_parte2

        scene ape_geral with Dissolve(1.0)













        $ nandom = random.randint(1,40)

        if nandom == 1:

            mc concentrando "A cama... parece que tá me chamando..."

        elif nandom == 2:

            "A forma como eu lido com as celebridades vai mudar completamente o meu futuro. Não posso ser um cuzão."

        elif nandom == 3:

            "Quanto mais eu seduzir a [c], mais fácil vai ser seduzir ela das próximas vezes."

            "Mas se eu quero uma relação mais séria com ela, não adianta só seduzir. Tenho que ser companheiro também."

        elif nandom == 4:

            "Eu posso visitar os pontos mais famosos da cidade em três períodos diferentes."

            "Eu posso encontrar pessoas diferentes de manhã, de tarde ou de noite."

        elif nandom == 5:

            "Eu preciso entregar uma pauta pro chefe a cada 5 encontros."

            "Posso passar os dias à vontade, mas quando eu estiver em um encontro, tenho que tentar descobrir pautas."

        elif nandom == 6:

            "Tem uma palavra que não sai da minha cabeça... [p]... Não sei o que isso quer dizer..."

            mc desconfiado "Eu tenho a impressão que é um nome... Mas nenhum ser humano se chamaria assim!"

        elif nandom == 7:

            if sayuri_evento1_check:

                "Preciso descobrir alguma coisa sobre a tal da [s]..."

                "Tenho que ir pra Cidade Chinesa. Posso pegar um ônibus saindo pelo sul da ilha."
            else:


                "As vezes eu esqueço que a [s] é uma atleta olímpica... Ela é incrível!"

                "Por que será que essas garotas dão bola pra mim?"

        elif nandom == 8:

            "Bem que eu podia morar em um apartamento maior..."

        elif nandom == 9:

            "Eu vi no noticiário que da capital dá pra ver a lua gigante. É um fenômeno que só acontece aqui..."

        elif nandom == 10:

            "Sendo mais amigo das celebridades, eu tenho mais chance de conseguir pautas. Tenho que tentar pensar com a cabeça de cima."

        elif nandom == 11:

            "O que não falta nessa ilha são garotas lindas. É muita sorte poder falar com algumas delas."

        elif nandom == 12:

            "Tem tanta coisa acontecendo comigo ultimamente que até parece um filme... ou um jogo. Doideira..."

        elif nandom == 13:

            "Do ponto de ônibus eu posso ir para a parte continental da cidade. Quem dera ter dinheiro pra comprar um carro..."

        elif nandom == 14:

            "O pessoal da redação fala que a capital é uma espécie de cebola... com camadas. O que raio isso quer dizer?"

        elif nandom == 15:

            "Todo o salário que eu ganho na revista vai pra pagar contas. Se eu quiser comprar outras coisas, preciso arranjar uns bicos."

        elif nandom == 16:

            "Na centro da cidade tem vários lugares interessantes, uma pizzaria famosa, o canal de TV, o museu, a prefeitura..."

        elif nandom == 17:

            "Nossa revista tá cada vez mais famosa. Se eu me der bem lá, com certeza eu tô feito pro resto da vida."

        elif nandom == 18:

            "{i}zzzzzzzzzk{/i}"

            mc desconfiado "Que barulho é esse? Eita! Deixei a TV ligada? Que estranho..."

        elif nandom == 19:

            "Conseguir pautas é muito importante pra eu não ser despedido. Preciso fazer as celebridades confiarem em mim."

        elif nandom == 20:

            "Fazendo bicos no bar e em outros lugares, eu posso devagar juntar uma grana. Seria massa comprar umas coisinhas."
        else:


            call checa_eventos from _call_checa_eventos

        menu:

            "Dormir por um período" if tempo < 3:

                $ tempo += 1

                scene apartamento cama with dissolve

                "z{size=20}{i}z{/i}{/size}{size=18}{i}z{/i}{/size}{size=16}{i}z{/i}{/size}{size=14}{i}z{/i}{/size}{size=12}{i}z{/i}{/size}{size=10}{i}z{/i}{/size}"

                menu:
                    "Visitar a [p] em Fadolândia":


                        call cenario_fadolandia from _call_cenario_fadolandia_1
                    "Acordar":


                        pass

                scene apartamento cama with dissolve

                show mc acordando with dissolve

                "Muito bom!"

                jump cenario_casa

            "Dormir até amanhã" if tempo > 2:

                $ dormir_em_casa = True
                $ mc_ja_tomou_banho = False

                jump dormir
            "Fazer alguma coisa em casa":


                "Tô com um tempo sobrando. O que eu vou fazer agora?"

                menu:
                    "Comer alguma coisa":


                        "Bateu aquela fome agora."

                        $ tempo += 1

                        scene mc ap_comendo with Dissolve(1.0)

                        pause

                        "{i}chomp chomp{/i}"

                        "{i}nom nom nom{/i}"

                        "..."

                        "Delícia de pizza!"

                        if tempo > 3:

                            "Agora deu aquele sono..."

                            "Vou direto pra cama!"

                            $ dormir_em_casa = True
                            $ mc_ja_tomou_banho = False

                            jump dormir
                        else:


                            mc "Beleza! Agora tô alimentado."

                            jump cenario_casa
                    "Tomar banho":


                        if not mc_ja_tomou_banho:

                            "Não dá pra se encontrar com tantos famosos e feder igual um animal do mato. Bora tomar uma ducha."

                            play sound "audio/som_16_chuveiro.mp3"

                            scene mc banho with Dissolve(1.0)

                            $ renpy.pause(5)

                            "..."

                            $ mc_ja_tomou_banho = True

                            "Delícia!"
                        else:


                            mc zerado "Eu acabei de tomar banho. Por que tomaria outro agora?"

                        jump cenario_casa
                    "Jogar videogame ([videogame])":


                        scene mc ap_jogando with Dissolve(1.0)

                        mc "Deixa eu ver o que tem de graça pra gastar um tempo..."

                        if videogame == 0:

                            $ videogame += 1

                            "Hoje eu vou jogar esse aqui... {b}Nautilus 05{/b}... que porra de nome é esse?"

                            "Com certeza é aquele tipo de título que tem algum mistério por trás. Daí uma hora vai aparecer e a gente fala AAAHHH!! ERA ISSO!"

                            show capa n05 with dissolve

                            mc "Uau! É um lance meio do futuro. E tem um pessoal bem gostoso no elenco."

                            "Um jogo de escolhas que acontece no futuro apocalíptico... no meu futuro? Meu futuro não é apocalíptico, não! Nem vem!"

                            "Quê?! É um jogo adulto com história de cinema?! Não é possível um negócio desses! Cena de sexo com história boa?! Isso existe?!"

                            "Esse aqui vale a pena jogar!"

                            "Por que eu tô pensando como se eu tivesse fazendo uma propaganda? Esse aqui é o Show de Truman?!"

                            menu:
                                "Baixar Nautilus 05 (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nautilus-05:-Serie-Cyberpunk-(Premium)-OzLBBUKHv'))
                                "Baixar Nautilus 05 (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/n05/'))
                                "Outra hora":


                                    pass

                        elif videogame == 1:

                            $ videogame += 1

                            "Vou tentar outra de graça aqui hoje... Encontros - Nome provisório. Este jogo aqui ainda não acabou."

                            "Sobre o que que é esta desgraça?"

                            mc "Um game que acontece no mundo de Celebrity Hunter, com personagens já conhecidos dessa incrível história."

                            mc "Reveja a Pixie, Ágata, Carol... QUÊ?! HAHAHA! Que coincidência! São nomes igualzinhos de umas que eu conheço aí."

                            mc "Que loucura... Encontros... Esse mundo de Celebrity Hunter deve ser uma doideira só..."

                            mc "Mais um jogo adulto, com uma história incrível, escolhas emocionantes e uma mecânica inovadora. Uau..."

                            menu:
                                "Baixar Encontros (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/'))
                                "Baixar Encontros (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/en/'))
                                "Outra hora":


                                    pass

                            mc "Minha vida já é conturbada demais pra jogar jogos complicados assim. Acho que vou só assistir uma coisa hoje."

                            "Imagina se eu fosse jogar Encontros e visse a... imagina? Haha... que doideira..."

                        elif videogame == 2:

                            $ videogame += 1

                            "Bora ver esse aqui... não é parecido com aquele... olha o nome... {b}Nautilus 10{/b}?!"

                            "É continuação daquele outro. Esse é '10' e o outro é '05'. Por que eles só não chamam de Nautilus 1 e Nautilus 2? Que frescura."

                            show capa n10 with dissolve

                            mc "Então continua aquela saga adulta apocalíptica. Aquele N05 foi bem massa. Então acho que vou continuar nesse aqui agora."

                            "Depois de sairem do CTM, os protagonistas vão para o Deserto, a região mais perigosa de Nova Doma, o nome do país."

                            "Será que eles vão conseguir sair de lá ou morrerão sem água e sem comida? E melhor... eles vão acabar transando muito?"

                            "Que sinopse mais doidona é essa?!"

                            "Seja como for eu vou jogar isso aqui! Nem que eu tenha que viver no lixão! Bora de Avenida Brasil!"

                            menu:
                                "Baixar Nautilus 10 (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nautilus-10:-Projeto-Cyberpunk-(Premium)-2wnrXt_c_'))
                                "Baixar Nautilus 10 (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/npc/'))
                                "Outra hora":


                                    pass

                        elif videogame == 3:

                            $ videogame += 1

                            "Ok! Hoje tô afim de um RPG! E com cenas adultas cheias de sexo! Será que existe?! {b}NFC +18{/b}?! Não é que existe?!"

                            "Nova Fantasia Clicker ou NFC +18 é um RPG focado em seduzir e dominar suas inimigas em combate ou com o sexo."

                            show capa nfc with dissolve

                            mc "Não é possível que existe um negócio desses mesmo..."

                            "O jogo se passa em uma terra que foi dominada por uma magia que torna todas as criaturas escravas do prazer."

                            "Seu objetivo vai ser descobrir a origem dessa magia e salvar o reino desse terrível mal!"

                            "Você pode acabar com elas ou vencer elas por meio do sexo, sedução e pode até levar elas pra viver com você."

                            mc "Sério isso?!"

                            "A história é incrível, continuação de Nova Fantasia, com finais alternativos e secretos pra você descobrir."

                            mc "Caraca! Esse com certeza eu vou jogar!"

                            menu:
                                "Baixar NFC +18 (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nova-Fantasia-Clicker-+18-(Premium)-UTkgjtBgK'))
                                "Baixar NFC +18 (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/nfc/'))
                                "Outra hora":


                                    pass

                        elif videogame == 4:

                            $ videogame += 1

                            "Não é possível... {b}Nautilus 20{/b}?! É outro daquela série! Eu pensei que tinha acabado!"

                            "Então tem o N05, o N10 e agora o N20. Que é tipo o terceiro da série. Por que esse tal de RB usou esses números tão estranhos?!"

                            show capa n20 with dissolve

                            mc "Então agora a história continua depois do Deserto. Eu queria mesmo jogar até chegar na Capital. Parece que é agora!"

                            "Depois de escaparem do Deserto, os protagonistas se envolvem em um duelo entre o governo e os rebeldes."

                            "Como eles podem usar esse conflito para chegarem na Capital e terem uma vida digna?! E com muito sexo!"

                            "Por que sempre tem SEXO jogado aleatoriamente em todas as sinopses dessa empresa?!"

                            "Será que eles acham que só porque tem sexo a gente vai jogar?! Que absurdo... deixa eu jogar, vai!"

                            menu:
                                "Baixar Nautilus 20 (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/'))
                                "Baixar Nautilus 20 (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/n20/'))
                                "Outra hora":


                                    pass
                        else:


                            $ videogame = 0

                            "Bora desestressar jogando esse aqui... {b}Nova Fantasia: RPG Adulto{/b}."

                            "Um jogo de RPG com um combate em ação nunca visto antes na história do celular! Por que celular? Eu to nô console. Cada uma..."

                            "Uma história de vingança e cheia de emoção, mistério, com cenários incríveis, músicas sensacionais e muitas novidades!"

                            "Além de ser o jogo mais difícil que o RB já criou e criará!"

                            mc "Como eles sabem que o cara nunca vai fazer um jogo mais difícil que esse? Então quem terminar esse aí é um herói?"





                            menu:
                                "Baixar Nova Fantasia (Premium)":


                                    $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nova-Fantasia:-RPG-Adulto-(Versao-Premium)-pa2lp7E-N'))
                                "Baixar Nova Fantasia (Grátis)":


                                    $ renpy.run(OpenURL('https://www.geiko.net/nf/'))
                                "Outra hora":


                                    pass

                            "..."

                            "Hmmm... Até que é interessante... é meio enrolado, mas a batalha é ação pura! Acho que eu nunca vi isso num jogo assim!"

                            "O cara que criou isso aqui deve ser um gênio. Com certeza!"







                            p rindo "Falar de um jogo dentro de outro jogo?"

                            p "Isso é um absurdo..."

                        mc "Ok... vamos lá!"

                        hide capa with dissolve

                        "..."

                        show black with dissolve

                        $ tempo += 1

                        hide black with dissolve

                        "Opa, olha a hora!"

                        if tempo > 3:

                            "Já tá tarde pra caramba..."

                            "Vou é já pra cama."

                            $ dormir_em_casa = True
                            $ mc_ja_tomou_banho = False

                            jump dormir
                        else:


                            mc "Joguei demais. Pra variar..."

                            "Bora continuar o dia."

                            jump cenario_casa



































            "Ligar para a [gina] e comprar o {b}novo apartamento{/b}" if compra_casa_evento and not casa_comprada:

                "Vou ligar pra [gina] e pagar a taxa pra passar o novo apartamento pro meu nome!"

                show mc cueca_telefone with Dissolve(1.0)

                "Smartphone" "Tuuu... Tuuuu...."

                gina "[mc]?"

                mc "Sou eu, [gina]. Queria falar com você sobre a casa."

                gina "Claro. Está pronto pra prosseguirmos?"

                mc "Sim."

                gina "Vamos nos encontrar lá no apartamento e acertamos tudo."

                mc "Combinado. Até lá."

                hide mc with dissolve

                "Agora é ir lá pro ap e pagar a taxa pra ela."

                python:
                    if renpy.android:
                        casa = PythonSDLActivity.pegaCasa()

                if not casa:

                    jump compra_casa
                else:


                    scene black with Dissolve(1.0)

                    "..."

                    scene ap sala with Dissolve(2.0)

                    pause

                    show gina ola with dissolve

                    gina "O valor pra passar o imóvel para o seu nome é de {b}R$ 2.000{/b}. Essa é a taxa que o cartório cobra. Será seu único custo."

                    jump casa_comprada

                jump compra_casa
            "Ir para o centro da cidade":


                $ nandom = random.randint(1,2)

                if nandom == 1:

                    mc normal "Não posso bobear agora. Vamos fazer algo útil!"

                elif nandom == 2:

                    pass

                $ mc_ja_tomou_banho = False

                jump call_cidade

    label cenario_tadaima:

        $ estou_na_cidade = False

        if tempo < 3:

            scene tadaima restaurante with Dissolve(1.0)

            play sound "audio/som_8_tadaima.mp3"

            if cash < 1000:

                "Esse restaurante japonês é caro pra caralho. Melhor eu pensar duas vezes antes de pedir algo aqui."
            else:


                "Engraçado que agora com essa grana que eu tô juntando, o Tadaima nem parece mais tão caro."

                "É bom ter dinheiro."

            menu:
                "Falar com a garçonete":


                    mc normal "Oi. Tudo bem?"

                    if tempo == 2:

                        if sayuri_e2 == "nada":

                            show garconete perguntando with dissolve

                            g "Boa tarde."

                            g "Como posso ajudar?"

                            if cenario_tadaima_1vez:

                                $ cenario_tadaima_1vez = False

                                menu:
                                    "Primeira vez que te vejo aqui. Você é linda.":


                                        show garconete provocando with dissolve

                                        g "Isso era pra ser uma cantada?"

                                        mc charmoso "Não. É só a verdade."

                                        g "Legal."

                                        g "Quando quiser pedir alguma coisa me chame."

                                        hide garconete with dissolve

                                        mc triste "..."

                                        jump cenario_tadaima
                                    "Vocês vendem alguma coisa por menos de C$ 100?":


                                        mc desconfiado "Vocês têm alguma coisa no menu que não custe os olhos da cara?"

                                        show garconete bemvindo with dissolve

                                        g "O Tadaima não é lugar pra pobretões como você."

                                        g "Sugiro que você vá comer em algum 'por quilo' da vida."

                                        mc zerado "..."

                                        mc serio "Não precisa falar assim..."

                                        g "Já perdi tempo demais com você. Pode dar o fora."

                                        hide garconete with dissolve

                                        mc bravo "..."

                                        jump cenario_tadaima
                                    "Esse quimono mexe com a fantasia de qualquer um.":


                                        show garconete provocando with dissolve

                                        g "E daí? Você é algum tipo de tarado?"

                                        mc charmoso "Não! Só queria que você soubesse que é bem sexy."

                                        g "..."

                                        mc "..."

                                        g "Quando quiser pedir alguma coisa me chame."

                                        hide garconete with dissolve

                                        mc triste "..."

                                        jump cenario_tadaima

                                "Já tomei um chega pra lá dessa garconete. Melhor voltar outra hora."

                                jump call_cidade
                            else:


                                menu:
                                    "Pensando bem... Não tenho dinheiro pra comer aqui.":


                                        mc envergonhado "Eu tô com fome, mas acho que não tenho dinheiro pra comer aqui."

                                        g "Por favor, não volte mais aqui."

                                        hide garconete with dissolve

                                        jump cenario_tadaima
                        else:


                            show garconete bemvindo with dissolve

                            g "Oi, [mc]."

                            if julia_seducao >= 99:

                                if not julia_inimigo:

                                    show garconete perguntando with dissolve

                                    g "Acho que a gente não começou bem, né?"

                                    g "Você nem me deu bola quando tava com a [s]."

                                    mc serio "Claro que não."

                                    g "Tudo bem. Eu não entendo direito, mas você tem sua razão."

                                    g "Não quero que você me odeie. Pelo contrário..."

                                    mc bravo "..."

                                    g "Tudo bem! Eu paro. Prometo que não vou dar em cima de você."

                                    mc serio "..."

                                    g "Você acha que a gente pode ser amigos?"

                                    mc serio "Hmmm..."

                                    "Eu não gostei do jeito que a [g] agiu antes, mas parece que ela está sendo sincera agora... Eu acho..."

                                    menu:
                                        "Eu vim aqui pra dizer que não quero mais papo com você.":


                                            mc serio "Olha, [g]. Eu vim aqui pra dizer que não quero mais falar com você."

                                            mc "Não tenho nada pessoalmente contra você. Mas eu acho que seu jeito não dá."

                                            mc "Eu quero me aproximar da [s] e você parece que tá querendo estragar isso."

                                            g "..."

                                            mc desculpa "Desculpa qualquer coisa, mas tô indo nessa."

                                            g "..."

                                            g "Ok..."

                                            g "Até."

                                            mc "Até."

                                            $ julia_inimigo = True

                                            jump call_cidade
                                        "Tudo bem. Acho que podemos ser amigos.":


                                            $ julia_seducao = 3

                                            mc concentrando "Ok... Acho que podemos ser amigos."

                                            mc normal "Mas você precisa pegar leve. Você é uma garota legal, mas não quero nada com você nesse sentido."

                                            g "Ok. Eu prometo que vou me comportar."
                                else:


                                    g "..."

                                    mc serio "..."

                                    g "Você veio pra me perdoar?"

                                    menu:
                                        "Isso. Acho que vou te dar uma chance.":


                                            $ julia_inimigo = False
                                            $ julia_seducao = 3

                                            mc serio "Acho que você merece uma chance."

                                            show garconete charmosa with dissolve

                                            g "Valeu, [mc]. Eu vou ser uma boa garota."

                            if julia_seducao >= -99:

                                if julia_e1 == "nada":

                                    g "Então você veio me ver mesmo, hein?"

                                    if julia_seducao <= 2:

                                        show garconete perguntando with dissolve

                                        g "Acho que a gente não começou bem, né?"

                                        g "Você nem me deu bola quando tava com a [s]."

                                        mc serio "Claro que não."

                                        g "Tudo bem. Eu não entendo direito, mas você tem sua razão."

                                        g "Não quero que você me odeie. Pelo contrário..."

                                        mc bravo "..."

                                        show garconete provocando with dissolve

                                        g "Tudo bem! Eu paro. Prometo que não vou dar em cima de você."

                                        mc serio "..."

                                        g "Você acha que a gente pode ser amigos?"

                                        mc serio "Hmmm..."

                                        mc normal "Ok. Acho que se você se comportar, podemos sim."

                                        show garconete bemvindo with dissolve

                                        g "Combinado!"
                                    else:


                                        g "Eu te achei muito interessante depois de te ver no Tadaima no outro dia."

                                        if julia_seducao >= 4:

                                            g "E depois do que a gente fez..."

                                            g "Acho que você me achou interessante também."

                                            mc safado "..."

                                        g "Acho que a gente devia passar um tempo juntos."

                                        "Essa [g] ainda é um mistério pra mim. Mas eu vou precisar me aproximar dela se eu quiser avançar com a [s]."

                                        if julia_seducao >= 4:

                                            "E depois que a gente se pegou no outro dia, acho que tem muita coisa que pode rolar."
                                else:


                                    g "Eu gosto quando você vem aqui."

                                label julia_tadaima:

                                    show garconete charmosa with dissolve

                                    if v18_fim:

                                        if julia_namoro:

                                            g "Então meu peguete veio me ver hoje no trabalho?"

                                            mc charmoso "Tá tudo legal?"

                                            g "Tudo sim, gato."

                                        elif julia_e4 == "caio":

                                            g "Oi, [mc]..."

                                            mc desconfiado "Como tão as coisas?"

                                            g "Tô tentando me acertar com o [caio], mas não sei se fiz certo de escolher ele."

                                            mc desculpa "Sei. Espero que dê tudo certo."

                                            g "Também..."
                                        else:


                                            g "Olha se não é meu melhor amigo me fazendo uma visita. Tá gato hoje, hein?"

                                            mc envergonhado "Haha! Valeu amigona."
                                    else:


                                        g "E o que eu posso fazer pro meu paparazzo preferido?"

                                    menu:

                                        "Eu recebi sua mensagem. Vim te ver." if julia_cel_msg1 and julia_e1 == "nada" and not julia_cel_msg1_resposta_check:

                                            mc charmoso "Eu vi sua mensagem. Vim ver você aqui no trabalho."

                                            g "A é?"

                                            jump julia_evento1
                                        "Tá tudo legal com você?":


                                            mc normal "E você? Tudo bacana?"

                                            g "Tá interessado em mim, é?"

                                            mc envergonhado "Só tô perguntando..."

                                            $ nandom = renpy.random.randint(1,5)

                                            if nandom == 1:

                                                g "O trabalho aqui é bem tranquilo. Não tem muitos clientes."

                                                show garconete perguntando with dissolve

                                                g "Mas tem muita gente rica que dá nojo. Às vezes a gente acha que porque tem dinheiro o cara é educado..."

                                                g "Tomá no cu! Metade deles querem pegar na minha bunda. E a outra metade quer pegar no peito."

                                                g "Nojentos..."

                                            elif nandom == 2:

                                                g "Eu tô legal. Ontem eu e a [s] assistimos um seriado novo."

                                                mc normal "Eu tenho Netflix também."

                                                g "Que Netflix o quê? Baixei no torrent mesmo, filho."

                                                g "Acha que eu vou gastar dinheiro que eu não tenho com seriado? Compartilhado não é roubado."

                                                mc envergonhado "..."

                                            elif nandom == 3:

                                                if sayuri_e2 == "amizade":

                                                    show garconete perguntando with dissolve

                                                    g "A [s] perde metade do dia digitando no celular..."

                                                    g "Tudo por SUA culpa!"

                                                    mc triste "Mas..."

                                                    g "Não ache que ela vai ser sua..."

                                                    g "Eu não vou perder pra ninguém!"

                                                    mc desconfiado "Perder?"

                                                    if julia_namoro:

                                                        mc zerado "Agora a gente tá namorando, idiota..."

                                                        g "Isso não muda nada! A [s] vai ser minha!"

                                                        mc "Sem comentários..."

                                                    g "Hmpf!"

                                                elif sayuri_e2 == "fracasso":

                                                    show garconete bemvindo with dissolve

                                                    g "Haha! Foi muito fácil enganar você aquele dia que você veio com a [s]."

                                                    g "Além de fazer a [s] desconfiar de você, ainda dei uns beijos."

                                                    g "Adorei..."

                                                    mc zerado "..."

                                            elif nandom == 4:

                                                if v18_fim:

                                                    jump julia_opcao_tadaima

                                                g "Eu tô muito bem."

                                                g "Ontem fiquei com um carinha da faculdade. Foi mais ou menos... Mas é melhor beijar do que não beijar certo?"

                                                mc desconfiado "..."

                                                g "O quê?! Vai me dizer que você também não prefere pegar uma mina do que não pegar?"

                                                menu:
                                                    "Não tenho como negar...":


                                                        g "Tá vendo?"
                                                    "Eu só quero beijar uma garota.":


                                                        g "Mentiroso..."

                                            elif nandom == 5:

                                                g "A ilha que a gente vive parece que deixa as pessoas com os hormônios quentes..."

                                                g "Se você souber ir nos lugares certos, você vai encontrar um monte de gente afim de dar pra você."

                                                mc zerado "Por que você tem que falar assim?"

                                                show garconete perguntando with dissolve

                                                g "Você é muito puritano, [mc]..."

                                                if julia_namoro:

                                                    mc zerado "Você sabe que a gente tá namorando, né?"

                                                g "Carpe diem!"

                                            elif nandom == 6:

                                                label julia_opcao_tadaima:

                                                    if julia_namoro:

                                                        g "Agora que a gente tá namorando... eu tô tentando não ficar com ninguém."

                                                        mc charmoso "..."

                                                        show garconete perguntando with hpunch

                                                        g "Acho bom você fazer o mesmo, idiota! Ou vou dar pra todo mundo naquela faculdade!"

                                                        mc zerado "Que tipo de ameaça é essa..."

                                                    elif julia_e4 == "caio":

                                                        g "Eu tô tentando ter uma relação mais séria com o [caio]."

                                                        show garconete perguntando with hpunch

                                                        g "Mas eu sei que aquele puto tá me traindo."

                                                        g "Não importa! Eu vou ficar com todos os amigos dele também pra ele aprender."

                                                        g "E com todas as amigas também!"

                                                        mc preocupado "[g]..."
                                                    else:


                                                        g "Depois de todo aquele rolo com o [caio] eu tô dando um tempo de rapazes."

                                                        mc normal "Isso vai ser bom pra você."

                                                        g "Agora eu só fico com garotas. Até comecei a me aproximar daquela [mari]..."

                                                        mc zerado "..."

                                            jump julia_tadaima
                                        "Alguma novidade da [s]?":


                                            mc normal "Queria saber da [s]. Como ela tá?"

                                            show garconete perguntando with dissolve

                                            g "..."

                                            if julia_namoro:

                                                g "Sério que você vem conversar com sua namorada e pergunta de outra?!"
                                            else:


                                                g "Você vem falar com uma mina que tá dando mole pra você e pergunta de outra?"

                                            mc desculpa "..."

                                            g "Você não aprendeu nada no parquinho?"

                                            mc zerado "Parquinho?"

                                            jump julia_tadaima
                                        "Não é nada.":


                                            if v18_fim:

                                                if julia_namoro:

                                                    mc "Sempre que der eu venho falar com você, tá?"

                                                    g "Agora só quer saber de ficar de namorico comigo."

                                                    g "Volta logo..."

                                                elif julia_e4 == "caio":

                                                    mc preocupado "Tô indo nessa. Tenta se comportar, tá?"

                                                    g "Se comportar? Hahaha! Eu nunca me comportei, [mc]."

                                                    g "Vão todos ver o que eu posso fazer..."

                                                    mc preocupado "Só toma cuidado."
                                                else:


                                                    mc feliz "Até a próxima, amiga."

                                                    g "Amiga... por enquanto..."

                                                    mc zerado "..."
                                            else:


                                                mc normal "Por hora é isso, [g]."

                                                g "Venha mais vezes. Eu gosto de te ver."

                                            jump cenario_tadaima
                    else:


                        if mc_massagem == 6 and not karli_p_tadaima:

                            $ karli_p_tadaima = True

                            show ana t_ola with dissolve

                            ana "Bom dia, senhor."

                            if not nathan_e1 == "nada":

                                mc normal "Você é a [ana], não é? A gente se viu no bar aquela vez com o [n]."

                                ana "Isso mesmo. Seu nome era [mc], não é?"

                                mc "Isso!"

                                mc "Olha..."
                            else:


                                mc normal "Bom dia."

                                ana "Bom dia. E como é o nome senhor?"

                                mc "Eu sou o [mc]. Muito prazer."

                                ana "E eu sou [ana]. O prazer é todo meu."

                            mc desculpa "Você é nova aqui?"

                            ana "Sim. Comecei esses dias."

                            mc "Você sabe o que aconteceu com a outra garota que trabalhava de manhã antes de você?"

                            ana "O nome dela era... [m], não é?"

                            mc normal "Isso."

                            ana "Ela deixou o emprego de um dia pro outro. O chefe até ficou bravo com ela."

                            ana "Mas isso é tudo o que eu sei."

                            mc desculpa "Ok. Obrigado pela ajuda."

                            hide ana with dissolve

                            "Que estranho... Onde será que a [m] foi?"

                            jump call_cidade

                        if mc_massagem >= 6 and karli_p_tadaima:

                            show ana t_ola with dissolve

                            ana "Bom dia, senhor [mc]."

                            mc charmoso "Bom dia, [ana]. Lembrou meu nome?"

                            ana "Claro. Seu rostinho é bonito, [mc]."

                            mc "O seu também. Quem sabe a gente podia tomar alguma coisa juntos depois do seu expediente?"

                            ana "Quem sabe um dia desses?"

                            ana "Venha me visitar mais vezes."

                            mc "Com certeza."

                            ana "Agora eu tenho que atender aquele outro rapaz, mas volte, ok?"

                            mc "Pode deixar. Bom trabalho."

                            ana "Beijo."

                            hide ana with dissolve

                            "Essa [ana] sabe como provocar."

                            jump call_cidade

                        if not massagista_parque:

                            $ m_nome = "Garçonete"

                        show karli kimono with dissolve

                        if not cenario_salao_1vez:

                            $ massagista_bonita = True

                            $ m_nome = "Karli"

                            m "Fala aí, [mc]."

                            m "Como que as coisas estão indo?"

                            mc normal "Tudo bem, [m]. E você?"

                            m "Levando..."
                        else:


                            m "Bom dia, rapaz."

                        label massagista_tadaima:

                            m "Posso te ajudar com alguma coisa?"

                            if not massagista_bonita:

                                "Espera..."

                                "Eu tenho a impressão que já vi essa moça antes..."

                                "Mas não tô conseguindo lembrar onde ou quando que eu vi."

                                if massagista_parque:

                                    "É a moça que eu vi no parque de noite!"

                                    "O nome dela era [m]..."

                            menu:

                                "Acho que eu já te vi antes..." if not massagista_bonita and cenario_salao_1vez:

                                    $ massagista_bonita = True

                                    if massagista_parque:

                                        mc envergonhado "Eu te vi no parque, lembra?"

                                        mc "Eu sou aquele estranho que te abordou durante a noite."

                                        m "Verdade! Agora tô conseguindo ver sua cara direito."

                                        mc desculpa "Hehe..."

                                        mc normal "Então você trabalha aqui."

                                        m "Também."

                                        mc desconfiado "Você não trabalha só aqui?"
                                    else:


                                        mc envergonhado "Desculpa falar assim, eu juro que não é uma cantada, mas acho que eu já te vi em algum lugar."

                                        m "Ah?"

                                        m "..."

                                        m "Pra falar a verdade, sabia que eu acho que já te vi também?"

                                        mc normal "Sério?"

                                        m "Sim. Só que não sei onde foi."

                                        mc "Mesma coisa no meu caso."

                                        mc "Você mora aqui perto?"

                                        m "Na verdade, sim. Eu moro aqui perto."

                                        mc "Eu também."

                                        m "Acho que a gente se viu aqui perto então."

                                        mc "Pode ser..."

                                        mc normal "Você só trabalha aqui?"

                                    m "Não. Eu sou massagista também."

                                    mc "Que bacana."

                                    m "E você? Faz o quê?"

                                    mc "Eu sou jornalista. Trabalho em uma revista."

                                    m "Que legal."

                                    mc desculpa "Mais ou menos..."

                                    m "..."

                                    "Essa conversa tá meio estranha..."

                                    jump massagista_tadaima

                                "Você é a única garçonete aqui?" if massagista_bonita:

                                    mc normal "Só você trabalha aqui?"

                                    m "Não. Uma menina trabalha aqui no período da tarde."

                                    m "Ela é divertida, mas é meio estranha também..."

                                    mc desconfiado "..."

                                    m "Quero dizer, assim... Quando ela fala da irmã, ela parece meio estranha, sei lá."

                                    m "Mas isso não tem nada a ver comigo. Se você vier durante a tarde, você encontra ela."

                                    jump massagista_tadaima

                                "Eu pensei em comer aqui, mas é meio caro..." if massagista_bonita:

                                    mc desculpa "Eu tava procurando um lugar pra comer, mas eu vi os preços..."

                                    m "Pois é! Eu também me assustei com os preços quando comecei aqui."

                                    m "Mas se algum dia você ganhar na loteria e quiser algo, só voltar."

                                    mc "Obrigado..."

                                    jump cenario_tadaima
                "Não tenho nada pra fazer aqui.":


                    "Tenho lugares mais interessantes para visitar agora."

                    jump call_cidade
        else:


            scene restaurante jap_fora with Dissolve(1.0)

            "O Tadaima tá fechado essa hora..."

            "Parece que eles não oferecem janta."

            mc zerado "Eu nem tenho dinheiro pra jantar aqui mesmo."

        jump call_cidade

label cenario_onibus:

    $ estou_na_cidade = False

    if tempo < 3:

        scene cidade onibus with Dissolve(1.0)
    else:


        scene cidade onibus_noite with Dissolve(1.0)

        if not quincy_e1:

            jump quincy_evento2

    label cenario_onibus_menu:

        $ randh = random.randint(1,16)

        if randh == 1:

            "Pra onde eu vou?"

        elif randh == 2:

            "Daqui eu posso ir pra Cidade Chinesa, pra parte continental da capital e até pra outros lugares."

        elif randh == 3:

            "Ter que andar de busão... vida de pobre é complicada."

        elif randh == 4:

            "Com a chegada das máquinas, a construção dos carros ficou mais barata, mas o preço continua o mesmo. Que merda..."

        elif randh == 5:

            "Andar de busão polui menos o meio ambiente. Queria saber se quem descobriu isso vendeu o carro dele..."

        elif randh == 6:

            mc zerado "Vamos ver que tipo de balada vai ter no busão hoje..."

        elif randh == 7:

            "Se viver nessa ilha não fosse tão caro, dava pra comprar um carrinho com meu salário."

        elif randh == 8:

            "A ilha é só um pedacinho da capital. No centro tem muito mais coisa."
        else:


            pass

    call screen onibus_menu

    "..."

screen onibus_menu():
    tag cidade

    zorder 100
    modal True

    imagebutton auto "images/mapa/ilha_%s.png":
        xpos 1170
        ypos 520
        action Jump("call_cidade")
        at cidade_trans

    imagebutton auto "images/mapa/chinatown_%s.png":
        xpos 80
        ypos 60
        action Jump("cenario_chinatown")
        at cidade_trans

    imagebutton auto "images/mapa/cidade1_%s.webp":
        xpos 80
        ypos 180
        action Jump("ilha_cidade_bus")
        at cidade_trans







    if stifler_conheceu and stifler_e1 != "desistiu":

        imagebutton auto "images/mapa/distrito_%s.png":
            xpos 80
            ypos 300
            action Jump("cenario_distrito_tempo")
            at cidade_trans

label boutique_voltar_cidade:

    "Ir embora e voltar para a ilha?"

    menu:
        "Sim. Voltar para a ilha.":


            scene black with dissolve

            "Hora de voltar."

            jump call_cidade
        "Não. Permanecer na loja.":


            jump menu_roupa

label cenario_boutique:

    if tempo >= 3:

        "Ops. As lojas do centro fecham seis da tarde. Agora já tá tarde demais. Vou ter que deixar pra amanhã."

        jump cenario_onibus

    "Ir pra loja de roupas vai usar um período do meu dia."

    "Será que vale a pena?"

    mc envergonhado "Eu sou um cara muuuuuuito ocupado..."

    menu:
        "Pegar o ônibus até a loja de roupas":


            "Bora. Vamos comprar alguma coisa."

            "Ou pelo menos dar uma olhadinha nos preços e não levar nada..."

            call cena_onibus from _call_cena_onibus_11

            jump boutique
        "Vou deixar pra outra hora.":


            "Não tô tão afim de gastar agora, não."

            "Deixa pra próxima."

            jump cenario_onibus_menu

    label boutique:

        hide screen cidade_tela
        with dissolve

        $ tempo += 1

        scene boutique geral with Dissolve(1.0)

    "Eu tenho que ser muito masoquista mesmo pra querer comprar roupa nessa loja..."

    "O problema é que é a única que eu conheço."

    show atendente normal with dissolve

    "Atendente" "Olá, senhor. Como posso ajudar hoje?"

    mc normal "Vou dar uma olhada, qualquer coisa eu te chamo."

    "Atendente" "Certo. Fique à vontade."



    label menu_roupa:

        python:
            if renpy.android:
                cash = PythonSDLActivity.pegaCash()
                roupa_blacktie = PythonSDLActivity.pegaBlacktie()
                roupa_blazer = PythonSDLActivity.pegaBlazer()

        scene boutique geral with Dissolve(1.0)

        "Certo. Deixa eu ver o que vou olhar aqui hoje."

    call screen escolhe_roupa

    "..."

screen escolhe_roupa():

    imagebutton auto "images/mapa/ilha_%s.png":
        yalign 0.9
        yanchor 0.5
        xalign 0.5
        xanchor 0.5
        action Jump("boutique_voltar_cidade")
        at cidade_trans

    hbox:

        yalign 0.4
        yanchor 0.5
        xalign 0.5
        xanchor 0.5
        spacing 10

        if not roupa_blazer:

            imagebutton auto "extra/roupa_blazer_%s.png":
                action Jump("roupa_blazer")
                at cidade_trans

        else:

            add "extra/roupa_blazer_hover.png"

        if not roupa_blacktie:

            imagebutton auto "extra/roupa_blacktie_%s.png":
                action Jump("roupa_blacktie")
                at cidade_trans

        else:

            add "extra/roupa_blacktie_hover.png"

label roupa_blazer:

    show roupa_blazer with Dissolve(1.0)

    pause

    mc normal "Esse blazer aqui tá bem legal. Seria muito bom se eu pudesse ter um desses pra ir no {b}Cassino{/b}."

    ate normal "Realmente. Ir em lugares de alta classe como o Cassino da ilha com essa roupa que você tá usando agora..."

    mc zerado "..."

    mc normal "Mas você tem razão."

    ate "Não se preocupe que ele está bem em conta."

    label roupa_blazer_menu:

        scene boutique geral with Dissolve(1.0)

        ate normal "O que você quer saber sobre o {b}Blazer{/b}?"

    menu:
        "Me fale sobre esse {b}Blazer{/b}.":


            show roupa_blazer with Dissolve(1.0)

            ate "O blazer é uma escolha moderna e coloquial em um cenário fino."

            mc desconfiado "Como?"

            ate "Em um ambiente fino como o Cassino, ele é considerado despojado e moderno. É uma excelente escolha."

            ate "O {b}Black Tie{/b} seria a escolha mais clássica e requintada, mas o blazer é moderno e coloquial."

            mc "Então para visitar o Cassino ele está bom?"

            ate "Com certeza. Ele é extremamente indicado, ainda mais pela idade do senhor que ainda é jovem."

            mc normal "Obrigado. Entendi..."

            ate "O preço dele é {b}R$ 500{/b}, mas eu consigo fazer para o senhor por apenas {b}R$ 250{/b} se o senhor levar hoje."

            mc desculpa "É um bom desconto..."

            ate "Com certeza. Eu recomendaria o senhor levar logo de uma vez."

            mc "Ok..."

            jump roupa_blazer_menu
        "Eu posso experimentar ele?":


            mc normal "Eu gostaria de experimentar ele, se não for muito incômodo."

            ate "Claro que não. Eu vou pegar ele pro senhor. Os provadores ficam ali atrás."

            mc "Ok."

            scene boutique trocador with Dissolve(1.0)

            "..."

            "Ela disse que o blazer é moderno e despojado. Seria um grande upgrade se comparado com esta roupa que eu uso sempre."

            show atendente normal with dissolve

            ate "Pronto. Aqui está."

            mc normal "Obrigado. Vou experimentar aqui..."

            ate "Se o senhor não se importar, eu gostaria de ver como ficou."

            mc "Seria legal ter sua opinião."

            "..."

            scene boutique roupa with Dissolve(1.0)

            "..."

            mc "Estou pronto."

            ate normal "Deixa eu ver."

            show mc roupa_blazer_total with dissolve

            show mc roupa_blazer_total at cena_sobe

            pause

            show mc roupa_blazer with dissolve

            pause

            mc "Ficou bom?"

            ate "Ficou, sim. O senhor está muito bonito."

            mc "Obrigado. Eu gostei também."

            ate "Caiu melhor do que eu imaginava em você."

            mc "Legal."

            ate "Posso fechar o pedido enquanto o senhor se apronta?"

            menu:
                "Certo. Vou comprar este {b}Blazer{/b}.":


                    jump comprar_blazer
                "Vou pensar mais um pouco.":


                    mc "Este blazer é o que eu preciso, mas vou pensar um pouco antes de fechar."

                    ate "Sem problemas. Vamos lá pra frente."

                    mc "Ok. Vou me trocar e vamos pra lá."

                    scene black with Dissolve(1.0)

                    "..."

                    jump roupa_blazer_menu
        "Vou comprar o {b}Blazer{/b}.":


            label comprar_blazer:

                "Hmm..."

                python:
                    if renpy.android:
                        cash = PythonSDLActivity.pegaCash()

                "Quanto que eu tenho mesmo?"

                "Eu estou com {b}R$ [cash]{/b}. Ela disse que com o desconto o blazer vai ficar em R$ 250..."

                if cash >= 250:

                    "Que beleza. Eu tenho grana suficiente pra comprar ele."

                    mc "Eu vou querer levar o blazer."

                    ate normal "Muito bom! Vamos para o caixa."

                    mc "Ok."

                    scene boutique caixa with Dissolve(1.0)

                    show atendente normal with dissolve

                    ate "Ficou R$ 250 com o desconto que falei."

                    mc normal "Perfeito."

                    python:
                        if renpy.android:
                            cash = PythonSDLActivity.pegaCash()
                            
                            if cash >= 250:
                                
                                PythonSDLActivity.compraBlazer()

                    $ renpy.block_rollback()

                    mc "Aqui está."

                    play sound "extra/carta.mp3"

                    "{b}Você usou R$ 250 e adquiriu Blazer!{/b}"

                    ate "Aqui está a sacola."

                    mc normal "Obrigado."

                    ate "Parabéns pela compra."

                    mc normal "Valeu!"

                    ate "Espero ver você de novo comprando aqui."

                    mc normal "Com certeza. Obrigado."

                    scene boutique geral with Dissolve(1.0)

                    "Com esse blazer vou poder impressionar muito mais os visitantes no Cassino."

                    "Agora sim tô ficando estiloso."

                    mc desconfiado "Pelo jeito que eu pensei agora parece que as pessoas vão gostar do blazer e não de mim..."

                    mc "Que estranho..."

                    jump call_cidade
                else:


                    "Merda... Não tenho grana pra levar."

                    show black with dissolve

                    p rindo "Parece que o [mc] tá querendo comprar o blazer, mas tá pobretão como sempre."

                    p "Você pode ajudar ele com dinheiro do seu mundo se você quiser."

                    p "{b}R$ 250{/b} para o [mc] comprar o blazer custa {b}R$ 4,90{/b} do seu mundo."

                    menu:
                        "Ok. Vou comprar.":


                            call comprar_250reais from _call_comprar_250reais

                            "..."

                            python:
                                if renpy.android:
                                    cash = PythonSDLActivity.pegaCash()

                            "..."

                            if cash >= 250:

                                p rindo "Agora você tem o dinheiro necessário pra comprar o {b}Blazer{/b}."

                                p "Vou voltar o [mc] no tempo pra que ele possa comprar."

                                p "Já parou pra pensar como uma fada tem o poder de fazer alguém voltar no tempo?"

                                p "Estranho, né?"

                                jump comprar_blazer
                            else:


                                p lecionando "Parece que sua compra não funcionou. Ou se você comprou com sucesso, talvez demore um pouquinho pra chegar na sua conta."

                                p rindo "Vou deixar você continuar e daí daqui a pouco você pode tentar novamente."

                                p "E não esqueça que você também pode juntar dinheiro trabalhando no bar!"

                                p "Bom jogo!"
                        "Não tem como. Tô pobre igual ele...":


                            p rindo "Não tem problema. Você pode juntar dinheiro trabalhando no bar."

                            p "Com determinação e paciência logo você terá o dinheiro!"

                            p "Ou junte aquela graninha e dê uma força pra ele."

                    hide black with dissolve

                    "Vou ter que trabalhar duro pra juntar essa grana."

                    jump blazer_naocomprar
        "Vou pensar melhor e te chamo.":


            label blazer_naocomprar:

                mc "Vou pensar melhor e te chamo."

            ate "Ok, senhor. Estou sempre por aqui."

            mc "Obrigado pela atenção."

            ate "Por nada."

            hide atendente with dissolve

            jump menu_roupa

label roupa_blacktie:

    show blacktie with Dissolve(1.0)

    pause

    mc surpreso "Uou! Esse Black Tie é incrível!"

    ate normal "Concordo com você."

    mc envergonhado "Opa. Você tava aí?"

    ate "Eu vou ajudar o senhor. Eu posso te falar sobre ele, te ajudar a experimentar ou fechar o pedido."

    label roupa_blacktie_menu:

        scene boutique geral with Dissolve(1.0)

        ate normal "E então? O que o senhor vai querer?"

        menu:
            "Me fale sobre esse {b}Black Tie{/b}.":


                show blacktie with Dissolve(1.0)

                ate normal "Esse Black Tie é perfeito para lugares frequentados pela alta sociedade."

                ate "É perfeito para usar no {b}Cassino{/b} por exemplo."

                ate "Com um desses com certeza você chamaria a atenção das pessoas certas."

                ate "É também uma forma de você impressionar a garota dos seus sonhos."

                ate "Este é sem dúvida um dos itens mais caros que temos na loja. Ele custa normalmente {b}R$ 3.500{/b}."

                ate "Mas usando meu desconto de vendedora, se você levar ele hoje, ele sai por apenas {b}R$ 1.000{/b}."

                mc surpreso "Que pechincha!"

                ate "Com certeza. Eu aproveitaria o quanto antes."

                jump roupa_blacktie_menu
            "Eu quero experimentar ele.":


                mc normal "Eu gostaria de experimentar ele, se não for muito incômodo."

                ate "Claro que não. Eu vou pegar ele pro senhor. Os provadores ficam ali atrás."

                mc "Ok."

                scene boutique trocador with Dissolve(1.0)

                "..."

                "Com certeza esse Black Tie vai ficar perfeito. Não tem como. Esse é um traje de outro nível."

                show atendente normal with dissolve

                ate "Aqui está."

                mc normal "Obrigado. Vou experimentar e já saio."

                ate "Se o senhor não se importar, eu gostaria de ver como ficou."

                mc "Sem problemas."

                "..."

                scene boutique roupa with Dissolve(1.0)

                "..."

                mc "Estou pronto."

                ate normal "Deixa eu ver."

                show mc roupa_blacktie_total with dissolve

                show mc roupa_blacktie_total at cena_sobe

                pause

                show mc roupa_blacktie with dissolve

                pause

                mc "E aí? Como ficou?"

                ate "Ficou excelente! O senhor está realmente muito bonito."

                ate "E... se permite... sexy..."

                mc "Obrigado. Eu também achei que ficou muito bom."

                ate "Ficou muito melhor do que bom. Pode acreditar em mim."

                ate "Posso fechar o pedido enquanto o senhor se apronta?"

                menu:
                    "Certo. Vou comprar o {b}Black Tie{/b}.":


                        jump comprar_blacktie
                    "Vou pensar mais um pouco.":


                        mc "Este Black Tie é incrível, mas eu preciso pensar um pouco antes."

                        ate "Sem problemas. Vamos lá pra frente."

                        mc "Ok. Vou me trocar e vamos pra lá."

                        scene black with Dissolve(1.0)

                        "..."

                        jump roupa_blacktie_menu
            "Vou comprar o {b}Black Tie{/b}.":


                label comprar_blacktie:

                    "Hmm..."

                    python:
                        if renpy.android:
                            cash = PythonSDLActivity.pegaCash()

                    "Quanto que eu tenho mesmo?"

                    "Eu estou com {b}R$ [cash]{/b}. Ela disse que com o desconto esse smoking custa R$ 1.000..."

                    if cash >= 1000:

                        "Que beleza. Eu tenho grana suficiente pra comprar ele."

                        mc "Eu vou querer levar este incrível Black Tie."

                        ate normal "É uma excelente aquisição, senhor. Vamos para o caixa."

                        mc "Ok."

                        scene boutique caixa with Dissolve(1.0)

                        show atendente normal with dissolve

                        ate "Ficou R$ 1.000 com aquele desconto especial que lhe falei."

                        mc normal "Perfeito."

                        python:
                            if renpy.android:
                                cash = PythonSDLActivity.pegaCash()
                                
                                if cash >= 1000:
                                    
                                    PythonSDLActivity.compraBlacktie()

                        $ renpy.block_rollback()

                        mc "Aqui está."

                        play sound "extra/carta.mp3"

                        "{b}Você usou R$ 1.000 e adquiriu Black Tie!{/b}"

                        ate "O seu produto."

                        mc normal "Obrigado."

                        ate "Parabéns pela excelente compra."

                        mc normal "Valeu!"

                        ate "Espero ver você de novo comprando em nossa loja."

                        menu:
                            "Só quando você estiver trabalhando aqui.":


                                mc charmoso "Só quando você estiver trabalhando aqui. Assim eu posso te ver."

                                ate "Vou ficar te esperando, então."

                                mc "Combinado."

                                ate "Beijos."

                                mc "Beijo."
                            "Quando eu precisar de roupa eu volto.":


                                mc normal "Pode deixar. Quando eu precisar comprar um traje novamente eu volto."

                                ate "Estarei aqui."

                                mc "Até."

                                ate "Até."

                        scene boutique geral with Dissolve(1.0)

                        "Caraca. Esse Black Tie é muito foda! Estou me sentindo muito bem de ter comprado ele."

                        "Tenho certeza que minhas idas ao Cassino vestido assim vão dar o tom certo pra minha noite."

                        mc desconfiado "Será que eu tô virando um consumista?"

                        jump call_cidade
                    else:


                        "Que droga. Eu não tenho grana pra tudo isso, não..."

                        show black with dissolve

                        p rindo "Parece que o [mc] tá querendo dar uma de riquinho, mas tá pobretão como sempre."

                        p "Você pode ajudar ele com dinheiro do seu mundo se você quiser."

                        p "{b}R$ 1.000{/b} para o [mc] comprar o Black Tie dele custa {b}R$ 17,90{/b} do seu mundo."

                        menu:
                            "Ok. Vou comprar.":


                                call comprar_milreais from _call_comprar_milreais

                                "..."

                                "..."

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "..."

                                if cash >= 1000:

                                    p rindo "Agora você tem o dinheiro necessário pra comprar o Black Tie."

                                    p "Vou voltar o [mc] no tempo pra que ele possa comprar."

                                    p "Já parou pra pensar como uma fada tem o poder de fazer alguém voltar no tempo?"

                                    p "Estranho, né?"

                                    jump comprar_blacktie
                                else:


                                    p lecionando "Parece que sua compra não funcionou. Ou se você comprou com sucesso, talvez demore um pouquinho pra chegar na sua conta."

                                    p rindo "Vou deixar você continuar e daí daqui a pouco você pode tentar comprar novamente."

                                    p "E não esqueça que você também pode juntar dinheiro trabalhando no bar!"

                                    p "Bom jogo!"
                            "Não tem como. Tô pobre igual ele...":


                                p rindo "Não tem problema. Você pode juntar dinheiro trabalhando no bar."

                                p "Com determinação e paciência logo você terá o dinheiro!"

                                p "Ou junte aquela graninha e dê uma força pra ele."

                        hide black with dissolve

                        "Vou ter que trabalhar duro pra juntar essa grana."

                        jump blacktie_naocomprar
            "Vou pensar melhor e te chamo.":


                label blacktie_naocomprar:

                    mc "Vou pensar melhor e te chamo."

                ate "Ok, senhor. Estou sempre por aqui."

                mc "Obrigado pela atenção."

                ate "Por nada."

                hide atendente with dissolve

                jump menu_roupa

screen ap_tela():
    tag ap

    predict False
    zorder 100
    modal True

    if not ap_comodo == "sala":

        imagebutton auto "images/mapa/ap_%s.png":
            xalign 0.05
            yalign 0.95
            action Call("ap_sala_menu")


    else:

        imagebutton auto "images/mapa/ilha_%s.png":
            xalign 0.05
            yalign 0.95
            action [ Hide("ap_tela"), Jump("call_cidade") ]


        if karli_casa and karli_esta:

            imagebutton auto "images/mapa/ap_karli_falar_%s.png":
                xalign 0.05
                yalign 0.55
                action Call("ap_karli_falar")

        elif xiang_casa:

            imagebutton idle "extra/xiang_casa.webp":
                xalign 0.05
                yalign 0.55
                action Call("ap_xiang_falar")

        imagebutton auto "images/mapa/ap_mc_tv_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("ap_mc_tv")

        if ( carro_evento == 1 or carro_evento == 2 ) and carro_gina < 3:

            imagebutton idle "images/botao_gina.webp":
                xalign 0.15
                yalign 0.75
                action Call("carro_antes")

    if not ap_comodo == "quarto":

        imagebutton auto "images/mapa/ap_quarto_%s.png":
            xalign 0.15
            yalign 0.95
            action Call("ap_quarto_menu")


    else:

        add "images/mapa/ap_quarto_hover.png":
            xalign 0.15
            yalign 0.95

        imagebutton auto "images/mapa/ap_mc_dormir_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("ap_mc_dormir")


    if not ap_comodo == "cozinha":

        imagebutton auto "images/mapa/ap_cozinha_%s.png":
            xalign 0.25
            yalign 0.95
            action Call("ap_cozinha_menu")


    else:

        imagebutton auto "images/mapa/ap_mc_comendo_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("ap_mc_comendo")


        add "images/mapa/ap_cozinha_hover.png":
            xalign 0.25
            yalign 0.95

    if not ap_comodo == "banheiro":

        imagebutton auto "images/mapa/ap_banheiro_%s.png":
            xalign 0.35
            yalign 0.95
            action Call("ap_banheiro_menu")


    else:

        imagebutton auto "images/mapa/ap_mc_chuveiro_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("ap_mc_chuveiro")


        imagebutton auto "images/mapa/ap_mc_banheira_%s.png":
            xalign 0.15
            yalign 0.75
            action Call("ap_mc_banheira")


        add "images/mapa/ap_banheiro_hover.png":
            xalign 0.35
            yalign 0.95

label ap_mc_banheira:

    hide screen ap_tela

    scene ap mc_banheira with Dissolve(1.0)

    pause

    "Simplesmente delicioso..."

    "Tenho que admitir. Acho que a banheira é o maior diferencial do novo apê."

    "A vontade é de nunca sair daqui."

    "Pena que os dedos ficam enrugados e começam a me irritar."

    "..."

    window hide

    pause

    mc "Tá bom por agora. Quem sabe depois eu volto..."

    jump ap_banheiro_menu

label ap_mc_chuveiro:

    hide screen ap_tela

    play sound "audio/som_16_chuveiro.mp3"

    scene ap mc_chuveiro with Dissolve(1.0)

    pause

    if tempo == 3:

        "Nada como tomar um banho antes de dormir."

    elif tempo == 2:

        "Tá acabando o dia. Bora dar aquela refrescada."

    elif tempo == 1:

        "Melhor coisa que tem pra acordar é começar o dia com um banho gelado."

    "O condomínio é caro, mas pelo menos a água tá inclusa."

    "Me desculpa planeta. Mas vou ficar uns 30 minutos..."

    "..."

    mc "Delícia!"

    $ tempo += 1

    jump ap_sala_menu

label ap_mc_comendo:

    hide screen ap_tela

    mc tarado "Deixa eu bater aquele lanchão."

    if karli_casa:

        "Tenho que ser rápido antes que a [m] veja e também queira."

    scene ap mc_cozinhando1 with Dissolve(1.0)

    "Muitas vezes menos é mais. Não adianta enfiar mil coisas em um lanche achando que vai ficar mais gostoso."

    "Às vezes a combinação do básico é tudo o que você precisa."

    "Pronto!"

    scene ap mc_cozinhando2 with Dissolve(1.0)

    pause

    mc "Delícia!"

    "Tenho que comer isso mais vezes."

    $ tempo += 1

    jump ap_cozinha_menu

label ap_karli_falar:

    hide screen ap_tela

    if not karli_evento_dia:

        $ karli_evento_dia = True

        scene ap_karli sofa with Dissolve(1.0)

        mc normal "E aí, [m]?"

        m "Fala, [mc]. O que foi?"

        menu:
            "Só queria trocar uma ideia":


                mc normal "Só queria conversar contigo um instante. Sem compromisso."

                m "Então senta aí, mano."

                if karli_evento_falar == 0:

                    $ karli_evento_falar += 1

                    call karli_evento_falar1 from _call_karli_evento_falar1

                elif karli_evento_falar == 1:

                    $ karli_evento_falar += 1

                    call karli_evento_falar2 from _call_karli_evento_falar2
                else:


                    call karli_evento_falar3 from _call_karli_evento_falar3
            "Quer comer um lanche?":


                if karli_evento_comer == 0:

                    $ karli_evento_comer += 1

                    call karli_evento_comer1 from _call_karli_evento_comer1

                elif karli_evento_comer == 1:

                    $ karli_evento_comer += 1

                    call karli_evento_comer2 from _call_karli_evento_comer2

                elif karli_evento_comer == 2:

                    $ karli_evento_comer += 1

                    call karli_evento_comer3 from _call_karli_evento_comer3
                else:


                    call karli_evento_comer4 from _call_karli_evento_comer4

        $ tempo += 1

        jump ap_sala_menu
    else:


        "Eu e a [m] já passamos um tempo juntos hoje. Melhor deixar pra amanhã."

        jump ap_sala_menu

label ap_xiang_falar:

    hide screen ap_tela with Dissolve(0.3)

    if not xiang_evento_dia:









        if xiang_casa_evento == 22:

            "Meus dias aqui em casa nunca mais foram os mesmos com estas duas..."

            "Eu quero aproveitar o tempo delas aqui o máximo que eu puder!"

            "Vou me divertir... mas também quero proteger elas de qualquer coisa que ameace as duas."

            "E eu tenho certeza que elas vão me proteger de qualquer coisa também..."

            "As coisas nunca foram tão bacanas."

            show screen ap_tela with Dissolve(0.3)

            pause

        if xiang_casa_evento > 12:

            menu:
                "Vou me divertir com a Xiang":


                    if randh > 18:

                        "Pena que ela não tá aqui na sala agora..."

                        show screen ap_tela with Dissolve(0.3)

                        pause

                    "Hoje eu quero um tempo sozinho com a minha gatinha esquisitinha."
                "Vou passar um tempo com a He Xiangu":


















                    if randh > 12:

                        "Pena que ela não tá aqui na sala agora..."

                        show screen ap_tela with Dissolve(0.3)

                        pause





























                    if xiang_casa_evento == 11:

                        "Eu decidi que ia ser só amigo da Xiang... e agora vou me atracar com a amiga dela?"

                        "Se eu for fazer algo com a Xiangu... eu vou ter que pegar a Xiang também. Seria muita injustiça deixar ela de lado."

                        menu:
                            "Eu e a Xiang seremos mais que amigos.":


                                "Chega de amizade Xiang... eu e você vamos ter o que no fundo a gente sempre quis!"
                            "Eu vou continuar amigo da Xiang":


                                "É melhor mesmo eu abandonar toda essa ideia de ficar com elas."

                                scene black with dissolve

                                jump ap_sala_menu

                    $ xiang_evento_dia = True

                    if xiang_casa_evento < 14:

                        $ xiang_casa_evento = 14

                        mc "Garotas? Tudo bem?"

                        i "Tudo! O [mc] tá com tempo agora?"

                        mc "Por quê?"

                        scene black with dissolve

                        scene xiangu_casa2 with Dissolve(1.0)

                        xu "X-xiang?!"

                        i "A Xiang queria passar um tempo entre a gente!"

                        xu "Quantas vezes eu te falei pra você não me pegar assim?!"

                        i "Você não sabe o que tá perdendo!"

                        xu "Eu..."

                        i "Fala pra ela, [mc]!"

                        mc "Bom... namorar realmente é gostoso..."

                        xu "E-eu... eu não tenho esse tipo de desejo. Eu sou pura como a He Xiangu da lenda."

                        i "Você só tá com medo, isso sim!"

                        xu "Eu não tenho medo de nada!"

                        i "Se não é medo... então a Xiang teve uma ideia!"

                        mc "Não sei se eu gosto quando você tem ideias... você é meio maluquinha."

                        i "Vem aqui!"

                        scene black with hpunch

                        mc "E-ei!"

                        scene xiang_ape9 with hpunch

                        mc "O que você tá fazendo, Xiang?!"

                        xu "A-ah!"

                        i "Vamos mostrar pra ela o que ela tá perdendo!"

                        xu "Por que ele tá sem roupa?! Mostrando... a... a coisa dele assim!"

                        scene black with hpunch

                        scene xiang_ape11 with vpunch

                        mc "Xiang!"

                        i "Olha só pra ele... [xu]... pro pau dele... não é suculento?"

                        xu "Q-quê?!"

                        i "Você não tem vontade de sentir ele... de pegar nele... e chegar pertinho..."

                        xu "Isso é um absurdo!"

                        mc "Xiang! Você tá indo com mu-"

                        i "Olha aqui!"

                        scene xiang_ape12 with vpunch

                        mc "Hmm!"

                        i "Hmmm..."

                        xu "Aah..."

                        i "Olha como eu beijo ele... escuta os barulhos... hmmm..."

                        mc "Nnngh..."

                        xu "E-eu..."

                        i "Olha como o caralho dele fica maior... mais duro... quando ele sente os peitos da Xiang nele..."

                        i "Homens adoram nossos peitos, sabia?"

                        xu "V-verdade?"

                        i "Ele vai pegar neles... apertar eles... você vai sentir muito gostoso... por ele brincar com seus peitos igual um brinquedo."

                        xu "Ah..."

                        xu "Eu tenho que ir embora!"

                        i "Calma!"

                        mc "Parece que ela foi embora..."

                        i "A gente vai pegar ela na próxima! E agora a Xiang vai aproveitar você aqui pra transar com ela!"

                        mc "Sem problemas... agora que você me deixou duro desse jeito..."

                        i "Ebaaa!"

                    elif xiang_casa_evento == 14:

                        $ xiang_casa_evento = 15

                        mc "O que vocês tão planejando hoje?"

                        i "Espera! [xu]!"

                        scene black with dissolve

                        scene xiangu_casa2 with Dissolve(1.0)

                        xu "Xiang!"

                        i "A Xiang quer que você perca essa vergonha!"

                        xu "Eu já disse que não é isso! Eu não tenho desejos carnais imundos!"

                        i "Mas desejos carnais imundos são deliciosos!"

                        mc "Ela tem razão, [xu]... sexo com alguém que você gosta é muito bom..."

                        xu "Eu... vocês não vão me convencer..."

                        i "Vamos mostrar pra ela de novo."

                        mc "Ok... se ela não sair correndo de novo."

                        xu "Eu... eu não vou..."

                        scene black with dissolve

                        scene xiang_ape12 with Dissolve(1.0)

                        i "Hmmm... beijar é tão bom! Sentir a lingua dele na sua boca..."

                        mc "É sim... você é muito gostosa, [i]..."

                        xu "Vocês... fazendo esse tipo de coisa..."

                        i "Você vai adorar beijar, Xiangu... a Xiang tem certeza!"

                        xu "Eu... beijar assim alguém..."

                        i "Você não viu nada..."

                        scene xiang_ape14 with Dissolve(1.0)

                        i "Aii..."

                        mc "Xiang... você é muito boa..."

                        xu "O q-que é isso? Sexo?"

                        mc "A gente tá transando, é..."

                        i "Olha como o pau dele entra gostoso na Xiang... hmmm... é tão gostoso... aah..."

                        i "Quando eu me esfrego assim nele! Aiinn!"

                        mc "S-sim! Nghh!"

                        xu "Esse... esse tipo de coisa..."

                        i "Ahnn! Assim! Faz mais!"

                        mc "Vem aqui!"

                        scene xiang_ape15 with vpunch

                        i "Assim! Aahhnn!"

                        xu "Isso... é... tão bom assim?"

                        i "Mete na Xiang! Aaahhhh!"

                        mc "Xiannnng!"

                        xu "Vocês... não tão nem me ouvindo..."

                        i "A Xiang vai gozarrr!"

                        mc "Eu também! Eu vou jorrar tudo dentro de você, Xiang!"

                        mc "Nnnghhh!"

                        xu "Minha nossa... isso..."

                        xu "Hmmm..."

                    elif xiang_casa_evento == 15:

                        $ xiang_casa_evento = 16

                        i "Que bom que você tá aqui!"

                        xu "L-lá vem ela!"

                        scene black with dissolve

                        scene xiangu_casa2 with Dissolve(1.0)

                        i "Cheguei!"

                        mc "Hehe... eu tô começando a gostar disso..."

                        xu "..."

                        mc "Não vai reclamar dessa vez, [xu]?"

                        xu "E adianta? Ela só faz o que ela quer..."

                        i "A Xiang sabe o que é bom pra você! Vai falar que não gostou de ver a gente trepando, hein?"

                        xu "A-absurdo..."

                        mc "Xiang... você não tem filtro mesmo, né?"

                        i "Hoje você vai querer ficar com ele?"

                        xu "Eu? Eu..."

                        i "A Xiang vai preparar ele pra você!"

                        mc "Q-que?!"

                        scene black with vpunch

                        scene xiang_ape9 with hpunch

                        mc "EII!"

                        i "Você não vai querer pegar ela com esse pintinho mole, né?!"

                        mc "Você não pode ir tirar minha roupa assim só porque você é mais forte do que eu!"

                        i "Não precisa ficar triste! A Xiang é mais forte que todo mundo!"

                        mc "N-não é essa a questão!"

                        i "Para de ser chato... a [xu] tá pronta..."

                        xu "E-eu..."

                        i "Vai logo, [mc]! Você tem que tomar a dianteira ou ela nunca vai aceitar!"

                        xu "A-ah..."

                        menu:
                            "Ok. Vem aqui, [xu].":


                                mc "Ok. Se tá dependendo de mim... Vem aqui."
                            "É melhor a gente esquecer isso.":


                                mc "Você não quer fazer isso, né, [xu]?"

                        xu "E-eu..."

                        scene black with dissolve

                        i "Vai logo garota!"

                        xu "!!!"

                        scene xiangu_sexo1 with Dissolve(1.0)

                        pause

                        xu "Eu não..."

                        mc "É só um beijo, Xiangu..."

                        xu "Você sem roupa me apertando assim..."

                        i "Não é gostoso quando um homem te pegar assim?"

                        xu "Nunca pensei que... ah... ele tá me apertando forte."

                        i "Assim que é bom, boba..."

                        xu "Eu tô ficando fraca..."

                        mc "Vem... me dá um beijo só."

                        xu "Ai... hmmm... você tá beijando meu pescoço... ah..."

                        i "O [mc] também não perde tempo... já tá experimentando ela inteirinha."

                        xu "Aah..."

                        xu "E-eu tenho que sair daquí!"

                        mc "[xu]!"

                    elif xiang_casa_evento == 16:

                        $ xiang_casa_evento = 17

                        mc "[xu]... pronta pra continuar... o que a gente tava..."

                        xu "Eu..."

                        i "Vai logo!"

                        xu "..."

                        mc "Vem aqui."

                        scene black with dissolve

                        scene xiangu_sexo1 with Dissolve(1.0)

                        mc "Que bom que você quis vir..."

                        xu "Não é que eu queira... só quero ter certeza que eu realmente não gosto disso..."

                        mc "Você tá aceitando experimentar uma coisa nova. Isso é muito bom."

                        i "Todo mundo aqui sabe que logo logo você vai tá implorando pra transar com ele."

                        mc "Não escuta ela... só deixa eu pegar em você... e te beijar."

                        xu "Aahn... isso de novo? Hmmm..."

                        mc "É gostoso, não é? Sentir um carinho assim?"

                        xu "Ah... n-não sei... eu fico ofegante... aah... e meu corpo tá mole.. nngh..."

                        mc "É assim mesmo."

                        xu "E-eu quase não penso em nada."

                        mc "Vem. Me beija."

                        scene black with dissolve

                        scene xiangu_sexo2 with Dissolve(1.0)

                        pause

                        xu "Ah..."

                        mc "Isso... usa sua língua assim..."

                        xu "Ahnn... a gente tá se lambendo... isso... ah..."

                        i "Isso é muito gostoso... a Xiang tá babando só de olhar..."

                        xu "Ah... hmmm... nossos lábios... essa língua na minha boca... aaah..."

                        mc "É que você é saborosa demais, Xiangu..."

                        xu "Nnnghh! V-você acha mesmo?"

                        mc "Sim... eu tô adorando beijar você..."

                        i "A Xiang também quer uma língua na boca dela..."

                        xu "Ela... ah.. tá na minha boca agora... aah..."

                        mc "Viu só como é gostoso?"

                        menu:
                            "Agora é hora da gente continuar.":


                                pass

                        mc "Beijar é gostoso... mas tem coisa ainda melhor, sabia?"

                        i "S-sim... a Xiang adora... coisa muito melhor..."

                        xu "Q-quê?"

                        mc "Não precisa ficar nervosa. Eu vou te mostrar."

                        scene black with dissolve

                        scene xiangu_sexo3 with Dissolve(1.0)

                        pause

                        xu "!!!"

                        xu "O que você tá fazendo?!"

                        i "É a melhor parte, Xiangu..."

                        xu "E-eu não quero a 'melhor parte'!"

                        mc "Você fala isso porque você ainda não experimentou."

                        xu "Toma essa!"

                        scene black with vpunch

                        mc "AAARRGHH!!!"

                        i "Xi..."

                    elif xiang_casa_evento == 17:

                        $ xiang_casa_evento = 18

                        mc "[xu]..."

                        xu "S-sim..."

                        scene black with dissolve

                        scene xiangu_sexo2 with Dissolve(1.0)

                        pause

                        mc "Ah... eu adoro te beijar."

                        xu "Hmm... sua língua..."

                        i "Desde quando os dois tão se beijando assim sem cerimônia, hein?"

                        xu "E-eu... é tudo culpa dele que... ah... me puxa... e... me beija assim... hmm... tarado..."

                        mc "Eu vou te beijar todo dia."

                        xu "Ah..."

                        i "Mas e a Xiang?!"

                        mc "A gente ficou bastante... deixa eu ficar com ela um pouquinho."

                        i "Hmm..."

                        xu "Não fala se tá me beijando."

                        mc "D-desculpa. Mas eu não quero só beijar. Eu quero sentir mais."

                        scene black with dissolve

                        scene xiangu_sexo3 with Dissolve(1.0)

                        xu "De novo isso?!"

                        mc "Calma... você gostou de beijar. Eu não vou fazer nada que você não goste."

                        xu "Isso é demais... minha roupa..."

                        mc "Eu vou te ajudar."

                        scene black with dissolve

                        scene xiangu_sexo4 with Dissolve(1.0)

                        pause

                        xu "Eu estou nua..."

                        mc "E seu corpo é lindo. Você é uma mulher perfeita, Xiangu."

                        i "É mesmo... você tem mais corpo que a Xiang."

                        mc "Você também é gostosa demais, Xiang."

                        i "Obrigada, [mc]. A Xiang gosta que você gosta do corpo da Xiang."

                        xu "Você realmente me acha bonita?"

                        mc "Com certeza. Olha pra esses peitos redondinhos, cinturinha... e essa coxa malhada..."

                        xu "T-tudo bem... não precisa falar tanto assim... e agora?"

                        mc "Agora você vem aqui e me beija."

                        xu "Assim? Pelada?"

                        mc "Sim. Vem aqui."

                        scene black with dissolve

                        scene xiangu_sexo5 with Dissolve(1.0)

                        pause

                        xu "Nggh..."

                        mc "Não é gostoso assim?"

                        xu "A gente tá se beijando pelados."

                        i "Sim... parece tão gostoso..."

                        xu "Ahnn... eu tô... sem ar..."

                        mc "Deixa eu te beijar mais!"

                        xu "Aah... ahnnn..."

                        mc "Tá gostando?"

                        xu "Hmm... me beija..."

                        mc "Com certeza..."

                        xu "Hmmm..."

                        scene black with dissolve

                        xu "Eu quero mais..."

                    elif xiang_casa_evento == 18:

                        $ xiang_casa_evento = 19

                        xu "[mc]..."

                        mc "Quer beijar?"

                        xu "Sim... mas... eu quero que você tire a roupa. Eu também vou."

                        mc "É mais quente assim, não é?"

                        scene black with dissolve

                        scene xiangu_sexo6 with Dissolve(1.0)

                        pause

                        xu "Sim... eu senti algo muito mais intenso te beijando sem roupa... no chão."

                        i "Igual dois animais?"

                        mc "Xiang... calma..."

                        xu "Ela tem razão."

                        mc "T-tem?"

                        xu "Eu sinto isso cada vez mais. Menos deusa e mais animal."

                        i "E é muito melhor, né?"

                        xu "Eu não sei... mas eu preciso experimentar mais. Me beija, [mc]."

                        mc "É aqui que eu entro."

                        scene black with dissolve

                        scene xiangu_sexo5 with Dissolve(1.0)

                        xu "Eu não consigo resistir... ah... é intenso demais!"

                        mc "É, sim... você beija muito bem, Xiangu."

                        xu "Obrigada... você também... o jeito que você lambe minha língua, que você chupa ela... ah..."

                        i "Para de deixar a Xiang excitada..."

                        xu "Eu quero mais! Eu preciso de mais! Mais beijo!"

                        scene xiangu_sexo7 with vpunch

                        pause

                        mc "Nghh!"

                        xu "Isso! Me lambe! Me beija!"

                        xu "Ah... aah!"

                        xu "Eu tô me sentindo quente! Minhas pernas!"

                        mc "Ah... Xiangu..."

                        xu "Nnghh! Assim!"

                        scene xiangu_sexo8 with vpunch

                        pause

                        xu "Aqui em baixo!"

                        mc "Você quer aqui em baixo?"

                        xu "Quanto mais em beijo... mais o meio das minhas pernas fica quente..."

                        i "Beijar não é mais suficiente, né?"

                        xu "Nnnghh!"

                        xu "Não sei o que tá! nnghh! Acontecendo! Aahhh!"

                        xu "Me dá mais, [mc]!"

                        scene xiangu_sexo7 with vpunch

                        mc "X-xiangu!"

                        xu "Eu vou ficar louca assim!"

                        mc "V-vem aqui!"

                        scene black with dissolve

                        scene xiangu_sexo9 with Dissolve(1.0)

                        pause

                        xu "O que você tá fazendo?!"

                        mc "Você vai sentir meu pau te apertando!"

                        xu "Aiin! Aii!"

                        xu "Tá lambendo meu pescoço! Aii! Dá um choque!"

                        xu "Aii, [mc]! O que é isso?!"

                        xu "Onde você tá apertando?! Aí atrás?!"

                        mc "Calma! É só pra pressionar! Você gosta?!"

                        xu "Ai!!!"

                        i "Claro que ela gosta! Olha a cara dela!"

                        mc "Então vem aqui. Tá na hora de você sentir ele de verdade."

                        scene black with dissolve

                        scene xiangu_sexo10 with Dissolve(1.0)

                        pause

                        xu "Ai... onde você tá esfregando?"

                        mc "Meu pau vai entrar em você, Xiangu."

                        xu "N-não! Aah! Eu sou virgem! Ngh!"

                        i "Você tá quase morrendo pra ele enfiar em você! Para de ser boba!"

                        menu:
                            "Eu vou meter agora.":


                                mc "A gente sabe que você quer, Xiangu. Então toma!"

                                scene xiangu_sexo10 with vpunch

                                xu "N-não!"

                                mc "Deixa eu!"
                            "Eu não posso fazer isso.":


                                mc "A gente vai fazer as coisas no seu tempo."

                                i "Para de ser bundão, [mc]! Enfia logo nela! Ela vai amar!"

                                xu "O-obrigada. E-eu!"

                        xu "Chega! Adeus!"

                        scene black with vpunch

                        mc "[xu]!"

                    elif xiang_casa_evento == 19:

                        $ xiang_casa_evento = 20

                        xu "[mc]... faz aquilo comigo de novo..."

                        mc "O quê?"

                        xu "Me pega sem roupa!"

                        mc "Não precisa nem pedir."

                        scene black with dissolve

                        scene xiangu_sexo11 with Dissolve(1.0)

                        pause

                        mc "Eu gosto dessa nova He Xiangu..."

                        xu "Essa... tarada..."

                        mc "Não é tarada... só uma mulher que sabe o que quer."

                        xu "Você fala isso porque você gosta de me ter."

                        mc "Talvez..."

                        xu "Não me importa... eu quero sentir aquilo de novo..."

                        xu "Começa me beijando!"

                        scene xiangu_sexo7 with vpunch

                        mc "Nnngh..."

                        "A Xiangu tá cada vez mais parecida com a Xiang... ela começou envergonhada... mas tá cada vez mais intensa."

                        xu "Hmmm... que gostoso... eu sinto tão bem... tão... aah... intenso..."

                        mc "É muito bom mesmo."

                        i "E a Xiang só olhando... vocês são maus com a Xiang..."

                        mc "Calm-"

                        xu "Ele é meu agora! Nngghh! Depois ele apaga seu fogo também."

                        i "..."

                        xu "Só beijo tá me deixando ansiosa de novo! Me pega daquele outro jeito por trás."

                        mc "Vem aqui."

                        scene black with dissolve

                        scene xiangu_sexo10 with Dissolve(1.0)

                        xu "Ahnn! Assim mesmo!"

                        mc "Você tá me deixando louco também, Xiangu! Esfregar meu caralho em você assim!"

                        xu "Esfrega! E me lambe! Que delícia!"

                        mc "Ah!"

                        xu "Você tá me apertando tão forte! Aiinn! É muito bom!"

                        xu "No pescoço! No peito! Aqui em baixo! Aaiin! É em todo lugar!"

                        i "Sortuda..."

                        mc "Xiangu... deixa eu transar com você. Vai ser mais intenso que tudo isso."

                        xu "M-mas..."

                        i "Eu vou ajudar você amiga."

                        xu "Você? Como?"

                        scene black with dissolve

                        scene xiangu_sexo9 with Dissolve(1.0)

                        i "Vem... a Xiang vai encaixar você."

                        xu "Me encaixar?"

                        i "Agora. [mc]!"

                        mc "C-com licença, Xiangu!"

                        scene black with dissolve

                        scene xiangu_sexo12 with Dissolve(1.0)

                        pause

                        xu "Ahhg! O que é isso?! Tá dentro de mim!"

                        i "Isso! Finalmente!"

                        mc "Você é demais, [xu]! Que delícia!"

                        xu "Nggh! Tá doendo, Xiang!"

                        i "Calma... não fica tensa... só piora... vai com calma..."

                        i "Deixa seus fluidos escorrerem pelo pinto dele... você vai ver..."

                        xu "Eu tô com medo..."

                        i "Calma... não vai acontecer nada... o [mc] vai fazer com carinho."

                        mc "Claro... pode deixar... vai falando o que você tá sentindo... bem devagar..."

                        xu "Ah... tá entrando e saindo..."

                        i "É assim mesmo... a Xiang... não aguenta mais... eu tô ensopada!"

                        i "[mc]! Cuida da Xiang também por favor!"

                        mc "D-deixa comigo..."

                        scene black with dissolve

                        scene xiangu_sexo13 with Dissolve(1.0)

                        pause

                        i "Aahh... isso... isso que a Xiang queria!"

                        mc "Uhuummm!"

                        i "Como você lambe gostoso, [mc]!"

                        xu "E-ele tá lambendo sua... enquanto me..."

                        i "Eu falei que o [mc] ia cuidar de nós duas!"

                        i "Aii... me lambe! Assim! Nnnghhh!"

                        xu "Xiang... seu gemido... aah... é... tão erótico... hmm..."

                        i "É porque tá... hmmm... muito bom! Ahnn!"

                        mc "Eu não vou aguentar muito mais assim! Vocês duas são coisa demais!"

                        i "Você vai ter que segurar!"

                        xu "Ah... aahnn..."

                        i "Tá gemendo também? Nnnghh..."

                        xu "Eu não sinto mais dor... aah... tá gostoso... nnnghh..."

                        i "Eu disse!"

                        xu "Quando entra... aah... esfrega gostoso... aahhn..."

                        i "S-sim! Nnghh!"

                        scene black with dissolve

                        scene xiangu_sexo14 with Dissolve(1.0)

                        pause

                        xu "Tá muito bom! Aahnnn!"

                        i "Sim! Aahnn!"

                        xu "Me aperta mais forte, Xiang!"

                        mc "Eu vou gozar!"

                        i "Nem! Aahnn! Nem pensa nisso! Aainin!"

                        xu "Não para!!! Ahhnn! Por favor!!!"

                        i "Tá bom! Tá muito bom!"

                        xu "Eu tô sentindo uma coisa!"

                        i "Sim! A Xiang vai gozar também!"

                        xu "Isso é gozar?! AAHNN!"

                        mc "GAROTASS!"

                        i "SSIIIMMM!!!!"

                        scene xiangu_sexo15 with vpunch

                        pause

                        mc "AAAAHHHH!!!"

                        i "AAAAHHHHH!!!"

                        xu "AAAAAHHHHH!!!"

                        scene xiangu_sexo15 with vpunch

                        pause

                        xu "Aah... o que foi isso..."

                        i "Isso... amiga... é uma delícia..."

                        mc "Xiang... eu preciso respirar..."

                        mc "Se bem que... morrer assim... não ia ser o pior dos mundos..."

                        mc "Aah..."

                    elif xiang_casa_evento == 20:

                        $ xiang_casa_evento = 21

                        "Nem acredito que eu realmente transei com a He Xiangu... e a Xiang ao mesmo tempo!"

                        "Será que... Opa! A Xiang tá em cima dela de novo..."

                        scene black with dissolve

                        scene xiangu_casa2 with Dissolve(1.0)

                        i "Foi tão gostoso transar! E nós duas juntas! A Xiang adorou!"

                        xu "Eu não sei o que eu tava na cabeça quando eu aceitei participar de tudo isso..."

                        xu "Até um tempo atrás eu era a He Xiangu... pura e perfeita... e agora eu transei com duas pessoas ao mesmo tempo..."

                        xu "Não era isso que eu esperava quando eu saí da Cidade Chinesa... acho que eu devia voltar pra lá."

                        mc "Quê?! Não! Só por causa disso?!"

                        i "Para de falar besteira! Você continua a mesma He Xiangu de sempre!"

                        xu "Mas... eu não sou mais pura..."

                        i "Claro que é!"

                        xu "Não sou!"

                        i "Se você acha que só porque não é mais virgem você deixou de ser pura... o que falar da Xiang que trabalhava com sexo?"

                        xu "Eu não queria te ofender... desculpa... mas eu..."

                        i "A Xiang não muda porque transou com zero ou 100 homens e mulheres. Não é ser virgem que diz se a Xiang é ou não é algo."

                        xu "Xiang... mas as pessoas não pensam assim..."

                        i "E desde quando a Xiang liga pro que as pessoas pensam? As pessoas são más, amiga. Se você for pela cabeça delas tá ferrada."

                        i "Faça o que VOCÊ quer fazer. Não transe pela Xiang ou pelo [mc] ou pelo seu namorado, esposa, sei lá."

                        i "Você é a dona do seu corpo e você tem que transar porque VOCÊ quer transar. É o que a Xiang faz pelo menos."

                        xu "Hmm..."

                        i "Antes a Xiang transava porque mandavam. Hoje, a Xiang só faz o que a Xiang quer."

                        i "Não é verdade o que a Xiang disse, [mc]?"

                        mc "Com certeza! Você é dona das suas vontades. Não deixe o que os outros pensam de você impedir que você faça o que acha certo."

                        xu "Talvez... você tenha razão."

                        i "Claro que eu tenho! Agora vamos comemorar transando?"

                        xu "Eu tenho que... pensar nisso tudo..."

                        i "A Xiang não falou tudo isso pra você ir pensar! Era pra você transar com a Xiang!"

                        mc "Xiang!"

                    elif xiang_casa_evento == 21:

                        $ xiang_casa_evento = 22

                        mc "E aí?"

                        scene black with dissolve

                        scene xiangu_casa2 with Dissolve(1.0)

                        "De novo a Xiang enchendo a He Xiangu... se continuar assim ela vai acabar expulsando a Xiangu de casa..."

                        i "Já acabou de pensar!?"

                        mc "Xiang é melhor você..."

                        xu "Você é muito mimada, garota... você não pode só falar o que você bem entende!"

                        i "Alguém tá bravinha!?"

                        xu "Desde o começo foi você! Foi você que fez eu vir pra cá! Que fez eu beijar o [mc]!"

                        xu "Foi graças a você que eu tirei minha roupa e deixei ele pegar em mim do jeito que ele queria!"

                        i "Uhum..."

                        scene black with dissolve

                        scene xiangu_sexo16 with Dissolve(1.0)

                        pause

                        mc "!!!"

                        xu "O-olha o que você tá fazendo!"

                        i "Vai falando. Foi tudo culpa da Xiang, né?"

                        xu "S-sim! Eu tô falando uma coisa séria e você tira minha roupa?!"

                        "Como que a Xiang consegue tirar a roupa das pessoas assim?"

                        "Mas parece que a Xiangu... não tá contrariada..."

                        i "É que você é tão linda! Você sabe que a Xiang gosta muito de você!"

                        xu "Você gosta do meu corpo... ah... você gosta de pegar em mim! Essa é a verdade, não é?!"

                        i "Sim... hmm..."

                        xu "O-onde você pensa que tá lambendo!?"

                        scene xiangu_sexo17 with Dissolve(1.0)

                        pause

                        xu "E-ei!"

                        i "A Xiang vai te ensinar que a mulher tem uma parte que é muito gosotosa de mexer..."

                        xu "A-ah!"

                        i "Sentiu o choque?"

                        xu "S-sim... o que você tá fazendo?"

                        i "Só sente, amiga..."

                        xu "Hm-hmmm... é d-disso que eu tô falando... aah... você... nnghh..."

                        xu "Eu tô começando a ficar zonza de novo..."

                        mc "É gostoso, [xu]?"

                        xu "C-cala a boca você também... aah..."

                        scene xiangu_sexo18 with Dissolve(1.0)

                        pause

                        xu "Para de lamber... aah... meu pescoço... e-eu... nnnghh..."

                        xu "Quando fazem assim... ah... você tá mexendo na minha... aah..."

                        i "Sua bucetinha é uma delícia... ela sente gostoso."

                        xu "Aaahnn... eu não sei o que... aah... tá acontecendo..."

                        i "Tá quente?"

                        xu "S-sim... minha buceta tá quente... d-digo... aahnnn..."

                        i "Agora imagina o pau do [mc] entrando em você..."

                        scene xiangu_sexo19 with Dissolve(1.0)

                        pause

                        xu "Aaah... para... e-eu não quero pensar nele..."

                        i "Lembra dele entrando e saindo no seu buraquinho? Não foi gostoso?"

                        xu "C-claro que foi... aaahnn..."

                        mc "Aleluia você disse que você adorou transar comigo."

                        xu "Aahh... eu gostei... e-eu não consigo mais pensar! Para Xiang!"

                        i "Você quer ou não quer sentir ele entrando dentro de você de novo?"

                        i "Mais forte? Mais duro?!"

                        xu "Eu quero! Aaahnnn! E-eu quero, sim!"

                        i "E aí, [mc]?"

                        mc "Só de ver vocês eu já fiquei no ponto."

                        i "Você vai me lamber de novo?"

                        mc "Claro."

                        i "Então vem, gostosa."

                        xu "A-aahhn!"

                        scene black with dissolve

                        scene xiangu_sexo20 with Dissolve(1.0)

                        pause

                        xu "Finalmente! Aahhhnn! Finalmente eu tô transando de novo!"

                        i "Aaahnn! Você queria, né?! Nngghh!"

                        xu "M-muito! Aaahh! Foi tão bom da outra vez! Aaahh!"

                        xu "Eu quero de novo! Aahhnn! S-sempre que vocês quiserem! Aaiinnng!"

                        i "Isso! A gente quer! Aahh!"

                        xu "Sexo é bom! Aaiinn! Transar é bom demais! Aaahhhnnn!"

                        i "Vai gozar de novo?!"

                        xu "Vou! Aagnnn! Continua entrando em mim, [mc]! AAGHH!"

                        mc "E-eu vou meter mais forte! Agh! Você é gostosa demais, Xiangu! NNGH!"

                        xu "Isso! NNGHH!!! METEEE!!! AAAAHHHH!!!"

                        scene xiangu_sexo21 with vpunch

                        pause

                        xu "GOZAAAAANDOOO!!! AAAAHHH!!!"

                        mc "E-eu também vou gozar em você!!!"

                        i "Isso! Engravida ela, [mc]! Igual você jorrou tudo em mim!!!"

                        mc "Vocês vão ser minhas mulheres! AAAHHH!!!"

                        xu "SIMMM!! T-TÔ SENTINDOOO!!! AAIINNN!!!"

                        i "Não para! Eu também! Tá vindo! Aahhnnn!"

                        scene xiangu_sexo22 with vpunch

                        pause

                        i "AAIINNNH!!! Na sua boca, gostoso!!! AAINN!!!"

                        mc "AAHGHHH!!"

                        i "Que delícia!!! Sexo a três é a melhor coisa!!!"

                        i "AAIIII!!!"

                        scene black with dissolve

                        pause 1.0

                        scene xiangu_sexo23 with Dissolve(2.0)

                        pause

                        xu "Aahh... ah..."

                        i "Puxa..."

                        xu "Eu nunca imaginei... aah... que algo podia ser tão intenso... aah..."

                        mc "Vocês tão bem?"

                        i "Aah... a Xiang... vai te chamar amanhã, tá?"

                        xu "Você tá louca..."

                        mc "A Xiang é insaciável... eu queria saber o que tem dentro de você pra te deixar assim..."

                        i "É o meu poder... o poder do sexo..."

                        xu "Só pode..."

                        mc "Ahahaha..."

                        "E pensar que essas duas vão continuar aqui em casa sei lá por quanto tempo... dá pra acreditar?"

                        "Como eu ia imaginar que minha vida ia ter um lance desses?"

                        "É por isso que... por pior que as coisas estejam... a gente nunca sabe quando as coisas podem mudar completamente."

                        "Agora é minha vez de aproveitar."

                    scene black with dissolve

                    $ tempo += 1

                    jump ap_sala_menu
        else:


            if xiangu_namoro:

                "Antes de trazer a He Xiangu pra roda, é melhor eu continuar avançando com a Xiang. Ela tá mais pronta pro fogo."

        $ xiang_evento_dia = True

        if xiang_casa_evento == 0:

            $ xiang_casa_evento = 1

            "Saber que a [i] tá fora daquela prisão que era o Distrito me deixa bem mais tranquilo."

            "Até hoje eu tive que pagar ela como prostituta pra gente poder conversar... como será que vai ser conversar com ela aqui?"

            i "Hm? Tá olhando pra [i]?"

            mc "É..."

            scene black with dissolve

            scene xiang_ape3 with Dissolve(1.0)

            pause

            mc "A-ah..."

            i "Que foi?"

            menu:
                "V-você tá legal?":


                    mc "É... como você tá?"

                    i "[i] tá bem."
                "Você tá gata com essa roupa.":


                    mc "E-eu fico meio sem saber o que falar... você tá bem sexy com essa roupa..."

                    i "Ela é confortável... e é novinha..."

                    mc "Pois é..."

                    i "E se a [i] fica bonita com ela, é melhor ainda. Pode me olhar sempre que quiser."

                    mc "Pode deixar..."

            mc "E você tá gostando daqui? Tipo... é melhor que o Distrito?"

            i "Xiang ainda tá se acostumando com tudo. Mas se você tiver aqui sempre, eu vou gostar muito mais."

            mc "Haha... às vezes eu vou sair pra fazer umas coisas. Mas eu volto logo."

            i "Não saia muito."

            mc "Eu vou tentar..."

            i "Passe o máximo de tempo com a Xiang. Você pode fazer o que você quiser comigo."

            mc "A-ah... m-melhor a gente conversar sobre isso depois."

            "Parece que ela ainda tá afim de mim. MAs eu ainda não sei se é uma boa a gente ficar."

            i "A Xiang vai conquistar você. Eu vou fazer você ficar com a Xiang querendo ou não."

            mc "Xiang... m-melhor eu ir fazer alguma coisa agora."

            i "Ok."

            mc "{i}gulp{/i}"

        elif xiang_casa_evento == 1:

            $ xiang_casa_evento = 2

            "Parece que a [i] tá se dando bem aqui..."

            i "[mc]. Pode passar um tempo com a [i]?"

            mc "C-claro."

            scene black with dissolve

            scene ape_xiang um with Dissolve(1.0)

            mc "Que foi? Ah... você tá achando chato ficar aqui? Bom... não tem muita coisa pra fazer, né?"

            i "É... não tem nada pra fazer aqui mesmo."

            mc "Ah... e-eu imaginei... eu não sei se é seguro você sair... mas se você quiser..."

            i "A [i] não quer."

            mc "Você entende o perigo... ufa..."

            i "Não. A [i] não tem medo. A Xiang gosta de ficar aqui. Eu quero fazer coisas aqui dentro."

            mc "Sério? Você tá gostando de ficar aqui então?"

            i "Sim. Mas a Xiang quer passar mais tempo com o [mc]."

            menu:
                "Eu vou aproveitar você também.":


                    mc "Eu quero aproveitar você também. Me divertir com você aqui."

                    i "A Xiang fica muito feliz. Eu aposto que a gente pode se divertir bastante."
                "Eu fico com você sempre que der.":


                    mc "Sempre que der eu venho falar com você, tá?"

                    i "Isso parece pouco..."

                    mc "Não é. Você vai ver."

            i "Agora você pode ter a Xiang de graça. Não é melhor assim?"

            mc "Xiang... eu gosto que você fique aqui, só que... lembra o que eu falei?"

            i "Não lembro."

            mc "Talvez você não goste de mim de verdade. Talvez seja só por causa de tudo que aconteceu."

            mc "Ainda mais agora que eu salvei você. Eu não sei se é uma boa a gente ir por esse caminho."

            i "A Xiang sabia que você ia querer correr falando isso. Mas eu decidi. A Xiang vai fazer você ficar com ela."

            mc "Haha... vamos ver."

            i "Nem que eu tenha que usar meu poder pra isso."

            mc "Que poder? O poder da sedução? Você é boa nisso..."

            i "O poder... hm... o [mc] vai ver na hora certa."

            mc "Ok..."

            "O que será que essa garota vai aprontar? Acho que eu vou dar o fora antes que ela tente alguma coisa."

            mc "E-então eu vou nessa. Depois a gente fala mais disso."

            i "Pode ir... mas não esquece a Xiang."

            mc "Pode deixar, boba."

        elif xiang_casa_evento == 2:

            $ xiang_casa_evento = 3

            "Deixa eu passar um tempo com a Xiang."

            scene black with dissolve

            scene ape_xiang um with Dissolve(1.0)

            mc "Oi. Tudo legal?"

            i "Tudo. Pronto pra dar um beijo na Xiang?"

            mc "A-ainda não."

            i "Não faça a Xiang usar o poder dela em você..."

            mc "Haha..."

            scene black with dissolve

            "{b}Vocês passam um tempo juntos{/b}"

        elif xiang_casa_evento == 3:

            $ xiang_casa_evento = 4

            mc "Tudo legal aí?"

            i "Sim. Na mesma."

            "Às vezes eu não sei se ela gosta ou não de ficar aqui."

            mc "Com licença."

            scene ape_xiang um with Dissolve(1.0)

            i "Vai fugir da Xiang de novo hoje?"

            mc "Não... sei..."

            i "Você é estranho, [mc]. Aposto que qualquer outro homem e até mulheres... iam se aproveitar da Xiang agora."

            mc "Parece que eu sou estranho mesmo... bastante gente fala isso pra mim."

            i "Será que é por isso que o [mc] sempre acaba em situações assim?"

            mc "Não sei. Parece que eu tenho alguma coisa com mulher. Talvez algum karma. Eu entro em poucas e boas por causa de vocês."

            i "E você não gosta?"

            menu:
                "Eu queria mais fácil.":


                    mc "Se fosse mais simples... mais fácil... acho que eu acharia bem melhor."

                    i "[mc] é folgado."

                    mc "Ei..."
                "Eu gosto assim mesmo.":


                    mc "Eu reclamo, mas no fundo acho que eu curto assim mesmo. Movimentado."

                    i "Será mesmo?"

                    mc "Ei..."

            mc "Você tá tentando me provocar, é?"

            i "A [i] gosta de ver as caretas que o [mc] faz."

            mc "..."

            i "Igual essa aí. Parece que o [mc] sempre encontra um jeito de ter uma reação exagerada."

            mc "Exagerada? Eu tenho uma reação normal."

            i "Não tem, não."

            mc "Melhor a gente encerrar o papo aqui por hoje."

            mc "A gente continua amanhã."

            i "Aww!"

            scene ape_xiang ape7 with hpunch

            i "A [i] quer conversar mais com o [mc]. A gente tá se dando bem."

            mc "É verdade... até que a gente tá."

            i "Agora a gente pode transar?"

            mc "Q-quê?!"

            i "Mas a gen-"

            mc "A-adeus!"

        elif xiang_casa_evento == 4:

            $ xiang_casa_evento = 5

            "Parece que eu e a [i] tá se dando cada vez melhor."

            "A gente realmente tá parecendo amigos depois daquela conversa. Eu achei divertido até."

            "Será que realmente tem alguma chance da gente..."

            i "Para de ficar olhando e vem logo aqui."

            mc "T-tá."

            scene black with dissolve

            scene ape_xiang ape5 with Dissolve(1.0)

            pause

            i "Agora a Xiang tá ajeitada..."

            mc "E-ei..."

            i "O [mc] nunca reclamou de sentir a Xiang lá no clube."

            mc "Touché."

            mc "Mas agora é diferente, Xiang. Você é uma garota livre. Não é mais seu trabalho fazer isso."

            i "A Xiang sabe."

            mc "Então..."

            i "E se a Xiang realmante gosta do [mc]? Você não consegue aceitar isso?"

            mc "Mas... como você pode gostar de mim se a gente nem se conhece?"

            i "Você já viu a Xiang sem roupa. O que mais você quer conhecer?"

            mc "X-xiang... não é isso... conhecer a cabeça e não o corpo..."

            i "Então... o que o [mc] quer saber da Xiang? Eu respondo tudo."

            mc "N-não é assim. Não é uma entrevista de emprego. A gente precisa de... sei lá... tempo."

            mc "A gente precisa passar pelas coisas e ver se a gente realmente tem uma ligação."

            i "E a gente não pode só fazer sexo?"

            mc "N-não. A gente só pode fazer isso depois que a gente tiver certeza."

            i "A Xiang não acha que as coisas são assim hoje em dia..."

            mc "Hoje em dia as pessoas tão rápidas demais..."

            mc "Ainda mais com alguém igual você, que não teve muita experiência, eu tenho que me responsabilizar."

            i "Quando o [mc] fala assim fica chato."

            mc "Azar o seu."

            i "A Xiang vai transar com outro então."

            mc "Q-quê?!"

            i "Se o [mc] não quer a Xiang, tem um monte que quer."

            mc "X-xiang!"

            i "Tchau!"

            scene black with vpunch

            "Eita... s-será que..."

        elif xiang_casa_evento == 5:

            $ xiang_casa_evento = 6

            "Da outra vez a Xiang ficou brava comigo..."

            "Mas eu sei que é melhor assim. Eu sou mais velho e ela precisa de algum responsável."

            "Eu não posso deixar ela me convencer com ciúmes desse jeito. Mas e se ela realmente... merda..."

            mc "Xiang..."

            i "..."

            mc "A gente pode conversar?"

            i "Xiang não pode conversar agora."

            mc "Por quê?"

            i "A Xiang tem um compromisso."

            mc "S-sério?"

            i "A Xiang vai se preparar. Adeus."

            scene black with dissolve

            mc "X-xiang!"

            scene ape_geral with Dissolve(1.0)

            "O que que deu nessa garota?"

            "Se preparar? Será que ela vai..."

            "{i}sheeesh{/i}"

            mc "Ela tá no banheiro..."

            scene black with dissolve

            scene ap quarto with Dissolve(1.0)

            mc "É. Ela tá lá. Tomando banho."

            "Será que..."

            menu:
                "Espiar ela no banho":


                    "Ela já deixou claro que quer fazer coisas comigo... então não vai ligar de uma espiadinha secreta..."

                    "... mesmo com a gente tando meio brigados... eu acho."

                    "Quem não chora não mama. Vou dar uma olhadinha rápida."

                    scene black with dissolve

                    scene ape_xiang ape16 with Dissolve(1.0)

                    pause

                    "Uuhh... que beleza."

                    "Será que eu tô sendo muito idiota de não pegar ela de uma vez?"

                    "Talvez eu tô deixando esse negócio de cavalheirismo entrar demais na minha cabeça."

                    "Não... eu não posso ser derrotado por uma bunda... mesmo sendo perfeita desse jeito..."

                    "Se eu realmente quero alguma coisa com a Xiang, precisa ser direito."

                    "Por enquanto eu vou só dar um olhadinha mesmo...{nw}"

                    i "Hm?"

                    mc surpreso "!!!"

                    scene ap quarto with hpunch

                    "Caraca... ela quase me viu..."
                "Dar espaço pra ela":


                    "Não é certo eu dar uma de voyeur aqui. Eu quero que ela se sinta em casa e ter um tarado te olhando não é tá em casa."

                    "Só de pensar o que eu tô perdendo..."

                    "Será que ela tá me provocando? Nah... ela deve só tá brava mesmo."

            mc "Deixa eu tomar meu rumo..."

            i "Hihi..."

        elif xiang_casa_evento == 6:

            $ xiang_casa_evento = 7

            "Será que ela já melhor comigo?"

            mc "Oi, [i]..."

            i "..."

            mc "Xiang?"

            i "[mc] não vai vir aqui?"

            "Eita... o que tá rolando agora?"

            mc "T-tô indo..."

            scene ape_xiang ape5 with Dissolve(1.0)

            i "Agora que a Xiang sentou assim, quero todo dia hihi..."

            mc "Você parece melhor agora."

            i "Eu já fiz o [mc] sofrer o suficiente."

            mc "Então você fez de propósito mesmo!"

            i "A Xiang fez... mas só porque o [mc] não quer ficar com ela!"

            menu:
                "Vingança nunca é plena!":


                    mc "Vingança nunca faz bem, Xiang!"

                    i "Mas o [mc] mereceu!"
                "Mas eu quero ficar com você!":


                    mc "Mas eu quero muito ficar com você também! Você não entende!?"

                    i "Mentiroso!"

                    mc "É sério! Eu quero, mas eu não consigo! Alguma coisa não deixa!"

            scene ape_xiang ape6 with Dissolve(1.0)

            i "Idiota..."

            mc "X-xiang! Eu tô tentando te proteger!"

            i "Você quer enganar a Xiang, só isso. Não quer ficar com ela e nem que ela fique com os outros."

            mc "V-você quer ficar com os outros mesmo?"

            i "E se eu quiser? A Xiang é adulta e agora tá livre. Pode ficar com quem quiser."

            mc "V-você tá certa..."

            i "Cala a boca..."

            mc "Hm?"

            i "Claro que a Xiang quer ficar com o [mc]. Não quer ficar com outro."

            mc "A-ah..."

            i "Então a Xiang vai ser obrigada a ficar com o [mc] que é quem ela quer ficar."

            mc "Eu fico feliz, Xiang... de você gostar de mim... mas você tem certeza?"

            mc "Talvez o melhor seja você conhecer outras pessoas e a gente só ser amigos. Pelo menos por um tempo."

            i "Não... a Xiang só quer o [mc]. E ela vai ser obrigada a ficar com ele."

            mc "O-obrigada?"

            i "É. Por isso eu vou ter que usar meu poder em você da próxima vez."

            mc "De novo essa história? Acho que tá na hora de eu ir, hein? A gente se fala depois."

            i "Ok..."

            mc "Só 'ok'?"

            i "Hoje, sim..."

            scene black with dissolve

            "O que essa mina tá planejando?"

        elif xiang_casa_evento == 7:

            $ xiang_casa_evento = 8

            mc "Posso sentar aí?"

            i "O [mc] sempre pode."

            scene black with dissolve

            scene ape_xiang ape6 with Dissolve(1.0)

            mc "O-opa."

            i "Hoje eu queria contar sobre um negócio lá do clube."

            mc "Eu adoro esse tipo de história."

            show black with dissolve

            hide black with dissolve

            i "E foi isso que a [i] fez."

            mc "Caraca... você passou por umas poucas e boas, Xiang."

            i "E o [mc]?"

            mc "Um dia desses eu conto uma história minha. Eu passei por umas boas aqui na ilha também."

            mc "Até depois, [i]."

            scene ape_xiang ape7 with hpunch

            i "Não!"

            mc "E-ei."

            i "Você vai ficar com a Xiang hoje."

            mc "Tudo bem. Eu conto uma história."

            i "Eu não quero saber de história! Eu quero que o [mc] pegue a Xiang!"

            i "A Xiang já até contou uma história que ela não queria pra você conhecer ela!"

            mc "X-xiang?!"

            i "Vai logo!"

            mc "M-mas só faz alguns dias, Xiang... não-"

            i "Você não tem jeito... eu vou ter que usar meu poder..."

            menu:
                "Você vai dançar pra mim?":


                    mc "Então você vai dançar pra mim?"

                    i "Dançar? Não... a Xiang não vai dançar."

                    i "A Xiang dançava bastante no clube, e ela não vai dançar nunca mais."

                    mc "Então qual poder..."
                "Não adianta... não é isso...":


                    mc "Não importa se você vai tentar me seduzir. Não é essa a questão."

                    i "A Xiang cansou de tentar seduzir o [mc]. A Xiang não quer mais seduzir ninguém."

                    mc "É? Então... do que você tá falando?"

            i "A Xiang tá falando disso aqui!{nw}"

            scene ape_xiang ape8 with vpunch

            pause

            mc "Kh-khaaah!"

            i "A Xiang vai obrigar o [mc] a ficar com ela!"

            mc "Nãum connxsigoohh rexprriarr!"

            i "A Xiang vai transar com o [mc] mesmo que ele desmaie!"

            mc "Isxco éh uhnm axbssurdoh!"

            scene ape_xiang ape8 with vpunch

            "Não consigo me mexer!"

            "Como ela é tão forte?!"

            i "Agora o [mc] vai tirar a roupa! A Xiang vai tirar a roupa dele enquanto imobiliza!"

            mc "Mheh sxoltah!"

            scene black with vpunch

            "{i}rshh rshhh{/i}"

            mc "Xiannng!"

            scene ape_xiang ape9 with vpunch

            i "Prontinho!"

            mc "Como você conseguiu isso?!"

            i "A Xiang é boa tirando a roupa."

            mc "E por que você é mais forte do que eu?!"

            if mc_fisico > 100:

                mc "Eu me matei na academia e mesmo assim você parece me segurar sem fazer força!"

            i "A Xiang é forte."

            mc "Isso não explica nada!"

            i "Agora a Xiang vai tirar a roupa dela. Você não foge, hein?!"

            mc "I-isso tá saindo do controle! Eu não quero ficar com você assim!"

            i "No fundo eu sei que o [mc] quer. Só tá com medo. Deixa que eu cuido de tudo."

            mc "O-onde você aprendeu falar desse jeito?!"

            mc "Obrigar uma pessoa assim não tá certo, Xiang! Você é má!"

            i "!"

            i "A Xiang..."

            mc "Essa é minha chance!"

            i "!?"

            scene black with vpunch

            i "Não!"

            i "Não adianta o [mc] se trancar no quarto! Amanhã a Xiang vai pegar!"

            "Caraca... o que tá acontecendo aqui?"

            $ tempo += 1

            jump ap_quarto_menu

        elif xiang_casa_evento == 8:

            $ xiang_casa_evento = 9

            "Ai ai... o que eu falo pra ela agora?"

            "A Xiang perdeu totalmente o controle da outra vez... caraca... eu tava ficando sem ar, mano."

            "Como que a gente pode ficar assim? Ela parece uma doida..."

            mc "Oi."

            i "Oi."

            mc "Tudo legal?"

            i "A Xiang vai tomar banho."

            mc "E-eu-"

            i "Agora a Xiang não tem tempo."

            scene black with dissolve

            scene ap quarto with Dissolve(1.0)

            "Parece que as coisas tão piores que da outra vez..."

            "Mas... ela deixou a porta aberta de novo. Ela deve tá incomodada demais pra ficar pensando em porta."

            "Melhor pra mim..."

            menu:
                "Espiar o banho":


                    "Não é porque eu tô em dúvida se é certo ou não transar com ela que eu não curto ver ela pelada."

                    "Certo? Não vou perder essa chance de dar uma olhadinha..."

                    scene black with dissolve

                    scene ape_xiang ape16 with Dissolve(1.0)

                    pause

                    "O bom que o barulho do chuveiro ajuda eu me esconder."

                    "Será que... eu consigo ver ela mais de perto?"

                    "Daqui não dá pra ver quase nada. Se eu conseguisse ir me arrastando até lá perto..."

                    "E agora?"

                    menu:
                        "Vou arriscar...":


                            "Só um pouco mais perto... pra poder apreciar melhor..."

                            "Aqui vamos nós!"

                            scene black with dissolve

                            scene ape_xiang ape17 with Dissolve(1.0)

                            pause

                            "Uau... que coisa linda..."

                            "Meu Deus... o que eu tô perdendo? Eu nem sei se tá certo eu ficar com ela."

                            "E agora eu tô agachado no banheiro me escondendo e vendo ela pelada tomando banho."

                            "Eu sou um verme..."

                            "Mas ela gosta de mim... ela é adulta... eu também..."

                            "E se eu só pulasse nesse box e encerrasse essa história agora mesmo?"

                            menu:
                                "Transar com ela no banho":


                                    "E-eu não aguento eu vou atacar ela!"

                                    scene ape_xiang ape17 with vpunch

                                    "ESPERA! Não!"

                                    "E-eu tenho que fazer as coisas direito!"
                                "Sair do banheiro":


                                    "Não! Eu não posso ceder aos desejos da carne desse jeito!"
                                "Ela é maravilhosa, mas eu tenho que dar o fora agora."
                                "Eu vou ficar com ela... mas do jeito certo."
                        "Melhor eu sair daqui":




                            "É perigoso demais."

                            "Mesmo que a gente fique juntos... não é assim que eu quero fazer isso."

                            "Vou fazer as coisas certas até ter certeza do que eu tô fazendo."

                            "Ou quem sabe a gente pode ser só amigos, né? Também seria bacana."
                "Deixar ela em paz":


                    "Eu vou deixar ela quieta lá."

                    "Mesmo que a gente fique juntos... não é assim que eu quero fazer isso."

                    "Vou fazer as coisas certas até ter certeza do que eu tô fazendo."

                    "Ou quem sabe a gente pode ser só amigos, né? Também seria bacana."

        elif xiang_casa_evento == 9:

            $ xiang_casa_evento = 10

            "Passou um tempinho... tomara que ela teja melhor."

            mc "Oi. Tudo legal?"

            scene xiang_ape3 with Dissolve(1.0)

            i "Sim. E com o [mc]?"

            mc "Também."

            i "Tô só descansando aqui..."

            menu:
                "Tá tudo bem com a gente?":


                    mc "Tá tudo legal com a gente?"

                    i "Legal?"
                "Posso sentar?":


                    mc "Posso sentar com você?"

                    i "Comigo..."

            i "Hmm..."

            scene ape_xiang ape8 with vpunch

            i "IA-HAH!"

            mc "AAAKHH!"

            scene ape_xiang ape9 with vpunch

            mc "XI-XIANG?!"

            i "Dessa vez eu vou conseguir! Você não vai me distrair de novo!"

            mc "De novo isso?!"

            i "Agora!"

            scene ape_xiang ape10 with vpunch

            pause

            mc "Xiang! ARGH! Tira seu pé daí!"

            i "Não é fácil manter um homem do seu tamanho quieto."

            mc "Não é possível que você realmente pretende me forçar a transar com você!"

            i "É minha última chance!"

            "Isso não faz sentido! Por que uma pessoa faria uma coisa dessas com outra?!"

            "Será que a Xiang é tão sem noção assim?!"

            mc "Xiang! Não! Você não pode forçar uma pessoa fazer algo que ela não quer só porque você tá afim!"

            i "M-mas!"

            mc "Você tá me machucando!"

            i "[mc]... eu..."

            mc "Para!!!"

            scene ape_xiang ape11 with hpunch

            pause

            i "[mc]... desculpa..."

            mc "Você tá louca, garota?"

            i "Você... você não me quer..."

            mc "Xiang... eu..."

            "Agora é a hora da verdade. Eu preciso decidir que tipo de relação eu quero ter com a Xiang."

            "Claramente ela tá afim de mim. Mas algo me diz que não é uma coisa saudável."

            "Ela cresceu naquele lugar, sendo aproveitada por todos a vida inteira. E agora ela quer ficar com alguém assim?"

            "Mas se eu for amigo dela... provavelmente a gente nunca vai ter nada juntos... eu sacrifico isso por ela?"

            "Minha nossa... o que eu respondo?"

            menu:
                "Não é tão simples.":


                    $ xiang_casa_evento = 12

                    mc "Xiang... me escuta... não é que eu não tem quero... eu te quero... MUITO!"

                    i "Então só fica comigo, [mc]!"

                    i "Beija a Xiang..."

                    mc "Agora?"

                    i "Agora... e amanhã... e depois... pra sempre..."

                    mc "Ai... Xiang..."

                    "Foda-se! Eu tô muito afim dela! E daí se ela teve uma vida difícil? A gente pode ficar juntos!"

                    mc "Você tá certa. A gente se quer, então bora. Vem aqui."

                    i "!"

                    scene ape_xiang ape12 with Dissolve(1.0)

                    pause

                    i "Hmm..."

                    mc "Que delícia..."

                    i "[mc]... finalmente..."

                    mc "Finalmente... eu não via a hora também."

                    i "Agora você vai ficar com a Xiang... não vai abandonar ela..."

                    mc "Claro que não. A gente vai fazer muito mais."

                    i "Você vai comer a Xiang também?"

                    mc "Vou. Agora."

                    i "Que bom... ahn..."

                    i "A Xiang tá pronta pro [mc]."

                    "Calma... eu vou até o fim com ela agora?"

                    menu:
                        "Transar com a Xiang":


                            "Agora é um caminho sem volta. A gente vai oficializar nossa paixão."

                            "Eu vou aproveitar essa garota do começo ao fim. E vai ser agora."
                        "Parar no beijo":


                            mc "Espera... a gente não precisa fazer tudo hoje."

                            i "Certeza?"

                            mc "Tenho... beijar você é o suficiente."

                            scene ape_xiang ape11 with Dissolve(1.0)

                            mc "A gente vai continuar depois. Eu prometo."

                            i "Tá..."

                            mc "A-até depois..."

                            i "Até..."

                    mc "Vem aqui, mina. Se ajeita."

                    scene ape_xiang ape13 with Dissolve(1.0)

                    pause

                    i "Ahh... a Xiang tá sentindo o pau do [mc]."

                    mc "Eu tô quase pronto pra você, Xiang."

                    i "Então beija mais a Xiang... pra você meter logo nela."

                    mc "Ah.. você é muito gostosa. Muito melhor do que eu imaginava."

                    mc "Sentir meu pau batendo na sua buceta assim tá me deixando louco."

                    i "Isso. Você vai ficar com a Xiang porque vai adorar comer ela."

                    mc "Eu vou adorar. Tenho certeza."

                    i "Então beija mais. A Xiang adora."

                    mc "Hmm!"

                    i "Ahn, [mc]... agora?"

                    mc "Eu tô pronto. Eu tô pronto pra sentir você no meu caralho."

                    i "Então vai!"

                    mc "Eu vou enfiar agora."

                    scene ape_xiang ape14 with Dissolve(1.0)

                    pause

                    i "Ahn! Tá na Xiang!"

                    mc "Tá! Você é muito apertada, Xiang! Tão gostosa!"

                    i "Isso! Agora mexe! Cutuca a Xiang!"

                    mc "Eu vou te comer! Ang!"

                    i "Ahnn! Assim!"

                    mc "Ah! Ah!"

                    i "O [mc]! An! Tá com tanta vontade! Annh!"

                    mc "Eu vou gozar em você! Eu não tô aguentando mais! Você é gostosa demais!"

                    i "Tá! O [mc] pode fazer na Xiang! Vai! Agn!"

                    scene ape_xiang ape14 with vpunch

                    mc "Ahg! Ah! AAaah!"

                    i "Vai!"

                    mc "{i}puf puf{/i}"

                    scene ape_xiang ape12 with Dissolve(1.0)

                    mc "Foi incrível."

                    i "A Xiang gostou muito. A gente vai fazer de novo?"

                    mc "A-agora não. Não precisa ter preça haha... a gente mora juntos..."

                    i "A Xiang vai tá esperando."

                    mc "O-ok..."

                    scene black with dissolve

                    scene ape_cama with Dissolve(1.0)

                    "Finalmente eu e a Xiang transamos. Não sei onde isso vai levar a gente, mas foi incrível."

                    "Espero que a gente continue se entendendo e se aproxime cada vez mais."

                    "Tanto tempo que a gente ficou se entranhando no clube e agora toda a investida dela aqui."

                    "Finalmente poder ter ficado com ela... caraca..."

                    "Com certeza não foi do jeito que eu tinha imaginado haha... mas com certeza foi demais."

                    "Se pá amanhã eu vou viver isso de novo! Nem acredito..."

                    $ tempo += 1

                    jump ap_quarto_menu
                "Eu quero ser apenas seu amigo.":


                    $ xiang_casa_evento = 11

                    mc "Eu não quero a mesma coisa que você, Xiang."

                    i "Mas... lá no clube..."

                    mc "Lá no clube era uma coisa, agora é outra. São coisas diferentes."

                    mc "Não é mais um lance profissional e físico. Agora a gente tá falando de sentimento."

                    mc "E eu não quero me envolver dessa forma com você. Será que você pode entender?"

                    i "Não..."

                    mc "Vai continuar tudo igual. A gente só não vai ficar. Mas a gente vai continuar perto."

                    i "Mesmo sem ser... amantes?"

                    mc "Claro. Você achou o quê? Que eu ia te abandonar só porque a gente não tá transando?"

                    i "É."

                    mc "Minha nossa senhora, Xiang... eu sei no clube as pessoas iam atrás de você por causa disso, mas aqui não é assim."

                    i "Você tem certeza? Não é melhor a Xiang forçar o [mc] transar com ela pra garantir?"

                    mc "N-não. Isso é justamente o que você não pode fazer. Forçar alguém transar é errado."

                    i "Ok..."

                    mc "Vem. Vamo se vestir e sentar."

                    i "..."

                    scene black with dissolve



                    mc "Bem melhor assim. Caraca... você machucou minha boca..."

                    i "Hmm... certeza que o [mc] não tá enganando a Xiang e vai deixar ela sozinha?"

                    mc "Certeza. A gente vai continuar juntos conversando, ok? Não precisa ser como parceiros sexuais."

                    i "Ok... então vai vir falar com a Xiang amanhã?"

                    mc "Sim. Eu vou."

                    mc "Às vezes eu esqueço o tipo de vida que você teve... tão diferente da minha e da maioria das pessoas."

                    mc "Mas agora é uma nova realidade. Você vai aprender melhor como são as coisas."

                    mc "E quem sabe você não acaba sendo bem mais feliz? Eu aposto que você vai se descobrir e vai ser incrível!"

                    i "A Xiang não entende tão bem... mas ela acredita no [mc]."

                    mc "Haha... pode acreditar. Agora vamo ver um pouco de TV."

                    i "Tá..."

                    scene black with dissolve

                    i "A Xiang pode deitar no seu colo?"

                    mc "Claro. Eu te faço um cafuné."

                    i "Hmm..."

                    i "O toque do [mc] é bem diferente... é quente... mas é quente diferente."

                    mc "Pois é. Isso é carinho. Gostou?"

                    i "Hmm..."

                    i "Adorei."

        elif xiang_casa_evento == 11:

            mc "Ei, Xiang. Quer ver alguma coisa na TV?"

            i "Oi. Eu quero com o [mc]."

            mc "Opa. Deixa eu sentar aí."

            scene black with dissolve

            scene ape_xiang um with Dissolve(1.0)

            pause

            i "[mc]... eu não sabia que a gente podia continuar assim mesmo sem transar."

            mc "Eu imagino... sua vida sempre foi diferente. Que bom que você tá entendendo isso agora."

            i "Mas continua com a Xiang, tá?"

            mc "Claro. Pode ficar aqui o tempo que você precisar. E eu vou tá do seu lado também, amiga."

            i "Amigo... vai ser legal viver com o [mc] esses dias aqui... como um amigo."

            mc "Haha."

            "Por um lado é triste pensar que eu e a Xiang não chegamos lá, mas tudo bem."

            "Não sei porque... mas eu sinto que esse foi o melhor caminho pra gente. Alguma coisa aqui dentro me diz isso."

        elif xiang_casa_evento == 12:

            $ xiang_casa_evento = 13

            mc "Xiang... bora?"

            i "[mc]..."

            mc "Entendeu? Bora se divertir um pouco?"

            i "Ah... a Xiang precisa tomar banho antes."

            scene black with dissolve

            scene ape_geral with Dissolve(1.0)

            mc "Hmm... tomar banho..."

            "Dessa vez eu posso ver ela inteira..."

            scene black with dissolve

            scene ape_xiang ape16 with Dissolve(1.0)

            pause

            scene ape_xiang ape17 with Dissolve(1.0)

            pause

            "Muito melhor poder ver ela assim sem medo dela me pegar."

            "Agora que a gente tá ficando... não tem problema, né?"

            mc "Oi."

            i "O que o [mc] tá fazendo aqui?"

            mc "Eu queria aproveitar você peladinha e cheirosinha desse jeito."

            i "A Xiang logo logo vai tá pronta."

            menu:
                "Eu não quero esperar. Bora.":


                    mc "Por que esperar?"

                    i "A Xiang tá no-"

                    mc "E daí? O banho é perfeito pra gente se divertir!"

                    i "[mc]!"

                    scene black with vpunch

                    mc "Deixa que eu cuido de tudo."

                    scene ape_xiang ape18 with hpunch

                    pause

                    i "Ahn!"

                    mc "Ahh!"

                    i "Ahh, [mc]! Você tá fazendo com tanta vontade na Xiang!"

                    mc "Você é ainda mais gostosa no banho, Xiang!"

                    i "Ahn! Aahh! A Xiang gosta do [mc] animado assim!"

                    mc "Você que me deixa assim, garota! Ah!"

                    mc "Vou gozar!"

                    i "Ahnn!"

                    scene ape_xiang ape18 with vpunch

                    mc "AAAHH!"

                    i "!!!"

                    mc "Ahh... ah..."

                    i "Agora a Xiang vai ter que tomar outro banho..."

                    mc "Deixa que eu te lavo..."

                    scene black with Dissolve(1.0)

                    "Esse tempo com a Xiang aqui vai ser incrível... já tá sendo..."
                "Vou te esperar lá fora.":


                    mc "Então termina aí. Eu te espero lá fora."

                    i "Tá."

                    scene black with dissolve

                    scene ap quarto with Dissolve(1.0)

                    mc "Só esperar ela..."

                    "..."

                    "..."

                    "..."

                    "Vou dar uma deitada enquanto isso."

                    "..."

                    "..."

        elif xiang_casa_evento >= 13:

            "Eu tô louco pra ficar com a Xiang de novo."

            mc "E aí, gata? Bora curtir um pouco?"

            i "A Xiang sempre tá afim quando o [mc] quer ela."

            mc "Assim que se fala."

            scene black with dissolve

            scene ape_xiang ape12 with Dissolve(1.0)

            pause

            i "Hmm..."

            mc "A gente vai curtir bastante."

            scene ape_xiang ape13 with Dissolve(1.0)

            pause

            i "A Xiang gosta de carinho..."

            mc "Eu vou te encher de carinho então."

            mc "Aposto que você vai adorar esse carinho aqui."

            scene ape_xiang ape14 with vpunch

            i "!!!"

            mc "Isso!"

            i "Ahn! O [mc] tá comendo a Xiang com força!"

            mc "Tô! Eu tô quase lá, Xiang!"

            i "Goza na Xiang! Ahnn!"

            mc "Ah! Ahh!"

            scene ape_xiang ape15 with vpunch

            pause

            mc "Ahh!"

            i "Ahn!"

            mc "{i}puf puf{/i}"

            mc "Você continua uma delícia... igual sempre..."

            i "A Xiang fica feliz quando o [mc] tá feliz com ela."

            mc "Logo logo a gente se vê de novo..."

            i "A Xiang tá sempre aqui."

        scene black with dissolve

        $ tempo += 1

        jump ap_sala_menu
    else:


        "Eu e a [i] já passamos um tempo juntos hoje. Melhor deixar pra amanhã."

        show screen ap_tela with Dissolve(0.3)

        pause

label ap_mc_dormir:

    hide screen ap_tela

    menu:

        "Dormir por um período" if tempo < 3:

            $ tempo += 1

            $ randh = renpy.random.randint(1,100)

            if randh <= 40:

                scene ap mc_dormindo1 with Dissolve(1.0)

            elif randh > 40:

                scene ap mc_dormindo2 with Dissolve(1.0)

            scene black with dissolve

            "z{size=20}{i}z{/i}{/size}{size=18}{i}z{/i}{/size}{size=16}{i}z{/i}{/size}{size=14}{i}z{/i}{/size}{size=12}{i}z{/i}{/size}{size=10}{i}z{/i}{/size}"

            menu:
                "Visitar a [p] em Fadolândia":


                    call cenario_fadolandia from _call_cenario_fadolandia_2
                "Acordar":


                    pass

            $ randh = renpy.random.randint(1,2)

            scene ap quarto with Dissolve(1.0)

            show mc acordando with dissolve

            "Nada como tirar um cochilo."

            jump ap_quarto_menu
        "Dormir até amanhã":


            $ dormir_em_casa = True
            $ mc_ja_tomou_banho = False

            $ randh = renpy.random.randint(1,100)

            if randh <= 40:

                scene ap mc_dormindo1 with Dissolve(1.0)

                pause

            elif randh > 40 and randh <= 80:

                scene ap mc_dormindo2 with Dissolve(1.0)

                pause

            elif randh > 80:

                scene ap mc_tv_quarto with Dissolve(1.0)

                pause

                "Opa. Massacre no Bairro Japonês! Eu adoro esse filme!"

                "Vou assistir."

                "..."

                "Não tô aguentando..."

            jump dormir

    jump ap_quarto_menu

label ap_mc_tv:

    hide screen ap_tela

    scene ap mc_assistindo with Dissolve(1.0)

    pause

    menu:
        "Assitir alguma coisa":


            $ randh = renpy.random.randint(1,3)

            if randh == 1:

                "Tem um seriado aqui chamado {b}Você{/b}."

                "..."

                "Mano! Esse cara perseguindo a mina, mano! Parece eu!"

                mc "Acho melhor eu me controlar..."

                "Se bem que meu trabalho é perseguir as celebridades. Que tipo de trabalho é esse?"

            elif randh == 2:

                "Hoje eu vou ver esse {b}House of Cards{/b}..."

                "..."

                "Caraca, não entendi nada!"

                "Essa série tinha que vir com um manual sobre política pra gente entender o que tá acontecendo."

                "Mas... um vice-presidente agindo contra o próprio partido pra derrubar o presidente."

                "Isso nunca aconteceria na vida real!"

            elif randh == 3:

                "Opa! Saiu a quarta temporada de {b}Vikings{/b}! Vou ver!"

                "..."

                "Quê?! Só tem a segunda... Mano... vai ter que se no torrent mesmo."

                "Tu paga o dinheiro que não tem por mês e ainda tem que ficar baixando coisa..."
        "Jogar videogame ([videogame])":




            mc "Deixa eu ver o que tem de graça pra gastar um tempo..."

            if videogame == 0:

                $ videogame += 1

                "Hoje eu vou jogar esse aqui... {b}Nautilus 05{/b}... que porra de nome é esse?"

                "Com certeza é aquele tipo de título que tem algum mistério por trás. Daí uma hora vai aparecer e a gente fala AAAHHH!! ERA ISSO!"

                show capa n05 with dissolve

                mc "Uau! É um lance meio do futuro. E tem um pessoal bem gostoso no elenco."

                "Um jogo de escolhas que acontece no futuro apocalíptico... no meu futuro? Meu futuro não é apocalíptico, não! Nem vem!"

                "Quê?! É um jogo adulto com história de cinema?! Não é possível um negócio desses! Cena de sexo com história boa?! Isso existe?!"

                "Esse aqui vale a pena jogar!"

                "Por que eu tô pensando como se eu tivesse fazendo uma propaganda? Esse aqui é o Show de Truman?!"

                menu:
                    "Baixar Nautilus 05 (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nautilus-05:-Serie-Cyberpunk-(Premium)-OzLBBUKHv'))
                    "Baixar Nautilus 05 (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/n05/'))
                    "Outra hora":


                        pass

            elif videogame == 1:

                $ videogame += 1

                "Vou tentar outra de graça aqui hoje... Encontros - Nome provisório. Este jogo aqui ainda não acabou."

                "Sobre o que que é esta desgraça?"

                mc "Um game que acontece no mundo de Celebrity Hunter, com personagens já conhecidos dessa incrível história."

                mc "Reveja a Pixie, Ágata, Carol... QUÊ?! HAHAHA! Que coincidência! São nomes igualzinhos de umas que eu conheço aí."

                mc "Que loucura... Encontros... Esse mundo de Celebrity Hunter deve ser uma doideira só..."

                mc "Mais um jogo adulto, com uma história incrível, escolhas emocionantes e uma mecânica inovadora. Uau..."

                menu:
                    "Baixar Encontros (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/'))
                    "Baixar Encontros (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/en/'))
                    "Outra hora":


                        pass

                mc "Minha vida já é conturbada demais pra jogar jogos complicados assim. Acho que vou só assistir uma coisa hoje."

                "Imagina se eu fosse jogar Encontros e visse a... imagina? Haha... que doideira..."

            elif videogame == 2:

                $ videogame += 1

                "Bora ver esse aqui... não é parecido com aquele... olha o nome... {b}Nautilus 10{/b}?!"

                "É continuação daquele outro. Esse é '10' e o outro é '05'. Por que eles só não chamam de Nautilus 1 e Nautilus 2? Que frescura."

                show capa n10 with dissolve

                mc "Então continua aquela saga adulta apocalíptica. Aquele N05 foi bem massa. Então acho que vou continuar nesse aqui agora."

                "Depois de sairem do CTM, os protagonistas vão para o Deserto, a região mais perigosa de Nova Doma, o nome do país."

                "Será que eles vão conseguir sair de lá ou morrerão sem água e sem comida? E melhor... eles vão acabar transando muito?"

                "Que sinopse mais doidona é essa?!"

                "Seja como for eu vou jogar isso aqui! Nem que eu tenha que viver no lixão! Bora de Avenida Brasil!"

                menu:
                    "Baixar Nautilus 10 (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nautilus-10:-Projeto-Cyberpunk-(Premium)-2wnrXt_c_'))
                    "Baixar Nautilus 10 (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/npc/'))
                    "Outra hora":


                        pass

            elif videogame == 3:

                $ videogame += 1

                "Ok! Hoje tô afim de um RPG! E com cenas adultas cheias de sexo! Será que existe?! {b}NFC +18{/b}?! Não é que existe?!"

                "Nova Fantasia Clicker ou NFC +18 é um RPG focado em seduzir e dominar suas inimigas em combate ou com o sexo."

                show capa nfc with dissolve

                mc "Não é possível que existe um negócio desses mesmo..."

                "O jogo se passa em uma terra que foi dominada por uma magia que torna todas as criaturas escravas do prazer."

                "Seu objetivo vai ser descobrir a origem dessa magia e salvar o reino desse terrível mal!"

                "Você pode acabar com elas ou vencer elas por meio do sexo, sedução e pode até levar elas pra viver com você."

                mc "Sério isso?!"

                "A história é incrível, continuação de Nova Fantasia, com finais alternativos e secretos pra você descobrir."

                mc "Caraca! Esse com certeza eu vou jogar!"

                menu:
                    "Baixar NFC +18 (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nova-Fantasia-Clicker-+18-(Premium)-UTkgjtBgK'))
                    "Baixar NFC +18 (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/nfc/'))
                    "Outra hora":


                        pass

            elif videogame == 4:

                $ videogame += 1

                "Não é possível... {b}Nautilus 20{/b}?! É outro daquela série! Eu pensei que tinha acabado!"

                "Então tem o N05, o N10 e agora o N20. Que é tipo o terceiro da série. Por que esse tal de RB usou esses números tão estranhos?!"

                show capa n20 with dissolve

                mc "Então agora a história continua depois do Deserto. Eu queria mesmo jogar até chegar na Capital. Parece que é agora!"

                "Depois de escaparem do Deserto, os protagonistas se envolvem em um duelo entre o governo e os rebeldes."

                "Como eles podem usar esse conflito para chegarem na Capital e terem uma vida digna?! E com muito sexo!"

                "Por que sempre tem SEXO jogado aleatoriamente em todas as sinopses dessa empresa?!"

                "Será que eles acham que só porque tem sexo a gente vai jogar?! Que absurdo... deixa eu jogar, vai!"

                menu:
                    "Baixar Nautilus 20 (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/'))
                    "Baixar Nautilus 20 (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/n20/'))
                    "Outra hora":


                        pass
            else:


                $ videogame = 0

                "Bora desestressar jogando esse aqui... {b}Nova Fantasia: RPG Adulto{/b}."

                "Um jogo de RPG com um combate em ação nunca visto antes na história do celular! Por que celular? Eu to nô console. Cada uma..."

                "Uma história de vingança e cheia de emoção, mistério, com cenários incríveis, músicas sensacionais e muitas novidades!"

                "Além de ser o jogo mais difícil que o RB já criou e criará!"

                mc "Como eles sabem que o cara nunca vai fazer um jogo mais difícil que esse? Então quem terminar esse aí é um herói?"





                menu:
                    "Baixar Nova Fantasia (Premium)":


                        $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/Nova-Fantasia:-RPG-Adulto-(Versao-Premium)-pa2lp7E-N'))
                    "Baixar Nova Fantasia (Grátis)":


                        $ renpy.run(OpenURL('https://www.geiko.net/nf/'))
                    "Outra hora":


                        pass

                "..."

                "Hmmm... Até que é interessante... é meio enrolado, mas a batalha é ação pura! Acho que eu nunca vi isso num jogo assim!"

                "O cara que criou isso aqui deve ser um gênio. Com certeza!"







                p rindo "Falar de um jogo dentro de outro jogo?"

                p "Isso é um absurdo..."

            mc "Ok... vamos lá!"

            hide capa with dissolve

            "..."

            show black with dissolve

            $ tempo += 1

            hide black with dissolve

            "Opa, olha a hora!"

    $ tempo += 1

    jump ap_sala_menu

label ap_sala_menu:

    $ ap_comodo = "sala"

    hide screen ap_tela

    if tempo > 3:

        "Putz. Olha a hora. Melhor eu capotar senão amanhã eu não aguento."

        $ dormir_em_casa = True

        jump dormir

    if karli_casa:

        if karli_esta:

            $ randh = random.randint(1,2)

            if randh == 1:

                scene ap_karli mc_sala1 with Dissolve(1.0)

                pause
            else:


                scene ap_karli mc_sala2 with Dissolve(1.0)

                pause

            $ randh = random.randint(1,12)

            if randh == 1:

                mc "Como tão indo as coisas do salão?"

                m "Caminhando. Mais alguns dias e acho que consigo reabrir ele."

                mc "Que bom."

                m "Tá com saudades de praticar massagem?"

                if karli_seducao >= 5:

                    mc "É isso, claro..."

                    m "Safado..."
                else:


                    mc "Sim. Não vejo a hora de voltar."

                    m "Isso que é um bom estudante.."

                mc "Hehe..."

            elif randh == 2:

                mc "O que achou do apartamento?"

                m "Achei incrível, né? Ainda não acredito que um assalariado igual você tem um apê desses."

                mc "Difícil de acreditar, né?"

            elif randh == 3:

                m "Ai, [mc]... tô curtindo ficar aqui."

                mc "Que bom, [m]. A casa é sua."

                m "A única pena é que eu tenho que dividir com você."

                mc "..."

                m "Brincadeirinha..."

                mc "Não tem ninguém rindo."

            elif randh == 4:

                m "Acho que hoje vou dormir o dia inteiro."

                mc "Você não tem que resolver seus problemas, não?"

                m "Tá me expulsando?"

                mc "Claro que não."

                m "Acho bom. Porque tô pensando em dormir o dia inteiro."

                mc "Você já... deixa pra lá."

            elif randh == 5:

                mc "É..."

                m "Que foi?"

                mc "Você não liga de ficar com essa roupa na minha frente?"

                m "Não. Por que?"

                mc "Nada, não."

                m "Cara doido..."

            elif randh == 6:

                mc "Como você tá fazendo com as roupas?"

                m "Eu tô levando na lavanderia. Relaxa."

                mc "Ah tá. Eu também deixo lá. Não tenho paciência pra eu lavar."

                m "Depois reclama que não tem dinheiro."

                mc "Me deixa..."
            else:


                pass
        else:


            scene ap sala with dissolve

            $ randh = renpy.random.randint(1,5)

            if randh == 1:

                "Parece que a [m] não tá aqui agora. Espero que esteja dando tudo certo as coisas dela."

            elif randh == 2:

                "A [m] saiu. Onde será que ela foi? Ah! Ela deve tá resolvendo o problema do salão."
            else:


                "A casa parece vazia sem a [m]."

    elif xiangu_namoro and not xiangu_partiu:

        if sofia_final2:

            $ xiangu_partiu = True

            scene black with dissolve

            scene ani48 with dissolve

            pause

            i "[mc]... onde tá a He Xiangu?"

            i "Faz tempo que você saiu atrás dela... e ela não voltou pra casa."

            mc "[i]... bom..."

            mc "Ela não vai voltar mais. Ela... tá com a mãe dela agora."

            i "Poxa... isso é bom, mas é triste. Eu gostava dela."

            mc "Eu também. Ela tinha deixado a casa mais animada."

            mc "Além de que ter duas gatinhas me esperando sempre era bom."

            i "Hmm... a Xiang vai ter que fazer o trabalho das duas agora."

            mc "C-como é?"

            scene black with dissolve

            scene ani49 with dissolve

            mc "A-aagh!"

            i "A buceta da Xiang vai satisfazer seu pau como se fosse duas! A Xiang consegue!"

            mc "Você vai me matar assim!"

            i "Xiang vai te matar de tanta pepecada! Se prepara, [mc]!"

            mc "Xiaaaaaannnnngg!"

            mc "AAAAGGHHHH!!! Vou morrer de gozar assim!"

            i "Assim mesmo! Aahnnn! Morre de tanto foder a Xiang!"

            mc "Essa menina não tem jeito!"

            scene black with dissolve

            scene ani50 with dissolve

            "Mesmo sem a He Xiangu... a Xiang com certeza vai deixar a casa sempre animada."

            "Boa sorte, He Xiangu, Liling. Espero que vocês sejam felizes."

            mc "AAAGHHH!!! Você me deu uma surra de xota!"

            i "Você tava pensando nela, não tava?!"

            mc "E-eu!"

            scene black with dissolve

            mc "XIAAAAAAANNNNNNGGGG!!!"

            scene black with dissolve

            jump ap_sala_menu

        $ randh = 0

        $ randh = random.randint(1,20)

        if randh <= 8:

            scene xiangu_casa1 with Dissolve(1.0)

        elif randh <= 12:

            scene xiangu_casa2 with Dissolve(1.0)

        elif randh <= 14:

            scene xiang_casa1 with Dissolve(1.0)

        elif randh <= 16:

            scene xiang_casa2 with Dissolve(1.0)

        elif randh <= 18:

            scene xiang_casa3 with Dissolve(1.0)
        else:


            scene ape_new with dissolve

        if randh == 1:

            mc "Eu ainda tô me acostumando com vocês duas aqui..."

            i "A casa triste do [mc] ficou muito mais linda com a Xiang e a He Xiangu."

            mc "Hehe... isso é verdade..."

            xu "E muito mais inteligente também."

            mc "Ei!"

        elif randh == 3:

            i "Quando você vai poder se divertir com a gente?"

            mc "X-xiang... precisa falar assim?"

            xu "O que você tá falando? Todo mundo vê que você é um tarado."

            mc "Droga... agora são duas contra um."

        elif randh == 5:

            mc "Agora que somos nós três... são mais bocas pra comer."

            i "Entendi! A Xiang vai ajudar! Ela sabe ganhar dinheiro com o corpo na rua!"

            xu "Eu buscarei oferendas de pedestres. A imagem da He Xiangu ainda é muito viva na mente dos plebeus."

            mc "P-podem esquecer! Deixem que eu vou pagar tudo."

        elif randh == 7 or randh == 8:

            i "O [mc] chegou! Bem-vindo de volta em casa!"

            xu "Bem-vindo, [mc]."

            mc "V-valeu, garotas..."

        elif randh == 9:

            xu "Xiang... por que você precisa me abraçar assim? E-eu..."

            i "Não precisa ficar com vergonha... a [i] gosta do seu cheiro..."

            xu "E precisa ficar pegando em mim desse jeito também?"

            i "A [i] gosta do seu cheiro... do seu corpo... do seu sabor..."

            "Hehe... essas duas realmente deixaram a casa mais animada."

        elif randh == 11:

            xu "Ahh... X-xiang... de novo?"

            i "Sim... a Xiang não aguenta..."

            mc "Parece que ela realmente gosta de você, [xu]."

            xu "Até de mais... apesar que... n-nada... esquece."

        elif randh == 13:

            mc "Por que você gosta de sentar aí? Não é assim que usa um sofá."

            i "Não? A [i] nunca sentou num lugar assim. Mas ela vai aprender a sentar direito."

            mc "Tudo bem... eu só tava comentando. Pode sentar do jeito que você quiser."

        elif randh == 15:

            mc "Quais as notícias do dia?"

            i "Hm? A [i] não sabe."

            mc "Você não tava vendo o noticiário?"

            i "O que é noticiário?"

            mc "Deixa pra lá..."

        elif randh == 16:

            mc "E aí? Tá se acostumando com a casa?"

            i "A [i] gosta daqui porque o [mc] vive aqui... eu sinto seu cheiro em todo lugar..."

            mc "[i]..."













        elif randh == 18:

            mc "Tá fazendo yoga?"

            i "É. A [i] gosta de fazer yoda desde criança. O pessoal do templo ensinou. Quer fazer também?"

            mc "Quem sabe na próxima..."

            i "O [mc] pode olhar a [i] fazer então..."

            mc "P-pode deixar... e-eu vou olhar bastante..."

        elif randh == 19:

            "Cadê aquelas duas? Eu fico nervoso toda vez que elas não tão aqui..."
        else:


            pass

    elif xiang_casa:

        $ randh = random.randint(1,10)

        if randh <= 4:

            scene xiang_casa1 with Dissolve(1.0)

            pause

        elif randh > 4 and randh <= 8:

            scene xiang_casa2 with Dissolve(1.0)

            pause
        else:


            scene xiang_casa3 with Dissolve(1.0)

            pause

        if randh == 1:

            mc "Por que você gosta de sentar aí? Não é assim que usa um sofá."

            i "Não? A [i] nunca sentou num lugar assim. Mas ela vai aprender a sentar direito."

            mc "Tudo bem... eu só tava comentando. Pode sentar do jeito que você quiser."

        elif randh == 2:

            mc "Quais as notícias do dia?"

            i "Hm? A [i] não sabe."

            mc "Você não tava vendo o noticiário?"

            i "O que é noticiário?"

            mc "Deixa pra lá..."

        elif randh == 5:

            mc "E aí? Tá se acostumando com a casa?"

            i "A [i] gosta daqui porque o [mc] vive aqui... eu sinto seu cheiro em todo lugar..."

            mc "[i]..."

        elif randh == 6:

            mc "Você vai ficar aqui mais alguns dias?"

            i "A [i] vai. Tudo bem pra você?"

            mc "Claro. Pode ficar quanto tempo você quiser."

            i "A [i] vai juntar dinheiro... mas antes ela precisa achar um trabalho..."

            mc "Vai demorar um tempinho então..."

        elif randh == 9:

            mc "Tá fazendo yoga?"

            i "É. A [i] gosta de fazer yoda desde criança. O pessoal do templo ensinou. Quer fazer também?"

            mc "Quem sabe na próxima..."

            i "O [mc] pode olhar a [i] fazer então..."

            mc "P-pode deixar... e-eu vou olhar bastante..."
        else:


            pass
    else:




        scene ape_new with dissolve

        $ randh = random.randint(1,40)

        if randh == 1:

            "Ainda não acredito que consegui minha casa própria."

            "E ainda por cima, um apartamento como este aqui não é pra qualquer um."

        elif randh == 2:

            "É menor do que o da [j], mas não tem comparação com o que eu vivia antes."

            "Pra um cara sozinho, está bom demais."

        elif randh == 3:

            "Vai ser muito legal chamar outras pessoas pra viver aqui também."

            "Às vezes bate aquela solidão de viver sozinho. Quem sabe eu não acabe pegando um animal de estimação?"

        elif randh == 4:

            "Não posso deixar de fazer a faxina de vez em quando."

            "Manter isso aqui brilhando desse jeito vai precisar de algum esforço."

        elif randh == 5:

            "Eu tô ainda mais perto da redação agora."

            "Quem sabe não dá até pra ouvir o chefe gritando? Espero que não..."

        elif randh == 6:

            "Nem acredito que a [m] foi embora."

            "A casa ficava muito mais animada com ela."

        elif randh == 7:

            "Bem que podia ter uma vizinha bacana e solteira aqui do lado..."

        elif randh == 8:

            "Esse apê aqui deixa o outro no chinelo. Nem acredito que a Gina arranjou isso aqui de graça pra mim... mas pagar os papéis... ugh... não foi fácil."

        elif randh == 9:

            "Eu vi no noticiário que da capital dá pra ver a lua gigante. É um fenômeno que só acontece aqui..."

        elif randh == 10:

            "Sendo mais amigo das celebridades, eu tenho mais chance de conseguir pautas. Tenho que tentar pensar com a cabeça de cima."

        elif randh == 11:

            "O que não falta nessa ilha são garotas lindas. É muita sorte poder falar com algumas delas."

        elif randh == 12:

            "Tem tanta coisa acontecendo comigo ultimamente que até parece um filme... ou um jogo. Doideira..."

        elif randh == 13:

            "Do ponto de ônibus eu posso ir para a parte continental da cidade. Quem dera ter dinheiro pra comprar um carro..."

        elif randh == 14:

            "O pessoal da redação fala que a capital é uma espécie de cebola... com camadas. O que raio isso quer dizer?"

        elif randh == 15:

            "Todo o salário que eu ganho na revista vai pra pagar contas. Se eu quiser comprar outras coisas, preciso arranjar uns bicos."

        elif randh == 16:

            "Na centro da cidade tem vários lugares interessantes, uma pizzaria famosa, o canal de TV, o museu, a prefeitura..."

        elif randh == 17:

            "Nossa revista tá cada vez mais famosa. Se eu me der bem lá, com certeza eu tô feito pro resto da vida."

        elif randh == 18:

            "{i}zzzzzzzzzk{/i}"

            mc desconfiado "Que barulho é esse? Eita! Deixei a TV ligada? Que estranho..."

        elif randh == 19:

            "Conseguir pautas é muito importante pra eu não ser despedido. Preciso fazer as celebridades confiarem em mim."

        elif randh == 20:

            "Nem acredito que consegui grana pra comprar este apê aqui. Minha vida tá mudando!"
        else:


            call checa_eventos

    if ( mc_massagem == 9 or ( mc_massagem == 8 and gina_bunda ) ) and carro_evento == 0 and tempo <= 2:

        jump compra_carro

    show screen ap_tela



    $ renpy.pause()



label ap_quarto_menu:

    $ ap_comodo = "quarto"

    hide screen ap_tela

    scene ap quarto with dissolve

    show screen ap_tela

    pause

label ap_cozinha_menu:

    $ ap_comodo = "cozinha"

    hide screen ap_tela

    scene ap cozinha with dissolve





    show screen ap_tela

    pause

label ap_banheiro_menu:

    $ ap_comodo = "banheiro"

    hide screen ap_tela

    scene ap banheiro with dissolve





    show screen ap_tela

    pause

label cenario_ap:

    stop sound

    $ estou_na_cidade = False

    if diana_final2_pre and not diana_final2:

        jump diana_final2_parte2

    if karli_casa:

        if karli_evento_auto == 0:

            $ karli_evento_auto += 1

            call karli_evento_auto0 from _call_karli_evento_auto0

            jump ap_sala_menu

        if tempo == tempo_karli:

            $ randk = renpy.random.randint(1,100)

            if randk <= 75:

                $ karli_esta = True

            elif randk > 75:

                $ karli_esta = False

            if tempo == 1:

                $ tempo_karli = 2

            elif tempo == 2:

                $ tempo_karli = 3
            else:


                $ tempo_karli = 1

        if karli_esta and karli_evento_auto <= 3:

            $ randh = renpy.random.randint(1,100)

            if randh <= 25:

                if karli_evento_auto == 1:

                    $ karli_evento_auto += 1

                    call karli_evento_auto1 from _call_karli_evento_auto1

                elif karli_evento_auto == 2:

                    $ karli_evento_auto += 1

                    call karli_evento_auto2 from _call_karli_evento_auto2

                elif karli_evento_auto == 3:

                    $ karli_evento_auto += 1

                    call karli_evento_auto3 from _call_karli_evento_auto3

                $ tempo += 1

                scene black with dissolve

                "..."

            elif randh > 25:

                pass

    jump ap_sala_menu



label cenario_estacionamento:

    stop sound

    $ estou_na_cidade = False

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    scene carro_estacionamento with Dissolve(1.0)

    "Nunca vou enjoar de olhar pra essa belezinha."

    scene black with dissolve

    scene carro_estacionamento2 with Dissolve(1.0)

    "Pra onde eu vou agora?"

    show screen carro_escolhe with Dissolve(0.5)

    pause



















screen carro_escolhe():

    predict False
    modal True



    imagebutton auto "images/mapa/cidade1_%s.webp":
        xalign 0.03
        yalign 0.03
        action [ SetVariable("destino", "cidade1"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/boutique_%s.png":
        xalign 0.12
        yalign 0.03
        action [ SetVariable("destino", "boutique"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/fliperama_%s.png":
        xalign 0.21
        yalign 0.03
        action [ SetVariable("destino", "fliperama"), Jump("carro_evento") ]



    imagebutton auto "images/mapa/cidade2_%s.png":
        xalign 0.03
        yalign 0.2
        action [ SetVariable("destino", "cidade2"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/biblioteca_%s.png":
        xalign 0.12
        yalign 0.2
        action [ SetVariable("destino", "biblioteca"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/cinema_%s.png":
        xalign 0.21
        yalign 0.2
        action [ SetVariable("destino", "cinema"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/universidade_%s.png":
        xalign 0.3
        yalign 0.2
        action [ SetVariable("destino", "universidade"), Jump("carro_evento") ]



    imagebutton auto "images/mapa/cidade3_%s.png":
        xalign 0.03
        yalign 0.37
        action [ SetVariable("destino", "cidade3"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/prefeitura_%s.png":
        xalign 0.12
        yalign 0.37
        action [ SetVariable("destino", "prefeitura"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/tkf_%s.png":
        xalign 0.21
        yalign 0.37
        action [ SetVariable("destino", "tkf"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/faux_%s.png":
        xalign 0.3
        yalign 0.37
        action [ SetVariable("destino", "faux"), Jump("carro_evento") ]



    imagebutton auto "images/mapa/cidade4_%s.png":
        xalign 0.03
        yalign 0.54
        action [ SetVariable("destino", "cidade4"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/pizzaria_%s.png":
        xalign 0.12
        yalign 0.54
        action [ SetVariable("destino", "pizzaria"), Jump("carro_evento") ]

    imagebutton auto "images/mapa/academia_%s.png":
        xalign 0.21
        yalign 0.54
        action [ SetVariable("destino", "academia"), Jump("carro_evento") ]



    imagebutton auto "images/china/china_%s.png":
        xalign 0.03
        yalign 0.71
        action [ SetVariable("destino", "china"), Jump("carro_evento") ]

    imagebutton auto "images/china/lamen_%s.png":
        xalign 0.12
        yalign 0.71
        action [ SetVariable("destino", "lamen"), Jump("carro_evento") ]

    imagebutton auto "images/china/superior_%s.png":
        xalign 0.21
        yalign 0.71
        action [ SetVariable("destino", "superior"), Jump("carro_evento") ]

    imagebutton auto "images/china/rua_%s.png":
        xalign 0.3
        yalign 0.71
        action [ SetVariable("destino", "rua"), Jump("carro_evento") ]



    imagebutton auto "images/china/caminho_%s.png":
        xalign 0.03
        yalign 0.88
        action [ SetVariable("destino", "caminho"), Jump("carro_evento") ]

    imagebutton auto "images/china/portal_%s.png":
        xalign 0.12
        yalign 0.88
        action [ SetVariable("destino", "portal"), Jump("carro_evento") ]

    imagebutton auto "images/china/templo_%s.png":
        xalign 0.21
        yalign 0.88
        action [ SetVariable("destino", "templo"), Jump("carro_evento") ]



    imagebutton auto "images/mapa/ilha_%s.png":
        xalign 0.5
        yalign 0.88
        action [ SetVariable("destino", "ilha"), Jump("carro_evento") ]

    if stifler_conheceu and stifler_e1 != "desistiu":

        imagebutton auto "images/mapa/distrito_%s.png":
            xalign 0.59
            yalign 0.88
            action [ SetVariable("destino", "distrito"), Jump("carro_evento") ]

label carro_evento:

    hide screen carro_escolhe with Dissolve(0.5)

    if destino == "ilha":

        scene black with dissolve

        jump call_cidade

    elif destino == "academia":

        if not academia:

            "Academia? Hahahaha!"

            "Até parece que eu vou gastar meu tempo pra bombar."

            "Eu tenho sorte de só poder comer pizza e lanche e não engordar, não tem porque perder tempo malhando. A vida é curta demais."

            "Pensando bem... se tivesse alguém interessante nessa academia... se pá até valeria à pena. Ou quem sabe pra conseguir uma pauta."

            "Bom... se alguma coisa mudar posso me inscrever, mas por enquanto eu quero sobreviver na capital! Aaahhh!"

            show screen carro_escolhe with Dissolve(0.5)

            pause

    elif destino == "distrito":

        if tempo < 3:

            "Visitar o Distrito de manhã ou à tarde pode chamar muita atenção. Melhor ir lá só durante a noite."

            show screen carro_escolhe with Dissolve(0.5)

            pause

        if xiang_escape >= 5 and not xiang_fim:

            if distrito_liberou:

                $ xiang_on = False

                "Mesmo com o rolo da Xiang, agora o Black Cash precisa de mim. Eles não vão me pegar."
            else:


                "Depois do que aconteceu lá quando eu salvei a [i] eu não volto lá nem ferrando."

                "E é bom eu ficar de olho aberto... mesmo aqui na ilha eu acho que eles podem vir atrás de mim."

                show screen carro_escolhe with Dissolve(0.5)

                pause

    mc "Bora!"

    play sound som_carro

    pause 1.0

    scene black with dissolve

    scene carro_mc_cidade1 with Dissolve(1.0)

    pause 2.0

    scene black with dissolve

    if destino == "cidade1":

        jump cidade1

    elif destino == "boutique":

        jump boutique

    elif destino == "fliperama":

        jump cidade_fliperama

    elif destino == "cidade2":

        jump cidade2

    elif destino == "biblioteca":

        jump biblioteca_1andar

    elif destino == "cinema":

        jump cidade_cinema

    elif destino == "universidade":

        jump cidade_universidade

    elif destino == "cidade3":

        jump cidade3

    elif destino == "prefeitura":

        jump cidade_prefeitura

    elif destino == "tkf":

        jump cidade_tkf

    elif destino == "faux":

        jump cidade_faux

    elif destino == "cidade4":

        jump cidade4

    elif destino == "pizzaria":

        jump cidade_pizzaria

    elif destino == "academia":

        if academia:

            "Acho que tô afim de dar aquela treinada."

            jump cidade_academia
        else:


            "Academia? Hahahaha!"

            "Até parece que eu vou gastar meu tempo pra bombar."

            "Eu tenho sorte de só poder comer pizza e lanche e não engordar, não tem porque perder tempo malhando. A vida é curta demais."

            "Pensando bem... se tivesse alguém interessante nessa academia... se pá até valeria à pena. Ou quem sabe pra conseguir uma pauta."

            "Bom... se alguma coisa mudar posso me inscrever, mas por enquanto eu quero sobreviver na capital! Aaahhh!"

            show screen carro_escolhe with Dissolve(0.5)

            pause

    elif destino == "china":

        jump cidade_chinesa

    elif destino == "lamen":

        jump chinatown_lamen

    elif destino == "superior":

        jump chinatown_superior

    elif destino == "rua":

        jump chinatown_rua

    elif destino == "caminho":

        jump chinatown_caminho

    elif destino == "portal":

        jump chinatown_portal

    elif destino == "templo":

        jump cenario_templo

    elif destino == "distrito":

        jump cenario_distrito
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
