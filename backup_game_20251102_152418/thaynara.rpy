label thaynara_menu:

    "Será que eu vou encontrar a [t] hoje?"

    menu:
        "Fazer compras e falar com a [t]":


            if thaynara_amizade:

                "A [t] pediu pra eu voltar aqui e falar com ela. Será que ela tá pronta?"

                scene thaynara caixa2 with Dissolve(1.0)

                mc "Oi, [t]. Tudo bem?"

                t "Oi, [mc]. Você pode me dar mais uns dias?"

                mc "Ok. Volto depois."

                "Ela ainda não quer conversar comigo... sobre o que será que ela quer falar?"

                scene black with dissolve

                "{b}A história da [t] continuará em atualizações futuras. Fique de olho nas redes sociais!{/b}"

                jump call_cidade

            python:

                renpy.choice_for_skipping()

                if renpy.android:
                    thaynara_db = PythonSDLActivity.pegaThaynara()



























            if thaynara_evento < thaynara_db:

                "{b}Você já fez compras [thaynara_db] vezes. Mas neste gameplay você comprou apenas [thaynara_evento] vezes.{/b}"

                "{b}Como não é preciso pagar duas vezes pelo mesmo evento, você pode continuar a história sem pagar novamente.{/b}"

                $ thaynara_evento += 1

                jump thaynara_evento

            python:
                if renpy.android:
                    cash = PythonSDLActivity.pegaCash()

            "Deixa eu ver aqui."

            "Tô com R$ [cash]."

            if cash >= 30:

                "Bacana. Dá pra comprar umas porcarias e daí na hora de acertar o valor eu falo com ela."

                menu:

                    "Gastar {b}C$ 30{/b} e falar com a [t]" if cash >= 30:

                        if thaynara_evento <= 11:

                            python:
                                if renpy.android:
                                    PythonSDLActivity.addThaynara()
                                    PythonSDLActivity.usaCash(30)

                                thaynara_evento += 1

                            jump thaynara_evento
                        else:


                            "É melhor dar um tempo pra ela respirar. Acho que vou voltar aqui outro dia."

                            "{b}A história da [t] continuará em atualizações futuras. Fique de olho nas redes sociais!{/b}"

                            jump call_cidade
                    "Não gastar essa grana agora":


                        "Pensando bem é melhor eu não gastar meu suado dinheirinho nisso."

                        "Depois eu volto e falo com ela."

                        jump call_cidade
            else:


                "Droga... não tenho grana suficiente pra gastar com porcaria."

                "Preciso arranjar uns trocados fazendo bicos antes de voltar aqui."

                mc zerado "É uma merda que o salário da revista só dê pra pagar o aluguel, comida e as contas..."

                mc angustiado "Por que a vida é tão complicada?!"

                jump call_cidade
        "Deixar para uma outra hora":


            "Não tô afim de fazer compras agora. Outra hora eu volto."

            jump call_cidade

label thaynara_evento:

    $ renpy.block_rollback()

    if thaynara_evento == 12:

        jump thaynara_evento12

    elif thaynara_evento == 11:

        jump thaynara_evento11

    elif thaynara_evento == 10:

        jump thaynara_evento10

    elif thaynara_evento == 9:

        jump thaynara_evento9

    elif thaynara_evento == 8:

        jump thaynara_evento8

    elif thaynara_evento == 7:

        jump thaynara_evento7

    elif thaynara_evento == 6:

        jump thaynara_evento6

    elif thaynara_evento == 5:

        jump thaynara_evento5

    elif thaynara_evento == 4:

        jump thaynara_evento4

    elif thaynara_evento == 3:

        jump thaynara_evento3

    elif thaynara_evento == 2:

        jump thaynara_evento2

    elif thaynara_evento == 1:

        jump thaynara_evento1

label thaynara_evento1:

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_1","thaynara","personagem")

    "Aquela garota que eu vi no outro dia é realmente linda."

    "Com certeza vale a pena gastar essa grana pra ter a chance de falar com ela."

    "Bora lá."

    scene mc mercado with Dissolve(2.0)

    mc "Boa. Deixa eu ver que vou comprar."

    "Acho que eu vou levar bolacha... ou seria biscoito?"

    "Também tô precisando de um treco que consiga tirar a barata quando elas se escondem embaixo das coisas."

    "Baratas... Deus tava muito bravo quando criou elas. E daí o diabo ainda fez o favor de colocar asas em algumas."

    "..."

    "Acho que isso é tudo. Hora da verdade."

    scene thaynara caixa with Dissolve(2.0)

    pause

    "Opa. Ela tá ali. Preciso agir de forma tranquila. Não quero assustar ela."

    "De boa, [mc]. Não vai exagerar. Tu não é um babaca."

    scene mercado caixa with Dissolve(1.0)

    mc normal "Olá. O dia tá bacana hoje, hein?"

    "Sério que isso foi o melhor que eu pensei?"

    show thaynara bemvindo with Dissolve(1.0)

    "Garota" "Oi, moço."

    "Garota" "Aqui tá sempre quente. Ainda não me acostumei."

    "Garota" "Se eu pudesse eu ficava pelada o tempo todo."

    mc surpreso "!"

    mc envergonhado "Pe-pelada?"

    "Garota" "Sim. Não é o que a gente faz no calor?"

    menu:
        "Seria complicado você trabalhar pelada.":


            mc normal "Seria melhor pra evitar o calor, mas trabalhar pelada seria um problema, não acha?"

            mc envergonhado "Todos veriam você sem roupa."

            show thaynara preocupada with dissolve

            "Garota" "O moço não ia querer me ver pelada?"

            mc "Nã-não é essa a questão..."

            "Garota" "Então por que?"

            mc normal "Tudo bem. Depois falamos melhor sobre isso."

            "Garota" "Tá..."
        "Eu iria comprar muito mais aqui se você ficasse pelada.":


            $ thaynara_seducao += 1

            mc charmoso "Com certeza eu ia comprar muito mais vezes aqui se você me atendesse pelada."

            "Garota" "Sério?!"

            mc "Ah... com certeza."

            "Garota" "Então parece uma boa ideia. Vou falar com o chefe."

            mc envergonhado "Ok..."

    show thaynara preocupada with dissolve

    "Garota" "Tem alguém na fila atrás do moço."

    "Garota" "Posso passar suas compras?"

    mc surpreso "Ah! Claro..."

    "..."

    show thaynara bemvindo with Dissolve(1.0)

    "Garota" "Vai ser só isso?"

    mc normal "Sim."

    "Garota" "Deu 30 reais."

    mc normal "Aqui está."

    "Garota" "Obrigada, moço. Até a próxima."

    mc normal "Ah, só queria saber seu no-"

    hide thaynara with dissolve

    "Garota" "Olá, senhor."

    "Droga... Ela já foi atender outro."

    scene mercado geral with Dissolve(1.0)

    "Não consegui nem descobrir o nome dela."

    "Tenho que voltar aqui outra hora e fazer compras de novo."

    $ tempo += 1

    jump call_cidade

label thaynara_evento2:

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_2","thaynara","personagem")

    "Deixa ver o que eu tenho que comprar hoje."

    scene mc mercado with Dissolve(2.0)

    "Tô pensando em comprar uma tranqueira..."

    "O que será melhor? Coxinha ou mortadela?"

    "Acho que nenhum dos dois..."

    "..."

    "Pronto."

    scene thaynara caixa with Dissolve(2.0)

    "Ela tá lá, igual da outra vez."

    "Não sei direito o que pensar sobre essa menina. Ela parece meio irônica, sarcástica."

    if mc_massagem > 0:

        "Esse jeito dela me lembra um pouco a [m]."

        "Essa forma irônica e sarcástica de falar."

    "Não é possível que ela tava sendo sincera quando disse que ia ficar pelada."

    "Espero que não seja uma doida..."

    scene mercado caixa with Dissolve(1.0)

    mc normal "Olá de novo."

    show thaynara bemvindo with Dissolve(1.0)

    "Garota" "Oi, moço. Eu me lembro de você."

    mc envergonhado "Que bom. Eu também lembro de você."

    "Algo na forma que ela fala sempre me deixa sem jeito."

    mc "É... da outra vez não consegui te perguntar."

    mc normal "Eu me chamo [mcc]. Qual é seu nome?"

    $ t_nome = "Thaynara"

    t "Eu sou Thaynara."

    mc "[t]. Que nome bacana."

    t "Que bom que você gostou."

    mc normal "É um nome que eu nunca tinha ouvido antes. Você nasceu aqui mesmo na capital?"

    show thaynara amizade with Dissolve(1.0)

    t "Não. Eu sou de outro lugar."

    mc "A é? De onde?"

    t "Eu venho de bem longe."

    menu:
        "Eu já entendi! Mas de onde?!":


            mc serio "Eu entendi que você não é daqui. Mas de onde você veio exatamente?! Isso que tô perguntando."

            show thaynara preocupada with dissolve

            t "Por que o moço tá bravo comigo?"

            mc envergonhado "Ah?! É... não tô bravo. Só quero que você seja mais específica."

            t "Mas eu não respondi sua pergunta?"

            mc concentrando "Tudo bem... respondeu sim..."
        "E é legal lá?":


            mc normal "E é legal lá onde você morava?"

            t "Muito! A gente era muito mais livre do que aqui."

            mc desconfiado "Muito mais livres?"

            t "Sim!"

            mc "Muito mais livres co..."

            mc concentrando "Deixa quieto. Tá bom por hoje."

            t "..."

    show thaynara preocupada with dissolve

    t "A fila já tá ficando grande, moço."

    mc envergonhado "Ops. Perdão. Volto outra hora."

    show thaynara bemvindo with dissolve

    t "Eu gosto de falar com você."

    mc normal "Então tá. Até a próxima."

    $ tempo += 1

    jump call_cidade

label thaynara_evento3:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_3","thaynara","personagem")

    "Essa [t]. Não consigo entender a dela. As respostas são sempre diretas e simples, como se ela não quisesse revelar a verdade."

    scene mc mercado with Dissolve(2.0)

    "Bom... hoje eu vou levar..."

    "Eu vi no Face aqueles vídeos de comida de dois minutos. Parece mó fácil... certeza que eu consigo fazer."

    "..."

    "Pronto! Vai ficar uma delícia!"

    "..."

    scene mercado caixa with Dissolve(1.0)

    "Ela tá lá. Preciso saber um pouco mais sobre ela."

    show thaynara bemvindo with Dissolve(1.0)

    t "Oi, moço."

    mc normal "Oi, [t]."

    t "Você lembrou meu nome! Você é a primeira pessoa que lembra meu nome de primeira."

    mc "Eu entendo. Ele é meio difícil de decorar mesmo."

    t "Seu nome..."

    show thaynara preocupada with dissolve

    t "..."

    t "É..."

    "..."

    mc "[mc]."

    t "Não consegui lembrar..."

    mc normal "Não tem problema."

    t "Você lembrou o meu, queria lembrar o seu também. Agora fiquei triste."

    menu:
        "Você fica mais bonita sorrindo.":


            $ thaynara_seducao += 1

            mc charmoso "Não quero que fique assim. Você fica muito mais bonita quando tá sorrindo."

            show thaynara amizade with dissolve

            t "Então eu vou sempre sorrir pra você, [mc]."

            t "Quero que você me ache bonita."

            mc envergonhado "Sé-sério? Mas..."

            t "Eu quero ser a mais bonita que eu puder."

            mc "Ok..."
        "Não precisa se preocupar com isso.":


            mc normal "Não precisa se preocupar com isso."

            t "Eu preciso. Quero poder lembrar seu nome igual você lembra do meu."

            "Esse jeito dela falar... Não parece certo, mas não sei dizer exatamente o problema."

            t "Eu vou me esforçar, [mc]. Vou acertar da próxima vez."

            mc "Combinado."

    mc normal "Bom. Tem gente chegando pra passar a compra. Vou indo nessa."

    show thaynara bemvindo with dissolve

    t "Ficou R$ 30."

    mc normal "Tá aqui."

    t "Obrigada. E venha comprar mais vezes. Eu gosto de ver você."

    mc envergonhado "O-ok..."

    hide thaynara with dissolve

    scene mercado geral with Dissolve(1.0)

    "Essa garota é uma peça. Será que é possível que ela fale assim de verdade? Que ela é tão inocente a esse ponto?"

    "Preciso falar com ela mais vezes."

    "Da próxima vez vou tentar conversar com ela por mais tempo. Talvez fazer um pouco de companhia pra ela enquanto ela trabalha."

    $ tempo += 1

    jump call_cidade

label thaynara_evento4:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_4","thaynara","personagem")

    "Eu resolvi que hoje eu quero saber mais sobre a [t]."

    scene mc mercado with Dissolve(1.0)

    "Deixa eu pegar qualquer coisa aqui só pra justificar a compra."

    "Palha de aço... Desinfetante... Multi uso... Nunca comprei nada dessas coisas."

    "..."

    scene thaynara caixa with Dissolve(2.0)

    "Ela tá lá."

    "Toda vez que ela fala comigo eu sinto uma inocência. Como se ela não escondesse os reais sentimentos dela."

    "Mas isso é impossível."

    mc zerado "Todo mundo sabe que os adultos nunca falam seus reais sentimentos."

    mc normal "Oi, [t]. Tudo bem?"

    scene mercado caixa with Dissolve(1.0)

    show thaynara incerta with dissolve

    pause

    t "Uaaahhhh...."

    show thaynara amizade with dissolve

    t "Oi, [mc]! Hehe! Hoje eu lembrei do seu nome!"

    mc normal "É verdade. Parabéns."

    t "Obrigada! Fiquei muito feliz!"

    mc envergonhado "Não é pra tanto, [t]..."

    show thaynara preocupada with dissolve

    t "Como assim?"

    mc desconfiado "É... quero dizer que... sei lá... não precisa ficar TÃO feliz por isso."

    t "Por que não posso ficar feliz?"

    mc "Hmm... não é que não pode. É que não é normal."

    t "Normal? O que é normal? Eu não sou normal?"

    "Ixi... por que eu fui me meter nesse vespeiro?"

    menu:
        "Você não é normal. Você é gata, além de sexy.":


            $ thaynara_seducao += 1

            mc charmoso "Quero dizer que você não é como as outras garotas, você é muito gata. Além de ser sexy."

            show thaynara seduzida with dissolve

            t "Você me acha gata?"

            mc "Óbvio."

            t "Você também é gato, [mc]. Eu te acho lindo."

            mc safado "Obrigado, [t]."

            mc "A gente-"
        "Você é normal, claro que é.":


            mc envergonhado "Você é normal, sim. Claro que é. Não fique pensando nisso!"

            t "Tem certeza?"

            mc "Claro. Você é como qualquer outra garota aqui da ilha."

            show thaynara bemvindo with dissolve

            t "Sério?! Isso é muito bom!"

            t "Eu queria ser muito como as garotas daqui."

            mc desconfiado "Como assim queria ser como as garotas daqui... Você não é daqui?"

            t "Lembra que eu-"

    t "Opa! Tá vindo um cliente. Você pode sair pra eu atender ele?"

    mc envergonhado "Ah! Claro. Tchau, [t]."

    t "Tchau, [mc]!"

    hide thaynara with dissolve

    "..."

    "Por que nossas conversas sempre partem pra algo nada a ver e eu fico sem falar sobre o que eu quero?"

    "Será que ela tá manipulando a conversa e eu não tô percebendo?"

    "Preciso voltar aqui pra ver isso."

    $ tempo += 1

    jump call_cidade

label thaynara_evento5:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_5","thaynara","personagem")

    "E tô eu aqui no mercado de novo pra ver essa guria estranha."

    "Hoje não importa o que aconteça, eu vou ficar aqui até eu entender qual é a dela. Nem que eu atrapalhe a fila toda."

    scene mc mercado with Dissolve(1.0)

    "Vou pegar aqui um {b}MEGA POWER Energy Drink{/b}. Porque gamers de verdade tomam {b}MEGA POWER Energy Drink{/b}."

    "Não acredito que tem gente que cai nesse tipo de marketing barato... Bando de trouxas."

    scene thaynara caixa with Dissolve(1.0)

    "Hmmm... como sempre ela tá lá."

    "Talvez eu devesse dar uma olhada na reação dela com outras pessoas..."

    mc zerado "..."

    "Eu não sei se eu me sinto um stalker ou um cientista analisando a fauna da cidade grande."

    "Opa! Vem vindo alguém..."

    scene mercado caixa with Dissolve(1.0)

    t "Vai ser só isso?"

    show sofia falando with dissolve

    w "Sim."

    if sofia_e1 != "nada":

        "QUÊ?! É a filha do chefe!"

    show sofia falando at direita with move

    show thaynara bemvindo with dissolve

    t "Vai dar C$ 12."

    show thaynara bemvindo at esquerda with move

    w "..."

    t "Seu troco."

    w "..."

    show thaynara desconfiada with dissolve

    t "Você é meio quieta, moça."

    show sofia seria with dissolve

    w "Como?"

    t "Por que você não fala?"

    w "O que isso te interessa?"

    t "Você me deixou interessada."

    show sofia meudeus with dissolve

    w "..."

    hide sofia with dissolve

    hide thaynara with dissolve

    show thaynara preocupada with dissolve

    t "Será que eu falei alguma coisa que eu não devia?"

    t "..."

    "Então quer dizer que ela tem esse jeito com os outros clientes também..."

    "Deixa eu falar com ela."

    mc normal "Olá, [t]. Como vai?"

    show thaynara bemvindo with dissolve

    t "Oi, [mc]! Que bom ver você!"

    mc "O que houve?"

    show thaynara preocupada with dissolve

    t "Eu acho que eu fiz alguma coisa de errado com a moça que tava aqui..."

    mc normal "Não precisa fazer essa cara."

    menu:
        "Vai ficar tudo bem. Você vai ver.":


            mc "Vai ficar tudo bem, ok? Não foi nada de mais."

            t "Certeza?"

            mc "Com certeza."

            show thaynara amizade with dissolve

            t "Que bom!"

            t "Ufa. Eu achei que ela não tinha gostado de mim."

            "Pronto? Ela só acreditou em mim e todas as preocupações dela se foram?"

            mc "Haha. Ela gosta de você. É só o jeito dela."
        "Você é muito mais atraente sorrindo.":


            $ thaynara_seducao += 1

            mc charmoso "Você sabe que você fica muito mais atraente quando tá sorrindo."

            t "Ah?"

            show thaynara seduzida with dissolve

            t "Ai, [mc]. Quando você fala assim comigo, eu sinto um calor..."

            t "Eu tenho vontade de te abraçar."

            "Como é?!"

            mc envergonhado "Ah... isso é normal..."

            t "Tá... Mas não fica fazendo assim..."

    "Não consigo acreditar nessa mina. Ela me desarma todas as vezes."

    mc envergonhado "Vou indo nessa. Aqui tem C$ 30."

    show thaynara desconfiada with dissolve

    t "Como você sabe que deu C$ 30?"

    mc "Po-pode ficar com o troco."

    scene mercado geral with Dissolve(1.0)

    mc concentrando "Ufa..."

    "A conversa ficou estranha demais. Não conseguia mais olhar pra cara dela."

    "É um sentimento impossível de descrever. É como se tudo o que eu sinto fosse refletido em um espelho..."

    "Que coisa maluca de se pensar..."

    "Sei lá. Preciso de um banho."

    $ tempo += 1

    jump call_cidade

label thaynara_evento6:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_6","thaynara","personagem")

    "Incrível como essa [t] tá mexendo com a minha cabeça. Eu ainda vou descobrir qual é a dessa garota."

    "Será que ela faz isso com todo mundo só pra gente gastar dinheiro no mercado?"

    mc zerado "E eu tô pagando de idiota..."

    scene mc mercado with Dissolve(1.0)

    "Vou pegar umas coisas aqui rapidão..."

    "{i}{b}Cavalo Power{/b} vai te deixar bombado e fazer as minas pagarem pau para você.{/i}"

    "{i}Se você quer virar homem de verdade, beba Cavalo Power.{/i}"

    "Caraca, isso aqui parece bom mesmo. Vou levar."

    "Hora da verdade."

    scene thaynara caixa2 with Dissolve(1.0)

    "Ela tá lá sozinha. Não tem mais ninguém no mercado. Perfeito."

    scene mercado caixa with Dissolve(1.0)

    mc normal "Oi, [t]."

    show thaynara amizade with dissolve

    t "Oi, [mc]. Tudo bem?"

    mc "Tudo. E você?"

    t "Um pouco cansada. O trabalho é bem cansativo, além de ser chato ficar fazendo a mesma coisa todos os dias."

    mc envergonhado "Imagino..."

    t "E o dinheiro que eu ganho eu acho que é pouco, porque eu quase não consigo comprar nada com ele."

    mc desculpa "Que droga..."

    t "Mas tudo bem. Se eu continuar me esforçando meu patrão disse que vai melhorar meu salário."

    mc normal "A é?"

    mc normal "Eu tava pensando. Será que eu podia conversar um pouco com você hoje?"

    show thaynara desconfiada with dissolve

    t "Mas a gente já não conversou um pouco? Como assim?"

    mc envergonhado "Digo. Posso ir desse lado do caixa com você?"

    show thaynara preocupada with dissolve

    t "Mas o chefe disse que ninguém pode vir aqui."

    menu:
        "Mas não tem problema não obedecer o chefe.":


            mc tarado "Mas não tem nenhum problema não obedecer o chefe de vez em quando."

            t "Sé-sério?"

            mc "Sim. Ninguém é perfeito, concorda?"

            t "Ninguém no mundo é perfeito?"

            mc "Não."

            t "Eu também não?"

            mc surpreso "Ah!"

            mc envergonhado "É... O que você acha?"

            t "Eu... não sei..."

            mc envergonhado "Então eu vou ir aí atrás e a gente vê isso."

            t "T-tá."
        "Vai ficar tudo bem.":


            mc normal "Não precisa ficar preocupada. Vai ficar tudo bem."

            t "Vai ficar tudo bem mesmo desobedecendo ele?"

            mc normal "Com certeza."

            show thaynara bemvindo with dissolve

            t "Então tá tudo bem. Pode vir."

    mc "Com licença."

    hide thaynara with dissolve

    "..."

    scene thaynara_mc_conversando with Dissolve(1.0)

    pause

    t "É a primeira vez que alguém vem aqui."

    mc "E o que você achou?"

    t "Eu achei divertido. E também me sinto menos sozinha."

    mc "Você gosta de conversar comigo?"

    t "Eu gosto. Você é muito legal, [mc]."

    mc "Que bom que você acha isso."

    menu:
        "Eu também te acho muito legal.":


            mc "Eu acho você muito legal também."

            t "Obrigada."

            mc "Eu gosto de conversar com você. Eu acho você uma pessoa verdadeira."

            t "O que é ser verdadeira?"

            mc "Como assim?"

            t "Eu não sei o que é ser verdadeira que você disse aí."

            mc "Hmm... ser verdadeiro é não mentir. É falar sempre a verdade."

            t "Por que eu iria mentir? Isso não é errado?"

            mc "É... É um tanto errado. Mas é mais complicado do que isso."

            t "Por que complicado? Se é errado a gente não devia fazer, não é?"

            mc "Sim. Mas a vida adulta não é fácil, [t]. Às vezes a gente precisa mentir pra manter as coisas bem."

            t "Mas se mentir é errado... Como isso pode ajudar?"

            mc "Eu não sei como te explicar isso. Bom..."

            mc "Você me acha o homem mais bonito do mundo?"

            t "Não."

            mc "Ok..."

            "Essa doeu. Mesmo sendo óbvio, ouvir assim na lata dói o coração."

            mc "Eu também não te acho a mulher mais linda do mundo."

            t "Certo."

            mc "Tudo bem?"

            t "Tudo."

            mc "Quero dizer. Tudo bem eu não te achar a mulher mais linda do mundo? Isso não te deixa triste ou algo assim?"

            t "Não. Eu deveria ficar? Fiz alguma coisa de errado?"

            mc "Não! Calma... é que às vezes as pessoas não se sentem bem quando elas não são as melhores."

            mc "E daí a gente mente alguma coisa pra que elas não se sintam mal. Você entende isso?"

            t "Não muito. Se eu não sou a mulher mais bonita do mundo, isso não muda muito minha vida."

            t "E se alguém falar que eu sou feia, tudo bem. É a opinião dela. Por que eu deveria me sentir mal?"

            mc "Pensando assim, até que você tem razão, mas..."
        "Eu te acho muito linda.":


            $ thaynara_seducao += 1

            mc "E eu te acho muito linda. E essa roupa mostra bastante do seu corpo. Você é muito gata."

            t "Você acha?"

            mc "Com certeza. Eu gosto muito de olhar pra você, tudo bem?"

            t "Tudo. Eu gosto quando você olha pra mim."

            mc "Verdade?"

            t "Sim. Eu sinto seus olhos passando por todo meu corpo. Olhando pra todas minhas partes."

            t "Parece que você quer poder me lamber, me morder. Pelo menos é o que eu sinto."

            mc "Você tá certinha."

            t "Isso faz eu sentir um negócio estranho. Eu sinto um calor no meu corpo."

            t "Eu fico com vontade de tirar minha roupa."

            mc "Por que você não tira?"

            t "O chefe disse que não posso tirar aqui na loja."

            mc "Que pena..."

            t "É verdade."

            "Caralho. Se continuar assim essa mina vai me deixar louco. Eu vou pular em cima dela aqui mesmo."

            mc "É..."

    mc "Tudo bem. Acho que por hoje tá legal."

    t "Você vai embora?"

    mc "Sim. Tudo bem?"

    t "Sim. Eu gostei. Você podia vir mais vezes aqui comigo."

    mc "Eu vou com certeza."

    mc "Tchau, [t]."

    t "Tchau."

    scene mercado geral with Dissolve(1.0)

    "Quanto mais eu converso com ela, menos eu entendo essa mina."

    "Será que ela tem algum problema na cabeça?"

    "Às vezes eu sinto como se tivesse conversando com uma criança."

    "Isso com certeza é muito suspeito. Eu tenho que voltar aqui de qualquer jeito."

    $ tempo += 1

    jump call_cidade

label thaynara_evento7:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_7","thaynara","personagem")

    "Eu aqui de novo no mercadinho pra stalkear uma pobre garota."

    "Pior é que eu vou acabar gastando todo o dinheiro que eu tô ganhando fazendo bico no bar por causa dessa mina."

    "Mas eu simplesmente não acredito "

    scene mercado mesas with Dissolve(1.0)

    "Vou pegar umas coisinhas rápido só pra ir pro caixa."

    "{i}Super Achocolatado LIGHT, 1%% menos carboidratos pelo dobro do preço! É simplismente IN-CRÍ-VEL!{/i}"

    "Parece que vale à pena esse Light pra dar aquela arrumada no shape. Vou comprar três do pequeno."

    "Agora é esperar não ter fila e nem ninguém pra me acelerar..."

    "..."

    "Bora!"

    scene thaynara caixa2 with Dissolve(1.0)

    "Ela tá ali. Só agir naturalmente..."

    mc "Oi, [t]. Tudo bem com você hoje?"

    t "Oi, [mc]! Tá tudo legal, sim."

    t "Hoje eu tô com uma preguiça..."

    scene thaynara_espreguicando with Dissolve(1.0)

    pause

    mc surpreso "!"

    t "Eu queria tanto tirar um soninho..."

    mc envergonhado "Não tá conseguindo dormir direito?"

    t "Tô... mas quando não tem ninguém na loja sempre dá sono."

    mc "Entendi..."

    "Do jeito que ela tá fazendo dá pra ver bem os... é..."

    menu:
        "Olhar para o busto dela":


            $ thaynara_seducao += 1

            "Não dá pra resistir."

            mc "Deixa eu chegar mais perto pra ajudar."

            t "Tá."

            mc safado "Se você continuar assim a preguiça passa."

            t "Sério?"

            mc "É. Estica bem os braços. Bem pra trás."

            scene thaynara_espreguicando_close with Dissolve(1.0)

            pause

            t "Hmmm..."

            t "Assim?"

            mc safado "Isso. Agora continua."

            mc "Conta até trinta bem devagar."

            t "T-tá... 1..."

            "Essa mina... Não é possível que ela não percebe."

            "Eu não vou reclamar..."

            window hide

            pause

            t "Trinta!"

            mc "Muito bem."

            scene thaynara_espreguicando with Dissolve(1.0)

            t "Até que foi gostoso..."
        "Desviar o olhar":


            mc envergonhado "Nah... você não merece isso."

            t "Não mereço?"

            mc "Não... você precisa tomar cuidado, [t]. Tem muito homem safado por aí."

            t "Homem safado? Como assim?"

            mc "Homem que não tem respeito por você e vai fazer de tudo pra tirar vantagem."

            t "Mas isso não é errado, [mc]?"

            mc "Com certeza..."

            t "E tem gente que faz mesmo assim?"

            "Eu não acredito que tô tendo esse diálogo."

            mc "Pois é..."

            t "Puxa... eu nunca vi um homem assim. Deve ser perigoso."

    mc envergonhado "É... agora acho que vou passar a compra."

    t "Tá legal. Da próxima vez você podia fazer companhia pra mim aqui."

    mc "Você não disse que o chefe não deixa?"

    t "É... mas... é..."

    mc charmoso "Entendi. Da próxima vez eu fico então e te ajudo com a preguiça. O que me diz?"

    t "Isso!"

    scene mercado geral with Dissolve(1.0)

    t "Os três ficou em C$ 30."

    mc angustiado "O anúncio realmente não mentiu!"

    t "Volte sempre!"

    $ tempo += 1

    jump call_cidade

label thaynara_evento8:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_8","thaynara","personagem")

    "Eu já comprei tudo o que eu precisava esses dias. Acho que já ficou óbvio que eu venho aqui só pra ver a [t] mesmo..."

    "Vou tentar pegar alguma coisa baratinha aqui... Ovo orgânico? Não tem preço aqui, mas ovo não pode ser tão caro, né?"

    scene thaynara caixa2 with Dissolve(1.0)

    "Ela tá lá de novo."

    "Sorte que eu nunca peguei ela doente nem nada disso. Ela parece sempre de boa. Ah! Teve aquela vez com a Sofia."

    "Acho que foi a única vez que eu vi a [t] meio down. Normalmente ela é bem pra cima."

    "Por que ao invés de eu ficar aqui pensando sozinho eu só não vou lá falar com ela?"

    mc normal "E aí, [t]? Tá tudo bem?"

    scene thaynara1 with Dissolve(1.0)

    pause

    t "[mc]! De novo você veio comprar aqui?"

    mc envergonhado "Que foi? Não gosta quando eu venho?"

    t "Não é isso. É que esse mercado é meio caro, sabe? E você parece meio pobretão."

    mc zerado "A é, é?"

    t "Mas uma vez me disseram que às vezes as aparências enganam... então será que você é rico?"

    menu:
        "Pffft! Tô mais pra pobretão mesmo.":


            mc envergonhado "Sem dúvidas eu tô mais pro lado do pobretão igual você disse."

            t "Haha... então seu livro é igual à capa, né?"

            mc normal "Acho que você pode dizer que o dinheiro da pessoa não quer dizer quem ela é."

            t "Eu concordo com você."
        "Eu tenho tudo o que eu preciso.":


            mc charmoso "Na verdade eu tenho tudo o que eu preciso. Tô de boa."

            t "Então tá."

            mc desconfiado "Você não acha bacana ter dinheiro?"

            t "Não."

            mc "..."

    t "Mas se você tem dinheiro pra comprar aqui e falar comigo, eu fico muito feliz."

    mc normal "Own... você é muito fofa, [t]."

    t "Você acha? Hmmm..."

    mc "É, sim. Aliás, você tá diferente. Você fez alguma coisa?"

    t "Então você percebeu? Eu mudei um pouco o cabelo. Deve ser isso. Mas tá melhor ou pior?"

    mc charmoso "Melhor. Ficou mais bonita."

    scene thaynara2 with Dissolve(1.0)

    pause

    t "A-ai... O-obrigada, [mc]... "

    mc desconfiado "Que foi? Por que tá com essa cara?"

    t "N-não sei o que acontece..."

    mc "Como assim? Você tá sentindo alguma coisa?"

    t "Às vezes... quando a gente tá conversando, eu sinto isso. É um aperto no peito."

    t "E eu sinto que minha respiração fica mais rápida e às vezes até parece que falta ar."

    mc envergonhado "Quando que isso acontece?"

    t "Quando eu tô falando com você às vezes."

    mc "[t]... você sabe o que você tá querendo dizer, né?"

    t "Hm? Como assim? Você acha que eu tenho algum problema?"

    mc "Eu não diria problema... mas... eu nem sei como falar isso pra você. Certeza que você não sabe?"

    t "Você tá me deixando preocupada, [mc]."

    mc normal "Olha... repara se isso acontece com outras pessoas que você conhece. Com outros rapazes ou garotas."

    t "E-eu acho que não..."

    mc envergonhado "Ai, caralho..."

    mc "Faça esse teste direitinho e da próxima vez que eu vier a gente conversa mais sobre isso."

    t "Tá... mas você acha que é grave? Eu não tô pronta pra voltar pra casa ainda. Mas se eu ficar doente..."

    mc normal "Relaxa. Isso é normal. Não é nada de mais, ok?"

    t "Você promete?"

    mc charmoso "Prometo."

    scene thaynara1 with Dissolve(1.0)

    t "Então tá combinado. Eu vou ver melhor quando isso acontece... e daí depois você me fala como resolver isso."

    mc envergonhado "Eu ainda não tô acreditando que a gente tá conversando sobre isso..."

    t "Mas eu não tô brincando."

    mc "É difícil de acreditar, mas eu acredito em você..."

    "Será que a [t] realmente tá gamada em mim? Essa descrição dela..."

    "Mas é impossível que alguém da idade dela não saiba o que é paixonite. Será que eu tô me antecipando?"

    "Talvez não seja nada disso e eu tô achando demais... seria meio vergonha alheia se no fundo ela nem tivesse aí pra mim."

    t "[mc]?"

    mc envergonhado "D-desculpa, tava pensando num negócio aqui."

    mc normal "Você precisa conversar com outras pessoas e veja se você sente a mesma coisa e da próxima vez a gente tira a dúvida, ok?"

    t "Tá bom. Até a próxima."

    mc "A gente se fala, [t]. Fica bem até lá."

    scene black with dissolve

    "Cada uma..."

    "Seria uma boa também eu pensar o que EU quero com a [t]. Ela é muito fofa, bonita, tem um corpão... mas esse jeito dela..."

    "Alguma coisa não tá cheirando bem aqui..."

    "O que eu faço?"

    $ tempo += 1

    jump call_cidade

label thaynara_evento9:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"
    $ thay_pega = False

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_9","thaynara","personagem")

    "Da outra vez que eu vim foi tudo super estranho... a [t] começou com aquele papo de falta de ar..."

    scene thaynara caixa2 with Dissolve(1.0)

    "Na hora eu achei que ela tava querendo se declarar pra mim. Querendo dizer que gostava de mim e talz."

    "Mas depois a conversa andou pra um lado estranho... como se ela realmente não tivesse entendendo."

    "E depois no fim eu comecei a pensar que não era nada disso. Uma total mudança no pensamento..."

    "Será que eu sofro de baixa autoestima?"

    "Foda-se. Bora ver o que tá acontecendo aqui."

    scene thaynara1 with Dissolve(1.0)

    pause

    mc normal "Olá."

    t "Oi! Veio comprar o quê hoje?"

    "Nada. Só vim ver você mesmo.{w} Melhor não ser sincero desse jeito..."

    mc envergonhado "Eu quero um desse aqui... e um desse aqui..."

    t "Parece que você tá escolhendo tudo agora, [mc]. Nem tá pensando direito hihi..."

    mc surpreso "É que eu precisava disso! Muito urgente!"

    t "Então tá. Você é engraçado."

    mc envergonhado "P-pelo menos eu fiz você rir."

    t "Ah!"

    scene thaynara2 with Dissolve(1.0)

    pause

    mc desconfiado "Que foi?"

    t "Aconteceu aquilo de novo..."

    mc envergonhado "Aquilo que a gente tava conversando da outra vez?"

    t "É. Eu tô sentindo agora. Um negócio na barriga..."

    mc normal "Você fez o que eu falei? Você viu se isso acontecia com outras pessoas?"

    t "Eu prestei atenção. Eu prometo, [mc]."

    mc envergonhado "Ok. Eu acredito. E aí?"

    t "Não senti nada..."

    mc "Com ninguém?"

    t "Não. Eu tentei com meu chefe, que é a pessoa que eu mais falo."

    mc desconfiado "Só com ele?"

    t "É... e c-com uma... amiga."

    mc "Certo..."

    t "E nada... isso só aconteceu agora de novo... desde que a gente se falou aquele dia."

    mc "E nem com outros clientes?"

    t "Tem um outro cliente só que fala comigo... ele é legal também... só que... não sei se é igual."

    mc envergonhado "Então tem outra pessoa que é parecida..."

    t "Ele é muito legal também, [mc]. Ele faz brincadeiras e conta piadas. Eu me divirto quando ele passa aqui."

    t "Mas não é a mesma coisa. Quando você fala comigo... e o jeito que você fala... eu fico assim..."

    "Então é isso. Acho que a [t] realmente tá afim de mim. Mas parece que nem ela sabe."

    "O que eu faço com isso agora?"

    "É uma sensação muito bacana ter alguém gostando de você. Eu posso aproveitar um pouco isso se pá..."

    "Uma brincadeirinha sem compromisso... só pra trollar ela um pouco."

    "Se bem que a [t] é super gatinha, né? Talvez dar uns beijos nela não ia ser ruim..."

    t "[mc]? Tá tudo legal? Você acha que é perigoso?"

    "Essa é minha chance. Será que eu faço isso com ela ou vou embora?"

    menu:
        "Acho que preciso examinar você.":


            $ thay_pega = True

            mc charmoso "A questão é que pra eu saber melhor, eu vou ter que te examinar."

            t "Isso é sério?"

            "Caralho... que merda que eu falei? Claro que nem ela ia cair nessa."

            mc envergonhado "Haha... eu tava só brincand-{nw}"

            t "Tudo bem. Se é pra ter certeza... como que é isso?"

            mc surpreso "S-sério?!"

            t "É melhor ter certeza, né?"

            mc envergonhado "C-claro. É uma coisa simples. Eu só vou ter que ir aí do seu lado."

            t "Tá..."

            scene black with dissolve

            mc "Agora me dá sua mão."

            scene thaynara_mc1 with Dissolve(1.0)

            pause

            t "[mc]... t-tão perto?"

            mc "Isso. Eu tenho que pegar nas suas mãos assim."

            t "Tá... ai..."

            mc "O que você tá sentindo agora? Melhorou?"

            t "Não! Tá muito pior!"

            mc "Sério? Quando eu passo minha mão em você assim... não melhora?"

            t "N-não! E-eu sinto meu coração batendo muito forte!"

            mc "Hmm... então é isso..."

            t "Ah..."

            mc "Acho que a gente vai ter que fazer outra dessa da próxima vez."

            t "Sério?"

            mc "Não precisa ficar preocupada por enquanto. Mas é melhor eu manter o olho em você."

            t "Tá. O-obrigada... {i}puf{/i}"

            mc "O importante é que você vai ficar bem. Eu vou te ajudar sempre que eu vier, tá?"

            t "Combi... nado..."

            mc "Até mais."

            scene black with dissolve

            "A garota quase teve um treco... o que eu tô fazendo?"

            "Bom... foi bem divertido. Vamos ver onde a gente chega com isso da próxima vez."
        "Eu não quero nada com ela. Esquece isso":


            "Não. Não vou causar com ela. Eu nem tô afim da [t] mesmo. Não tenho porque fazer isso."

            mc normal "Relaxa. Você tá bem, ok?"

            t "Você tem certeza?"

            mc "Isso é normal. Hoje eu já fiquei tempo demais aqui. Mas da próxima vez a gente conversa sobre isso, ok?"

            scene thaynara1 with Dissolve(1.0)

            t "Ufa. Eu fico mais tranquila, [mc]. Como sempre, você me ajudando."

            t "Quando der então venha comprar mais dessas coisinhas aí."

            mc "Pode deixar. Até outro dia."

    scene black with dissolve

    $ tempo += 1

    jump call_cidade

label thaynara_evento10:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_10","thaynara","personagem")

    "Nem tenho mais porque disfarçar. Nessa altura do campeonato a [t] já sabe que eu venho aqui só por causa dela."

    "Da outra vez foi demais..."

    "Ficou na cara que a [t] tá na minha. Só que ela é inocente demais. Como que ela pode não entender uma coisa dessas?"

    "Será que ela nunca se apaixonou antes com essa idade? Impossível."

    if thay_pega:

        "E eu ainda resolvi brincar com ela. Quando eu peguei nela... mano... a minha quase teve um treco."

        "O que será que eu consigo fazer com ela hoje?"
    else:


        "Eu resolvi não causar com ela ontem."

        "Primeiro que eu não tô afim da [t] desse jeito. E segundo que é mancada, né?"

    "Só que eu vou ter que falar sobre isso com ela. E se realmente eu for a primeira pessoa que ela gostou... vixi..."

    "Eu vou ter que tomar cuidado pra não machucar ela. Não importa o que eu decida fazer, eu tenho que ser bacana."

    "O Pequeno Príncipe fala que a gente é responsável por aqueles que a gente cativa, então... né... foda."

    scene black with dissolve

    scene thaynara1 with Dissolve(1.0)

    mc normal "Oi, Thay."

    t "Oi, [mc]."

    mc "Eu vim falar com você sobre o outro dia."

    t "Ah..."

    mc "Será que eu posso ir aí?"

    if thay_pega:

        t "V-você vai precisar me examinar de novo? Igual da outra vez?"

        mc charmoso "É muito importante."

    t "Ok..."

    scene black with dissolve

    "..."

    scene thaynara_mc1 with Dissolve(1.0)

    pause

    t "Ai... meu coração tá batendo tanto, [mc]."

    mc "Olha... o que eu vou falar pra você é muito sério."

    t "Ok..."

    "Eu preciso {b}decidir agora{/b} o que eu quero com a [t]."

    "Não precisa ser nada sério por enquanto... mas eu vou querer dar uns pegas nela ou só amizade mesmo?"

    label thaynara_pega_escolha:

        "Essa escolha vai mudar completamente meus próximos passos com ela."

    menu:
        "Eu vou me divertir com ela":


            $ thay_pega = True

            "A [t] é muito gata e essa inocência dela só me dá mais vontade de abusar. Eu sou um ser humano horrível mesmo..."

            "Mas se ela gosta de mim... qual o problema, certo?"

            t "[mc]..."
        "Eu não quero nada com ela":


            "Não quero nada com ela mesmo... a partir de hoje ela é só uma amiga mesmo."

            "É isso mesmo que eu quero?"

            menu:
                "Sim. Só amizade.":


                    mc "Sim. Ela é só uma amiga mesmo."

                    $ thay_pega = False

                    jump thaynara_evento_amizade
                "Calma... deixa eu pensar...":


                    "Espera... tenho que pensar..."

                    jump thaynara_pega_escolha

    mc "Então... depois de fazer meu diagnóstico completo, eu cheguei a uma conclusão sobre sua condição..."

    t "E o que é?"

    mc "Acontece que você e eu temos uma ligação. Uma ligação muito forte. E quando a gente tá perto você sente isso."

    t "Então é isso?"

    mc "Exatamente. Olha bem pra mim."

    t "Tá..."

    mc "Você é linda, [t]. Eu gosto muito de você. E eu gosto de pegar em você, igual a gente tá agora."

    t "[mc]!"

    scene thaynara_mc2 with Dissolve(1.0)

    pause

    t "P-por que você tá falando isso?!"

    mc "E aí? Você sentiu isso?"

    t "Ai, [mc]..."

    mc "Eu adoro passar a mão pelos seus braços assim... sua pele é tão macia..."

    t "Ah... {i}puf puf{/i}"

    mc "Posso pegar mais em você?"

    t "A-ah!"

    mc "Não é gostoso quando eu faço assim?"

    t "Eu não sei! E-eu! {i}puf{/i}"

    t "Isso é demais pra mim! E-eu! M-meu coração vai sair do meu peito, [mc]!"

    mc "Essa é a ligação que a gente tem, [t]. Isso é a mesma coisa que eu sinto por você."

    t "Verdade?!"

    mc "Sim. Você não vê? A gente só consegue sentir isso quando a gente tá juntos."

    mc "Essa coisa forte é a razão pra gente ficar assim. E agora que isso foi aberto, a gente precisa manter esse sentimento."

    mc "Se a gente parar isso agora, pode ter algum resultado horrível pra nós dois!"

    t "[mc]..."

    "{i}tling tling{/i}"

    mc "Opa. Um cliente."

    t "E agora?"

    mc "Eu vou voltar outra hora, ok? Daí a gente continua isso. Fica bem até lá."

    t "Tá... eu... vou sentir saudades..."

    mc "Eu também."

    scene black with dissolve

    "Quanta bosta que eu falei. Ainda não acredito que ela caiu nessa."

    "Eu posso fazer praticamente o que eu quiser com ela que ela vai engolir agora."

    "O que eu faço da próxima vez?"

    $ tempo += 1

    jump call_cidade

label thaynara_evento11:

    $ renpy.block_rollback()

    $ t_nome = "Thaynara"

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_11","thaynara","personagem")

    "Depois daquele papo de energia e não sei o quê a [t] tá na minha mão."

    "Hoje eu quero aproveitar um pouco mais disso. Quem sabe sentir melhor essa gostosa..."

    scene black with dissolve

    t "Oi, [mc]. Vo-"

    mc safado "Não quero perder tempo hoje. Deixa eu ir aí."

    scene thaynara_mc2 with Dissolve(1.0)

    pause

    t "Eu senti tanta saudade de você. Eu queria que você voltasse logo pra comprar alguma coisa."

    mc "E eu queria voltar logo também. E não tem nada a ver com compra. Eu só queria poder ver você, [t]."

    t "[mc]... a gente tem essa ligação, né?"

    mc "Isso aí. Agora, a gente precisa ir pro próximo nível."

    t "Como assim?"

    mc "Hoje eu quero sentir mais você. Não quero só pegar na sua mão, no seu braço. Eu quero sentir você mais perto."

    t "Isso é importante?"

    mc "Isso é muito importante pra garantir que a gente vai ficar bem."

    t "Tá. E o que eu faço?"

    mc "Você fica quietinha e deixa que eu salvo a gente."

    t "Ok... Obrigada..."

    scene black with dissolve

    mc "Vem aqui."

    scene thaynara_mc3 with Dissolve(1.0)

    pause

    t "A-ah... [mc]..."

    mc "Isso... deixa eu fazer minha análise aqui."

    t "Ah! Você tá muito perto... demais..."

    mc "Tem que ser assim. Eu tenho que pegar em você inteira, [t]. É o único jeito."

    t "Tá..."

    mc "Você é muito cheirosa, sabia?"

    t "Ai..."

    mc "Deixa eu sentir bem tudo."

    t "Eu tô... meio fraca, [mc]... e nas minhas pernas... o que você tá fazendo?"

    mc "Isso é normal."

    t "É?"

    mc "Eu só vou ter que examinar seu peito também. Pra garantir que você... não... é... vai ter um ataque."

    t "{i}puf puf{/i}"

    t "Ok. Eu tô pronta."

    window hide

    pause

    scene thaynara_mc4 with Dissolve(1.0)

    t "Ah!"

    mc "Hmmm..."

    t "[mc]! Ah! Isso é demais!"

    mc "Calma, é só o exame. Fica quietinha e vai ficar tudo bem. Aproveita."

    t "Ah! Quando você aperta meu peito, meu ar acaba! Ah!"

    mc "É assim mesmo!"

    t "Minha perna, não consigo parar ela!"

    mc "Você é uma delícia, [t]. Eu vou treinar você direitinho, viu?"

    t "Ah! Ai!"

    mc "Assim. Pode gemer."

    t "Ahh!"

    window hide

    pause

    mc "Isso só mais um pouco."

    "{i}tling tling{/i}"

    "O barulho da porta!"

    mc "C-com licença!"

    scene black with hpunch

    t "Ah..."

    mc "Eu volto outro dia, [t]."

    scene thaynara2 with Dissolve(1.0)

    t "Mas eu tô-"

    mc "Não termina essa frase! Não fala nada! Aguenta que eu volto outro dia!"

    t "Mas tava bom... eu acho... Não quero que pare."

    mc "Calma. Eu volto outro dia. Segura aí. Até!"

    scene black with dissolve

    "Uou... as coisas avançaram rápido hoje."

    "Se eu continuar assim, logo eu posso levar a [t] à loucura. E me divertir um pouco também claro."

    "Ela simplesmente não entende nada. Eu posso fazer o que eu quiser com ela."

    "Será que isso tá certo? Eu realmente devia fazer isso?"

    "Eu tenho que pensar com calma sobre isso antes de entrar de cabeça... de cabeça, entendeu? Eu sou um gênio."

    $ tempo += 1

    jump call_cidade

label thaynara_evento12:

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_12","thaynara","personagem")

    "Da outra vez eu quase fiz a [t] gozar só com meu 'exame'. Dessa vez eu pego ela."

    "Eu vou fazer ela ficar viciada no prazer até ela implorar pra eu examinar o problema dela."

    mc "Oi, Thay!"

    mc "[mc]... veio faz-"

    scene black with dissolve

    mc "Vem logo aqui."

    scene thaynara_mc3 with Dissolve(1.0)

    pause

    t "A-ah... [mc]... você veio analisar de novo?"

    mc "Isso."

    t "Que bom... e-eu tava com saudades da sua análise. Da outra vez foi muito bom."

    mc "Da outra vez a gente teve que parar na metade, mas hoje você vai ver o poder do amor.."

    t "Ai... o poder do amor, né?"

    mc "Eu vou beijar você, vou apertar você."

    t "Isso. Pode me apertar. Pode fazer o que você quiser. Eu adoro."

    mc "Isso é muito importante."

    t "E-eu sei! Você vai me salvar, né? Ah!"

    mc "Vou. Vou salvar você."

    t "{i}puf puf{/i}"

    scene thaynara_mc4 with Dissolve(1.0)

    pause

    mc "Agora é a hora do exame de verdade!"

    t "Ah!"

    mc "Fica quietinha e deixa eu salvar você!"

    t "Isso! Vai! Me salva!"

    mc "Sentir sua bunda roçando no meu pau é maravilhoso."

    t "Ai! Você tá apertando seu negócio na minha bunda! Ah!"

    mc "Tudo isso é preciso!"

    t "T-tá! Eu tô gostando! Me examina mais!"

    mc "Isso! Pode colocar pra fora! Aproveita que não tem ninguém aqui!"

    t "Tá! Ah! Isso! Me aperta! Passa a língua em mim! Minhas pernas tão pegando fogo, [mc]!"

    t "T-tá vindo! Eu sinto que tá vindo uma coisa!"

    mc "Isso! Deixa vir, [t]!"

    t "Aperta mais na minha bunda! Vai! Aperta!"

    scene thaynara_mc4 with hpunch

    t "Ah! Aaagh!"

    t "{i}puf puf{/i}"

    scene thaynara_mc5 with Dissolve(1.0)

    pause

    mc "E aí? Gostou?"

    t "E-eu... não sei o que aconteceu..."

    menu:
        "Isso foi um orgasmo.":


            mc "Você acabou de ter um orgasmo."

            t "E-eu nunca tinha sentido uma coisa assim... foi tão... intenso..."

            mc "Isso é muito bom. Você vai sentir saudades disso."

            t "Ai... eu tô até meio zonza, [mc]..."

            mc "Haha..."
        "Esse é o problema saindo do seu corpo.":


            mc "Isso foi as energias malignas do problema deixando seu corpo."

            t "N-nossa... f-foi bom..."

            mc "Pois é. Seu corpo comemorou a cura. Eu tenho certeza que ele vai querer mais logo."

            t "Você acha? Eu tô tão cansada agora..."

    mc "Da próxima vez que você me ver, você vai querer sentir isso de novo. Isso é normal."

    t "Hmm..."

    mc "Eu prometo que eu vou cuidar de você direitinho. Você vai se sentir muito bem na minha mão."

    t "T-tá... só não sei se isso vai ser bom. Eu gritei muito. E se vier alguém?"

    mc "Se vier alguém vai ser um problema. Mas aposto que logo logo você vai querer correr o risco."

    t "N-não... não pode..."

    mc "Quero ver o que você vai falar das próximas vezes."

    t "..."

    "{i}tling tling{/i}"

    t "Ah! Tem alguém vindo. É m-melhor você ir."

    mc "Ok... se você quer..."

    t "Eu quero! Vai. Atá l-logo."

    mc "Até a próxima, [t]."

    scene black with dissolve

    "Essa foi boa. Fazer ela gozar assim e sentir o prazer... vai ficar cada vez mais fácil de pegar nela desse jeito..."

    "Logo logo vai ser minha hora de aproveitar isso também."

    "Eu tenho que voltar aqui o mais rápido possível."

    $ tempo += 1

    jump call_cidade

label thaynara_evento13:

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_13","thaynara","personagem")

    "Conteúdo"



    $ tempo += 1

    jump call_cidade

label thaynara_eventoX:

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("thaynara_evento_11","thaynara","personagem")

    "Conteúdo"



    $ tempo += 1

    jump call_cidade



label thaynara_evento_amizade:

    $ thaynara_amizade = True

    mc "Sabe, Thay... eu não sou a melhor pessoa pra te falar isso. Eu sou só um cara normal, sabe?"

    mc "Certeza que seus pais ou quem cuida de você ou um psicólogo soubesse te explicar melhor tudo isso."

    t "É tão grave assim?"

    mc "Não. Não é nada grave. O que você tá sentindo é paixão. Só isso."

    t "Paixão? Tipo de... marido e mulher?"

    mc "É. Tipo isso."

    t "Nossa! Então é isso?!"

    mc "Esse arrepio, esse nervosismo que a gente sente quando tá perto de alguém e mesmo assim a gente gosta de ficar perto..."

    mc "Essa coisa louca que acontece na nossa cabeça, que a gente não sabe se gosta ou odeia, que fica encardido na cabeça e no coração."

    mc "Isso é paixão."

    t "Então... eu tô apaixonada por você?"

    mc "Olha... quem tinha que decidir isso era você... mas parece que você realmente não entende nada disso, né?"

    t "I-isso... é tão... difícil de acreditar, [mc]."

    mc "Como assim? Por quê?"

    t "É difícil de te explicar, [mc]... o que eu preciso saber é..."

    scene thaynara_mc2 with Dissolve(1.0)

    t "Você... Se for verdade... e eu tiver apaixonada... Você... também tá apaixonado por mim?"

    "Merda... era essa parte que eu queria fugir..."

    mc "Não."

    t "!!!"

    mc "Isso que você sente na barriga, no peito... essa falta de ar... eu não sinto isso com você."

    t "Ai... Por que tá doendo agora?"

    mc "Isso é tomar um fora... quando a gente gosta de alguém mas ela não gosta da gente igual."

    t "Então... tudo isso... É por que eu sou feia, [mc]?"

    mc "Isso não tem a ver com você, [t]. Não adianta ficar pensando no que você fez. Gostar de alguém depende de quem gosta."

    mc "Não adianta pensar muito nisso. Ainda mais quando a gente nem conhece o outro direito."

    mc "Tomar um fora dói. A gente fica triste, é normal. Mas é só a gente dar um tempo que logo essa coisa ruim passa."

    t "Mas aqui tá doendo ainda."

    mc "Sim. Não é rápido desse jeito haha... mas eu sei que você ainda vai encontrar a pessoa certa pra você."

    mc "Alguém que você sinta tudo isso e mais ainda. E ela também vai sentir por você. Eu tenho certeza."

    t "Você acha?"

    mc "Com certeza. Você... é uma pessoa única. É bonita, muito jovem ainda."

    t "Porque eu só posso voltar pra casa quando eu descobrir o meu amor verdadeiro..."

    mc "Hm?"

    t "Pelo menos agora eu sei como eu vou achar..."

    menu:
        "Certeza que você vai achar.":


            mc "Eu tenho certeza que você vai achar. Mais cedo do que você imagina."

            t "Você acha mesmo?"

            mc "Com certeza. Pode escrever o que eu tô falando."

            t "Tá."
        "Como assim você só pode voltar quando achar?":


            mc "O que você quer dizer com isso? Voltar pra casa só quando achar o amor?"

            t "É. Foi o que eu decidi."

            mc "Que tipo"

    t "Obrigada por ser sincero comigo, [mc]. Dói, mas eu não queria que você mentisse pra mim."

    t "Você podia voltar aqui daqui um tempo? Eu preciso pensar... e depois eu quero ser sincera com você também."

    mc "Ok... eu volto em breve então."

    t "Tá. Agora é melhor você ir."

    mc "Beleza. Fica bem, [t]. A gente se fala depois."

    scene black with dissolve

    "Que porra de conversa foi essa? Mas é melhor assim."

    "A [t] quer encontrar alguém legal que realmente gosta dela. Ela precisa ser forte agora que um dia vai aparecer."

    "Agora... o que será que ela quer falar comigo?"

    "Tenho que dar um tempo pra ela e voltar depois."

    $ tempo += 1

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
