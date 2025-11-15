define demonio = Character("Garota Demônio", color="#ff66cc")

image bg demon_pc = "intro-comeco/garota-demonio/fundo-gamer-com-pc.png"
image demonio neutral = "intro-comeco/garota-demonio/pose-normal-neutra.png"
image demonio smile = "intro-comeco/garota-demonio/pose-joinha-sorrindo-alegre.png"
image demonio talk = "intro-comeco/garota-demonio/pose-bracos-abertos-conversando.png"
image demonio serious = "intro-comeco/garota-demonio/pose-apontando-ded-com-raiva-falando.png"


label intro_codex_notice:

    scene bg demon_pc with dissolve
    show demonio neutral at center

    demonio "Ei, jogador! Aqui é a garota demônio enviada pelo pessoal do canal Team HP Infinit pra garantir que você está na versão certa."
    show demonio talk
    demonio "Confirmado: esta build é a {b}0.93{/b}, recheada com mais de {b}130 animações novas{/b} e os ajustes de estabilidade que o Codex cuidou pra gente."
    show demonio smile
    demonio "Os cheats liberam conteúdo pra testar rota e tirar o peso das antigas travas premium, mas lembra: eles existem pra facilitar QA e balanceamento."
    show demonio serious
    demonio "Se você abusar dos cheats de desenvolvimento pode corromper saves ou quebrar progressão. Use por sua conta e risco e sempre faça backup antes!"
    show demonio talk
    demonio "Divirta-se, credita o Codex quando espalhar a notícia e, se der ruim, não diga que eu não avisei. Agora sim, bora voltar pra história!"

    hide demonio talk
    scene black with dissolve

    return


label start:

    play sound "extra/start.mp3"

    if not codex_notice_done:
        $ codex_notice_done = True
        call intro_codex_notice


    call priscila_inicio from _call_priscila_inicio

    if persistent.demitido:

        scene black with dissolve

        p "Huhu... é bom saber que você não desistiu."

        p "Boa sorte no seu novo game. E cuidado para não ser demitido de novo."

        p "Se precisar, dê uma olhada no Youtube ou nos nossos grupos no WhatsApp e Telegram e eles vão te ajudar a encontrar as pautas."

        p "Boa sorte!"





    scene mc acorda_fadolandia with Dissolve(3.0)

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("inicia_jogo","pixie","personagem")

    play sound "audio/som_4_fadolandia.mp3"

    "Pera... onde que eu tô?"

    "Casa de madeira? Floresta?"

    "Ai minha cabeça..."

    "A última coisa que eu lembro é de tá em casa vendo vídeo no Youtube... Como eu vim parar aqui?"

    "?" "Oi oi, bonitinho!"

    mcantes "Quem disse..."

    scene pixie primeira_vez with vpunch

    pause

    "?" "Oi?"

    mcantes surpreso "AH!?"

    mcantes angustiado "AH! O que tá acontecendo?! O que é você?!"

    "?" "Calma, bebê. Tá tudo legal?"

    mcantes preocupado "Não tá nada legal! Não tô me lembrando de nada! E o que é você?!"

    p "Teehee! Meu nome é Pixie. Bem-vindo à Vila das Fadas!"

    mcantes zerado "Vila das Fadas? Isso é ridículo..."



    p "Como assim ridículo? Não está vendo a floresta mágica? Não está vendo a fada mais gostosa do mundo?"

    mc preocupado "Como?"

    p "Espera. Eu vou te ajudar a levantar."

    scene black with dissolve

    scene ani08 with Dissolve(1.0)

    pause



    p "Melhorou?"



























































    mc concentrando "Acho que sim... Só que ainda não tô entendendo o que tá acontecendo."



    p "É normal vocês seres humanos se sentirem meio confusos quando vêm parar aqui. Mas você é um rapaz de sorte porque..."

    "..."



    p "Ei! Você está ouvindo o que eu estou falando?"

    p "Ou meu decote está chamando mais atenção que meus olhos?"

    menu:
        "Cla-claro que não! Só estou confuso com a situação...":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pixie1_decote_nao","inicio","pixie")

            mcantes triste "Cla-cla-claro que não! Só estou confuso com a situação..."

            $ pixie_amizade += 1



            p "Tehee! Desculpa, então. Isso é normal... Eu vou te ajudar a se lembrar de tudo."
        "Não.... posso negar.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pixie1_decote_sim","inicio","pixie")

            mcantes charmoso "Opa! Perdão... mas não consegui evitar."

            $ pixie_seducao += 1



            p "Tehee! Vou considerar como um elogio por hora. Mas não ache que ser um tarado vai funcionar sempre."
        "Claro! Com essa roupa é como se você tivesse me convidando.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pixie1_decote_cuzao","inicio","pixie")

            mcantes tarado "Claro! Com essa roupa é como se você tivesse me convidando."




            p "Você é um cuzão, sabia?! Isso não é coisa que se diga para uma garota."


            mcantes desculpa "Ok, desculpe..."



            p "Eu prefiro as coisas diretas, só que a maioria das garotas do seu mundo não gostam de caras que vão com muita sede ao pote."

            p "Você não quer parecer um cachorro no cio."

            mc envergonhado "Claro que não."

            p "Para você fazer o que eu tenho planejado, você tem que ser foda na conquista, entendeu?"

            mc normal "Ok. Pode deixar."

    mcantes triste "Mas eu não consigo me lembrar de nada."

    p "Já falei que isso é normal. Vamos começar pelo começo."

    label escolhe_nome:

        p "Você pode me falar seu nome?"

    menu:
        "Acho que sim...":


            jump nome_sim
        "Não quero pensar nisso...":


            jump nome_nao

    label nome_sim:



        p "Que bom! Isso mostra que você já está melhorando."

        p "Qual é seu nome e sobrenome então?"

        $ mcpnome = "Gustavo"
        $ mcsnome = "Rodrigues"
        call screen text_input_screen

        call screen confirmar_nome

        if mcpnome and mcsnome:

            mc normal "Eu me lembro! Meu nome é [mcpnome]. E meu sobrenome é [mcsnome]..."

            p "Está vendo? Eu falei que com o tempo você ia se sentir melhor."

            mc "É verdade. Obrigado."

        elif mcpnome and not mcsnome:

            $ mcsnome = "Rodrigues"

            mc normal "Eu lembro que meu nome é [mcpnome], mas..."

            p "Seu sobrenome é [mcsnome]! Estou vendo aqui na sua mente..."

            mc desconfiado "Acho que você tem razão... Pensando bem, acho que era [mcsnome] mesmo. Obrigado."

        elif mcsnome and not mcpnome:

            $ mcpnome = "Gustavo"

            mc triste "Eu lembro só que meu sobrenome é [mcsnome]... Mas o mais fácil, meu nome, não..."

            p "Seu nome é [mcpnome]! Estou vendo aqui na sua mente..."

            mc desconfiado "Acho que você tem razão... Pensando bem, acho que era [mcpnome] mesmo. Obrigado."
        else:


            mc desculpa "Não tô conseguindo me lembrar..."

            jump nome_nao










































        jump pcena_continua

    label nome_nao:



        python:
            mcpnome = "Gustavo"
            mcsnome = "Rodrigues"

        p "Deixa que eu te ajudo."

        p "As fadas conseguem ler o pensamento dos humanos, pensamentos que nem vocês mais lembram que existem."

        p "Por isso posso descobrir seu nome rapidinho. Só um segundo."

        "..."



        p "Você se chama Gustavo Rodrigues. É um nome bonito, igual você..."

        menu:
            "Obrigado pela ajuda.":


                mc normal "Valeu."
            "Valeu. Você também é bonita.":


                mc charmoso "Obrigado, você também não é nada mal."

        mc normal "Mas você tem razão... Eu acho que meu nome é [mcc]. Estou me lembrando do meu apartamento também..."

        p "Está vendo? Eu falei que as coisas iriam se ajeitar."

        jump pcena_continua

    label pcena_continua:



    p "Mas eu não estou aqui para isso... ou melhor... VOCÊ não está aqui para isso."

    mc preocupado "Não estou? Você sabe como eu vim parar aqui?"

    p "Obviamente. Eu te trouxe para cá."

    mc surpreso "O quê?!"

    p "Sua vida vai dar uma virada de 180 graus e você precisa entender uma coisa antes."

    mc desconfiado "... Ok..."

    p "O importante é que você se lembre que suas escolhas têm significado nesta vida."





    p "Você vai {b}conhecer muitas garotas e garotos{/b} e se você vai ter um {b}romance duradouro{/b} ou {b}sexo casual{/b} depende de você."

    p "Você também pode ser apenas um {b}amigo{/b} ou ignorar certos personagens completamente."



    p "Pensando agora, qual você acha que é seu principal objetivo?"

    menu:
        "Viver um romance com uma pessoa especial.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("objetivo_romance","objetivo","fada")

            mc charmoso "Conhecer a pessoa certa e viver uma grande história de amor."



            p "Eca. Amor. Eu sou muito mais do rala e rola."

            p "Mas você poderá encontrar a pessoa certa para você e viver uma história de amor digna de cinema se é isso que você quer."

            p "Existem várias garotas e garotos para você conhecer e um deles pode ser seu {b}grande amor!{/b}"
        "Transar com o máximo de pessoas que eu puder.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("objetivo_sexo","objetivo","fada")

            mc safado "Eu quero poder levar quem quiser pra cama sem me preocupar muito com sentimentos."



            p "Você é dos meus. Eu sinto que a gente vai se dar muito bem."

            mc tarado "Que bom..."

            p "No seu mundo existem diversas garotas e garotos te esperando. Mas comer esse povo não vai ser tão fácil."

            p "Primeiro de tudo você precisa conquistá-los, sendo um cara bacana e charmoso. Ninguém vai dar pra você só porque você quer."
        "Encontrar bons amigos para compartilhar a vida.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("objetivo_amizade","objetivo","fada")

            mc normal "Eu quero viver um tempo massa com amigos e amigas de verdade."

            p "Isso parece realmente tentador... Mas a amizade só traz desgraça e infelicidade..."

            mc zerado "Pelo jeito alguém aqui tem problemas com amigos..."



            p "Calado!"

            p "Mesmo te alertando contra, será possível você ser apenas amigo das pessoas que você quiser."

            p "Você também pode começar como amigo e se encontrar alguém especial, aprofundar sua relação ou só levar ela pra cama mesmo."

    scene black with dissolve

    scene fadolandia geral_bot with Dissolve(1.0)

    show pixie animada with dissolve

    p "Resumindo, é você quem vai escolher como sua história vai acontecer e acabar."

    p "Não existe certo ou errado, ou melhor e pior caminho."

    p "Existe apenas o seu caminho. O caminho de [mcc]."



    mc zerado "Que lindo..."

    p "Ah! E mais uma coisa!"



    scene mc fado_juramento_anime at diana_direita with Dissolve(2.0)

    p "Você precisa concordar com uma coisa antes de acordar."

    p "De que você é o único responsável pelas suas escolhas."

    p "Este é um momento muito importante, para que depois você não venha culpar os outros pelo resultado."

    menu:
        "Eu concordo":


            mc "Eu concordo."



            p "Perfeito! Era justamente essa resposta que eu esperava de você! ;)"

            mc "Mas essa era a única... Deixa pra lá..."

    p "Só que nem todas suas escolhas serão simples como essa. Algumas vão realmente testar sua autoestima."

    p "Dependendo do que você escolher sua história pode mudar completamente."



    show seta save with dissolve

    p "Por isso, não se esqueça de salvar o game sempre que você estiver em dúvida sobre qual decisão tomar."

    p "Você pode voltar pro ponto que você salvou usando o botão {b}Carregar{/b} ou o {b}Continuar{/b} na tela inicial."

    hide seta with dissolve





















    mc "Não sei se eu entendi o que você acabou de dizer..."







    p "É normal não entender algo quando a fada mais sexy do mundo está bem na sua frente."

    p "Agora pode ir! Não vai ser fácil, mas tenha confiança em você!"

    p "{cps=15}Quem sabe um dia a gente pode se ver de novo... Xau xau!{/cps}{w=1.0}{nw}"

    scene black with Dissolve(2.0)

    $ renpy.save("None-continue", extra_info="None-continue")





    scene mc dormindo_dois with Dissolve(3.0)

    pause

    p rindo "Olha como ele dorme como um anjo..."

    p "Ei! O [mc] não vai se lembrar de nada que aconteceu no mundo dos sonhos."

    p "Depende de {b}você{/b} garantir que ele tenha uma vida feliz. Se ele vai se dar bem no amor e no trabalho depende das suas escolhas."

    p "Ele também pode acabar {b}sozinho{/b} e até {b}morrer{/b} se você não tomar cuidado."

    if not persistent.inicia:

        $ persistent.inicia = True

        p "Para te ajudar, eu vou te dar umas moedinhas especiais. Não vai se assustar."

        menu:
            "Pegar as moedas da Pixie.":


                $ renpy.notify("Links externos desativados nesta edicao.")

                p "Assustou? Prontinho."

    p "Bom jogo!"

    scene apartamento cama with Dissolve(1.0)

    show mc acordando with dissolve

    "Ugh... O que foi isso?"

    "Que dor no corpo. Parece que eu nem dormi..."

    "Só que... tem algo diferente…"

    scene apartamento cama_celular with Dissolve(1.0)



    mc "Mesmo morando em um apartamento de merda, sem namorada e praticamente sem dinheiro eu tô me sentindo muito bem."

    mc "Tô quase com vontade de rir."

    "Não consigo lembrar com o que eu sonhei, mas deve ter sido algo muito bom."

    "É como se eu pudesse fazer o que quiser! Estou pronto pa…"

    scene apartamento cama with Dissolve(1.0)

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    mc "Mas que caramba! Não pode nem esperar eu... "

    show mc cueca_telefone with dissolve

    mc "Alô?"

    "Voz Masculina" "[mc], preciso falar com você assim que chegar na redação. Primeira coisa, ouviu?"

    mc "Ok, chefe."

    "Chefe" "PRIMEIRA COISA!"

    "Smartphone" "tu... tu... tu..."

    "Pau no cu."

    hide mc with dissolve

    mc "Ele nunca me chamou na sala dele desde que comecei a trabalhar lá."

    mc "Certeza que ele vai querer me despedir..."

    mc "Que merda! Só porque eu tinha acordado tão bem hoje!"



    scene mc ap_pensando with Dissolve(2.0)

    "Eu sei que minha situação não tá fácil na redação. Faz, acho, que três meses que eu tô lá e ainda não tive uma matéria publicada na revista."



    mc "Que bosta! Eu só precisava de mais um pouco de tempo."

    "Minha mãe vai encher tanto meu saco se eu perder o emprego que ela arranjou pra mim."

    "Eu nem queria trabalhar com celebridades. Por que é tão difícil trabalhar como jornalista?"

    "Não é hora de avaliar minha profissão. Já é hora de sair."

    mc "Ou eu posso fazer aquele velho me esperar. Não é como se eu tivesse ansioso para falar com ele..."

    "O que vou fazer agora?"

    menu:
        "Tomar banho e ir para o trabalho":


            mc "Não é sendo um cuzão que vou convencer o chefe. Melhor seguir a rotina."

            "..."

            play sound "audio/som_16_chuveiro.mp3"

            scene mc banho with Dissolve(1.0)

            $ renpy.pause(4)

            "..."

            mc "Não vou deixar a ligação dele me abalar! Hoje será um grande dia!"

            mc "Bora sair."

            stop sound
        "Ver o que tem de novo na Netflix":


            "Deixa eu ver o que tem de novo na Netflix."

            scene apartamento tv with Dissolve(1.0)

            "..."

            mc zerado "Não tenho vontade de ver nenhum desses lançamentos..."

            mc zerado "Eles deviam contratar alguém que realmente entende de cinema..."

            mc normal "Bom. Já enrolei o bastante. Vamos lá."
        "Jogar algum game no Xbox":


            mc "Quem toma banho pra ser despedido? Foda-se essa gente."

            "Vou é jogar esse game aqui que comprei esses dias."

            scene mc ap_jogando with Dissolve(1.0)

            "..."

            "Um monte de jogador tendo que se matar até sobrar um só?"

            "E depois ficar repetindo sem nenhuma diferença?"

            "Quem inventou isso é muito burro. Um jogo assim nunca vai fazer sucesso..."

            "Eita. Já enrolei bastante. Hora de ir pro trampo."





    play sound "audio/som_11_cidadedia_1.mp3"

    scene cidade dia with Dissolve(3.0)

    "Graças a esse trabalho eu pude me mudar para a capital do estado. A maior cidade do país."

    "Eu não vivo no centro da cidade, mas em uma ilha paradisíaca, cheia de gente rica e famosa."

    "Nossa revista fica aqui por causa disso. Para termos acesso a essas pessoas."

    "O pagamento não é perfeito, mas paga o aluguel e a comida."

    "Por isso também não quero ser despedido. Sem esse trampo não vou conseguir me manter aqui."

    mc zerado "E voltar pra casa dos meus pais é a última coisa que vou fazer."

    scene fundo_dia with Dissolve(1.0)

    show cidade rua_trabalho with Dissolve(1.0)

    "O prédio onde eu trabalho é este aqui da direita. Fica bem perto da onde eu moro."

    "Não quero perder tudo o que eu conquistei."

    mc angustiado "Preciso falar pro chefe que aceito qualquer negócio que ele quiser. Ele pode me usar como centro de mesa..."

    "..."

    scene trabalho geral with Dissolve(3.0)

    play sound "audio/som_2_redacao.mp3"

    "Entrar na redação é sempre uma merda."

    "Dá pra escutar aquele {i}tec tec tec{/i} das pessoas digitando no computador, parecendo super úteis."

    mc zerado "Devem estar todas no Facebook xeretando a vida alheia."

    "O que no fundo não é algo horrível quando a gente trabalha em uma revista de fofoca sobre famosos. É importante ser xereta."

    scene trabalho mesa with Dissolve(3.0)

    "Minha mesa não tem porra nenhuma..."

    "Assim, não é que eu não seja xereta, mas é que eu ainda não consegui descobrir nada. Não consegui um dado importante sobre qualquer celebridade."



    "Agora o chefe me liga e me chama pra sala dele."

    mc triste "É óbvio que ele vai me despedir…"

    "..."

    "Aliás, ele tá demorando... Melhor ir até lá. Certeza que ele vai colocar a culpa em mim."





    scene trabalho chefe_porta with dissolve

    "A sala do chefe é aquela ali. Fica no fundo da cozinha."

    "Um dia escutei um cara falando que ele escolheu assim pra poder ouvir a gente conversando."

    "Bom, tô aqui. Não sei se estou preparado para o pior. Seja como for..."

    "Voz feminina esganiçada" "{size=15}Já é a terceira vez na semana! Eu não vou tolerar mais isso!{/size}"

    "Que isso?! Tem uma mulher muito puta lá dentro…"

    "Não consigo ver nada porque depois da porta ainda tem um corredor até a sala dele."

    "Chefe" "{size=10}Você ... calma, princesa. Você sabe que ...{/size}"

    "Não consigo ouvir a voz do chefe direito."

    "Princesa(?)" "{size=15}Calma tua bunda!{/size}"

    "Princesa(?)" "{size=15}{i}Cof…{/i}{/size}"

    "Princesa(?)" "{size=15}Quer dizer… Não me peça para... Vocês estão cruzando a linha...{/size}"

    "Chefe" "{size=10}... baixo, por favor...{/size}"

    "..."

    mc serio "Não consigo mais escutar a conversa..."

    menu:
        "Colar a orelha na porta":


            $ orelha_porta = True
            mc desculpa "Foda-se! Não tem ninguém olhando."
        "Permanecer onde está":


            $ orelha_porta = False
            mc normal "Essa conversa não me diz respeito, não vou pagar mico por causa disso."

    if orelha_porta:

        scene trabalho mc_ouvindo with Dissolve(1.0)

        "Outra Mulher" "{size=15}A senhorita Priscila tem razão, senhor.{/size}"

        "Outra Mulher" "{size=15}Sua revista tem o direito de fazer cobertura de pessoas públicas, mas isso não pode trazer prejuízo moral ou físico para minha cliente.{/size}"

        "Priscila? Será que é aquela modelo teen? Impossível…"

        "Impossível que uma revista como a nossa esteja realmente incomodando gente de calibre nacional."

        "Ou será que está?"

        "Caralho... se for ela mesmo vai ser ainda pior ser despedido agora... Que merda!"

        "{i}DUMP DUMP{/i}"

        c "É a primeira e última vez que vou avisar! Na próxima é processo! Velho tarado!"

        mc "AH?!"

        scene priscila mc_trombada with hpunch

        pause

        "{i}TUMP{/i}"

        "[mc] e [c]" "Ai!"

        scene priscila_caida1 with hpunch

        pause

        c "O que é isso?!"

        c "Olha por onde anda!"

        "U-uou! O decote abriu tudo..."

        "Porra, que peitão..."

        "Melhor parar de encarar."

        window hide

        pause

        scene trabalho chefe_porta with Dissolve(1.0)

        c "Você me desajeitou toda..."

        mc envergonhado "D-desculpa..."

        show priscila d_brava with dissolve
    else:


        "..."

        "..."

        "..."

        "Finalmente a porta tá abrindo."

        show priscila d_brava with dissolve

        c "É a primeira e última vez que vou avisar! Na próxima é processo! Velho tarado!"

    c "E quem é esse idiota parado aqui!? Até aqui vocês colocam gente pra me seg..."



    show priscila d_hehe with dissolve

    c "Hmmm... Se bem que um paparazzi como você eu até ia gostar."

    c "Um gato que nem você pode me fotografar quando quiser."

    menu:
        "Quem? Eu?":


            mc envergonhado "Quem? Eu?"

            $ p1_quem = True

            show priscila d_feliz with dissolve

            c "E além de tudo é fofo."

            c "Até outro dia, gatinho."

            c "{i}smack{/i}"
        "Obrigado. Você também é.":


            mc charmoso "Obrigado, você também é linda."

            $ priscila_seducao += 1

            show priscila d_provocando with dissolve

            c "..."

            c "Até outro dia, gato."

            c "{i}smack{/i}"
        "Eu sei.":


            mc tarado "Eu sei."



            c "..."

            c "Até."

    hide priscila with dissolve

    "Quê?!"

    "Era ela! Priscila Fontinelli! A modelo teen! Ela tá na Consigo toda semana!"

    "Gato? Eu?"

    "..."

    b "Ei, [mc]! Tá fazendo o que parado aí, caralho!?"

    b "Traz logo essa bunda branca pra cá!"

    mc zerado "Velho insuportável..."

    b "Você disse alguma coisa?!"

    "..."





    scene trabalho chefe with Dissolve(1.0)

    "É a segunda vez que entro aqui. Essa sala deve ser mais cara que o resto do prédio inteiro."

    show chefe emburrado with dissolve

    b "Você não é burro, [mc]. Sabe que eu te chamei pra te despedir!"

    b "Semana que vem é seu quarto mês aqui e eu ainda não aproveitei uma linha escrita por você!"

    menu:
        "Me desculpe, chefe! Eu faço o que quiser! Não me demita!":


            mc angustiado "Me desculpe, chefe! Eu faço o que quiser! Não me demita!"

            show chefe satisfeito with dissolve

            b "É bom ver que você reconhece sua situação."

            b "Se todos os malditos jornalistas fossem como você, essa revista já estaria no topo!"
        "Eu sei, mas eu ainda não tive tempo para me adaptar.":


            mc triste "Eu sei, mas eu ainda não tive tempo para me adaptar."

            show chefe irritado with dissolve

            b "Adaptar? Adaptar?! Está achando que aqui é o parquinho?! Adaptar o caralho!"

            b "Se você falar mais um absurdo desses eu te coloco para fora pessoalmente!"
        "Foda-se! Não dou a mínima para você e essa revista de merda.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("chefe_p1","gameover","escolha")

            mc bravo "Foda-se! Não dou a mínima para você e essa revista de merda!"

            show chefe irritado with dissolve

            b "Você é maluco, seu merda?! Tá drogado!!?"

            b "Sai da minha frente antes que eu te foda com um cabo de vassoura!"

            jump end_z

    show chefe emburrado with dissolve

    b "Eu tava pronto pra te mandar embora com uma mão na frente e outra atrás."

    b "Só que eu vi o que aconteceu agora."

    b "Graças à Priscila acho que podemos fazer algo sobre seu futuro aqui."

    b "Não quero saber sua opinião sobre isso. Nem ouvir um 'A' sobre ética ou qualquer coisa parecida."

    b "Estamos entendidos?!"

    menu:
        "Sim, senhor.":


            mc normal "Sim, senhor."

            b "Muito bem."

    b "Não sei o que passa na cabeça daquela guria, mas parece que ela foi com a sua cara."

    b "Os paparazzi são vistos como impertinentes, xeretas, inconvenientes e uma série de outras merdas."

    b "Mas somos um mal necessário para a sociedade."

    b "Todos reclamam dos profissionais, mas gostam de saber tudo o que acontece com as celebridades."

    mc normal "Você tem razão, senhor."

    b "Calado."

    mc triste "Sim, senhor."

    show chefe satisfeito with dissolve

    b "As pessoas precisam falar da vida alheia para compensar suas vidinhas medíocres."

    b "Precisamos dar a elas o que elas querem: coisas que elas não sabem sobre os famosos."

    b "Quanto mais podre, obscuro e exclusivo melhor."

    show chefe emburrado with dissolve

    b "Você está ouvindo, [mc]?"

    mc serio "Sim, senhor."

    b "Pois bem. Se a princesa das garotinhas está disposta a se abrir para você, não podemos perder a oportunidade."

    b "Eu tinha decidido que se você não me entregasse algo em sete dias, eu ia te despedir."

    b "E faltam dois dias para completar essa data limite. Entendeu sua situação?"

    b "Quero que você me traga algo sobre ela até depois de amanhã."

    b "Faça o que for preciso. Se torne o melhor amigo dela, o amante, o amor da vida dela, um escravo!"

    b "Você tem dois dias para me trazer alguma coisa que eu possa publicar sobre ela."

    show chefe irritado with dissolve

    b "DOIS DIAS, [mc]!"

    b "E agora saia daqui!"





    scene trabalho chefe_porta with dissolve

    "..."

    "Como eu odeio esse velho. Mas aquela Priscila salvou meu emprego."

    "E ainda me chamou de gato. Isso nunca aconteceu antes..."

    "Eu tenho dois dias para conseguir algo sobre ela."

    "É sua última chance, [mc]. Se você não conseguir, vai viver na casa dos pais pra sempre."

    mc triste "Isso não! Por favor..."

    mc normal "Preciso começar pesquisando sobre ela."

    scene trabalho mesa with Dissolve(1.0)

    "[cc]."

    "Vamos ver o que o site da Consigo tem a dizer sobre ela."

    "..."

    show priscila modelo1 with dissolve

    "Consigo" "[cc] é o fenômeno adolescente do ano! Com seus trajes fofos e seu jeito meigo, tanto garotos como garotas se inspiram na celebridade."

    "Jeito meigo? Não sei onde."

    "Consigo" "... Pesquisa recente indica que, mesmo tendo apenas 19 anos, [c] é reconhecida por mais de 93%% dos adolescentes entre 12 e 16 anos."

    "Consigo" "Nessa faixa etária, ela é mais reconhecida que Jesus Cristo!"

    show priscila modelo2 with dissolve

    "Consigo" "Ela gosta de comer bolo de chocolate e tomar sorvete e seu passatempo preferido é ver filmes de princesas."

    "Consigo" "[c] diz estar procurando o verdadeiro amor e espera encontrar o verdadeiro príncipe encantado que possa dar para ela uma vida de princesa."

    "Consigo" "Será que o príncipe dela está próximo? Com sua beleza e personalidade, temos certeza que a princesa está cheia de pretendentes!"

    scene trabalho mesa with Dissolve(1.0)

    mc zerado "Príncipe encantado? Bolo de chocolate? Que besteira... Por que as pessoas lêem esse tipo de coisa?"

    "..."

    mc angustiado "Droga! Não existe nada aqui que me seja útil."

    "E todo esse tempo pesquisando ainda me deu uma baita dor de cabeça. Vou ter que ir pra casa."

    $ tempo += 1

    scene cidade tarde with dissolve

    "Não posso desperdiçar um dia todo... Só que minha cabeça tá me matando."

    "Minha vista tá embaçada e parece que tem dois quilos de pedra em cima de mim..."

    "Fazia tempo que eu não tinha dor de cabeça. Por que justo hoje?"

    "..."

    scene apartamento tarde with dissolve

    mc normal "Que sono..."

    "Acho que o dia foi estressante demais. Uma noite de descanso vai me recuperar e amanhã vou descobrir algo sobre ela."

    scene apartamento cama with dissolve

    "Tenho que aproveitar que ela me achou atraente. É uma oportunidade de ouro para um paparazzo..."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v0_fim","final","local")

    scene black with dissolve

    $ renpy.save("None-continue", extra_info="None-continue")

    "{i}zzzzzzz{/i}"





    $ tempo += 1

    "..."

    scene mc acorda_fadolandia with Dissolve(3.0)

    mc "O quê?! O que é isso?"

    mc "Não... espera..."

    scene fadolandia geral_bot with Dissolve(2.0)

    "De novo esse lugar? Eu já estive aqui da outra vez..."

    mc serio "..."

    "Mas dessa vez aquela fada não está aqui."

    mc serio "Ela disse que me trouxe aqui da primeira vez. Será que foi ela de novo?"

    "Não sei o que fazer agora..."

    menu:
        "Procurar a fada ou a saída":


            $ procurar_fada1 = True
            "Não consigo só ficar aqui esperando. Tenho que encontrar ela ou uma forma de sair daqui."
        "Permanecer no local e esperar ajuda":


            $ procurar_fada1 = False
            "O que adianta sair andando sem rumo? Talvez a fada esteja chegando."

    if procurar_fada1:

        scene fadolandia geral with Dissolve(1.0)

        "Consigo ver aquela casa lá em cima..."

        "Esse lugar é realmente estranho. Será que é possível que isso tudo seja real?"

        "Provavelmente é só um sonho. Mas então por que não acordo?"

        "Se isso realmente é um sonho, é o mais estranho que eu já tive."

        "Bom... deixa eu subir até lá..."

        "..."

        scene fadolandia casa with Dissolve(1.0)

        "..."

        mc triste "Que caminhada..."

        "Cheguei até o topo da árvore. Desde a primeira vez, eu fiquei interessado em ver qual é a dessa casa."

        "Uma casa de madeira... Sobre uma árvore... A casa perfeita para uma..."

        p "Hmm---hm-hmmmm...."

        mc surpreso "É a voz da fada!"

        p "Vocês estão muito mais bonitas hoje. Hmmm... Ele tava uma delícia... hmmm..."

        "Com quem ela está falando? Preciso ver."

        "Acho que consigo uma visão de dentro pela janela..."

        scene fadolandia casa_janela with Dissolve(1.0)

        "Deixa eu dar uma olhada..."

        mc surpreso "E o que é isso agora?"

        scene fadolandia interior with Dissolve(1.0)

        "É como o quarto de uma mulher rica dentro de uma caixa de madeira... Tão estranho..."

        mc surpreso "..."

        "Acho que ela tá se trocando!"

        "..."

        "Meu Deus! O que faço agora?!"

        menu:
            "Deixar a janela e esperar do lado de fora":


                $ pixie_amizade += 1

                "Posso não ter namorada, mas não tô necessitado a ponto de ficar espiando os outros."

                mc charmoso "Não vou fazer algo tão baixo..."

                scene fadolandia casa
                with dissolve

                "..."

                "..."

                show pixie animada
                with dissolve

                p "Oi! Você está aí, bonitinho? Chegou cedo e ficou com saudades?"

                mc desculpa "Não tive paciência pra te esperar."

                p "Ué. E por que não bateu em casa?"

                mc triste "Na-não.. Eu acabei de chegar."

                show pixie sonhadora
                with dissolve

                p "Tem certeza?"

                mc desculpa "Sim, sim. Tô falando sério."

                p "Ok, então vamos lá pra dentro e conversamos melhor."

                hide pixie
                with dissolve

                scene fadolandia interior
                with dissolve
            "Se esconder e observar":


                $ p1_pixie_espiar = True
                $ pixie_seducao += 1

                "Por que interromper ela? Nunca se apressa uma mulher enquanto ela se apronta."






                scene pixie_casa5 with Dissolve(1.0)

                pause

                mc tarado "Essa não dá pra perder."

                p "Onde eu deixei minha pulseira?"

                p "Ah, tá ali."

                p "Tenho que estar em minha melhor forma. Ele deve chegar logo."

                mc tarado "..."

                p "Estou cansada de usar a mesma roupa sempre!"

                p "Eu quero tanto poder usar as roupas que os humanos usam! Quero ficar linda!"

                p "Quero ter os homens aos meus pés, loucos para pegar o pedacinho que eu quiser dar..."

                p "Hmmm..."









                scene pixie_casa6 with Dissolve(1.0)

                pause

                "Nossa... que fada deliciosa..."

                "Será que dá pra rolar um enrosco entre a gente... mesmo no sonho?"

                show black with Dissolve(0.2)

                hide black with Dissolve(0.2)

                "HUH?"

                "Eu tenho quase certeza que ela virou o corpo e me olhou nos olhos por meio segundo."

                "Que sensação estranha..."

                "Opa! Ela está terminando. Vou esperar na ponte e fingir que estou chegando."

                scene black with dissolve

                scene fadolandia casa with dissolve

                "..."

                show pixie animada
                with dissolve

                p "Oi! Você está aí, bonitinho? Chegou cedo e ficou com saudades?"

                mc desculpa "Não tive paciência pra te esperar."

                p "Você parece um pouco consternado. Alguma coisa aconteceu?"

                mc triste "Na-não.. Não é nada. Só estava pensando que já é a segunda vez que venho aqui."

                p "Se é por causa disso, não se preocupe. Vamos para dentro e te explico tudo."

                hide pixie with dissolve

                scene fadolandia interior with Dissolve(1.0)

                p "Fique à vontade..."
    else:


        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("notas_confinado_um","final","local")

        $ notas_do_confinado1 = True

        "Esperar aqui é a melhor saída. Ela só deve estar atrasada."

        "..."

        "..."

        mc normal "E o que é isso no chão?"

        mc normal "Uma nota?"

        "{i}Notas do Confinado I{/i}"

        mc zerado "Notas... do confinado?"

        show mc lendo_nota with dissolve

        "{i}Se você está lendo isto, é porque eu não estou mais neste mundo.{/i}"

        "{i}Espero que eu tenha conseguido escapar, mas se não fui feliz, torço para que pelo menos possa te ajudar{/i}"

        mc "O que raios isso significa?"

        "{i}Tenha cuidado. As fadas podem ler os nossos pensamentos. Na verdade, elas vivenciam nossas emoções e sentimentos.{/i}"

        "{i}Quando elas acessam nossa memória, elas podem reviver nossas experiências como se fossem elas próprias que as vivenciaram.{/i}"

        "{i}Algumas delas ficam...{/i}"

        mc "Ficam? Ficam o que?!"

        hide mc with dissolve

        show pixie animada with moveinbottom

        p "Oi, bonitinho."

        mc surpreso "HAH?!"

        p "Vamos passar por isso de novo?"

        mc triste "Não não... Você só me assustou."

        p "Me desculpe, então. Você parecia concentrado em algo..."

        mc normal "Não é nada. Só estava pensando que já é a segunda vez que venho aqui."

        p "Se é por causa disso, não se preocupe."

    show pixie detetive with dissolve

    p "Fui eu que te chamei novamente."

    mc normal "Por que desta vez?"

    p "Digamos que faz parte do seu treinamento."

    mc zerado "Treinamento? Pra quê?"

    p "Para mudar sua vida, obviamente."




    p "É óbvio que você precisa de um empurrãozinho para endireitar o caminho."

    p "Digamos que eu sou uma placa de trânsito. Vou apenas ajudar você a corrigir o trajeto."

    mc normal "Eu realmente não tô entendendo a metáfora."

    p "Não se preocupe, bobinho. Como da outra vez, apenas deixe minhas palavras acariciarem seus ouvidos."

    menu:
        "Esse seu jeito de falar é meio forçado.":


            mc zerado "Esse seu jeito de falar é meio forçado..."

            show pixie desconfiada with dissolve

            p "Não te perguntei nada. E você não devia falar assim com quem vai te ajudar a sair da lama."

            mc zerado "Ok... Perdão."

            p "Assim é bem melhor."
        "Certo. Sou todo ouvidos.":


            $ pixie_amizade += 1
            mc zerado "Ok..."

    p "Muito bem."

    show pixie sorrindo with dissolve

    p "Você está prestes a reencontrar a pessoa que vai mudar sua vida. E a forma como você vai abordá-la vai mudar seu futuro."







    p "Preste atenção nos detalhes, nas feições. Tente descobrir o que ela quer ouvir. O primeiro contato não é para ser verdadeiro, é para impressionar."

    mc zerado "Isso não é igual a ser um mentiroso? Um tanto antiético?"

    show pixie impaciente with dissolve

    p "Não estou falando para você falar que tem uma mansão, bobinho. A gente vê na sua cara que você é pobre."

    mc zerado "..."

    p "Quero apenas que você foque em seus pontos positivos."

    p "Não precisa falar para ela que você não namora desde que entrou na faculdade ou que seu apartamento é minúsculo ou que o trabalho tá indo para o buraco."

    mc triste "Ok, entendi."

    p "Bom garoto."

















    show pixie provocando with dissolve

    p "Estou ansiosa para sentir... quer dizer... para acompanhar seus novos passos."

    mc triste "Espere! Eu quero alguma explicação do porquê tudo isso."

    p "Eu adoraria passar a noite toda do seu lado, bebê. Mas não temos tempo. Você precisa acordar."

    mc zerado "Preciso? Por quê?"

    show pixie animada with dissolve

    p "O sonho acabou. Xau xau!"





    scene black with Dissolve(2.0)

    $ renpy.save("None-continue", extra_info="None-continue")

    scene mc dormindo with Dissolve(2.0)

    "!"

    "Que horas são?"

    "Meu Deus! É meu último dia de traba..."

    scene apartamento cama_celular with Dissolve(1.0)

    mc "Quê?! Ainda são dez da noite?!"

    mc "Por que estou gritando?! Estou com muita energia!"

    scene apartamento noite with Dissolve(1.0)

    mc normal "E agora? O que devo fazer?!"

    menu:
        "Assistir Netflix":


            "..."

            scene apartamento tv with Dissolve(1.0)

            mc feliz "Bora começar ver esse tal de Orange Is The New Black..."

            mc normal "..."

            mc bravo "Chega! Tô sem paciência pra essa loirinha."

            mc triste "Se eu continuar aqui em casa sinto que vou explodir!"

            mc normal "Já sei! Vou sair para um bar e gastar meus últimos trocados em bebidas baratas!"

            mc tarado "Excelente ideia."
        "Assistir algum canal no Youtube":


            scene mc ap_celular with Dissolve(1.0)

            "..."

            mc "AH! Ver esses vídeos não tá adiantando nada!"

            mc "Sempre a mesma merda... Sinto que vou explodir!"

            mc "Ficar em casa não vai resolver..."

            mc "Já sei! Vou sair para um bar e gastar meus últimos trocados em bebidas baratas!"

            mc "Excelente ideia."
        "Ir para o bar":


            "Ficar em casa não vai adiantar nada..."

            mc normal "Já sei! Vou sair para um bar e gastar meus últimos trocados em bebidas baratas!"

            mc tarado "Excelente ideia."

    scene cidade noite with Dissolve(3.0)

    "Esse é o barato das cidades grandes. As luzes durante a noite são muito foda."

    "Tem um bar no caminho para o trabalho. Vou dar um pulo e ver como tá o movimento."

    scene priscila bar_principal at cenario_direita with Dissolve(2.0)

    $ renpy.pause(delay=3, hard=True)



    "O lugar é bem bacana. Já escutei o pessoal da revista falando de vir aqui, mas nunca me chamaram obviamente."

    mc zerado "Quem diria que pessoas que trabalham com comunicação seriam tão fechadas..."

    "Pera!"

    "..."

    "Aquela moça no balcão!"

    scene priscila bar_principal at cenario_volta_meio with move




    "É a [cc]!"

    "O que ela faz aqui?!"

    "Que belo paparazzo, nem sei onde ela mora. Se todos aqueles sites tivessem informações importantes ao invés de 'bolo de chocolate' e 'príncipe'."

    "Ela parece estar conversando e bebendo com o rapaz do balcão. Será que ela tá sozinha?"

    "Sozinha ou não, ela parece estar se divertindo pra caramba... Por que ela pararia de fazer o que tá fazendo pra falar comigo?"




    "Quem quero enganar? Sou praticamente um desempregado, de roupa amassada, que não namora há anos... Qual é minha chance?"

    mc triste "Aahh..."

    "Será que eu deveria tentar falar com ela?"

    menu:
        "Não tenho coragem...":


            mc angustiado "Não consigo! Não tenho coragem!"

    scene cidade noite with dissolve

    "..."

    mc triste "O que me resta é voltar pra casa e ser despedido..."

    "..."

    "Não!"

    "Quem disse que eu quero ficar com ela?"

    "Pouco importa minha roupa ou minha situação profissional."

    "Eu preciso de algo sobre essa mulher e eu vou conseguir não importa o que eu tenha que fazer."

    mc bravo "Vamos lá, [mc]!"








    scene priscila bar_principal_zoom with Dissolve(2.0)

    "Primeiro eu preciso esperar ela parar de falar com o garçom..."

    "Ué..."




    scene priscila bar_triste with Dissolve(2.0)

    pause

    mc triste "Ela... parece tão triste..."

    "O barman está atendendo outras pessoas, mas ela continua sozinha no balcão."

    "Será que ela veio ao bar sozinha?"

    mc zerado "Igual eu?"

    "Olhar pra ela assim parece tão diferente das matérias da Consigo."

    "Muito diferente de hoje à tarde durante a briga com o chefe"

    "Ela parece tão..."

    "Frágil e vulnerável."




    "Precisa ser agora. Deixa eu entrar no bar."

    "..."




    scene pub geral with Dissolve(1.0)

    mc triste "Eu não lembro a última vez que falei com uma garota."

    mc angustiado "Meu coração vai sair pela boca..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Carregar para voltar aqui.")
        renpy.save("p1_save", extra_info="p1_save")

    mc concentrando "Inspira... expira..."

    mc serio "Vamos lá!"

    menu:
        "Boa noite, Priscila. Sou eu, o gato que você viu mais cedo.":


            $ priscila_seducao += 1

            mc tarado "Boa noite, Priscila. Sou eu, o gato que você viu mais cedo na redação da revista."




            scene priscila bar_primeiravez with Dissolve(1.0)

            c "?"

            c "..."

            mc desconfiado "O que foi?"

            c "Eu lembro de você. O paparazzo..."

            if orelha_porta:

                c "O idiota que trombou em mim hoje à tarde."

            jump p1_escolha2
        "É... é... é...":


            $ p1_dificuldade = True

            scene priscila bar_primeiravez with Dissolve(1.0)

            c "O que foi?"

            menu:
                "É... é...":


                    c "Fala alguma coisa... Você tá me assustando..."

                    menu:
                        "Ah... ah...":


                            mc angustiado "Ah... ah..."

                            scene pub geral with vpunch

                            show priscila n_preocupada with hpunch

                            c "Fabrício! Tira esse cara daqui! Ele tá me assustando!"

                            hide priscila
                            with dissolve

                            "..."

                            show garcom confabulando with moveinleft

                            "Fabrício" "Vem aqui, seu tranqueira! Para de incomodar as garotas do bar!"

                            mc angustiado "Mas.. mas..."

                            jump end_y
                        "Eu... na redação da revista...":


                            c "Ah! Você é o paparazzo da revista de hoje à tarde."

                            if orelha_porta:

                                c "Você é o idiota que trombou em mim."

                            mc triste "Isso..."

                            c "Meu Deus, homem... Você precisa de uma dose de coragem..."

                            mc triste "Me desculpe..."

                            c "Não precisa se cagar... eu não vou te morder."

                            "... O que eu tô fazendo?"

                            "Preciso me concentrar ou tudo vai por água abaixo."

                            mc concentrando "..."

                            mc bravo "!"

                            mc normal "Não sei o que aconteceu. Me deu uma tontura..."

                            c "Sei..."

                            mc normal "Agora estou melhor."

                            c "E daí? O que você tá fazendo aqui? O que você quer comigo?"

                            mc triste "Eu..."

                            c "Não! Pera!"

                            jump p1_escolha2
                "Eu... sou o rapaz da revista de hoje à tarde.":


                    $ priscila_amizade += 1

                    if orelha_porta:

                        c "Você é o idiota que trombou em mim..."
                    else:


                        c "Ah! Eu lembro de você."

                    mc normal "Isso. A gente se encontrou logo que você saiu da sala do chefe."

                    c "Certo. E daí?"

                    c "Não! Pera!"

                    jump p1_escolha2

        "Tava passando pelo bar e vim te pedir desculpas pela trombada hoje." if orelha_porta:

            $ priscila_seducao += 1

            mc normal "Oi. É Priscila, né? Tava passando pelo bar e vim te pedir desculpas pela trombada hoje."

            scene priscila bar_primeiravez with Dissolve(1.0)




            c "?"

            mc normal "Da revista de fofoca hoje à tarde."

            c "..."




            c "Ah, sim! Fala a verdade. Você tava tentando ouvir nossa conversa, não estava?"

            mc envergonhado "Não posso negar."

            mc normal "Mas, em minha defesa, você estava BEM exaltada."

            c "Claro!"

            c "..."

            c "Certo. Tá desculpado. E agora?"

            c "Não! Pera!"

            jump p1_escolha2

    label p1_escolha2:




        c "Você realmente acreditou no que eu disse? Realmente achou que é um 'gato' e poderia tirar fotos de mim?"

        menu:
            "Claro que sim.":


                $ priscila_seducao += 1
                mc charmoso "Claro que sim. Você não é a primeira que fala isso pra mim."

                c "Hmm..."

                mc charmoso "Fazia tempo que eu não vinha ao bar sozinho. Achei que ia ser uma noite triste, mas vejo que tirei a sorte grande."

                c "A é? Por que?"

                mc charmoso "Não é todo dia que a gente tem a chance de conversar com uma garota tão linda."

                c "Hmm..."
            "Claro que não.":


                $ priscila_amizade += 1

                mc envergonhado "HAHA... Claro que não! Estava brincando você."

                c "Verdade?"

                mc envergonhado "Sim. Te vi aqui sozinha e não sabia como puxar conversa..."

                if p1_quem:

                    $ priscila_seducao += 1
                    $ priscila_amizade += 1
                    c "Não sei se você lembra, mas eu te disse outra coisa. E essa era verdade."

                    mc desconfiado "O que?"

                    c "Que você é um fofo."

                    mc envergonhado "Ah... Obrigado."

                    mc charmoso "Você também é fofa quando quer..."

                    c "Quando quero?"

                    mc feliz "Você não foi nada fofa hoje à tarde."

                    c "Isso é verdade. Mas é que sua revista também, né?"

                    mc feliz "Eu entendo..."
                else:


                    c "Tenho que admitir que você foi corajoso."

                    mc feliz "Não é mesmo?"

                    mc envergonhado "E você parecia estar sozinha, e como eu também estava..."

                    c "Entendi onde você quer chegar."





    scene pub geral with Dissolve(1.0)

    show priscila n_feliz with dissolve

    c "Olha. Você realmente deu sorte hoje."

    c "Estou no bar sozinha e eu poderia usar sua companhia."

    "Meu Deus!"

    "Olha para essa garota..."

    "É a garota mais linda que eu já vi na minha vida."

    mc normal "Vou me sentar aqui, então."

    c "Não."

    mc desconfiado "Não? Mas..."

    c "Vamos sentar ali nos bancos. É mais reservado e bem melhor que o balcão quando a gente tem companhia."

    hide priscila with moveoutright

    c "Vem!"

    mc normal "Ah. Ok!"

    mc concentrando "Acho que estou indo bem... Preciso continuar assim..."

    scene pub booth with Dissolve(3.0)




    show priscila n_feliz with dissolve

    c "O que você está esperando? Vem logo!"

    "..."

    mc feliz "Aqui a gente vai poder conversar melhor."

    c "Não é? Por isso que te chamei pra cá."

    c "Mas eu acho que você não me disse nem seu nome ainda."

    mc normal "É verdade. Meu nome é [mc]. [mcc]."

    c "Você falou igual ao James Bond."

    menu:
        "Haha! É verdade.":


            $ priscila_amizade += 1

            mc envergonhado "Verdade! Deve ter soado bem estranho."

            show priscila n_hehe with dissolve

            c "Até que não. Foi engraçado."

            c "Eu não gosto muito dos filmes dele, mas é impossível não conhecer essa frase."
        "Na verdade o James Bond...":


            mc normal "Na verdade, o James Bond fala o sobrenome antes do nome completo."

            mc normal "Então seria assim: eu sou [mcsnome], [mcc]."




            show priscila n_chateada with dissolve

            c "Verdade?"

            c "Eu não gosto muito dos filmes dele, mas pelo menos essa fala eu achei que sabia..."




            c "Bom... tanto faz."

    c "Deixa eu sentar."

    "..."

    scene priscila bar_feliz with Dissolve(1.0)

    mc envergonhado "É..."

    mc feliz "Ah! E que tipo de filmes você gosta?"



    c "Eu gosto de comédias românticas."

    c "Aquelas histórias de amor, mas que também sejam engraçadinhas."

    c "Filme só de romance é um pouco chato. Principalmente quando tem drama no meio."

    c "Eu não tenho paciência pra filme lento."

    c "E você?"

    menu:
        "Eu prefiro games. Não sou um cara muito do cinema.":


            mc feliz "Eu prefiro games. Não sou um cara muito do cinema."

            c "Entendi..."

            mc feliz "Mas jogos são muito bacanas também."

            mc feliz "Eles possuem histórias mais complexas que os filmes às vezes."

            c "Eu não costumo jogar, só no celular de vez em quando. Mas tenho vontade de aprender mais sobre eles algum dia."

            mc feliz "Você devia fazer isso. Games são incríveis. Você só precisa encontrar aquele que você gosta."

            c "Ok. Vou dar uma olhada."
        "Eu prefiro filmes mais adultos.":


            $ priscila_seducao += 1
            mc concentrando "Hm..."

            mc "Eu gosto de filmes mais adultos."




            c "Adultos? Você diz eróticos?"

            menu:
                "Não.":


                    mc muitofeliz "Hahaha! É brincadeira."




                    c "Ah..."

                    mc feliz "Mas você parecia estar ficando interessada."

                    c "Cala a boca! Não tava não!"

                    c "Só achei que você ia falar algo interessante. Mas pelo jeito eu tava errada."
                "Sim.":


                    mc tarado "Sim. Ultimamente só tenho assistido pornô."




                    c "E eu achando que você ia falar algo refinado."

                    menu:
                        "Pornô que é bom! É fácil de entender e cumpre bem o objetivo.":


                            mc tarado "Pornô que é bom! É fácil de entender e cumpre bem o objetivo."

                            mc tarado "Não tem o que não gostar."

                            scene pub booth with vpunch

                            show priscila n_brava with hpunch

                            p "Eca! E você acha que eu quero ouvir esse tipo de coisa assim?"

                            p "Você é um idiota, isso sim!"

                            p "Com licença. E vai te catar."

                            hide priscila with dissolve

                            mc angustiado "Que? Calma, [c]! Era só brincadeira!"

                            jump end_y
                        "Era só brincadeira.":


                            mc muitofeliz "Hahaha! É brincadeira."

                            c "Ah..."

                            mc feliz "Mas você parecia estar ficando interessada."

                            c "Cala a boca! Não tava não!"

                            c "Só estava sendo educada e ouvindo você."

                            c "E mesmo você sendo um chato..."
                "Também.":


                    mc charmoso "Também. Eu me refiro a filmes que abordam temas de forma mais complexa. Onde nem tudo é preto e branco."

                    scene priscila bar_empolgada with Dissolve(1.0)

                    mc charmoso "São filmes que falam de escolhas difíceis, de pecado, de prazer. Coisas que os adultos vivenciam na vida real."

                    c "Hmm..."

                    "Ela parece interessada nesse assunto... Só que tenho que tomar cuidado pra não exagerar."

                    c "Mas... você fala de prazer, tipo sexo? Explícito?"

                    menu:
                        "Não.":


                            $ priscila_seducao += 1

                            mc serio "Não."

                            mc charmoso "Tô falando de filmes que, entre outras coisas, falam de conquista, sedução. E não só sexo."

                            mc charmoso "Mostram como um homem se aproxima de uma mulher e faz ela se sentir desejada, especial."

                            scene priscila bar_interessada with Dissolve(1.0)

                            c "De-desejada?"

                            c "Mas... mas isso não é pornografia?"

                            mc normal "Claro que não. Existem muitos filmes que falam de sexo e prazer e não são pornográficos."

                            c "Sexo... Prazer... Eu nunca..."

                            mc charmoso "Um homem precisa saber ser gentil, mas firme na hora da conquista. Precisa fazer a mulher se sentir desejada."

                            c "Sei..."

                            mc charmoso "Precisa mostrar para a mulher que ele tem tudo sobre controle e que vai fazer dela uma mulher especial."

                            c "A-hã..."

                            mc charmoso "... E vai saber como dar todo o prazer que ela busca."

                            c "Sim... Ah..."

                            mc charmoso "..."

                            c "?"

                            scene pub booth with vpunch

                            show priscila n_surpresa with dissolve

                            c "Ah!"

                            mc normal "Tudo bem?"

                            c "Sim, sim!"

                            show priscila n_chateada with dissolve

                            c "É... Estava só prestando atenção no que você estava dizendo."

                            c "Não é nada mais do que isso."

                            mc envergonhado "Eu sei. Não tô pensando em nada."

                            c "{i}Cof{/i}"
                        "Sim.":


                            mc normal "Sim."

                            c "Ah..."

                            c "Mas isso é pornô, não é?"

                            mc normal "Sim. E daí?"

                            scene priscila bar_feliz with Dissolve(1.0)

                            c "Não! Nada. Eu só achei que... fosse algo diferente."

                            mc normal "Não é que eu assista pornô. Foi só um exemplo pra você entender."

                            c "Entendi..."

                            "Eu sinto que perdi ela em algum ponto da conversa..."
        "Eu gosto de comédia romântica também!":


            $ priscila_amizade += 1

            mc feliz "Eu gosto de comédia romântica também!"

            c "Você tá se esforçando demais... Tá falando isso só pra me agradar."

            mc serio "Claro que não!"

            mc feliz "Comédia romântica é muito bom para se divertir. E não é tão idiota igual filme de comédia que é só comédia."




            scene priscila bar_empolgada with Dissolve(1.0)

            c "É exatamente o que eu penso!"

            c "Comédia que é só comédia é idiota demais! Acho que só homem gosta disso."

            "Uou. Ela tá se empolgando mesmo com a conversa."

            c "Mas pelo jeito nem todos os homens são idiotas assim, né?"

            mc charmoso "Verdade..."

    c "Olha... Nem sei como falar isso..."




    scene priscila bar_mc with Dissolve(2.0)

    c "Você até que é uma pessoa fácil de conversar."

    mc preocupado "Então por que você parece decepcionada?"

    c "Eu esperava que você só fosse outro babaca, igual aos outros."

    mc desconfiado "Outros?"

    c "Você não acha que é o único a chegar em mim nesse bar, né?"

    menu:
        "Claro que não, você é linda.":


            $ priscila_seducao += 1

            mc envergonhado "Claro que não. Você é linda, e ainda é conhecida no país inteiro. Acho que até um gay daria em cima de você."

            c "Obrigada, mas não é verdade."
        "Você estava sozinha quando cheguei, mas agora não está mais.":


            $ priscila_amizade += 1

            mc triste "Você estava sozinha quando cheguei..."

            mc feliz "Mas agora não está mais. E tenho que dizer, você é uma excelente companhia."

            c "Você é gentil, mas não é verdade."

    c "Ninguém me conhece nesse bar."

    c "Sabe qual é o problema de você ser reconhecida por todos?"

    "A pose que ela tá agora... dá pra ver tudo..."

    menu:
        "Olhar as pernas dela":


            "Eu não aguento..."

            scene priscila_bar1 with Dissolve(1.0)

            pause

            "Caraca..."

            "Como eu queria enfiar a boca no meio desse pernão..."

            "Será que eu tenho alguma chance?"

            c "[mc]?"

            mc "O-oi."

            scene priscila bar_mc with Dissolve(1.0)

            mc "T-tô ouvindo."

            c "Ok..."
        "Prestar atenção na conversa":


            "Eu tenho que prestar atenção!"

            mc "Qual o problema?"

            c "Você não tem privacidade. Você não pode fazer nada sem que os outros saibam."

            c "E isso é por causa de revistas como a sua também."

            c "Mas crianças não vêm aqui. Este é um bar pouco conhecido e apenas quem vive perto frequenta."

            c "Este é um dos únicos lugares que consigo estar sem que ninguém me reconheça."

            c "É aqui que eu venho quando tento encontrar amigos de verdade."

            c "Pessoas que aceitem quem eu sou sem que o lado celebridade interfira no que elas pensam de mim."




            c "Mas cedo ou tarde elas descobrem. E então tudo vai pro saco."

            c "Elas mudam."

            c "Ou elas se afastam ou fazem tudo o que eu quero."

            c "É horrível."

    $ renpy.notify("Priscila está avaliando suas ações no encontro...")

    c "Mas você é diferente. Pelo menos por enquanto."

    c "Você veio e falou comigo, como qualquer outra pessoa. Mesmo sabendo quem eu sou."

    if p1_dificuldade:




        c "Por mais que no começo você estivesse um pouco assustado."

        mc zerado "Podemos esquecer aquela parte?"

        c "Pensando bem, até que foi fofo."




    scene priscila bar_feliz with Dissolve(1.0)

    c "Eu estou realmente feliz que você tenha vindo falar comigo."

    c "Mas eu ainda tenho um último teste para você."

    menu:
        "Odeio testes! Mas quero que confie em mim.":


            $ priscila_amizade += 1

            mc angustiado "Odeio testes!"

            c "Agora já somos quase amigos. Não pode voltar atrás!"

            mc normal "Ok. Estou gostando muito de conversar com você. Por isso, se precisar me testar pra ter certeza que não sou um idiota, acho que eu aguento."
        "Pode mandar.":


            $ priscila_seducao += 1

            mc charmoso "Pode me pedir o que quiser. Esta noite você é minha única preocupação."

    if priscila_seducao > 4:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e1_seducao","seducao","resultado")




        label priscila_e1_finalseducao:

            $ persistent.priscila_cena2 = True

            scene priscila bar_interessada with Dissolve(1.0)

        $ renpy.notify("Priscila achou você sexy e charmoso...")

        c "Falando assim você parece tão confiante."

        c "E um homem confiante é tão sexy."

        c "Eu fico toda..."




        scene pub booth with vpunch

        show priscila n_surpresa with hpunch

        c "Quero dizer..."

        c "Me desculpe! Eu não sei porque eu disse isso!"

        mc charmoso "Tenha calma, [c]. Está tudo bem."




        show priscila n_excitada with Dissolve(1.0)

        c "Eu não sei porque, mas eu tô me sentindo..."

        c "Eu tô me sentindo quente."

        $ renpy.notify("Você adquiriu uma nova memória")

        c "Acho que eu nunca me senti assim antes. Eu quero..."

        c "Me dá licença um segundo. Volto logo para o seu teste."

        hide priscila with dissolve

        "Uou..."

        "Minha estratégia até aqui tá funcionando melhor do que eu imaginava. Quero que ela se sinta atraída por mim, e meu jeito confiante está dando certo."

        "Não posso parar agora. Preciso continuar nesse ritmo."

        "Só mais um pouco. Um empurrãozinho e eu posso chegar longe com ela hoje."

        mc tarado "Vou aproveitar e pegar uma bebida para nós. Pode ser o detalhe que faltava."

        mc tarado "Gênio."

        scene pub geral with Dissolve(1.0)

        mc normal "Poderia me ver dois chopes escuros, por favor?"

        show garcom diabolico with dissolve

        $ garcomname = "Fabrício"

        "Fabrício" "Boa noite, senhor. Meu nome é [gar]."

        "Fabrício" "Se me permite a intromissão, eu tenho algo melhor do que isso para você."

        mc desconfiado "O que quer dizer com 'melhor'?"

        "Fabrício" "Desculpe-me pela indiscrição, mas não pude deixar de notar suas intenções com a senhorita [c]."

        mc zerado "..."

        "Fabrício" "Normalmente eu te daria uma bebida com sonífero para que ambos acabassem logo com essa promiscuidade."

        "Fabrício" "Mas hoje é um dia diferente. Sinto que a senhorita [c] poderia usar de um pouco de..."

        "Fabrício" "Diversão adulta, vamos dizer assim."

        mc desconfiado "Certo..."

        "Fabrício" "Por isso vou lhe oferecer um copo de um drinque especial."

        "Fabrício" "Não se preocupe. Ele não faz nada fora do normal. Não quero drogar a senhorita."

        "Fabrício" "Trata-se apenas de um teor alcoólico mais 'alinhado' com seus objetivos."

        mc zerado "Você tem certeza que isso não é proibido?"

        "Fabrício" "Obviamente que não, senhor. É apenas uma cortesia da casa."

        "Fabrício" "Volto em um instante."

        hide garcom with dissolve

        "..."

        show garcom diabolico with moveinbottom

        "Fabrício" "Aqui está. Faça bom proveito."

        menu:
            "Muito obrigado.":


                $ p1_bebida = True

                "Fabrício" "Levarei um aperitivo diferenciado para ela comer também. Tudo por conta da casa."

                mc feliz "Muito obrigado pela cortesia. Estou confiando em você."

                "Fabrício" "Pode confiar, senhor. Não vai se arrepender."

                "O cheiro dessa bebida é bem agradável. Não estou reconhecendo. Parece vinho, algo com fruta, mas diferente."
            "Eu acho melhor ficar com o básico.":


                mc normal "Não é que eu não confie em você, mas acho que vou ficar com o básico. E por favor traga algo para ela comer também."

                mc normal "Por enquanto vem funcionando para mim."

                "Fabrício" "A escolha é sua, senhor."

                "Fabrício" "Estará na mesa em um segundo."

        scene pub booth with Dissolve(1.0)

        "Essa garota está ligas acima do meu nível. Ela é linda, gostosa, cheirosa, divertida."

        "Preciso continuar sendo confiante e sensual, mas sem exagerar. Preciso passar segurança e mostrar que sei o que eu estou fazendo."

        mc zerado "Mesmo que no fundo eu não tenha muita certeza do que eu estou fazendo."

        "Lá vem ela."




        scene priscila bar_interessada with Dissolve(1.0)

        "Desculpa a demora. Eu..."

        mc charmoso "Não precisa se desculpar. Só estava ansioso para te ver de novo."

        c "Ah..."

        c "Eu ainda estou me sentindo um pouco estranha."

        c "Mas você está pronto para o meu teste?"

        mc charmoso "Com certeza."

        c "Então..."

        mc surpreso "..."

        window hide

        scene priscila parte1 with Dissolve(2.0)

        pause

        c "..."

        menu:
            "Focar nos olhos":


                mc charmoso "Seu corpo é lindo. E eu adoro que você esteja me provocando, mas eu ainda prefiro seus olhos."

                c "..."

                c "Você... sabe como fazer uma garota se sentir especial."

                c "Se você continuar assim... eu não sei o que vai acontecer."
            "Focar em 'outras coisas'":


                mc tarado "..."

                "Não consigo tirar os olhos do meio das pernas dela..."

                scene pub booth with dissolve

                show priscila n_chateada with dissolve

                c "Ei! Onde você está olhando?"

                mc angustiado "Eu.. eu..."

                c "..."

                jump final_amizade

        mc charmoso "Você é especial. Você é linda, tem o corpo de uma deusa. E além disso é uma excelente companhia."

        c "..."

        c "Se isso é verdade, por que eu nunca..."

        c "..."

        mc triste "..."

        mc charmoso "Não pense nisso agora."

        if p1_bebida:

            mc tarado "Eu pedi um copo de uma bebida especial."

            mc tarado "Por que você não toma um gole?"
        else:


            mc normal "Eu pedi esse chop escuro pra gente. Por que você não toma um gole?"

        c "Acho que é uma boa ideia."

        c "Eu não costumo beber. Meus contratos não me deixam beber..."

        c "Mas acho que hoje vou fazer algo diferente."

        "{i}glup{/i}"

        c "Ah!"

        if p1_bebida:

            "..."

            c "Essa bebida é saborosa..."

            c "Ela é quente também. Está descendo esquentando meu corpo ainda mais."

            c "{i}puf{/i}"

            c "Estou me sentindo... ofegante..."

            c "..."

            c "Eu não sabia... que bebida alcoólica era assim..."

            mc desconfiado "Você nunca bebeu antes?"

            c "Não!"

            c "{i}puf{/i}"

            c "Eu não posso... Por causa dos contratos..."

            mc triste "..."

            c "Mas... estou começando e me sentir muito bem!"

            c "Uma vontade de gritar!"

            mc surpreso "..."

            scene priscila parte2 with Dissolve(2.0)

            pause

            c "Preciso me espreguiçar! Preciso gritar!"

            mc surpreso "Você está bem?!"

            c "Muito... bem!"

            c "Ah!"

        scene pub booth with dissolve

        show priscila n_excitada with dissolve

        c "..."

        c "Estou me sentindo tão quente, [mc]."

        c "No meu peito. Nas minhas pernas..."

        mc desculpa "..."

        c "Estou zonza, [mc]. Não consigo respirar direito..."

        c "Ah..."

        mc charmoso "Vou sentar do seu lado e te ajudar."

        c "Isso..."

        c "Vem..."

        c "Me ajuda..."

        mc charmoso "..."

        c "Deixa eu deitar em você."

        scene priscila dormindo with Dissolve(1.0)

        c "Hm..."

        c "Você tem um cheiro bom, [mc]."

        mc charmoso "Obrigado. Você também."

        c "Minhas pernas tão se mexendo sozinhas..."

        c "{i}puf{/i}"

        c "Vo-você podia encostar em mim?"

        c "Pegar no meu braço?"

        menu:
            "Claro, [c]. Qualquer coisa que você me pedir.":


                $ p1_corpo = True

                mc charmoso "Claro, [c]. Qualquer coisa que você me pedir."

                scene priscila deitada-mao with Dissolve(1.0)

                c "Isso..."

                c "Ah... Sua mão é tão quente."

                mc normal "Você tá toda arrepiada."

                c "Tô! É por sua causa."

                c "Aperta meu braço por favor."

                "..."

                c "Me aperta, [mc]."

                c "Isso! Ah..."

                c "Mas eu preciso de mais... Me aperta mais forte."

                c "Pega em mim."

                c "Pega no meu corpo."

                mc desculpa "[c], acho que o cara do bar pode ver a gente."

                c "Não importa!"

                c "Pega no meu peito! Por favor!"

                window hide

                scene priscila juntos with Dissolve(1.0)

                pause

                c "Ah! Isso!"

                c "Me aperta forte!"

                c "Pega no meu corpo, [mc]!"

                c "Assim! Eu tô queimando!"

                scene priscila_bar2 with Dissolve(1.0)

                pause

                c "{i}puf puf{/i}"

                c "Ai!"

                c "Aahh!"



                c "{i}puf puf{/i}"

                c "Tira minha blusa, [mc]."

                mc surpreso "C-como é?"

                c "Eu tô quase lá! Tira a alça e pega em mim!"

                mc "Priscila... vão acabar vendo a ge-"

                c "Cala a boca e faz!"

                mc tarado "Ok... Se você quer..."

                scene black with dissolve

                "Com licença."

                c "Isso!"

                scene priscila_bar3 with Dissolve(1.0)

                mc "Assim?"

                c "Assim! Pega em mim!"

                mc "..."

                c "Eu vou gozar! Ah!"

                c "Aah!"

                c "{i}puf puf{/i}"

                scene black with dissolve



                "Caralho... isso foi muito foda."

                "..."

                "..."
            "Eu não quero que pensem que estou me aproveitando de você.":


                mc charmoso "Você sabe que eu adoraria, mas tenho medo que pensem que estou abusando de você."

                c "..."

                mc charmoso "Você entende, né?"

                c "..."

                mc "..."

    elif priscila_amizade > 1:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e1_amizade","amizade","resultado")

        label final_amizade:

            $ persistent.priscila_cena1 = True

            scene priscila bar_mc with Dissolve(1.0)

            c "Eu sei que não tenho o direito de 'testar' você."

            $ renpy.notify("Priscila achou você confiável e um verdadeiro amigo...")

            c "Mas é que esses últimos tempos têm sido um pouco complicados pra mim."

            c "Tem tantas coisas acontecendo e eu sinto que todos ao meu lado só se importam com a 'celebridade'."

            c "Você tem sido um cara muito bacana comigo durante toda a noite."

            c "Muito mais do que eu poderia esperar de um estranho..."



            c "Sabe, [mc]... Vamos esquecer o teste?"

            mc "Huh?"

            c "Eu... não estou me sentindo muito bem..."

            $ renpy.notify("Você adquiriu uma nova memória")

            c "Você poderia só vir aqui perto por favor?"

            mc "Claro, [c]. O que você precisa?"

            c "..."

            scene pub booth with dissolve

            "O que será que tá acontecendo?"

            mc surpreso "Ei!"

            scene priscila amizade-deitada with Dissolve(1.5)

            pause

            mc "Pri-pri...!"

            c "Será que a gente podia ficar assim... só um pouco?"

            mc "Tu-tudo bem..."

            c "Eu queria sentir você."

            c "Eu queria sentir seu corpo. Só um pouco."

            mc "..."

            c "Estou te incomodando?"

            mc "Cla-claro que não."

            mc "Só estou um pouco surpreso."

            c "Por que?"

            mc "Não imaginei que você..."

            c "Eu quero confiar em você. Nem que seja só por um dia. Só por uma noite."

            c "Eu preciso confiar em alguém."

            c "Tenho que saber que alguém estará lá pra mim. Que alguém se preocupa comigo."

            c "Mesmo que não seja verdade. Mesmo que eu esteja me enganando. Preciso sentir que alguém me ama."

            c "Que alguém ama a [c] e não a [cc]."

            mc "Eu..."

            c "Não. Não precisa falar nada."

            c "Você... pode me tocar se quiser."

            menu:
                "Segurar o braço dela":


                    mc "Claro, [c]. Eu estou aqui pra você."

                    scene priscila deitada-mao with dissolve

                    mc "..."

                    c "Ah..."

                    mc "O que foi? Estou te machucando?"

                    c "Não. Seu toque é gentil e sua mão é macia."

                    c "Por favor, deixe sua mão aí."

                    c "Ela é quente."

                    mc "..."

                    "..."

                    jump priscila_dorme
                "Recusar o convite":


                    mc desculpa "Eu acho melhor não, [c]. A última coisa que eu quero é que achem que estou me aproveitando de você agora."

                    c "Você é um cavalheiro, [mc]."

                    c "Um verdadeiro príncipe..."

                    "..."

                    jump priscila_dorme
    else:


        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e1_gameover","gameover","resultado")

        c "Olha... está ficando meio tarde e é melhor eu ir agora."

        mc desconfiado "O que?"

        c "Não é nada com você. Eu... só preciso ir agora, ok?"

        c "Boa noite."

        mc angustiado "Não! Espere!"

        mc triste "..."

        "O que foi que eu fiz? Parece que minha {b}Abordagem{/b} não funcionou como eu esperava..."

        "Não consegui nem ser um cara bacana para estabelecer uma amizade e também não consegui seduzir ela."

        "Eu preciso lembrar do começo do encontro e entender o que eu errei!"

        "Se eu tivesse outra oportunidade, teria que fazer algo diferente..."

        jump end_y

    label priscila_dorme:

        window hide

        scene priscila dormindo with Dissolve(1.0)

        pause

        "..."

        mc desculpa "Priscila?"

        mc desconfiado "Pris..."

        c "{i}zzz{/i}"

        mc desculpa "Dormiu..."

        $ renpy.end_replay()

        if p1_corpo:

            "Essa é a coisa mais louca que já me aconteceu."

            "Isso foi tão maluco!"

            mc tarado "E tão sexy..."

        "Não consigo imaginar pelo que essa garota está passando."

        "Ela não é nada como eu imaginei que fosse."

        "Todos olham para ela e vêem uma mulher incrível, imbatível, confiante."

        "Mas em um bar qualquer da capital, ela deita no colo de um estranho e dorme como uma criança."

        "A máscara é pesada demais às vezes eu acho."

        "Ela parecia tão necessitada de contato humano."

        if p1_corpo:

            mc tarado "E eu dei um belo de um contato."
        else:


            mc normal "Eu fui o apoio que ela precisava. Pelo menos esta noite, eu fui o melhor amigo dela."

            mc triste "Talvez o único."

        play sound "audio/som_3_celular.mp3"

        "?" "Trrrr... trrrr..."

        "?" "Trrrr...."

        mc desconfiado "E o que é isso agora?"

        mc surpreso "É o celular dela!"

        "Smartphone" "Trrr..."

        mc zerado "Por que tô gritando?"

        "Eu preciso me acalmar. Essa é a chance que eu tava esperando..."

        "Preciso descobrir alguma coisa que eu possa usar na revista."

        "Eu sei que não é legal xeretar, mas é minha única chance de não ser despedido..."





        scene pub booth
        with dissolve

        show mc celular
        with dissolve

        "Sem tela de bloqueio? Que descuidada."

        "Deixe me ver..."

        "Uma ligação não atendida."

        "Algumas mensagens no WhatsApp. Deixa eu abrir."

        "Velho" "Oi, bonequinha. Onde você tá?"

        "Velho" "Papai está com saudades de você."

        mc "..."

        "Que nojo! Quem é esse velho?!"

        "Opa! Tem algo interessante aqui."

        "Sayu" "Vou ta no templo amnha desculpa ;("

        "Sayu" "Mas vamos marcar pra outro dia ok"

        "Sayu" "Ah n é q n confie em vc linda mas vou repetir"

        "Sayu" "Ninguem pode saber do templo ta"

        "Quem é essa? Vamos fuçar as informações do contato..."

        "[sc]..."

        "Esse nome não me é estranho."

        "Certo. Próxima."

        "E-mails talvez?"

        "'Parabéns! A negociação foi um sucesso!'"

        "'Olá, querida. A negociação foi um sucesso. Nossa viagem para a capital foi providencial para fecharmos o contrato.'"

        "'Você foi maravilhosa como sempre. E me desculpe por aquele negócio lá. Tivemos que aceitar, senão ele fecharia com outra.'"

        "'Não fique chateada por causa disso. Isso é normal, ok? Você vai ficar bem.'"

        "'PS.: Quem vai ser a nova estrela de cinema nacional?'"

        "Estrela nacional?! Contrato?! Este e-mail é de hoje! Talvez eu tenha conseguido algo incrível!"

        "Mas por que algo me parece tão errado?"

        "O que é 'aquele negócio lá'? Por que ela ficaria chateada por fechar um contrato?"

        "É coisa demais por hora. Depois eu pesquiso mais sobre tudo isso."

        "Melhor devolver o celular antes que ela acorde."

    hide mc
    with dissolve

    show garcom chamando
    with dissolve

    if p1_bebida:

        "Fabrício" "Vejo que minha bebida foi um sucesso."

        mc desconfiado "Mas o que raios era aquilo?"

        "Fabrício" "Já lhe disse senhor: nada de mais. Apenas um teor alcoólico apropriado."

        mc zerado "Que seja..."

    "Fabrício" "Longe de mim querer atrapalhar vocês, senhor."

    "Fabrício" "Mas tem um carro parado em frente ao bar esperando pela senhorita [c]."

    "Fabrício" "Talvez fosse do seu interesse acordá-la antes que os senhores de terno dentro do carro resolvam vir ver o que está ocorrendo."

    mc surpreso "!"

    mc desculpa "Eles não vão gostar de ver ela nesse estado."

    "Fabrício" "Concordo com o senhor. Boa sorte."

    scene priscila dormindo with dissolve

    mc desculpa "[c]..."

    mc normal "[c]!"

    c "Hm..."

    mc normal "Acho que seus seguranças estão te esperando."

    if p1_corpo:

        c "Não tenho coragem de olhar pra você."

        c "Não depois de tudo o que aconteceu."

        mc normal "Não precisamos falar sobre isso agora."

    c "Eu estou com tanto sono. Tão cansada."

    c "Não sei se vou conseguir levantar."

    mc charmoso "Não tem problema. Deixa comigo."

    c "Ei! Espere!"

    window hide

    scene pub geral with Dissolve(1.0)

    show priscila bar_carregada with Dissolve(1.0)

    mc "Prontinho!"

    mc "Assim você não precisa se levantar."

    c "Você..."

    mc "Ei! Só estou te ajudando!"

    c "..."

    mc "Vamos princesa. Sua carruagem tá esperando."

    c "Obrigada."







    scene cidade noite with Dissolve(3.0)

    "Eu não tenho certeza, mas acho que ela deixou cair uma lágrima quando a coloquei no carro."

    "Prefiro pensar que era uma lágrima de alegria..."

    "A cara dos seguranças... Não vou esquecer tão cedo também."

    "Com certeza a noite não saiu como eu esperava."

    "Foi muito melhor!"

    "Tudo foi tão rápido e eu estava tão nervoso... Não consigo nem lembrar direito."

    "Mas, no geral..."

    show screen menu_pontos

    if priscila_seducao > 4:

        $ priscila_e1 = "seducao"

        $ priscila_seducao_evento += 1

        "Minha confiança foi essencial para seduzi-la. Assim como sempre deixar claro minhas segundas intenções."

        "Infelizmente, não pude ser o amigo que ela precisava, mas com certeza dei a ela uma noite que não vai esquecer."

        "Sem dúvida, o resultado foi o que eu esperava."

        "Estou ansioso para vê-la novamente. E eu tenho certeza que isso vai acontecer."

    elif priscila_amizade > 2:

        $ priscila_e1 = "amizade"

        $ priscila_amizade_evento += 1

        "Não sendo um idiota, fiz ela se sentir segura comigo. Era o mínimo que eu podia fazer."

        "Eu consegui ser o amigo que ela precisava esta noite. Um ombro amigo em um momento que parecia ser de tamanha dificuldade."

        "Por um lado, não consegui seduzir ela."

        mc desculpa "E ela com certeza era uma garota linda."

        "Mas eu não me sinto frustrado."

        "Eu me senti muito bem por ter sido a rocha onde ela pôde se encostar. E quem sabe o que o futuro me aguarda?"

    hide screen menu_pontos

    scene apartamento noite with dissolve

    "Estou esgotado. Preciso dormir."

    "Amanhã preciso decidir o que fazer com o que eu descobri no celular da [c]."

    "Mas só amanhã."

    scene black with Dissolve(2.0)

    $ finalizou = "v0"

    $ v1_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("fim_v1","final","local")





    p rindo "Está gostando de Celebrity Hunter até aqui? Não deixe de curtir as redes sociais da Geiko!"

    p "A gente faz sorteios, posta novidades e dicas praticamente todos os dias!"

    menu:
        "Instagram":


            $ renpy.notify("Links externos desativados nesta edicao.")

            p rindo "Valeu!"
        "Facebook":


            $ renpy.notify("Links externos desativados nesta edicao.")

            p rindo "Valeu!"
        "Twitter":


            $ renpy.notify("Links externos desativados nesta edicao.")

            p rindo "Valeu!"
        "Sai pra lá":


            p lecionando "Hmpf... que sem educação."

























    p "Agora pode continuar... que eu tenho uma coisa pra fazer lá em casa..."

    jump v1

    label end_z:

        scene cidade dia with Dissolve(0.5)

        "Mesmo com meus pedidos de desculpa, o chefe me colocou pra fora."

        "Dois quarteirões depois eu ainda conseguia ouvir ele me amaldiçoando."

        "Tive que voltar a morar com minha família. Eles me empregaram como repositor de estoque na empresa que tínhamos."

        "Eu nunca tive namorada ou vida própria e morri sozinho de frustração com 32 anos."

        "{i}Final Z: Fala o que quer, morre como não quer{/i}"

        show pixie desconfiada
        with dissolve

        p "Opa... opa... epa..."

        p "Parece que você irritou o chefe e foi despedido..."

        p "Não se preocupe. Isso acontece com muita gente."

        if renpy.variant("mobile"):

            p "Está vendo o botão de voltar ali na parte de cima da tela? É só usar ele e retornar até antes da decisão que provocou isso."
        else:


            p "Use o botão Voltar, aqui na parte de baixo para retornar um pouco e tentar outras opções."

        p "O chefe é um cara irritado, e não precisa de muito para ele te despedir. Por isso tome cuidado, ok?"

        hide pixie
        with dissolve

        p "..."

        show pixie desconfiada
        with dissolve

        p "Ainda está aqui? Se você continuar vai dar game over e você vai voltar para o começo do jogo... Bye bye!"

        hide pixie
        with dissolve

        p "..."

        $ renpy.full_restart()

    label end_y:

        scene cidade noite with Dissolve(0.5)

        "Eu estraguei tudo! Não disse uma palavra sequer depois daquilo..."

        "Como era de se esperar, não consegui nenhuma informação dela e fui despedido da revista."

        show pixie desconfiada
        with dissolve

        p "Opa... opa... epa..."

        p "Parece que sua {b}Abordagem{/b} neste encontro não foi a melhor possível."

        p "Não se preocupe. Isso acontece com muita gente."

        if renpy.variant("mobile"):

            p "Está vendo o botão de {b}Voltar{/b} ali na parte de cima da tela? É só usar ele e retornar o encontro e tentar outras opções."
        else:


            p "Use o botão Voltar, aqui na parte de baixo para retornar para o começo e tentar outras opções."

        p "Muitas vezes estamos indo bem, mas cada celebridade gosta de uma coisa. Ser confiante demais pode ser um problema, assim como ser medroso demais."

        p "Tudo depende da garota, ou do garoto, que você quer impressionar."

        p "..."

        p "Que? Ainda não voltou? Você está brincando com fogo."

        p "Já que você ainda está aqui, deixe-me te ensinar uma coisa:"

        if renpy.variant("mobile"):

            p "Você pode salvar e carregar seu jogo clicando nos botões lá em cima. É sempre bom você salvar antes de um encontro, assim você pode voltar se precisar."
        else:


            p "Acessando o menu, clicando no botão menu aqui embaixo, você pode salvar e carregar seu jogo ou usar saves automáticos."

        p "Já pode voltar agora. Bye!"

        hide pixie
        with dissolve

        "..."

        "Tive que voltar a morar com minha família. Eles me empregaram como repositor de estoque na empresa que tínhamos."

        "Eu nunca tive namorada ou vida própria e morri sozinho de frustração com 33 anos."

        "{i}Final Y: Eu ainda não estava pronto{/i}"

        $ renpy.full_restart()

    label end_w:

        $ persistent.demitido = True

        scene cidade noite with Dissolve(1.0)

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("gameover_pauta","gameover","escolha")

        "Ele realmente me despediu..."

        if pautas > 0:

            "Eu tinha pautas pra revista..."

            "Mas não queria passá-las. Não queria prejudicar as celebridades."

            "Ou talvez eu possa só ter esquecido do meu deadline..."



        "Prefiro desistir de tudo do que implorar para as celebridades me ajudarem com dinheiro."

        "Eu ia parecer um interesseiro. Não foi pra ser um interesseiro que eu vim pra capital."

        "Também não tenho outra forma de ganhar dinheiro suficiente pra pagar condomínio, luz, comida etc."



        "Vou ter que desistir de tudo... e admitir que eu não tinha capacidade..."

        "Justo agora que eu comecei a conhecer pessoas tão interessantes na capital..."

        "Adeus capital! Adeus minhas queridas cebridades!"

        "{i}Final W: Imperfeito para o trabalho{/i}"

        scene black with Dissolve(3.0)

        show pixie impaciente with dissolve

        p "Ai... ai..."

        p "Sério mesmo que {b}você{/b} fez o [mc] ser despedido?"

        p "Você sabia muito bem que ele precisava de informações sobre os famosos. Como é o nome mesmo? Pautas... isso aí."

        show pixie detetive with dissolve

        p "Se ele não tiver o trabalho de paparazzo, como ele vai pagar o aluguel, o condomínio, as contas de água, luz, comida etc etc etc etc...?"

        p "Agora você vai ter que recomeçar o jogo e fazer escolhas diferentes. Ou pelo menos voltar alguns encontros atrás e tentar novas coisas."

        p "Seja mais amigo das celebridades. Tente fazer elas confiarem em você e revelar seus segredos. Não pense só em SEXO!"

        show pixie provocando with dissolve

        p "Claro que você também pode só desinstalar o game e voltar para aqueles jogos que não importa o que você escolha o final é sempre feliz."

        p "Mas eu confio em você. Eu sei que você vai fazer o [mc] feliz."

        p "Ah! Não se esqueça do que você concordou comigo no começo do game."

        p "Você é responsável pelas suas escolhas."

        if not premium:

            p "Na versão premium de CH eu dou dicas de como achar cada pauta no começo dos encontros."

            p "Fica bem mais fácil de não ser despedido! Se você curtiu, dá uma olhada na versão premium que tá cheia de vantagens!"

            p "Além da ajuda com as pautas, tem ganho de C$ dobrado no bar, cenas +18 exclusivas e muito mais!"

            p "Além de dar vantagens em TODOS os jogos da Geiko! Não é só CH, são todos!"

            menu:
                "Acessar site de apoiador":


                    $ renpy.notify("Links externos desativados nesta edicao.")
                "Talvez outra hora":


                    p "Sem problemas. Quando tiver afim de fazer parte do nosso clube exclusivo, basta acessar www.apoia.se/geiko"

        p "Até logo!"

        $ renpy.full_restart()

    label v1:

        "..."

    scene fadolandia geral_bot with Dissolve(3.0)

    "..."

    mc zerado "De novo esse lugar?"

    "Este sonho está cada vez mais frequente. Eu volto para essa terra da fada quase todos os dias."

    "Se eu me lembro bem, ela disse que minha vida ia mudar drasticamente. Mas eu só consigo lembrar do que ela fala quando estou aqui."

    "Não importa. Preciso achar ela..."

    "Consigo ver a casa daqui. Vou dar uma subida lá."

    mc desconfiado "Ué. Espera..."

    "Eu não vi isso das outras vezes... Parece que tem um caminho para dentro da floresta."

    menu:
        "Continuar para a casa da fada":


            mc normal "Melhor não se perder no meio deste lugar. Vamos só continuar o caminho até a casa."

            "..."

            scene fadolandia casa
            with dissolve

            "Andar por aqui realmente cansa... {i}puf{/i}"

            "Acho que estou ouvindo barulhos vindo da casa."

            menu:
                "Aproximar-se da janela":


                    mc tarado "Melhor averiguar o que está havendo antes de me denunciar."

                    scene fadolandia casa_janela with Dissolve(1.0)

                    "..."

                    "Eu consigo escutar um som vindo de dentro... algo rangendo."

                    p "Hmm..."

                    p "Ah..."

                    mc surpreso "{i}glup{/i}"

                    mc surpreso "Pa-parecem gemidos..."

                    "O que eu faço? Não quero ser pego, mas também..."

                    menu:
                        "Se afastar e chamar a fada":


                            jump p1_chamarfada
                        "Levantar a cabeça para ver":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("pixie_nua","fada","escolha")

                            "Vou dar só uma olhad..."

                            p "Eu adorei..."

                            p "{i}puf{/i}"

                            p "... Quando você me pegou daquele jeito..."

                            p "{i}puf{/i}"

                            mc surpreso "O que raios está acontecendo lá dentro?! Preciso ver!"

                            scene fadolandia casa_janela
                            with vpunch

                            "{i}TUMP{/i}"

                            "Droga! Bati minha cabeça! Ela vai me ouvir!"

                            p "Quem está aí?!"

                            p "RESPONDA!"

                            mc angustiado "..."




                            scene pixie_casa1 with Dissolve(1.0)

                            mc angustiado "..."

                            p "..."

                            mc surpreso "Eu... eu..."

                            menu:
                                "Caraca! Você é linda!":


                                    mc tarado "Você é mais linda e gostosa do que eu imaginei!"

                                    p "..."

                                    mc feliz "..."

                                    p "Você achou mesmo que ia funcionar?"

                                    mc triste "Talvez..."
                                "Perdão! Não era me intenção!":


                                    mc angustiado "Por favor! Não me mate! Não era minha intenção!"

                                    p "..."

                                    mc triste "..."

                                    p "Pff... Você é fofo quando quer."

                                    p "Mas você me interrompeu em um momento muito... como posso dizer... delicado..."

                                    p "O que você vai fazer a respeito?"

                                    mc surpreso "Eu... eu..."

                            scene pixie_casa2 with Dissolve(1.0)

                            p "Será que você merece um pedaço disto aqui?"

                            mc surpreso "..."

                            p "O que você acha? Quer um pedaço?"

                            menu:
                                "Eu... eu...":


                                    mc normal "Não... Eu..."

                                    p "É assim que você pretende conquistar as celebridades, bobinho?"

                                    p "Você é fofo, mas precisa de mais coragem."

                                    p "Eu sei que você quer me morder."
                                "Qualquer hora.":


                                    mc charmoso "Qualquer hora."

                                    p "Falando assim você deixa qualquer garota arrepiada."

                                    p "Então pode ser agora?"

                                    mc tarado "Com certeza."




                            p "Quem sabe na sua próxima visita?"

                            p "Vem aqui. Temos que conversar."
                "Chamar a fada":


                    label p1_chamarfada:

                        "É melhor eu não arriscar."

                        "Vai saber o que ela pode fazer comigo se me ver zanzando pela propriedade dela."

                        "..."

                        scene fadolandia casa
                        with dissolve

                        mc normal "Pixie!"

                        "..."

                        p "É você, bebê?!"

                        p "Só um segundo..."

                        "..."

                        p "Pode entrar. Estou te esperando!"

                        mc "..."
        "Seguir o caminho por entre as árvores":


            mc triste "Não sei se eu deveria me aventurar por este lugar, mas a curiosidade é maior que o gato. Pelo menos é o que dizem."

            scene fadolandia ponte with Dissolve(3.0)

            "Esse lugar é completamente novo para mim."

            "É como se eu pudesse controlar meu próprio sonho."

            "Pensando bem, desde que comecei a sonhar com essa fada, toda vez que durmo é a mesma coisa."

            "Esses sonhos são tão reais. E, por mais que eles sejam meio loucos, eu tenho a impressão que não são como os outros sonhos que eu tenho."

            "É como se na verdade fosse..."

            show velho morto with vpunch

            mc surpreso "ARGH!"

            mc angustiado "O que é isso!?"

            mc angustiado "Mas que merda é essa?!"

            mc triste "Eca... Parece um velho... mas com a pele toda esquisita"

            "O que esse corpo faz aqui?"

            mc triste "Por que eu tive que andar até aqui..."

            menu:
                "Investigar o corpo":


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("notas_confinado_dois","velho","escolha")

                    "O que eu estou pensando?"

                    "Por que eu iria querer encostar nesse defunto?"

                    "..."

                    show velho morto with dissolve

                    mc triste "Eca. A pele dele tá toda estranha. Tá seca... e parece que vai soltar do corpo."

                    "É como se não tivesse nada dentro dele."

                    mc desconfiado "Epa!"

                    "Acho que tem um bilhete embaixo dele."

                    "Deixa eu ver."

                    "{i}Notas do Confinado II{/i}"

                    if notas_do_confinado1:

                        "Espere!"

                        "Eu lembro de ter lido algo parecido em outro de meus sonhos."

                        "Era um recado deixado por outra pessoa que esteve aqui."

                        "A nota falava algo que eu não entendi muito bem na hora, mas era algo sobre as fadas."

                        "Aparentemte o cara que escreveu essas notas não teve um final feliz."

                        "..."

                        "Não importa. Deixa eu ler esta aqui."

                    "{i}Foi aos poucos. Obviamente que seria. De que outra forma seríamos convencidos?{/i}"

                    "{i}Um pouco mais longe, só mais um pouco. Estou perto do que eu quero.{/i}"

                    "{i}Eu quero ela. É por isso que venho. É por isso que volto.{/i}"

                    "{i}Mas qual é o preço? Qual é o preço da minha perversão?{/i}"

                    "{i}Não importa. Eu pagarei o que me for pedido. Pagarei com meu corpo e até com minha alma.{/i}"

                    "{i}E o que será de mim depois?{/i}"

                    "{i}Será que fiz a escolha certa?{/i}"

                    "{i}Se você está lendo isto, saiba que ainda há tempo. Você ainda pode fugir.{/i}"

                    "{i}Mas você quer fugir?{/i}"

                    mc triste "..."

                    "Que porra foi essa?!"

                    "Não sei ao que ele se refere. Mas seja o que for parece que o final foi horrível."

                    "Tenho a impressão que ele se arrependeu antes do fim."

                    "E o que ele quer dizer com {i}Se você está lendo isto, saiba que ainda há tempo{/i}?"

                    "Tempo pra quê?"

                    "Tudo isso tá me deixando assustado. Melhor eu voltar para o meu caminho."

                    $ notas_do_confinado2 = True

                    jump p1_chamarfada
                "Dar meia volta e ir até a casa da fada":


                    jump p1_chamarfada

    scene fadolandia interior with Dissolve(1.0)

    "..."

    mc surpreso "!"



    scene pixie_casa3 with Dissolve(1.0)

    p "O que foi?"

    mc envergonhado "Não foi nada..."

    p "Não precisa ficar assim, bebê."

    if p1_pixie_espiar:

        p "Eu sei que não é a primeira vez que você me vê assim."

        mc envergonhado "..."

        p "Eu sei que você adorou me ver assim daquela vez."

        p "Não esquece que eu posso ler sua mente."

        p "Você parecia estar tirando minha roupa com os olhos"

        mc charmoso "Não posso negar."

        p "Bom menino. Quero que você me deseje."

        p "Você me deseja?"

        mc charmoso "Claro."

        p "Muito bem..."

        mc charmoso "..."

        p "Mas isso que você tá pensando vai ficar para outra visita. Agora vamos focar no que é importante."

    p "Te chamei aqui para conversarmos sobre esta noite."

    mc desconfiado "Esta noite?"

    p "Exatamente."

    if priscila_seducao_evento > 0:

        p "Eu adorei o que você fez com a garota Priscila."




        p "Você foi confiante e soube aproveitar todas as oportunidades para atacar."

        p "Eu sei que não foi fácil, mas você insistiu até conseguir."

        p "E daí que ela estava fragilizada?"

        p "Ela sentiu prazer da mesma forma."

        mc zerado "Tem certeza que tá tudo certo?"

        p "Não pense nisso agora. O importante é que vocês se divertiram..."

        p "E eu senti tudo também."

        p "Tanto tesão. Você estava prestes a explodir. Ela também."

        p "Depois desta noite restou pouco que eu possa te ensinar."

        p "Apenas continue atento. Cada garota possui uma forma diferente de ser conquistada."

        p "Preste atenção em cada uma delas. Tente decifrá-las antes de atacar."

        mc desconfiado "Atacar?"

        p "Exatamente."

        p "Ah! E outra coisa: por mais que dominar todas elas seja algo tentador, tome cuidado para não ser descoberto."

        p "Sua sociedade é monogâmica, então sua {b}namoradinha{/b} pode não gostar de descobrir que você está se divertindo com outras."

        mc desconfiado "Você dizendo isso? Você parece não se preocupar muito com essas coisas."

        p "É claro que eu não me preocupo, bebê. Mas preciso te ensinar tudo o que eu posso, para que depois você não me culpe quando acabar sozinho."

        mc triste "..."

        p "Mas não quero saber de medo. Você é um caçador. E caçadores capturam TODAS presas possíveis. É o que eu espero de você."

        mc zerado "..."

    elif priscila_amizade_evento > 0:

        p "Você foi um cavalheiro com a Priscila."




        p "Ela estava fragilizada, e você esteve lá para ela. Isso foi muito importante se você deseja ter uma relação mais duradoura com ela."

        p "É importante que ela confie em você. Por isso te dou meus parabéns."

        p "MAS!"

        mc zerado "Tudo tem um 'mas'?"

        p "Obviamente que você não quer ser um amigo para ela para sempre. Mesmo que você possa fazer isso, não seria nada divertido."

        p "Eu quero sentir... quer dizer, eu quero que você sinta excitação. Quero que você domine ela também, como um verdadeiro caçador."

        p "Se for preciso, não se esqueça do meu poder. Contanto que você tenha gravado o momento do encontro, eu posso te mandar para reviver a noite."

        mc desconfiado "Eu ainda acho isso extremamente viajado..."

        p "Não importa o que você acha."

        p "Nesta altura do campeonato você já entende que é possível mudar seu destino dependendo de como você interage com as pessoas."

        p "Quero dizer que, caso você tivesse seduzido ela, eu estaria falando outra coisa totalmente diferente para você agora."

        mc zerado "..."

        p "Por isso, talvez você queira sempre tentar coisas diferentes, pois você nunca sabe o que o destino te aguarda."

        mc normal "Ok. Vou tentar lembrar das suas lições."

        p "Bom garoto."



    mc envergonhado "Até quando você vai ficar falando com seus melões de fora?"

    p "Tá te incomodando?"

    mc surpreso "Não! Parace que você não liga..."

    p "Bom... se isso é demais pra um puritano igual você, eu cubro eles."

    scene black with dissolve

    scene pixie_casa4 with Dissolve(1.0)

    pause

    p "Melhorou?"

    mc zerado "Você cobriu os peitos e tirou a parte de baixo?"

    p "Tee-hee..."

























    p "Mas por esta noite é o suficiente."

    p "Estamos nos aproximando do fim do seu curso. Fico triste só de pensar."

    mc normal "O que isso quer dizer?"

    p "Quer dizer que eu não vou mais te trazer aqui à força."

    mc surpreso "Estou livre de você?!"

    p "Não fale como se fosse uma coisa boa."

    mc envergonhado "Foi engraçado, vai..."

    p "Mas a partir de agora você vai poder me visitar quando você quiser."

    p "Sempre que você dormir, você pode, por conta própria, vir me visitar. A gente pode fazer várias coisas divertidas."

    mc desconfiado "Por que tudo o que você fala tem uma certa conotação sexual?"

    p "Porque nós s... fadas... temos hormônios incontroláveis."

    if p1_pixie_espiar:

        p "Quero que você acorde duro pensando em mim."

    p "Xau xau, bebê."

    scene black with Dissolve(2.0)

    $ tempo = 1
    $ dia += 1

    scene apartamento cama with Dissolve(3.0)

    show screen menu_funcao

    "z{size=20}{i}z{/i}{/size}{size=18}{i}z{/i}{/size}{size=16}{i}z{/i}{/size}{size=14}{i}z{/i}{/size}{size=12}{i}z{/i}{/size}{size=10}{i}z{/i}{/size}"

    show mc acordando with dissolve

    "Uaahh..."



    "Tô me sentindo legal hoje também. Tomara seja um dia tão bom quanto ontem."

    scene apartamento cama_celular with dissolve



    mc "E lembrando tudo o que eu descobri sobre a Priscila..."

    "Ela vai estrelar um filme..."

    "Eu tenho bastante material para a revista."

    "Mas o que vai acontecer com ela se eu contar tudo para o chefe?"

    "Eu sou um paparazzo, não devia tá pensando nisso, mas não consigo só ignorar ela."

    play sound "audio/som_16_chuveiro.mp3"

    scene mc banho with Dissolve(1.0)

    $ renpy.pause(5)

    "Preciso pensar muito bem o que fazer com essas informações. A vida dela vai mudar, assim como minha relação com ela muito provavelmente."

    "E ainda por cima tem a tal da Sayuri e o templo."

    "Templo? Existe esse tipo de coisa no nosso país?"

    mc "Nunca ouvi falar de templo algum."

    "Ele fica na {b}Cidade Chinesa{/b}... que é um bairro da capital. É mais ou menos perto daqui."

    "Preciso pegar a saída ao sul da ilha e ir de ônibus."

    "Enfim, tenho que me arrumar."

    stop sound

    scene apartamento geral with Dissolve(1.0)



    "Amanhã o chefe vai me despedir. Tenho que fazer alguma coisa. Posso começar pesquisando sobre a tal Sayuri..."

    "Nessas horas o Google é o caminho."

    "Sayuri..."

    "Sayuri..."

    mc surpreso "QUÊ?!"

    "SporET" "Sayuri Ichigo é medalhista olímpica por três edições seguidas. Já são 13 anos no topo, como a principal atleta do país."

    "SporET" "Muitos especialistas apontam Ichigo como a expressão máxima da ginástica. Seus movimentos são precisos, graciosos e de impecável técnica."

    "SporET" "Agora com 25 anos, Ichigo é medalhista de ouro desde os 12. Daqui a 3 anos, ela participará de sua última competição olímpica."

    "SporET" "Sua meta é finalizar sua carreira com chave de ouro: 'Não é mais que minha obrigação', disse Ichigo comentando a possibilidade de sua quarta medalha."

    "SporET" "Muitos apontam como segredo de Sayuri seu local secreto de treinamento. Nem mesmo seus fãs mais próximos sabem onde ela treina."

    "SporET" "Uma quantidade enorme de jornalistas já tentou encontrar esse 'local secreto', mas sem sucesso. Quem sabe um dia ela revele?"

    mc surpreso "O TEMPLO!"

    $ priscila_numero = True
    $ pautas += 2
    $ sayuri_p1 = True
    $ priscila_p1 = True

    if priscila_amizade_evento > 0:

        $ priscila_cel_msg1 = True
        $ celular_notificacao = True

    "Por isso ela foi tão assertiva sobre a [c] guardar o segredo... É algo que ninguém sabe..."

    mc tarado "E agora eu sei..."

    mc desculpa "Preciso pensar muito bem no que vou fazer... Tanto passar essa informação para o chefe como investigar ela por mim mesmo e quem sabe descobrir mais coisas."

    "Decisões... Decisões..."

    "Seja como for, preciso sair daqui e fazer alguma coisa. O dia me espera!"







    $ renpy.choice_for_skipping()









    menu:
        "Ir para a cidade":




            label voltar_cidade:

                jump call_cidade

    jump voltar_cidade

    "Estou aqui eeee"





    label cenario_bar:

        $ estou_na_cidade = False

        scene pub geral with Dissolve(1.0)

        if tempo > 1 or trabalho_bar:

            if v4_fim and not trabalho_bar:

                jump trabalho_bar_introducao

            if tempo > 1:

                play sound "audio/som_6_bar.mp3"

                $ randh = random.randint(1,20)

                if randh == 1:

                    "O bar do [gar] é sempre movimentado. E agora, o que eu faço?"

                elif randh == 2:

                    "É muito bom vir aqui, ver as pessoas, escutar a música..."

                elif randh == 3:

                    "O [gar] deve ser o cara mais estranho que eu vi nessa ilha."

                elif randh == 4:

                    "Olha, às vezes até dá vontade de encher a cara, mas gastar dinheiro com isso? A vontade some na hora."

                elif randh == 5:

                    "No barzinho sempre dá pra encontrar umas pessoas interessantes. Quem sabe..."

                elif randh == 6:

                    "Ainda lembro do dia que eu conheci a [c]..."

                elif randh == 7:

                    "A primeira pauta que eu consegui foi aqui. Nunca vou esquecer aquela noite."

                elif randh == 8:

                    "Fazer bicos aqui no bar tá fazendo eu ter outros olhos pra isso aqui."

                elif randh == 9:

                    "O [gar] parece conhecer bastante sobre as pessoas da ilha. Como será que ele faz isso?"

                elif randh == 10:

                    "Bem que o [gar] podia me dar na broderagem... uma pauta! Qualquer informação sobre famosos já ajudava."

                elif randh == 11:

                    "Olha... pra manter um barzinho desses aberto do lado de um Cassino, o [gar] deve fazer alguma mágica."

                elif randh == 12:

                    "Nada melhor que o clima de barzinho... quando a gente não tá lavando prato..."
                else:


                    pass
            else:


                "Essa hora o bar ainda não abriu. Eu posso ajudar o [gar] a arrumar tudo e ganhar uma grana."

            label fabricio_bar_menu:

                pass

            menu:

                "{b}Comprar a roupa para trabalhar na Blergh!{/b} (C$ 250) (continua a história)" if n8_roupa == 1:

                    python:
                        if renpy.android:
                            roupa_nathan = PythonSDLActivity.pegaRoupaNathan()

                    mc "Pagar pra trabalhar pra você... onde já se viu isso?"

                    if roupa_nathan:

                        $ n8_roupa = 2

                        "{b}Como você já pagou por isto antes, você não precisa pagar novamente{/b}"

                        mc "Beleza, toma aqui a grana."

                        mc "Vamos lá!"

                        gar "Vamos, adorado ajudante. A festa nos aguarda!"

                        scene black with dissolve

                        jump nathan_evento8_parte2

                    python:
                        if renpy.android:
                            cash = PythonSDLActivity.pegaCash()

                    "Então eu preciso de {b}C$ 250{/b} pra comprar essa roupa e trabalhar na Blergh! Fabrício muquirana."

                    gar "Imagine todas as possibilidades..."

                    "Deixa eu ver..."

                    if cash >= 250:

                        mc "Eu tenho o dinheiro suficiente comigo."

                        gar "Não esperava menos do senhor, leal parceiro. Vai querer?"

                        menu:
                            "Sim. Eu preciso ir trabalhar lá. (continua a história)":


                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()
                                        
                                        if cash >= 250:
                                            
                                            PythonSDLActivity.compraRoupaNathan()
                                            
                                            roupa_nathan = True

                                if roupa_nathan:

                                    $ renpy.block_rollback()

                                    mc charmoso "Com certeza."

                                    play sound "extra/carta.mp3"

                                    "{b}Você usou {b}C$ 250{/b} e adquiriu o uniforme de garçom!{/b}"

                                    "{b}Mesmo que você volte ou reinicie o jogo, não será preciso pagar pelo uniforme novamente{/b}"

                                    python:
                                        if renpy.android:
                                            PythonSDLActivity.registraEvento("final_nathan1","mc","personagem")

                                    $ n8_roupa = 2

                                    mc "Vamos lá!"

                                    gar "Vamos, adorado ajudante. A festa nos aguarda!"

                                    scene black with dissolve

                                    jump nathan_evento8_parte2
                                else:


                                    "{b}Algo deu errado com sua compra. Tente novamente{/b}"

                                jump fabricio_bar_menu
                            "Agora não. Outra hora.":


                                gar "Estarei esperando, honorável amigo."

                                "{b}É necessário continuar a história do Nathan para ver o final dos outros personagens principais{/b}"

                                jump fabricio_bar_menu
                    else:


                        mc "Não tenho grana..."

                        gar "Ora, ora, amigo... são apenas C$ 250. Para conquistar milhões! Você sabe onde conseguir tal montante."

                        mc "Sei... trabalhando pra você..."

                        gar "A recompensa será muito maior do que seu cérebro reptiliano pode imaginar."

                        "{b}É necessário continuar a história do Nathan para ver o final dos outros personagens principais{/b}"

                        "{b}Junte C$ 250 trabalhando no bar, no lámen, ou compre com dinheiro real para prosseguir a história{/b}"

                        jump fabricio_bar_menu

                "Trabalhar no bar" if trabalho_bar:

                    if tempo == 1 or tempo == 3:

                        jump trabalho_inicio

                    if tempo == 2:

                        mc normal "Fala, [gar]. Queria ajudar você a dar uma arrumada no bar."

                        show garcom confabulando with dissolve

                        gar "Como lhe disse, senhor [mc]. Só podemos temperar com o bar pela manhã antes dele abrir ou de madrugada depois que todos deixaram o aposento."

                        mc envergonhado "Ah, verdade. Esqueci..."

                        mc normal "Volto outra hora."

                        gar "Estarei sempre lhe aguardando."

                        hide garcom with dissolve

                        "O jeito que esse cara fala sempre me incomoda..."

                        jump cenario_bar

                "Pedir uma pauta para o [gar]" if not fabricio_p1 and fabricio_atencao == 0:

                    "Tô precisando de uma pauta urgente, senão posso ser despedido uma hora que o chefe me chamar."

                    "O [gar] parece saber de tudo o que acontece por aqui. Bem que ele podia me arranjar algo pra publicar."

                    "Deixa eu ver com ele."

                    "..."

                    mc normal "Fala aí, [gar]."

                    show garcom chamando with dissolve

                    gar "Que alegria imensurável encontrar-me próximo a criatura de tal estatura."

                    mc zerado "Você também..."

                    gar "Como posso ser de serventia, senhor [mcc]?"

                    mc envergonhado "Você sabe que eu trabalho na revista aqui da ilha e tô sempre precisando de informações quentes."

                    mc "Você, por acaso, não teria uma informação que eu possa publicar?"

                    gar "Tenho muitas informações que o senhor chefe adoraria publicar na revista, senhor [mc]."

                    mc surpreso "Sério?! Você pode me falar uma?!"

                    if trabalho_bar:

                        gar "Obviamente não será possível. Estas informações são valorosas justamente por não serem públicas."

                        mc angustiado "Não tem nada que eu possa fazer pra você me falar?!"

                        gar "Em verdade te digo... existe, sim."

                        gar "Preciso que você prossiga me auxiliando a lavar a louça do bar sempre que possível."

                        mc zerado "Não tô gostando de onde essa conversa tá indo."

                        gar "Portanto, lhe direi algo para publicar e salvar sua estável posição perante o trabalho dignificante."

                        gar "Tenho apenas uma condição. Você terá que me pagar o valor de {b}C$ 250{/b} pela informação."

                        python:
                            if renpy.android:
                                pauta_fabricio = PythonSDLActivity.pegaPauta()

                        if not pauta_fabricio:

                            "Hmmm...."

                            "Comprar uma pauta... será que é uma boa?"

                            show black with dissolve

                            p rindo "Oi! Tudo bem? Agora é uma boa hora para te explicar uma coisa importante sobre o jogo."

                            p "Tudo o que precisa esperar {b}tempo real{/b} ou usa {b}Celebrity Reias{/b} ou {b}Celebrity Coins{/b} NÃO desaparece quando você reinicia o jogo."

                            p "Isso quer dizer que se você usar C$ para pagar por esta pauta, e depois reiniciar o jogo, é só voltar aqui e falar com o [gar] novamente."

                            p "Ele vai te dar a pauta de graça, sem precisar pagar novamente. Legal, né?"

                            p "O criador do jogo fez assim para você poder reiniciar o game quantas vezes quiser para ver todos os finais possíveis."

                            p "Ah! Isso não vale só pra esta pauta. Se você comprar o apartamento novo, cartas, esperar pelas aulas de massagem ou até me visitar em Fadolândia."

                            p "Todas essas coisas não precisa pagar ou esperar novamente se reiniciar."

                            p lecionando "IMPORTANTE! Caso você precise apagar o jogo do celular, tenha certeza que você está logado na sua conta para depois recuperar tudo."

                            p lecionando "Se você estiver logado na sua conta, você pode apagar e reinstalar o jogo e daí é só fazer login novamente na mesma conta."

                            p rindo "Assim você recupera tudo o que você já comprou e esperou."

                            p "Desculpa por falar demais. Mas acho que é algo importante para todo jogador saber. Bom jogo!"

                            hide black with dissolve

                            label fabricio_pauta_menu:

                                python:
                                    if renpy.android:
                                        cash = PythonSDLActivity.pegaCash()

                                gar "Então. São C$ 250 pela informação. Assim faço você trabalhar no bar me ajudando até conseguir toda a grana."

                            mc envergonhado "Entendi..."

                            if cash >= 250:

                                "Eu tenho dinheiro suficiente pra pagar..."

                                "Pautas são essenciais pra eu continuar na ilha e o valor nem é alto. Eu acho que é um excelente negócio."

                                menu:

                                    "Comprar a pauta do [gar]" if cash >= 250:

                                        python:
                                            if renpy.android:
                                                PythonSDLActivity.compraPauta()

                                        $ renpy.block_rollback()

                                        "Vou comprar."

                                        jump fabricio_pauta_comprou
                                    "Não comprar a pauta":


                                        "Mesmo tendo grana, não quero comprar isso agora."

                                        mc envergonhado "Valeu, [gar]. Mas vou pensar um pouco e depois volto pra gente ver isso."

                                        gar "A pressa é inimiga da perfeição, senhor [mc]. Pense o tempo necessário e volte com a certeza no coração."

                                        gar "Tenha uma boa vida."

                                        mc zerado "Você também..."

                                        jump call_cidade
                            else:


                                mc surpreso "Tudo isso?!"

                                mc angustiado "Eu sou pobre, [gar]!"

                                show black with Dissolve(1.0)

                                p lecionando "Ixi. O [mc] tá pobre que só ele..."

                                p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                                p "Além de garantir essa pauta para te manter tranquilo no trabalho, você ainda contribui com o desenvolvimento de CH."

                                p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

                                menu:
                                    "Sim. Tô com uma graninha sobrando aqui.":


                                        p rindo "Que bom!"

                                        call comprar_cash from _call_comprar_cash_7

                                        p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                                        hide black with dissolve

                                        jump fabricio_pauta_menu
                                    "Não. Tô pobre igual a ele...":


                                        p rindo "Não esquente."

                                        p "Escute as dicas do [gar] e você vai ficar bem."

                                        hide black with dissolve

                                gar "A única pobreza problemática é a pobreza de espírito, senhor [mc]."

                                gar "Você não há de se preocupar com dinheiro, pois basta trabalhar comigo no bar e tudo será resolvido."

                                mc angustiado "Mas você me paga muito pouco!"

                                show garcom confabulando with dissolve

                                gar "Ora ora, senhor [mc]. Há de fazermos as contas para descobrir isso."

                                mc envergonhado "Ok..."

                                gar "Você pode ganhar C$ 9, C$ 12 ou C$ 15 por cada trabalho no bar, estou correto?"

                                mc normal "Sim. Muito pouco."

                                gar "Mas você não é de ferro, pois isto é só um bico. Você precisa dividir esse tempo cumprindo hora na redação."

                                mc zerado "Além de correr atrás de famosos, fazer compras, lavar roupa, pagar as contas, limpar a casa, jogar games..."

                                gar "Exatamente. Digamos que em um mundo hipótetico você possa trabalhar quatro vezes por dia."

                                gar "Por exemplo, se você acordar 9h, você pode trabalhar 9h, 12h, 15h e 18h."

                                mc normal "Certo. Não é tanto assim, já que o trabalho aqui é rápido."

                                gar "Ganhando em média C$ 12 por trabalho, você receberá C$ 48 por dia."

                                mc normal "E eu posso complementar até mesmo com outros bicos pela cidade."

                                gar "Exatamente! É muito fácil ganhar C$ 50 por dia. Isso quer dizer que em 5 dias você terá dinheiro para me pagar pela pauta."

                                mc desculpa "Até que não é tão complicado assim..."

                                show garcom diabolico with dissolve

                                gar "Agora que você viu a luz, venha me ajudar aqui sempre que possível e se torne um milionário!"

                                mc zerado "Essa era a conclusão que você queria chegar desde o começo, né?"

                                mc "Adeus..."

                                gar "Volte quando quiser a pauta, senhor [mc]! Boa vida!"

                                hide garcom with dissolve

                                "Ele é um manipulador, mas ele tem razão em uma coisa."

                                "Se eu trabalhar direitinho, vou conseguir ter uma grana extra pra aproveitar muito melhor minha vida nesta ilha!"

                                mc charmoso "Força, [mc]! Só depende de você!"

                                jump call_cidade
                        else:


                            label fabricio_pauta_comprou:

                                $ pautas += 1
                                $ fabricio_p1 = True

                                mc charmoso "Tá aqui o dinheiro."

                                show garcom diabolico with dissolve

                                gar "Excelente! Tenho certeza que você vai apreciar o conteúdo desta informação."

                                gar "Trata-se da mágica [qui]. Ela visita este bar todas as noites de lua cheia."

                                mc surpreso "Quê?! Nem sei quem é essa!"

                                gar "Seu conhecimento é limitado, mas seu chefe entenderá."

                                gar "Só alerto para o seguinte fato. Talvez a Quincy venha atrás de você quando ela descobrir quem a dedurou."

                                mc zerado "E por que ela não vai atrás de você que falou?"

                                gar "Ela me deve um favor, e não pode me matar até que o favor seja retribuído. Está no Livro de Ética dos magos."

                                mc "..."

                                mc normal "De qualquer forma, obrigado pela informação."

                                gar "Tenha um bom resto de vida, excelentíssimo senhor [mc]."

                                hide garcom with dissolve

                                "Essa pauta com certeza vai me manter na ilha por mais tempo. Isso é excelente."

                                scene black with dissolve

                                play sound "extra/carta.mp3"

                                "{b}[mc] recebeu informações sobre a maga [qui]{/b}"

                                jump call_cidade
                    else:


                        gar "Obviamente não será possível. Estas informações são valorosas justamente por não serem públicas."

                        mc zerado "Tá me zoando..."

                        gar "Continue seus afazeres na ilha, principalmente com a jovem e linda [cc] e venha falar comigo mais tarde."

                        gar "Talvez eu possa lhe ajudar."

                        mc "Ok..."

                        gar "Tenha um bom resto de dia."

                        jump call_cidade

                "Falar com o garçom" if tempo > 1:

                    jump bar_garcom

                "Procurar o [n]" if nathan_evento and tempo > 1:

                    if tempo == 3:

                        jump nathan_evento1
                    else:


                        "..."

                        "..."

                        "Parece que ele não está aqui agora..."

                        "Pensando bem, a [j] disse que ele vem aqui durante a noite."

                        mc zerado "O que eu estou fazendo?"

                        jump cenario_bar
                "Sair":


                    $ estou_na_cidade = True

                    jump call_cidade
        else:


            "O bar está fechado agora."

            mc zerado "O que eu tô fazendo aqui?"

        jump call_cidade

    label bar_garcom:

        show garcom chamando with dissolve

        gar "Olá, senhor. Com o que posso ajudar?"

        menu:

            "O que você sabe sobre o Barão?" if natasha_e2 == "patricia":

                $ natasha_e2 = "fabricio"

                mc normal "Estou escrevendo uma matéria sobre o Barão... o que você sabe sobre ele?"

                gar "Minha pessoa? O que ela poderia saber, senhor [mc]?"

                mc zerado "Eu tenho a impressão que você sabe mais do que aparenta..."

                gar "Tamanha desconfiança esmaga meu coração, estimado [mc]..."

                mc "Vai falar algo ou não?"

                gar "O senhor não me deixa alternativa..."

                mc normal "Opa."

                show garcom confabulando with dissolve

                gar "O Barão é o dono do Cassino do Barão. É o que sei."

                mc zerado "Tá brincado..."

                gar "Hohoho... eu sou deveras espirituoso, ou não sou, senhor [mc]?"

                mc "..."

                gar "Você já vive na ilha há um bom tempo... você deve ter notado certas sombras pela capital..."

                mc desconfiado "Sombras?"

                gar "Aqueles que estão sobre a cidade projetam sua presença em todos os cantos da mesma."

                gar "Por conta disso, o sol não lhes convém. Esconder-se faz parte daqueles que agem longe dos olhos."

                mc desconfiado "Hm?"

                "O que ele quer dizer com isso? Por que o [gar] fala desse jeito?"

                gar "Entende, senhor [mc]?"

                mc envergonhado "Não tenho certeza..."

                gar "O senhor pode ser um tanto quanto desprovido de plasticidade neuronal, mas acredito que você chegará à resposta."

                gar "Expondo mais do que isso, estaria fazendo-me alvo de um tiro mais do que certeiro."

                mc desculpa "Não tem nada de concreto?"

                gar "Nem as paredes de meu humilde estabelecimento são tão concretas quanto as informações que foram lhe passadas nesta noite."

                mc zerado "Ok... Valeu."

                gar "Talvez o próximo passo seja o mais fácil, senhor [mc]."

                mc envergonhado "Acho difícil..."

                gar "Pense... se você fosse um mago e dividisse sua alma em sete pedaços, deixaria todos longe de você?"

                mc desconfiado "Hm?"

                gar "Nos vemos em breve, senhor [mc]."

                hide garcom with dissolve

                "Eu tenho a impressão que tudo o que ele disse foi besteira..."

                "Tenho que pensar com calma no que ele disse..."

                "Mas isso ainda não é suficiente. Eu sinto que tô perto, mas preciso saber onde ele vai..."

                "Eu descobri algumas coisas, mas ainda falta uma última peça."

                "O [gar] disse que talvez agora seria o mais fácil... o que ele quer dizer?"

                "Hora de encarnar o detetive!"

            "Quero saber mais sobre a missão da Interpol." if nathan_final2:

                gar "Por qual resposta seu âmago clama?"

                label fabricio_interpol:

                    pass

                menu:
                    "Como a Interpol chegou no Grupo?":


                        gar "Ah, a Interpol... uma organização de envergadura global!"

                        gar "Seus tentáculos se estendem por todos os continentes, combatendo o crime com a tenacidade de um leão e a astúcia de uma raposa!"

                        gar "Seus agentes são como sombras, infiltrando-se nas organizações criminosas, coletando informações, desmantelando seus planos..."

                        gar "Eles são os guardiões invisíveis da ordem mundial, lutando contra as forças do caos que ameaçam a estabilidade global."

                        mc "E como eles descobriram o Grupo? Como eles chegaram até a Capital?"

                        gar "Os fios do destino são longos e complexos, meu caro."

                        gar "As ações do Grupo ecoam por além das fronteiras da Capital, deixando rastros em transações financeiras internacionais."

                        gar "Inclusive em rotas de tráfico de drogas e armas, em esquemas de lavagem de dinheiro..."

                        gar "A Interpol, com sua rede global de informações, conseguiu identificar esses rastros, seguindo-os até a Capital, até o coração do Grupo."

                        gar "A investigação durou anos, envolvendo agentes infiltrados, informantes, escutas telefônicas... uma verdadeira operação de inteligência!"

                        mc "E eu... eu faço parte dessa operação agora?"

                        gar "Sim, senhor [mc]! O senhor se juntou à nossa causa! E, com sua ajuda, desvendaremos os segredos do Grupo e os levaremos à justiça!"

                        gar "Que a força esteja com o senhor!"

                        mc "Caralho..."
                    "A Natasha... ela realmente tá com a gente?":


                        gar "A senhorita Natasha... ela é como uma leoa ferida, meu caro. Forte, majestosa, mas marcada pelas cicatrizes do passado."

                        gar "Sua alma carrega o peso de um fardo cruel, de uma injustiça que a corrói por dentro. Ela busca redenção, anseia por justiça..."

                        gar "Mas a dúvida, como uma sombra, a acompanha em cada passo."

                        mc "Você tá falando do que o prefeito fez com ela?"

                        gar "Sim, senhor [mc]. As ações do prefeito Donatello a feriram profundamente, deixando marcas que o tempo não consegue apagar."

                        gar "A traição, a humilhação, a dor... elas a moldaram, transformando-a em uma guerreira implacável, mas também em uma alma atormentada."

                        mc "Mas... ela está do nosso lado? Podemos confiar nela?"

                        gar "A senhorita Natasha escolheu o caminho da justiça, meu caro."

                        gar "Ela se juntou à nossa causa, de corpo e alma, arriscando tudo para combater o mal que a assola. Sua lealdade é inquestionável."

                        gar "Mas... ainda há uma ferida aberta em seu coração. Uma ferida que só o tempo... e a justiça... poderão curar. Ou seu amor."

                        mc "M-meu amor?!"
                    "Por que você se juntou à Interpol? Qual é a sua história?":


                        gar "Minha história... ah, meu caro [mc]! Ela é como um rio subterrâneo, fluindo por entre camadas de rocha e sedimentos, escondida dos olhos do mundo."

                        gar "Minhas origens... elas se perdem nas brumas do tempo, em um passado distante, envolto em mistérios e sombras."

                        gar "Nasci em uma terra longínqua, sob a gélida vigilância da Ursa Maior, onde os invernos são rigorosos e as noites são longas..."

                        mc "Você... você é russo, né?"

                        gar "Sim, meu caro. Minhas raízes se conectam àquela terra fria e distante."

                        gar "Mas o destino, como um vento implacável, me conduziu para longe, para terras estrangeiras, para uma jornada em busca de... redenção."

                        gar "O passado... ele molda nossas almas, meu caro [mc]. Ele nos marca com cicatrizes invisíveis, que carregamos conosco por toda a vida."

                        gar "As minhas... elas me impulsionaram para o caminho da justiça, para a luta contra a escuridão que se esconde sob a máscara da beleza e do poder."

                        mc "Mas... o que aconteceu? O que te fez deixar a Rússia? O que te fez se juntar à Interpol?"

                        gar "Meu passado... ele me pertence, meu caro. Ele é um fardo que carrego em silêncio."

                        gar "Algumas feridas... algumas feridas são profundas demais para serem reveladas."

                        mc "Hmm... suspeito."

                        gar "Desculpe-me, senhor [mc]. O passado... às vezes ele nos assombra, mesmo nas noites mais alegres."
                    "O que você sabe sobre a história da capital?":


                        gar "Ah, meu caro [mc]! A história da Capital... ela é como um palimpsesto."

                        gar "Uma obra com camadas de tinta sobrepostas, revelando fragmentos de um passado obscuro, de segredos ancestrais, de lutas pelo poder..."

                        mc "Fala direito, Fabrício!"

                        gar "Pois bem, senhor. A Capital, esta cidade que hoje se ergue com a pompa de uma rainha, tem suas raízes em um passado de violência e conspiração."

                        gar "Sua fundação... ela foi marcada por um pacto de sangue entre duas famílias: os Donatello e os Alighieri."

                        mc "Donatello... Alighieri... esses nomes..."

                        gar "Sim, meu caro! Os Donatello, com sua ambição e sede de poder, e os Alighieri, com sua fortuna e influência, uniram forças para dominar estas terras."

                        gar "Eles forjaram um império que se perpetua até os dias de hoje."

                        mc "Mas... como eles conseguiram? Quem os apoiava?"

                        gar "A Cidade Chinesa, com sua sabedoria milenar e suas redes de comércio."

                        gar "E o Distrito, com seus prazeres proibidos e seus segredos obscuros."

                        gar "Eles se juntaram a esse pacto, formando um quarteto de poder que controla os destinos da Capital."

                        menu:
                            "Me explica melhor. Quero mais detalhes dessa história.":


                                gar "Ah, a fundação da Capital! Um evento épico, marcado por um pacto de sangue e um sonho de grandeza!"

                                gar "Era o final do século XIX, o país recém-saído das amarras da monarquia, e a promessa de um novo futuro pairava no ar..."

                                gar "Dois homens, com ambições grandiosas e destinos entrelaçados, chegaram a esta terra inóspita, em busca de fortuna e poder."

                                gar "Giovanni Donatello, um imigrante italiano com a astúcia de Maquiavel e a audácia de César."

                                gar "E Augusto Alighieri, um rico comerciante português e italiano com a visão de um estadista e a fortuna de um rei."

                                mc "Donatello... Alighieri... os nomes se repetem..."

                                gar "Sim, meu caro! Os descendentes desses homens audaciosos herdaram a ambição de seus antepassados, perpetuando o legado de poder e domínio sobre a Capital."

                                gar "Mas voltemos à fundação..."

                                gar "Donatello, com seu carisma e lábia, conseguiu a concessão de terras da Coroa."

                                gar "Enquanto Alighieri, com sua fortuna, financiou a construção dos primeiros edifícios, das primeiras ruas, do primeiro porto."

                                gar "A Capital nascia, como um bebê frágil, sob a sombra da ambição e da cobiça."

                                mc "E a Cidade Chinesa? O Distrito?"

                                gar "Ah, sim! Eles não tardaram a se juntar a este banquete de poder!"

                                gar "Wei Chan, um sábio mestre chinês com a astúcia de Sun Tzu e a paciência de Confúcio, liderou um grupo de imigrantes orientais."

                                gar "Eles se estabeleceram na região que hoje conhecemos como a Cidade Chinesa."

                                gar "Eles trouxeram consigo seus costumes, sua cultura, e seu conhecimento milenar, se tornando uma força econômica e social importante na Capital."

                                gar "Wei Chan fez um acordo com os italianos. Um pedaço de terra em troca de apoio incondicional."

                                mc "E o Distrito?"

                                gar "O Distrito... ah, meu caro! Ele surgiu das sombras, como um fruto proibido."

                                gar "Atraindo aqueles que buscavam prazeres clandestinos e refúgio da moralidade opressora da época."

                                gar "Madame Esmeralda, uma cortesã francesa com a beleza de Cleópatra e a astúcia de Madame de Pompadour, estabeleceu o primeiro bordel da Capital."

                                gar "O local se tornou um centro de poder e influência, atraindo políticos, empresários e artistas em busca de... diversão."

                                mc "Então... desde o início, a Capital foi dominada por esses grupos?"

                                gar "Sim, senhor [mc]. O pacto de sangue entre os Donatello, os Alighieri, a Cidade Chinesa e o Distrito moldou os destinos da Capital."

                                gar "Essas pessoas criaram uma teia de poder que se perpetua até os dias de hoje."

                                gar "Mas... a história não está escrita em pedra, meu caro! E nós... nós podemos mudá-la!"

                                mc "Quero ver..."
                            "É o suficiente sobre história pra mim.":


                                gar "Que assim seja."
                    "Era isso. Até outra hora.":


                        gar "Que a espada da justiça esteja sempre embanhada em nosso coração, inestimado amigo."

                        jump cenario_bar

                jump fabricio_interpol

            "Aquela bebida..." if p1_bebida:

                mc desconfiado "Ei! Aquela bebida que você me deu..."

                gar "O senhor deseja mais?"

                mc bravo "Não!"

                mc bravo "Só quero que você me fale sobre ela..."

                gar "Hmmm..."

                show garcom diabolico
                with dissolve

                gar "Aquela bebida é o estado da arte da manipulação do álcool."

                gar "Você precisa juntar 13 diferentes tipos de bebidas..."

                mc surpreso "TREZE?!"

                gar "E adicionar um ingrediente secreto..."

                mc normal "E que ingrediente é esse?"

                gar "Segredo..."

                mc bravo "Bah!"

                gar "Muito bem. Estarei te esperando quando precisar de mim."

                mc zerado "Quem fala desse jeito?"

                gar "..."

            "Você conhece alguma celebridade?" if garcom_1vez:

                $ garcom_1vez = False

                show garcom confabulando with dissolve

                gar "Eu conheço muitas celebridades, senhor [mc]."

                mc desconfiado "Você ainda se lembra do meu nome?"

                gar "Minha tarefa neste mundo é conhecer e recordar conhecimentos úteis e inúteis, senhor."

                mc zerado "Espero que meu nome seja um dos úteis..."

                gar "..."

                mc normal "Quais celebridades você conhece? Pode me falar algo sobre elas?"

                gar "Eu conheço inúmeras celebridades, mas nem sobre todas posso revelar segredos."

                gar "Por hora, posso falar sobre a [cc], [sc] e [nc]."

                mc desconfiado "Uou. É mais do que eu imaginava."

                gar "Você se contenta com pouco, senhor [mc]."

                mc zerado "..."

                jump bar_garcom

            "Queria notícias sobre uma celebridade." if not garcom_1vez:

                show garcom chamando with dissolve

                gar "Claro, senhor [mc]."

                gar "Sobre quem você quer informações?"

                menu:
                    "[cc]":


                        if priscila_e2 == "nada":

                            gar "A senhorita [c] ainda está na cidade depois de uma reunião para estrelar um filme."

                            mc zerado "Como você sabe do filme?"

                            gar "É minha tarefa neste mundo, senhor [mc]."

                            mc desconfiado "Se você diz."

                            jump bar_garcom

                        elif v6_fim:

                            gar "A senhorita [c] está hospedada no hotel da ilha."

                            gar "Existe um homem estranho que está sempre de olho nela. Um grandão que fica no parque."

                            gar "Eu não gosto nem um pouco dessa situação toda."

                            mc bravo "Nem me fala..."

                            jump bar_garcom
                        else:


                            gar "A senhorita [c] está fora da cidade para fazer campanhas de produtos para adolescentes."

                            gar "Neste exato momento ela deve estar se vestindo de coelhinha, ou gatinha, ou ratinha..."

                            mc zerado "Ok, ok... Eu entendi."

                            jump bar_garcom
                    "[sc]":


                        if sayuri_evento1_check:

                            gar "A senhorita [s] está normalmente treinando no templo próximo à Cidade Chinesa."

                            mc desconfiado "Como você sabe isso? Isso é um segredo que..."

                            gar "Senhor, [mc]. Esse..."

                            mc serio "Entendi. É o seu trabalho."

                            gar "Exatamente."

                            jump bar_garcom

                        elif not sayuri_e2 == "nada":

                            gar "A senhorita [s] está treinando como escrever mensagens no celular."

                            mc surpreso "É simplesmente impossível que você saiba isso!"

                            gar "... Será que eu fui longe demais agora?"

                            mc zerado "..."

                            jump bar_garcom
                        else:


                            gar "No momento não tenho novidades pecisas sobre a senhorita [s]."

                            gar "Volte um outro dia e talvez eu possa te ajudar."

                            "Finalmente as informações desse cara acabaram."

                            jump bar_garcom
                    "[nc]":


                        if nathan_e1 == "nada":

                            gar "O senhor [n] ainda é uma celebridade em nascimento."

                            mc desconfiado "Como assim? Ele é um bebê ainda?"

                            gar "O senhor [n] ainda não é muito conhecido, mas existem paparazzi de olho no potencial dele."

                            gar "Uma jornalista especificamente."

                            mc serio "Hmmm..."

                            jump bar_garcom
                        else:


                            gar "O senhor [n] vem aqui durante a noite de vez em quando."

                            gar "Ele gosta de tomar meu drink especial."

                            if p1_bebida:

                                mc desconfiado "Aquela bebida que deixou a [c] muito louca, né?"

                                gar "Exatamente."

                            if n1_bebida:

                                mc surpreso "Ei! Essa é aquela bebida que eu tomei também."

                                gar "E o senhor apreciou?"

                                mc zerado "Não me lembro de nada depois que tomei ela."

                                gar "Isso pode acontecer às vezes. {size=15}Quase todas as vezes.{/size}"

                                mc "..."

                            jump bar_garcom
            "Nada por enquanto.":


                gar "Muito bem. Estarei te esperando quando precisar de mim."

                mc zerado "Quem fala desse jeito?"

                gar "..."

        jump cenario_bar



    label cenario_trabalho:

        $ estou_na_cidade = False

        if tempo < 2 and sofia_xp == 34:

            $ sofia_xp += 1

            jump sofia_trabalho_evento3

        if tempo < 3:



            if sofia_premium == 1:

                jump sofia_18_2



            if v47_fim and sofia_premium == 0:

                jump sofia_18_1



            if v36_fim and sofia_e5 == "nada":

                jump sofia_evento5



            if v28_fim and dia_sofia and sofia_e4 == "nada":

                jump sofia_evento4

            scene trabalho mesa with Dissolve(1.0)



            if v15_fim and dia_sofia and sofia_e3 == "nada":

                jump sofia_evento3_pre

            if v10_fim and entregou_pauta >= 2 and sofia_e1 == "nada":

                jump sofia_evento1

            if sofia_e1 == "iniciado":

                if dia >= dia_sofia and not sofia_evento_manha:

                    if sofia_e1_count < 3:

                        call sofia_e1_evento from _call_sofia_e1_evento

            if not cassia_nathan_entregou and v4_fim and not nathan_e1 == "nada" and not cassia_ponte:

                jump cassia_ponte

            play sound "audio/som_2_redacao.mp3"

            if cenario_trabalho_1vez:

                $ cenario_trabalho_1vez = False

                "Aqui é a redação da revista. É onde eu trabalho."

                scene trabalho geral with Dissolve(1.0)

                "Como paparazzo, meu trabalho será descobrir furos e informações quentes sobre famosos."

                "No jornalismo nós chamamos essas informações de {b}pauta{/b}."

                "A pauta é a primeira etapa da reportagem. Eu trarei a pauta para o chefe e ele vai distribuir para outros fazerem as matérias."

                "Eu preciso ter sempre uma pauta comigo pra se o chefe me chamar eu ter algo pra entregar pra ele."

                "Tenho que tomar cuidado pra não prejudicar a vida das celebridades que eu mais gosto."

                mc zerado "Por que eu tô narrando as coisas como se tivesse alguém lendo meu pensamento?"

                show black with dissolve

                p rindo "Ser chamado pelo chefe e não ter nenhuma pauta será {b}game over{/b} para você, bebê."

                p "Por isso, preste bastante atenção nas suas escolhas."

                p "E não se esqueça do contrato que VOCÊ fez comigo no começo do jogo. Você é a única pessoa responsável pelas suas escolhas e seu futuro."

                p "Como eu sou uma f-fada bacana... vou te dar duas dicas..."

                p "Primeiro, você não precisa responder as mensagens das pessoas assim que você recebe. Você pode apertar no botão vermelho do celular."

                p "E, mais importante do que isso, caso você se sinta travado no jogo ou não saiba onde ir, não esqueça de falar com outros jogadores!"

                p "No MENU tem o link para grupos do WhatsApp, Face, Insta e outros locais onde você pode pedir ajuda."

                p "Boa sorte e não venha reclamar comigo se o [mc] for despedido!"

                hide black with dissolve

                "Bom... sem esse emprego eu não tenho grana pra me manter aqui. Então melhor eu me esforçar e me tornar um caçador de celebridades!"

                mc zerado "Que merda..."

                scene trabalho mesa with Dissolve(1.0)

            if not v15_fim:

                $ randevent = renpy.random.randint(1,4)

                if randevent == 1:

                    mc zerado "Consigo ouvir todos os {i}tec tec tec{/i}..."

                elif randevent == 2:

                    mc angustiado "Dá pra ouvir o chefe gritando com alguém daqui..."
                else:


                    pass
            else:


                $ randevent = renpy.random.randint(1,4)

                if randevent == 1:

                    mc desconfiado "Parece que a [w] tá dando bronca em alguém de novo..."

                elif randevent == 2:

                    mc normal "Hoje a redação tá tranquila..."
                else:


                    pass

            menu:

                "Falar com a Cássia sobre a filha dela" if sofia_final2_pre and not sofia_final2:

                    if banho_evento >= 20:

                        jump sofia_final2_cassia
                    else:


                        "Eu tenho que {b}descobrir sobre a filha da Cássia{/b}."

                        "Ela existe mesmo? Onde ela pode estar?"

                        play sound notificacao

                        scene black with dissolve

                        p rindo "Fala, meu lindo!"

                        p "Quer uma dica? Não? Ahh! Quanto orgulho, hein?!"

                        p "Vou te dar uma dica mesmo assim porque eu que mando nessa porra!"

                        p "Você vai ter que ir na {b}Cidade Chinesa{/b} e tomar banhos de Saúde e Beleza com a chinesa doidinha lá!"

                        p "Para fazer este final, SERÁ necessário descobrir a verdade. E a verdade está lá."

                        p "Só depois de finalizar tudo lá no banho, volte e {b}fale com a Cássia na redação{/b}."

                        menu:
                            "Terminar os banhos na Cidade Chinesa e falar com a Cássia depois, ok.":


                                pass
                            "Eu faço o que eu quero, maldita.":


                                pass

                        p "Hehe! Boa sorte!"

                        jump cenario_trabalho

                "Falar com o chefe" if not chefe_saiu:

                    if sofia_final2:

                        $ chefe_saiu = True

                        "Caralho..."

                        "Esqueci que o chefe saiu em desgraça..."

                        "Vai dar até saudades desse velho ranzinza em cobrando pauta."

                        if pautas_liberado:

                            "Eu aceitei ser cachorrinho da Cássia, então tô livre das pautas!"

                            "Nem acredito... não vou precisar me preocupar mais com essa merda e ainda posso trepar com ela."

                            "Me dei bem ou não?"
                        else:


                            "Eu não aceitei ser cachorrinho dela. Então ela vai me cobrar o DOBRO de pautas agora!"

                            "Merda... MERDA!"

                            "Pelo menos eu mantenho minha dignidade. Foi uma boa escolha... eu acho."

                        "Vamos ver como vai ser a redação agora."

                        "As coisas vão mudar bastante aqui."

                        scene black with dissolve

                        jump cenario_trabalho

                    "Tenho que falar com o idiota..."

                    jump trabalho_chefe

                "Falar com a [jc]" if cassia_evento:

                    if sofia_final2:

                        "Agora ela é a chefe... a porta dela tá sempre fechada."

                        "Ou ela tá comendo a Renata ou o Ronaldo tá comendo ela."

                        "E a Kaira? Como será que ela tá?"

                        jump cenario_trabalho
                    else:


                        jump trabalho_cassia

                "Falar com a [w]" if sofia_e1 != "nada":

                    if sofia_final2:

                        "Agora a Sofia tá recepção..."

                        scene black with dissolve

                        scene 9243 with dissolve

                        mc "Oi..."

                        w "Oi. Curtindo ser jornalista pra aquela vaca?"

                        mc "Sofia..."

                        menu:
                            "Como tão as coisas com a Cássia?":


                                scene black with dissolve

                                scene ani45 with dissolve

                                w "Aquela puta fica me apalpando, me apertando..."

                                w "Ela manda e eu sou obrigada a obedecer, oferecer meu corpo pra ela fazer o que quiser."

                                w "Eu não... aguento mais isso, [mc]. Essa mulher... ela vai me deixar doida assim."

                                mc "S-sofia... aguenta."

                                w "Hmm..."

                                "Será que eu consigo pegar algo assim acontecendo na redação se eu vir aqui na hora certa?"
                            "Sofia, vai dar tudo certo. Aguenta.":


                                pass

                        if sofia_namoro:

                            mc "Eu sei que a gente não namora mais... mas aguenta. Eu não vou perder o que eu sinto por você."

                        scene black with dissolve

                        scene 9241 with dissolve

                        mc "Eu tô aqui por você, tá? Pode contar comigo."

                        w "Sei... você foi o culpado de tudo isso, [mc]. Saiba disso. Eu nuca vou esquecer."

                        mc "..."

                        "Vale a pena isso pra evitar que o Grupo tenha a revista? E se eu entregasse tudo pra eles?"

                        scene black with dissolve

                        jump cenario_trabalho
                    else:


                        if dia < dia_sofia:

                            "Melhor eu não incomodar mais ela hoje."

                            jump cenario_trabalho

                        jump trabalho_sofia
                "Ir embora":


                    "Não tenho nada para fazer aqui agora."

                    $ estou_na_cidade = True

                    jump call_cidade
        else:


            scene trabalho geral with Dissolve(1.0)

            mc zerado "O que eu tô fazendo aqui? Só tem o segurança..."

            mc bravo "E ainda nem deixam usar o computador..."

            mc triste "Deixa eu ir embora e voltar amanhã cedo."

            if not v15_fim and sofia_e1_count == 2 and dia >= dia_sofia:

                jump sofia_e1_conversa

            jump call_cidade

    label trabalho_chefe:

        scene trabalho chefe_porta with Dissolve(1.0)

        mc triste "Chefe..."

        b "PODE ENTRAR!"

        scene trabalho chefe with Dissolve(1.0)

        stop sound

        mc triste "..."

        show chefe emburrado with dissolve

        if cenario_trabalho_1vez_chefe:

            $ cenario_trabalho_1vez_chefe = False

            b "Você lembra do nosso acordo, não é mesmo?!"

            b "Traga algo sobre a [c] até o dia acabar ou vai ser DESPEDIDO!"

            mc triste "Você vai estar aqui durante a noite?"

            show chefe irritado
            with dissolve

            b "Claro que não!"

            b "Como se eu fosse aguentar ficar três períodos aguentando gente como você!"

            mc zerado "..."

            mc triste "Aliás, a pauta precisa ser sobre a [c]?"

            show chefe surpreso
            with dissolve

            b "QUÊ!? Está dizendo que você conseguiria qualquer coisa sobre outra celebridade?!"

            mc desculpa "Talvez..."

            b "Hm... Se você acha que consegue... Qualquer pauta será mais útil do que você faz ultimamente."

            mc zerado "..."

            show chefe irritado
            with dissolve

            b "MAS não ache que é só isso!"

            b "Quero que você me traga uma nova pauta a cada {b}SETE dias{/b}."

            b "Se você falhar... RUA! GAME OVER!"

            b "E o que você veio fazer aqui hoje?"

            mc angustiado "..."

            show chefe emburrado with dissolve

        b "O que é?!"

        menu:

            "O que você sabe sobre o Cassino?" if natasha_e2 == "iniciado":

                $ natasha_e2 = "chefe"

                mc desculpa "Desculpa incomodar, mas você pode me falar um pouco sobre o Cassino do Barão?"

                b "Quê?"

                mc normal "Queria saber um pouco mais sobre ele de alguém que conhece a ilha muito mais que eu."

                b "..."

                b "Por que o interesse nisso agora, jovem?"

                menu:
                    "Tem uma moça que eu gosto...":


                        mc envergonhado "É que tem uma garota que e-"

                        show chefe irritado with hpunch

                        b "VOCÊ É DOIDO, MOLEQUE?! OCUPANDO MEU TEMPO POR UMA RAPARIGA QUALQUER?!"

                        mc angustiado "De-desculpa, senhor! Era brincadeira!"

                        b "Isso é algo que você tem que entender... Mulher só vai arranjar problema pra sua vida!"

                        if sofia_e1 != "nada":

                            mc desconfiado "Sei... mas o senhor é casado, não é? Tem a Sofia..."

                            b "E daí?! Por que você acha que a menina só chegou agora?!"

                            b "Eu não aguentei a mãe dela por muito tempo!"

                        b "Mulheres só servem pra pedir dinheiro e para nós nos aliviarmos quando precisamos."

                        show chefe emburrado with dissolve

                        b "Elas ficam com essa história de emoção, de sentimentos... bah! Coisa besta!"

                        b "Se agir pelo coração fosse útil, Deus não teria inventado a cabeça pra pensar."

                        mc envergonhado "..."

                        b "O coração serve pra mandar sangue pra cabeça, ou seja, não passa de um suporte. Quem vive pelo coração são seres tristes."

                        mc desculpa "..."
                    "Pode ser que eu encontre uma pauta...":


                        mc normal "Posso estar no caminho de uma pauta..."

                        show chefe surpreso with dissolve

                        b "Uma pauta?!"

                        mc desconfiado "Que foi, é meu trabalho conseguir pautas, certo? É pra isso que você me paga."

                        show chefe emburrado with dissolve

                        b "Por que você está falando assim comigo?!"

                        mc angustiado "D-desculpa! É só qu-"

                        b "É óbvio que é para isso que você está aqui, mas vocês trabalham tão pouco que até esqueço. Por isso a surpresa."

                        mc zerado "..."

                        b "Não sei que tipo de pauta você espera conseguir naquele lugar."

                        mc desconfiado "Por que? O cassino é um lugar tão importante pra ilha. Devem ter pautas lá."

                b "Enfim... Talvez eu possa te falar um pouco sobre o que eu sei."

                mc surpreso "Sério?!"

                b "E, pelo amor de Deus, pare de gritar."

                mc envergonhado "Ok..."

                hide chefe with dissolve

                b "Venha aqui."

                scene chefe_sentado_bravo with Dissolve(1.0)

                b "Aquele é um ninho de vespas, garoto."

                mc desconfiado "Como assim?"

                b "O que acontece no Cassino do Barão é o que move a ilha onde você vive."

                mc "Nossa ilha?"

                b "Presta atenção!"

                mc preocupado "O-ok..."

                b "Tudo o que acontece aqui gira em torno do cassino e do seu hotel. Pense comigo..."

                b "Os famosos se hospedagem no hotel do cassino, comem, compram e se divertem no cassino."

                b "Eles possuem uma cantora que SÓ se apresenta lá. E essa é só uma das exclusividades do local."

                mc desculpa "A [d]..."

                b "Isso, mas não apenas ela. Repare nas garotas que trabalham lá. São todas incrivelmente lindas e simpáticas."

                b "Um mundo criado para divertir e fazer você se esquecer do resto. Eles querem te manter lá o máximo de tempo possível."

                b "Eu já ouvi falarem que existem pessoas que vivem lá que nunca deixaram o cassino sequer uma vez depois que chegaram."

                mc surpreso "Como assim?!"

                b "Pense... pelo menos uma vez na vida! Você é rico! Sua vida é um tédio! Te dão um lugar onde você pode perder seu tempo jogando."

                b "Trazer um pouco de emoção e ainda por cima rodear você de mulheres que agem como você fosse um príncipe!"

                b "Quem recusaria isso se pudesse viver? Comida boa, mulheres, emoção, entretenimento e um senso de superioridade..."

                mc concentrando "Parece bom demais..."

                b "Deve ser mesmo..."

                mc tarado "O senhor deve curtir muito..."

                b "Tá louco, moleque?! Olha pra minha cara de quem vai em um lugar assim!"

                mc desconfiado "P-por que não?"

                scene chefe_sentado_close with Dissolve(1.0)

                b "Eu não tenho que falar da minha vida, principalmente para meus empregados."

                mc zerado "..."

                b "Agora escute. O Barão é, sem dúvida, o maior beneficíário desse paraíso. Mas ele não é o único."

                mc desconfiado "..."

                b "Dinheiro e poder andam juntos, menino. Nunca se esqueça disso."

                b "É preciso ter dinheiro para chegar ao poder, e dinheiro sem poder não dura."

                b "Uma mão lava a outra no pequeno círculo da capital, entendeu?"

                "O chefe parece saber muito sobre isso... será que ele também..."

                b "Ei! Preste atenção!"

                mc desculpa "Desculpa..."

                b "Enfim... era isso que você precisava saber?"

                mc normal "Obrigado. Você sabe algo sobre o Barão também?"

                b "Não..."

                "Que pena..."

                b "Bem... o Barão é o homem mais rico da capital. Algumas pessoas dizem que ele criou a ilha."

                mc desconfiado "Como se cria uma ilha?"

                b "Não nesse sentido, idiota."

                mc envergonhado "Ah... desculpa. Quando ele chegou, tudo aqui era mato?"

                b "Claro que não. Ele é relativamente jovem."

                mc desconfiado "Sério?"

                b "Você não conhece ele?"

                mc envergonhado "Não..."

                b "E ainda se diz paparazzo. Que vergonha, garoto..."

                mc zerado "..."

                b "Mesmo sendo figura pública e tendo o cassino, ele não vive aqui. Mas eu não sei mais nada sobre o homem, pouco me importa o que ele faz."

                "Isso que ele é o editor-chefe de uma revista semanal que fala sobre famosos..."

                b "Se você quiser saber mais, vai ter que ser jornalista uma vez na vida e entrevistar pessoas que convivem com ele."

                mc envergonhado "P-pode deixar... vou fazer isso. Obrigado por me ajudar."

                b "Garoto..."

                mc desconfiado "Hm?"

                b "Lembre-se... Temos que pensar muito bem no buraco que a gente está se metendo."

                b "Alguns podem te chamar de covarde, outros vão falar que você é aliado, mas eu vejo como cautela."

                b "Comprar briga com as pessoas erradas é a forma mais fácil de estragar sua vida sem necessidade."

                mc envergonhado "Acho que eu entendi..."

                b "..."

                mc "Obrigado...?"

                scene chefe_sentado_bravo with hpunch

                b "Agora vai trabalhar logo! E se você ocupou todo esse meu tempo e não me trouxer algo pra revista, é OLHO DA RUA pra você!"

                mc angustiado "Tá bom! Tchau!"

                scene trabalho chefe_porta with Dissolve(1.0)

                "..."

                "O chefe acabou me passando algumas coisas interessantes... mas agora tenho que falar com pessoas mais próximas do Barão."

                "Não sei se é dar bandeira demais... mas não consigo pensar em outra pessoa que não seja {b}ela{/b}."

                "Espero que ela esteja lá hoje à noite."

                jump cenario_trabalho
            "Tenho uma pauta para a revista!":


                "O que vou publicar na revista?"

                label entregar_pauta:

                    menu:

                        "A [cc] vai estrelar no cinema." if priscila_p1:

                            $ pautas -= 1
                            $ priscila_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ priscila_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_priscila_p1

                        "O templo da cidade é o local secreto da [sc]." if sayuri_p1:

                            $ pautas -= 1
                            $ sayuri_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ sayuri_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_sayuri_p1

                        "Descobri mais informações sobre o filme da [cc]." if priscila_p2 and not priscila_p1:

                            $ pautas -= 1
                            $ priscila_p2 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ priscila_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_priscila_p2

                        "O [nc] fechou seu primeiro contrato." if nathan_p1:

                            $ pautas -= 1
                            $ nathan_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ nathan_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_nathan_p1

                        "A [sc] é virgem e nunca teve um namorado." if sayuri_p2:

                            $ pautas -= 1
                            $ sayuri_p2 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ sayuri_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_sayuri_p2

                        "A [dc] fará um grande concerto pro seu novo single." if diana_p1:

                            $ pautas -= 1
                            $ diana_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ diana_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_diana_p1

                        "Pode usar a pauta que a [j] deixou em meu nome." if favor_cassia_pauta:

                            $ pautas -= 1
                            $ favor_cassia_pauta = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ entregou_pauta += 1

                            mc charmoso "A [j] deixou aqui uma pauta que eu encontrei..."

                            b "Ah, eu sei! Vamos usá-la."

                            b "Dessa vez você se safou..."

                            mc tarado "..."

                            b "Agora dá o fora, moleque!"

                            jump cenario_trabalho

                        "Descobri um podre sobre o diretor do Banco Central." if celeste_p1:

                            $ pautas -= 1
                            $ celeste_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ celeste_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_celeste_p1

                        "Uma das cabeças do Distrito tá envolvida no tráfico de pessoas." if caio_p1:

                            $ pautas -= 1
                            $ caio_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ distrito_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_caio_p1

                        "Tenho informações sobre a maga [qui]." if fabricio_p1:

                            $ pautas -= 1
                            $ fabricio_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ fabricio_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_fabricio_p1

                        "A TKF está na etapa final de produzir um robô humanóide." if tkf_p1:

                            $ pautas -= 1
                            $ tkf_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ tkf_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_tkf_p1

                        "A obra do novo aeroporto foi superfaturada." if hacker_p1:

                            $ pautas -= 1
                            $ hacker_p1 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ hacker_atencao += 1
                            $ entregou_pauta += 1
                            jump cena_hacker_p1

                        "{b}O diretor [diretor] abusa da atriz [cc] (continua a história){/b}" if priscila_p3:

                            $ pautas -= 1
                            $ priscila_p3 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ priscila_atencao += 1
                            $ entregou_pauta += 1
                            jump priscila_evento7_parte2

                        "Eu descobri que o cassino compra e vende pessoas." if diana_p2:

                            $ pautas -= 1
                            $ diana_p2 = False
                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ diana_atencao += 1
                            $ entregou_pauta += 1

                            jump cena_diana_p2

                        "{b}Tenho esta pauta que a cantora Diana te mandou (continua a história){/b}" if diana_e7 == "pre":

                            $ foi_despedido = False
                            $ iconchefe = 0
                            $ hora_pauta = False
                            $ entregou_pauta += 1
                            $ diana_e7 = "pauta"

                            jump cena_diana_p3

                        "Não tenho nada pra publicar..." if not foi_despedido:

                            jump sem_pauta
            "Não é nada... por enquanto...":


                label sem_pauta:

                    mc angustiado "Foi um engano! Não é nada. Me desculpe..."

                    show chefe irritado with dissolve

                    b "VOCÊ É DOENTE?!"

                    b "NÃO É PORQUE VOCÊ VIVE COMO UM VAGABUNDO QUE A GENTE TAMBÉM VIVE!"

                    mc angustiado "..."

                    b "SAIA DAQUI!"

                    "Droga... Odeio esse velho."

                    "..."

                    jump cenario_trabalho



    label cena_hacker_p1:

        mc desculpa "Eu tenho uma informação meio bombástica..."

        b "Hm?"

        mc serio "Eu tenho informações do NBC mostrando que a obra do novo aeroporto da ilha foi superfaturada."

        show chefe surpreso with vpunch

        b "QUÊ?!"

        mc "Isso aí. Uma fonte me passou dados que comprovam que o Donatello viciou a licitação pra que a obra custasse mais."

        mc "E o diretor financeiro do NBC, o [gi], sabia de tudo e validou diretamente. As transações foram validadas pelo código pessoal dele."

        b "Menino..."

        scene chefe_sentado_bravo with Dissolve(1.5)

        b "Isso é coisa muito séria."

        mc desculpa "Eu sei chefe, mas tá tudo aí. Eu acompanhei e chequei tudo. Se quiser, posso ver com a [w] também."

        b "Não! Espera... deixa eu pensar..."

        b "O Donatello vai vir com tudo pra cima se a gente publicar isso. Eu preciso checar isso melhor."

        b "E vou ter que encontrar alguém que tenha bolas pra checar e escrever essa matéria. A pessoa vai ter que entrevistar o [gi] e o prefeito."

        mc desconfiado "Não parece algo simples..."

        b "Por mais irônico que pareça... as duas pessoas com habilidade e bolas aqui pra fazer isso são a [j] e a minha filha."

        b "Deixe tudo comigo e assim que eu ajeitar tudo eu te aviso. E parabéns pelo trabalho."

        mc surpreso "V-valeu..."

        scene black with dissolve

        mc "Tá tudo aqui."

        b "Certo. Deixa comigo agora. Até outra hora."


        $ hacker_p1 = False
        $ foi_despedido = False
        $ iconchefe = 0
        $ hora_pauta = False



        mc "A-até..."

        jump cenario_trabalho

    label cena_tkf_p1:

        mc charmoso "Eu tenho uma informação incrível sobre a TKF."

        b "Aquela empresa idiota de tecnologia?"

        mc "Essa mesma. Eles estão perto de produzir o que eles chamam de primeiro humano sintético do mundo."

        b "Como é?"

        mc envergonhado "Em outras palavras, eles vão lançar um robô com inteligência artificial que se parece mais um humano do que um robô."

        show chefe irritado with hpunch

        b "Você acha que eu sou idiota, pirralho?!"

        b "Vim falar de uma besteira dessas pra mim essa hora do dia!"

        mc preocupado "É verdade! Eu conversei com uma das cientistas, a [se]. Ela me entregou documentos com especificações sobre o projeto."

        mc normal "Eu já dei uma olhada e tenho certeza que a notícia é verdadeira, pois eu mesmo vi."

        b "Dá aqui!"

        mc "Toma."

        hide chefe with dissolve

        b "Hmmm..."

        show chefe satisfeito with dissolve

        b "Isso é notícia de primeira, meu filho. Isso aqui inclusive, está acima do que nossa revista costuma publicar."

        b "Talvez... uma das maiores notícias que eu já coloquei as mãos na vida."

        mc normal "Que legal."

        b "Essa empresa, TKF, é doente."

        mc desconfiado "Hm?"

        b "Mexer com essas coisas... inteligência artificial... humanos sintéticos. Isso não é normal."

        mc envergonhado "O senhor não concoroda?"

        show chefe emburrado with dissolve

        b "Claro que não."

        "Nem sei por que pergunto..."

        b "É impossível parar o avanço da tecnologia. Mas quando os humanos começam a brincar de Deus, as coisas não acabam bem."

        mc zerado "Será que o senhor não tá vendo muito filme, não?"

        show chefe irritado with hpunch

        b "Claro que não, IDIOTA!"

        mc envergonhado "..."

        b "Agora dê o fora e vamos trabalhar nessa pauta. Assim que a matéria estiver pronta, vou te chamar."

        mc surpreso "Me chamar?!"

        b "Você é um imbecil, mas a pauta é sua. Acho que você merece dar uma olhada."

        mc charmoso "O-ok."

        b "Agora sai daqui!"

        mc zerado "..."

        jump cenario_trabalho

    label cena_fabricio_p1:

        mc charmoso "Eu descobri que a mágica [qui] vem para a ilha e visita o bar aqui perto toda noite de lua cheia."

        show chefe surpreso with dissolve

        b "[qui]?!"

        b "Você tem certeza disso?!"

        mc "Sim. Tenho uma fonte confiável que viu ela no bar várias vezes, sempre durante a lua cheia."

        show chefe empolgado with dissolve

        b "Isso é demais, filho! Meus parabéns!"

        b "[qui] é um dos maiores mistérios de nosso país. Ninguém sabe nada sobre ela."

        b "Ela faz apresentações incríveis que não podem ser explicadas pela ciência e sempre desaparece após o show."

        b "Ninguém sabe onde ela está. Dizem que nem mesmo a polícia ou o governo sabem as reais informações sobre ela."

        b "Essa pauta vai nos trazer muito dinheiro!"

        mc charmoso "Que bom que você ficou satisfeito chefe."

        show chefe irritado with hpunch

        b "Que merda de sorrisinho é esse?!"

        mc preocupado "Não! Eu-"

        b "Vai fazer seu trabalho! Quero mais informações sobre ela! Vai!"

        mc angustiado "Si-sim, senhor!"

        hide chefe with dissolve

        "Esse cara nunca fica satisfeito? Velho maldito."

        jump cenario_trabalho

    label cena_caio_p1:

        mc desculpa "Eu tenho um dossiê que prova que uma das cabeças do Distrito tá envolvida com tráfico de pessoas."

        show chefe surpreso with dissolve

        b "Como?! Repete..."

        mc "A Madame Nora, uma das resp-"

        show chefe irritado with dissolve

        b "Moleque! Você tem noção do que você tá falando?!"

        b "Isso não é coisa que se diga assim!"

        mc preocupado "Mas eu tenho pro-"

        b "Não me interessa se você tem provas!"

        b "Me dá tudo aqui e pica a mula! E não abre a boca sobre isso pra ninguém!"

        mc angustiado "..."

        hide chefe with dissolve

        "Por que ele ficou assim?"

        "Deixa eu sair daqui antes que ele literalmente me chute pra fora."

        jump cenario_trabalho



    label cena_priscila_p1:

        mc charmoso "Eu descobri que a [c] vai estrelar um filme!"

        show chefe surpreso with dissolve

        mc charmoso "Ela acabou de fechar o contrato. É algo que só ela, a assessora e os contratantes sabem..."

        b "Como você descobriu isso?!"

        mc normal "Nós conversamos no bar e eu consegui ter acesso ao celular dela."

        show chefe empolgado
        with dissolve

        b "Muito bem, meu filho!"

        b "Eu sabia que você tinha potencial!"

        b "Essa notícia é de capa! Vamos pesquisar sobre isso. Vamos fuçar a vida dela até conseguir todas as informações necessárias."

        b "E você também! Me traga mais informações sobre isso e com certeza você vai continuar ganhando seu salário de merda."

        mc zerado "..."

        b "Quem sabe até um pequeno aumento!"

        mc feliz "..."

        mc normal "Ok, chefe! Ficarei de olho!"

        show chefe irritado
        with dissolve

        b "E agora saia da minha sala que eu tenho que trabalhar!"

        mc triste "..."

        jump cenario_trabalho

    label cena_priscila_p2:

        mc serio "Consegui mais informações sobre o filme da [cc]."

        show chefe surpreso with dissolve

        b "Não foi justamente você que descobriu sobre isso outro dia? Já conseguiu mais informações?"

        mc charmoso "Sim. Primeiro que o diretor do filme será o famoso [diretor]."

        mc serio "E, mais incrível que isso, será o filme mais caro do cinema nacional."

        show chefe empolgado with dissolve

        b "Muito bem, meu filho!"

        b "Isso é matéria de capa! Vamos colocar uma foto dela seminua com uma insinuação bem cabeluda."

        mc triste "..."

        b "Imagina o que ela teve que fazer pra conseguir esse papel!"

        mc bravo "Quê?"

        show chefe satisfeito with dissolve

        b "Você acha que essas meninas ganham esse tipo de papel do nada?"

        b "Que talento e esforço são as coisas que mais importam?"

        mc bravo "..."

        b "Não seja ingênuo, filho. Elas precisam se entregar de alma e {b}corpo{/b}."

        b "Se você conseguir algo que prove esse tipo de coisa eu até te daria um aumento, sabia?"

        mc bravo "Não sei se quero provar esse tipo de coisa..."

        b "Pense que você estaria fazendo um favor a ela revelando esse tipo de coisa para o mundo."

        mc desculpa "Acho que já vou indo, chefe. Não estou me sentindo muito bem."

        b "Excelente ideia, filho. Vá fazer algo de útil."

        scene trabalho chefe_porta with Dissolve(1.0)

        "Não é possível que isso seja verdade. Isso é coisa de filme."

        "Não quero pensar que a [c] teve que fazer algo desse tipo para conseguir o papel."

        "Seria triste demais..."

        jump cenario_trabalho



    label cena_sayuri_p1:

        mc charmoso "Eu descobri que o templo da cidade é o local secreto de treino da [sc]!"

        show chefe surpreso
        with dissolve

        b "Isso é algo que ninguém sabe, meu filho!"

        mc normal "Eu consegui essa informação lendo uma troca de mensagens entre a [s] e a [c]."

        mc normal "A [sc] pedia para que a [c] não falasse do templo para ninguém."

        mc normal "E pelo jeito dela era um pedido que ela fazia frequentemente. Ou seja, deve ser um local..."

        show chefe empolgado
        with dissolve

        b "... Um local que ela visita com frequência!"

        mc bravo "Isso!"

        b "Isso é incrível!"

        b "Vamos enviar nossos papparazi para lá e descobrir tudo que pudermos!"

        b "Isso é matéria de capa!"

        b "Você também tem o direito de participar. Se conseguir qualquer informação adicional falando com ela, traga!"

        mc normal "Ok, chefe! Ficarei de olho!"

        show chefe irritado
        with dissolve

        b "E agora saia da minha sala que eu tenho que trabalhar!"

        mc triste "..."

        jump cenario_trabalho

    label cena_sayuri_p2:

        mc desculpa "Eu descobri que a [sc], além de ser virgem, nunca teve namorado e nem beijou."

        show chefe surpreso with dissolve

        b "Mas ela não tem 25 anos?!"

        mc envergonhado "Por isso que a pauta é ainda mais incrível..."

        b "Você tem razão, filho!"

        show chefe empolgado with dissolve

        b "Normalmente o público gosta mais de coisas obscuras, mas isso também vai servir!"

        b "Já consigo imaginar metade das pessoas duvidando e a outra metade chamando ela de encalhada."

        b "Você fez um excelente trabalho novamente. Meus parabéns!"

        mc surpreso "É a primeira vez que você me dá os parabéns, chefe!"

        b "..."

        show chefe irritado with dissolve

        b "O tempo de passar a mão na cabecinha acabou!"

        b "Você não faz mais que o seu trabalho! E agora dá o fora que eu tenho que publicar isso!"

        mc zerado "..."

        jump cenario_trabalho



    label cena_nathan_p1:

        mc serio "O modelo [nc] fechou um contrato com a Blergh! pra ser o principal garoto propaganda da marca."

        show chefe surpreso with dissolve

        b "Esse tal de [n] não é o rapaz que a [j] tá investigando?"

        mc "Esse mesmo."

        b "E você conseguiu essa informação antes dela?"

        mc normal "Aparentemente sim, chefe."

        show chefe empolgado with dissolve

        b "Você realmente leva jeito pra coisa, filho! Quem iria imaginar..."

        mc normal "Obrigado chefe."

        show chefe emburrado with dissolve

        b "Agora desembucha!"

        mc serio "..."

        mc "Ele acertou um contrato baseado na fama que ele trouxer. Então ele precisa da gente também."

        show chefe empolgado with dissolve

        b "Isso é muito bom pra gente, filho. Quer dizer que temos ele na nossa mão."

        mc desculpa "..."

        b "Vou mandar pesquisarem sobre esse contrato com a Blergh! e se você descobrir mais coisas, me avise."

        mc serio "Pode deixar. Vou continuar fazendo meu trabalho."

        b "Muito bem."

        show chefe irritado with dissolve

        b "E agora saia da minha sala que eu tenho que trabalhar!"

        "Ele continua me tratando igual..."

        jump cenario_trabalho

    label cena_diana_p1:

        mc serio "A cantora [dc] já gravou seu novo single e está preparando um grande concerto para o lançamento da música."

        mc charmoso "Várias celebridades estarão no Cassino no dia pra participar do evento."

        show chefe surpreso with dissolve

        b "Essa [d] é aquela do Cassino. Eu já vi um show dela. Essa é uma informação muito quente, rapaz!"

        b "Você está se saindo melhor do que eu esperava como paparazzo!"

        mc feliz "Muito obrigado, chefe."

        show chefe empolgado with dissolve

        b "Você não está fazendo mais que seu trabalho. Mas quando a gente não espera nada de alguém, qualquer coisa vale!"

        mc zerado "..."

        b "Se você conseguir mais informações sobre ela, não deixe de trazer pra mim."

        mc serio "Pode deixar, chefe. Vou ficar de olho."

        show chefe irritado with dissolve

        b "E agora sai daqui que esse farsa de eu parecer feliz já me cansou."

        mc triste "Mas..."

        b "Dá o fora!"

        hide chefe with dissolve

        "Esse velho maldito..."

        "..."

        jump cenario_trabalho

    label cena_diana_p2:

        mc serio "A cantora [dc] revelou pra mim que o Cassio do Barão tá traficando pessoas. Ou seja, vendendo e comprando gente."

        show chefe surpreso with dissolve

        b "Isso é um absurdo, garoto! Como ela pode saber isso?!"

        mc "A [d] conhece o Barão de perto. Eu me encontrei com os dois em um bar muito suspeito e ela me deu a informação depois que ele saiu."

        b "Por que eu acreditaria nessa mulher?"

        mc "Ela deixou esse depoimento. Ela mesma disse que precisaria de mais investigação, mas isso deve ser o suficiente pra iniciar algo."

        show chefe irritado with dissolve

        b "Dá aqui isso aqui. Eu vou ouvir. Se for merda e você tiver querendo me foder, você vai pra rua, ouviu?!"

        mc "Eu tenho certeza que não é. A [d] é uma mulher com informações privilegiadas no cassino."

        b "Cada uma que aparece..."

        b "Qualquer coisa eu te aviso! Agora dá o fora que eu cansei de olhar pra sua cara de fuinha!"

        hide chefe with dissolve

        "Só porque eu achei que ele tava melhorando..."

        "Pelo menos ganhei mais um tempo aqui na revista. Vai demorar pra ele me pedir outra paura. Valeu mesmo, [d]..."

        "..."

        jump cenario_trabalho

    label cena_diana_p3:

        mc "A Diana te mandou este envelope. É pra ter uma pauta aqui dentro."

        b "Hmm... você fazendo seu trabalho? Coisa rara."

        mc "Eu sempre faço meu trabalho."

        b "Me dá isso aqui."

        hide chefe with dissolve

        b "Uhumm... Hmm... ok."

        menu:
            "Posso saber o que é?":


                b "Calado. Isso aqui não é pro seu bico... devo tá lendo algo errado."
            "...":


                pass

        b "Não é possível..."

        mc "Hm?"

        show chefe emburrado with dissolve

        b "Tem certeza que isso é confiável?"

        mc "Com certeza. Ela me deu em mãos, lá no quarto dela no Cassino."

        show chefe surpreso with dissolve

        b "N-no quarto dela?"

        b "Posso saber o que o senhor fazia no quarto de uma cantora como a Diana?"

        menu:

            "Bem... a gente tá namorando..." if diana_namoro:

                b "Tá falando sério, moleque?! Não tá inventando pra cima de mim, não, né?!"

                mc "É verdade..."

                b "Quem diria..."
            "Ela que me chamou.":


                b "Ela?"

                mc "Sim... eu... acabei virando um confidente dela."

        b "Hmf... será que você finalmente aprendeu alguma coisa?"

        b "Conhecendo as celebridades, se tornando amigo delas... até ficando com elas se elas quiserem."

        b "E retornando com algo exclusivo como isto."

        show chefe emburrado with dissolve

        b "Realmente parece que eu consegui te ensinar alguma coisa."

        menu:
            "Você não me ensinou nada. Eu aprendi ralando.":


                b "É isso que você pensa?!"

                mc "É isso que eu tenho certeza!"
            "Obrigado. É a primeira vez que o senhor fala algo bom de mim.":


                b "Eu falaria mais, se você fizesse por merecer."

                mc "Claro... tava bom demais pra ser verdade..."

        show chefe irritado with hpunch

        b "A vida não é fácil, moleque!"

        b "Quer algo na vida?! Você precisa correr atrás!"

        b "Você tem que me agradecer de joelhos por eu não ter te mandado embora quando acabou o período de experiência!"

        mc "Mas o senhor ia mandar! Se não fosse a Priscila Fontinelli!"

        b "Óbvio! Você não tinha trazido um NADA pra mim!"

        mc "Mas eu tava tentando! Eu era recém-formado!"

        b "Eu te dei a chance de realizar um bom trabalho! E você foi péssimo até hoje!"

        b "Agora que começou a aparecer algum resultado... você já tá querendo ganhar um troféu?! Por fazer o que você ganha pra fazer?!"

        b "Se tem algo que eu te ensinei e vou continuar te ensinando, é que só ralando essa bunda branca que você chega em algum lugar!"

        b "A vida é assim! A gente se fode todo dia e toda noite! E quem sabe um dia a gente dá uma risada."

        b "Aproveita que você não fodeu ela completamente ainda e tenta fazer as coisas direitos."

        menu:
            "Como que um 'parabéns' virou esse sermão?":


                pass

        b "CULPA SUA!"

        mc "Se já acabou, eu vou dando o fora."

        b "Acabei porcaria nenhuma."

        show chefe emburrado with dissolve

        b "Ela fala aqui que você é o único da nossa revista que vai poder cobrir o evento."

        mc "Então vai ser um evento? Um show dela?"

        b "E pela lista de convidados... o resto tudo faz parte da FAUX. Esses desgraçados."

        b "Você vai ter que fazer uma cobertura dos céus. Eu nunca tinha visto uma lista como essa aqui."

        mc "Pera aí... eu vou ser o único?!"

        b "Exatamente. A Faux vai tá em peso lá com a TV, o jornal, a rádio... e você."

        show chefe irritado with hpunch

        b "E você vai me dar uma cobertura melhor que a deles!"

        menu:
            "Como isso é possível?! Um cara sozinho contra a FAUX?!":


                pass

        b "Dá seus pulos, moleque! Você não queria um troféu?! É sua chance!"

        show chefe emburrado with dissolve

        b "Eu vou deixar minha fi... digo... a coordenadora Sofia aqui na redação pra te auxiliar."

        b "Qualquer furo você manda pra ela e ela publica."

        b "Ela diz aqui que você pode levar somente seu próprio celular. Então vai ter que gravar com ele."

        b "Certeza que eles tão privilegiando a FAUX... até acho incrível ter uma vaga pra você."

        if diana_namoro:

            "Valeu, amor! Aposto que foi a Diana que conseguiu isso pra mim. Talvez até porque a gente tá juntos."

        elif diana_e6 == "barao":

            "Será que é por que eu tô do lado do Barão? Tá com os poderosos tem suas vantagens..."

        mc "Então se eu conseguir alguma coisa... eu mando pra Sofia."

        b "É. E ela já bota no site. Vamos tentar vencer a FAUX pelo menos na velocidade."

        b "Eu nunca vi um evento deste tamanho na cidade. Olha só para as figuras que vão tá lá."

        b "O Barão não tá economizando. Ele deve tá querendo mostrar a jóia dele para todo mundo."

        menu:
            "O que o Barão faz com a Diana é errado.":


                show chefe irritado with hpunch

                b "Óbvio que é errado!"
            "Ele que tornou ela no que ela é hoje.":


                show chefe irritado with hpunch

                b "Desde quando você lambe a bota desses filhos da puta, hein?! Será que eles te compraram igual com a..."

                mc "N-não! Só tô faland-"

                b "Não tá falando nada! Fica de bico calado e escuta!"

        b "Essas pessoas que vão tá na festa são a desgraça desta cidade!"

        b "Eles corromperam tudo! Desde os esgotos até a prefeitura! Nada escapa desses porcos!"

        b "E você vai tá no meio desse vespeiro! Então vê se abre o olho, idiota!"

        menu:
            "Se é meu trabalho eu vou fazer.":


                pass

        b "Dá pra parar de se achar?"

        show chefe empolgado with dissolve

        b "Se você fizer o mínimo, a gente vai poder mostrar pra aqueles idiotas dos investidores que nossa revista vale à pena."

        b "É mais um reforço que a gente não pode deixar os porcos colocarem as patas no nosso trabalho."

        show chefe irritado with hpunch

        b "Acho bom você não me decepcionar, moleque!!!"

        mc "P-pode deixar... eu vou fazer uma boa cobertura."

        python:
            if renpy.android:
                roupa_blacktie = PythonSDLActivity.pegaBlacktie()

        b "'Boa' é demais pra você! Só não estrague TUDO!"

        b "E comece vestindo uma roupa decente. Nem pense em ir num evento de gala desses com menos de um Black Tie."

        if roupa_blacktie:

            mc "Eu tenho um traje perfeito pra ocasião."

            show chefe surpreso with dissolve

            b "Tem mesmo, é? Você sabia que isso custa pelo menos umas mil pilas, né?"

            mc "Eu sei... mas eu consegui... fazendo um bico aqui e ali."

            b "A-agora até eu fiquei surpreso."
        else:


            mc "Como eu vou conseguir uma roupa com esse salário unha de fome que você paga?!"

            b "Já disse e repito: dá seus pulos, moleque!"

            b "E se você reclamar do salário que eu pago você vai ter que comprar um Black Tie SEM o salário!"

            mc "T-tudo bem! Eu vou dar um jeito!"

        b "Com a roupa em mãos, se prepara e vai até o Cassino do Barão. Vou te passar os dados do evento."

        b "Veja o que você consegue descobrir lá e não esquece de mandar para a Sofia."

        b "A FAUX provavelmente vai tá ao vivo. Mas ALGUMA COISA você tem que descobrir antes deles."

        b "E vê se não me decepciona."

        scene black with dissolve

        scene trabalho mesa with Dissolve(1.0)

        "Um evento de gala com as maiores figuras da cidade? Foi isso que eu entendi..."

        "Por que o Barão e a Diana não fazendo isso? Quem deu a ideia?"

        "E o que tinha no outro envelope?"

        "Parece que eu só vou descobrir tudo isso no show."

        "A Diana disse que esse pode ser o último show dela. Por isso tanta ostentação? O que eles tão planejando?"

        "Preciso pegar o Black Tie e ir até o Cassino do Barão. Esperar até o evento começar."

        "Até o chefe agora tá em cima de mim. Meu futuro na ilha depende disso."

        "Como eu acabo nessas situações?"

        $ tempo += 1

        jump call_cidade

    label cena_celeste_p1:

        mc serio "Eu descobri que o diretor financeiro do Banco Central esteve no Distrito dos Prazeres."

        show chefe surpreso with dissolve

        b "Di-diretor?!"

        mc desconfiado "O que foi, chefe? Você parece transtornado."

        b "É-é..."

        show chefe irritado with hpunch

        b "Não é nada que te interesse!"

        b "Você fez o seu trabalho. Agora pode dar o fora."

        mc "Mas eu ainda não te passei tudo."

        show chefe emburrado with dissolve

        b "Ainda tem mais?"

        mc serio "Sim. Aqui estão as fotos do ocorrido. Elas realmente parecem verídicas."

        b "Vou pedir pro pessoal do técnico ver se não é montagem. Provavelmente é tudo montagem."

        mc desculpa "Sinceramente, eu acho que não-"

        show chefe irritado with hpunch

        b "Ninguém perguntou se você acha alguma coisa!"

        b "Mais alguma coisa que eu precise saber?"

        mc bravo "Não."

        b "Então me deixa trabalhar!"

        hide chefe with dissolve

        mc "..."

        "Eu ainda vou dar uma mordida na careca desse velho..."

        "Pelo menos ele não vai mais me encher o saco por um tempo."

        jump cenario_trabalho



    label cenario_chinatown:

        "Ir pra Cidade Chinesa vai usar um período do meu dia."

        "Não sei se eu tô com saco pra ir até lá..."

        menu:
            "Pegar o ônibus até a Cidade Chinesa":


                "Bora. Não adianta ficar com preguiça."

                "Agora é esperar o busão."

                call cena_onibus from _call_cena_onibus_9

                jump cidade_chinesa
            "Vou deixar pra outra hora.":


                "Acho que não vou lá agora, não."

                jump cenario_onibus_menu

        label cidade_chinesa:

            if cenario_china_1vez:

                "Preciso ir de ônibus..."

                "Essa tal de Cidade Chinesa é longe pra caramba."

                "Não consigo nem imaginar como ela é..."

                "..."

            play sound "audio/som_7_cidade_chinesa.mp3"

            $ chinatown_area = "geral"

            hide screen chinatown_tela

            scene chinatown geral with Dissolve(1.0)

        if cenario_china_1vez:

            $ cenario_china_1vez = False

            mc surpreso "..."

            mc surpreso "Olha só pra isso!"

            "Todos os prédios, tão altos e próximos uns dos outros."

            "Olha para as pessoas! Todas andando para lá e para cá tão rápido!"

            "São muitas pessoas, a maioria com os olhos puxados..."

            "É como se eu tivesse viajado para outro país muito longe."

            "{i}zum zum zum{/i}"

            "O barulho tá me deixando surdo..."

            "E eu não entendo nada que está escrito nas placas."

            "É um mundo totalmente diferente do meu..."

            if sayuri_evento1_check:

                "..."

                "Pera! Esta placa eu consigo entender..."

                "Templo Jian Zi-Hao -> 15 km"

                mc surpreso "QUINZE???"

                mc concentrando "Não sei nem como pegar um ônibus..."

                "Bom... pra conhecer uma atleta olímpica vale a pena."

                mc charmoso "Bora lá!"

                jump sayuri_evento1




        if sayuri_e9 == "pre":

            if tempo == 1:

                jump sayuri_evento9
            else:


                "Pra encontrar a [s] e resolver tudo com ela, eu preciso vir aqui na primeira hora do dia, de manhã."

        "A Cidade Chinesa é sempre movimentada. Pra onde eu vou agora?"

        show screen chinatown_tela

        pause

        menu:
            "Ir para o Templo Jian Zi-Hao":


                if sayuri_evento1_check:

                    jump sayuri_evento1
                else:


                    jump cenario_templo
            "Voltar para o centro da cidade":


                $ cenario_china_1vez = False

                "Está na hora de voltar pra casa."

                jump call_cidade



    label cenario_templo:



        $ chinatown_area = "templo"

        hide screen chinatown_tela
        hide screen chinatown_tela2

        scene chinatown templo with Dissolve(1.0)

        play sound "audio/som_10_templo.mp3"

        if tempo > 3:

            "Caraca... tá tarde pra caramba. Melhor voltar pra ilha."

            jump call_cidade

        mc preocupado "Mano... são 15 quilômetros daqui até o centro da Cidade Chinesa..."

        mc normal "E agora?"

        menu:
            "Andar pelo templo":


                jump templo_passeio
            "Voltar para a Cidade Chinesa":


                jump chinatown_caminho
            "Voltar para a ilha":


                $ tempo += 1

                jump call_cidade

    label cena_celular_notificacao:

        $ celular_notificacao = False
        $ ligacao_ativa = False

        if diana_e2_roupa_evento and not v13_fim:

            $ diana_e2_roupa_evento = False

            "Ufa. Consegui dar uma passada na boutique. Dar um pulo em casa agora."

            jump diana_e2_cassino

        elif v17_fim and not v18_fim and j4_roupa:

            jump j4_pos_roupa

        elif priscila_e3_check == "iniciado":

            jump priscila_evento3

        elif julia_e2 == "iniciando":

            jump julia_evento2

        elif priscila_e4_check == "iniciado":

            $ priscila_e4_check = "finalizado"

            jump priscila_evento4

        elif julia_e3 == "iniciado":

            jump julia_evento3

        elif nathan_e3 == "iniciado":

            jump nathan_evento3

        elif sayuri_e5 == "iniciado":

            jump sayuri_evento5

        elif julia_e4 == "iniciado":

            jump julia_evento4

        elif v17_fim and not v18_fim and j4_roupa:

            jump j4_pos_roupa

        elif cassino_evento == "iniciado" and not silver_card:

            jump cassino_evento

        elif cena_gadget and not gadget_final:

            jump gadget_final

        elif priscila_e6_ligacao_check and not priscila_e6_ligacao:

            jump priscila_e6_ligacao

        elif diana_e4 == "comecou":

            jump diana_evento4_pre

        elif nona_e1 == "iniciado":

            jump nona_evento1

        elif priscila_e7 == "iniciado" and not v31_fim:

            jump priscila_evento7

        elif sayuri_e7 == "iniciado" and not v32_fim:

            jump sayuri_evento7_pre

        elif julia_e6 == "iniciado":

            jump julia_evento6_pre

        elif julia_e6 == "passeio_inicia":

            jump julia_e6_passeio

        elif diana_e5 == "iniciado":

            jump diana_evento5

        elif nona_e2 == "iniciado":

            jump nona_evento2

        elif naru_e1 == "iniciado":

            jump naru_evento1

        elif priscila_e8 == "iniciado":

            jump priscila_evento8

        elif sayuri_e8 == "iniciado":

            jump sayuri_evento8

        elif julia_e7 == "iniciado":

            jump julia_evento7

        elif diana_e6 == "iniciado":

            jump diana_evento6

        elif nathan_e7 == "iniciado":

            jump nathan_evento7

        elif natasha_e4 == "iniciado":

            jump natasha_evento4

        elif nona_e3 == "iniciado":

            jump nona_evento3

        elif priscila_e9 == "iniciado":

            jump priscila_evento9

        elif priscila_e9 == "iniciado2":

            jump priscila_e9_miranda

        elif priscila_e9 == "iniciado3":

            jump priscila_e9_pre_julgamento

        elif sayuri_e9 == "iniciado":

            jump sayuri_evento9_pre

        elif julia_v8 == "iniciado":

            jump julia_evento8

        elif julia_v8 == "iniciado2":

            jump julia_evento8_parte2

        elif julia_v8 == "final3" and not julia_final3:

            jump julia_final3

        elif julia_v8 == "final2_final" and not julia_final3:

            jump julia_final2_final

        elif diana_e7 == "iniciado":

            jump diana_evento7_pre

        elif nathan_e8 == "iniciado":

            jump nathan_evento8

        elif sofia_evento6 == 1:

            jump sofia_evento6

        elif sofia_evento6 == 3:

            jump sofia_evento6_parte2







        $ renpy.vibrate(1)

        play sound "audio/som_3_celular.mp3"

        if tempo == 1:

            scene mapa cidade with hpunch

        elif tempo == 2:

            scene mapa cidade_tarde with hpunch
        else:


            scene mapa cidade_noite with hpunch

        mc normal "Opa. Meu celular vibrou..."

        "Tomara que seja mensagem de alguém interessante."

        if quem_ligou == "priscila":

            if priscila_e5 == "iniciado":

                $ priscila_cel_msg6 = True

            mc surpreso "Não acredito! Mensagem da [c]."





            "Tô louco pra falar com ela."

            show screen celular_priscila

            "..."

        elif quem_ligou == "sayuri":

            $ sayuri_numero = True

            mc surpreso "É da [s]!"

            show screen celular_sayuri

            "..."

        elif quem_ligou == "julia":

            $ julia_numero = True

            mc desconfiado "Mensagem da [g]..."

            show screen celular_julia

            "..."

            if julia_cel_msg3_evento:

                $ julia_cel_msg3_evento = False

                jump julia_cel_msg3_evento

        elif quem_ligou == "diana":

            $ diana_numero = True

            mc surpreso "Opa. Mensagem da [d]. Deixa eu ver."

            show screen celular_diana

            "..."

        elif quem_ligou == "cassia":

            $ cassia_numero = True

            mc incomodado "É da [j]..."

            mc bravo "O que será que ela quer?"

            show screen celular_cassia

            "..."

            if cassia_aceitou and nathan_e1 == "nada":

                $ nathan_evento = True

                mc triste "Eu ainda não consegui nada sobre ele..."

                "E ela vai acabar com o lance que eu tenho com a [c] se eu não conseguir algo que ela possa usar sobre esse cara."

                "Não tem como..."

                mc bravo "Vou ter que falar com ele de uma forma ou de outra."

                "Então ele aparece no bar durante a noite..."

                if tempo < 3:

                    "Ainda é muito cedo. Vou ter que fazer uma hora até ir pra lá."

                if tempo == 3:

                    "Bem na hora! Se eu for até o bar, possível que eu encontre ele."

                "Espero que ele vá para o bar hoje. Aliás, não acho que é coincidência a [j] ter me avisado justo agora."

                mc desculpa "Não confio nessa mulher..."

                jump call_cidade

            elif not cassia_aceitou and not cassia_priscila_avisou:

                $ cassia_priscila_avisou = True

                mc triste "Que merda..."

                "Ela realmente publicou a matéria."

                "Espero que não seja o fim da minha relação com a [c]..."

                "Eu preciso avisar ela e a situação é urgente demais para mandar mensagem."

                mc serio "Melhor eu ligar."

                "..."

                "{i}Trr... Trr...{/i}"

                c s_feliz "Oi! É você, [mc]?"

                mc desculpa "Priscila? Sim, sou eu."

                c s_feliz "Que legal você me ligar!"

                mc "Sim. Olha..."

                c triste "Aconteceu alguma coisa? Você parece meio pra baixo."

                mc "Pois é. Aconteceu um problema na minha revista."

                c "..."

                mc "Lembra lá no parque que eu tive que sair porque ia resolver um negócio?"

                c "Lembro..."

                mc serio "Então. Vai sair uma matéria sobre a gente na minha revista."

                c surpresa "O quê?! Como assim?"

                mc "Uma paparazzo tirou uma foto nossa juntos na praça e agora vai usar isso pra inventar uma mentira e dizer que estamos juntos."

                c "Ma-mas isso é mentira! Ela não pode fazer isso!"

                mc desculpa "Ela vai fazer de uma forma ou de outra. Ela não tá nem aí pra verdade."

                c triste "Isso é muito sério, [mc]."

                mc "Eu sei. Por isso que tô te ligando e te contando."

                c "Você... Você tentou falar com ela?"

                mc serio "Sim. Tentei. Mas ela está irredutível. É uma vigarista."

                c "Sei... Obrigada por tentar..."

                mc desculpa "Desculpa por isso."

                c "Eu entendo... Vou ter que conversar com minha agente. Ela vai saber o que fazer."

                mc "Ok..."

                c "Talvez a gente tenha que ficar um tempo sem se ver."

                mc triste "Eu entendo."

                c "Ok. Vou ver com ela então. Até outra hora."

                mc "Até, [c]. Fica bem."

                c "Você também..."

                "{i}Tu... tu... tu...{/i}"

                mc bravo "Que droga! Maldita, [j]!"

                "..."

                jump v4_fim

        elif quem_ligou == "nathan":

            mc normal "O [n] me mandou mensagem."

            show screen celular_nathan

            pause

        mc normal "Vou responder depois. Hora de continuar o dia."

        jump call_cidade

    label priscila_cel_msg1_resposta:

        if estou_na_cidade:

            if tempo < 3:

                scene mapa cidade
            else:


                scene mapa cidade_noite

        $ priscila_cel_msg1_resposta_check = False

        "Uau! Isso é incrível! Ela até me mandou uma mensagem!"

        "Mesmo com tanta coisa acontecendo, ela foi atenciosa e me escreveu para agradecer."

        "Está até me convidando para falar com ela de novo! Não acredito!"

        "[mc] você não pode perder essa chance! Não estrague tudo!"

        menu:
            "Não tem o que agradecer, Pri.":


                $ priscila_amizade += 1
                $ priscila_cel_msg1_r = "amizade"

                mc feliz "Não quero que ela sinta que eu fiz um grande favor."
            "Foi um prazer passar a noite com você.":


                $ priscila_seducao += 1
                $ priscila_cel_msg1_r = "seducao"

                mc tarado "O prazer foi todo meu..."
            "Ei! Como você sabe meu telefone?!":


                $ priscila_cel_msg1_r = "zoado"

                mc zerado "Preciso de respostas..."

        "Respondido!"

        "..."

        $ priscila_cel_msg2 = True

        show screen celular_priscila

        "..."

        "Ops... Melhor voltar para o que eu estava fazendo..."

        $ priscila_cel_msg1_resposta_check = False

        if estou_na_cidade:



            call screen cidade
        else:


            return

    label priscila_cel_msg2_resposta:

        if estou_na_cidade:

            if tempo < 3:

                scene mapa cidade
            else:


                scene mapa cidade_noite

        mc surpreso "..."

        mc surpreso "Ela quer sair comigo!"

        mc concentrando "Calma, [mc]..."

        "Devo ter causado uma boa impressão ontem."

        if priscila_seducao_evento > 0:

            mc safado "Se ela está entrando em contato comigo agora, ela deve ter gostado do meu carinho..."

            "Nunca imaginei que chegaríamos naquele ponto logo no primeiro encontro."

            "E nem era bem um encontro."

            mc safado "Será que ela vai querer continuar de onde paramos?"

        elif priscila_amizade_evento > 0:

            mc normal "Acho que a noite no bar foi realmente especial pra ela."

            "Ela conseguiu se abrir comigo e falar de várias coisas."

            "Se a gente continuar saindo, preciso decidir se vou continuar como um amigo ou se tento ir além..."

        mc triste "Agora não é hora de viajar. Preciso responder ela."

        menu:
            "Sair com você? Com certeza.":


                $ priscila_amizade += 1
                $ priscila_cel_msg2_r = "amizade"
                $ priscila_cel_msg2_resposta_check = False

                mc feliz "Só um idiota perderia essa chance! Claro que vou aceitar! Na hora que ela quiser."

                mc feliz "Deixa eu responder ela."

                show screen celular_priscila

                "..."

                mc feliz "Uma garota como essas não dá pra deixar esperando."

                mc feliz "Melhor eu me apressar e chegar antes dela."

                jump priscila_evento2
            "Vou pensar e já te respondo.":


                $ priscila_cel_msg2_r = "zoado"
                $ priscila_cel_msg2_resposta_check = False

                mc tarado "Não quero que ela fique se achando muito. Assim quem sabe ela vai dar mais valor."

                "..."

                "..."

                "..."

                mc normal "Agora sim: deixa eu responder ela."

                show screen celular_priscila

                "..."

                mc normal "Ela disse que está na praça. Vou enrolar um pouco para não parecer desesperado."

                "..."

                "..."

                mc normal "Vamos lá."

                jump priscila_evento2














        $ priscila_cel_msg1_resposta_check = False

        if estou_na_cidade:

            jump call_cidade
        else:


            return

    label cidade_fim_resposta:



        call screen cidade

    label chefe_game_over:

        $ foi_despedido = True

        $ renpy.vibrate(1)

        if tempo <= 1:

            scene mapa cidade with hpunch

        elif tempo == 2:

            scene mapa cidade_tarde with hpunch
        else:


            scene mapa cidade_noite with hpunch

        "Smartphone" "Trr... Trr..."

        $ cenario_trabalho_1vez_chefe = False

        if not pauta_1vez:

            mc preocupado "Que merda. É o chefe me ligando. Hoje é meu último dia, mas ainda é tão cedo."

            mc "Alô?"

            b "[mc], você parece calmo demais."

            mc zerado "Como assim?"

            b "Quem fica calmo desse jeito no dia que vai ser despedido!?"

            "Velho maldito. Ele tem tanta certeza que eu não consegui a pauta que chega até a ser engraçado."

            b "Ficar calado não vai ajudar em nada! Vem pra redação AGORA!"

            "Smartphone" "Tu tu tu..."

            "Eu descobri duas pautas. Tenho que decidir qual das duas vou entregar."

            "A celebridade que eu entregar vai ter um segredo exposto para todos os leitores da revista. Isso é algo muito sério."

            "..."
        else:


            mc serio "Que merda, é o chefe. Será que ele já vai querer outra pauta?"

            mc "Alô? Chefe?"

            b "Você já sabe do que se trata! Traz a bunda branca pra cá agora."

            mc zerado "..."











        scene trabalho chefe with Dissolve(3.0)

        mc triste "..."

        show chefe irritado with hpunch

        if not pauta_1vez:

            $ pauta_1vez = True

            b "Você sabia do nosso trato! Eu sabia que era perda tempo! Nem sei porque eu ainda acredito nesses merdas!"

            mc serio "Eu consegui a pauta."

            b "Vocês só fazem merda e roubam o meu dinheiro! Se..."

            mc bravo "Eu consegui a pauta!"

            show chefe surpreso with dissolve

            b "QUÊ?!"

            mc serio "Isso mesmo. Eu tenho uma pauta pra nossa revista. Eu cumpri nosso acordo."

            show chefe irritado with hpunch

            b "Não brinque comigo, fedelho! Se você sabe alguma coisa, desembucha!"

            "E agora? Qual das pautas vou entregar?"

            jump entregar_pauta
        else:


            b "Você sabe como nosso acordo funciona. Se eu não tiver nada pra publicar, você precisa me dar algo."

            b "E aí?! Você tem ou não tem pautas?!"

            if pautas >= 1:

                mc serio "Tenho."

                b "Pauta não significa nada se ela está na sua cabeça e não na revista! Então desembucha logo!"

                jump entregar_pauta
            else:


                mc angustiado "Eu não tenho nenhuma pauta, chefe! Mas por favor, não me-"

                b "RUA!"

                if pauta_cassia <= 2:

                    jump compra_pauta_over
                else:


                    jump end_w



































    jump end_a

label v4_fim:

    $ v4_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v4_fim","inicio","local")

    "..."

    "Tantas coisas aconteceram nos últimos dias."

    if cassia_priscila_avisou:

        "A [j] publicou a matéria sobre mim e a [c]. Ela acha que vamos ter que ficar um tempo sem nos ver."

        mc triste "E se {i}ficar um tempo{/i} quer dizer não se ver nunca mais?"

        mc angustiado "Droga..."

        "Não posso ficar na mão da [j] pra sempre. Preciso reverter essa situação de alguma forma."

    if cassia_nathan_entregou:

        "Eu acabei entregando as informações do [n] pra [j]. Espero que isso não se volte contra ele."

        "Mas era a única forma de evitar que ela publicasse a matéria."

        "Como as coisas vão ficar a partir de agora?"

        "Quero ver a [c]. E tem a [sc]. Agora também o [n] e a [j]."

        mc angustiado "Parece que eu tô me enrolando cada vez mais..."

    elif cassia_nathan_naoajudou:

        "Eu não quis ajudar o [n] e ele acabou revelando sobre seu contrato pra [j]."

        "Mesmo indiretamente ele me ajudou com a [c]."

        "Mas será que eu fiz o certo me esquivando de ajudar ele? Será que ele vai ficar bem?"

        mc incomodado "..."





    if sayuri_evento1_check:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("sayuri_esquecida","sayuri","local")

        "Mudando completamente de assunto, eu esqueci da tal da [sc]."

        "Pelas mensagens que ela trocou com a [c], elas parecem bem amigas."

        "Se eu me aproximar dela, posso decobrir mais sobre a [c]."

        "A própria [s] também é uma celebridade. Com certeza posso conseguir mais pautas com ela."

        "E quem sabe ela é uma garota bacana? Não posso perder essa chance de encontrar ela."

        "Ela está no templo. Primeiro preciso ir pra {b}Cidade Chinesa{/b} pegando o ônibus na saída sul da ilha."

        "..."

    jump call_cidade

label v5_fim:

    "Preciso parar e pensar um pouco."

    mc desculpa "As coisas estão acontecendo muito rápido na minha vida."





























label guia_priscila_e1:

    scene black with Dissolve(2.0)

    p lecionando "Seu encontro com a [c] na verdade começa muito antes do que você imagina."

    p "A primeira decisão que você toma é se você vai ou não escutar a conversa dela com seu chefe. Se você escutar, você pode falar sobre isso adiante."

    p "A segunda decisão é logo em seguida."

    scene guia p_e1_1 with Dissolve(1.0)

    p rindo "Após receber o elogio dela, como você vai reagir?"

    p "A [c] é uma garota que vive grandes contradições. Ela trata do imaginário fantasioso adolescente, mas ao redor dela os adultos são extremamente reais."

    p "Ela quer um príncipe. Alguém confiante, com pegada, que possa defender ela dos problemas em que ela se encontra."

    p "Se você pretende ser mais que um amigo, você terá que encarnar esse personagem."

    p "Por isso, neste momento o melhor é mostrar toda sua confiança e elogiar ela de volta."

    p "A primeira resposta não é ruim, pois ela pode te achar fofo e isso vai te render bons pontos dependendo de como você conversar com ela no bar."

    p "Mas se você prefere o caminho da sedução, mostrar confiança é o melhor."

    scene black with dissolve

    p "Depois disso, vamos direto para o encontro propriamente dito. É lá que tudo será definido."

    scene guia p_e1_2 with Dissolve(1.0)

    p lecionando "Assim que você chega para falar com ela, você precisa puxar assunto de alguma forma."

    p "Se vocês trombaram na redação da revista, você terá a terceira opção disponível. Se não, apenas as duas primeiras aparacerão. Vamos focar nessas."

    p "Aqui nós vamos continuar com nossa estratégia. Não tenha medo de ser exibido. Seja confiante e mostre pra ela que você não tem medo dela."

    p "A primeira opção é a mais indicada para seduzir, enquanto a segunda te deixa mais vulnerável, facilitando que ela se abra com você."

    scene black with dissolve

    p rindo "Depois que você chegar com tudo, não pode voltar atrás. Se ela duvidar de você, seja ainda mais firme."

    p "Diga que você acreditou nela com certeza porque é normal te chamarem de gato. Você vai parecer um pouco babaca, mas não se preocupe."

    p "Você vai ter tempo para que ela te entenda melhor. A outra alternativa é melhor para se tornar um amigo."

    p "Continuando..."

    scene guia p_e1_3 with Dissolve(1.0)

    p lecionando "Aqui eu nem preciso falar, né?"

    p "Por que raios você iria corrigir a moça? Olha a carinha dela!"

    p "Esse ponto da conversa, no entanto, é o que vai separar o conquistador do amigo."

    p "Preste muita atenção."

    scene guia p_e1_4 with Dissolve(1.0)

    p lecionando "Aqui é o seguinte. Para se tornar amigo dela, é só escolher a comédia romântica. Vai gerar uma afinidade e uma cumplicidade. Muito fácil."

    p "Mas se você quiser ir além, não adianta ficar de lenga-lenga. Esta é uma excelente oportunidade para mudar o rumo da conversa."

    p "Você quer excitar ela. Você quer que ela saia de uma zona neutra e veja você com outros olhos."

    p "Uma excelente forma de fazer isso é falar de temas adultos. Fazer ela imaginar cenas que remetam ao prazer e relacionar isso a você."

    p "Mas aqui mora um grande perigo. A [c], se você prestar atenção, tem uma certa repulsa à pornografia. Ela tem vários motivos para isso."

    p "Por isso, você precisa andar em uma linha tênue entre falar de temas adultos, mas sem cair na pornografia."

    p "Diga que você gosta de temas que envolvem sexo, mas não apenas isso. E se ela falar de pornografia, negue prontamente."

    p "Você gosta de prazer, do pecado, de assuntos cinzas, mas ao mesmo tempo você é contra sexo explícito."

    p "Isso vai instigar algo dentro dela e preparar o terreno para você dar o bote."

    p "A partir de agora, se você fez tudo certo o caminho é muito mais fácil."

    scene guia p_e1_5 with Dissolve(1.0)

    p rindo "Elogiar nunca faz mal. Se o objetivo é seduzir, chame ela de linda."

    p "Agora, se você deseja aprofundar sua amizade, reafirme sua disponibilidade. Diga que você está lá para ela."

    p "A próxima escolha também é muito simples. Continue mostrando que você tem tudo sob controle para deixar ela maluquinha."

    p "Nada que ela quiser aprontar para cima de você vai te deixar sem jeito. Você é forte e pode defender ela. Lembre-se disso."

    scene black with dissolve

    p rindo "Quanto à bebida, é com você. Isso não muda muito o que ela vai achar de você. Eu recomendo que você aceite."

    mc zerado "Claro que você recomenda..."

    p lecionando "Bom... Continuando..."

    scene guia p_e1_6 with Dissolve(1.0)

    p lecionando "Esta é a última etapa."

    p "E ela não chamaria de 'teste' se não fosse uma pegadinha. Ela quer se sentir segura, lembra?"

    p "Foque nos olhos dela e mostre que você não é fraco para cair em uma coisa besta."

    p rindo "Nesse ponto ela já perdeu o chão. Ela tá sendo consumida por todos esses sentimentos que você despertou nela."

    p "A bebida vai ajudar ela a se soltar e daí é só dar a ela o que ela quer."

    p "É o primeiro encontro. Não pense em você. Só dê prazer para a moça."

    scene black with dissolve

    p rindo "E é isso. Você entrará para a vida dela com o rapaz mais corajoso e diferenciado que ela já conheceu."

    scene fadolandia geral with Dissolve(1.0)

    show pixie provocando with dissolve

    p "Eu sou mesmo incrível, né?"

    mc zerado "..."

    p "Sabendo como as coisas funcionam fica mais fácil, não acha?"

    mc normal "Não posso negar que você realmente entendeu ela."

    p "Claro. Eu entendo tudo."

    p "Agora é só usar meus poderes e viver o encontro novamente."

    mc desconfiado "Mas eu não vou me esquecer de tudo? O que adianta?"

    p "Ai ai, [mc]. Será que um dia você vai entender a dinâmica disso tudo?"

    mc desconfiado "..."

    return

label cena_cards1:

    scene black with Dissolve(3.0)

    "{b}Em um dos lofts do hotel da ilha{/b}"

    scene hotel loft with Dissolve(3.0)

    c "Que dia mais cansativo..."

    show priscila cansada with dissolve

    c "A impressão que eu tenho é que eu tirei 1293812903812903 fotos."

    c "Que número será que foi esse que eu acabei de falar?"

    c "Tanto faz... Acho que vou tirar aquela soneca..."

    hide priscila with dissolve

    c "Até daqui a pouco mundo..."

    scene black with Dissolve(1.0)

    c "{size=15}zZzZzZzZz{/size}"

    scene fadolandia geral with Dissolve(1.0)

    c "Quê?!"

    show priscila impressionada with dissolve

    c "Que lugar é esse?"

    c "Será que eu tô sonhando?"

    p "Mais ou menos..."

    c "Que-que-quem é você?!"

    show priscila impressionada at esquerda with move

    show pixie bonitinha with dissolve

    show pixie bonitinha at direita with move

    p "Oi! Eu sou a [p], a fada mais sexy do mundo!"

    c "Pi-pi..."

    p "Não. Isso aí é a forma gracinha de chamar o que o homem tem no meio das pernas."

    c "A-ah..."

    p "Calma, [c]. Tá tudo bem. Eu sou sua amiga."

    c "..."

    show pixie explicando with dissolve

    p "Isso. Respira um pouco e tenta se acalmar..."

    c "..."

    show priscila preocupada with dissolve

    c "Desculpa... Eu fiquei um pouco nervosa, mas já tô melhor."

    p "Que bom. É normal você se sentir meio confusa. Isso acontece com todos humanos que vêm aqui."

    p "Se bem que você ficou um pouco mais assustada que o normal."

    c "Desculpa..."

    show pixie sonhadora with dissolve

    p "Está tudo bem. Só quero que você se acostume logo pra gente poder começar."

    c "Começar o quê?"

    p "Você vai ver."

    p "A próxima visita já tá chegando."

    hide pixie with dissolve

    p "Aí vem ela!"

    show garconete e_emburrada with dissolve

    g "Ei! O que tá havendo aqui?!"

    show garconete e_emburrada at direita with move

    p "Calma, calma, maninha."

    g "Quem aqui é tua maninha?!"

    show pixie explanando with dissolve

    p "Calma, estressadinha."

    p "Eu que chamei vocês aqui pra gente ter uma reunião só de garotas."

    show priscila incerta with dissolve

    c "Senhorita [p]..."

    p "Fala, linda."

    c "Eu ainda tô um pouco confusa com tudo isso..."

    p "Não esquente, fofa. Eu... Opa! Tem mais gente chegando aí."

    hide pixie with dissolve

    p "Com licença."

    show karli preocupada with dissolve

    m "..."

    m "O que que é isso?!"

    m "Que lugar é esse?!"

    c "Não precisa ficar assim. Tá tudo legal."

    m "Ah! Oi! Não sei direito o que tá acontecendo..."

    show garconete e_resignada with dissolve

    g "Você não parece muito inteligente..."

    m "Ei!"

    p "Garotas! Calma!"

    show pixie desconfiada at entra_direita with dissolve

    p "Eu não tô aqui pra cuidar de vocês. Podem ficar todas quietas antes que eu literalmente mate todas vocês."

    show priscila impressionada with dissolve

    "Galera" "..."

    p "Assim é bem melhor."

    g "{size=10}Vaca...{/size}"

    p "Quê?!"

    g "..."

    hide pixie with dissolve

    g "E ainda nem chegou todo mundo..."



    hide karli with dissolve



    "..."

    "FIM"

    return

label gadget_final:

    $ gadget_final = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("cena_gadgets","tkf","personagem")

    scene ape_geral with Dissolve(1.0)

    "!"

    "Nossa. Me veio uma coisa na cabeça agora. Parece que esses dias eu eu tô sonhando com uma f-"

    $ renpy.vibrate(1)

    "Eita! Alguma coisa vibrou aqui."

    $ renpy.vibrate(1)

    "Ué. Não é meu celular."

    $ renpy.vibrate(1)

    "O-o que é isso?!"

    show gadget_gama with dissolve

    "O negócio tá brilhando."

    show gadget_alfa at entra_esquerda with dissolve

    "Uou. Este outro treco também."

    show gadget_beta at entra_direita with dissolve

    "E esse aqui!"

    mc surpreso "Eles tão brilhando juntos!"

    "{i}zzzzkkkk{/i}"

    "{i}Trying to connect to HQ...{/i}"

    "{i}Connected.{/i}"

    "{i}Retrieving HQ location...{/i}"

    "{i}Processing location image representation...{/i}"

    "{i}Showing image.{/i}"

    mc surpreso "Tem uma imagem aparecendo!"

    show cidade tkf with Dissolve(1.0):
        alpha 0.5

    mc "É tipo um holograma!"

    "TKF... Eu já ouvi falar disso antes..."

    mc surpreso "!"

    "Esse lugar... ele fica na capital! Esses prédios! Eu conheço isso!"

    "Caralho caralho caralho!"

    "Esse é o tipo de coisa que essa TKF tá fazendo?! Eu nunca vi uma coisa dessa antes."

    "Eu preciso saber mais sobre isso. Tenho que ir lá de qualquer jeito."

    hide cidade tkf with dissolve

    "Com certeza essas peças que eu encontrei não são algo simples. Elas devem tá ligadas a alguma coisa relacionada a essa TKF."

    "Não sei se eu tô com mais empolgação ou cagaço."

    "Tenho que ir no centro da cidade e falar com eles sobre isso. Urgente."



    jump call_cidade

label gadget2cena:

    $ gadget2cena = True

    mc preocupado "A peça tá brilhando!"

    mc "Pera! O outro treco que eu encontrei antes também tá brilhando!"

    "{i}zzzzkkkk{/i}"

    "{i}Trying to connect to HQ...{/i}"

    mc preocupado "Tá falando alguma coisa!"

    "{i}Connection failed...{/i}"

    "{i}Missing Gadget Gama{/i}"

    "{i}Trying to locate Gadget Gama...{/i}"

    "{i}Unable to locate Gadget Gama... Missing Location Component.{/i}"

    "{i}Please locate Gadget Gama manually and retry.{/i}"

    "{i}tccchhhkkkk{/i}"

    mc triste "Mas que merda foi essa..."

    mc concentrando "Ele falou em outro idioma... Meu inglês não é perfeito, mas pelo que eu entendi está faltando uma peça..."

    mc serio "As duas peças que eu encontrei não são suficientes pro equipamento funcionar."

    mc "Seja lá o que for isso, é impossível fazer ele pegar agora."

    mc "Vou precisar encontrar uma terceira peça... Onde será que ela está?"

    mc desconfiado "E do que se trata isso aqui? Parece algo do futuro... que viagem."

    mc "Melhor eu esquecer isso e me concentrar em encontrar a [c]."

    hide gadget_beta with dissolve
    hide gadget_alfa with dissolve

    return

label aviso_final:





    p rindo "Ei! Não esqueça de me visitar no mundo do sonhos de vez em quando, hein?"

    p "Dependendo da hora do dia em que você dorme, podem acontecer coisas diferentes em Fadolândia."

    p "Eu te encontro lá!"

    $ aviso_final = False

    jump call_cidade

    show screen salvar_jogo

    "..."

    p "Pra voltar aqui, é só usar o botão {b}Continuar{/b} na tela inicial ou o botão {b}Carregar{/b} ali em cima."

    p "Agora você também pode salvar o jogo na nuvem. Assim mesmo que você desinstale o aplicativo, é possível voltar aqui."



    show screen salvar_nuvem

    "..."

    p "Caso você queira recuperar seu jogo que está salvo na nuvem, é só acessar o menu inicial e clicar em {b}Baixar Jogo da Nuvem{/b}"

    p "Tome cuidado para não ficar dormindo e avançando o tempo ou você vai ser despedido."

    p "Não esqueça das aulas de massagem."

    p rindo "Deixe o aplicativo instalado para receber notificações com notícias!"

    $ aviso_final = False

    jump call_cidade

    menu:
        "Salvar o jogo":


            python:
                renpy.notify("Seu jogo foi salvo no seu aparelho")
                renpy.save("continue", extra_info="continue")

            p "Prontinho. Pra voltar aqui, é só usar o botão {b}Continuar{/b} na tela inicial ou o botão {b}Carregar{/b} ali em cima."
        "Não salvar":


            p "Ok!"

label pixie_tutorial_cel:

    scene black with Dissolve(1.0)

    p rindo "Oie. Tudo legal?"

    p "Você quer que eu te explique como o celular funciona? Prometo que é rápido e vai ser muito útil no decorrer do jogo."

    menu:
        "Ok. Me fale sobre o celular.":


            p rindo "Que bom! Vou explicar rapidinho como ele funciona."

            $ proibido_salvar = True
            $ show_quick_menu = False



            p lecionando "Celebridades e outras pessoas vão te mandar mensagens de vez em quando."

            p "Você deve apertar em {b}Responder{/b} para dar continuidade ao seu encontro com ela."

            p "Você não precisa responder a pessoa na hora que ela lhe enviar a mensagem. É só você"
        "Já sei como funciona, não precisa.":


            p "Ok! Bom game então!"

    if tempo == 1:

        scene mapa cidade with dissolve

    elif tempo == 2:

        scene mapa cidade_tarde with dissolve
    else:


        scene mapa cidade_noite with dissolve

    mc normal "Nem acredito que a [c] tá me ligando."

    return

label adeus_casa:

    scene black with Dissolve(1.0)

    "..."

    scene apartamento tarde with Dissolve(1.0)

    "Aqui está. Meu apartamento."

    "Você pode não ser grande, mas sem você eu nunca teria conseguido viver tudo o que eu estou vivendo."

    "Eu consegui. Não foi fácil, mas eu consegui."

    "Consegui me manter no trabalho, consegui ganhar uma grana extra. E finalmente estou pronto pra ir pra um outro lugar."

    "Mas se não fosse você, nada disso teria sido possível."

    "Vou sentir saudades de você amigo."

    "Espero que o próximo que viver aqui cuide de você como eu cuidei."

    mc zerado "Só que derrubando menos gordura de pizza no chão."

    "Adeus!"

    scene black with Dissolve(5.0)

    "{b}2 dias depois{/b}"

    $ dia += 2
    $ tempo = 1

    if xiangu_namoro:

        $ xiang_casa = True

        "É hora de avisar a Xiang e a He Xiangu que eu tenho uma casa maior."

        "Vai ser bacana poder morar com elas por um tempo! O que será que vai dar?!"

        "Se eu quiser... provavelmente bastante sacanagem hehehe..."

    return

label ban_story:

    hide screen navegar
    hide screen menu_game
    hide screen quick_menu

    $ renpy.block_rollback()

    $ proibido_salvar = True
    $ show_quick_menu = False

    scene black

    $ renpy.block_rollback()

    $ proibido_salvar = True
    $ show_quick_menu = False

    "..."

    $ renpy.block_rollback()

    $ proibido_salvar = True
    $ show_quick_menu = False

    p "Interessante..."

    show pixie detetive with dissolve

    p "Achou mesmo que você ia roubar no meu jogo e sair ileso?"

    p "Desculpa, bebê, mas sem jogo pra você."

    show pixie impaciente with dissolve

    p "Hmf!"

    p "Se você acha que eu errei ao bloquear sua conta. Ou seja, se você não adquiriu nada de forma ilegal, você pode recuperar ela."

    p "Envie um e-mail para {b}game@celebrityhunter.com.br{/b} com todos os comprovantes de compra da Google Play."

    p "Eu vou dar uma olhada neles e se estiver tudo certo, liberarei sua conta, ok?"

    show pixie provocando with dissolve

    p "Mas você sabe que no fundo você é só um ladrãozinho de quinta que sacrifica seus escrúpulos pra se dar bem em um joguinho."

    $ renpy.choice_for_skipping()

    p "Coitado..."

    label ban_story_loop:

        $ renpy.choice_for_skipping()

        $ renpy.block_rollback()

        $ renpy.choice_for_skipping()

        p "Hihi..."

        jump ban_story_loop

label bstor_new:

    hide screen navegar
    hide screen menu_game
    hide screen quick_menu

    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()

    $ proibido_salvar = True
    $ show_quick_menu = False

    scene black

    $ renpy.block_rollback()
    $ renpy.choice_for_skipping()

    $ proibido_salvar = True
    $ show_quick_menu = False

    "{b}Sua conta foi bloqueada automaticamente por suspeita de atividade irregular{/b}"

    $ renpy.block_rollback()
    $ renpy.choice_for_skipping()

    $ proibido_salvar = True
    $ show_quick_menu = False

    "{b}Nosso sistema busca proteger você e nosso game de violações contra nossos Termos de Uso{/b}"

    "{b}Se você acha que isso é um engano, entre em contato pelo email contato@geiko.net e vamos te ajudar com toda a atenção{/b}"

    $ renpy.choice_for_skipping()

    $ renpy.quit()

    jump bstor_new

label compra_pauta_over:

    scene black with Dissolve(1.0)

    if pauta_cassia == 0:

        "Não acredito..."

        j "Pombinho?"

        mc desconfiado "Hm?"

        scene cassia_pauta1 with Dissolve(1.0)

        pause

        mc zerado "[j]..."

        j "É difícil não ouvir os gritos do velho. A coisa foi feia, hein?"

        mc desculpa "Já era... perdi o emprego."

        j "Que pena, pombinho..."

        mc "..."

        j "Vem aqui."

        scene cassia_pauta2 with Dissolve(1.0)

        j "Eu tenho um negócio aqui que TALVEZ possa te ajudar."

        mc envergonhado "Só se for dinheiro ou uma pauta..."

        j "Acertou em cheio."

        mc surpreso "C-como?!"

        j "Eu tenho algumas informações que o chefe iria adorar. Mas como eu só trabalho em grandes reportagens, não vou usar."

        mc normal "E você me daria?! Sério?!"

        j "Claaaro... que não."

        mc zerado "Então o quê?"

        j "Eu posso vender."

        mc "[j] você sabe que eu nem tenho onde cair morto, né?"

        j "Eu sei. Mas eu quero pouco dinheiro. Eu tô mais interessada no que você vai ter que fazer pra mim."

        mc desconfiado "Hmm... quanto você quer?"

        j "Pouca coisa. {b}C$ 250{/b} e você pode ir pra casa tranquilo com seu emprego."

        mc "Só isso? É pouco por uma pauta..."

        j "Como eu disse, isso é só pra eu comprar um sapato novo. O que importa é que você vai ficar me devendo uma."

    elif pauta_cassia == 1:

        mc angustiado "Fui despedido de novo!"

        scene cassia_pauta1 with Dissolve(1.0)

        j "De novo, pombinho..."

        mc zerado "[j]... você de novo..."

        j "Exatamente. Vim te socorrer outra vez. Mas esta é a ÚLTIMA!"

        scene cassia_pauta2 with Dissolve(1.0)

        j "São as mesmas condições. C$ 250 e um favor que eu vou cobrar depois."

    label pauta_cassia_escolhe:

        python:
            if renpy.android:
                pauta_cassia_db = PythonSDLActivity.pegaPautaCassia()

        $ renpy.choice_for_skipping()

        "..."

        if pauta_cassia < pauta_cassia_db:

            "{b}Você já pagou por [pauta_cassia_db] pauta(s) da [j], mas neste gameplay você usou [pauta_cassia].{/b}"

            "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode pegar uma nova pauta sem pagar novamente.{/b}"

            jump pauta_cassia_comprou

        python:
            if renpy.android:
                cash = PythonSDLActivity.pegaCash()

        $ renpy.choice_for_skipping()

        "Eu tô com {b}C$ [cash]{/b}..."

        $ renpy.choice_for_skipping()

        j "E então? É pegar ou largar."

    "Se eu não comprar essa pauta, eu vou ser despedido e é o fim da minha vida na ilha. É comprar ou comprar."

    menu:
        "Vou querer. Preciso do emprego.":


            if cash < 250:

                show black with dissolve

                "{b}Infelizmente o [mc] não tem esse dinheiro com ele para comprar a pauta da [j]{/b}"

                "{b}Você pode ajudar o [mc] usando dinheiro do nosso mundo. Além de evitar o fim do jogo, você contribui com o desenvolvimento do game{/b}"

                menu:
                    "Ok. Quero comprar.":


                        call comprar_cash from _call_comprar_cash_8

                        "{b}Se sua compra foi processada com sucesso, você recebe os C$ imediatamente. Qualquer problema, use o link na loja para falar com o suporte{/b}"

                        hide black with dissolve

                        jump pauta_cassia_escolhe
                    "A vida é dura. Tô pobre igual ele.":


                        "{b}Relaxa. Você pode ganhar C$ trabalhando no bar e juntar para evitar o fim do jogo. Boa sorte!{/b}"

                        hide black with dissolve

                        jump pauta_cassia_escolhe

            python:
                if renpy.android:
                    PythonSDLActivity.addPautaCassia()
                    PythonSDLActivity.registraEvento("pauta_cassia","a","a")

                renpy.block_rollback()

            label pauta_cassia_comprou:

                pass

            $ foi_despedido = False
            $ iconchefe = 0
            $ hora_pauta = False
            $ entregou_pauta += 1
            $ pauta_cassia += 1

            mc charmoso "Tá aqui."

            scene cassia_pauta3 with Dissolve(1.0)

            j "Perfeito, pombinho. Agora pode ir tranquilo que eu converso com o chefe no seu lugar."

            mc preocupado "Mas e se ele não aceitar?"

            j "Deixa que eu cuido do velho. Eu sei como acalmar aquela cabecinha..."

            mc envergonhado "..."

            j "Homens são todos iguais, [mc]. Só muda a quantidade de cabelo na cabeça."

            j "Agora vai. E não se esqueça que você tá me devendo uma. Eu vou cobrar."

            mc "Ok... valeu, [j]. Você me salvou."

            j "Beijo."

            scene black with Dissolve(1.0)

            "A [j] me salvou de verdade... mas... o que será que ela vai querer em troca?"

            mc angustiado "..."

            $ tempo += 1

            jump call_cidade
        "Infelizmente não tenho a grana.":


            mc preocupado "Droga. Não tenho a grana."

            j "É uma pena, pombinho. Espero que sua vida seja boa. Mas eu acho que não vai ser."

            mc "..."

            j "Vai rápido pra sofrer menos."

            mc desculpa "Adeus."

            scene black with Dissolve(1.0)

            jump end_w
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
