

label massagem_curso:

    if mc_massagem == 0:

        jump karli_aula1

    elif mc_massagem == 1:

        jump karli_aula2

    elif mc_massagem == 2:

        jump karli_aula3

    elif mc_massagem == 3:

        jump karli_aula4

    elif mc_massagem == 4:

        jump karli_aula5

    elif mc_massagem == 5:

        jump karli_aula6

    elif mc_massagem == 6:

        jump karli_aula7

    elif mc_massagem == 7:

        jump karli_aula8

    elif mc_massagem == 8:

        jump karli_aula9

    elif mc_massagem == 9:

        jump karli_aula10

    call call_cidade from _call_call_cidade_1

label karli_aula1:

    show karli satisfeita with dissolve

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    m "Que bom que você não desistiu. Era o mínimo que eu esperava de você."

    m "Agora deixa eu ver onde paramos."

    mc normal "Nós não paramos. Nós nem começamos na verdade. Hoje que você ia começar realmente a me ensinar."

    m "Verdade."

    show karli normal with dissolve

    m "Hoje vai ser diferente da sua visita de antes. Hoje eu vou começar a te ensinar de verdade a arte da massagem."

    m "Vou te ensinar os {b}quatro pontos fundamentais{/b} e vou dar uma tarefa simples já que é sua primeira vez."

    m "Daí vou deixar você praticar me massageando. O que acha?"

    menu:
        "Parece trabalhoso demais...":


            mc incomodado "Parece bem trabalhoso..."

            show karli meudeus with dissolve

            m "Nem começamos ainda e você já tá assim? Onde eu tava com a cabeça quando te aceitei como discípulo?"

            m "O que eu fiz pra merecer isso deuses da massagem?"

            mc zerado "Não é pra tanto assim também."

            m "... Bom..."
        "Eu vou fazer você se sentir muito bem.":


            $ karli_seducao += 1

            mc tarado "Eu vou te fazer se sentir muito bem. Pode confiar em mim."

            show karli provocando with dissolve

            m "Tenho certeza que você ia adorar me ver relaxada."

            mc safado "..."

            m "Mas duvido que você consiga isso hoje."

            mc tarado "Não duvide de mim."

            m "..."
        "Entendi. Estou pronto.":


            mc normal "Eu estou pronto pra fazer o que for preciso pra me tornar bom nessa arte."

            show karli feliz with dissolve

            m "Assim que se fala, [mc]. Gostei de ver!"

            m "É importante que você entenda logo a importância do que estamos fazendo aqui."

            mc "Eu entendo. Pode ficar tranquila."

    show karli normal with dissolve

    m "Vamos começar indo para a sala e lá vou te explicar melhor."

    mc normal "Ok."

    scene salao massagem with Dissolve(1.0)

    m "Vai se acostumando com o lugar que vamos passar bastante tempo aqui."

    if karli_seducao >= 3:

        show karli provocando with dissolve

        m "Não que você fosse se importar, né?"

        mc safado "Eu e você sozinhos aqui? Não me importo nem um pouco."

        m "Não precisava nem falar."
    else:


        show karli normal with dissolve

    m "Você vai ter que tirar a roupa igual da outra vez."

    mc charmoso "Hmmm..."

    menu:
        "Dessa vez eu só tiro se você me acompanhar.":


            $ karli_seducao += 1

            mc charmoso "Desta vez você não escapa. Só tiro se você me acompanhar."

            m "De novo essa história?"

            mc "Com certeza. Não é justo só eu ficar praticamente pelado aqui."

            m "Hmmm..."

            m "De jeito nenhum."

            mc zerado "..."
        "Não precisa nem falar.":


            mc normal "Não precisa falar duas vezes. Pronto."

            m "Vou demorar pra me acostumar com a velocidade que você tira a roupa."

    m "Agora é só você se ajeitar ali na mesa e eu já vou começar."

    hide karli with dissolve

    "..."

    scene massagem mc with Dissolve(1.0)

    "Dessa vez eu não vou dormir de jeito nenhum. Quero aproveitar ao máximo."

    "Depois daquela massagem eu me senti tão bem. E ainda tô sentindo meu corpo melhor."

    m "E aí? Já tá pronto?"

    mc "Sim. Tô bem ajeitado."

    m "Ok. Primeiro eu vou começar te falando os {b}4 pontos fundamentais da massagem{/b} e depois eu mostro no seu corpo onde eles ficam."

    m "Os pontos são {b}Kita{/b}, {b}Higashi{/b}, {b}Minami{/b} e {b}Nishi{/b}."

    mc "Quê?!"

    m "Calma. Eu sei que você não vai decorar de cara. Não entre em pânico."

    mc "Ok..."

    m "Agora eu vou mostrar onde fica cada um deles."

    scene massagem e1 with Dissolve(1.0)

    m "{b}Kita{/b} é o ponto mais acima das costas. Nos ombros e clavícula."

    m "Resumindo, {b}Kita{/b} é o ponto de cima. Não se esqueça disso."

    mc "Certo. Kita em cima."

    m "Isso mesmo. Agora vamos para o próximo."

    m "O segundo ponto é chamado {b}Higashi{/b} e ele fica na base das costas. Bem na junção com as nádegas."

    m "Você precisa abaixar bem as mãos. Não tenha medo de tocar na bunda."

    mc "..."

    m "Só não vai tentar dar uma de engraçadinho ou vai acabar na cadeia."

    mc "Calma..."

    m "Não é calma. Se a pessoa massageada não confiar em você, nunca ela vai conseguir curtir de verdade."

    m "É preciso passar confiança. E a coisa mais básica é que a pessoa não seja violada."

    mc "Entendi. Pode deixar. Não sou um cachorro no cio."

    m "Tem muito engraçadinhos e engraçadinhas por aí. Aqui é coisa séria."

    m "Bom. Então não se esqueça que o {b}Higashi{/b} é na base das costas. Nosso segundo ponto."

    mc "Higashi é o segundo ponto, na base das costas."

    m "Exatamente."

    m "E como chama o primeiro ponto mesmo?"

    menu:
        "Kita":


            mc "Kita."

            m "Isso aí."
        "Shita":


            mc "Shita."

            m "Que porra é essa?"

            m "É Kita."
        "Mina":


            mc "Mina."

            m "..."

            m "É Kita."
        "Keiko":


            mc "Keiko."

            m "Nada a ver."

            m "É Kita."

    m "Continuando..."

    m "O terceiro ponto é chamado de {b}Minami{/b} e ele é nos pés."

    m "Por ficar longe do restante dos pontos, os pés são massageados de forma separada e recebem atenção especial."

    mc "É muito bom mesmo."

    m "Exatamente. O {b}Minami{/b} é extremamente relaxante e prazeroso."

    m "E o último ponto é o {b}Nishi{/b}. Ele fica no centro das costas, mas é um pouco diferente dos dois primeiros."

    m "Para estimular da forma correta esse ponto, você deve usar seu cotovelo."

    mc "Isso não machuca?"

    m "Não, idiota. Você não vai fazer igual um cavalo."

    mc "Ok, ok... Calma..."

    m "O {b}Nishi{/b} é feito com muito cuidado e deve estar junto dos outros pontos nas costas."

    m "Uma massagem completa estimula Kita, Higashi e Nishi nas costas. E depois completa com Minami nos pés."

    m "Se você estimular os pontos corretos, com a intensidade correta, não tem como dar errado."

    mc "Desse jeito nem parece tão difícil."

    m "Viu só?"

    m "..."

    m "Claro! Eu ainda não terminei!"

    mc "Eu sabia que tava fácil demais."

    m "Trabalhar os pontos é a base, o café com leite da massagem. Fazendo o essencial direito é excelente."

    m "Mas é aqui que minha arte transcende o comum e atinge a estratosfera do bem-estar."

    mc "..."

    m "O segredo é a {b}ordem que você trabalha cada um dos pontos{/b}."

    m "Faz toda diferença se você começa com Kita e passa pra Higashi ou o contrário."

    m "É a ordem de estímulo dos pontos que vai dizer se a pessoa vai sair relaxada ou excitada da sessão."

    if karli_seducao >= 3:

        m "E pelo jeito que você tá agindo nas aulas, você quer mesmo é deixar a pessoa com tesão."

        mc "Com certeza."

        m "De preferência já começar comigo..."

        mc "É o objetivo."

        m "Hmm..."

    m "Então é isso que a gente vai fazer aqui."

    m "Hoje você vai só entender os pontos. Mas a partir da segunda aula vamos trabalhar as várias ordens."

    m "Você acha que entendeu os 4 pontos fundamentais?"

    menu:
        "Acredito que sim. Posso começar a praticar?":


            mc "Acho que eu toô pronto pra começar a prática."

            m "Muito bem. Quero só ver."
        "Acho que eu preciso de uma revisão.":


            mc "Acho que seria bom você repassar."

            m "Tudo bem. É normal ter dificuldades."

            m "O primeiro ponto é o Kita, a parte superior."

            m "O segundo ponto é o Higashi, a base das costas."

            m "O terceiro é o Minami, nos pés."

            m "E o quarto e último a gente chama de Nishi e é no centro das costas com o cotovelo."

            mc "Certo. Agora acho que peguei."

            m "Perfeito."

    m "Então agora eu vou me deitar e você vai tentando encontrar os pontos e eu vou te ajudando."

    mc "Ok. Deixa eu levantar."

    scene salao massagem with Dissolve(1.0)

    "Finalmente chegou a hora de eu começar a praticar."

    menu:
        "Estou pronto pra começar.":


            mc normal "Estou pronto pra começar a treinar."

            show karli normal with dissolve

            m "Beleza. Eu vou deitar e você pode começar a treinar os pontos."

            "..."
        "Você vai tirar a roupa pra eu te massagear?":


            $ karli_seducao += 1

            mc charmoso "Agora você vai tirar a roupa pra eu te massagear?"

            if karli_seducao >= 4:

                show karli provocando with dissolve

                m "A ideia está cada vez mais tentadora..."

                mc safado "Então..."

                m "Só que não."

                mc zerado "..."
            else:


                show karli normal with dissolve

                m "Continua sonhando..."

                mc envergonhado "Droga..."

                m "Quem sabe um dia..."

    m "Vou me ajeitar."

    mc "Certo, e eu vou começar então com a primeira posição."

    "..."

    scene massagem kita with Dissolve(1.0)

    m "Hmmm..."

    mc "Que foi? Tô acertando?"

    m "Não. Mas você pelo menos tem força nas mãos."

    mc "Obrigado."

    m "Normalmente o pessoal começa com mais medo."

    m "Você até que tá indo bem pra sua primeira vez, [mc]."

    mc "Valeu."

    m "Bom. Vejo que você entendeu o local da primeira posição. Agora você tem que ir com a mão esquerda um pouco pro lado."

    mc "Certo."

    m "E com a direita pra fora."

    m "Isso. Já tá melhor. Agora um pouco mais forte."

    mc "..."

    m "Ok. Continue fazendo esse movimento, mas cuidado para não ficar muito tempo em um mesmo ponto."

    mc "Entendi."

    m "Enquanto você brinca com as minhas costas, eu vou perguntar pra você o nome das posições, ok?"

    mc "Quê?!"

    m "Pra ver se você gravou direitinho. Quando você acertar todas vamos estar em um bom ponto pra primeira aula."

    mc "O-ok... Acho que eu consigo."

    m "Assim que se fala. Eu vou perguntar na ordem que você aprendeu. É muito babinha."

    m "Então vamos lá:"

    label karli_aula1_teste:

        scene massagem kita with Dissolve(1.0)

        m "Qual o nome da primeira posição, a da parte superior?"

        menu:
            "Higashi":


                jump k_a1_errou
            "Kita":


                m "Isso mesmo!"
            "Nishi":


                jump k_a1_errou
            "Minami":


                jump k_a1_errou

        m "Qual o nome da segunda posição, na base das costas?"

        menu:
            "Nishi":


                jump k_a1_errou
            "Kita":


                jump k_a1_errou
            "Minami":


                jump k_a1_errou
            "Higashi":


                m "Acertou, mizerávi!"

        m "E o nome da terceira posição? A dos pés."

        menu:
            "Minami":


                m "Certinho."
            "Nishi":


                jump k_a1_errou
            "Higashi":


                jump k_a1_errou
            "Kita":


                jump k_a1_errou

        m "E a última. Qual é a do cotovelo?"

        menu:
            "Nishi":


                m "Perfeito!"
            "Minami":


                jump k_a1_errou
            "Kita":


                jump k_a1_errou
            "Higashi":


                jump k_a1_errou

        jump k_a1_acertou

    label k_a1_errou:

        m "Não."

        m "Vamos voltar do começo, até você conseguir todos."

        scene black with dissolve

        jump karli_aula1_teste

    label k_a1_acertou:

        m "Muito bem. Você acertou todas. Parabéns!"

        mc "Valeu. Você que é uma excelente professora."

        m "Aí já não sei. Mas que eu sou boa na massagem eu sou."

    m "Bom. Acho que por hoje tá bom de brincar comigo."

    "..."

    scene salao massagem with Dissolve(1.0)

    mc envergonhado "E como foram meus movimentos? Suas perguntas meio que me desconcentraram."

    m "Imagino. Mas pelo menos minhas costas não tão doendo. É um começo."

    mc zerado "..."

    show karli meudeus with dissolve

    m "Impossível que você realmente achou que ia acertar logo de primeira..."

    mc envergonhado "... Quem sabe?"

    m "Nossa senhora, [mc]. Quantos anos você tem?"

    m "As coisas não são fáceis desse jeito que você tá pensando, não."

    mc desculpa "Ok! Não precisa esculachar."

    show karli normal with dissolve

    m "Vai chorar, é?"

    mc zerado "Claro que não..."

    m "Tava paracendo."

    mc normal "Para de pegar no meu pé."

    m "Tá. Por hoje tá bom."

    m "E sobre seu curso, eu acho que você progrediu muito bem hoje."

    m "Na sua próxima aula as coisas vão ficar mais interessantes."

    if karli_seducao >= 4:

        mc tarado "Quem sabe eu não convença você a tirar a roupa?"

        show karli provocando with dissolve

        m "Quem sabe..."

    m "E agora pode ir vazando que eu vou tomar um banho na minha banheira aquecida..."

    mc safado "Será que eu não posso..."

    scene salao massagem with hpunch

    m "Tchau!"

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_1","massagem","aula")
            
            if mc_massagem == 0:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    scene salao massagem with hpunch

    mc surpreso "Não precisa me empurrar!"

    "..."

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula2:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    show karli normal with dissolve

    m "E não é que você voltou mesmo?"

    mc normal "Claro. Eu gostei muito da nossa aula anterior."

    if karli_seducao >= 4:

        m "Eu sei que você gostou foi de pegar em mim..."

        mc safado "Isso também é claro."

    m "Fico feliz que você esteja gostando do curso. Mas ainda é só o começo. A coisa vai pegar fogo agora."

    mc desconfiado "Não precisa tentar colocar medo em mim."

    m "Não estou colocando medo. Mas eu vi que você ficou decepcionado aula passada porque não me deu barato."

    mc envergonhado "É... fiquei um pouco, sim. Achei que eu ia conseguir fazer algo."

    show karli meudeus with dissolve

    m "Por isso que tô falando, tonto. Não é de uma hora pra outra que você vai fazer isso."

    m "Se você não ajustar isso, você vai acabar desistindo antes da hora. A vida não é fácil."

    mc "Ok, ok. Não precisa começar a dar lição de moral sobre a dificuldade da vida."

    m "Existem pessoas passando por dificuldades no mundo..."

    mc zerado "Tá bom. Agora você só tá zuando."

    show karli normal with dissolve

    m "Falando sério, eu quero que você dê o seu melhor nas nossas aulas e dê tempo ao tempo."

    mc normal "Pode deixar."

    m "Então chega de papo e vamos pra sala de massagem."

    scene salao massagem with Dissolve(1.0)

    mc normal "Aqui tem sempre um cheiro muito bom."

    show karli feliz with dissolve

    m "Eu uso velas aromatizadas para fazer um clima. Ajuda a relaxar e aumenta a sensação de bem-estar."

    mc "Você realmente sabe o que tá fazendo."

    m "Claro. Eu sou uma profissional. Posso gostar de fazer piadas de humor questionável, mas meu trabalho eu levo à sério."

    menu:
        "Eu acho isso realmente incrível.":


            mc charmoso "A seriedade que você atua é impressionante."

            m "Valeu, [mc]. Mas é que eu realmente gosto do que eu faço."

            m "Infelizmente não dá tanto dinheiro, mas eu não vou desistir."

            mc serio "..."
        "Você deveria pegar mais leve.":


            mc normal "Vai acabar ficando com rugas se não pegar mais leve."

            show karli meudeus with dissolve

            m "E você sabe o que de qualquer coisa?"

            mc "Só tô falando que levar tudo muito à sério pode ser ruim também."

            m "Pra mim sua opinião vale tanto quanto a Rebecca Black vale pro mundo da música."

            mc zerado "Rebecca quem?"

            m "..."

    show karli normal with dissolve

    m "Como eu falei na aula passada, hoje você vai começar a aprender a sequência dos pontos fundamentais."

    mc normal "Ah, verdade. Eu me lembro."

    mc "Você disse que a sequência dos pontos é que vai definir como a massagem vai influenciar a pessoa."

    m "Exatamente. Vamos começar com sequências simples e a cada aula vou te passar mais e mais complexas. Se prepare!"

    menu:
        "Isso parece problemático...":


            mc incomodado "Isso parece bem complicado..."

            m "[mc]! Não vai desistir, né? É a segunda aula ainda."

            mc envergonhado "Cla-claro que não."
        "Eu quero começar excitando você.":


            $ karli_seducao += 1

            mc charmoso "A primeira sequência que quero aprender é como excitar você."

            m "Hmmm..."

            m "Vou pensar na possibilidade."

            mc safado "..."
        "Vou me esforçar para fazer o melhor.":


            mc serio "Vou me esforçar o máximo para aprender todas as sequências."

            m "Boa! Com esforço e paciência você vai chegar lá mais rápido que você imagina."

            mc normal "Pode confiar."

    m "Como de costume, eu quero que você tire as roupas e deite na mesa."

    m "Vou começar mostrando a sequência pra você e então será sua vez de praticar."

    m "Tudo bem?"

    menu:
        "Hoje você vai ter que tirar a roupa comigo.":


            $ karli_seducao += 1

            $ karli_roupao = True

            mc charmoso "Hoje você não escapa. Vai ter que tirar a roupa também."

            show karli provocando with dissolve

            m "Será que eu tiro?"

            mc safado "..."

            m "..."

            m "Hoje não."

            m "Mas se você fizer tudo direitinho na aula eu prometo que na próxima eu te acompanho."

            mc tarado "Combinado. Vou cobrar, hein?"

            m "..."

            mc "Pronto."
        "Pronto.":


            mc normal "..."

            m "Nem comento mais nada sobre isso."

            mc "Sou incrível, fala aí."

            m "Pior é que nem posso negar..."

    m "Agora vai pra mesa e fique confortável."

    mc normal "Beleza."

    "..."

    scene massagem mc with Dissolve(1.0)

    "Tô começando a me viciar nas massagens da [m]. Meu corpo tá muito melhor e tô com menos dor desde que comecei a vir aqui."

    "Parece que massagem realmente é terapêutica. Depois tenho que agradecer a [c] por esse vale. Se não fosse ela, eu..."

    m "{size=15}[mc]...{/size}"

    mc "?"

    m "Acorda, filho!"

    mc "Ah, desculpa."

    m "Tava viajando aí?"

    mc "Mais ou menos. Desculpa."

    m "Tudo bem. Mas preste atenção no que eu vou falar agora."

    scene massagem e1 with Dissolve(1.0)

    mc "Hmmm..."

    m "Pare de relaxar demais e preste atenção!"

    mc "Vou tentar..."

    m "..."

    m "A sequência de hoje vai ser muito simples. Serão apenas três pontos e sem repetição."

    m "Quero dizer... Você vai estimular uma vez cada um desses três pontos na ordem que eu disser e sucesso."

    mc "Parece bem simples."

    m "Mais ou menos. Você vai ter que se lembrar dos nomes da aula anterior, que você já deve ter esquecido."

    mc "..."

    m "E tem um {b}novo detalhe{/b} muito importante. A ordem da sequência não é o único elemento."

    m "Você precisa de {b}ritmo{/b}."

    mc "Ritmo? Igual música?"

    m "Isso aí. Se você demorar demais em um ponto, começa a incomodar. Então não dá pra você ficar pensando qual é o próximo ponto."

    m "Você precisa estimular e trocar. Quanto mais etapas a sequência tem, mais rápido você deve passar de um ponto pra outro."

    m "Você precisa manter o {b}ritmo{/b} para não cansar a pessoa e chegar no resultado que você deseja."

    mc "Acho que tô entendendo."

    m "Que bom. Na prática isso quer dizer que é só você não demorar demais pra trocar de ponto."

    m "A partir de hoje, você vai ter então duas tarefas nas nossas aulas."

    m "Primeiro, você precisa acertar a ordem que eu vou passar para você."

    m "E segundo, você não pode demorar demais para passar de um ponto para outro."

    mc "É tipo então decorar e não enrolar pra escolher."

    m "Exatamente. Essa é a teoria. Mas não esqueça que existem outras coisas, como a força e a técnica."

    m "Não adianta você acertar o ponto e o ritmo, mas machucar ou estimular da forma incorreta."

    mc "Entendi. Essa parte eu acho que vou pegar com a prática."

    m "Concordo. Foque na ordem e no ritmo e o resto praticando você vai chegar lá."

    if karli_seducao >= 5:

        m "E é por isso que tô deixando você pegar no meu corpo delicioso."

        mc "Achei que é porque você gostasse de sentir minha mão te apertando."

        m "Isso não vem ao caso..."

        mc "Não vai negar?"

        m "..."

    mc "Ok. Focar no ritmo e na ordem. Fechou."

    m "Então agora pode se levantar e se preparar. Eu vou te falar a ordem e você já começa."

    "..."

    scene salao massagem with Dissolve(1.0)

    m "Vou me ajeitar aqui."

    mc "Vai ficar de roupa igual a outra vez?"

    m "Sim."

    m "Certo. Pode colocar a mão nos meus ombros e começar com a primeira posição. O {b}Kita{/b}."

    "Eu já esqueci todos os nomes..."

    mc serio "Ok."

    scene massagem kita with Dissolve(1.0)

    mc "..."

    m "..."

    mc "Estou fazendo certo?"

    m "A força está boa. Mas ainda falta muito. Continue praticando."

    mc "Ok."

    m "..."

    m "Certo. Agora vamos para seu teste. Você vai ter que aplicar três movimentos na ordem que eu disser, ok?"

    mc "Tomara que eu esteja pronto."

    m "Não tem problema se você errar. Você está aqui pra aprender. Vamos voltar quantas vezes forem necessárias."

    mc "Assim fico mais calmo."

    m "Legal. Agora escute bem."

    m "Vou te falar a sequência. São apenas três movimentos."

    label k_a2_teste:

        $ timeout_label = "k_a2_teste_demorou"

        m "A sequência é {b}Higashi{/b}, {b}Nishi{/b} e {b}Kita{/b}."

        m "Pode começar."

        menu:
            "Kita":


                m "Não! Ordem errada!"

                m "Comece de novo."

                jump k_a2_teste
            "Higashi":


                m "Muito bem."

                "Acertei o primeiro movimento. Mas não posso me descuidar da força e de manter os movimentos no lugar certo."

                "Qual era o segundo ponto?"

                menu:
                    "Kita":


                        m "Não! Ordem errada!"

                        m "Comece de novo."

                        jump k_a2_teste
                    "Higashi":


                        m "Não! Ordem errada!"

                        m "Outra vez."

                        jump k_a2_teste
                    "Minami":


                        m "Não! Ordem errada!"

                        m "Comece de novo."

                        jump k_a2_teste
                    "Nishi":


                        m "Aí mesmo. Esse é o ponto."

                        "Beleza. Consegui acertar o segundo ponto. Agora só falta mais um."

                        "Tenho que tomar cuidado para minhas mãos ou meu cotovelo não tocarem onde não devem."

                        "Só falta um. O terceiro ponto era..."

                        menu:
                            "Kita":


                                m "Isso aí! Agora continue assim..."

                                m "Hmmm..."

                                mc "Tá gostando?"

                                m "Sim... Você tá indo bem..."

                                "Boa! Consegui acertar os três movimentos!"

                                jump k_a2_teste_sucesso
                            "Higashi":


                                m "Não! Ordem errada!"

                                m "Comece de novo."

                                jump k_a2_teste
                            "Minami":


                                m "Não! Ordem errada!"

                                m "Outra vez."

                                jump k_a2_teste
                            "Nishi":


                                m "Não! Ordem errada!"

                                m "Comece de novo."

                                jump k_a2_teste
            "Minami":


                m "Não! Ordem errada!"

                m "Outra vez."

                jump k_a2_teste
            "Nishi":


                m "Não! Ordem errada!"

                m "Outra vez."

                jump k_a2_teste

    label k_a2_teste_demorou:

        m "..."

        m "Você ficou tempo demais na mesma posição."

        m "Pode recomeçar."

        jump k_a2_teste

    label k_a2_teste_sucesso:

        $ timeout_label = None

        m "..."

        m "Seus movimentos estão um pouco desajeitados. Mas você está fazendo muito bem pra sua primeira vez."

        m "Pode continuar..."

        mc "..."

        "..."

        m "Acho que agora está bom. Pode parar."

        mc "Ok."

        m "Deixa eu me levantar."

        scene salao massagem with Dissolve(1.0)

        m "Hmmm..."

        show karli normal with dissolve

        m "Você foi melhor do que eu imaginava, sabia?"

        m "Ainda tem chão pra você ficar bom, mas foi realmente surpreendente."

        mc feliz "Que bom que você gostou."

        m "Gostei. Espero você na próxima aula pra gente continuar."

        mc normal "Pode ter certeza que eu vou vir."

        m "Tchau, [mc]."

        m "Até, [m]."


















    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_2","massagem","aula")
            
            if mc_massagem == 1:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula3:

    show karli normal with dissolve

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    m "Tô começando a acreditar que você realmente quer aprender minha arte."

    menu:
        "Com certeza. Vou até o fim.":


            mc charmoso "Eu não sou de desistir. Quero aprender tudo até ser tão bom quanto você."

            m "Não exagere."

            mc "No mínimo fazer o suficiente pra te deixar orgulhosa de mim."

            m "Você tá me saindo um bom discípulo, viu? Pelo menos no papo."

            mc "Você vai ver na minha técnica também."

            m "Quero só ver, [mc]."
        "Estou mais interessado em você na verdade.":


            $ karli_seducao += 1

            mc charmoso "Na verdade, acho que eu estou mais interessado em te ver do que na massagem."

            show karli provocando with dissolve

            m "Toda vez que você vem aqui você vem com essa fala mansa."

            mc "Eu só tô sendo sincero com você."

            m "..."

            m "Não sei se fico lisongeada ou se fico brava por você não estar levando minha arte à sério."

            mc "Claro que eu estou levando à sério. É só que levo você mais à sério ainda."

            m "..."

            show karli meudeus with dissolve

            m "Tá! Chega de cantadas por hoje."

            mc "Não precisa ficar vermelha."

            m "Quem aqui tá vermelha, mané?!"

            mc "..."

            m "Que droga... Você vai me pagar..."

            m "..."

            m "Pronto. Tô melhor."

    m "Sobre hoje."

    show karli normal with dissolve

    m "Vamos continuar com o exercício de ontem. Vou te passar uma sequência com mais dois pontos."

    m "Você vai ter menos tempo pra fazer a troca de movimentos também."

    mc desconfiado "Mais pontos e menos tempo?!"

    mc desconfiado "Tá fazendo isso de propósito só pra eu me ferrar?"

    show karli satisfeita with dissolve

    m "Para de ser chorão."

    m "Eu preciso pegar pesado com você ou você vai demorar muito pra melhorar."

    m "Você está indo super bem. Eu sinto que posso pegar mais pesado nas aulas."

    mc zerado "Era pra eu me sentir motivado?"

    show karli normal with dissolve

    m "Não funcionou?"

    mc "..."

    m "Chega de papo. A sala de massagem nos espera. Bora lá."

    hide karli with dissolve

    mc normal "Vamos..."

    "..."

    scene salao massagem with Dissolve(1.0)

    show karli normal with dissolve

    m "Como de costume, pode tirar a roupa."

    if karli_roupao:

        mc charmoso "Pode parando aí."

        m "?"

        mc "Se eu me lembro bem ontem alguém prometeu que ia tirar a roupa comigo se eu fizesse tudo certinho."

        mc "E pelo que consta eu fiz tudo certinho. Até recebi elogios da professora."

        show karli provocando with dissolve

        m "..."

        m "Você não vai desistir, né?"

        mc "Pode ter certeza que não. Eu quero muito poder ver você."

        m "..."

        label karli_roupao:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("karli_roupao","roupao","aula")

            m "Ok... Você venceu."

            $ karli_roupao = True

            m "Vou colocar o roupão que eu dou pras minhas clientes."

            if karli_seducao >= 5:

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("karli_seducao_1","roupao","aula")

                show karli provocando with dissolve

                m "Vai poder me massagear só de calcinha e sutiã. Era isso que você queria desde o começo?"

                mc charmoso "Desde que a gente começou o curso, eu quero poder ver você e pegar em você."

                m "... Você é impossível..."

                hide karli with dissolve

                m "Mas não quer dizer que seja ruim..."

                mc "..."

                "As coisas com ela estão progredindo muito bem. Eu preciso continuar mostrando confiança e deixar claro meus objetivos."

                "Tenho que tomar cuidado pra não ser um idiota. Conquistar não é babar nela como um cachorro."

                "..."

                "Deixa eu tirar minha roupa também."

                "..."

                "..."

                m "Pronto pra ficar duro?"

                mc "Opa. Com certeza."

                show karli roupao_provocando with Dissolve(1.0)

                pause

                m "E então?"

                m "O que achou?"

                mc safado "Linda..."

                m "..."

                m "Mas você só pode olhar e treinar massagem. Não venha com ideias estranhas só porque tô vestida assim."

                mc charmoso "Pode deixar. Nunca que eu vou fazer alguma coisa sem sua vontade."

                m "É o mínimo. Mas se você continuar sendo um cavalheiro e se dedicar nas aulas, quem sabe no futuro..."

                mc "Pode ter certeza que eu vou continuar sendo um bom aluno, professora."

                m "Ai, você..."

                jump k_a3_continuar
            else:


                "..."

                "Vou tirar a minha roupa também."

                "..."

                "..."

                m "Pronto."

                show karli roupao_provocando with dissolve

                m "O que achou?"

                mc charmoso "Tá linda."

                m "Valeu, [mc]."

                m "Mas você só pode olhar e treinar massagem. Não venha com ideias estranhas só porque tô vestida assim."

                mc charmoso "Pode deixar. Nunca que eu vou fazer alguma coisa sem sua vontade."

                m "É o mínimo. Mas se você continuar sendo um cavalheiro e se dedicar nas aulas, quem sabe no futuro..."

                mc "Pode ter certeza que eu vou continuar sendo um bom aluno, professora."

                jump k_a3_continuar
    else:


        mc serio "..."

        menu:
            "Nessa altura já me acostumei.":


                mc normal "Ok... Nessa altura já me acostumei."

                m "Você vê que não tem nada de mais. É só algo essencial pra você poder ter todos os benefícios da massagem."

                mc "Verdade."

                "..."

                mc "Pronto."

                m "Continua rápido..."

                mc "Você tem que se acostumar com isso também."

                m "Verdade..."
            "Você tem que tirar também.":


                $ karli_seducao += 1

                mc normal "Sem querer se repetitivo, mas por que só eu tiro a roupa?"

                mc "Agora eu também estou praticando a massagem em você."

                m "Hmmm..."

                jump karli_roupao

    label k_a3_continuar:

        m "Agora que a gente tá pronto, vamos pra mesa de massagem. Quero ver se hoje você vai se sair bem igual na aula passada."

        mc charmoso "Vou dar meu melhor."

        "..."

    scene massagem mc with Dissolve(1.0)

    m "Não preciso nem falar pra você deitar e relaxar."

    mc "Verdade. É a força do hábito."

    m "Mas ainda estamos no começo do curso, viu? Não vai achando que já pode sair daqui e ir distribuindo massagens."

    m "Só se forem massagens bem meia tigela. E nem pense em falar que aprendeu comigo."

    mc "Pode deixar. Não vou sujar seu nome por aí."

    m "Bom... Deixa eu começar."

    if karli_roupao:

        scene massagem roupao_e1 with Dissolve(1.0)
    else:


        scene massagem e1 with Dissolve(1.0)

    m "Hoje, antes do teste, vou gastar um tempinho te dando uma massagem completa."

    mc "Uou!"

    m "Quero que você sinta na prática a força e a forma como faço cada movimento."

    mc "Ok."

    mc "Hmmm..."

    m "É bom, né?"

    mc "Com certeza..."

    if karli_seducao >= 5:

        m "Apertar você assim, com nós dois quase sem roupa..."

        m "Isso tá mexendo um pouco comigo..."

        mc "Tá mexendo comigo também."

        m "Ai..."

    "..."

    "..."

    mc "Se você continuar assim eu vou dormir logo logo..."

    m "Ok. Então é melhor parar."

    m "Deu pra sentir e entender melhor os movimentos, não deu?"

    mc "Com certeza."

    m "Certo. Então vamos trocar de lugar e eu vou te passar o exercício de hoje."

    scene salao massagem with Dissolve(1.0)

    mc "Beleza. Pode deitar e relaxar."

    m "Ei!"

    mc normal "Não é assim que se fala?"

    m "..."

    if karli_roupao:

        mc desconfiado "Que foi?"

        show karli roupao_provocando with dissolve

        m "Não sei se tiro o roupão..."

        mc charmoso "Você disse que dessa vez você ia fazer igual eu. E eu fiquei só de cueca."

        show karli roupao_meudeus with dissolve

        m "Eu sei... Mas eu nunca fiz isso..."

        mc charmoso "Não precisa ficar assim, [m]. É só uma massagem. Eu juro que não vou tentar nada mais que isso."

        m "Promete?"

        mc "Claro. Prometo."

        m "Tudo bem..."

        hide karli with dissolve

        "..."

    m "Ok. Estou pronta. Pode começar com a primeira posição igual da outra vez."

    if karli_roupao:

        scene massagem roupao_kita with Dissolve(1.0)

        pause
    else:


        scene massagem kita with Dissolve(1.0)

    mc "Eu lembro. O nome deste ponto é Kita, né?"

    m "Isso aí, [mc]. Você tem alguma salvação..."

    mc "..."

    m "Hmmm..."

    m "Você está melhor do que na aula passada."

    mc "A massagem que você me deu hoje ajudou bastante."

    m "Tô vendo. Seus movimentos estão mais fluidos."

    mc "Agora você já tá chique demais."

    m "Calado... Deixa eu aproveitar um pouco..."

    if karli_seducao >= 5:

        m "Hmmm..."

        mc "Parece que você tá gostando mesmo."

        m "Não vejo a hora que você aprenda como dar prazer de..."

        mc "Quê?"

        m "Nada não..."

    "..."

    m "Ok. Está bom por hoje. Pronto para o exercício?"

    mc "Talvez a gente pudesse pular essa parte."

    m "Engraçadinho."

    m "Igual da outra vez, eu vou te passar os {b}5 pontos{/b} e você vai ter que estimular eles na ordem."

    mc "Certo."

    m "Não se esqueça do {b}ritmo{/b}. O tempo de cada movimento será menor do que da outra vez."

    mc "Ainda tem isso, verdade..."

    m "Relaxe e vamos lá."

    label k_a3_teste:

        $ timeout_label = "k_a3_teste_demorou"
        $ timeout = 4.0

        m "A ordem é {b}Kita{/b}, {b}Nishi{/b}, {b}Kita{/b} novamente, {b}Minami{/b} e {b}Higashi{/b}."

        m "Pronto? Pode começar."

        menu:
            "Kita":


                m "Esse é o ponto."

                "Acertei o primeiro movimento."

                "Agora o segundo ponto..."

                menu:
                    "Kita":


                        m "Não! Ordem errada!"

                        m "Comece de novo."

                        jump k_a3_teste
                    "Higashi":


                        m "Não! Ordem errada!"

                        m "Outra vez."

                        jump k_a3_teste
                    "Minami":


                        m "Não! Ordem errada!"

                        m "Comece de novo."

                        jump k_a3_teste
                    "Nishi":


                        m "Aí mesmo."

                        m "Hmmm..."

                        "Tenho que focar no meu cotovelo, pra não forçar demais."

                        "O terceiro ponto era?"

                        menu:
                            "Kita":


                                m "Muito bem..."

                                "Boa! Era aqui de novo."

                                "Agora o quarto ponto."

                                menu:
                                    "Kita":


                                        m "Não! Ordem errada!"

                                        m "Pode voltando do começo."

                                        jump k_a3_teste
                                    "Higashi":


                                        m "Não! Ordem errada!"

                                        m "Comece de novo."

                                        jump k_a3_teste
                                    "Minami":


                                        m "Certinho..."

                                        "Esse era o quarto. Falta apenas o último. Vamos lá!"

                                        menu:
                                            "Kita":


                                                m "Não! Ordem errada!"

                                                m "Outra vez."

                                                jump k_a3_teste
                                            "Higashi":


                                                m "Hmmm..."

                                                m "Era bem aí o último."

                                                "Boa! Consegui todos os cinco pontos!"

                                                jump k_a3_teste_sucesso
                                            "Minami":


                                                m "Não! Ordem errada!"

                                                m "Outra vez."

                                                jump k_a3_teste
                                            "Nishi":


                                                m "Não! Ordem errada!"

                                                m "Comece de novo."

                                                jump k_a3_teste
                                    "Nishi":


                                        m "Não! Ordem errada!"

                                        m "Comece de novo."

                                        jump k_a3_teste
                            "Higashi":


                                m "Não! Ordem errada!"

                                m "Comece de novo."

                                jump k_a3_teste
                            "Minami":


                                m "Não! Ordem errada!"

                                m "Outra vez."

                                jump k_a3_teste
                            "Nishi":


                                m "Não! Ordem errada!"

                                m "Comece de novo."

                                jump k_a3_teste
            "Higashi":


                m "Não! Ordem errada!"

                m "Comece de novo."

                jump k_a3_teste
            "Minami":


                m "Não! Ordem errada!"

                m "Outra vez."

                jump k_a3_teste
            "Nishi":


                m "Não! Ordem errada!"

                m "Outra vez."

                jump k_a3_teste

    label k_a3_teste_demorou:

        m "..."

        m "Você demorou demais nesse ponto."

        m "Pode recomeçar."

        jump k_a3_teste

    label k_a3_teste_sucesso:

        $ timeout_label = None

        m "Excelente. Você conseguiu de novo."

        m "Foi um pouco forte e desengonçado demais em alguns dos movimentos."

        mc "Desculpa. Eu tava meio nervoso."

        m "Isso é normal."

        m "Pode parar agora. Deixa eu levantar e me vestir."

    scene salao massagem with Dissolve(1.0)

    if karli_roupao:

        show karli roupao_normal with dissolve
    else:


        show karli normal with dissolve

    m "Você foi muito bem. Me surpreendeu de novo."

    mc charmoso "Eu disse que seria um bom aluno."

    m "Se continuar assim você vai chegar longe, [mc]."

    mc "Obrigado."

    m "Claro que ainda faltam mais ou menos umas 6 ou 7 aulas. Mas se você aguentar até o final, vai ser incrível!"

    mc feliz "Eu sinto que tô melhorando também."

    m "E tá mesmo. Você foi incrível hoje pra um iniciante."

    m "Eu devo ser mesmo uma boa professora."

    if karli_seducao >= 5:

        mc safado "E uma professora muito boa também..."

        m "Safado..."
    else:


        mc normal "..."

    m "É isso por hoje. Tá liberado."

    mc charmoso "Obrigado, [m]. Valeu mesmo pela paciência."

    m "Relaxa. Não liga pra isso."

    m "Beijos, [mc]."

    mc "Beijo."

    hide karli with dissolve


















    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_3","massagem","aula")
            
            if mc_massagem == 2:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    scene salao geral with Dissolve(1.0)

    mc desconfiado "Hm?"

    show gina provocando at esquerda with dissolve

    "Senhora" "... E quem é você, gatinho?"

    mc "..."

    "Senhora" "A [m] tá aí?"

    mc "Ela tá na sala ali."

    "Senhora" "Obrigada. Até outra hora..."

    hide gina with dissolve

    mc "..."

    jump call_cidade

label karli_aula4:

    show karli preocupada with dissolve

    m "Hmm..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    m "Então, [mc]. Acho que hoje não vamos poder praticar."

    mc incomodado "Ué? Por quê?"

    m "É que eu tenho um compromisso. Estou esperando uma pessoa..."

    mc desconfiado "Então você tem namorado?"

    m "Não..."

    mc "Namorada?"

    m "Não é isso..."

    m "É só que..."

    menu:
        "Tá tudo legal com você?":


            mc preocupado "Você não parece normal. Tá tudo legal com você?"

            m "Sim... É que eu tô meio..."

            mc normal "Não tô entendendo nada. Desembucha, mulher!"

            m "Eu..."

            show karli preocupada at esquerda with move

            show gina seria with dissolve

            show gina seria at direita with move

            gina "Voltei, fedelha. Espero..."

            show gina provocando at direita with dissolve

            gina "Hmmm..."

            gina "Oi, jovem. Eu lembro de você."

            mc desconfiado "Eu vi a senhora aqui da outra vez."
        "Ok. Vou indo nessa. Volto outro dia.":


            mc normal "Ok. Não vou encher o saco. Volto outro dia, ok?"

            m "Tá... Beijo."

            mc "Beijo."

            hide karli with dissolve

            show salao geral with hpunch

            $ renpy.vibrate(1)

            "{i}TUMP{/i}"

            show gina seria with dissolve

            gina "Ei! Olha por..."

            show gina provocando with dissolve

            gina "Oi, jovem. Eu lembro de você."

            mc desconfiado "Eu vi a senhora aqui da outra vez."

            show gina provocando at direita with move

            show karli preocupada with dissolve

            show karli preocupada at esquerda with move

    gina "Infelizmente eu tenho que vir aqui mais vezes do que eu gostaria."

    $ gina_nome = "Gina"

    gina "Meu nome é Genoveva, mas pode me chamar de [gina]."

    mc normal "Eu sou o [mc]. Muito..."

    m "O [mc] já tava de saída."

    gina "Sério? Que pena..."

    menu:
        "Não tava, não. O que está acontecendo?":


            mc normal "Na verdade eu não tava saindo ainda. Vocês são amigas?"

            m "..."

            gina "Mais ou menos."

            mc desconfiado "..."
        "Acho que eu posso ficar mais um pouco.":


            mc desculpa "Eu não queria atrapalhar vocês."

            m "..."

            gina "Não atrapalha, jovem."

    gina "A [m] sabe porque eu vim aqui."

    m "Pois é. Não se preocupe que eu já estou quase com ele. Eu vou na casa da senhora amanhã."

    show gina seria with dissolve

    gina "Amanhã?"

    m "Eu prometo..."

    mc preocupado "..."

    gina "Olha a cara que o [mc] tá fazendo. Não quero perturbar ele à toa. Combinado, pode passar lá amanhã."

    mc desconfiado "..."

    m "Obrigada, [gina]."

    gina "Agradeça esse rapaz. Até outra oportunidade, [mc]. Foi um prazer."

    mc normal "O prazer é meu."

    hide gina with dissolve

    show karli preocupada at centro with move

    m "..."

    mc preocupado "O que está havendo aqui?"

    m "Hmm..."

    show karli normal with dissolve

    m "Esquece! Não é assunto pra plebeus."

    m "São apenas algumas coisas que eu tenho que resolver com ela."

    m "Aliás, agora que ela foi embora e ficou certo da gente conversar outro dia, podemos ir pra sua aula."

    mc preocupado "Desculpa, [m]. Mas eu tô meio preocupado com você. Você não pode me falar o que tá havendo?"

    if karli_roupao:

        m "É impressão minha ou você tá negando me ver de roupão?"

        mc "Não é isso..."

    show karli meudeus with dissolve

    m "Ok ok!"

    m "Pode parar de insistir. Eu vou te explicar."

    m "Mas você precisa prometer que não vai se intrometer em coisa minha. Promete?"

    menu:
        "Prometo.":


            mc charmoso "Prometo. Não quero atrapalhar."

            m "Então tá. Você prometeu, hein."

            mc "..."
        "Depende do que for. Eu quero te ajudar.":


            mc preocupado "Não quero passar por cima de você. Você é adulta e pode resolver suas coisas sozinha."

            mc "Só que eu me considero seu amigo. Não posso prometer que não vou te ajudar."

            m "Às vezes você é tão cabeça dura..."

            m "Não quero você complicando minha situação ainda mais."

            mc charmoso "Eu prometo que se eu fizer qualquer coisa que atrapalhe, você tem o direito de me dar uma surra."

            m "..."

            m "Tá. Mas por favor presta atenção se você for querer fazer algo."

    show karli preocupada with dissolve

    m "A [gina] é a dona deste prédio aqui."

    mc surpreso "Ela é a dona do prédio que a gente mora?!"

    m "Verdade... Você mora aqui, né?"

    mc normal "Pois é. Não sei porque nunca falamos sobre isso."

    m "Então. Provavelmente você alugou ou comprou o apartamento com outra pessoa e não diretamente com ela."

    mc serio "Sim. Eu aluguei com um senhor quando me mudei pra cá por conta do trabalho."

    mc desculpa "Até parece que eu ia ter dinheiro pra comprar um imóvel aqui na ilha."

    m "Então! O preço do aluguel aqui é caríssimo, mas é o único lugar que eu consegui."

    m "E mesmo tendo alguns clientes, incluindo famosos como a [c] eu não consigo ganhar o suficiente pra pagar o aluguel."

    mc zerado "E provavelmente você não tá vendendo muito bem os produtos também, porque você é uma péssima vendedora."

    m "Ei! Ok... Talvez você tenha razão..."

    m "Daí eu acabei arrumando um emprego de meio período no Tadaima pra ajudar com as despesas. Mas mesmo assim não é o suficiente."

    mc preocupado "Entendi..."

    m "Eu estou devendo pra [gina] e ela vem direto aqui me cobrar. Ela tá falando em me despejar agora."

    mc "Isso é muito ruim..."

    m "Se ela entrar na Justiça, ela vai ganhar com certeza. Eu vou ter menos de um mês pra sair daqui."

    mc preocupado "E não tem ninguém que possa te emprestar um dinheiro?"

    m "Não quero pedir ajuda pros meus pais e não tenho muitos amigos na ilha."

    mc "..."

    show karli normal with dissolve

    m "Tá vendo? Isso não tem nada a ver com você."

    mc incomodado "Claro que tem! Como vou terminar meu curso sem minha professora?"

    m "É. Tem isso..."

    menu:
        "Infelizmente não posso fazer nada.":


            mc triste "Eu entendo sua situação, mas eu também tô no fundo do poço..."

            m "E quem aqui pediu sua ajuda? Por isso não queria te contar."

            "Se eu não fizer nada, a [m] vai ter que deixar a ilha."

            "Eu provavelmente não vou conseguir terminar meu curso de massagem."

            if karli_seducao >= 5:

                "E todo o avanço que eu tava tendo pra conquistar ela vai pro buraco também."

            "Será que essa é a melhor escolha pra mim?"

            menu:
                "Não quero me meter na vida dela.":


                    $ karli_roupao = False
                    $ karli_ajudou = False

                    "Isso é problema demais e eu já tenho meus próprios problemas."

                    "Se ela tiver que se mudar vai ser ruim, mas a vida segue."

                    jump karli_nao_ajudou
                "Vou ajudar a [m] no que eu puder.":


                    "Pensando bem, não posso deixar ela na mão."

                    jump karli_ajudou
        "Eu vou te ajudar.":


            label karli_ajudou:

                $ karli_ajudou = True

                mc charmoso "Não posso te deixar na mão. Você é minha professora de massagem, e uma amiga."

                mc "Eu vou te ajudar."

                show karli meudeus with dissolve

                m "Não!"

                m "Isso era justamente o que eu não queria, [mc]!"

                mc desculpa "Eu sei. E sei que eu posso tá invadindo seu espaço."

                mc "Mas eu juro que eu tô fazendo isso pra te ajudar. É porque eu quero que você fique aqui."

                m "E se você complicar ainda mais minha situação?"

                m "E se você nem quiser mais continuar nossas aulas?"

                mc charmoso "Nunca que eu ia parar de vir aqui."

                if karli_seducao >= 5:

                    mc "Você sabe que eu tô mais ligado em você do que na massagem, né?"

                    m "Pior é que eu sei..."

                    mc "Não quero te perder, [m]."

                    m "Ai..."

                mc "E eu quero masterizar sua arte! Eu já te falei isso."

                m "Eu não sei o que pensar, [mc]..."

                mc "Não pense em nada. Fique tranquila. Tome um banho na banheira aquecida."

                mc normal "Eu vou pensar em alguma coisa e daí eu te falo se eu tiver alguma ideia."

                mc zerado "Porque infelizmente eu sou pobre demais pra te ajudar com dinheiro..."

                m "O-ok... Acho que eu vou pra banheira mesmo."

                m "Por favor. Não faça nenhuma loucura, tá?"

                mc charmoso "Pode deixar."

                m "Até depois."

                mc "Até."

                hide karli with dissolve

                "E eu tenho que tomar um rumo também... Vou dar uma andada por aí..."

    $ tempo += 1

    play sound "audio/som_5_cidadenoite.mp3"

    scene cidade angulo_1_noite with Dissolve(1.0)

    "Certo. Eu não posso falar bonito desse jeito e agora não fazer nada."

    "Não tenho dinheiro pra emprestar e também não tenho ninguém pra pedir..."

    mc triste "Será que eu devia ter ficado na minha?"

    "..."

    mc surpreso "Pera!"

    "Talvez eu possa começar trocando uma ideia com a tal da [gina]."

    "Fiquei com a impressão de que ela se interessou em mim."

    "Claro que a gente não vai transar. Mas pelo menos eu poderia ouvir o que ela tem pra dizer."

    "Talvez ela possa dar mais tempo pra [m] se eu conseguir virar amigo dela."

    "Ela não me pareceu terrível. A velha até foi bem simpática. Talvez ela acabe sendo melhor do que tá parecendo."

    "Certo. Preciso começar descobrindo o contato dela."

    "..."

    "Se ela é a dona do prédio, então deve ter algo sobre ela na portaria ou em algum lugar na entrada."

    "Deixar eu dar uma olhada."

    "..."

    scene apartamento portaria with Dissolve(2.0)

    "Uou. Nunca reparei como nosso prédio tá caindo aos pedaços..."

    "Como dizem, por fora bela viola, por dentro pão bolorento."

    mc zerado "Esse tipo de comentário entrega minha idade."

    mc desconfiado "Oi? Tem alguém aí?"

    "Pra que portaria se não tem porteiro?"

    "Deixa eu ver aqui o quadro de recados..."

    "..."

    "Achei! Que beleza! Tem o contato dela caso alguém queira locar apartamentos vagos."

    "Gina... telefone... 41... 69..."

    "Ainda é cedo."

    "Já vou ligar."

    "..."

    "Smartphone" "Tuuuuu.... Tuuuuuuu...."

    gina "Alô?"

    scene apartamento portaria with dissolve

    show mc telefone with dissolve

    mc "Oi, [gina]. Aqui é o [mc]. A gente conversou hoje mais cedo."

    mc "Desculpa tá ligando essa hora."

    gina "Imagina. Que bela surpresa você me ligar."

    mc "Eu não quero incomodar você, então vou direto ao ponto."

    gina "Claro, meu bem. Diga."

    mc "Eu queria conversar sobre o caso da [m]. Ela me falou que ela tá com o aluguel atrasado."

    gina "?"

    mc "[gina]?"

    gina "Oi, querido. Por que você tá ligando pra falar sobre a [m]?"

    mc "Eu sei que isso não tem nada comigo. Mas a [m] é minha amiga e eu queria fazer alguma coisa."

    mc "Eu sei que é idiota. Me desculpa..."

    gina "Meu bem, não fale uma coisa dessas. É incrível você estar fazendo isso pra ajudar sua amiga."

    mc "Sério?"

    gina "Claro. Eu acho muito honrado um homem fazer algo assim. Você é muito corajoso."

    mc "Obrigado."

    gina "E não posso deixar esse ato corajoso passar em branco."

    mc "..."

    gina "Fale pra [m] que ela não precisa vir aqui amanhã. Vamos esquecer esse atraso."

    mc "Sério? Isso é incrível, [gina]! Muito obrigado!"

    gina "Não precisa agradecer. É o mínimo que eu posso fazer por você."

    mc "Nem sei como agradecer..."

    gina "Não precisa, lindo. E eu ainda posso te ajudar mais."

    gina "Quando você tiver um tempo, venha aqui em casa. Vamos conversar pessoalmente e resolver juntos o problema da [m]."

    gina "Você parece uma boa pessoa. Tenho certeza que vai poder mediar essa nossa situação."

    mc "Com certeza. Pode contar comigo."

    gina "Perfeito."

    mc "Então assim que eu tiver um tempo eu falo pra [m] e dou um pulo aí."

    gina "Estarei esperando. Eu moro na Avenida Brasil, número 71. Fica no centro da capital."

    mc "Beleza. É rápido chegar aí de ônibus. Pode deixar comigo, [gina]. E obrigado novamente."

    gina "Beijão, querido. Te espero."

    mc "Beijo."

    hide mc with dissolve

    "..."

    "Uou! Isso foi incrível! Uma rápida conversa e agora a [m] vai ter mais tempo pra pagar o aluguel!"

    mc feliz "Ela vai ficar muito feliz. Tenho que contar pra ela urgente."

    "..."

    scene salao geral with Dissolve(1.0)

    mc feliz "[m]! [m]! Ainda tá aí?! Oii!"

    "..."

    show karli roupao_preocupada with dissolve

    m "Calma, maldito. O que aconteceu?"

    mc zerado "Tava na banheira até agora?"

    m "Não enche..."

    mc feliz "Tudo bem. Isso não importa. Tenho uma excelente notícia!"

    m "?"

    mc normal "Eu falei com a [gina] e ela disse que você não precisa levar o dinheiro pra ela amanhã."

    m "Quê?!"

    mc "Ela disse pra você esquecer o atraso e não se preocupar com isso agora."

    m "Impossível..."

    mc feliz "Tô falando sério!"

    m "Mas como?"

    mc normal "Eu peguei o telefone dela aqui na portaria e liguei pra ela. Ela foi super gente fina comigo."

    mc "Disse que você não precisa se preocupar com o pagamento e pra eu ir na casa dela um dia pra gente resolver o seu problema."

    m "Isso é tão estranho, [mc]... Mas você parece tão animado. Eu..."

    show karli roupao_normal with dissolve

    m "Eu nem sei como te agradecer."

    m "Tudo isso ainda está muito estranho, mas graças a você não vou ser despejada."

    mc normal "Relaxa. Não foi nada de mais. A [gina] foi super bacana."

    m "Isso que me preocupa. Mas você é adulto e sabe onde tá se metendo."

    m "Você pretende ir na casa dela?"

    menu:
        "Não sei. Ainda tô pensando nisso.":


            mc desculpa "Não sei ainda. Quero pensar com calma."

            m "Você tem toda razão. Tome cuidado."

            mc normal "Pode deixar."
        "Sim. Eu quero resolver seu problema.":


            mc charmoso "Eu vou fazer o que for preciso pra que você não seja despejada."

            show karli roupao_preocupada with dissolve

            m "Eu agradeço por toda a ajuda, mas por favor tome cuidado, [mc]."

            mc normal "Não se preocupe. Ela tá sendo legal de verdade comigo."

            m "Ok... Mas não faça nada estranho por minha causa, tudo bem?"

            mc "Pode deixar."

    m "Hmmm..."

    show karli roupao_normal with dissolve

    m "A hora tá meio avançada, mas acho que não podemos deixar você sem sua aula."

    m "Ainda mais depois de tudo o que você fez pra me ajudar. O que acha?"

    mc normal "Com certeza. Eu tô dentro."

    m "Então vamos lá!"

    hide karli with dissolve

    m "{size=15}Você me deixou muito animada! Vai ter que fazer 10 pontos em metade do tempo!{/size}"

    mc surpreso "Quêêê!?"

    m "{size=10}E sem choro!{/size}"

    mc normal "..."

    jump k_a4_final

    label karli_nao_ajudou:

        mc preocupado "Obrigado por me contar e desculpa por não poder ajudar."

        m "Relaxa, [mc]. Você vai ver como eu vou dar um jeito nisso sozinha."

        m "Então vamos pra aula?!"

        mc charmoso "Com certeza."

    label k_a4_final:

        scene black with Dissolve(2.0)

        "Eu e a [m] fomos pra minha aula e tudo correu bem."

        if karli_ajudou:

            "Foi a vez que mais vi ela animada."

            "Não parava de falar e de contar histórias sobre seus clientes famosos."

            "Ganhei uma massagem completa."

            if karli_seducao >= 5:

                "Ela ainda disse que eu merecia uma massagem especial."

                "Estimulou vários pontos que segundo ela me dariam muita energia sexual."

                "Eu tava quase explodindo de vontade de pegar ela."

                "Não vejo a hora que nossa relação evolua pra algo assim."

            "Depois ela pegou pesado no teste. Eu errei tipo 25 vezes, mas finalmente consegui acertar a sequência."

            "No fim, ela agradeceu de novo e me fez prometer que não faria nada estranho pra resolver o problema dela."

            "Foi uma boa noite."
        else:


            "Só que ela parecia meio avoada."

            "Ela não falou muito e a aula correu mais rápido também."

            "Provavelmente o lance do aluguel tá preocupando ela."

            "E mesmo assim ela foi com a aula até o fim. Ela é uma garota bacana."

            "Espero que ela consiga resolver esse problema."

            "Depois da aula a gente se despediu e eu saí sem falar muito."


















    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_4","massagem","aula")
            
            if mc_massagem == 3:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula5:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    "..."

    show karli preocupada with dissolve

    m "A situação tá bem complicada, [mc]."

    if karli_ajudou:

        m "Sua ajuda foi muito importante, mas mesmo assim ainda preciso acertar o valor."
    else:


        mc desculpa "Desculpa não ter te ajudado antes"

        m "Relaxa. Só que..."

    $ gina_nome = "Gina"

    m "A [gina] não vai deixar minha dívida simplesmente sumir."

    mc serio "Eu vou fazer algo sobre isso."

    m "Eu já disse que não é pra você se meter demais nisso. Não seja intrometido."

    mc desculpa "Mas não quero perder minha professora."

    if karli_seducao >= 5:

        mc safado "E justo agora que a gente tava se entendendo melhor..."

        if karli_roupao:

            mc "Você até aceitou tirar a roupa comigo nas aulas."

        mc "De forma alguma vou deixar você sair daqui."

        show karli provocando with dissolve

        m "Isso é mesmo..."

        m "Até que você não é tão idiota quanto eu achei que fosse quando você começou as aulas."

        mc zerado "Eu nunca fui idiota."

        m "Tá sendo agora."

        mc "..."

    show karli normal with dissolve

    m "Você já é grandinho. Não vou falar de novo. Mas tenho dois alertas pra você."

    mc normal "Diga."

    m "Primeiro... se der mais merda pra mim ainda, nunca mais venha falar comigo."

    mc preocupado "..."

    m "Segundo... tome cuidado com a velha. Ela... parece que gostou de você. E isso não tá me cheirando bem."

    mc desconfiado "Você acha que ela pode..."

    m "Eu acho. E eu tô te avisando agora... se você se envolver com ela, pode esquecer qualquer chance comigo."

    mc tarado "Então eu tenho uma chance..."

    m "Não! E agora tchau que até eu resolver esse problema não tem aula!"

    hide karli with dissolve

    "Eu tenho que ajudar ela de algum jeito ou não vou conseguir continuar minhas aulas..."

    "Vou voltar pro ap e pensar melhor."

    "..."



    if tempo >= 3:

        scene apartamento noite with Dissolve(1.0)
    else:


        scene apartamento tarde with Dissolve(1.0)

    if karli_ajudou:

        "Eu falei com a [gina] pelo telefone e ela pareceu uma senhora bem razoável."
    else:


        "Eu não cheguei a falar com a [gina]... mas espero que ela seja razoável."

    "Se a [m] tá com problemas pra pagar o aluguel, bem que ela podia ser legal e dar mais tempo pra ela."

    "Vou tentar ligar pra ela e conversar sobre isso."

    "Smartphone" "Tuu... Tuuu..."

    gina "Boa tarde. Quem fala?"

    show mc telefone with dissolve

    mc "Oi, [gina]. Tudo bem? Aqui é o [mc]."

    gina "Oi, [mc]."

    if karli_ajudou:

        gina "Estou com muita saúde e energia. Isso que importa, né? E você? Tudo bem?"

        mc "Tudo legal. Só continuo preocupado com a questão da [m]."

        gina "Claro... eu entendo."

        mc "É que você tinha me falado pra quando eu tivesse um tempo eu dar um pulo na sua casa pra gente conversar sobre a situação dela..."

        gina "Com certeza. Você parece ser um rapaz honesto e muito proativo. Tenho certeza que você vai poder ajudar nós duas."
    else:


        gina "Que surpresa agradável sua ligação."

        mc "Pois é. Desculpe incomodar a senhora."

        mc "Eu queria conversar sobre o caso da [m]. Ela me falou que ela tá com o aluguel atrasado."

        gina "?"

        mc "[gina]?"

        gina "Oi, querido. Por que você tá ligando pra falar sobre a [m]?"

        mc "Eu sei que isso não tem nada comigo. Mas a [m] é minha amiga e eu queria fazer alguma coisa."

        mc "Eu sei que é idiota. Me desculpa..."

        gina "Meu bem, não fale uma coisa dessas. É incrível você estar fazendo isso pra ajudar sua amiga."

        mc "Sério?"

        gina "Claro. Eu acho muito honrado um homem fazer algo assim. Você é muito corajoso."

        mc "Obrigado."

        gina "E não posso deixar esse ato corajoso passar em branco."

        mc "..."

        gina "Eu posso te ajudar."

        gina "Quando você tiver um tempo, venha aqui em casa. Vamos conversar pessoalmente e resolver juntos o problema da [m]."

        gina "Você parece uma boa pessoa. Tenho certeza que vai poder mediar essa nossa situação."

        mc "Com certeza. Pode contar comigo."

        gina "Perfeito."

        mc "Na verdade, eu tô tranquilo hoje."

    mc "Então você acha que eu posso passar aí mais tarde pra gente resolver isso?"

    gina "Hoje... só um instante."

    "..."

    "..."

    gina "[mc]?"

    mc "Oi."

    gina "Infelizmente hoje não vai dar."

    if tempo == 2:

        gina "Já está no fim da tarde."
    else:


        gina "Já é de noite."

    gina "E eu ainda preciso resolver alguns assuntos."

    mc "Tudo bem, entendi..."

    gina "E amanhã logo cedo? O que você acha? Me livrei de uns compromissos do trabalho pra gente poder resolver esse problema."

    mc "Perfeito! Muito obrigado mesmo, [gina]."

    gina "Não precisa agradecer, meu bem. Eu só quero ver você e a [m] felizes."

    gina "O endereço é Avenida Brasil, número 71."

    mc "Certo. Então amanhã cedo eu passo aí, ok?"

    gina "Vou estar te esperando, querido. Até amanhã."

    mc "Até."

    hide mc with dissolve

    "Legal! Está tudo dando certo."

    "Preciso pensar agora em como convencer ela adiar o pagamento do aluguel da [m]."

    "Mas será que a [m] tá certa sobre aquilo? Será que a [gina] tem alguma intenção estranha comigo?"

    mc desconfiado "?"

    "E se for verdade... Será que... que..."

    menu:
        "É até um bônus!":


            mc tarado "Não vejo nenhum problema. É até um bônus."
        "De forma alguma!":


            mc angustiado "Tá doido?! Eu não vou me envolver com ela de jeito nenhum."
        "Se for pra ajudar a [m]...":


            mc concentrando "Se for pra ajudar a [m], acho que eu toparia..."

    "Melhor eu não ficar viajando demais nisso."

    "Vamos jogar um pouco..."

    scene black with Dissolve(1.0)

    "{b}Um dia depois{/b}"

    $ dia += 1
    $ tempo = 1

    scene apartamento cama_celular with Dissolve(1.0)

    "Acabei jogando até dormir... Já são 10 horas."

    "Vou sair pra casa da [gina] e aviso ela no meio do caminho."

    "..."

    scene cidade onibus with Dissolve(3.0)

    "Eles podiam dar uma melhorada nesse ponto de ônibus."

    "Opa! Aí vem ele."

    scene black with Dissolve(1.0)

    play sound "audio/som_14_onibus.mp3"

    $ renpy.pause(delay=5, hard=True)

    "..."

    "Ter que pegar esse busão toda vez pra ir pra área continental da cidade é um saco..."

    "..."

    "Avenida Brasil... número 71..."

    mc surpreso "!"

    stop sound

    scene mansao entrada with Dissolve(3.0)

    mc "Que tipo de casa é essa?!"

    mc zerado "Isso não é uma casa... é praticamente um condomínio inteiro..."

    mc "Como pode ter gente tão rica nesse mundo?"

    "{i}tchhk{/i}"

    "Voz metalizada" "Oi, [mc]."

    mc surpreso "Eita! Onde?!"

    "Voz metalizada" "É o interfone, querido."

    mc envergonhado "Ah! Ok..."

    "Voz metalizada" "Estou vendo você pela câmera."

    mc "Entendi..."

    "Voz metalizada" "Vou abrir pra você. Por favor, entre."

    "Gente, quanta pompa..."

    "..."

    "Acho que eu estou andando há uns 5 minutos só pra cruzar o jardim da casa..."

    scene mansao porta with Dissolve(3.0)

    "Ainda não tô acreditando nisso aqui tudo..."

    show gina b_ola with dissolve

    gina "Bom dia, [mc]."

    mc surpreso "!"

    gina "Tudo bem?"

    mc envergonhado "Tu-tudo bem..."

    "Ela tá de biquíni... e o corpo dela... bem... tá bem conservado..."

    gina "Ah. Desculpa te atender assim. É que eu estava relaxando na piscina."

    gina "Você acha melhor eu me trocar?"

    menu:
        "Eu acho que seria mais apropriado.":


            $ gina_biquini = False

            mc envergonhado "Eu acho que eu ficaria mais à vontade para conversar."

            mc "Mas não quero te incomodar, a casa é sua."

            gina "Não se preocupe, querido. Eu vou me vestir e já te encontro."

            gina "Pode entrar e ficar à vontade."

            mc normal "Obrigado."
        "A casa é sua. Não precisa se trocar por minha causa.":


            $ gina_biquini = True

            mc charmoso "Que isso. Não precisa, não. A casa é sua, pode vestir o que achar melhor."

            gina "Obrigada, meu bem. A gente trabalha a vida toda e agora precisa curtir um pouco do que juntou, né?"

            mc "Você está mais do que certa."

            "Mas mesmo com tudo isso não pode perdoar o aluguel da [m]? Essa velha é muquirana mesmo."

            show gina b_provocando with dissolve

            gina "Mas não vamos ficar aqui. Vamos entrar."

            mc envergonhado "Ok..."

            gina "Só ficar de olho em mim e não se perder."

            mc "Certo..."

    scene mansao hall with Dissolve(3.0)

    gina "Fique à vontade. Eu já volto."

    mc normal "Ok."

    "Só esse pequeno hall de entrada da casa já é maior que meu apartamento eu acho..."

    "..."

    "Tenho um tempo sozinho aqui. Será que eu devo..."

    menu:
        "Fuçar nas coisas dela.":


            "Eu sei que não é educado, mas minha missão é ajudar a [m]..."

            "Se bem que a [gina] está sendo tão legal comigo. Será que eu devo bisbilhotar a casa dela?"

            menu:
                "Sim. Vou bisbilhotar.":


                    $ gina_procurou = True

                    "Ela até pode ser legal comigo, mas ela tá sendo mesquinha em cobrar a [m] desse jeito."

                    "..."

                    "Parece que tem uma papelada aqui..."

                    "Deixa eu ver melhor."

                    show item papeis with dissolve

                    "Hmm... O que é isto aqui em cima dos papéis?"

                    "{i}Querida, Genoveva Ávila.{/i}"

                    "{i}Como pedido, analisei o contrato e seus temores não são infundados.{/i}"

                    "Parece uma carta. Tem o selo de uma empresa."

                    "{i}Realmente existem irregularidades no seu acerto com esse coletivo.{/i}"

                    "{i}Caso eles sejam assessorados por um advogado competente, não será impossível eles te processarem.{/i}"

                    "{i}Como se trata de um grupo de pessoas pobres, pelo que você disse, provavelmente eles nunca encontrarão essa brecha.{/i}"

                    "{i}Não há mais como alterar o contrato, a não ser que você tenha o interesse de devolver a eles o montante corrigido.{/i}"

                    "{i}Por isso, mesmo não sendo o caminho mais previsível, aconselho que você deixe tudo como está.{/i}"

                    hide item

                    if gina_biquini:

                        show gina b_pensando with hpunch
                    else:


                        show gina pensando with hpunch

                    gina "Jovem?"

                    mc surpreso "Ah!"

                    gina "O que está fazendo com isso na mão?"

                    mc desculpa "Ah..."

                    menu:
                        "Do que se trata essa carta aqui?":


                            $ gina_idiota = True

                            mc serio "É... Você poderia me falar do que se trata esta carta aqui?"

                            mc "Fala de uma irregularidade..."

                            gina "São assuntos jurídicos da minha empresa. Não precisa se preocupar com eles. Não tem nada a ver com a [m]."

                            mc desculpa "Certo. Desculpa por bisbilhotar."
                        "Ah! Me desculpe, eu fiquei esperando e...":


                            mc desculpa "Desculpe. Não quis ser bisbilhoteiro."

                            mc "Eu tava te esperando e este papel caiu ali da mesa e..."

                    if gina_biquini:

                        show gina b_ola with dissolve
                    else:


                        show gina ola with dissolve

                    gina "Não precisa se preocupar. A culpa foi minha de deixar você esperando."

                    mc desculpa "Claro que não. Eu que..."

                    gina "Não quero mais ouvir sobre isso."
                "Não. Ela não merece isso.":


                    "Não. Não vou fazer isso com ela. Ela tá sendo tão legal comigo."

                    "..."

                    "..."
        "Esperar ela voltar.":


            "Vou ficar de boa só esperando ela voltar."

            "Ela tá sendo super gente fina comigo. Não tem por que eu causar."

            "..."

            "..."

    if gina_biquini:

        show gina b_ola with dissolve
    else:


        show gina ola with dissolve

    gina "Desculpa deixar você esperando. Venha comigo por aqui. Quero que você veja uma coisa."

    mc normal "Certo..."

    "..."

    scene mansao piscina with Dissolve(3.0)

    mc surpreso "Uou!"

    if gina_biquini:

        show gina b_ola with dissolve
    else:


        show gina ola with dissolve

    gina "Gostou?"

    mc normal "Claro. É um espaço maravilhoso."

    gina "É o meu lugar preferido na mansão. Sempre que eu posso eu venho pra cá."

    mc "Eu também viria se tivesse uma dessas."

    gina "Se não for ruim demais vir da ilha pra cá, pode ficar à vontade e usar quando quiser."

    mc envergonhado "Obrigado..."

    if gina_biquini:

        show gina b_pensando with dissolve
    else:


        show gina pensando with dissolve

    gina "Desculpa enrolar você com essas baboseiras todas. Vamos falar sobre a [m]?"

    mc normal "Certo. Tenho certeza que será possível resolver de uma forma que fique bom para vocês duas."

    gina "É o que eu espero, [mc]. Tenho certeza que você vai entender a situação facilmente."

    gina "O que acontece é que a [m] está com diversos meses do aluguel atrasado."

    gina "E você pode olhar pra minha casa e pensar que eu sou mesquinha por ficar cobrando ela."

    gina "Mas não é simples assim. Quando fazemos um acordo é para cumprir, correto?"

    gina "Além do mais, se eu fizesse isso com todos os inquilinos meu negócio já teria falido."

    gina "Tenho certeza que você entende isso."

    mc desculpa "Hmm..."

    menu:
        "Mas o caso da [m] é diferente. Ela não tem como pagar.":


            mc preocupado "Mas, [gina]. O caso da [m] é diferente. Ela não tá fazendo corpo mole. Ela realmente não tem como pagar."

            gina "E eu entendo, querido. Mas isso é responsabilidade de cada um, concorda?"
        "Entendo... Então ela só será despejada?":


            mc desculpa "Você tem razão, mas então ela só vai ser despejada?"

            gina "Eu poderia entrar com um processo de despejo agora mesmo."

    mc preocupado "Eu não quero que ela seja despejada. Ela é minha professora de massagem e já virou uma amiga."

    if gina_biquini:

        show gina b_ola with dissolve
    else:


        show gina ola with dissolve

    gina "Eu entendo perfeitamente. Não chamei você aqui pra torturar você."

    gina "Eu estou disposta a dar mais tempo para ela acertar o valor comigo. Mas ela precisa pagar ao menos um mês."

    mc feliz "Obrigado, [gina]!"

    gina "Estou diposta a fazer isso não por ela, mas por que você veio até aqui de boa vontade para conversar."

    mc normal "Obrigado mesmo."

    gina "Então dê a boa notícia pra ela e avise que ela precisa do dinheiro de pelo menos um mês, certo?"

    mc normal "Tá bom. Vou falar."

    gina "E se ela não puder acertar esse valor mínimo, me ligue e marcamos outra visita sua."

    gina "Não quero que você perca sua professora e suas aulas."

    mc normal "Combinado."

    gina "E esperamos que não seja preciso, mas se você voltar, quero que você traga seu calção de banho."

    gina "Quero que você experimente dar um pulo na minha piscina."

    mc "Combinado."

    gina "Até mais, querido."

    mc "Até."

    "..."

    scene black with Dissolve(1.0)

    "Uou! A [gina] foi muito bacana outra vez. A [m] não vai ser despejada. Ela vai ter mais tempo pra pagar o aluguel."

    "Preciso correr avisar pra ela."

    $ tempo += 1

    scene salao geral with dissolve

    mc feliz "[m]!"

    mc "{i}puf puf{/i}"

    show karli normal with dissolve

    m "O que foi, [mc]? Por que tá ofegando assim?"

    mc normal "Vim correndo te avisar!"

    m "Vai me dizer que..."

    mc feliz "Você não vai ser despejada, moça!"

    m "Como assim?!"

    mc normal "Falei com a [gina] e ela vai dar mais tempo pra você pagar! E tem mais..."

    mc surpreso "Ei!"

    show karli abraco with hpunch

    pause

    m "Não acredito! Ela vai me dar mais tempo, mesmo?!"

    mc surpreso "S-sim! Cuidado..."

    m "Uhuuull!"

    m "Valeu, [mc]!"

    mc envergonhado "Ca-calma..."

    m "Me segura direito, muleque! Se eu cair tu vai ver!"

    mc charmoso "Daí eu faço uma massagem pra você..."

    m "Nem pense nisso! Você ainda é só um coitado! Tem muitas aulas ainda!"

    m "Obrigado mesmo... Eu não sabia mais o que fazer..."

    menu:
        "Não precisa agradecer.":


            mc normal "Não precisa agradecer. Não quero perder minha professora."

            m "Você é um fofo."
        "Você pode me agradecer saindo comigo.":


            $ karli_seducao += 1
            $ karli_sair = True

            mc charmoso "O que acha de me agradecer saindo comigo?"

            m "Saindo com você? Tipo um encontro?"

            mc "Isso."

            m "Hmmm... Mas será que você seria uma boa companhia? Sei não..."

            mc zerado "Ei..."

    m "Agora deixa eu descer."

    hide karli with dissolve

    m "Mudando de assunto..."

    show karli satisfeita with dissolve

    m "Pronto pra sua aula de hoje?! Não vou deixar você em paz!"

    if karli_roupao:

        mc tarado "Só se você tirar a roupa igual da outra vez."

        show karli provocando with dissolve

        m "Tá bom, safado..."

        m "Mas não vai achando que eu tô facinho..."

        menu:
            "Claro que não...":


                mc tarado "Claro que não..."

                show karli normal with dissolve

                m "Ei! Isso foi irônico?"

                m "Nada de roupão hoje, então!"

                mc angustiado "Não! Não! Desculpa!"

                m "Tarde demais! Bora pra aula!"
            "Pfff... Você sabe que eu me esforcei pra isso, né?":


                mc triste "Facinho? Sabe quantas vezes você negou?!"

                m "Acho bom você saber que aqui a coisa pega."

                m "Agora vamos lá..."
    else:


        hide karli with dissolve

        mc angustiado "Ei! Espera! Não precisa empurrar!"

        m "Vai logo!"

        mc "Eeiii!"

    scene black with Dissolve(1.0)

    "{i}Creck Tleck{/i}"

    mc "Ai minhas costas!"

    m "Tô muito animada hoje!"

    "{i}Creck Tleck{/i}"

    mc "Aaaaiiii!"

    "..."

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_5","massagem","aula")
            
            if mc_massagem == 4:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula6:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    "..."

    show karli meudeus with dissolve

    m "..."

    mc preocupado "Tudo bem, [m]? Aconteceu alguma coisa?"

    m "adskldjalskdjasdasd"

    mc desconfiado "Como? Não entendi nada..."

    m "euaskdjaosidjqiqwi..."

    mc zerado "Dá pra tirar as mãos da cara por favor?"

    show karli preocupada with dissolve

    m "Tô com vergonha de falar pra você..."

    mc normal "Não precisa ficar assim. Só me fala o que tá rolando."

    m "É..."

    m "É que eu não tenho dinheiro nem pra um aluguel..."

    mc surpreso "Nem pra um?!"

    m "Não..."

    m "Eu sei que você se esforçou bastante com a [gina]... mesmo assim acho que vou ser despejada."

    mc triste "Não fale isso, [m]..."

    mc preocupado "E seu trabalho no Tadaima?"

    m "Quase tudo o que eu ganho lá eu uso pra viver..."

    mc "Caraca... sua barra tá complicada mesmo, hein?"

    show karli normal with dissolve

    m "Você fez o que era possível. Mais do que era possível, aliás..."

    m "Não fique triste. [mc], tudo vai dar certo."

    mc "[m]..."

    m "Mas claro que não vou te deixar sem aula hoje."

    m "Vamos?"

    mc normal "Claro."

    scene salao massagem with Dissolve(1.0)

    if karli_roupao and karli_seducao >= 5:

        show karli roupao_provocando with dissolve

        m "Assim que você gosta de massagear?"

        mc safado "Exatamente."

        m "Você vai fazer direitinho hoje?"

        mc "Com certeza, professora."

        m "Vai apertar nos lugares certinhos?"

        mc "Você tá me provocando..."

        m "Eu sei. Mas hoje só eu que vou aplicar massagem. Tenho que te ensinar uma coisa nova."

        mc zerado "Você faz de propósito..."

        m "Sim. E sem choro. Tira a roupa e já pra mesa."

        mc "Ok, megera..."
    else:


        show karli normal with dissolve

        m "Pronto? Hoje só eu que vou aplicar massagem. Tenho que te ensinar uma coisa nova."

        mc normal "Ok."

        m "Pode tirar a roupa e se ajeitar."

    scene black with Dissolve(1.0)

    "{b}Depois da aula{/b}"

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_6","massagem","aula")
            
            if mc_massagem == 5:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    scene salao geral with dissolve

    if karli_roupao and karli_seducao >= 5:

        show karli roupao_normal with dissolve
    else:


        show karli normal with dissolve

    m "Então é isso por hoje."

    mc charmoso "Valeu. E pode deixar que eu vou te ajudar com o problema do aluguel."

    m "Relaxa, [mc]. Você já me ajudou demais."

    mc "Só vou parar quando você estiver fora de perigo. Deixa comigo."

    m "Falou, super herói. Super Paparazzo. Suparazzo!"

    mc zerado "Tá me zoando..."

    m "Imagina. Agora adeus."

    mc normal "Falou, dramática."

    "..."

    if tempo == 2:

        scene apartamento tarde with Dissolve(1.0)
    else:


        scene apartamento noite with Dissolve(1.0)

    "A [m] se esforçou pra parecer normal, mas é claro que ela tá nervosa."

    "Não posso deixar isso acabar assim. Vou ter que falar com a [gina] de novo."

    "Ela tem sido muito bacana comigo. Eu podia pelo menos tentar alguma coisa."

    show mc cueca_telefone with dissolve

    "Smartphone" "Tuu... Tuuu..."

    gina "Alô?"

    mc "Oi, [gina]! É o [mc]."

    gina "Oi, querido. Que bom receber uma ligação sua."

    mc "Você sabe que não queria incomodar novamente, né?"

    gina "Eu sei. Não vai me dizer que a [m] está com problemas."

    mc "Está. Eu queria..."

    gina "Não se preocupe. Você sabe que podemos resolver tudo juntos."

    gina "Venha aqui em casa logo cedo e eu vou te ajudar com o que precisar."

    mc "Então tá combinado."

    gina "Fico contente. Eu gosto de falar com você. Você é um rapaz inteligente."

    menu:
        "Também gosto de falar com você.":


            mc "Também gosto de falar com você."

            gina "Você me deixa encabulada."
        "Até amanhã, então.":


            mc "..."

            mc "Amanhã então a gente se vê."

    gina "Então até amanhã."

    mc "Boa noite."

    hide mc with dissolve

    "Amanhã vou ver ela novamente então. Preciso pensar como convencer ela a perdoar um mês de aluguel da [m]."

    "Não sei por que ela simplesmente deixaria de receber o dinheiro. Mas tenho que tentar alguma coisa."

    if gina_procurou:

        "Não posso esquecer daquela carta que eu li na casa dela. Falava algo sobre contrato ilegal... algo assim..."

        "Será que se eu conseguisse pegar isso... a gente poderia ameaçar ela?"

        "Ela tá sendo tão legal comigo. Não sei por que eu faria isso com ela..."

    "Talvez a [m] esteja certa e ela realmente quer algo comigo..."

    mc preocupado "Não sei o que pensar sobre isso..."

    "Bom... tenho que me preparar para amanhã."

    scene black with Dissolve(1.0)

    "{b}Um dia depois{/b}"

    $ dia += 1
    $ tempo = 1

    scene apartamento dia with Dissolve(1.0)

    mc normal "Estou pronto. Vamos lá."

    scene cidade onibus with Dissolve(3.0)

    scene black with Dissolve(1.0)

    play sound "audio/som_14_onibus.mp3"

    $ renpy.pause(delay=5, hard=True)

    "..."

    "..."

    stop sound

    scene mansao entrada with Dissolve(3.0)

    mc desconfiado "Ainda não me acostumei com o tamanho disso aqui."

    "Interfone" "{i}tcchhhkk{/i}"

    gina "Bom dia, [mc]."

    mc normal "Bom dia."

    "Como ela sabe que eu cheguei?"

    gina "Estou na piscina novamente. Será que você poderia vir aqui? Você já sabe o caminho."

    mc "Claro."

    gina "Te espero."

    "Interfone" "{i}tcchhhkk{/i}"

    mc "Ok. Vamos lá."

    scene mansao hall with Dissolve(1.0)

    if gina_procurou:

        "Foi aqui que eu encontrei a carta da outra vez."

        "Se a [gina] tá na piscina, provavelmente ela não vai me incomodar."

        "Será que eu devo arriscar e fuçar naquela outra sala de novo?"

        menu:
            "Vou arriscar.":


                "Tenho que olhar aquilo melhor... Pode acabar ajudando a [m]."

                "..."

                if not gina_idiota:

                    $ gina_segredo = True

                    "Ufa. A porta tá destrancada."

                    "E os papéis estão exatamente no mesmo lugar."

                    show item papeis with dissolve

                    "A carta e os contratos estão aqui..."

                    "Espera. A carta diz que o grupo que está sendo enganado é pobre e não vai descobrir."

                    "Mas agora que eu sei disso eu posso contar pra eles..."

                    mc surpreso "!"

                    "É como se eu tivesse uma arma pra ameaçar a [gina] se eu quiser."

                    "Essa informação nas mãos da [m] pode livrar ela de pagar o aluguel talvez até pra sempre!"

                    "Ou talvez a [gina] só use todo seu dinheiro pra acabar com a gente..."

                    mc angustiado "... E agora?"

                    "Bom... eu descobri o nome do grupo que ela tá enganando. Depois posso passar pra [m] se eu quiser."

                    "Agora é melhor eu ir pra piscina. Demorei demais aqui."
                else:


                    "{i}Gatchak{/i}"

                    "Droga! A porta tá fechada..."

                    "Dessa vez ela foi mais cuidadosa."

                    "Agora é melhor eu ir pra piscina."
            "Melhor dar o fora daqui.":


                "Não quero causar com ela. Melhor eu ir direto pra piscina."
    else:


        "Eu conheço o caminho pra piscina. É só seguir por aqui."

    "..."

    scene mansao piscina with Dissolve(2.0)

    mc normal "[gina]?"

    gina "Estou aqui, [mc]."

    mc normal "Ok. Tô indo..."

    if gina_segredo:

        gina "Você demorou. Se perdeu no caminho?"

        mc desculpa "É. Mais ou menos isso..."

        "Não posso falar de forma alguma sobre os documentos..."

    mc surpreso "!"

    gina "Senta aqui do meu lado."

    mc envergonhado "O-ok..."

    scene gina b_sentada with Dissolve(2.0)

    pause

    gina "Isso. Confortável?"

    mc "Sim..."

    gina "Você parece um pouco consternado. O que aconteceu?"

    menu:
        "Você tá em forma...":


            mc envergonhado "É... não sei como falar isso sem parecer um tarado."

            gina "Só fale, querido."

            mc "Você tá em forma. Eu fiquei impressionado."

            gina "Obrigada. Me deixa feliz ouvir isso de um jovem da sua idade."

            mc normal "Mas..."

            gina "Você quer saber como eu tenho um corpo assim tendo minha idade?"

            mc envergonhado "..."

            gina "Não precisa ficar com vergonha. Eu sei que sou velha."

            gina "Mas hoje em dia velhice não é mais como antigamente."

            gina "A medicina evoluiu muito e mesmo uma pessoa de idade avançada pode ter saúde e disposição."

            gina "E não vamos esquecer das minhas condições."

            gina "Manter um corpo assim precisa de muito dinheiro. Infelizmente, não é pra qualquer um."

            mc charmoso "Com todo o respeito, meus parabéns. Você realmente não deve nada pra nenhuma garota."

            gina "Não me deixe encabulada."
        "Não é nada. Só tô um pouco cansado.":


            mc desculpa "Não é nada. Só cansei um pouco do rolê de vir até aqui."

            gina "Espero não estar incomodando você."

            mc normal "De forma alguma. Eu que agradeço por você me receber."

            mc envergonhado "Eu sinto que eu que tô incomodando nos últimos tempos."

            gina "Não pense nisso."

    gina "Acho que está bom de preliminares. Vamos ao que interessa?"

    mc desculpa "Certo... Como você sabe, estou aqui pela [m] que tá com problemas em pagar o aluguel."

    mc "Eu sei que é difícil de entender, mas mesmo com toda sua ajuda, ela não consegue pagar nem um aluguel no momento."

    gina "Puxa..."

    mc "Pois é. Daí... o que eu queria..."

    gina "Calma. Não precisa falar mais nada. Eu entendi tudo."

    gina "E digo que é possível resolvermos isso de uma forma que fique bom para a [m] e para mim."

    mc surpreso "Sério?!"

    gina "Sim."

    scene mansao piscina with Dissolve(1.0)

    show gina b_pensando with dissolve

    gina "A questão é que, não dá pra negar, eu estou velha. E muitas vezes eu sinto dores nas costas."

    gina "Eu sei o quanto a [m] domina a arte da massagem. É só uma questão de tempo até ela ficar famosa."

    mc feliz "Também acho!"

    gina "Só que ela se recusa a me ter como cliente."

    mc desconfiado "Se recusa?"

    gina "Sim. Não entendo qual é o problema, mas ela simplesmente não me aceita."

    mc normal "Você quer que eu fale com ela pela senhora?"

    mc "Tenho certeza que posso convencer ela a reconsiderar. Ainda mais na situação que ela tá."

    gina "Seria uma boa, [mc]. Mas não sei se ela aceitaria. Ela parece ser uma garota resoluta."

    mc zerado "Pior é que você tem razão. Ela é bem cabeça dura."

    gina "Sim... eu conheço essa pilantrinha... Digo, ela já disse que não aceitaria."

    mc preocupado "Mas, então... como..."

    show gina b_ola with dissolve

    gina "Você disse que é um aprendiz dela, não disse?"

    mc surpreso "E-eu?!"

    gina "Sim. Eu lembro de você ter mencionado isso."

    mc envergonhado "Sim... mas eu só completei metade das aulas até agora..."

    mc "A [m] me mataria se ela descobrisse que eu estou usando o nome dela."

    mc preocupado "Me dá um calafrio só de pensar."

    gina "Ela não precisa saber. Vai ser nosso segredinho."

    gina "E se você aceitar, eu estou disposta a perdoar um mês de aluguel por uma única massagem."

    mc surpreso "!"

    gina "Isso mesmo. É pra você ver o quanto eu tô necessitada de uma boa massagem..."

    "Essa é uma excelente proposta! Eu resolvo o problema da [m] e só preciso fazer uma massagem."

    "É algo completamente inofensivo... somente uma massagem... certo?"

    gina "Você não vai deixar uma senhora com dor nas costas, não é?"

    menu:
        "Pode contar comigo. Eu farei a massagem.":


            mc charmoso "Pode contar comigo. Eu vou ajudar a senhora e a [m] também."

            gina "Perfeito!"

            gina "Tenho certeza que eu vou adorar sentir sua massagem..."

            jump k6_gina_massagem
        "Peço desculpas, mas não me sinto confortável.":


            mc desculpa "Peço desculpas, [gina]. Você tem sido tão legal comigo."

            mc "Mas eu realmente não me sinto preparado para fazer massagens ainda."

            show gina b_pensando with dissolve

            gina "Eu entendo perfeitamente, jovem. Não estou pedindo para você fazer nada que te deixe desconfortável."

            gina "A única coisa é que você vai salvar sua amiga [m] em troca de apenas uma massagem."

            gina "Mesmo não sendo tão boa, eu tenho certeza que vai me ajudar demais."

            gina "O que me diz?"

            menu:
                "Não tenho coragem mesmo. Me perdoe.":


                    mc desculpa "Eu não tenho coragem mesmo, me perdoe."

                    gina "É realmente uma pena, jovem. Eu imaginei que você queria ajudar sua amiga."

                    mc "Eu quero, mas não dessa forma."

                    gina "Infelizmente essa é a única forma disponível pra você."

                    mc "Eu entendo..."

                    gina "Terminamos nossa conversa. Por favor, pode se retirar e espero que não volte a me ligar."

                    mc serio "Certo..."

                    gina "Adeus."

                    mc "..."

                    jump k6_final
                "Se realmente vai ajudar a [m], eu aceito.":


                    mc envergonhado "A senhora tem razão. Se isso for ajudar a [m], eu aceito."

                    show gina b_ola with dissolve

                    gina "Perfeito!"

                    jump k6_gina_massagem

    label k6_gina_massagem:

        $ gina_massagem = True

        gina "Eu tenho uma mesa de massagem aqui em casa. Eu vou buscá-la e retorno logo."

        gina "Ah! Um último pedido. Eu ficaria mais à vontade com a massagem se você estivesse usando menos roupa."

        mc surpreso "Como?!"

        gina "Eu vou estar só de biquíni... se você pudesse me acompanhar, eu acharia melhor."

        "Essa velha tá com coisa na cabeça... Mas agora que eu tô aqui. Não dá pra pular fora."

        mc envergonhado "Tudo bem. Se você vai se sentir mais à vontade..."

        gina "Muito obrigada por atender os caprichos de uma velha."

        hide gina with dissolve

        "Caraca... onde eu me meti? Parece que a [gina] tá animada demais com uma simples massagem..."

        "Será que ela tem segundas intenções mesmo? E se for verdade, como eu me sinto quanto a isso?"

        menu:
            "Eu gostaria de ter segundas intenções com ela...":


                $ gina_atraido = True

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("gina_sexo_sim","gina","personagem")

                mc charmoso "Não teria nada demais em ter algo com ela."

                "A [gina] é uma mulher atraente como muitas outras aqui na ilha. Não vejo nenhum problema em ter uma relação com ela."
            "Não quero nada com ela nesse sentido.":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("gina_sexo_nao","gina","personagem")

                "Com certeza não. Por mais que ela seja uma senhora atraente, não quero nada nesse sentido com ela."

                "Preciso fazer essa massagem o quanto antes e dar o fora."

        "Opa. Ela vem aí."

        mc normal "Deixa que eu te ajudo com a mesa."

        gina "Obrigada, querido. Você é um jovem cavalheiro."

        show gina b_ola with dissolve

        gina "Pode colocar ela ali."

        mc normal "Ok."

        gina "Como eu faço agora?"

        mc "Pode se deitar e ficar à vontade."

        gina "Vou me ajeitar então."

        hide gina with dissolve

        "..."

        gina "Ufa... pronto."

        if gina_atraido:

            mc surpreso "..."

            scene gina mas_chamando with Dissolve(3.0)

            pause

            gina "E então? Pronto para fazer esta senhora se sentir muito bem?"

            mc charmoso "Com certeza."

            "Caraca... a [gina] com certeza conseguiu evitar o efeito do tempo. Ela tem um corpo..."

            gina "Você acha que eu posso ficar de barriga pra cima? Eu gostaria que você massageasse esta região."

            gina "Aqui na barriga, no tórax e também minhas pernas."

            mc "Tudo bem. Onde você preferir."

            "Eu não sei se eu aprendi a fazer massagem nesses lugares. Mas vamos ver..."

            gina "Você se importa também se eu ficar com as pernas abertas? Eu vou me sentir melhor."

            mc "Claro. Sem problemas."

            gina "Perfeito. Então pode começar, [mc]. Eu sou sua."

            mc "..."

            scene black with Dissolve(1.0)

            gina "Hmmm..."

            gina "Sua pegada é firme. Eu adorei..."

            mc charmoso "..."

            gina "Ahh..."

            scene gina massagem_normal with Dissolve(3.0)

            pause

            gina "Ai..."

            gina "Você tá pegando nos lugares certos..."

            gina "Hmm..."

            "A [gina] parece estar gostando mesmo da massagem."

            "E eu não tô conseguindo evitar de ficar um pouco excitado do jeito que ela tá reagindo."

            gina "Eu tô sentindo meu corpo todo arrepiado, [mc]."

            mc "Só relaxe e deixe que eu vou cuidar bem do seu corpo."

            gina "Tá..."

            "..."

            "..."

            gina "Hmmm..."

            mc "Pronto. Pode se levantar."

            gina "Certo, meu bem..."
        else:


            scene black with Dissolve(1.0)

            mc normal "Espero que você goste."

            gina "Tenho certeza que vou gostar."

            "..."

            "{b}Meia hora depois{/b}"

            mc normal "Pronto. Pode se levantar."

            "..."

    scene mansao piscina with Dissolve(1.0)

    show gina b_ola with dissolve

    gina "Hmmmm... maravilhoso."

    gina "Foi tão bom quanto eu imaginava. Meus parabéns, [mc]."

    mc normal "Obrigado."

    if gina_atraido:

        mc charmoso "Eu gostei muito de massagear a senhora também."

        gina "Eu senti que você gostou mesmo. O jeito e a força que você passou a mão em mim."

        mc safado "..."

    gina "E como agradecimento pelos seus serviços, um mês de aluguel da [m] está perdoado."

    mc feliz "Isso é incrível, [gina]! Muito obrigado mesmo!"

    gina "Você mereceu. E, vamos torcer que não, mas se a [m] precisar de ajuda novamente venha me ver."

    gina "Eu vou estar ansiosa por mais uma massagem sua."

    if gina_atraido:

        mc tarado "Eu tenho certeza que você vai adorar de novo."

        gina "Eu acho que eu vou gostar ainda mais da próxima vez... E você também..."

        mc "Estou ansioso."
    else:


        mc normal "Combinado."

    gina "Tenha um bom dia, [mc]."

    mc "Você também. Até."

    label k6_final:

        $ tempo += 1

        scene black with Dissolve(1.0)

        "Hora de voltar pra casa."

        "..."

    scene apartamento geral with Dissolve(1.0)

    "Lar doce lar..."

    if gina_massagem:

        "Eu consegui que a [gina] perdoasse um mês de aluguel da [m]."

        "Isso vai fazer com que ela não seja despejada e eu possa continuar minhas aulas de massagem."

        "A [m] vai ficar muito feliz quando eu contar pra ela."
    else:


        "Eu resolvi não fazer massagem nela então ela não vai perdoar o aluguel da [m]."

        "Talvez então ela seja despejada e eu não consiga terminar meu curso."

    if gina_segredo:

        "E também tem o lance dos documentos..."

        "Agora eu sei o nome do grupo de pessoas que a [gina] tá enganando."

        "Preciso ver o que fazer com isso. Isso pode ajudar a [m] também. E até mais..."

        "Só tenho que decidir se realmente eu tenho cacife pra enfrentar a velha."

    "Agora eu tenho que avisar a [m] do que eu consegui. Espero que ela fique feliz."

    jump call_cidade

label karli_aula7:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    scene ilha predio_entrada with Dissolve(2.0)

    "..."

    "Tô muito preocupado com a [m]. Ela não tá mais trabalhando no Tadaima... o salão tá fechado..."

    mc incomodado "O que será que houve?"

    if gina_massagem:

        "Mulher" "Qual a preocupação, [mc]?"

        show gina ola with Dissolve(1.0)

        mc surpreso "Gi-gina?!"

        gina "Oi."

        mc envergonhado "Você me assustou."

        gina "Desculpa."

        mc "Não foi nada."

        mc preocupado "Eu só tava pensando em uma coisa..."

        show gina pensando with dissolve

        gina "O que aconteceu? Alguma coisa te incomodando?"

        mc "Não quero te perturbar."

        show gina ola with dissolve

        gina "Você nunca me perturba."
    else:


        "Mulher" "Veja se não é o medroso."

        mc desconfiado "Quê?"

        show gina pensando with dissolve

        mc surpreso "Gi-gina?!"

        gina "O que foi?"

        mc "Na-nada."

        gina "Ainda estou sentida por você não ter feito a massagem no outro dia."

        mc desculpa "Perdão. Eu não me sinto preparado pra isso ainda."

        gina "Não importa agora."

        mc "Deixa eu te perguntar uma coisa..."

        gina "Seja breve."

    mc desculpa "O que aconteceu com a [m]? Ela desapareceu."

    mc "Você... despejou ela?"

    show gina ola with dissolve

    gina "A garota teve o que merecia."

    mc "Como?"

    gina "Eu sei que ela é sua amiga. Mas ela não conseguiu cumprir o nosso combinado."

    mc angustiado "Mas você disse q-"

    gina "Tenha calma, jovem. Ela está bem."

    mc surpreso "Sério?!"

    show gina pensando with dissolve

    gina "Você se preocupa tanto assim com ela?"

    mc desculpa "Ela é uma grande amiga."

    gina "Será que é só isso mesmo?"

    menu:

        "Na verdade, tem rolado um clima entre a gente..." if karli_seducao >= 5:

            mc envergonhado "Pra falar a verdade, acho que tá rolando um clima..."

            gina "Sério?"

            mc desconfiado "Sim. Mas, o que isso tem a ver-"

            gina "Nada não, jovem. É só que..."
        "É apenas amizade.":


            mc normal "É apenas amizade, sim."

            gina "Entendo..."

    show gina ola with dissolve

    gina "Não é nada."

    mc desconfiado "..."

    gina "Olha..."

    if gina_massagem:

        gina "Você foi incrível aquele dia em casa."

        if gina_atraido:

            mc charmoso "Fico feliz que você tenha gostado. Eu gostei de massagear você também."
        else:


            mc normal "Que bom que você gostou."

        gina "E minha parte do trato era pegar leve com a menina. Mas ela acabou tendo que deixar o salão mesmo assim."

        gina "Eu sinto que estou em débito com você."

        mc envergonhado "Não precisa pen-"
    else:


        if gina_segredo:

            show gina pensando with dissolve

            gina "Eu sei que você bisbilhotou minha sala e viu a mensagem do meu advogado."

            mc surpreso "!"

            "Merda! Como ela sabe isso?! Eu tenho certeza que ela não tava olhando quando entrei na sala!"

            gina "Eu tenho câmeras na casa, seu tolo. Achou mesmo que eu deixaria informações como aquelas desguarnecidas?"

            mc serio "..."

            mc "E então?"

            gina "Eu julguei você errado. Achei que fosse só um jovem burro, e paguei caro por isso."

            mc "Quem é o burro agora?"

            gina "Não precisa fazer essa cara. Eu vou fazer algo por você e então encerramos esse assunto. O que me diz?"

            mc desconfiado "Eu não quero nad-"
        else:


            $ sem_casa = True

            gina "A menina vai ficar bem. Não pense demais nisso."

            gina "Tenha uma boa tarde."

            mc preocupado "Bo-boa tarde..."

            hide gina with dissolve

            "Sinto que a [gina] queria falar algo pra mim. Se eu tivesse feito a massagem nela, talvez as coisas fossem diferentes."

            "E também tinha aquela sala dela. Se eu conseguisse investigar melhor..."

            "Agora não adianta chorar pelo leite derramado. A não ser que eu conseguisse voltar pro passado..."

            jump karli_a7_continua

    gina "Não diga isso. Eu quero fazer uma proposta pra você. Uma proposta que eu nunca fiz pra ninguém antes."

    mc desconfiado "O-ok."

    gina "Uma das minhas propriedades aqui na ilha acabou de ser desocupada. O que você acha de ficar com ela?"

    mc surpreso "Quê?!"

    gina "Mas não pense que é igual esse kitão que você mora hoje. É um apartamento de alto padrão, de três comodos."

    gina "Ele não é grande, mas está mobiliado em perfeitas condições, e é extremamente luxuoso. O que você me diz?"

    gina "Quer dar uma olhada?"

    mc envergonhado "I-isso... não sei se posso pagar algo assim."

    gina "Quem disse em pagar, bobinho? É do outro lado da praça. Vamos comigo dar uma olhada e se você gostar a gente conversa melhor."

    mc normal "Ok."

    scene black with Dissolve(1.0)

    "..."

    scene ap sala with Dissolve(2.0)

    pause

    mc surpreso "!"

    gina "E aí? O que achou?"

    mc "Incrível!"

    gina "Isso aqui é um apartamento de luxo em um prédio de luxo. Muito diferente de onde você mora hoje."

    gina "São realidades totalmente diferentes."

    "Ela não precisa ficar lembrando toda hora que eu moro em um kitão de quinta."

    mc envergonhado "..."

    gina "Vamos continuar. Dê uma olhada na cozinha."

    mc normal "Ok."

    scene ap cozinha with Dissolve(2.0)

    pause

    gina "É pequena, mas eu imagino que você não cozinhe."

    mc envergonhado "Eu praticamente só como pizza e-"

    gina "Imaginei. Normalmente os residentes deste tipo de apartamento não cozinham, por isso apenas geladeira e microondas."

    gina "Para seu estilo de vida, acredito que cairá como uma luva."

    "Ainda não entendi a dela. Ela realmente acha que eu vou conseguir comprar um apê como este aqui?"

    mc envergonhado "Pois é hehe..."

    gina "Vamos continuar."

    mc normal "Vamos."

    scene ap quarto with Dissolve(2.0)

    pause

    mc surpreso "Caraca! Olha o tamanho da cama!"

    gina "Sim. Como te disse, o quarto está mobiliado de forma planejada. A cama foi feita especialmente para este projeto e é maior que uma king size."

    mc normal "Coisa fina..."

    gina "Sem dúvida. Agora deixa eu te mostrar a última área. Sinto que você vai adorar."

    scene ap banheiro with Dissolve(2.0)

    pause

    gina "O banheiro é maior que o padrão e tem banheira."

    mc normal "Uou. Demais!"

    gina "Além de que ele vem com três vagas na garagem. Quem sabe você não ganha um carro um dia desses também."

    mc "Haha... agora que eu tenho garagem... posso até pensar em algo assim... apesar que com minha grana..."

    gina "Você nunca pensou que visitaria um apartamento como esse aqui também."

    gina "Aliás, é o lugar perfeito pra você trazer suas paqueras e se dar bem com elas. Vai trazer a [m] aqui?"

    mc envergonhado "Que isso, [gina]... hehe..."

    show gina ola with Dissolve(1.0)

    gina "Esse é todo o tempo que eu tenho por hoje."

    gina "Espero que tenha dado pra você conhecer o lugar. Claro que se você ficar com ele, ainda tem mais pra ver com o tempo."

    mc "Gina... sobre isso... Como você espera que eu pague um lugar como esse?"

    if gina_massagem:

        gina "Eu não disse que eu tenho que me redimir com você?"

        gina "O que acha de aceitar esta casa de presente?"

        mc surpreso "Como assim?!"
    else:


        show gina pensando with dissolve

        gina "Os papéis que você descobriu sobre mim. Você fica com a casa, e nós esquecemos esse assunto."

        gina "Fica bom assim pra você?"

        mc surpreso "!"

        "Uma casa pra eu ficar quieto sobre aquele rolo. Certeza que com esse lugar eu posso ajudar a [m]."

        "Eu não vou ter como derrotar essa mulher no tribunal de qualquer forma. Estou ganhando mais do que eu esperava."

        "Vou aceitar."

    show gina ola with dissolve

    gina "Não é nada pra mim, mas pra você vai ser uma grande diferença. Aceite e ficamos limpos."

    "Nem acredito! Vou sair do aluguel! Vai sobrar bem mais grana pra mim no fim do mês!"

    gina "Ah! Só uma coisa antes."

    mc normal "O que?"

    gina "O valor condomínio é um pouco mais caro que o que você paga de aluguel hoje no seu apartamento."

    mc zerado "Alegria de pobre dura pouco..."

    gina "Como?"

    mc envergonhado "Nada não..."

    mc normal "Entendi. O condomínio é o de menos."

    gina "Vai valer a pena, eu garanto. Um apartamento deste padrão nesta ilha das celeridades? Não sai por menos de 1 milhão."

    mc surpreso "A-ah..."

    gina "E uma última coisa. Eu vou precisar do valor para fazer a documentação e passar o imóvel para o seu nome."

    gina "Vamos sair do banheiro?"

    mc normal "Claro."

    python:
        if renpy.android:
            casa = PythonSDLActivity.pegaCasa()

    if not casa:

        jump compra_casa
    else:


        jump casa_comprada

    label compra_casa:

        scene black with Dissolve(1.0)

        "..."

        scene ap sala with Dissolve(2.0)

        pause

        show gina ola with dissolve

        gina "O valor pra passar o imóvel para o seu nome é de {b}R$ 2.000{/b}. Essa é a taxa que o cartório cobra. Será seu único custo."

        python:
            if renpy.android:
                cash = PythonSDLActivity.pegaCash()

        "Realmente, um apartamento desse porte, MEU, por apenas {b}R$ 2.000{/b} é uma oportunidade que poucos têm na vida."

        if cash >= 2000:

            "Eu tenho o dinheiro suficiente comigo. Nem acredito que vou poder ter uma casa própria."

            mc normal "Ok. Eu tenho essa valor comigo. Passo rapidinho no banco e te transfiro."

            gina "Perfeito. Aqui tem minhas informações bancárias."

            gina "Então posso passar o apartamento para seu nome?"

            menu:
                "Sim. Eu vou querer o apartamento.":


                    python:
                        if renpy.android:
                            cash = PythonSDLActivity.pegaCash()
                            
                            if cash >= 2000:
                                
                                PythonSDLActivity.compraCasa()

                    $ renpy.block_rollback()

                    mc charmoso "Com certeza."

                    play sound "extra/carta.mp3"

                    "{b}Você usou {b}C$ 2.000{/b} e adquiriu Apartamento!{/b}"

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("comprou_apartamento","mc","personagem")

                    show black with dissolve

                    "{b}O Apartamento fica salvo no aparelho, se você fez login, ele também fica salvo online na sua conta.{/b}"

                    "{b}Você não precisará pagar por ele novamente, mesmo que reinicie o jogo do zero.{/b}"

                    "{b}Entretanto, se você recomeçar, você precisa voltar neste ponto da história para poder morar nele novamente.{/b}"

                    hide black with dissolve

                    label casa_comprada:

                        $ casa_comprada = True

                        mc charmoso "Então vou transferir o dinheiro pra você logo mais."

                    gina "Perfeito. Vou dar início ao processo, mas a partir de agora o lugar já é seu. Fique à vontade para se mudar quando quiser."

                    mc normal "Ok."

                    gina "Espero que assim fique tudo certo entre a gente."

                    mc normal "Vai sim."

                    if not k7_continua:

                        if gina_massagem:

                            gina "E eu vou esperar você ir em casa mais vezes."

                            mc envergonhado "Sim. Pode deixar."

                        gina "Quem vai querer saber da notícia é sua amiga massagista. Por que você não avisa ela?"

                        mc normal "Essa é uma boa ideia. Vou falar com ela."

                        gina "Boa tarde, [mc]. Aproveite a casa."

                        mc "Obrigado. Até."

                        hide gina with dissolve

                        "Vou falar com a [m]. Quem sabe ela não quer ficar aqui agora que eu tenho um apartamento decente."

                        mc zerado "Espera... eu... não tenho o número dela..."

                        jump karli_a7_continua
                    else:


                        python:
                            if renpy.android:
                                casa = PythonSDLActivity.pegaCasa()

                        gina "Boa tarde, [mc]. Aproveite a casa."

                        mc "Obrigado. Até."

                        hide gina with dissolve

                        "Nem acredito! Consegui! Vou ser o dono desse lugar incrível!"

                        "Tenho que começar a mudar todas minhas coisas."

                        call adeus_casa from _call_adeus_casa

                        "..."

                        jump call_cidade
                "Não. Vou pensar um pouco antes.":


                    jump casa_nao_comprar
        else:


            "Infelizmente, mesmo sendo pouco pra uma casa própria, dois paus é muito pra mim agora."

            "Vou ter que dar um jeito de trabalhar e conseguir essa grana antes."

            show black with Dissolve(1.0)

            p lecionando "Ixi. O [mc] tá pobre que só ele..."

            p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

            p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

            p "Além de garantir este lindo apartamento com muitas cenas inéditas, você ainda contribui com o desenvolvimento de CH."

            p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

            menu:
                "Sim. Tô com uma graninha sobrando aqui.":


                    p rindo "Que bom!"

                    call comprar_cash from _call_comprar_cash_1

                    p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."



                    jump compra_casa
                "Não. Tô pobre igual a ele...":


                    p rindo "Não esquente."

                    p "Trabalhe sempre que possível no bar e vá juntando seus Celebrity Reais. Logo logo você já vai estar com grana suficiente."

                    p "Demora, mas vale a pena!"

                    hide black with dissolve

                    jump casa_nao_comprar

            label casa_nao_comprar:

                if not k7_continua:

                    if cash >= 2000:

                        "Eu tenho a grana pra passar o apartamento pro meu nome, mas não sei se quero isso."
                    else:


                        "Preciso trabalhar bastante no bar e ir juntando devagar esse valor."

                        "Posso pedir pra [gina] esperar e daí quando eu tiver a grana eu aviso ela."

                        "Ou eu posso só esquecer esse lance de apartamento por hora e deixar isso só pro futuro."

                        "Seria bem legal morar aqui, mas preciso ter o pé no chão."

                        "O que eu respondo pra [gina]?"

                    menu:
                        "Preciso de um tempo pra pensar":


                            pass
                        "Continuar a história sem o apartamento":


                            mc normal "Eu agradeço a proposta, mas no momento mudar de casa não me interessa."

                            gina "Você tem certeza, [mc]? Você entende que estou dando ele de graça, né?"

                            mc "Sim. E eu agradeço muito por isso."

                            gina "A proposta estará de pé por tempo indeterminado. Quando você mudar de ideia, me ligue, ok?"

                            mc normal "Muito obrigado."

                            gina "Até mais, [mc]."

                            mc "Até."

                            jump karli_a7_continua

                mc desculpa "Preciso pensar um pouco sobre tudo isso antes. Eu agradeço muito a oferta, mas quero só um tempinho."

                gina "Não há problema. Pense com calma e me avise quando estiver pronto."

                gina "Você tem meu número. Me ligue e resolvemos tudo."

                mc normal "Obrigado."

                gina "Boa tarde, [mc]. Pode olhar a casa à vontade. Quando acabar, deixe a chave na portaria por favor."

                mc "Pode deixar. Obrigado. Até."

                hide gina with dissolve

                "Então eu posso mudar para uma casa como esta. Só preciso de R$ 2.000. É um montante e tanto..."

                "Mas se eu trabalhar com afinco no bar do [gar] e souber guardar, em algum tempo vou ter esse valor."

                "Força, [mc]! Um lugar melhor pra viver só depende de você!"

                jump call_cidade

    label karli_a7_continua:

        $ k7_continua = True

        python:
            if renpy.android:
                casa = PythonSDLActivity.pegaCasa()

        if casa:

            call adeus_casa from _call_adeus_casa_1

            scene mc parque_sentado with Dissolve(2.0)

            pause

            "Já passaram dois dias que eu já posso morar na minha nova casa."

            "Consegui mudar tudo. Por um lado foi triste dar adeus a tudo o que eu tinha."

            "Mas não quis levar nada."

            mc "Não que eu tivesse muita coisa pra levar também."

            "Eu queria conseguir falar com a [m]. Avisar ela que eu tenho uma casa maior agora."

            "Como eu nunca pensei em pegar o telefone dela?"
        else:


            scene black with dissolve

            "{b}Dois dias depois{/b}"

            scene mc parque_sentado with Dissolve(2.0)

            pause

            "Já passaram dois dias que eu encontrei a [gina]."

            if gina_massagem or gina_segredo:

                "Eu não paguei a taxa pra passar o novo apartamento pro meu nome. Espero conseguir mudar isso um dia."

                "Se eu tivesse aquele apê, com certeza eu podia chamar a [m] pra passar um tempo lá até ela ajeitar as coisas."
            else:


                "Fico preocupado com a [m], mas não tem o que eu fazer pra ajudar ela."

            "Se bem que eu nem tenho o telefone dela..."

        "Enfim, não adianta ficar aqui chorando. Ela é adulta e vai conseguir dar um jeito nisso."

        "Se tem uma coisa que a [m] mostrou que é, é ser casca grossa."

        if casa:

            "Vou dar uma última olhada no meu prédio antigo."
        else:


            "Deixa eu voltar pra casa."

    "..."

    scene ilha predio_entrada with Dissolve(2.0)

    "O bom da ilha é que é tudo bem perto uma coisa da outra."

    mc desconfiado "Epa!"

    mc surpreso "[m]!"

    show karli normal with dissolve

    m "Fala aí, [mc]. Beleza?"

    mc normal "Fala aí, garota! Onde você tava?!"

    show karli preocupada with dissolve

    m "Eu?"

    mc desculpa "Claro. Você não tava no salão, e não tá mais trabalhando no Tadaima..."

    mc "Achei que você tivesse morrido, sei lá."

    m "Pois é..."

    m "Mancada preocupar você, só que tô com uns rolos aí."

    mc preocupado "Tô ligado. É o lance do aluguel, né?"

    m "Isso é o principal. Minha grana acabou e eu não tive como acertar nada."

    mc "Eu pensei que a [gina] ia te dar uma folga. Ela tinha-"

    show karli satisfeita with dissolve

    m "Não esquente com isso. Pode deixar que eu vou dar um jeito. Eu sou grandinha."

    mc "..."

    mc desculpa "Olha... eu sei que é meio complicado e talz, mas o que você acha de ficar no meu apê?"

    show karli provocando with dissolve

    m "Calma aí, mocinho. Você tá adiantando as coisas. Nós nem jantamos ainda..."

    mc serio "Eu tô falando sério, [m]."

    show karli preocupada with dissolve

    m "Desculpa. E pra falar a verdade eu também já pensei nisso. Mas eu sei o tamanho desses kitnet do prédio."

    m "Não tem como nós dois morarmos aí."

    if casa:

        mc charmoso "Você não sabe da última?"

        m "Última?"

        mc "Eu mudei de apê. Agora tô o fino do fino."

        show karli normal with dissolve

        m "Como assim, [mc]? Que história é essa?"

        mc desculpa "Bom... não precisa dos detalhes. Só que eu fiz um rolo com a [gina] aí e ela me arranjou um apê."

        mc normal "E um apê de luxo ainda."

        show karli meudeus with dissolve

        m "A [gina]?! Você tá doido, [mc]?!"

        m "Essa mulher é o demônio. Eu falei pra você não se meter com ela..."

        mc charmoso "Não tinha como, [m]. Ter uma casa própria de graça! Não tinha como deixar essa passar."

        m "Bom..."

        show karli preocupada with dissolve

        m "Acho que você tem razão. Teria que ser muito idiota pra deixar essa passar."

        mc charmoso "Que bom que você entende."

        m "..."

        mc normal "Bom. Agora que a cagada tá feita, bora aproveitar. Quer dar uma olhada no lugar?"

        show karli normal with dissolve

        m "Vamo, pô!"

        jump k7_mostra_ap
    else:


        mc desculpa "Acho que você tem razão... O lugar é super pequeno."

        show karli normal with dissolve

        m "Mas valeu por me deixar ficar lá. Você é o cara, [mc]."

        "Droga... eu queria tanto que a [m] ficasse um tempo comigo. A gente ia poder se conhecer melhor e eu ainda ia ajudar ela."

        if not sem_casa:

            "Eu bem que podia arranjar uma grana e pagar o lance da [gina] pra ela me passar o apê."

            "Não é tão caro assim. Algum tempo trabalhando no bar e eu dou um jeito nisso. Vai ser massa demais ter a [m] um tempo em casa."

            "Hmmm... será que eu deixo a situação com a [m] em espera até resolver isso?"

            "Ou será que é melhor desistir dessa ideia dela ficar em casa de uma vez e deixar a [m] resolver o problema sozinha?"

            menu:
                "Esperar um tempo antes de continuar vendo a [m]":


                    "Eu acho que vou pensar melhor nesse lance da casa antes de continuar a ver a [m]."

                    mc normal "[m], calma que eu tô vendo umas coisas aqui e falo com você daqui uns dias, beleza?"

                    m "Como assim, doido? O que você pode fazer nesse tempo?"

                    mc charmoso "Deixa comigo. Ah! Como posso falar contigo?"

                    m "Este é meu telefone. Qualquer coisa me liga."

                    mc "Demorou. Vou tentar ver um lance aqui. Tomara que dê certo."

                    m "Ok... acho que você só tá meio drogado, mas vou te esperar."

                    mc zerado "..."

                    m "Falous."

                    hide karli with dissolve

                    "A [m] tá contando comigo. Quando eu conseguir a grana, preciso ligar pra [gina] e fechar com ela o lance do apê."

                    "Bora continuar o dia agora."

                    jump call_cidade
                "Deixar a [m] resolver o problema sozinha e continuar":


                    "Não tem como eu ajudar ela. Não vou conseguir a grana da [gina] mesmo."

                    "É uma pena, mas ela é grande. Não adianta eu ficar chorando por ela."

                    jump k7_sem_ap
        else:


            "Mas infelizmente não tem muito o que eu possa fazer."

            jump k7_sem_ap

    label k7_mostra_ap:

        $ karli_casa = True

        $ k7_poscasa = True

        scene black with Dissolve(1.0)

        mc normal "Por aqui."

        "..."

        scene ap sala with Dissolve(1.0)

        pause

        mc normal "Bem vinda!"

        m "Uou!"

        mc "Este é meu novo apê. O que achou?"

        m "Não tô acreditando nisso..."

        show karli preocupada with dissolve

        m "Você conseguiu em um rolo com a [gina], né?"

        mc normal "Já falei pra você não se preocupar com isso."

        mc "Vai ser um prazer ter você uns dias aqui."

        m "Sé-sério?"

        mc tarado "Impressão minha ou a [m] que sempre tem respostinha pra tudo ficou sem ter o que falar?"

        show karli meudeus with dissolve

        m "..."

        mc desconfiado "[m]?"

        m "..."

        mc "Tá chorando?"

        m "Cala a boca..."

        mc normal "Você acha que eu ia deixar você na mão?"

        if karli_seducao >= 5:

            mc charmoso "Ainda mais agora que tá rolando um clima entre a gente."

            m "Safado... Mas..."

        m "Valeu, [mc]."

        m "Só dá um tempinho."

        mc "Claro."

        hide karli with dissolve

        "Nem acredito que essa mina ficou emocionada de verdade. Quem diria que a [m] também tem sentimentos."

        show karli preocupada with dissolve

        m "Desculpa por ficar toda emocionada."

        mc desculpa "Eu entendo. Esses tempo não têm sido fáceis pra você, né?"

        m "Nem fala..."

        show karli satisfeita with dissolve

        m "Mas agora tá tudo resolvido. Vou ficar uns dias aqui até resolver um negócio e depois vou poder voltar com o salão."

        mc surpreso "Sério?!"

        m "Sim."

        show karli normal with dissolve

        m "Se não tiver problema, eu gostaria de ficar {b}7 dias{/b} aqui. É o suficiente pra eu dar um jeito na minha vida."

        mc normal "Fique o tempo que você precisar."

        m "Ok... 7 dias então... mas contando a partir de amanhã."

        mc feliz "Ok. Combinado."

        show karli satisfeita with dissolve

        m "Agora eu vou usar aquela sua banheira que achei ela demais."

        mc desconfiado "Ei... nem eu usei ela ai-"

        hide karli with moveoutright

        m "Tchau!"

        mc zerado "..."

        "Vou dar um pouco de privacidade pra ela."

        "Ter a [m] por 7 dias vai ser incrível. Espero que a gente se dê bem."

        $ dia_karli = dia + 8

        jump call_cidade

    label k7_sem_ap:

        $ k7_poscasa = True

        mc desculpa "Eu queria realmente te ajudar, mas como você disse meu apê é pequeno demais."

        m "Sim. Nem eu e nem você ficaríamos confortáveis lá. Mas relaxe, [mc]."

        m "Eu vou precisar de uns dias. Acho que uma semana e pouco é o suficiente e daí já volto com meu salão."

        mc normal "Sério?"

        show karli satisfeita with dissolve

        m "Óbvio, né? Eu sou [m], a resolvedora de problemas."

        mc zerado "Sei..."

        m "Então me dá esse tempo e em {b}9 dias{/b} venha no salão. Eu já vou estar pronta pra continuarmos."

        mc normal "Combinado. Se cuida até lá."

        m "Se cuida você."

        hide karli with dissolve

        "Espero que ela fique bem..."

        $ dia_karli = dia + 8

        jump call_cidade

    label k7_final:

        scene salao geral with dissolve

        mc feliz "Finalmente! O salão tá aberto!"

        show karli satisfeita with moveinbottom

        m "Tcharããããn!"

        m "Tô de volta, pessoal!"

        mc normal "Bem vinda de volta."

        show karli normal with dissolve

        m "Obrigado, nobre súdito."

        if karli_morou:

            m "Falando sério, não teria conseguido sem sua ajuda, [mc]."

            if karli_seducao >= 5:

                show karli provocando with dissolve

                m "Se eu não te conhecesse, ia achar que você queria me comer."

                mc safado "E se eu quiser?"

                m "Por enquanto você não passa de um discípulo no meio do treinamento."

                m "Talvez, se você continuar assim..."

                mc "Vou me esforçar, professora."

                m "Bom garoto..."
            else:


                m "Nunca imaginei que teria um amigo como você."

                mc desconfiado "Falar assim não é sua cara."

                show karli meudeus with dissolve

                m "Cala a boca! Eu tô me esforçando, não tá vendo?"

                mc feliz "Haha! Não precisa disso comigo."

            show karli normal with dissolve

            m "Mas agora é sério. Valeu mesmo, [mc]."
        else:


            m "Tive que aguentar uns perrengues aí, mas cá estou!."

            mc normal "Que bom que deu tudo certo. Estava realmente torcendo pra você voltar."

            if karli_seducao >= 5:

                show karli provocando with dissolve

                m "Você queria era voltar a pegar em mim, né?"

                mc safado "Principalmente... digo, também. Quer dizer..."

                m "Ok, já entendi. Vou deixar você pegar hoje então."

                mc "Oba."

        m "Na verdade depois de todo esse tempo eu vou ter que arrumar tudo por aqui antes de voltar a dar aulas."

        mc preocupado "Sério? Tava pronto pra terminar o curso."

        m "Não seja apressado, homem. Falta pouco agora."

        m "Se bem que faz tempo que você não treina. Acho que posso abrir uma exceção hoje."

        mc charmoso "Perfeito."

        m "Vamos lá pra mesa. Coisa rápida."

        mc "Pode deixar."

        scene salao massagem with Dissolve(1.0)

        if karli_roupao:

            m "Vou colocar meu roupão e deitar."

            m "Cuida bem de mim."

            mc safado "..."

            scene massagem roupao_kita with Dissolve(1.0)

            pause

            "Tenho que prestar bastante atenção."

            "..."

            m "Hmmm..."

            m "Você parece um pouco tenso, mas você não perdeu o jeito depois desse tempo."

            m "Você continua apertando com força. Tô perdida quando eu te ensinar a massagem erótica."

            mc "Tô louco pra aprender."

            m "Eu sei que você tá."
        else:


            m "Vou deitar."

            mc normal "Ok."

            scene massagem kita with Dissolve(1.0)

            pause

            "Tenho que prestar bastante atenção."

            "..."

            m "Você parece um pouco tenso, mas você não perdeu o jeito depois desse tempo."

            mc "Valeu."

        m "Pressione agora os quatro pontos e podemos finalizar por hoje."

        mc "Sim, senhora."

        m "Senhorita."

        mc "Ok, senhorita."

        m "Agora, sim."

        scene black with Dissolve(1.0)

        "É bom voltar a treinar massagem novamente."

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_7","massagem","aula")
            
            if mc_massagem == 6:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula8:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    show karli abraco with vpunch

    m "[mc]!"

    mc "Opa!"

    m "Tô de volta! Hahahaha!"

    mc "Que legal! Bem-vinda!"

    m "Tá. Agora me põe no chão. Que intimidade toda é essa?"

    hide karli with dissolve

    mc zerado "Mas foi você que..."

    show karli satisfeita with dissolve

    m "A deusa do bem estar voltou. Não sei como sobreviveram sem mim."

    mc normal "É bom ver você empolgada assim."

    if karli_morou:

        show karli normal with dissolve

        m "Os dias na sua casa foram sensacionais. Você realmente foi um cavalheiro."

        if karli_seducao >= 5:

            m "No começo até tava um pouco com medo de você me atacar, mas você se comportou direitinho."

            mc zerado "Tava com medo, mas ficava andando de calcinha e sem sutiã..."

            m "Eu tava testando ver se você era um homem ou um cachorro no cio."

            mc "Sei..."
        else:


            mc normal "Obrigado. Você foi uma grande companhia também."
    else:


        show karli normal with dissolve

        m "Fiquei mó tempão longe daqui, mas voltei!"

        mc normal "Que bom!"

    m "E o melhor de tudo é que tô livre da [gina] pra sempre! Nunca mais vamos precisar se preocupar com ela!"

    mc surpreso "Sério?!"

    if gina_atraido:

        "E o pior é que eu tava começando a querer conhecer ela melhor depois daquela massagem..."

    mc feliz "Isso é incrível."

    m "Nem fala... Aquela velha é insuportável. Todo dia no meu pé."

    mc "Hehe."

    m "Ah! E curti você não ter desistido do nosso curso depois desse tempo todo."

    show karli satisfeita with dissolve

    m "A partir de agora, você será condecorado como meu melhor discípulo! Uma honra!"

    menu:
        "É uma honra mesmo! Obrigado!":


            mc feliz "Obrigado! É uma grande honra!"

            m "É mesmo. Ajoelhe e beije meus pés."

            mc zerado "Não exagere."

            m "Ingrato!"
        "Provavelmente eu sou o único fazendo o curso.":


            mc zerado "..."

            mc envergonhado "Alguma coisa me diz que eu sou o único fazendo o curso..."

            m "Calado! Isso não vem ao caso."

            mc zerado "Só q-"

            m "Eu disse CALADO PLEBEU!"

    "A [m] tá com a corda toda. Acho que nunca vi ela tão feliz."

    show karli normal with dissolve

    m "Pensando bem... acho que você merece um ritual de condecoração."

    mc envergonhado "A é? Você vai pegar sua espada e me transformar em cavaleiro?"

    m "Não, mas eu vou providenciar um ritual à altura."

    m "O que você acha da gente ir pra balada, hoje?"

    mc surpreso "Balada?!"

    m "É ué. Putz putz, tchdum tchdum, BEE WOO WOOP.... BOOT DOO DOOT!"

    mc desconfiado "..."

    m "Pera, deixa eu fazer de novo."

    mc zerado "Eu já entendi. Não precisa fazer de novo."

    m "Então? Tá afim ou não?"

    mc charmoso "Claro que eu tô."

    menu:
        "Vai ser legal.":


            mc normal "Vai ser massa a gente passar um tempo juntos."

            mc "Você vai me contar mais sobre seu passado obscuro que levou você a virar essa coisinha rebelde."

            m "Só fala bosta..."

            mc "Sei..."
        "Só se a gente for se beijar lá.":


            $ karli_seducao += 1

            mc safado "Mas só se a gente for se beijar lá."

            show karli provocando with dissolve

            m "Como gosta da minha boca..."

            m "Ele queria tanto poder morder ela..."

            mc "Com certeza."

            m "Talvez hoje finalmente role algo entre a gente."

            m "Mais do que já rolou, né? Porque com o curso você deve ser o homem que mais pegou em mim na vida."

            mc charmoso "Bom saber."

    m "Então tá combinado."

    if tempo == 2:

        m "Ainda nem é noite. Vai em casa, assiste seus animes e me encontra ali na entrada do prédio umas onze."
    else:


        m "Já tá meio tarde. Só toma um banho e pode voltar aqui. A gente sai umas onze."

    mc normal "Fechou."

    m "Vou tomar um banho de banheira."

    hide karli with dissolve

    mc surpreso "Você tá tirando a roupa?!"

    m "Para de olhar, tarado."

    mc envergonhado "..."

    play sound "audio/som_16_chuveiro.mp3"

    scene ape_chuveiro with Dissolve(2.0)

    "Sair com a [m]... Em uma balada..."

    if karli_morou:

        "A gente ficou bem mais próximos dias que ela passou uns dias aqui em casa."

    if karli_seducao >= 5:

        "Eu e ela nos engraçamos um pouco durante as aulas."

        "Várias vezes eu tentei puxar a conversa pra um lado mais sensual, e ela nunca fugiu das minhas investidas."

        "Pensando bem agora, mesmo nunca brigando comigo, acho que ela nunca realmente entrou na minha."

        "Talvez eu tô achando que tô abafando e na verdade continuo no limbo..."

        if karli_roupao:

            "Ela aceitou até colocar o roupão nas aulas comigo."

        "Eu sinto que a gente tem, sim, uma certa tensão sexual."

        "Hoje vai ser a hora certa de aumentar essa tensão e finalmente dar o bote."

        "Mas a [m] é meio espertinha demais. Se eu for com muita sede ao pote, ela vai acabar me chutando."

        "Tenho que chegar na manha, seduzir ela e fazer ela querer ficar comigo."
    else:


        "Eu não parti para o lado sensual com a [m], por isso hoje vai ser tipo uma noite de amigos."

        "Vou aproveitar pra descobrir mais sobre ela e principalmente mais sobre massagem."

        "Às vezes a [m] parece mó relax, mas ela leva a arte dela muito à sério. Eu posso realmente virar um excelente massagista como aluno dela."

    if tempo == 2:

        "Ainda dá tempo de ver uma Netflix."

        $ tempo += 1

        scene ape_tv with Dissolve(1.0)

        stop sound

        "Dois irmãos boa pinta nesse carro caçando bruxas, vampiros e até o papai noel?"

        "A série fala mais sobre eles dois que sobre os monstros."

        "Certeza que isso não vai durar nem uma temporada direito. Vai ser um fracasso, escuta o que eu tô falando."

    "Ixi, dá mais tempo pra nada. Vou me trocar e encontrar a [m]."

    "..."

    scene ilha predio_entrada with Dissolve(1.0)

    "Epa. Ela já tá esperando."

    mc surpreso "!"

    show karli n_cheiona with dissolve

    m "Fala aí, [mc]. Que demora."

    mc charmoso "[m], tu tá linda."

    m "Hm?"

    show karli n_falando with dissolve

    m "Só agora você viu?"

    m "Você tem problema na vista?"

    mc normal "Tá bom. Pode parar com suas piadinhas de humor questionável."

    if karli_seducao >= 5:

        mc charmoso "Hoje a gente tem um encontro e vai ser bem massa."

        show karli n_seduzida with dissolve

        m "Você vai cuidar bem de mim?"

        mc "Com certeza."

        m "Não deixa nada acontecer comigo até eu voltar pra casa, moço..."

        mc envergonhado "Você gosta mesmo de brincar comigo, hein."

        m "Eu adoro."
    else:


        mc normal "Bora beber muito. Quero ver você dançando."

        m "E vai ver."

        mc envergonhado "Não creio..."

        m "Eu adoro dançar."

        mc "Nunca iria imaginar."

        m "Ah... cala a a boca."

    m "Olha..."

    show karli n_falando with dissolve

    m "A gente vai num lugar meio da pesada, beleza?"

    m "Espero que não seja demais pra você."

    mc desconfiado "Como é?"

    m "É uma balada subterrânea que um pessoal meio estranho frequenta."

    mc "..."

    m "Mas não esquente que você vai tá comigo. Morou?"

    if v10_fim:

        mc charmoso "E eu lá tenho medo disso?"

        "Se ela soubesse que já apontaram uma arma pra minha cabeça..."
    else:


        mc envergonhado "Ok. Não precisa colocar medo em mim."

        m "Nada. Só tô avisando."

    show karli n_cheiona with dissolve

    m "Vamo?"

    mc charmoso "As damas na frente."

    m "Então pode ir."

    mc zerado "..."

    m "Tudo bem... eu posso ser uma dama hoje."

    hide karli with dissolve

    mc envergonhado "Quem entende essa mina?"

    m "Eu ouvi isso!"

    scene onibus parado_noite with Dissolve(1.0)

    "..."

    mc normal "Fica na parte continental da cidade?"

    m "Mais ou menos. Fica numa parte que você nunca viu."

    mc desconfiado "Como assim?"

    m "Você vai ver."

    scene black with dissolve

    "..."

    "..."

    m "Vamos descer aqui."

    mc "Opa."

    scene cidade centro6 with Dissolve(2.0)

    pause

    mc desconfiado "Que biboca é esta aqui?"

    show karli n_cheiona with dissolve

    m "Não precisa cagar nas calças, [mc]."

    mc zerado "Ninguém tá cagando nada aqui."

    show karli n_falando with dissolve

    m "Este lugar tem um segredinho. Já ouviu falar da {b}Isla de Muerta{/b}?"

    mc envergonhado "Acho que não..."

    m "É uma ilha que não pode ser encontrada, a não ser por aqueles que sabem onde ela está."

    mc desconfiado "Não sei se eu entendi."

    m "Quero dizer que a gente vai num lugar que só quem sabe onde está pode achar."

    mc envergonhado "Você tá assistindo muita série."

    hide karli with dissolve

    m "Para de falar e vem."

    "..."

    scene black with dissolve

    "..."

    "A gente tá passando por uns lugares bem estranhos."

    "Será que é possível que a [m] queira me assassinar?"

    if gina_atraido:

        "E se ela descobriu que eu fiz aquela massagem na [gina]?"

    "Pare de pensar idiotice. É claro que el-"

    mc surpreso "!"

    scene chinatown viela with Dissolve(2.0)

    pause

    show karli n_cheiona with dissolve

    m "Bem-vindo à {b}China Negra{/b}."

    if s4_chinatown_visita:

        "Porra. Eu conheço aqui. É que eu não lembrei deste trecho."

        "A primeira vez que eu vim aqui foi o [chi] que me trouxe."

        mc charmoso "Tô ligado. Eu conheço aqui."

        m "Não creio..."

        mc "O [chi], que trabalha no bar, me trouxe aqui pela primeira vez."

        m "Tu é rodado, hein, [mc]."

        mc zerado "Por que isso não parece um elogio..."

        m "Mas, deixando a zoação de lado, tô realmente impressionada que você conhece esse lugar."

        m "Você é cheio dos lance."

        mc envergonhado "..."
    else:


        mc surpreso "Que lugar é esse?!"

        m "É um dos bairros obscuros da capital."

        mc surpreso "..."

        m "Não precisa ficar de boca aberta assim por 5 minutos."

        mc envergonhado "Caraca..."

        m "Não sei por que, mas alguma coisa tá me dizendo que seu trabalho de paparazzo ainda vai te trazer aqui outras vezes."

        mc "Não sei se fico empolgado ou com medo."

        m "Haha! Cagão!"

    m "Bom. Estamos quase lá. Vem."

    hide karli with dissolve

    "..."

    scene chinatown clube with Dissolve(2.0)

    pause

    m "Aqui é a entrada do clube. Você vai curtir muito."

    "Olha pra tudo isso. Essa China Negra é de outro mundo."

    m "Vem!"

    scene black with dissolve

    "{i}DUNG DUNG ~~ DUNG DUNG{/i}"

    "Esse som martelando minha cabeça. Fazia muito tempo que eu não vinha num lugar assim."

    "{i}DUNG DUNG ~~ DUNG DUNG{/i}"

    "..."

    play sound "audio/som_20_balada.mp3" loop

    scene balada geral at treme_balada with Dissolve(2.0)

    pause

    "{i}DUNG DUNG ~~ DUNG DUNG{/i}"

    show karli n_cheiona with dissolve

    m "{size=8}E aí? curtiu?{/size}"

    mc desconfiado "QUÊ?!"

    m "E AÍ? CURTIU?!"

    mc normal "CURTI SIM!"

    m "O DJ DAQUI É MUITO BOM! O CARA MANJA DAS PARADAS!"

    mc "MUITO LEGAL!"

    show karli n_seduzida with dissolve

    m "NINGUÉM VEM NA BALADA PRA CONVERSAR! BORA DANÇAR!"

    mc envergonhado "Não sei, não, [m]..."

    m "QUÊ?!"

    mc zerado "A gente vai ter que se falar gritando assim o tempo todo?"

    m "QUÊÊ?!"

    mc envergonhado "NÃO VOU DANÇAR AGORA!"

    show karli n_falando with dissolve

    m "AH!"

    m "TÁ LEGAL! VOU LÁ!"

    hide karli with dissolve

    "Que merda..."

    "Caralho, mano. Eu sou muito bundão. Só que não adianta. Não tenho coragem de dançar. Nunca dancei na vida."

    "A [m] parece que ficou super decepcionada."

    "Afe! Tenho que fazer alguma coisa."

    "Acho que vou pelo menos dar uma olhada na pista."

    "..."

    mc surpreso "!"

    scene karli balada_dancando with Dissolve(2.0)

    pause

    "Uou..."

    "A [m] tá tão sexy dançando desse jeito."

    "É como se não tivesse ninguém além dela aqui. Tão de boa... É tipo ela e a música só."

    "Não sei porque, mas ver ela assim deixa ela tão atraente..."

    if karli_seducao >= 5:

        "Como eu queria poder subir ali e pegar ela. Poder dar uma mordida nessa mina."

        "Calma... respira..."

        mc concentrando "..."

        "Eu preciso dançar. É o único jeito."

    m "[mc]? Pronto pra dançar?"

    mc envergonhado "Hehe... NÃO SEI!"

    m "VEM COMIGO! VAI DEIXAR UMA DELÍCIA DESSAS DANÇANDO SOZINHA?!"

    m "VEM! EU TE AJUDO!"

    "Se eu subir lá e dançar igual um pato eu estrago tudo..."

    "Mas se eu não subir, talvez eu estrague tudo sem nem tentar."

    "Droga... E agora?"

    menu:
        "Vou tentar dançar.":


            "Ah, mano! Seja o que Deus quiser! Bora mexer o esqueleto."

            mc envergonhado "TÁ LEGAL! MAS ME AJUDA!"

            m "EBA! PODE DEIXAR!"

            jump karli_e8_danca
        "Não vou dançar. Vou esperar no bar.":


            "Não tenho coragem. Melhor não arriscar e investir no certo."

            "Vou esperar ela no bar."

            mc normal "VOU TOMAR ALGO NO BAR. DEPOIS VAI LÁ!"

            m "TÁ!"

            "..."

            jump karli_e8_bar

label karli_e8_danca:

    $ karli_dancou = True

    scene balada pista at treme_balada with Dissolve(2.0)

    show karli n_seduzida with dissolve

    m "É FÁCIL! SÓ MEXE UM POUCO O CORPO! TENTA MEXER NO PASSO DA BATIDA!"

    "É muito mais fácil falar do que fazer..."

    m "SEGUE EU E COMEÇA!"

    hide karli with dissolve

    mc "OK..."

    show karli mc_dancando with dissolve

    pause

    m "VAI FAZENDO ASSIM. VAI SEGUINDO MEU QUADRIL."

    "Não acredito que tô fazendo isso... Eu devo parecer um idiota."

    m "VOCÊ TÁ INDO BEM. OLHA BEM PRA MIM."

    mc "TÁ!"

    "Pelo menos parece que ela tá se empolgando."

    if karli_seducao >= 5:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("karli_beijo","karli","personagem")

        $ karli_beijo = True

        "Opa. Acho que ela chegou mais perto de mim."

        m "ISSO. MEXE COMIGO. DEIXA EU TE AJUDAR."

        "Opa! Ela tá quase encostando em mim!"

        m "Assim não preciso gritar."

        mc "Hehe verdade..."

        m "..."

        "O clima tá esquentando. Ver ela rebolando desse jeito tão perto, tá me deixando duro."

        m "Deixa eu te mostrar outra coisa agora."

        mc "T-tá!"

        m "Quando tem uma mina dançando bem pertinho, você pode passar seus braços e pegar na cintura dela."

        mc "Qu-quê?!"

        m "Pega logo."

        show karli mc_dancando2 with Dissolve(1.0)

        pause

        m "Assim. Isso! Você é um homem. Pega com força."

        m "Continua mexendo."

        mc "O-ok."

        "A bunda dela tá roçando em mim. E do jeito que ela tá mexendo, tô ficando louco."

        "Eu acho que ela tá curtindo isso também."

        m "Quando uma mina tá dançando assim com você, pode ser atrevido. Se você fizer algo que não deve, ela vai saber te mostrar."

        m "Pode arriscar, [mc]."

        "Ela tá falando diretamente pra mim. Não vou perder a chance."

        show karli mc_dancando3 with Dissolve(1.0)

        pause

        m "Ai..."

        mc "Seu cheiro é muito bom."

        m "Hmmm..."

        m "Continua... dançando..."

        "Ela tá muito excitada eu acho."

        "É agora ou nunca."

        mc "Vira aqui, [m]."

        m "Quê?"

        show karli balada_beijo with Dissolve(2.0)

        pause

        m "Hmmm"

        m "[mc]."

        mc "..."

        mc "Faz tempo que eu quero te beijar."

        m "Mas..."

        mc "Só me beija."

        m "..."

        window hide

        pause

        hide karli with dissolve

        if priscila_namoro:

            "Droga... acabei esquecendo da [c]. Que mancada..."

        if sayuri_e4 == "namoro":

            "Desculpa, [s]... eu não aguentei."

        "Caraca. Que beijão que a gente deu."

        "Nem sei o que pensar depois de uma dessas."

        show karli n_seduzida with dissolve

        m "E não é que a gente ficou mesmo?"

        mc charmoso "Espero que você tenha gostado. Eu gostei muito."

        m "Eu também..."

        "Ela não parece muito empolgada. Mas não vou começar com insegurança agora."
    else:


        "Nem sem quanto tempo a gente já tá dançando. A [m] parece tá curtindo pra caramba."

        mc normal "Você tá realmente se divertindo, hein?"

    mc "E o que você acha daquela bebida agora?"

    show karli n_cheiona with dissolve

    m "Tô dentro. Gogogo!"

    "..."

label karli_e8_bar:

    scene balada bar with Dissolve(2.0)

    if not karli_dancou:

        "Será que eu devia ter arriscado? Mas e se eu ferrasse tudo?"

        "Não. Melhor ir pelo seguro e não passar vergonha."

        "Vou dar um tempo aqui, beber uma coisa e esperar ela voltar."

        "..."

        "..."

    show karli n_seduzida with dissolve

    m "Ufa... cansei..."

    if karli_dancou:

        m "Você foi uma boa companhia."

        if karli_beijo:

            m "Abusadinho... mas até que dançou bem."

            mc safado "Nunca imaginei que dançar fosse tão bom."

            m "Gostou, né?"

        m "Obrigada por ter me acompanhado. Teve uma hora lá que eu achei que você não ia, não."

        mc envergonhado "Eu também achei."

    mc normal "Mas que bom que você se divertiu."

    m "Foi massa ter vindo com você."

    mc zerado "E graças aos céus a música aqui não tá tão alta. Até consigo te escutar."

    show karli n_falando with dissolve

    m "Será que se eu ficar muito tempo perto de você eu pego sua chatisse?"

    mc zerado "Como é?"

    m "Daí eu vou começar a reclamar da música e querer dormir nove da noite?"

    m "Que perigo..."

    mc "..."



    m "Mas mesmo com esse jeito de zumbi, até que você é legal, [mc]."

    show karli n_ferrada with dissolve

    m "Desde que você apareceu no salão pra fazer o curso, você só tem me ajudado."

    m "E se eu tô pronta pra voltar a massagear e seguir com meu sonho, é porque você esteve comigo."

    mc preocupado "[m]..."

    m "E quando você apareceu lá no salão com seu cupom achei que era só mais um otário querendo pegar nas novinhas."

    if karli_seducao >= 5:

        m "E você é até um pouco mesmo."

        mc envergonhado "..."

    m "Só que, tipo, você é muito mais que isso."

    m "Eu queria falar várias coisas da hora agora, mas eu não tenho jeito pra isso."

    m "Então, obrigada."

    mc desculpa "Não precisa agradecer. Não fiz nada de mais."

    show karli n_cheiona with dissolve

    m "Bom que você acha isso. Porque se quisesse dinheiro em troca, tava ferrada."

    mc zerado "..."

    m "Bom. Sem querer ser a chatona, mas acho que tá dando nossa hora. Já é quase quatro."

    mc concentrando "Já? Por isso que me bateu o sono aqui."

    m "Cansadão..."

    mc "..."

    m "Então bora."

    mc "Vamos."

    scene black with Dissolve(1.0)

    "..."

    mc normal "Sorte que o ônibus da ilha pro centro é 24 horas."

    m "Alguma coisa tinha que funcionar direito nessa cidade."

    mc "Parece uma chata falando."

    m "Chata? Então bora ser chata. Vou daqui até a ilha te falando todas as características teóricas de cada ponto da massagem."

    mc angustiado "Não, por favor!"

    m "O primeiro ponto é o..."

    "..."

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_8","massagem","aula")
            
            if mc_massagem == 7:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula9:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    m "E aí? Quais são as novas?"

    mc desconfiado "Eu que te pergunto. Conseguiu arrumar tudo aí?"

    m "Na verdade eu nem vou precisar."

    mc "Como assim?"

    m "Eu vou ser despejada de novo..."

    mc angustiado "Como assim?!"

    m "Pois é. Aconteceram umas coisas aí..."

    mc zerado "Que coisas? Você pode ser um pouco mais clara?"

    show karli preocupada with dissolve

    m "Umas coisas aí, [mc]..."

    mc "..."

    m "Tá! Eu explico!"

    if karli_morou:

        m "Lembra que eu fiquei na sua casa um tempo, né?"

        mc normal "A-hã."
    else:


        m "Lembra aqueles dias que eu sumi?"

        mc desconfiado "Sim."

    m "Então. Eu acabei resolvendo meus problemas com a dona do prédio aqui."

    mc feliz "Que beleza."

    m "Sim. Por isso que eu consegui voltar."

    mc normal "Certo. E daí..."

    m "Daí que agora tudo caiu por terra de novo e ela vai me expulsar."

    mc zerado "Mas como..."

    m "Não interessa, [mc]."

    m "Olha... eu agradeço, de coração, tudo o que você fez por mim. De verdade."

    m "Mas não vai ter jeito. É melhor a gente aceitar logo que não vai dar pra eu continuar morando por aqui."

    m "Além de que pra você não faz muito diferença. Você já tá quase completando o curso."

    m "A gente faz uma aula hoje e daí amanhã a outra e daí eu posso formar você."

    mc preocupado "Não, [m]! Não é essa a questão!"

    m "Quê? Calma..."

    menu:

        "Porra! Tu sabe que eu tô afim de você!" if karli_seducao >= 5:

            mc zerado "Você sabe que eu tô afinzão de você, [m]. Não quero que você vá."

            if karli_morou:

                mc desculpa "Aquele tempo que você morou em casa foi muito foda."

            if karli_beijo:

                mc desculpa "Quando a gente foi na balada eu curti pra caralho. Nosso beijo e tudo!"

            mc "Não quero que você se ferre e tenha que se mudar sei lá pra onde."

            show karli normal with dissolve

            m "[mc]... você fica todo fofo apaixonado."

            mc zerado "E pare de brincar comigo..."

            show karli preocupada with dissolve

            m "Desculpa... não queria zoar com isso. Eu entendo..."

            m "Mas eu queria que vo-"
        "Eu não quero que você desista do seu sonho!":


            mc preocupado "Não quero que por causa de dinheiro você tenha que deixar seu sonho."

            mc serio "Isso é ridículo."

            m "A vida não é fácil, [mc]... A gent-"

    mc serio "Não! Não vou aceitar isso."

    mc "Eu vou resolver seu problema. Eu já resolvi mais de uma vez, não resolvi."

    m "O pior é que resolveu, só que dessa vez não tem como."

    mc "Merda..."

    if karli_ajudou:

        mc "Você sabe que eu já consegui livrar sua barra conversando com a [gina]. Eu posso fazer isso de novo."

        show karli meudeus with dissolve

        m "Não! Não quero que você se meta com ela!"

        mc preocupado "Mas eu já-"

        m "Já disse que não, [mc]! Você é tonto?!"

        mc desculpa "Tá. Eu só queria te ajudar..."

        m "{i}tsc{/i}"

        "A [m] realmente tem asco dessa mulher. A [gina] também não morre de amores por ela. Com certeza elas não se bicam."

    show karli normal with dissolve

    m "Olha... você é um cara diferente. Você, sei lá, gosta de ajudar as pessoas. Mesmo sem querer nada em troca."

    m "Tipo, isso é coisa de alien. Ninguém na terra é assim."

    mc zerado "Não exagere."

    m "Eu tô fazendo cara de séria, olha aqui. Não tô te zuando."

    m "Eu realmente acho que você veio de outro mundo. Um mundo onde existem fadas e a gente é atacado por criaturas embaixo da água."

    mc angustiado "Credo!"

    m "Eu fico muito feliz de ter encontrado você e tudo o que aconteceu."

    if karli_morou:

        m "Os dias que a gente passou juntos na sua casa."

    if karli_beijo:

        m "A gente dançando na balada..."

        m "O nosso beijo. Vai ser algo inesquecível pra mim."

        mc zerado "Eu agradeço, mas foi só um beijo..."

        m "Foi mais que só um beijo pra mim, tá?"

        mc tarado "Tenho 100 porcento de certeza que eu me lembraria se tivesse rolado algo mais que um beijo."

        m "Me deixa, filho do cão!"

    m "Mas dessa vez realmente não dá. Se tivesse um jeito, você não acha que eu te falaria?"

    mc "Mas, [m]. A ge-"

    "{i}Ding Dong{/i}"

    m "Agora dá o fora que eu tenho cliente."

    mc surpreso "Então você realmente trabalha?!"

    show karli provocando with dissolve

    m "Engraçadinho... Pica a mula!"

    mc desculpa "Eu volto hoje ainda. Não vai se mudar antes de me dar um tchau decente."

    m "Tá. Pode deixar. Agora tchau!"

    hide karli with dissolve

    mc surpreso "Calma, tô saindo!"

    if tempo == 2:

        scene mc parque_sentado with Dissolve(1.0)

    elif tempo >= 3:

        scene mc parque_sentado_noite with Dissolve(1.0)

    mc "Que saco..."

    if gina_massagem:

        "Eu fiz massagem na [gina] aquele dia e ela ficou bem agradecida."

        "Eu podia tentar alguma coisa com ela de novo."

        "Provavelmente ela vai querer outra massagem..."

        if gina_atraido:

            mc "E do jeito que as coisas tão indo, já consigo até ver onde vai dar..."

            "Não seja tarado, [mc]!"
        else:


            "O problema é que com certeza as coisas vão avançar mais ainda..."

            "O que eu vou fazer se ela não quiser ficar só na massagem? Não vou conseguir fazer isso."

    if gina_segredo:

        "Eu descobri aquele podre da [gina]. E ela até sabe que eu sei."

        "Mas ela me ofereceu a casa de graça. Eu não quero perder essa chance comprando briga com ela."

    if gina_massagem:

        label karli_e9_decisao:

            "O que eu não entendo é porque a [m] não quer que eu fale com a [gina]. Ela deixou isso bem claro."

        "Mas se eu não fizer nada ela vai ser despejada. Isso ia ser uma bela merda."

        "Não tem jeito. É uma decisão que eu vou ter que tomar por mim mesmo."

        menu:
            "Ignorar o aviso da [m] e falar com a [gina]":


                "A [m] foi bem incisiva pra eu não falar com a [gina]."

                "Será que realmente é uma boa eu entrar em contato com ela? Eu não vou desrespeitar a [m]?"

                menu:
                    "É pelo bem da [m]. Eu vou falar com a [gina].":


                        $ karli_gina = True

                        mc "Eu tenho que falar com a [gina]. Eu não posso deixar a [m] ser despejada sem fazer nada."

                        mc "Desculpa, [m]. Tomara que você não fique puta demais comigo."

                        "Deixa eu voltar pra casa e ligar pra ela."
                    "Tenho que pensar melhor.":


                        "Melhor eu pensar direito na minha decisão."

                        jump karli_e9_decisao
            "Deixar a [gina] de lado e não ajudar a [m]":


                "A [m] falou pra eu não falar com a [gina]. Então acho melhor eu não desrespeitar ela."

                "Só que se eu não fizer nada, ela vai ser despejada. E agora?"

                menu:
                    "Não vou desrespeitar a [m]. Não vou procurar a [gina].":


                        mc "Não posso invadir o espaço da [m]. Se ela prefere ser despejada ao invés de falar com a [gina], a decisão é dela."

                        "Acho que eu vou dar um tempo pra ela atender o cliente e voltar falar com ela."

                        "Se ela realmente vai ser despejada, eu quero dar um adeus pra ela."

                        "Quem sabe minhas útlimas aulas de massagem."

                        jump karli_e9_depois
                    "Tenho que pensar melhor.":


                        "Melhor eu pensar direito na minha decisão."

                        jump karli_e9_decisao
    else:


        "Bom... eu não quis fazer massagem na [gina] naquele dia. Eu não tenho como fazer nada nesse caso."

        "Acho que eu vou dar um tempo pra ela atender o cliente e voltar falar com ela."

        "Se ela realmente vai ser despejada, eu quero dar um adeus pra ela."

        "Quem sabe minhas útlimas aulas de massagem."

        jump karli_e9_depois

    "..."

    scene ape_geral with Dissolve(1.0)

    show mc telefone with dissolve

    "{i}tuuu.... tuuu...{/i}"

    gina "[mc]?"

    mc "Oi, [gina]."

    gina "Que bom ouvir sua voz. Tudo bem?"

    mc "Tudo sim."

    gina "Eu sabia que você ia me ligar, sabia?"

    mc "Sério?"

    gina "Sim. Mas o que acha de conversarmos aqui em casa? Eu estou na piscina, sem nada pra fazer. O que acha?"

    "Obviamente..."

    mc "Pode deixar. Chego logo."

    gina "Estou esperando. Beijos."

    mc "Até."

    hide mc with dissolve

    "Tenho que ir pra lá. Bora."

    scene black with Dissolve(1.0)

    "..."

    mc normal "Oi."

    gina "Pode entrar, [mc]."

    scene mansao porta with Dissolve(1.0)

    mc normal "Boa tarde, [gina]."

    show gina b_provocando with dissolve

    gina "Boa tarde, lindo. Você chegou na hora certa. Minhas costas estão me matando."

    mc envergonhado "Então você vai querer outra massagem?"

    gina "Com certeza. Vamos conversar enquanto você me massageia."

    mc "Tudo bem."

    gina "Fico contente de você ter aceitado tão fácil agradar esta pobre velha."

    "Só se for pobre de espírito..."

    mc "Haha..."

    gina "Agora vamos. Estou MUITO ansiosa."

    play sound "audio/som_35_passos.mp3"

    "..."

    scene mansao piscina with Dissolve(1.0)

    show gina b_pensando with dissolve

    gina "Você espera enquanto eu pego o equipamento?"

    mc normal "Claro. Quer ajuda?"

    gina "Não se preocupe. Volto em um instante."

    mc "Tá."

    hide gina with dissolve

    "..."

    gina "Vou colocar aqui, igual da outra vez."

    mc "Já pode se ajeitar."

    gina "Sim, senhor."

    scene gina mas_chamando with Dissolve(1.0)

    gina "Estou pronta, doutor."

    mc envergonhado "Ok..."

    mc "Vou fazer igual da outra vez, tudo bem?"

    gina "Claro. O que você achar melhor."

    scene gina massagem_normal with Dissolve(1.0)

    gina "Hmm..."

    gina "Tá perfeito, [mc]."

    mc "Que bom que você tá gostando."

    gina "Atrapalha o tratamento se eu falar?"

    mc "Não, não. Fique à vontade."

    gina "Então... provavelmente você ligou pela situação da [m] novamente, estou certa?"

    mc "Sim..."

    gina "Então no fundo vocês não tinha nada mesmo. Eu achei que vocês eram namorados ou algo assim."

    if karli_beijo:

        mc "Pra falar a verdade, a gente foi pra balada e se beijou até."

        gina "Como?!"

        mc "Ué, que que tem?"

        gina "Nada, não..."

        gina "Mas as coisas não evoluíram."

        mc "Exatamente."

    elif karli_seducao >= 5:

        mc "Eu senti que tava rolando um clima entre a gente. Eu dei em cima dela e ela até aceitou."

        gina "Entendo..."

        gina "Mas as coisas não evoluíram."

        mc "Exatamente."
    else:


        mc "Não, não. A gente só é amigo mesmo."

        gina "Entendi."

    gina "A [m] sempre teve problemas com namorados."

    mc "Ah? Como você sabe disso?"

    gina "Ah! Bem... eu conheço ela há bastante tempo. Não é à toa que ela locou um imóvel meu."

    mc "Eu sinto que vocês não se dão tão bem."

    gina "Sim. Ela fez coisas que me machucaram muito."

    mc "Sério?"

    gina "Sim. Eu sei que é difícil de acreditar, pois ela parece um anjinho. Mas você sabe que ela pode ser meio cabeça dura."

    mc "Haha! Isso você tem razão."

    gina "O que você acha da gente pular a história triste e ir pro que importa?"

    mc "Pra mim, tudo bem."

    gina "Eu mandei ela desocupar o prédio e não tem nada que você possa fazer pra mudar isso, infelizmente."

    mc "Como?! Por que?!"

    gina "Peço desculpas."

    mc "Mas, [gina]!"

    scene gina mas_chamando with Dissolve(1.0)

    mc "Então-"

    gina "Calma. Eu sei que você aceitou me massagear por causa da [m], mas eu pensei que eu pudesse te pagar de OUTRA FORMA."

    mc desconfiado "[gina]... eu..."

    gina "Eu estou com um músculo muito dolorido aqui atrás... um pouco abaixo das costas. Será que você não quer dar uma olhada?"

    gina "Eu acho que suas mãos com certeza poderiam me ajudar. Pegar bem firme na minha traseira e dar um jeito nela. O que você acha?"

    mc surpreso "!"

    "E-ela tá falando... Essa- essa- mulher!"

    gina "O que você acha?"

    menu:
        "Talvez eu possa dar uma olhada...":


            mc tarado "Assim... talvez eu realmente possa ajudar com sua dor. A massagem é pra isso, certo?"

            gina "Sim. E talvez você possa até usar outra coisa além das mãos, pra dar aquela ajuda."

            mc surpreso "!"

            gina "Eu acho que você vai gostar muito da minha proposta."

            "Deus do céu... eu tenho certeza que ela tá pensando besteira."

            menu:
                "Eu aceito. Pode se virar.":


                    $ gina_bunda = True

                    mc safado "Não posso deixar você sozinha com essa dor. Eu sou um cavalheiro. Pode se virar."

                    gina "Muito obrigada, doutor. Cuide bem de mim."

                    mc "..."

                    scene gina_massagem1 with Dissolve(1.0)

                    mc "E-então vou dar uma olhada aqui, tudo bem?"

                    gina "Isso. Mais pra baixo... aí mesmo."

                    mc "Ok..."

                    gina "Hmmm... perfeito. Veja bem, doutor. Eu estou nas suas mãos."

                    mc "Pode deixar. Vou massagear bem a região."

                    gina "Isso. Pode pegar pesado comigo. Eu preciso mesmo."

                    mc "Deixa comigo."

                    window hide

                    pause

                    gina "Acho que seria melhor se você subisse em cima da mesa e se concentrasse só nessa parte."

                    mc safado "Também acho."

                    scene gina_massagem2 with Dissolve(1.0)

                    gina "Muito bom. Chega mais perto da região agora e pode colocar a mão na massa."

                    mc "Eu vou trabalhar muito bem aqui."

                    mc "Inclusive deixa eu aplicar mais pressão com meu corpo."

                    gina "Muito bom. Você é o especialista. Pode fazer como você quiser."

                    "Nem acredito que ela tá deixando eu apertar a bunda dela com meu..."

                    gina "Isso. Pode mexer bastante. Eu adoro quando massageiam aí."

                    mc "Melhor quando usam outras coisas além das mãos, né?"

                    gina "Melhor ainda. Pode usar."

                    window hide

                    pause

                    mc "Acho que seu biquini aqui embaixo tá atrapalhando."

                    gina "Isso! Tira ele, doutor!"

                    scene black with dissolve

                    gina "Isso! Bem melhor! Eu tô sentindo você."

                    mc tarado "Você vai sentir muito mais."

                    scene gina_massagem3 with Dissolve(1.0)

                    gina "AH!"

                    gina "ASSIM!"

                    gina "Isso! Me massageia!"

                    mc "{i}Ugh{/i}"

                    gina "Mais um pouco! Assim!"

                    gina "AAH!"

                    mc "AAH!"

                    scene black with dissolve

                    mc "{i}puf puf{/i}"

                    mc "Ufa..."

                    mc "{i}puf puf{/i}"

                    gina "Você massageou muito bem, [mc]."

                    scene gina mas_chamando with Dissolve(1.0)

                    mc concentrando "Obrigado."

                    gina "Acho que eu vou dormir agora. Você sabe como sair, né?"

                    mc charmoso "Sim. Já tô indo."

                    gina "Qualquer coisa, só me ligar."

                    mc safado "Tá."

                    scene mansao piscina with dissolve

                    play sound "audio/som_35_passos.mp3"

                    "..."

                    scene mansao porta with Dissolve(1.0)

                    "Uou... a [gina] conseguiu o que queria."

                    "E quem diria que massagear a traseira dela ia ser tão bom?"

                    "Agora tenho que voltar."

                    "Não acredito que eu não consegui nada pra [m]. A [gina] sempre foi uma pessoa tão razoável, mas ela parecia irredutível dessa vez."

                    "Preciso ir no salão e falar com a [m]."
                "Melhor não. Isso está indo longe demais.":


                    mc desculpa "Pensando bem, acho que isso é um pouco demais, [gina]."

                    jump karli_e9_negou
        "Acho melhor eu sair agora.":


            mc desculpa "Você entendeu tudo errado, [gina]. Acho melhor eu ir embora."

            label karli_e9_negou:

                gina "Tem certeza, lindo? Eu cuido muito bem do meu corpo. Eu tenho certeza que você vai se divertir bastante."

            mc "Me-melhor eu sair agora."

            gina "Ok. Tenha uma boa noite. Pode me ligar quando quiser."

            mc "A-a-até!"

            scene mansao piscina with dissolve

            play sound "audio/som_35_passos.mp3"

            "..."

            scene mansao porta with Dissolve(1.0)

            "Ufa! Ela realmente tava falando do que eu tava pensando!"

            "Tenho que voltar e falar com a [m]."

            "Não acredito que eu não consegui nada. A [gina] sempre foi uma pessoa tão razoável, mas ela parecia irredutível dessa vez."

            "Não adianta pensar nisso agora. Deixa eu voltar pro salão."

    label karli_e9_depois:

        scene black with dissolve

        "..."

        scene salao geral with Dissolve(1.0)

        mc desconfiado "[m]. Tá aí?"

        m "Tô indo, [mc]! Calma!"

        mc normal "Vou aí."

        m "Não! Tô na banheira! Já tô indo!"

        mc desconfiado "Ok..."

        "..."

        show karli satisfeita with dissolve

        m "Que foi? Saudades, já?"

        mc desconfiado "Você não tava atendendo uma cliente?"

        m "Sim. E daí?"

        mc envergonhado "Nada."

        if karli_gina:

            mc desculpa "Olha, eu sei que você falou pra eu não fazer, mas eu falei com a [gina]."

            show karli preocupada with hpunch

            m "Quê?!"

            mc "E o pior é que eu não consegui nada. Ela disse que vai te desalojar..."

            scene karli_puta with hpunch

            m "Você é idiota?! Eu falei pra você não ir!"

            mc desculpa "Malz... eu só queria ajudar."

            if karli_beijo:

                mc preocupado "Eu gosto de você, [m]! Eu quero que você fique!"

                m "Foda-se."

            m "O que ela mandou você fazer?"

            mc "Não interessa."

            m "Eu quero saber! Fala!"

            mc "Ela só queria que eu fizesse massagem nela. Só isso."

            if gina_massagem:

                mc "Foi assim que eu consegui aliviar sua barra das outras vezes."

            m "E você? O que você fez?!"

            mc "Bom... eu fiz até ela falar que não ia te ajudar."

            m "Aposto que não foi só massagem, né? Aquela velha filha da puta queria muito mais que massagem, não queria?!"

            mc envergonhado "Sim..."

            m "..."

            if gina_bunda:

                mc "Bom..."

                m "Não acredito! Você comeu ela, seu puto!"

                mc angustiado "Eu só queria te ajudar!"

                m "É assim que você gosta de mim, seu idiota?!"

                mc "Eu-"

                m "Eu nunca mais quero ver você na minha frente, [mc]! Você morreu pra mim!"

                m "Eu achei que você fosse um cara diferente. Mas você só quer meter esse pinto em qualquer lugar!"

                m "Sai daqui! AGORA!"

                mc angustiado "[m]!"

                m "SAI E NUNCA MAIS VEM AQUI!"

                scene black with hpunch

                "Estraguei tudo... que merda..."

                "Adeus, [m]..."

                jump call_cidade
            else:


                mc preocupado "Claro que eu não fiz nada, louca. Eu não quero nada com ela. Eu só queria te ajudar."

                m "É o mínimo, né, [mc]? Se você tivesse feito algo assim, eu nunca mais ia olhar na sua cara."

                mc desculpa "Eu sei... não fiz nada."

                scene salao geral with dissolve

                show karli meudeus with dissolve

                m "Eu vou acreditar em você. Mas se eu descobrir o contrário, você tá fodido comigo!"

                mc preocupado "Eu sei. Eu nunca faria isso."
        else:


            mc desculpa "Eu queria ajudar você de alguma forma, daí pensei em falar com a [gina] igual das outras vezes."

            m "Tá doido? Eu falei pra você não falar com aquela decrépita!"

            mc envergonhado "Eu sei... resolvi esquecer a ideia."

            m "Tá. Valeu por me respeitar, [mc]. Eu não quero mais nada com ela, nunca."

    mc preocupado "Mas e agora? Como você vai ficar?"

    m "Não sei. Não quero falar disso."

    hide karli with dissolve

    play sound "audio/som_35_passos.mp3"

    mc desconfiado "Ei!"

    scene salao massagem with Dissolve(1.0)

    mc serio "Para, [m]!"

    show karli meudeus with dissolve

    m "Me deixa, [mc]!"

    mc irritado "[m]!"

    m "?!"

    show karli preocupada with dissolve

    m "Q-que foi?"

    mc concentrando "Você só tá ignorando o problema."

    m "Eu sei..."

    "Que merda!"

    if karli_seducao >= 5:

        "Eu tenho certeza que rolou um lance entre eu e a [m] nas nossas aulas."

        "Certeza que ela sentiu isso também."

        if karli_beijo:

            "Ainda mais depois do nosso beijo."

            "Eu não quero perder ela pra sempre."

    mc desculpa "[m]..."

    mc preocupado "Eu não quero perder você pra sempre."

    m "[mc]... Eu também... também não quero... mas-"

    mc preocupado "Sem 'mas'. Me escuta."

    if karli_seducao >= 5:

        "É agora ou nunca. Se eu quero algo a mais com ela, precisa ser agora."

    menu:

        "Pedir a [m] em namoro" if karli_seducao >= 5:

            $ karli_declaracao = True

            "Eu sei o que eu quero. Eu quero que a [m] seja minha namorada. E por isso ela não pode se mudar."

            "Ela tá super vulnerável. Eu preciso falar isso pra ela e passar confiança."

            "Não posso ter medo de falar o que eu sinto. Preciso de coragem."

            mc concentrando "[m]..."

            mc desculpa "Eu tenho algo muito importante pra falar."

            m "Não, [mc]. Não-"

            mc charmoso "Eu quero você como minha namorada."

            m "E-eu?"

            mc "Sim. Eu senti uma química entre a gente e sei que você sentiu também."

            mc "Por favor. Fica comigo."

            m "[mc]... eu preciso sentar."

            mc desculpa "Cl-claro!"

            scene karli_conversando with Dissolve(1.0)

            pause

            m "Ai ai..."

            m "[mc]... eu tinha muito medo que você me falasse isso."

            mc "Medo?"

            mc "Vo-você não gosta de mim... é isso..."

            m "Não... não é isso."

            m "É que a gente não pode ficar juntos..."

            mc "Se o problema é o dinheiro a gente vai dar um jeito!"

            m "N-não é isso."

            mc "Então..."

            m "[mc]... eu sou lésbica."

            mc "C-como? Você é o quê?"

            m "Lésbica. Eu curto garotas. Eu não gosto de pipi."

            mc "[m]... Você tá fazendo uma piada de humor questionável?"

            m "Sim."

            mc "..."

            m "Brincadeira. Não tô, não. Eu realmente sou lésbica."

            mc "Não tô entendendo, [m]."

            m "Eu sei. A culpa é toda minha. Me perdoa."

            mc "Eu não sei o que falar agora..."

            scene karli_conversando2 with Dissolve(1.0)

            pause

            m "É que eu tava meio confusa..."

            mc "Como assim confusa?"

            m "Quando a gente se conheceu, você veio me provocando, como quase todos os babacas..."

            m "Mas eu senti uma coisa diferente com você. Não é bem uma atração, mas eu estava gostando das nossas brincadeiras."

            m "Daí a gente continuou e isso foi crescendo dentro de mim. Eu achei que talvez eu só nunca tivesse encontrado o cara certo."

            m "Talvez no fundo eu não fosse lésbica."

            m "Então eu dei corda e eu realmente tava gostando de tudo."

            m "Daí a gente foi na balada."

            if karli_beijo:

                m "E a gente se beijou lá."
            else:


                m "E eu tive uma noite muito legal com você."

            m "Mas daí eu percebi que eu realmente não sentia atração nenhuma por você."

            m "Você me protegeu, foi um verdadeiro cavalheiro. E ainda rolou uma química entre a gente."

            m "Você era o cara perfeito, [mc]! Se algum dia eu fosse ficar com um cara, com certeza seria você!"

            m "Mas eu realmente não senti nenhuma vontade de continuar depois daquilo."

            mc "[m]..."

            m "Eu nasci assim. Eu nasci gostando de garotas. Desde que eu me dei conta da minha vida, eu me sinto assim."

            m "Eu cresci em um lar comum, com pai, com mãe, héteros. E mesmo assim eu nunca consegui sentir atração por garotos."

            m "Acho que a gente só nasce assim, sabe."

            scene karli_conversando with Dissolve(1.0)

            m "Você me perdoa? Desculpa por enganar você. Mas eu realmente não queria. Eu achei que talvez..."

            m "..."

            mc "[m]... não precisa pedir desculpas."

            mc "Não posso negar que a sensação é de que você acabou de pisar nas minhas bolas."

            mc "Mas eu entendo. Se você não sente vontade de namorar comigo, não adianta."

            mc "Você sente atração por garotas e eu sou um garoto. Não tem muito o que discutir, certo?"

            m "A-acho que sim..."

            mc "Vem aqui."

            m "Opa!"

            scene karli_abraco with Dissolve(2.0)

            pause

            mc "Tá tudo bem. Eu te desculpo, mesmo não tendo nada pra desculpar."

            m "[mc]..."

            m "Se você tivesse nascido com uns peitões caprichados e menos pelo eu te atacava na banheira..."

            mc "É. Isso eu vou ficar devendo."

            m "De verdade... você é o cara mais incrível eu já vi."

            m "Ainda não entra na minha cabeça que tem um cara como você andando nesse mundo."

            mc "Fale mais."

            m "Idiota..."

            mc "Agora chega antes que EU te ataque na banheira."

            m "Perigo. Agora você me deixou com medo."
        "Falar que ela é sua grande amiga":


            "A [m] é minha amiga e eu quero que ela realize o sonho dela."

            "Não tem a ver com querer ficar com ela ou não."

            mc "Vem aqui. Senta comigo."

            m "T-tá."

            scene karli_conversando with Dissolve(1.0)

            pause

            mc "Eu comecei a fazer o curso com você nem sei porque."

            mc "Eu percebi que eu podia provocar reações nas garotas e era de graça, né? Então..."

            mc "Mas com o tempo, minha motivação foi mudando. Eu comecei a me afeiçoar por você."

            m "Agora a gente fala palavras bonitas, tipo 'afeiçoar'."

            mc "Para de brincadeira e escuta."

            m "S-sim, senhor."

            mc "Me deixa muito triste saber que você vai embora. E eu nem sei por que você não vai nem lutar."

            mc "Das outras vezes a gente conseguiu resolver. Por que você só vai desistir?"

            m "AAAHHH!"

            mc "!!"

            scene karli_conversando2 with Dissolve(1.0)

            pause

            m "[mc]..."

            m "Você vai me fazer contar tudo, né? Mesmo não querendo."

            mc "Pode começar a falar."

            m "Ai ai... Nem sei por onde começar."

            mc "Por que você não começa pela coisa mais bombástica? Assim a gente já resolve isso."

            m "Caralho... tu é foda, [mc]."

            mc "Fala logo."

            m "L-lésbica."

            mc "Como é?"

            m "Eu sou lésbica. Eu curto garotas. Eu não gosto de pipi."

            mc "[m]... Você tá fazendo uma piada de humor questionável?"

            m "Sim."

            mc "..."

            m "Brincadeira. Não tô, não. Eu realmente sou lésbica."

            mc "Sério?!"

            m "Eu nasci assim. Eu nasci gostando de garotas. Desde que eu comecei a sentir atração por alguém, já era por garotas."

            m "Eu cresci em um lar comum, com pai, com mãe, héteros. E mesmo assim eu nunca consegui sentir atração por garotos."

            m "Acho que a gente só nasce assim, sabe."

            m "Mesmo com todas as dificuldades. Minhas amigas não me entendiam. Minha mãe menos ainda."

            m "Todas as vezes que eu tentei contar pra alguém quando era adolescente, todos só deram risada ou nem quiseram falar comigo."

            m "Teve gente que falou coisas horríveis, tipo 'isso é falta de pinto'. Não foi fácil."

            mc "[m]... eu nunca falaria algo assim pra você."

            m "Não?"

            mc "Claro que não. Grande coisa se é homem ou mulher. O que importa é o sentimento, não o corpo."

            m "[mc]... mesmo depois de tudo isso. Você tem coragem de me abraçar?"

            mc "Vem aqui."

            m "Ei!"

            scene karli_abraco with Dissolve(2.0)

            pause

            mc "Tá tudo bem. Eu entendo. Não vou ficar contra você."

            m "[mc]..."

            m "De verdade... você é o cara mais incrível eu já vi."

            m "Ainda não entra na minha cabeça que tem um cara como você andando nesse mundo."

            mc "Fale mais."

            m "Idiota..."

            mc "Eu sei que tem gente que não entende essas coisas. Mas a gente não pode ter ódio delas também."

            mc "Só não é o tempo delas ainda. O que importa é o que a gente faz da nossa vida."

            mc "E eu vou estar com você, porque eu gosto de você. Se você gosta de homem ou de mulher, não muda quem você é."

            m "Obrigada..."

    scene karli_conversando2 with Dissolve(1.0)

    m "Sabe... eu nunca me dei bem com a minha mãe por causa disso."

    m "Ela nunca entendeu minha escolha. Sempre falou que eu que escolhi ser assim."

    mc "Ela não sabe de nada."

    m "Mas eu nunca vou querer nada dela. Por isso que eu vou arranjar a grana pra pagar ela pelo salão. Ou só vou embora mesmo."

    mc "Como é? Pagar pra sua mãe?"

    m "É, tontão. A [gina] é minha mãe."

    mc "!!!"

    mc "Sabia que eu desconfiava?"

    m "Claro..."

    mc "Como assim sua mãe?!"

    m "Pois é..."

    scene karli_conversando with Dissolve(1.0)

    m "Ela nunca me aceitou. Daí eu saí de casa, mudei pra ilha e aluguei o salão."

    m "Quando ela descobriu, ela comprou o prédio, acredita?"

    mc "..."

    m "Então... coisas que pessoas com dinheiro infinito podem fazer."

    m "Por algum motivo ela achou que a gente tava juntos. Acho que porque você tentou me ajudar."

    m "Meio que a gente se aproximou. Mas eu não saquei que era por sua causa."

    mc "Entendi... então ela queria falar comigo..."

    mc "Mas então por que ela-"

    m "Ela é doente, [mc]! Aposto que ela não ia transar com você, mas certeza que ela tava te provocando."

    m "Provavelmente pra ver se você era hétero e confiável, sei lá. Essa velha é louca."

    mc "Isso é loucura mesmo..."

    scene karli_conversando2 with Dissolve(1.0)

    m "Daí depois da balada eu voltei com a minha namorada."

    mc "Ela era a 'cliente' de hoje, né?"

    m "Sim..."

    mc "Podia ter falado..."

    m "Eu tava pensando em desaparecer e nunca ter que te contar nada."

    mc "Corajosa você, hein?"

    m "Você pode me abraçar de novo?"

    mc "C-claro."

    scene karli_abraco with Dissolve(1.0)

    m "Seu abraço é muito gostoso."

    mc "Que bom."

    m "Eu não quero mais desistir daqui, [mc]. O que eu faço?"

    mc "Agora não tem mais jeito. Vai ter que morar embaixo da ponte."

    m "Ei..."

    mc "Tô brincando. A gente vai pensar em alguma coisa."

    m "Verdade? Você vai me ajudar?"

    mc "Claro, né?"

    if karli_declaracao:

        m "Mesmo sabendo que não vai conseguir nada comigo?"

        mc "Ah! verdade... esquece, então."

        m "Como é tonto..."

        mc "Ei!"

    m "Acho que eu fui alguém muito legal na última encarnação pra merecer um amigo igual você."

    mc "Você não acha que vai ficar de graça, né?"

    m "Não? Não tenho dinheiro nem pra cair morta... literalmente..."

    mc "E a minha aula?"

    m "Ah. Eu achei que você queria aulas só pra pegar em mim."

    mc "Mais ou menos... mas agora que já comecei, não vou desistir, né?"

    m "Perfeito!"

    scene black with Dissolve(1.0)

    m "Hoje vai ser uma aula SÉRIA!"

    "{i}treck trock{/i}"

    m "Suas costas fazem um barulho estranho."

    mc "AAAAAHHHHHHHHH!"



















    label karli_e9_fim:

        pass

    if not gina_bunda:

        python:
            if renpy.android:
                
                PythonSDLActivity.registraEvento("massagem_aula_9","massagem","aula")
                
                if mc_massagem == 8:
                    
                    if mc_massagem == mc_massagem_db:
                        mc_massagem_db = PythonSDLActivity.maisMpontos()
                    
                    mc_massagem += 1

        $ tempo += 1
        $ dia_karli = dia + 1

        $ renpy.block_rollback()

        play sound "extra/carta.mp3"

        "{b}[mc] melhorou sua técnica em massagem{/b}"

    jump call_cidade

label karli_aula10:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("m1_save", extra_info="m1_save")

    m "E aí? Pensou em alguma coisa?"

    mc envergonhado "Pior que não... Eu queria muito te ajudar com alguma ideia monstra, mas não veio nada."

    m "Relaxa, [mc]. Eu entrei em contato com a energia cósmica da mãe terra e descobri os segredos da vida."

    mc "A é? E o que você descobriu?"

    m "Uma forma de você me salvar."

    mc desconfiado "Como é?"

    m "Isso mesmo, meu herói!"

    if karli_declaracao:

        m "Depois de se declarar pra mim e cair de cara no chão, você ainda vai salvar meu salão!"
    else:


        m "Você vai salvar meu salão, [mc]! Você é o melhor amigo do mundo!"

    mc zerado "..."

    m "Que foi?"

    mc "Tô meio desconfiado..."

    m "Eu garanto pra você que vai doer mais em mim do que em você..."

    mc zerado "..."

    m "Calma, rapazinho! O que aconteceu com você que seu coração virou essa caverna fria e sem paixão?"

    mc "..."

    mc "Tô esperando você contar a ideia."

    m "Não vou contar, não."

    mc "Como é?"

    m "Eu quero que você venha aqui amanhã à tarde. E venha preparado, porque não vai ser fácil pro seu coraçãozinho gelado."

    menu:
        "Ok. Amanhã à tarde?":


            "..."
        "E se eu não quiser vir?":


            mc desconfiado "E se eu não quiser?"

            m "Venha sem querer. Não me importa."

            mc zerado "Que audácia..."

    m "Você tem [mc_massagem] pontos no jogo e [mc_massagem_db] pontos salvos online antes de computar."

    python:
        if renpy.android:
            
            PythonSDLActivity.registraEvento("massagem_aula_10","massagem","aula")
            
            if mc_massagem == 9:
                
                if mc_massagem == mc_massagem_db:
                    mc_massagem_db = PythonSDLActivity.maisMpontos()
                
                mc_massagem += 1

    $ tempo += 1
    $ dia_karli = dia + 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    "{b}[mc] masterizou a arte da massagem! Agora ele pode fazer massagens perfeitas!{/b}"

    jump call_cidade

label karli_1vez:

    $ m_nome = "Atendente"

    mc normal "Tem alguém aí?"

    "..."

    show karli feliz with dissolve

    m "Oi."

    m "Como posso ajudar?"

    mc surpreso "Você!"

    mc "Você é a garota que eu vi no parque!"

    m "Hmmm..."

    mc normal "Você tava no Tadaima também. Seu nome era..."

    menu:
        "Marli.":


            mc charmoso "Marli!"

            m "Quase lá."

            m "Mas Marli é o nome do cachorro do filme lá."

            mc zerado "Esse é o Marley..."
        "Karli.":


            mc charmoso "Karli!"

            m "Não."

            mc zerado "Droga..."

            "Eu tinha quase certeza que era Karli..."
        "Kinsley.":


            mc charmoso "Kinsley!"

            m "Exatamente!"

            mc "Eu sabia..."
        "Mindi.":


            mc charmoso "Mindi!"

            m "Você gosta de jazz também?"

            mc desconfiado "Quê?"
        "Kairi.":


            mc charmoso "Kairi!"

            m "Essa aí é de outro jogo..."

            "De qual jogo ela tá falando será?"
        "... Garota do cabelo roxo?":


            mc envergonhado "Garota do cabelo roxo?"

            m "E você é o garoto do cabelo preto? Uga uga..."

            mc "..."

    $ m_nome = "Karli"

    m "Enfim, meu nome não importa. O que você está fazendo aqui?"

    mc desconfiado "E se eu sou um cliente e quero comprar alguma coisa? Você trata assim seus clientes?"

    m "Você ainda não é um cliente."

    mc "Desse jeito eu nunca vou ser."

    m "Tá vendo? Por isso que tô tratando você assim."

    mc "Mas..."

    m "..."

    mc zerado "Tudo bem... Eu desisto."

    mc normal "Eu ganhei de presente de uma amiga este curso de massagem gratuito. Eu tava afim de fazer."

    m "Deixa eu ver se isso é realmente oficial."

    mc serio "Claro que é. Ela nunca faria algo errado desse jeito."

    show karli normal with dissolve

    m "Esse é o vale que eu dei pra [c], não é?"

    mc normal "Isso mesmo!"

    m "E você é amigo dela?"

    mc "Sim. A gente conversou algumas vezes."

    m "Hmmm..."

    m "Por que ela perderia tempo com um cara como você?"

    mc desconfiado "Você tá falando sério? O que tem de errado comigo?"

    m "Sei lá. Ela é linda, rica, famosa. E você é, sei lá, só um carinha... qualquer..."

    menu:
        "Não importa. Só quero fazer o curso.":


            mc serio "Não me importa sua opinião sobre nossa relação. Só quero fazer o curso que este cupom me dá direito."

            m "Ok, ok. Parei. Só tô tentando quebrar o gelo."

            mc desconfiado "É assim que você tenta quebrar o gelo conversando com alguém? Chamando de qualquer?"

            m "Essa história de politicamente correto tá com nada."

            mc zerado "Acho que isso não tem nada a ver com o que tá acontecendo aqui."
        "Eu não sou um qualquer. Sou um jornalista.":


            mc normal "Se eu fosse um qualquer ela não daria bola pra mim mesmo. Eu sou um jornalista."

            mc charmoso "Minhas matérias podem mudar a vida de muita gente. Pode ser uma coisa boa ou uma coisa {b}terrível{/b}."

            m "Tá certo. Não precisa me ameaçar. Eu entendi."

            m "Só tava querendo fazer amizade."

            mc normal "Seu jeito de fazer amizade é terrível."
        "Qualquer é você tentando se fazer de rebelde.":


            mc charmoso "E você tentando se fazer de rebelde com esse cabelo roxo e tatuagenzinha?"

            mc tarado "Não passa de uma classe média que deve ter sido rejeitada pelo pai."

            m "Calma lá! Aí pegou pesado, rapaz."

            mc serio "Você que tá pegando pesado. Nem me conhece e vem me chamar de qualquer."

            m "Tá bom. Você venceu. Não precisa apelar. Só queria iniciar a conversa."

            mc zerado "Belo jeito de conhecer alguém..."

    m "Bom, seu vale parece tudo certo. Acho que eu vou deixar você fazer o curso."

    mc desconfiado "Como assim deixar? Se eu tenho o vale você tem que ministrar o curso, pô!"

    m "Eu não tenho que fazer nada. Esse cupom é só a primeira etapa. Existem outras etapas."

    mc zerado "... Como é?"

    show karli satisfeita with dissolve

    m "O que eu faço aqui não é algo comum, amigo. Aqui se pratica uma arte milenar de terras inexploradas."

    mc normal "Com certeza..."

    m "Tá duvidando?!"

    mc "Claro."

    m "Estou começando a repensar se eu devo realmente te aceitar como meu discípulo..."

    mc envergonhado "Tá bom, tá bom! Técnicas milenares e desconhecidas, saquei."

    m "Que bom que você entendeu a importância do que acontece aqui."

    m "Então. Aqui eu ensino como levar uma pessoa para o nirvana apenas com o leve toque dos seus dedos."

    mc normal "..."

    m "Você sabe como Buda levou uma vida inteira para atingir o nirvana. Aqui a gente só precisa de alguns minutos."

    menu:
        "Incrível!":


            mc surpreso "Impressionante!"

            show karli normal with dissolve

            m "Você tá sendo irônico?"

            mc envergonhado "Claro que não."

            m "Ok... Não tente se fazer de esperto comigo."

            mc "Claro que não."
        "Obviamente...":


            mc zerado "Com certeza..."

            show karli normal with dissolve

            m "Não duvide de mim, paspalho!"

            mc envergonhado "Tá bom! Calma!"

            m "Acho bom mesmo."
        "...":


            mc normal "..."

            show karli normal with dissolve

            m "Que foi?"

            mc "Nada. Só tô ouvindo."

            m "Hmm."

    mc normal "Você quer dizer que sua massagem é tão boa que a pessoa chega no nirvana só com ela."

    m "Traduzindo no linguajar mundano dos povos subdesenvolvidos, é mais ou menos isso."

    mc "Ok."

    m "Mas eu não vou ficar só de blá blá aqui. Eu vou te mostrar na prática."

    mc surpreso "Uou! Agora sim!"

    m "E não vai ser só uma vez. Se você for aprovado como meu discípulo, você vai poder chegar ao nirvana várias vezes pelas minhas mãos."

    menu:
        "Se é o que eu tenho que fazer pra aprender.":


            mc normal "Eu estou pronto se for necessário pra eu aprender a técnica."

            m "Eu vou te mostrar como fazer e você irá aprender por meio de teoria e prática."
        "Sua técnica parece incrível.":


            mc surpreso "Tudo isso parece incrível!"

            m "Tá sendo irônico de novo?"

            mc normal "Não. Tô falando sério dessa vez."
        "Estou louco pra que você me leve ao nirvana.":


            $ karli_seducao += 1

            mc safado "Estou louco pra que você me leve pro nirvana."

            show karli provocando with dissolve

            m "Minha técnica pode levar ao desejo sexual também, com certeza. Depende dos seus objetivos."

            mc "Bom saber..."

    show karli normal with dissolve

    m "Certo. Acho que te passei toda a explicação inicial. E normalmente eu ensino só garotas..."

    m "Mas você não me parece tão ruim, mesmo sendo só normalzinho."

    mc zerado "De novo isso..."

    m "Ah! Eu tenho uma última pergunta antes que você vire meu discípulo."

    mc desconfiado "O quê?"

    show karli feliz with dissolve

    m "Uma massagem profissional, minha incrível arte, serve pra várias coisas."

    m "Bem-estar, redução do estress, relaxamento, melhora na circulação do sangue, alívio de dores e até ajuda a dormir."

    m "E você também pode usar pra safadezas quando tiver com alguém na cama ou na banheira."

    m "Então minha última pergunta é saber qual seu objetivo aprendendo a incrível arte da massagem."

    mc desculpa "Hmm... Meu objetivo?"

    menu:
        "Quem sabe pode virar minha nova profissão.":


            mc desculpa "Eu tava pensando que poderia virar algo profissional se eu ficasse bom de verdade nisso."

            m "Eu acho que é bem possível. E eu não teria nenhum medo de ter você como rival. Olha pra gente!"

            mc zerado "Não precisa esculachar..."

            m "Hehe... Tô zuando."
        "Eu quero deixar as pessoas com tesão.":


            $ karli_seducao += 1

            mc tarado "Eu quero deixar as pessoas loucas de tesão."

            show karli provocando with dissolve

            m "A massagem também pode servir pra isso."

            mc safado "Era isso que eu queria."

            m "Ok, pode deixar que vou levar isso em consideração nas aulas."
        "Eu quero que meus amigos se sintam bem.":


            mc normal "Acho que o bem-estar e o alívio é o principal. Quero que meus amigos fiquem de boa."

            m "Muito bom! É um excelente objetivo."

            mc "Obrigado."

    m "Sabendo disso, acho que podemos ir pra próxima fase. Vamos pra mesa e agora deixe que minhas mãos vão falar no meu lugar."

    if karli_seducao >= 2:

        mc safado "Finalmente essa gostosa vai pegar em mim..."
    else:


        mc normal "Legal! Bora lá!"

    $ cenario_salao_1vez = False

    hide karli with dissolve

    m "Vem aqui comigo."

    "..."

    jump karli_evento1



label karli_evento1:

    $ tempo += 1

    scene salao massagem with Dissolve(2.0)

    m "Aqui é onde a magia acontece. Vai se acostumando."

    mc normal "O lugar é bem bacana. Parabéns."

    show karli feliz with dissolve

    m "Valeu. Agora eu quero que você tire suas roupas e fique só de cueca."

    mc surpreso "Quê?!"

    show karli normal with dissolve

    m "Como eu vou aplicar uma massagem com você de roupa?"

    mc "..."

    menu:
        "Só se você tirar sua roupa também.":


            $ karli_seducao += 1

            mc tarado "Eu tiro. Mas só se você tirar também."

            show karli provocando with dissolve

            m "Hmm..."

            m "Só porque você quer."

            mc safado "Combinado."

            "..."

            m "Vai se aprontando então que já venho."

            "..."

            mc zerado "Você tá me zuando, né?"

            show karli normal with dissolve

            m "Claro."

            mc "..."
        "Isso é realmente necessário?":


            mc normal "Eu realmente preciso?"

            m "Já te falei. Como vou fazer com você..."

            mc desculpa "Ok ok... Entendi. Vou tirar."

            m "Você vai entender melhor o processo no decorrer do curso."
        "Já tirei.":


            mc normal "Pronto."

            m "Nossa, você é rápido."

    show karli normal with dissolve

    m "Agora é só vir até a mesa e se deitar."

    mc normal "Ok."

    show karli feliz with dissolve

    m "Na aula de hoje só eu que vou massagear. Você vai ficar quieto e sentir o poder de uma arte milenar."

    m "A partir da próxima aula eu vou te ensinar como fazer e você vai começar a praticar em mim."

    if karli_seducao >= 2:

        show karli provocando with dissolve

        m "Eu sei que você tá louco pra poder pegar em mim."

        mc safado "Com certeza."

        m "Vamos ver se você vai merecer."

        mc "Eu vou me comportar direitinho, professora."

        m "Falando assim você ganha pontos."

    m "Então se ajeite e me fale quando você estiver pronto."

    hide karli with dissolve

    "..."

    scene massagem e1 with Dissolve(1.0)

    pause

    mc "Ok. Estou pronto."

    m "Tá confortável?"

    mc "Mais impossível."

    m "Perfeito. Respire fundo e tente ficar calmo. Não que uma pessoa falar isso ajude, né?"

    mc "Pois é."

    m "Não se preocupe e deixe tudo nas minhas mãos. Literalmente."

    mc "..."

    "Tá dando um pouco de nervoso..."

    "Opa! Ela começou..."

    "..."

    "Hmm..."

    "Ela tem muita firmeza nas mãos. É difícil imaginar que uma garota magrinha assim ia ter tanta força."

    "Com certeza a [m] sabe o que tá fazendo. {i}Hmm...{/i} Ela aperta nos lugares certos."

    "..."

    menu:
        "Sua arte é incrível mesmo...":


            mc "Tenho que admitir. Sua arte é incrível mesmo..."

            m "Valeu. Mas agora calado."

            mc "Ok..."
        "...":


            mc "Hmm..."

            m "Tô vendo que você tá aproveitando."

            m "Isso mesmo. Só fique quieto e aproveite a magia."

            mc "Certo."

    "..."

    "Eu tô tão relaxado. Mas não quero dormir. Quero aproveitar ao máximo."

    "Não seja idiota, [mc]! Mantenha os olhos... abertos!"

    "Não sei... se vou conseguir... {size=15}ficar acordado...{/size}"

    scene black with Dissolve(2.0)

    "{b}30 minutos depois{/b}"

    scene salao massagem with Dissolve(1.0)

    m "Acordou?"

    mc "Hmm... Eu dormi?"

    m "O que você acha?"

    mc envergonhado "Desculpa. Isso é falta de respeito com o massagista?"

    show karli normal with dissolve

    m "Hahaha. Claro que não, doido. Isso acontece em boa parte das sessões. É um dos meus poderes, não lembra?"

    mc "É verdade."

    m "Bom. É isso. Nesta primeira aula eu só queria que você sentisse na pele como uma massagem funciona."

    m "A partir do nosso próximo encontro você vai começar a aprender a técnica."

    mc normal "Estou muito empolgado. Serão quantas aulas?"

    m "Depende do quão rápido você vai aprender. Mas em média o curso dura 10 aulas."

    mc "A gente vai se ver uma vez por semana?"

    m "Depende de você na verdade. Eu estou aqui todo dia. Eu só não posso de manhã, porque, você sabe, eu trabalho no Tadaima."

    mc "Verdade. Então posso vir aqui uma vez por dia? No {b}período da tarde ou da noite{/b}?"

    m "Isso aí."

    mc "Combinado."

    m "Eu espero você então. Até."

    mc "Até."

    scene mapa cidade_noite with Dissolve(1.0)

    "Uou. Essa aula foi melhor do que eu imaginava. Eu estou me sentindo muito bem. Massagem realmente ajuda, não é brincadeira."

    if karli_seducao >= 2:

        "Eu senti que rolou um clima mais quente em alguns momentos. Ela não fugiu das minhas investidas."

        mc safado "Será que essas aulas podem virar algo mais?"

    "Eu tenho que voltar amanhã então a partir da tarde pra continuar minhas aulas."

    "Saber fazer massagem pode ser algo muito útil pra eu usar nas celebridades também. Quem não gosta de massagem?"

    "Mas por hoje tá bom disso. Bora lá."

    python:
        if renpy.android:
            
            mastempo = PythonSDLActivity.setMtempo()
            mastemponext = PythonSDLActivity.getMtempoNext()
            mc_massagem_db = PythonSDLActivity.pegaMpontos()
            
            if mastempo >= mastemponext:
                if mc_massagem >= mc_massagem_db:
                    PythonSDLActivity.setMtempoNext()
            
            PythonSDLActivity.registraEvento("massagem_introducao","massagem","aula")

    $ dia_karli = dia + 1

    scene black with Dissolve(1.0)

    p rindo "Oi!"

    p "..."

    p lecionando "Ei! Não faça essa cara só porque eu tô atrapalhando a continuação do jogo."

    p "Eu vim aqui explicar algo muito importante."

    p "Suas aulas de massagem só podem ser feitas uma vez por dia aqui no jogo. Mas o seu tempo real também conta."

    p "Você só pode continuar o curso {b}8 horas{/b} depois da aula anterior."

    p "Mesmo que você avance 10 dias no jogo, enquanto essas 8 horas não passarem, não adianta."

    p "Você só precisará fazer isso uma vez por aula. Ou seja, se você recomeçar o jogo, não vai ser preciso esperar de novo as que você já esperou."

    p rindo "É possível pular esse tempo usando {b}Celebrity Coins{/b}. Você pode ganhar essas moedas na {b}Loja de Cartas{/b} vendo vídeos."

    p lecionando "Se você não tiver paciência para isso, você pode conseguir moedas na nossa {b}Loja{/b}. É só acessar o {b}MENU{/b}."

    p "Se você tiver mais dúvidas, venha conversar comigo quando dormir. Eu posso te explicar melhor lá."

    p rindo "Bom jogo!"

    jump call_cidade

label karli_evento_auto0:

    "Acho que dei um tempo suficiente pra [m] se acomodar."

    "..."

    scene ap sala with Dissolve(1.0)

    mc normal "[m]? Voltei."

    m "Oi, [mc]. Tô sentada aqui."

    mc surpreso "!"

    scene ap_karli sofa with vpunch

    pause

    m "Oi."

    mc surpreso "Ka-Karli?!"

    m "Que foi?"

    "Essa mina só pode tá brincando comigo."

    mc envergonhado "Su-sua roupa..."

    m "Ah. Não tem problema, tem? Tipo, se eu vou ficar uma semana aqui, quero ficar à vontade."

    "Isso não é à vontade demais?"

    mc "Acho que eu estou sendo bobo, sei lá."

    m "Relaxa, [mc]. Você só tá sendo um cavalheiro. Valeu."

    mc "Ok..."

    m "A gente é parceiro, né? E tipo, tu não vai me atacar."

    mc "Claro que não."

    if karli_seducao >= 5:

        menu:
            "Mas vou querer dar uma olhada...":


                mc tarado "Mas, assim, sem querer parecer um tarado, mas não sei se vou aguentar não dá uma olhadinha..."

                m "Tô ligada. Você gosta de mulher, né? Tô de boa com isso."

                mc safado "Tamo combinados."
            "Então por mim beleza.":


                m "Isso que importa."

                mc normal "Por mim beleza então."

    m "Então tá tudo certo. Ah! E você também, quero ver você de boa. Não é pra usar roupa só por minha causa."

    mc normal "Pode deixar."

    if karli_seducao >= 5:

        m "Talvez eu dê uma olhadinha de vez em quando..."

        mc safado "Pode olhar..."

        m "Mesmo que você não deixasse eu ia olhar mesmo."

        "Essa mina sabe como mexer comigo."

    scene ap sala with Dissolve(1.0)

    mc normal "Ah. Outra coisa. Você pode dormir no meu quarto, eu fico aqui na sala."

    show karli p_feliz with dissolve

    m "De jeito nenhum. A casa é sua. Você fica no quarto e eu me ajeito aqui no sofá."

    mc preocupado "Mas você é uma dama. Não posso fazer isso com você."

    m "Dama é o caralho. Eu vou ficar aqui."

    mc envergonhado "Haha. Se você quer assim."

    m "Valeu, [mc]. Tu é um cara bacana."

    mc normal "E você é engraçada."

    m "Se tirar sarro de mim vou te dar uma voadora."

    mc "Ok..."

    return

label karli_evento_auto1:

    scene ap sala with Dissolve(1.0)

    mc normal "[m]. Eu tava-"

    mc desconfiado "[m]?"

    "Acho que ela foi resolver as coisas dela."

    "Tô pensando em tirar um cochilo."

    scene ap quarto with Dissolve(1.0)

    mc concentrando "Sinto que não tô dormindo direito ultima-"

    mc surpreso "AH!"

    scene ap_karli cama with vpunch

    mc envergonhado "..."

    "O que ela tá fazendo dormindo aqui?"

    "Será que eu chamo ela?"

    m "Hmmm...."

    "Opa, ela tá acordando."

    m "Oi, [mc]..."

    m "Sua cama é tão gostosa..."

    mc desconfiado "Quem deixou a senhorita dormir aí?"

    m "Mas é tão bom... não quero nem abrir os olhos..."

    m "Só mais 5 minutinhos..."

    mc normal "Ok. Vou tirar um soneca na sala enquanto isso."

    m "Valeu, pai."

    mc zerado "..."

    "Folgada..."

    if karli_seducao >= 5:

        "Mas como essa [m] é linda. E olha esse corpo."

        "Se eu pudesse, eu atacava ela aqui mesmo."

        "Como ela tem coragem de ficar assim na minha frente? Toda desprotegida."

        "Se controle, [mc]... você não é um animal. Se controle."

        m "Tudo bem aí, [mc]? Você tá olhando pra mim faz um tempo..."

        mc envergonhado "Ah.. não é nada."

        m "Tudo bem. Como você deixou eu dormir aqui, pode olhar à vontade."

        mc safado "..."

        window hide

        pause

        "Bom, deixa eu ir antes que eu fique parecendo um esquisitão."

    scene ap sala with Dissolve(1.0)

    mc concentrando "Bom... o jeito vai ser tirar um cochilo aqui mesmo."

    scene ap mc_dormindo3 with Dissolve(1.0)

    pause

    return

label karli_evento_auto2:

    scene ap sala with Dissolve(1.0)

    mc concentrando "Canseira..."

    "{i}hm-hm-hmmm{/i}"

    mc desconfiado "Que cantoria é essa?"

    "Será que é a [m]? Isso não faz a cara dela."

    "Tá vindo do quarto eu acho."

    "..."

    scene ap quarto with Dissolve(1.0)

    "Ué. Será que no banheiro? Mas..."

    "{i}hm-hm-hmmm{/i}"

    "[m]?"

    mc surpreso "!"

    scene ap_karli banheira with Dissolve(2.0)

    pause

    m "[mc]?"

    mc envergonhado "O-oi..."

    m "Tô curtindo a banheira aqui, tudo bem?"

    mc "T-t-tá."

    m "Que foi? Tudo isso por que tô peladinha aqui na banheira?"

    mc "Eu vou deixar você-"

    m "Para com isso, [mc]. Agora a gente tá morando juntos. Pode ficar à vontade."

    m "Se precisar dar uma mijada, fique à vontade."

    mc "Relaxa. Tô de boa."

    m "Eu tinha um dos meus sabonetes especiais que eu vendo no salão e usei aqui. Beleza, né?"

    mc "Claro."

    m "Vou deixar o que sobrou pra você aqui. É uma delícia."

    mc "Beleza. Pode curtir aí à vontade."

    m "Tá legal. Vou deixar a porta aberta. Você pode entrar quando quiser."

    mc "Beleza."

    "Essa mina é louca."

    return

label karli_evento_auto3:

    scene ap sala with Dissolve(1.0)

    mc concentrando "Maluco... que canseira..."

    mc "Preciso de um banho."

    scene ap quarto with Dissolve(1.0)

    "..."

    scene ap_karli banheira with vpunch

    pause

    mc surpreso "Ka-Karli?!"

    m "Fala aí. De novo gritando?"

    mc envergonhado "Ainda não tô de boa com isso."

    m "Tá tudo de boa."

    mc "Bom... se tá tudo de boa, posso tomar um banho com você aí? Tô precisando de verdade."

    m "Claro. Por mim tudo de boa."

    mc "Então de boa."

    "Será que eu tenho coragem de tomar um banho com ela me olhando assim?"

    menu:
        "Se ela nem liga, bora tomar banho.":


            "Foda-se. Ela nem liga."

            play sound "audio/som_16_chuveiro.mp3"

            scene ap mc_chuveiro with Dissolve(2.0)

            pause

            if karli_seducao >= 5:

                "É incrível como nossa intimidade tá aumentando esses dias."

                "Eu tô xavecando ela desde o começo e agora com a gente morando juntos assim."

                "Segunda vez que ela me deixa ver ela na banheira. E agora ela tá me vendo pelado também."

                "Isso vai progredir mais rápido do que eu imaginava."
            else:


                "Só de pensar que tô tomando banho com a [m] logo aqui atrás podendo me ver."

                "Que coisa doida."

            m "[mc]. Terminei. Tô saindo, tá?"

            mc "Ok."

            if karli_seducao >= 5:

                m "Até que seu corpo não é ruim, não, viu?"

                mc "Ei!"

                m "Só tô dando uma olhadinha. Você viu o meu também."

                mc "Culpado..."

            "..."

            "Pronto. Deixa eu sair e me troc-"

            scene ap_karli cama with vpunch

            pause

            m "Tô aqui..."

            mc "[m], eu preciso me trocar."

            m "Pode se trocar. Tô de olho fechado."

            "Falar o que pra essa mina?"

            scene black with dissolve

            if karli_seducao >= 5:

                m "Só quero ver o tamanho..."

                mc "Ei!"
        "Melhor não. Deixa quieto.":


            "Melhor não causar com ela. Vai que fica um clima chatão depois."

    return

label karli_evento_falar1:

    scene ap_karli mc_conversando1 with Dissolve(2.0)

    pause

    mc "A gente nunca teve tempo de trocar uma ideia durante as aulas."

    m "Iii... já tô vendo onde isso vai acabar. Essa história de trocar ideia, a gente quase pelado..."

    if karli_seducao >= 5:

        mc "Seria uma excelente ideia..."

        m "Quem sabe..."

    mc "Mas não é nada disso. Quero saber de você mesmo."

    m "Ah, mano. Sei lá o que tem de interessante sobre mim. Sou só uma mina normal."

    mc "Tá. Como é seu nome completo?"

    m "Haha! Sério mesmo, [mc]?"

    mc "Quê?! Tô falando sério."

    m "Não interessa meu nome."

    mc "Tá. Quantos anos tu tem?"

    m "Tenho 23. E você?"

    mc "Meu nome completo é [mcc]."

    mc "E não interessa minha idade."

    m "Justo..."

    mc "E sua família?"

    m "Bah! Falar de família? Eu tenho uma mãe que me enche o saco o tempo todo e meu pai é falecido."

    mc "Malz."

    m "Relaxa. Eu não ligo muito pra isso. Inclusive eu acho que minha mãe que matou ele."

    mc "Cala a boca! Que isso?"

    m "Tô te falando, [mc]. Aquela mulher não presta. Ela é o demônio."

    mc "Vocês não se dão bem?"

    m "A gente não se dá, ponto. Não quero nada com ela. E ela nem se importa muito comigo também."

    mc "Por isso que ela não pode te ajudar nesse lance?"

    m "Pra falar a verdade ela quer me ajudar, sou eu que não quero."

    mc "Mas-"

    m "Esse papo de mãe me deixou irritada. Chega de papo por hoje."

    mc "Mas eu nem-"

    m "Calado!"

    mc "Ok..."

    scene ap sala with dissolve

    "..."

    m "[mc]."

    mc desconfiado "Hm?"

    show karli p_explicando with dissolve

    m "Eu nunca fui de conversar muito. Desculpa se eu não tenho jeito pra trocar ideia."

    mc normal "Relaxa."

    m "Lá em casa a gente nunca foi muito de conversar. Eu... não tenho esse costume."

    m "Só que... valeu por ser de boa comigo."

    mc charmoso "Não esquenta. Vai no seu tempo."

    show karli p_feliz with dissolve

    m "Agora já tá se achando."

    mc "..."

    m "Tira logo esse sorrisinho da cara!"

    return

label karli_evento_falar2:

    scene ap_karli mc_conversando2 with Dissolve(2.0)

    pause

    m "Só não vai querer falar de mãe de novo, né?"

    mc "Haha! Deixa quieto, aprendi minha lição."

    m "Se bem que... eu tava pensando depois do que a gente conversou..."

    m "Acho que eu preciso resolver os lances com a minha mãe."

    mc "Sério?"

    m "A história é meio enrolada. Certeza que tu quer ouvir isso?"

    mc "Claro."

    m "Tipo... aconteceu uns rolos comigo e minha mãe me jogou pra fora de casa."

    mc "QUÊ?!"

    m "Pois é. Tipo, a gente brigou depois que ela descobriu um negócio sobre mim."

    m "E ela disse que era pra eu parar senão eu ia pro olho da rua. Só que eu não parei. E quando ela descobriu ela me chutou."

    mc "Que barra, [m]..."

    m "Mas tudo bem. Tava tranquila. Eu dei meu jeito."

    m "Até voltei a falar com ela faz um tempo. Só que ela tá entendendo tudo errado."

    mc "Hmmm..."

    m "Mas é isso! Só queria que você soubesse porque eu disse aquilo da minha mãe."

    mc "Valeu por me contar."

    mc "Só que assim... o mais importante tu não falou."

    m "Ah! E nem vou falar. É muito cedo pra você saber sobre isso."

    mc "Quê?! Mas-"

    m "Nem pensa."

    mc "Ok..."

    m "Mas e você? Cadê OS SEUS pais?"

    mc "Eu que sou o paparazzo aqui. Eu que faço as perguntas."

    m "Nem vem!"

    mc surpreso "Ei!"

    scene ap sala with vpunch

    mc angustiado "Não precisava me atacar no chão!"

    show karli p_feliz with dissolve

    m "Você fica perguntando tudo e depois vem com papinho que não pode falar de você. Pode abrindo o bico."

    mc envergonhado "Sei lá..."

    mc desculpa "Tipo. Eu também meio que fugi dos meus pais."

    mc normal "Mas é só isso que você vai saber."

    m "Você é um maldito. Mas se não quer contar, foda-se. Morra com seus segredos."

    mc "Valeu."

    m "Fala de mim, mas você também é cabeça dura."

    mc charmoso "Acho que tô aprendendo com a mestra."

    m "Engraçadinho..."

    m "Agora deixa eu sentar que já me cansei."

    return

label karli_evento_falar3:

    scene ap_karli mc_conversando1 with Dissolve(1.0)

    pause

    m "O que você acha da gente falar de filmes ao invés de dramas familiares?"

    mc normal "Fechou."

    "..."

    scene ap_karli mc_conversando2 with Dissolve(1.0)

    pause

    m "E eu bati no cara que entregava a pipoca."

    mc angustiado "..."

    "..."

    scene ap sala with Dissolve(1.0)

    show karli p_feliz with dissolve

    m "Valeu pelo papo."

    mc normal "Valeu você."

    m "Eu acho fácil conversar com você, sei lá."

    mc "Eu sou bom, pode falar."

    m "Cala a boca."

    m "Agora vou sentar."

    mc zerado "Parece uma velha..."

    if karli_seducao >= 5:

        m "Bem que você queria comer essa velha."

        mc envergonhado "Touché."

    return

label karli_evento_comer1:

    mc "Bateu aquela fome. Posso fazer algo pra você?"

    m "Uou! Sério mesmo que você cozinha?"

    mc zerado "Claro."

    m "E que delícia você vai fazer?"

    mc normal "Lanche de hamburguer."

    m "Hahaha!"

    mc zerado "Que foi?"

    m "Você chama isso de cozinhar?"

    mc "Sacanagem..."

    m "Tô brincando. Com certeza eu vou querer."

    mc "Beleza. Vou lá."

    scene ap cozinha with dissolve

    "As coisas pro lanche tão aqui na geladeira. Eu comprei no mercadinho esses dias."

    "..."

    scene ap mc_cozinhando1 with Dissolve(1.0)

    "Acho que os ingredientes ainda tão na data. Tomara..."

    "Agora eu só tenho que ajeitar aqui e daí{w=0.8}{nw}"

    show karli p_feliz with moveinbottom

    m "Bu!{w=0.5}{nw}"

    scene ap cozinha with vpunch

    mc angustiado "ARGH!"

    show karli p_explicando with dissolve

    m "Ops..."

    mc surpreso "Você fez eu derrubar tudo no chão!"

    m "Desculpa..."

    mc concentrando "Tudo bem..."

    m "Eu só queria dar uma animada."

    mc "..."

    m "E se a gente pedir uma pizza?"

    mc zerado "Pizza..."

    show karli p_feliz with dissolve

    m "Pode deixar que eu pago."

    mc "..."

    scene black with Dissolve(3.0)

    return

label karli_evento_comer2:

    mc zerado "E aí? Será que agora eu posso fazer um lanche sem uma babaca jogar tudo no chão?"

    m "Quê?! Babaca?! Foi você que jogou tudo no chão..."

    mc "..."

    m "Tá bom! Pode fazer sua mágica lá. Vou ficar comportada aqui."

    mc desconfiado "Ok..."

    scene ap cozinha with Dissolve(1.0)

    m "Obrigado pelo lanche!"

    "Depois de todo esse rolo, acho bom eu fazer um lanche decente."

    scene ap mc_cozinhando1 with Dissolve(1.0)

    "..."

    "E agora é só..."

    "Pronto!"

    "Espero que ela goste."

    scene ap cozinha with Dissolve(1.0)

    mc normal "Tá pronto!"

    m "Vem logo."

    "..."

    scene ap_karli sofa with Dissolve(1.0)

    m "Dá logo, [mc]! Esse cheirinho deu fome."

    mc normal "Tá aqui. Bom proveito."

    m "Aleluia!"

    scene ap_karli comendo with Dissolve(2.0)

    pause

    m "Hmmmm! Que delícia!"

    mc "Gostou?"

    m "Falar a verdade verdadeira, não tava botando fé nesse lanche seu não."

    mc "A é?"

    m "Sei lá, só pareceu idiota lanche de hamburguer hehe... Mas retiro tudo o que eu pensei! Tá puta bom!"

    mc "Valeu. Que bom que você curtiu."

    m "Morar sozinho não é fácil, né?"

    mc "Tem bastante coisa pra fazer, mas eu tô dando meu jeito."

    mc "Você também passa por isso, né?"

    m "Sim. Mas com um problema a mais."

    mc "Qual?"

    m "Não sei fazer um hamburguer bom assim!"

    mc "Haha! É fácil."

    m "Ok. Dá próxima vez eu faço pra você e a gente testa."

    mc "Cristo..."

    m "Ei!"

    mc "Hahaha!"

    scene black with Dissolve(1.0)

    m "Tava uma delícia."

    "..."

    return

label karli_evento_comer3:

    mc envergonhado "E aí? Lanche hoje... de novo?"

    m "Sim! Só que hoje eu vou fazer pra você."

    mc desconfiado "Sério?"

    m "Pode confiar em mim."

    mc preocupado "Mas você disse que não sabe..."

    m "Vamos ver quem não sabe o quê."

    m "Vai assistindo alguma coisa aí e quando tiver pronto eu te chamo."

    mc "O-ok..."

    m "E não precisa fazer essa cara."

    scene ap sala with Dissolve(1.0)

    m "Logo logo te chamo."

    mc normal "Tá. Valeu."

    scene ap mc_assistindo with dissolve

    "Agora é esperar. Tomara que pelo menos não fique cru. A pior coisa vai ser pegar desinteria por causa de hamburguer."

    "..."

    "{i}KLANK TLANK{/i}"

    "Meu Deus..."

    "..."

    m "Tá pronto! Pode vir!"

    "Senhor, me proteja."

    "..."

    scene ap cozinha with Dissolve(1.0)

    mc normal "E aí? Cadê?"

    show karli p_feliz with dissolve

    m "Ficou melhor do que eu imaginava. Tá faltando um pedaço porque eu comi pra experimentar."

    mc zerado "..."

    m "Aqui. Pode comer."

    scene ap mc_cozinhando2 with Dissolve(2.0)

    pause

    mc "Bom... até que ficou bonito."

    "Dá pra ver onde ela mordeu aqui... Que doidera essa mina."

    m "Eu disse. Pode comer."

    mc "..."

    m "Tá esperando o quê?!"

    mc "Não sei se tenho coragem."

    m "Ah, cuzão! Para de zoera e come logo!"

    mc "Ok..."

    scene black with dissolve

    mc "{i}chomp chomp{/i}"

    "..."

    m "E aí?"

    mc "Até que ficou bom..."

    "Certeza que essa merda ficou crua..."

    return

label karli_evento_comer4:

    mc normal "Vamo de hamburguer hoje?"

    m "Demorou."

    mc "Vou lá fazer e já trago."

    m "Valeu, garçom."

    mc zerado "..."

    scene ap mc_cozinhando1 with Dissolve(1.0)

    pause

    "Até que é massa cozinhar pra alguém. Sei lá, dá uma satisfação a [m] curtir minha comida."

    "Pronto."

    scene ap_karli sofa with Dissolve(1.0)

    mc normal "Tá aqui. Bom proveito."

    m "Aeeeeee! O cheiro tá bom."

    scene ap_karli comendo with Dissolve(2.0)

    pause

    m "Tá uma delícia, [mc]. Valeu, mano."

    mc "Da próxima vez tu que faz. Mas frita bem a porra do hamburguer."

    m "Haha! Pode deixar."

    scene black with dissolve

    m "Tava uma delícia."

    return

label karli_despedida:

    m "Ah! [mc]!"

    scene ap sala with Dissolve(1.0)

    mc normal "Que foi?"

    show karli p_explicando with dissolve

    m "Hoje eu tô saindo fora daqui..."

    mc surpreso "Quê?! Como assim?"

    m "Eu consegui resolver o que eu tinha que resolver e vou voltar a morar na minha casa mesmo."

    mc feliz "Isso é incrível, [m]! Parabéns!"

    m "Pois é..."

    mc preocupado "Que que tá pegando? Você parece, sei lá..."

    m "Não é nada. É só que... foi maneiro morar com você esses dias."

    mc envergonhado "Eu também achei muito bacana. De verdade."

    m "Foi mais legal que morar sozinha. Isso com certeza."

    menu:
        "Eu concordo. Também achei.":


            mc normal "Verdade. Foi legal dividir o apê com alguém."

            m "Sim..."
        "E se você ficasse aqui mais um tempo?":


            mc normal "E se você ficasse aqui mais um tempo?"

            m "Sério?"

            mc "Claro."

            m "Hmmm... eu até gostaria. Mas depois desse tempo todo, minha casa precisa de um tapa."

            mc desculpa "Tô ligado."

    mc charmoso "Mas, ó! Vamo repetir esse lance um dia. Quando você tiver de boa, me avisa e você fica aqui mais uns dias."

    show karli p_feliz with dissolve

    m "Ía ser maneiro."

    mc "Fechou?"

    m "Fechou. Aparece lá no salão {b}durante a tarde{/b} e vamos continuar com seu curso."

    m "Daí um dia desses a gente marca de novo."

    mc normal "Beleza."

    m "Vou me trocar e já vou saindo."

    mc "Vou te esperar então."

    m "Tá vou lá."

    hide karli with dissolve

    "Esses dias que a [m] passou aqui foi tudo de bom. Espero que a gente possa repetir isso um dia."

    m "Tô pronta. Bora?"

    mc normal "Bora."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
