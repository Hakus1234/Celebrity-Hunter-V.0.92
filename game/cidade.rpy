label pre_tela:





    if area == "ilha":

        play sound "audio/som_38_passos2.mp3"
    else:


        play sound "audio/som_35_passos.mp3"

    hide screen cidade_tela
    with dissolve

    return

label pos_tela:

    show screen cidade_tela
    with dissolve

    return

label ilha_cidade_bus:

    hide screen onibus_cidade with Dissolve(0.2)

    $ estou_na_cidade = False

    call cena_onibus from _call_cena_onibus_10

    jump cidade1

label ilha_voltar_bus:

    hide screen cidade_tela with Dissolve(0.5)

    if carro:

        jump voltar_carro
    else:


        "Já vou voltar pra ilha?"

        menu:
            "Sim":


                "Bora pra casa."

                scene black with Dissolve(1.0)

                $ tempo += 1

                if tempo < 3:

                    scene mc onibus with Dissolve(1.0)
                else:


                    scene mc onibus_noite with Dissolve(1.0)

                "..."

                jump call_cidade
            "Não":


                "Ainda tenho coisas pra fazer aqui."

                show screen cidade_tela with Dissolve(0.5)

                pause

label voltar_carro:

    hide screen cidade_tela with Dissolve(0.5)

    "Já vou voltar pra ilha?"

    menu:
        "Sim":


            "Deixa eu pegar o carro."

            play sound som_carro

            scene black with Dissolve(1.0)

            scene carro_mc_cidade2 with Dissolve(1.0)

            pause

            jump call_cidade
        "Não":


            "Ainda tenho coisas pra fazer aqui."

            show screen cidade_tela with Dissolve(0.5)

            pause



label praia_voltar_ilha:

    hide screen cidade_tela
    with dissolve

    "Bora voltar."

    scene black with dissolve

    $ tempo += 1

    jump call_cidade

label praia1:

    call pre_tela from _call_pre_tela_3

    $ estou_na_cidade = False

    $ area = "ilha"
    $ mapa = "praia1"

    scene ilha praia with Dissolve(1.0)

    call pos_tela from _call_pos_tela_1

    pause

label praia2:

    call pre_tela from _call_pre_tela_4

    $ area = "ilha"
    $ mapa = "praia2"

    scene ilha praia_quiosque with Dissolve(1.0)

    call pos_tela from _call_pos_tela_2

    pause

label praia3:

    call pre_tela from _call_pre_tela_5

    $ area = "ilha"
    $ mapa = "praia3"

    if tempo == 3 and quincy_e1 and not quincy_e2:

        call quincy_evento3 from _call_quincy_evento3

        call pos_tela from _call_pos_tela_3

        pause

    scene ilha praia_gazebo with Dissolve(1.0)

    call pos_tela from _call_pos_tela_4

    pause

label praia4:

    call pre_tela from _call_pre_tela_6

    $ area = "ilha"
    $ mapa = "praia4"

    if tempo == 1:

        scene praia dia with Dissolve(1.0)

    elif tempo == 2:

        scene praia tarde with Dissolve(1.0)

    call pos_tela from _call_pos_tela_5

    pause

label praia4_passear:

    hide screen cidade_tela
    with dissolve

    "Deixa eu curtir um pouco essa praia."

    if tempo == 1:

        play sound "audio/som_13_praia.mp3"

        scene mc praia_dia with Dissolve(1.0)

        "Nesta hora o sol ainda tá fraquinho. É muito bom andar pela areia."

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

    jump praia4



label cidade1:

    call pre_tela from _call_pre_tela_7

    $ area = "cidade"
    $ mapa = "cidade1"
    $ submapa = "nada"

    if tempo == 3 and quincy_e3 and not quincy_e4:

        $ fundo_especial = True

        scene cidade centro1 with Dissolve(1.0)

        pause

        jump quincy_evento5

        call pos_tela from _call_pos_tela_6

        pause

    scene cidade centro1 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_7

    pause

label cidade_fliperama:

    call pre_tela from _call_pre_tela_8

    $ area = "cidade"
    $ mapa = "cidade1"
    $ submapa = "fliperama"

    scene cidade fliperama with Dissolve(1.0)

    if nona_e1 == "banco":

        jump nona_evento1_final

    call pos_tela from _call_pos_tela_8

    pause

label cidade2:

    call pre_tela from _call_pre_tela_9

    $ area = "cidade"
    $ mapa = "cidade2"
    $ submapa = "nada"

    scene cidade centro2 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_9

    pause

label cidade_museu:

    call pre_tela from _call_pre_tela_10

    $ area = "cidade"
    $ mapa = "cidade2"
    $ submapa = "museu"

    scene cidade museu with Dissolve(1.0)

    call pos_tela from _call_pos_tela_10

    pause

label cidade_cinema:

    call pre_tela from _call_pre_tela_11

    $ area = "cidade"
    $ mapa = "cidade2"
    $ submapa = "cinema"

    scene cidade centro12 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_11

    pause

label cidade_universidade:

    call pre_tela from _call_pre_tela_12

    $ area = "cidade"
    $ mapa = "cidade2"
    $ submapa = "universidade"

    if tempo == 3 and quincy_e2 and not quincy_e3:

        $ fundo_especial = True

    scene cidade universidade with Dissolve(1.0)

    call pos_tela from _call_pos_tela_12

    pause

label uni1:

    call pre_tela from _call_pre_tela_13

    $ area = "universidade"
    $ mapa = "uni1"

    scene uni_hall geral with Dissolve(1.0)

    if tempo == 3 and quincy_e2 and not quincy_e3:

        jump quincy_evento4

        call pos_tela from _call_pos_tela_13

        pause

    call pos_tela from _call_pos_tela_14

    pause

label uni2:

    call pre_tela from _call_pre_tela_14

    $ area = "universidade"
    $ mapa = "uni2"

    scene uni_biblioteca geral with Dissolve(1.0)

    call pos_tela from _call_pos_tela_15

    pause

label uni3:

    call pre_tela from _call_pre_tela_15

    $ area = "universidade"
    $ mapa = "uni3"

    scene uni_quadra geral with Dissolve(1.0)

    call pos_tela from _call_pos_tela_16

    pause

label cidade3:

    call pre_tela from _call_pre_tela_16

    $ area = "cidade"
    $ mapa = "cidade3"
    $ submapa = "nada"

    scene cidade centro3 with Dissolve(1.0)

    if sayuri_e7 == "pre" and tempo == 1:

        jump sayuri_evento7

    call pos_tela from _call_pos_tela_17

    pause

label cidade_prefeitura:

    call pre_tela from _call_pre_tela_17

    $ area = "cidade"
    $ mapa = "cidade3"
    $ submapa = "prefeitura"

    scene cidade centro9 with Dissolve(1.0)

    if xiang_escape == 1:

        $ xiang_escape = 2

        jump xiang_escape1

    call pos_tela from _call_pos_tela_18

    pause

label cidade_tkf:

    call pre_tela from _call_pre_tela_18

    $ area = "cidade"
    $ mapa = "cidade3"
    $ submapa = "tkf"

    scene cidade tkf with Dissolve(1.0)

    if gadget_final and not tkf_evento1:

        "Aqui. O lugar que apareceu naquele holograma..."

        "Eu tenho certeza absoluta que foi isso que eu vi quando aquelas três peças brilharam."

        "Eu preciso falar com eles sobre isso."

    call pos_tela from _call_pos_tela_19

    pause

label tkf_entrada:

    call pre_tela from _call_pre_tela_19

    if area == "cidade":

        if tempo < 3:

            "Essa empresa me dá calafrios."
        else:


            "Eles não ficam abertos duran-"

            mc desconfiado "Hm?"

            "{size=17}{i}Zzzzznnnnnnnn{/i}{/size}"

            mc "Que merda de barulho é esse? Parece uma serra..."

            "Melhor eu sair daqui."

            show screen cidade_tela
            with dissolve

            pause

    $ area = "tkf"
    $ mapa = "tkf1"

    scene tkf_entrada with Dissolve(1.0)

    if not tkf_1vez:

        $ tkf_1vez = True

        pause

        "Que porra de lugar é esse?"

        "Olha pra esse visual. Espera. Parece... parece que eu já vi esse lugar antes."

        "Mas eu tenho certeza que nunca vim aqui."

        "Essas cadeiras... esse design. Eu tenho certeza. Aliás, isso só pode dizer uma coisa."

        show moena ola with moveinbottom

        mo "Seja bem-vindo à sede das Corporação TKF. Como posso ajudar?"

        mc surpreso "!"

        mo "Senhor? Posso ser de alguma ajuda?"

        mc envergonhado "Você podia começar não me matando do coração."

        $ mo_nome = "Moena"

        show moena incerta with dissolve

        mo "Senhor, eu não pretendo te matar. Isso é um absurdo. [mo] está aqui para auxiliar."

        mc desconfiado "Hm?"

        mc envergonhado "É... eu sei. Foi só uma expressão."

        mo "Eu não entendi essa expressão."

        mc "Tudo bem."

        menu:
            "Você tem um nome muito bonito.":


                $ moena_nome = True

                mc charmoso "Achei seu nome bem diferente, muito bonito."

                show moena ola with dissolve

                mo "Muito obrigada."
            "Acho que eu nunca ouvi seu nome antes.":


                mc desconfiado "[mo]... acho que nunca ouvi esse nome na minha vida."

                show moena ola with dissolve

                mo "Realmente não é um nome muito conhecido nesta região do mundo."

        mo "Meu nome é de origem japonesa, e tem diversos significados."

        mc desconfiado "Como assim?"

        mo "O significado do meu nome depende dos kanjis que você usar para formá-lo."

        mo "Pelo menos é o que me falaram..."

        mc normal "Então é um nome oriental."

        mo "Exatamente. É um nome japonês. Bem interessante, não acha?"

        mc normal "Com certeza."

        mo "O senhor é muito gentil. Mas me diga."
    else:


        show moena ola with dissolve

        mo "Seja bem-vindo à sede das Corporação TKF."

    mo "Como posso ajudar?"

    label tkf_moena_menu:

        pass

    menu:

        "Eu vi um holograma que mostrava este lugar..." if gadget_final and not tkf_evento1:

            $ tkf_evento1 = True

            jump tkf_evento1

            pause
        "O que a TKF faz?":


            mc normal "[mo], o que sua empresa - TKF, né? - O que ela faz?"

            mo "A TKF é uma das mais avançadas corporações do mundo em avanço tecnológico."

            mo "Nós trabalhamos incessantemente para contribuir com o progresso da tecnologia nas mais diversas esferas."

            mo "O trabalho da TKF abrange tanto o mundo offline como o online, desde pesquisa até produção, estando na vanguarda da evolução humana."

            mc charmoso "Puxa. Parece incrível."

            mo "E é. A TKF tem diversos laboratórios espalhados pelo mundo e recebe bilhões em financiamento todos os anos."

            mo "Nosso objetivo é transformar a vida de milhões de seres humanos por meio dos avanços descobertos e produzidos por nós."

            mc "Meus parabéns. Você deve estar muito orgulhosa do seu trabalho."

            show moena incerta with dissolve

            mo "Eu?"

            mc "Sim."

            mo "Não não, senhor. Eu sou apenas uma recepcionista aqui na sede. Todos louros devem ser dirigidos para nossa extensa e capaz equipe de engenheiros."

            mc normal "Mas se não fosse por você, eu não saberia nada disso. Pra mim, você também faz um excelente trabalho."

            mo "O-obrigada, senhor..."

            mo "Posso ajudar com mais alguma coisa?"

            jump tkf_moena_menu
        "Quem é você?":


            mc charmoso "Seu nome é [mo], certo? O que você faz aqui?"

            show moena ola with dissolve

            mo "Minha função é recepcionar nossos inestimáveis visitantes, como você, e lhes explicar sobre a incrível missão da TKF."

            mo "Não somos apenas uma corporação, mas uma ferramenta para a evolução da raça humana nas mais diversas esferas."

            mc normal "E é legal trabalhar aqui?"

            show moena incerta with dissolve

            mo "Como assim 'legal'?"

            mc desconfiado "Como como assim? Você gosta de trabalhar aqui?"

            mo "Gostar..."

            mo "..."

            mo "..."

            mc desconfiado "[mo]?"

            mo "Ah!"

            show moena ola with dissolve

            mo "Posso ajudar com mais alguma coisa?"

            mc desconfiado "?"

            jump tkf_moena_menu
        "Era isso. Tenha um bom dia, [mo].":


            mc normal "Já vou indo nessa, [mo]. Obrigado."

            mo "Volte sempre que precisar e tenha um bom dia, senhor."

            hide moena with dissolve

            scene black with dissolve

            jump cidade3

    call pos_tela from _call_pos_tela_20

    pause

label cidade_faux:

    call pre_tela from _call_pre_tela_20

    $ area = "cidade"
    $ mapa = "cidade3"
    $ submapa = "faux"

    scene cidade faux with Dissolve(1.0)

    if sofia_e3 == "pre":

        if tempo == 2:

            jump sofia_evento3
        else:


            "Eu marquei com a [w] de vir aqui na parte da tarde."

            "Tenho que voltar aqui quando o céu tiver alaranjado."

            mc zerado "Como se eu não soubesse que horas é à tarde."

            mc desconfiado "Às vezes eu sinto que esses pensamentos que eu tenho é pra outra pessoa. Que doideira..."

    call pos_tela from _call_pos_tela_21

    pause

label cidade4:

    call pre_tela from _call_pre_tela_21

    $ area = "cidade"
    $ mapa = "cidade4"
    $ submapa = "nada"
    $ submapa2 = "nada"

    scene cidade centro4 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_22

    pause

label cidade_china:

    call pre_tela from _call_pre_tela_22

    $ area = "cidade"
    $ mapa = "cidade4"
    $ submapa = "china"

    scene cidade centro6 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_23

    pause

label cidade_pizzaria:

    call pre_tela from _call_pre_tela_23

    $ area = "cidade"
    $ mapa = "cidade4"
    $ submapa = "pizzaria"
    $ submapa2 = "nada"

    scene cidade pizzaria with Dissolve(1.0)

    call pos_tela from _call_pos_tela_24

    pause

label cidade_pizzaria_out:

    call pre_tela from _call_pre_tela_24

    $ area = "cidade"
    $ mapa = "cidade4"
    $ submapa = "pizzaria"
    $ submapa2 = "pizzaria_out"

    if tempo == 3 and diana_e4 == "pre":

        jump diana_evento4

    elif tempo == 2 and nathan_e5 == "pre":

        jump nathan_evento5

    elif natasha_e2 == "ana" and tempo == 3 and submapa2 != "pizzaria_in":

        $ natasha_e2 = "segredo"

        "..."

        "Eu pensei... pensei... pensei..."

        "E o lugar que mais se encaixa é aqui. A Pizzaria Alighieri."

        "É um lugar familiar, tranquilo, tem boa comida, é chique e fica aqui no continente."

        "Eu lembro que o [gar] disse alguma coisa sobre ter medo do sol ou alguma coisa assim. Talvez ele queira dizer à noite."

        "Pior é que eu podia ter perguntado pra [ana] que horas que ele recebeu a ligação aquela vez."

        mc zerado "Que anta..."

        "Mas se eu estiver certo... ele pode aparecer aqui..."

        "Agora só tenho que ter sorte... dele estar aqui bem agora..."

        "..."

        "..."

        "..."

        "..."

        "..."

        "..."

        "{i}zZzZzzZz{/i}"

        mc surpreso "!"

        mc zerado "Nada dele..."

        "Mas não vou desistir. Talvez em outro momento ou outro dia..."

    elif natasha_e2 == "segredo" and tempo == 3 and submapa2 != "pizzaria_in":

        $ randh = random.randint(1,10)

        if randh == 1:

            jump natasha_e2_barao_chefao
        else:


            "Se eu concluí tudo ceritnho, o Barão vai aparecer aqui..."

            "..."

            "..."

            "..."

            "..."

            "..."

            "..."

            "{i}zZzZzzZz{/i}"

            mc surpreso "!"

            mc zerado "Nada dele..."

            "Mas não vou desistir. Talvez em outro momento ou outro dia..."

    if tempo < 3:

        scene cidade pizzaria_out_dia with Dissolve(1.0)
    else:


        $ randh = random.randint(1,2)

        if randh == 1:

            scene pizzaria_out_noite with Dissolve(1.0)
        else:


            scene pizzaria_out_italiano with Dissolve(1.0)

            "Hoje aquele cara tá aqui de novo..."

    call pos_tela from _call_pos_tela_25

    pause

label cidade_pizzaria_in:

    call pre_tela from _call_pre_tela_25

    $ area = "cidade"
    $ mapa = "cidade4"
    $ submapa = "pizzaria"
    $ submapa2 = "pizzaria_in"

    scene cidade pizzaria_interior with Dissolve(1.0)

    call pos_tela from _call_pos_tela_26

    pause

label museu1:

    call pre_tela from _call_pre_tela_26

    if area == "cidade":

        if tempo < 3:

            "Deixa eu dar uma passada no museu."
        else:


            "O museu fecha no fim da tarde. Vou ter que deixar pra amanhã."

            show screen cidade_tela
            with dissolve

            pause

    $ area = "museu"
    $ mapa = "museu1"

    scene museu1 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_27

    pause

label museu2:

    call pre_tela from _call_pre_tela_27

    $ area = "museu"
    $ mapa = "museu2"

    scene museu2 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_28

    pause

label museu3:

    call pre_tela from _call_pre_tela_28

    $ area = "museu"
    $ mapa = "museu3"

    scene museu3 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_29

    pause

label museu4:

    call pre_tela from _call_pre_tela_29

    $ area = "museu"
    $ mapa = "museu4"

    scene museu4 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_30

    pause

label biblioteca_1andar:

    call pre_tela from _call_pre_tela_30

    $ area = "museu"
    $ mapa = "biblioteca1"

    scene biblioteca geral with Dissolve(1.0)

    if julia_e6 == "pre" and tempo == 1:

        jump julia_evento6

    call pos_tela from _call_pos_tela_31

    pause

label biblioteca_2andar:

    call pre_tela from _call_pre_tela_31

    $ area = "museu"
    $ mapa = "biblioteca2"

    scene biblioteca 2andar with Dissolve(1.0)

    call pos_tela from _call_pos_tela_32

    pause

label biblioteca:

    hide screen cidade_tela
    with dissolve

    "Tem um monte de livro aqui. Será que tem alguma coisa que pode ser útil?"

    menu:
        "A Fundação da Capital":










            scene biblioteca mc_lendo with Dissolve(1.0)

            "{i}Este livro fala sobre como a capital surgiu e como ela se tornou o que é hoje{/i}"

            label biblioteca_livro3:

                mc "Interessante..."

            menu:
                "Capítulo 1 - Imigração":


                    "{i}A história da capital se confunde com a história do país em vários pontos.{/i}"

                    "{i}Ponto de chegada de imigrantes de diversos continentes, a terra onde a capital se encontra se tornou ponto de prosperidade e conflito.{/i}"

                    "{i}Quando os primeiros viajantes do Velho Mundo chegaram ao país, notaram que o solo desta terra era diferente de seu reino de origem.{/i}"

                    "{i}As cores vivas e reluzentes da terra denunciavam a existência de um mineral raro, que mais tarde ganhou diversos usos na tecnologia.{/i}"

                    "{i}Os primeiros a chegar foram os italianos e, notando a riqueza do solo, criaram as primeiras construções. Logo seguiram os chineses.{/i}"

                    "{i}Italianos e chineses se envolveram em diversos combates no decorrer de décadas, conflito que recebeu o nome de Guerra do Minério.{/i}"

                    "{i}Fugindo do velho mundo que escravizava suas nações, povos de origem africana deixaram o continente e se refugiaram na capital.{/i}"

                    "{i}Mesmo vindo de três continentes distintos, os povos conseguiram delimitar regiões e após cerca de 200 anos os conflitos acabaram.{/i}"

                    "{i}Os Imigrantes, como ficaram conhecidos os primeiros habitantes da capital do Novo Mundo, levantaram a cidade que hoje vivemos.{/i}"

                    "{i}Pessoas de várias nações hoje vivem na capital, mas estes três grupos ainda são o de maior tamanho segundo a pesquisa mais recente.{/i}"

                    jump biblioteca_livro3
                "Capítulo 2 - Civilização Antiga":


                    "{i}Estudos arqueológicos realizados na capital comprovaram a existência de uma civilização antiga pré-colonização.{/i}"

                    "{i}Ruínas de templos e até mesmo de centros habitados foram encontrados na região. Artefatos podem ser vistos em museus pelo mundo.{/i}"

                    "{i}Essa civilização antiga não foi determinada ainda, mas pesquisadores continuam observando sítios e artefatos em busca de respostas.{/i}"

                    "{i}Tábulas encontradas apresentam escrita cuneiforme, tida como a primeira forma de escrita utilizada pelo homem.{/i}"

                    "{i}Do que foi recuperado e traduzido, a teoria dominante afirma que esse povo não se originou no continente, mas veio de outro lado do globo.{/i}"

                    "{i}Por que esse povo deixou a terra de origem e se mudou para esta região ainda é desconhecido, mas algo aconteceu em sua terra natal.{/i}"

                    "{i}Arqueólogos datam o início dessa civilização a milhares de anos antes de Cristo, tornado-os, possivelmente, um dos primeiros assentamentos humanos.{/i}"

                    "{i}Por que vieram e o que ocorreu com esse povo... ainda não existem respostas para essas perguntas.{/i}"

                    jump biblioteca_livro3
                "Eu já li o suficiente. Bora sair daqui":


                    jump biblioteca_2andar

        "?????" if sacerdotisas == 0:

            "{b}Para liberar este livro você precisa descobrir um segredo na história da Júlia (Final 2){/b}"

            "{b}Se você fizer esse final e carregar em um ponto anterior, o livro continuará liberado{/b}"

            "{b}Mesmo que você reinicie o game, contanto que você não exclua o app, o livro continuará liberado{/b}"

        "Prostituição Sagrada e os Rituais Sexuais" if sacerdotisas > 0:

            scene biblioteca mc_lendo with Dissolve(1.0)

            "{i}Este livro traz estudos do sexo como um ritual religioso desde a primeira civilização humana até a atualidade.{/i}"

            "{i}Este livro não é recomendado para menores de 18 anos.{/i}"

            label biblioteca_livro4:

                mc "Vamos ver..."

            menu:
                "Capítulo 1 - Prostituição Sagrada, Inanna e Energia da Fertilidade":


                    "{i}Um dos principais rituais praticados na Suméria se chamava Prostituição Sagrada ou Matrimônio Sagrado.{/i}"

                    show livro3_img1 with Dissolve(1.0)

                    "{i}Nesse ritual, o rei tinha uma relação sexual com a sacerdotisa de um dos templos dedicados à deusa Inanna.{/i}"

                    "{i}A deusa de nome Inanna na Suméria e depois Ishtar na Mesopotâmia, representava a fertilidade, o amor e a boa ventura.{/i}"

                    "{i}Durante o ritual, a sacerdotisa encarnava a deusa e o sexo entre ela e o rei simbolizava a união entre homens e deuses.{/i}"

                    "{i}A comunhão sexual entre os dois liberava a Energia da Fertilidade, que ajudava o reino na lavoura e com as intempéries.{/i}"

                    "{i}Já a sacerdotisa que oferecia seu corpo à deusa era uma virgem que crescia reclusa no templo especialmente para esse ato.{/i}"

                    "{i}Era um ato de grande honra e celebrado por toda a capital, pois todos sabiam dos benefícios para a sociedade.{/i}"

                    "{i}Era comum também que homens de grande virilidade fossem levados até o templo para terem relaxões sexuais.{/i}"

                    "{i}Esses homens transavam com as sacerdotisas de Inanna e esse ato liberava constantemente Energia para o bem do reino.{/i}"

                    hide livro3_img1 with Dissolve(1.0)

                    "{i}Com o passar dos séculos, essa tradição se perdeu, mas alguns juram que grupos ainda realizam o ritual nas sombras.{/i}"

                    jump biblioteca_livro4
                "Capítulo 2 - Período Jomon, China e Suméria":


                    "{i}O Período Jomon é o período japonês que começa em 14.000 A.C. e vai até 300 A.C. É o tempo mais antigo do país.{/i}"

                    show livro3_img2 with Dissolve(1.0)

                    "{i}Durante esse período, várias técnicas e elementos culturais vieram da China no contiente para as ilhas japonesas.{/i}"

                    "{i}O estudioso francês Albert Terrien de Lacouperie afirmou em 1892 que a China foi criada por imigrantes babilônicos.{/i}"

                    "{i}A Babilônia, por sua vez, era uma cidade da Mesopotâmia, que, em sua primeira forma, era chamada de Suméria.{/i}"

                    "{i}Os sumérios deram origem à Mesopotâmia e levaram seu conhecimento para várias regiões do mundo, como o Egito.{/i}"

                    "{i}No Egito, na Cultura Naqada, vemos a poderosa influência da Suméria, como na adaga Gebel el-Arak e em gravuras diversas.{/i}"

                    "{i}Dessa forma, é possível dizer que os sumérios levaram sua influência para diversas regiões da Ásia, inclusive no Japão.{/i}"

                    "{i}Muitas dessas teorias foram desafiadas pela atual comunidade acadêmica e a lembrança da Suméria se perde a cada dia.{/i}"

                    "{i}Entretanto muitos ainda acreditam que os sumérios foram os grandes pais da Civilização e lá surgiram todas as jóias da humanidade.{/i}"

                    hide livro3_img2 with Dissolve(1.0)

                    "{i}Dessa forma, existe a suposição de que os rituais dos deuses sumérios são reproduzidos até hoje em várias partes do Mundo.{/i}"

                    jump biblioteca_livro4
                "Capítulo 3 - Utagaki e as Sacerdotisas da Lua":


                    "{i}Utagaki é um ritual praticado no Japão até hoje. Mas, com o passar do tempo, ele perdeu muito de suas origens.{/i}"

                    show livro3_img3 with Dissolve(1.0)

                    "{i}Não se sabe ao certo quando o primeiro Utagaki aconteceu, mas seu pico foi no Período Nara, no Século VIII.{/i}"

                    "{i}No dia do ritual, habitanes de diversas vilas subiam ao topo da montanha para celebrar a chegada da primavera e honrar os deuses.{/i}"

                    "{i}Durante o Utagaki, era permitido ter relações sexuais abertas entre os moradores, sem nenhum tipo de tabu social.{/i}"

                    "{i}De forma prática, o ritual mantinha a taxa de natalidade das aldeias, promovendo a fertilidade e virilidade de seus membros.{/i}"

                    "{i}Mas, para aquelas pessoas, era muito mais do que isso. Era a chance de entrar em contato com os deuses e oferecer uma festa em seu nome.{/i}"

                    "{i}Antes da liberação sexual, sacerdotisas realizavam a kagura, uma dança tradicional. Naquele momento, a deusa encarnava em seu corpo.{/i}"

                    "{i}Por meio dos atos sexuais, os deuses dividiam sua energia com todos, trazendo boa ventura para todos que viviam na região.{/i}"

                    "{i}Hoje, o Utagaki não conta mais com a liberação sexual. Mas existem rumores de que grupos específicos continuam o realizando da forma antiga.{/i}"

                    hide livro3_img3 with Dissolve(1.0)

                    "{i}Garotas são criadas para serem Sacerdotisas da Lua e então doarem seus corpos para que a deusa possa ter relações sexuais com os humanos.{/i}"

                    jump biblioteca_livro4
                "Eu já li o suficiente. Bora sair daqui":


                    jump biblioteca_2andar
        "Seção Reservada (+18)":


            if livros_liberados < 1:

                "Hm? Seção reservada para adultos..."

                "O que que tem aqui?"
            else:


                "Bora dar uma olhada naquelas mulheres incríveis."

            menu:
                "As Sacerdotisas de Inanna (+18)":


                    "{i}Este livro tem mais de 100 fotos exclusivas de sacerdotisas do Templo de E-anna, em Uruk, na antiga Suméria.{/i}"

                    "{i}As fotos foram geradas por meio de descrições e relatos descobertos em tabuletas cuneiforme vindas de 1.000 A.C.{/i}"

                    menu:
                        "Sacerdotisas de Inanna - Volume 1 (+18)":


                            if livros_liberados < 1:

                                $ proibido_salvar = True
                                $ show_quick_menu = False

                                "Droga. Essa seção da Biblioteca não é grátis. Pra ler estes livros eu tenho que pagar."

                                python:
                                    if renpy.android:
                                        livros_liberados_db = PythonSDLActivity.pegaLivros()

                                "E olha o preço! C$ 250! Esses livros adultos devem ser bons mesmos..."

                                "{i}Este volume contém 20 fotos exclusivas de sacerdotisas de Inanna em seu traje tradicional ou nuas.{/i}"

                                "{i}Estas fotos não são recomendadas para menores de 18 anos. Contamos com a colaboração de todos.{/i}"

                                if livros_liberados < livros_liberados_db:

                                    "{b}Você já liberou os livros [livros_liberados_db] vezes. Mas neste gameplay você liberou [livro_liberados] livros.{/b}"

                                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, o próximo livro será liberado automaticamente.{/b}"

                                    $ livros_liberados += 1

                                    jump livro1_evento

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "Certo. Parece que vai custar C$ 250."

                                "Eu tô com {b}R$ [cash]{/b}."

                                $ renpy.choice_for_skipping()

                                if cash >= 250:

                                    "Eu tenho dinheiro suficiente."

                                    menu:

                                        "Comprar acesso ao Volume 1 por {b}C$ 250{/b}" if livros_liberados < 1:

                                            python:
                                                if renpy.android:
                                                    
                                                    livros_liberados_db = PythonSDLActivity.pegaLivros()
                                                    
                                                    if livros_liberados == livros_liberados_db:
                                                        PythonSDLActivity.addLivros()
                                                        
                                                        livros_liberados += 1



                                                renpy.block_rollback()

                                            "{b}Você usou C$ 250 para liberar este volume{/b}"

                                            if not renpy.variant("android"):

                                                $ livros_liberados += 1

                                            jump livro1_evento
                                        "Melhor deixar pra outra hora":


                                            "Nem tô afim agora. Melhor deixar pra outra hora."

                                            jump biblioteca_2andar
                                else:


                                    show black with Dissolve(1.0)

                                    p lecionando "Ixi. O [mc] não tem C$ 250. Tá pobre que só ele..."

                                    p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                                    p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                    p "Você quer comprar C$ agora?"

                                    menu:
                                        "Sim. Tô com uma graninha sobrando aqui.":


                                            p rindo "Que bom!"

                                            call comprar_cash

                                            p "Se pagar por PIX, não esqueça de mandar o comprovante. Se pagou pelo Mercado Pago não precisa."

                                            p "Pode demorar até 24 horas para seus créditos caírem. Se demorar mais que isso, envie um e-mail para contato@geiko.net."

                                            p "Centenas de pessoas compram nos nossos games todo mês, então pode ficar tranquilo. Qualquer problema, vamos te ajudar."

                                            p "Bom jogo!"
                                        "Sem chance.":


                                            p "É sua aescolha! Bom jogo!"

                                    hide black with dissolve

                                jump biblioteca_2andar
                            else:


                                label livro1_evento:

                                    $ proibido_salvar = False
                                    $ show_quick_menu = True

                                scene black with dissolve

                                scene livro1_adulto1 with dissolve

                                "{i}Na antiga Suméria, garotas eram entregues ao maior templo do reino chamado E-anna, na cidade de Uruk.{/i}"

                                "{i}Estas jovens tinham uma vida de retidão, e eram preparadas para terem seus corpos usados em rutais sagrados.{/i}"

                                "{i}Segundo as lendas, essas sacerdotisas receberiam a deusa Inanna, e então a deusa usava seus corpos para transar.{/i}"

                                "{i}A deusa mantinha relações sexuais com reis, príncipes, ou qualquer homem viril que visitasse seu templo.{/i}"

                                "{i}Veja fotos dessas mulheres que viviam para terem seus corpos usados nesses rituais sexuais.{/i}"

                                scene black with dissolve

                                scene livro1_adulto2 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto3 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto4 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto5 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto6 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto7 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto8 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto9 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto10 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto11 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto12 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto13 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto14 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto15 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto16 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto17 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto18 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto19 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto20 with dissolve

                                pause

                                scene black with dissolve

                                scene livro1_adulto21 with dissolve

                                pause

                                scene black with dissolve

                                scene biblioteca mc_lendo with Dissolve(1.0)

                                "{i}Veja sacerdotisas ainda mais quentes no nosso próximo Volume.{/i}"

                                "Essas foram todas as fotos. Quantas mulheres fantásticas."

                                "Quem dera eu pudesse voltar pra aquela época e entrar nesse templo."

                                "Essa deusa Inanna deve saber transar como ninguém... t-tô babando!"

                                jump biblioteca_2andar



                        "Sacerdotisas de Inanna - Volume 2 (+18)" if livros_liberados >= 1:

                            if livros_liberados < 2:

                                $ proibido_salvar = True
                                $ show_quick_menu = False

                                "Este também custa C$ 250. Deve ser ainda melhor que o primeiro!"

                                python:
                                    if renpy.android:
                                        livros_liberados_db = PythonSDLActivity.pegaLivros()

                                "{i}Este volume contém 20 fotos exclusivas de sacerdotisas de Inanna em seu traje tradicional ou nuas.{/i}"

                                "{i}Estas fotos não são recomendadas para menores de 18 anos. Contamos com a colaboração de todos.{/i}"

                                if livros_liberados < livros_liberados_db:

                                    "{b}Você já liberou os livros [livros_liberados_db] vezes. Mas neste gameplay você liberou [livro_liberados] livros.{/b}"

                                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, o próximo livro será liberado automaticamente.{/b}"

                                    $ livros_liberados += 1

                                    jump livro2_evento

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "Certo. Parece que vai custar C$ 250."

                                "Eu tô com {b}R$ [cash]{/b}."

                                $ renpy.choice_for_skipping()

                                if cash >= 250:

                                    "Eu tenho dinheiro suficiente."

                                    menu:

                                        "Comprar acesso ao Volume 2 por {b}C$ 250{/b}" if livros_liberados < 2:

                                            python:
                                                if renpy.android:
                                                    
                                                    livros_liberados_db = PythonSDLActivity.pegaLivros()
                                                    
                                                    if livros_liberados == livros_liberados_db:
                                                        PythonSDLActivity.addLivros()
                                                        
                                                        livros_liberados += 1



                                                renpy.block_rollback()

                                            "{b}Você usou C$ 250 para liberar este volume{/b}"

                                            if not renpy.variant("android"):

                                                $ livros_liberados += 1

                                            jump livro2_evento
                                        "Melhor deixar pra outra hora":


                                            "Nem tô afim agora. Melhor deixar pra outra hora."

                                            jump biblioteca_2andar
                                else:


                                    show black with Dissolve(1.0)

                                    p lecionando "Ixi. O [mc] não tem C$ 250. Tá pobre que só ele..."

                                    p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                                    p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                    p "Você quer comprar C$ agora?"

                                    menu:
                                        "Sim. Tô com uma graninha sobrando aqui.":


                                            p rindo "Que bom!"

                                            call comprar_cash

                                            p "Se pagar por PIX, não esqueça de mandar o comprovante. Se pagou pelo Mercado Pago não precisa."

                                            p "Pode demorar até 24 horas para seus créditos caírem. Se demorar mais que isso, envie um e-mail para contato@geiko.net."

                                            p "Centenas de pessoas compram nos nossos games todo mês, então pode ficar tranquilo. Qualquer problema, vamos te ajudar."

                                            p "Bom jogo!"
                                        "Sem chance.":


                                            p "É sua aescolha! Bom jogo!"

                                    hide black with dissolve

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar
                            else:


                                label livro2_evento:

                                    $ proibido_salvar = True
                                    $ show_quick_menu = False

                                scene black with dissolve

                                scene livro2_adulto1 with dissolve

                                "{i}Neste Volume, trazemos mais fotos das sacerdotisas do templo de Inanna, chamado E-anna, na cidade de Uruk.{/i}"

                                "{i}Estas garotas eram confinadas no templo e deviam viver em busca do corpo perfeito para serem usadas posteriormente.{/i}"

                                "{i}Era uma grande honra ser a veste carnal da deusa do amor, e serem usadas para trazer boa ventura para o reino.{/i}"

                                "{i}Essas relações sexuais transcendiam o prazer e o ato sexual em si, e eram verdadeiros rituais sagrados.{/i}"

                                "{i}Mesmo assim, diversos homens viam essas mulheres como fonte de prazer e procuravam o templo para se satisfazer.{/i}"

                                scene black with dissolve

                                scene livro2_adulto2 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto3 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto4 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto5 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto6 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto7 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto8 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto9 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto10 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto11 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto12 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto13 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto14 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto15 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto16 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto17 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto18 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto19 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto20 with dissolve

                                pause

                                scene black with dissolve

                                scene livro2_adulto21 with dissolve

                                pause

                                scene black with dissolve

                                scene biblioteca mc_lendo with Dissolve(1.0)

                                "{i}Veja sacerdotisas ainda mais quentes no nosso próximo Volume.{/i}"

                                "Acho que eu tô viciando nessas belezinhas..."

                                "Eu preciso ver como as próximas são!"

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar

                        "Sacerdotisas Tocadas pela Deusa - Volume 3 (+18)" if livros_liberados >= 2:

                            if livros_liberados < 3:

                                $ proibido_salvar = True
                                $ show_quick_menu = False

                                "Este também custa C$ 250. Deve ser tão bom quanto o anterior!"

                                python:
                                    if renpy.android:
                                        livros_liberados_db = PythonSDLActivity.pegaLivros()

                                "{i}Este volume contém mais de 20 fotos exclusivas de sacerdotisas de Inanna nuas.{/i}"

                                "{i}Estas fotos não são recomendadas para menores de 18 anos. Contamos com a colaboração de todos.{/i}"

                                if livros_liberados < livros_liberados_db:

                                    "{b}Você já liberou os livros [livros_liberados_db] vezes. Mas neste gameplay você liberou [livro_liberados] livros.{/b}"

                                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, o próximo livro será liberado automaticamente.{/b}"

                                    $ livros_liberados += 1

                                    jump livro3_evento

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "Certo. Parece que vai custar C$ 250."

                                "Eu tô com {b}R$ [cash]{/b}."

                                $ renpy.choice_for_skipping()

                                if cash >= 250:

                                    "Eu tenho dinheiro suficiente."

                                    menu:

                                        "Comprar acesso ao Volume 3 por {b}C$ 250{/b}" if livros_liberados < 3:

                                            python:
                                                if renpy.android:
                                                    livros_liberados_db = PythonSDLActivity.pegaLivros()
                                                    
                                                    if livros_liberados == livros_liberados_db:
                                                        PythonSDLActivity.addLivros()
                                                        
                                                        livros_liberados += 1

                                                renpy.block_rollback()

                                            "{b}Você usou C$ 250 para liberar este volume{/b}"

                                            if not renpy.variant("android"):

                                                $ livros_liberados += 1

                                            jump livro3_evento
                                        "Melhor deixar pra outra hora":


                                            "Nem tô afim agora. Melhor deixar pra outra hora."

                                            jump biblioteca_2andar
                                else:


                                    show black with Dissolve(1.0)

                                    p lecionando "Ixi. O [mc] não tem C$ 250. Tá pobre que só ele..."

                                    p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                                    p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                    p "Você quer comprar C$ agora?"

                                    menu:
                                        "Sim. Tô com uma graninha sobrando aqui.":


                                            p rindo "Que bom!"

                                            call comprar_cash

                                            p "Se pagar por PIX, não esqueça de mandar o comprovante. Se pagou pelo Mercado Pago não precisa."

                                            p "Pode demorar até 24 horas para seus créditos caírem. Se demorar mais que isso, envie um e-mail para contato@geiko.net."

                                            p "Centenas de pessoas compram nos nossos games todo mês, então pode ficar tranquilo. Qualquer problema, vamos te ajudar."

                                            p "Bom jogo!"
                                        "Sem chance.":


                                            p "É sua aescolha! Bom jogo!"

                                    hide black with dissolve

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar
                            else:


                                label livro3_evento:

                                    $ proibido_salvar = True
                                    $ show_quick_menu = False

                                scene black with dissolve

                                scene livro3_adulto1 with dissolve

                                "{i}No templo de E-anna, havia uma câmara separada da construção principal. Lá, viviam sacerdotisas especiais.{/i}"

                                "{i}Estas mulheres apresentavam uma condição diferente das outras. E isso as tornavam naturalmente mais cobiçadas.{/i}"

                                "{i}Para os reis, príncipes e guerreiros que procuravam o ritual sagrado do sexo com a deusa, estas eram as primeiras escolhidas.{/i}"

                                "{i}A ligação destas garotas com a deusa vinha desde seu nascimento e isso era marcado no detalhe diferencial em seus corpos.{/i}"

                                "{i}Era o sinal de que Inanna havia escolhido aquela jovem como sua futura hospedeira para voltar a terra e distribuir o prazer.{/i}"

                                scene black with dissolve

                                scene livro3_adulto2 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto3 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto4 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto5 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto6 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto7 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto8 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto9 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto10 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto11 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto12 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto13 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto14 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto15 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto16 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto17 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto18 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto19 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto20 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto21 with dissolve

                                pause

                                scene black with dissolve

                                scene livro3_adulto22 with dissolve

                                pause

                                scene black with dissolve

                                scene biblioteca mc_lendo with Dissolve(1.0)

                                "{i}Veja sacerdotisas ainda mais quentes no nosso próximo Volume.{/i}"

                                "Então essas sacerdotisas especiais são ruivas. Interessante..."

                                "Tem algumas ruivas bem perigosas na minha vida..."

                                "Que delícia... quero mais!"

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar

                        "Sacerdotisas que Abandonaram o Templo - Volume 4 (+18)" if livros_liberados >= 3:

                            if livros_liberados < 4:

                                $ proibido_salvar = True
                                $ show_quick_menu = False

                                "Este também custa C$ 250. Deve ser tão bom quanto o anterior!"

                                python:
                                    if renpy.android:
                                        livros_liberados_db = PythonSDLActivity.pegaLivros()

                                "{i}Este volume contém mais de 20 fotos exclusivas de sacerdotisas de Inanna nuas.{/i}"

                                "{i}Estas fotos não são recomendadas para menores de 18 anos. Contamos com a colaboração de todos.{/i}"

                                if livros_liberados < livros_liberados_db:

                                    "{b}Você já liberou os livros [livros_liberados_db] vezes. Mas neste gameplay você liberou [livro_liberados] livros.{/b}"

                                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, o próximo livro será liberado automaticamente.{/b}"

                                    $ livros_liberados += 1

                                    jump livro4_evento

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "Certo. Parece que vai custar C$ 250."

                                "Eu tô com {b}R$ [cash]{/b}."

                                $ renpy.choice_for_skipping()

                                if cash >= 250:

                                    "Eu tenho dinheiro suficiente."

                                    menu:

                                        "Comprar acesso ao Volume 4 por {b}C$ 250{/b}" if livros_liberados < 4:

                                            python:
                                                if renpy.android:
                                                    livros_liberados_db = PythonSDLActivity.pegaLivros()
                                                    
                                                    if livros_liberados == livros_liberados_db:
                                                        PythonSDLActivity.addLivros()
                                                        
                                                        livros_liberados += 1

                                                renpy.block_rollback()

                                            "{b}Você usou C$ 250 para liberar este volume{/b}"

                                            if not renpy.variant("android"):

                                                $ livros_liberados += 1

                                            jump livro4_evento
                                        "Melhor deixar pra outra hora":


                                            "Nem tô afim agora. Melhor deixar pra outra hora."

                                            jump biblioteca_2andar
                                else:


                                    show black with Dissolve(1.0)

                                    p lecionando "Ixi. O [mc] não tem C$ 250. Tá pobre que só ele..."

                                    p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                                    p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                    p "Você quer comprar C$ agora?"

                                    menu:
                                        "Sim. Tô com uma graninha sobrando aqui.":


                                            p rindo "Que bom!"

                                            call comprar_cash

                                            p "Se pagar por PIX, não esqueça de mandar o comprovante. Se pagou pelo Mercado Pago não precisa."

                                            p "Pode demorar até 24 horas para seus créditos caírem. Se demorar mais que isso, envie um e-mail para contato@geiko.net."

                                            p "Centenas de pessoas compram nos nossos games todo mês, então pode ficar tranquilo. Qualquer problema, vamos te ajudar."

                                            p "Bom jogo!"
                                        "Sem chance.":


                                            p "É sua aescolha! Bom jogo!"

                                    hide black with dissolve

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar
                            else:


                                label livro4_evento:

                                    $ proibido_salvar = True
                                    $ show_quick_menu = False

                                scene black with dissolve

                                scene livro4_adulto1 with dissolve

                                "{i}As sacerdotisas de Inanna são proibidas de ter parceiros, se casar e constituir família. Seus corpos pertencem ao templo.{/i}"

                                "{i}Elas devem permanecer em retidão, participando dos rituais sexuais sempre que necessário, sem que tenham seus próprios desejos.{/i}"

                                "{i}Por isso, precisam recusar qualquer pedido de matrimônio ou qualquer outro que as retirem de suas funções. Mas nem todas seguem.{/i}"

                                "{i}Algumas sacerdotisas, inebriadas pela riqueza de reis e outros homens de poder, trocam a vida no templo para se tornarem parceiras.{/i}"

                                "{i}Elas escapavam do templo, ilegalmente, e viviam para atender aos desejos sexuais desses poderosos, deixando seus afazeres como sacerdotisas.{/i}"

                                scene black with dissolve

                                scene livro4_adulto2 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto3 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto4 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto5 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto6 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto7 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto8 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto9 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto10 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto11 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto12 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto13 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto14 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto15 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto16 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto17 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto18 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto19 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto20 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto21 with dissolve

                                pause

                                scene black with dissolve

                                scene livro4_adulto22 with dissolve

                                pause

                                scene black with dissolve

                                scene biblioteca mc_lendo with Dissolve(1.0)

                                "{i}Veja sacerdotisas ainda mais quentes no nosso próximo Volume.{/i}"

                                "Elas abandonavam a deusa pra terem uma vida de rainhas sendo concubinas dos reis da Suméria."

                                "Será que valia a pena ter essa vida?"

                                "Com certeza eu ia adorar ter uma sacerdotisa dessa como minha parceira..."

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar

                        "Sacerdotisas Hereges que se Entregaram ao Prazer - Volume 5 (+18)" if livros_liberados >= 4:

                            if livros_liberados < 5:

                                $ proibido_salvar = True
                                $ show_quick_menu = False

                                "Este também custa C$ 250. Deve ser tão bom quanto o anterior!"

                                python:
                                    if renpy.android:
                                        livros_liberados_db = PythonSDLActivity.pegaLivros()

                                "{i}Este volume contém mais de 20 fotos exclusivas de sacerdotisas de Inanna nuas.{/i}"

                                "{i}Estas fotos não são recomendadas para menores de 18 anos. Contamos com a colaboração de todos.{/i}"

                                if livros_liberados < livros_liberados_db:

                                    "{b}Você já liberou os livros [livros_liberados_db] vezes. Mas neste gameplay você liberou [livro_liberados] livros.{/b}"

                                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, o próximo livro será liberado automaticamente.{/b}"

                                    $ livros_liberados += 1

                                    jump livro5_evento

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                "Certo. Parece que vai custar C$ 250."

                                "Eu tô com {b}R$ [cash]{/b}."

                                $ renpy.choice_for_skipping()

                                if cash >= 250:

                                    "Eu tenho dinheiro suficiente."

                                    menu:

                                        "Comprar acesso ao Volume 5 por {b}C$ 250{/b}" if livros_liberados < 5:

                                            python:
                                                if renpy.android:
                                                    livros_liberados_db = PythonSDLActivity.pegaLivros()
                                                    
                                                    if livros_liberados == livros_liberados_db:
                                                        PythonSDLActivity.addLivros()
                                                        
                                                        livros_liberados += 1

                                                renpy.block_rollback()

                                            "{b}Você usou C$ 250 para liberar este volume{/b}"

                                            if not renpy.variant("android"):

                                                $ livros_liberados += 1

                                            jump livro5_evento
                                        "Melhor deixar pra outra hora":


                                            "Nem tô afim agora. Melhor deixar pra outra hora."

                                            jump biblioteca_2andar
                                else:


                                    show black with Dissolve(1.0)

                                    p lecionando "Ixi. O [mc] não tem C$ 250. Tá pobre que só ele..."

                                    p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                                    p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                    p "Você quer comprar C$ agora?"

                                    menu:
                                        "Sim. Tô com uma graninha sobrando aqui.":


                                            p rindo "Que bom!"

                                            call comprar_cash

                                            p "Se pagar por PIX, não esqueça de mandar o comprovante. Se pagou pelo Mercado Pago não precisa."

                                            p "Pode demorar até 24 horas para seus créditos caírem. Se demorar mais que isso, envie um e-mail para contato@geiko.net."

                                            p "Centenas de pessoas compram nos nossos games todo mês, então pode ficar tranquilo. Qualquer problema, vamos te ajudar."

                                            p "Bom jogo!"
                                        "Sem chance.":


                                            p "É sua aescolha! Bom jogo!"

                                    hide black with dissolve

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar
                            else:


                                label livro5_evento:

                                    $ proibido_salvar = True
                                    $ show_quick_menu = False

                                scene black with dissolve

                                scene livro5_adulto1 with dissolve

                                "{i}As sacerdotisas de Inanna são proibidas de ter parceiros, se casar e constituir família. Seus corpos pertencem ao templo.{/i}"

                                "{i}Elas devem permanecer em retidão, participando dos rituais sexuais, sem que tenham seus próprios desejos e amores.{/i}"

                                "{i}Algumas delas, no entanto, ignoram seu destino e se vendem ao prazer efêmero, transando entre elas mesmas no Templo.{/i}"

                                "{i}Essas sacerdotisas se apaixonam às escondidas e, após a prática do sexo por seu próprio prazer, deveriam ser expulsas.{/i}"

                                "{i}Seus corpos foram estragados pela prática do sexo carnal, e seus rituais não farão mais efeito.{/i}"

                                "{i}Alguns dizem que calamidades foram trazidas à Suméria devido ao erro dessas mulheres consumidas pelo desejo impuro.{/i}"

                                scene black with dissolve

                                scene livro5_adulto2 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto3 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto4 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto5 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto6 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto7 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto8 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto9 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto10 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto11 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto12 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto13 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto14 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto15 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto16 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto17 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto18 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto19 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto20 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto21 with dissolve

                                pause

                                scene black with dissolve

                                scene livro5_adulto22 with dissolve

                                pause

                                scene black with dissolve

                                scene biblioteca mc_lendo with Dissolve(1.0)

                                "{i}Veja sacerdotisas ainda mais quentes no nosso próximo Volume.{/i}"

                                "Essas sacerdotisas se entregaram pro prazer do sexo entre elas mesmas."

                                "Imagina viver em um lugar cheio de mulheres nuas perfeitas... aposto que eu não aguentava também."

                                "O que será que acontecia quando essas mulheres que fizeram coisa errada faziam os rituais? Vixi..."

                                $ proibido_salvar = False
                                $ show_quick_menu = True

                                jump biblioteca_2andar

                        "????? (+18)" if livros_liberados < 6:

                            if livros_liberados < 5:

                                "{b}Compre acesso ao livro anterior para poder ler este volume do livro{/b}"
                            else:


                                "{b}Os livros continuam nas próximas atualizações de CH! Se você gostou, fique de olho!{/b}"
                        "Não quero nada agora":


                            label livros_sair:

                                $ proibido_salvar = False
                                $ show_quick_menu = True
                "As Mikos do Utagaki (+18)":


                    "{i}Este livro tem mais de 100 fotos exclusivas de sacerdotisas que participaram do Utagaki, no Japão.{/i}"

                    "{i}As fotos foram geradas por meio de informações obtidas em descobertas arqueológicas desde o Século VIII.{/i}"

                    menu:

                        "????? (+18)" if livros_liberados < 5:

                            "{b}Compre todos os volumes do livro Sacerdotisas de Inanna para liberar os volumes deste livro{/b}"
                "Não ler nada no momento":


                    pass
        "Não ler nada no momento":


            pass

    $ proibido_salvar = False
    $ show_quick_menu = True

    "Tô sem saco pra ler isso agora."

    jump biblioteca_2andar

label cidade_academia:

    call pre_tela from _call_pre_tela_32

    if area == "cidade":

        if tempo < 3:

            if academia:

                "Acho que tô afim de dar aquela treinada."

            elif maria_evento == 8 and not academia:

                "Então aqui é a academia da [ma]... quem diria..."

                "Tenho que falar com ela e virar um membro pra começar a usar aqui."

                scene cidade academia2 with Dissolve(1.0)

                jump maria_academia_evento
            else:


                "Academia? Hahahaha!"

                "Até parece que eu vou gastar meu tempo pra bombar."

                "Eu tenho sorte de só poder comer pizza e lanche e não engordar, não tem porque perder tempo malhando. A vida é curta demais."

                "Pensando bem... se tivesse alguém interessante nessa academia... se pá até valeria à pena. Ou quem sabe pra conseguir uma pauta."

                "Bom... se alguma coisa mudar posso me inscrever, mas por enquanto eu quero sobreviver na capital! Aaahhh!"

                show screen cidade_tela
                with dissolve

                pause
        else:


            "A academia não é 24 horas. Ela já tá fechada essa hora."

            show screen cidade_tela
            with dissolve

            pause

    $ proibido_salvar = False
    $ show_quick_menu = True

    $ area = "academia"
    $ mapa = "academia1"

    scene academia academia1 with Dissolve(1.0)

    call pos_tela from _call_pos_tela_33

    pause

label academia_treino:

    call pre_tela from _call_pre_tela_33

    "Vou aproveitar que a [ma] não tá aqui agora pra dar aquela malhada."

    $ proibido_salvar = True
    $ show_quick_menu = False

    call checa_logado from _call_checa_logado_7

    call anuncio from _call_anuncio_8

    "O foda é que ela falou pra eu não pegar pesado demais."

    $ renpy.choice_for_skipping()

    call checa_tempo from _call_checa_tempo_9

    python:
        if renpy.android:
            mttempo = PythonSDLActivity.checkMTtempoNext()

    if not mttempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        "Melhor eu esperar um pouco mais antes de treinar."

        show black with Dissolve(1.0)

        p rindo "O [mc] pode malhar na academia uma vez a cada 1 hora do mundo real."

        label academia_coins:

            p "Use o app Relógio no celular do [mc] para ver quando o próximo treino estará disponível."

            p "Lembrando que os treinos com a [ma] e sozinho usam o mesmo horário."

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

                    mc "E daí que eu tô cansado?! Vale à pena pra impressionar a [ma]!"

                    jump academia_treino_pronto
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

                    call comprar_coins from _call_comprar_coins_5

                    p "Se você comprou, agora pode avançar o tempo usando Celebrity Coins."

                    hide black with dissolve

                    jump academia_coins
                "A vida é dura. Tô sem grana pra isso agora.":


                    p rindo "Não tem problema."

                    p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais."

                    jump cidade_academia
    else:


        label academia_treino_pronto:

            $ proibido_salvar = True
            $ show_quick_menu = False

            "Bora lá!"

        python:
            if renpy.android:
                PythonSDLActivity.setMTtempoNext()
                
                renpy.block_rollback()

    "Qual treino eu faço hoje?"

    menu:
        "Rotina leve":


            $ menos_folego = 4
            $ esteira_tempo = 30
            $ fisico_recompensa = 5

            "Vou pra algo mais tranquilo hoje que é garantido que eu consigo."

            scene mc_academia_treino1 with Dissolve(1.0)
        "Rotina completa":


            $ menos_folego = 40
            $ esteira_tempo = 40
            $ fisico_recompensa = 10

            "Hoje é dia de treino de gente grande."

            scene mc_academia_treino1 with Dissolve(1.0)
        "Rotina monstrão":


            $ menos_folego = 80
            $ esteira_tempo = 50
            $ fisico_recompensa = 20

            "É hoje que eu saio da jaula! BIRRRLLL!"

            scene mc_academia_treino3 with Dissolve(1.0)

    "1... 2... 3..."

    "Vamo!"

    $ treinando_sozinho = True
    $ esteira_velo = 0.5
    $ folego = 150
    $ mc_folego = mc_fisico // 10

    show screen academia_esteira
    show screen esteira_tempo
    show screen esteira_reduz_folego
    call screen esteira_base

    pause

label academia_treino_finalizar:

    $ treinando_sozinho = False

    if folego <= 0 or folego >= 300:

        "AAAAHHH!"

        "Não!"

        scene academia_mc_caido with vpunch

        pause

        mc "Ai... Que merda..."

        "Acho que foi demais pra mim."

        "Melhor eu fazer um treino mais tranquilo antes de puxar assim. Ou vou ter que me esforçar mais."

        "Afe, eu fico todo destruído quando isso acontece..."

        "Sorte que não tem ninguém olhando."
    else:


        pause

        "Massa!"

        "Acho que tá bom por agora."

        scene black with dissolve

        scene mc_academia_sucesso with Dissolve(1.0)

        play sound "extra/carta.mp3"

        "{b}O físico do [mc] melhorou [fisico_recompensa] pontos{/b}"

        "Boa! Hoje o treino foi muito bom."

        "Se eu continuar assim eu vou fazer bonito pra [ma]."

        "Agora deixa eu sair daqui que tô quase caindo."

    $ tempo += 1

    jump cidade_academia

screen cidade_tela():
    tag cidade

    modal True
    zorder 99
    predict False

    if area == "ilha":

        if mapa == "praia1":

            add "images/mapa/praia1_hover.png":
                xalign 0.03
                yalign 0.97

            imagebutton auto "images/mapa/praia_quiosque_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("praia2")

            imagebutton auto "images/mapa/praia_gazebo_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("praia3")

            if tempo < 3:

                imagebutton auto "images/mapa/praia_%s.png":
                    xalign 0.3
                    yalign 0.97
                    action Jump("praia4")



            imagebutton auto "images/mapa/ilha_%s.png":
                xalign 0.03
                yalign 0.80
                action Jump("praia_voltar_ilha")

            imagebutton auto "images/mapa/praia_especial_%s.png":
                xalign 0.12
                yalign 0.80
                action Jump("praia_especial")

        elif mapa == "praia2":

            imagebutton auto "images/mapa/praia1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("praia1")

            add "images/mapa/praia_quiosque_hover.png":
                xalign 0.12
                yalign 0.97

            imagebutton auto "images/mapa/praia_gazebo_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("praia3")

            if tempo < 3:

                imagebutton auto "images/mapa/praia_%s.png":
                    xalign 0.3
                    yalign 0.97
                    action Jump("praia4")

        elif mapa == "praia3":

            imagebutton auto "images/mapa/praia1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("praia1")

            imagebutton auto "images/mapa/praia_quiosque_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("praia2")

            add "images/mapa/praia_gazebo_hover.png":
                xalign 0.21
                yalign 0.97

            if tempo < 3:

                imagebutton auto "images/mapa/praia_%s.png":
                    xalign 0.3
                    yalign 0.97
                    action Jump("praia4")

        elif mapa == "praia4":

            imagebutton auto "images/mapa/praia1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("praia1")

            imagebutton auto "images/mapa/praia_quiosque_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("praia2")

            imagebutton auto "images/mapa/praia_gazebo_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("praia3")

            add "images/mapa/praia_hover.png":
                xalign 0.3
                yalign 0.97



            imagebutton auto "images/mapa/praia_andando_%s.png":
                xalign 0.03
                yalign 0.80
                action Jump("praia4_passear")

    elif area == "cidade":

        if carro:

            imagebutton idle "images/botao_carro.webp":
                xalign 0.99
                yalign 0.8
                action Call("voltar_carro")

        if mapa == "cidade1":

            add "images/mapa/cidade1_hover.webp":
                xalign 0.03
                yalign 0.97

            imagebutton auto "images/mapa/cidade2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("cidade2")

            imagebutton auto "images/mapa/cidade3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("cidade3")

            imagebutton auto "images/mapa/cidade4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("cidade4")



            imagebutton auto "images/mapa/ilha_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("ilha_voltar_bus")

            imagebutton auto "images/mapa/boutique_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("boutique")

            if submapa == "fliperama":

                add "images/mapa/fliperama_hover.png":
                    xalign 0.21
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/fliperama_%s.png":
                    xalign 0.21
                    yalign 0.8
                    action Jump("cidade_fliperama")

        if mapa == "cidade2":

            imagebutton auto "images/mapa/cidade1_%s.webp":
                xalign 0.03
                yalign 0.97
                action Jump("cidade1")

            add "images/mapa/cidade2_hover.png":
                xalign 0.12
                yalign 0.97

            imagebutton auto "images/mapa/cidade3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("cidade3")

            imagebutton auto "images/mapa/cidade4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("cidade4")



            if submapa == "museu":

                add "images/mapa/museu_hover.png":
                    xalign 0.03
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/museu_%s.png":
                    xalign 0.03
                    yalign 0.8
                    action Jump("cidade_museu")

            if submapa == "cinema":

                add "images/mapa/cinema_hover.png":
                    xalign 0.12
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/cinema_%s.png":
                    xalign 0.12
                    yalign 0.8
                    action Jump("cidade_cinema")

            if submapa == "universidade":

                add "images/mapa/universidade_hover.png":
                    xalign 0.21
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/universidade_%s.png":
                    xalign 0.21
                    yalign 0.8
                    action Jump("cidade_universidade")



            if submapa == "museu":

                imagebutton auto "images/mapa/museu2_%s.png":
                    xalign 0.03
                    yalign 0.63
                    action Jump("museu1")

            if submapa == "universidade":

                imagebutton auto "images/mapa/uni1_%s.png":
                    xalign 0.03
                    yalign 0.63
                    action Jump("uni1")

        if mapa == "cidade3":

            imagebutton auto "images/mapa/cidade1_%s.webp":
                xalign 0.03
                yalign 0.97
                action Jump("cidade1")

            imagebutton auto "images/mapa/cidade2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("cidade2")

            add "images/mapa/cidade3_hover.png":
                xalign 0.21
                yalign 0.97

            imagebutton auto "images/mapa/cidade4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("cidade4")



            if submapa == "prefeitura":

                add "images/mapa/prefeitura_hover.png":
                    xalign 0.03
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/prefeitura_%s.png":
                    xalign 0.03
                    yalign 0.8
                    action Jump("cidade_prefeitura")

            if submapa == "tkf":

                add "images/mapa/tkf_hover.png":
                    xalign 0.12
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/tkf_%s.png":
                    xalign 0.12
                    yalign 0.8
                    action Jump("cidade_tkf")

            if submapa == "faux":

                add "images/mapa/faux_hover.png":
                    xalign 0.21
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/faux_%s.png":
                    xalign 0.21
                    yalign 0.8
                    action Jump("cidade_faux")



            if submapa == "tkf":

                imagebutton auto "images/mapa/tkf1_%s.png":
                    xalign 0.03
                    yalign 0.63
                    action Jump("tkf_entrada")

        if mapa == "cidade4":

            imagebutton auto "images/mapa/cidade1_%s.webp":
                xalign 0.03
                yalign 0.97
                action Jump("cidade1")

            imagebutton auto "images/mapa/cidade2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("cidade2")

            imagebutton auto "images/mapa/cidade3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("cidade3")

            add "images/mapa/cidade4_hover.png":
                xalign 0.3
                yalign 0.97



            if submapa == "china":

                add "images/mapa/cidade_china_hover.png":
                    xalign 0.03
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/cidade_china_%s.png":
                    xalign 0.03
                    yalign 0.8
                    action Jump("cidade_china")

            if submapa == "pizzaria":

                add "images/mapa/pizzaria_hover.png":
                    xalign 0.12
                    yalign 0.8

            else:

                imagebutton auto "images/mapa/pizzaria_%s.png":
                    xalign 0.12
                    yalign 0.8
                    action Jump("cidade_pizzaria")

            imagebutton auto "images/mapa/academia_%s.png":
                xalign 0.21
                yalign 0.8
                action Jump("cidade_academia")



            if submapa == "pizzaria":

                if submapa2 == "pizzaria_out":

                    add "images/mapa/pizzaria_out_hover.png":
                        xalign 0.03
                        yalign 0.63

                else:

                    imagebutton auto "images/mapa/pizzaria_out_%s.png":
                        xalign 0.03
                        yalign 0.63
                        action Jump("cidade_pizzaria_out")

                if submapa2 == "pizzaria_out" or submapa2 == "pizzaria_in":

                    if submapa2 == "pizzaria_in":

                        add "images/mapa/pizzaria_in_hover.png":
                            xalign 0.12
                            yalign 0.63

                    else:

                        imagebutton auto "images/mapa/pizzaria_in_%s.png":
                            xalign 0.12
                            yalign 0.63
                            action Jump("cidade_pizzaria_in")

    elif area == "universidade":

        if mapa == "uni1":

            add "images/mapa/uni1_hover.png":
                xalign 0.03
                yalign 0.97

            imagebutton auto "images/mapa/uni2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("uni2")

            imagebutton auto "images/mapa/uni3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("uni3")



            imagebutton auto "images/mapa/universidade_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("cidade_universidade")

        if mapa == "uni2":

            imagebutton auto "images/mapa/uni1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("uni1")

            add "images/mapa/uni2_hover.png":
                xalign 0.12
                yalign 0.97

            imagebutton auto "images/mapa/uni3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("uni3")

        if mapa == "uni3":

            imagebutton auto "images/mapa/uni1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("uni1")

            imagebutton auto "images/mapa/uni2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("uni2")

            add "images/mapa/uni3_hover.png":
                xalign 0.21
                yalign 0.97

    elif area == "museu":

        if mapa == "museu1":

            add "images/mapa/museu1_hover.png":
                xalign 0.03
                yalign 0.97

            imagebutton auto "images/mapa/museu2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("museu2")

            imagebutton auto "images/mapa/museu3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("museu3")

            imagebutton auto "images/mapa/museu4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("museu4")



            imagebutton auto "images/mapa/biblioteca_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("biblioteca_1andar")

            imagebutton auto "images/mapa/museu_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("cidade_museu")

        elif mapa == "museu2":

            imagebutton auto "images/mapa/museu1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("museu1")

            add "images/mapa/museu2_hover.png":
                xalign 0.12
                yalign 0.97

            imagebutton auto "images/mapa/museu3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("museu3")

            imagebutton auto "images/mapa/museu4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("museu4")



            imagebutton auto "images/mapa/biblioteca_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("biblioteca_1andar")

            imagebutton auto "images/mapa/museu_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("cidade_museu")

        elif mapa == "museu3":

            imagebutton auto "images/mapa/museu1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("museu1")

            imagebutton auto "images/mapa/museu2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("museu2")

            add "images/mapa/museu3_hover.png":
                xalign 0.21
                yalign 0.97

            imagebutton auto "images/mapa/museu4_%s.png":
                xalign 0.3
                yalign 0.97
                action Jump("museu4")



            imagebutton auto "images/mapa/biblioteca_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("biblioteca_1andar")

            imagebutton auto "images/mapa/museu_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("cidade_museu")

        elif mapa == "museu4":

            imagebutton auto "images/mapa/museu1_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("museu1")

            imagebutton auto "images/mapa/museu2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("museu2")

            imagebutton auto "images/mapa/museu3_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("museu3")

            add "images/mapa/museu4_hover.png":
                xalign 0.3
                yalign 0.97



            imagebutton auto "images/mapa/biblioteca_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("biblioteca_1andar")

            imagebutton auto "images/mapa/museu_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("cidade_museu")

        elif mapa == "biblioteca1":

            add "images/mapa/biblioteca_hover.png":
                xalign 0.03
                yalign 0.97

            imagebutton auto "images/mapa/biblioteca2_%s.png":
                xalign 0.12
                yalign 0.97
                action Jump("biblioteca_2andar")

            imagebutton auto "images/mapa/livros_%s.png":
                xalign 0.21
                yalign 0.97
                action Jump("biblioteca")



            imagebutton auto "images/mapa/museu4_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("museu4")

            imagebutton auto "images/mapa/museu_%s.png":
                xalign 0.12
                yalign 0.8
                action Jump("cidade_museu")

        elif mapa == "biblioteca2":

            imagebutton auto "images/mapa/biblioteca_%s.png":
                xalign 0.03
                yalign 0.97
                action Jump("biblioteca_1andar")

            add "images/mapa/biblioteca2_hover.png":
                xalign 0.12
                yalign 0.97



            imagebutton auto "images/mapa/livros_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("biblioteca")

    elif area == "academia":

        imagebutton auto "images/mapa/cidade1_%s.webp":
            xalign 0.03
            yalign 0.97
            action Jump("cidade4")

        if tempo == 1:

            imagebutton auto "images/mapa/academia_maria_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("academia_maria")

        elif tempo == 2:

            imagebutton auto "images/mapa/academia_treino_%s.png":
                xalign 0.03
                yalign 0.8
                action Jump("academia_treino")

    elif area == "academia_maria":

        imagebutton auto "images/mapa/academia_%s.png":
            xalign 0.03
            yalign 0.97
            action Jump("academia_maria_cancelar")

        imagebutton auto "images/mapa/treino_maria_%s.png":
            xalign 0.12
            yalign 0.97
            action Jump("maria_academia_treino")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
