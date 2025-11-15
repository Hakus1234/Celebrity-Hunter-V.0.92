label templo_passeio:

    "..."

    scene chinatown templo_lateral with Dissolve(1.0)

    pause

    "Uou. Este lugar é incrível."

    "Me dá uma paz vir aqui..."

    "Eu sinto uma certa paz. E também uma energia. Um tipo de pressão, como se eu tivesse de frente pra um gigante."

    if tempo == 1 and v17_fim and not fenju_treino:

        if fenju_evento == 0:

            $ fenju_treino = True
            $ fenju_evento += 1

            "{i}SWEPT!{/i}"

            mc desconfiado "Que barulho é esse?"

            "..."

            scene chinatown treino_fenju with Dissolve(1.0)

            pause

            mc surpreso "[fen]!"

            show treino_fenju fenju1 with dissolve

            pause

            show treino_fenju fenju2 with dissolve

            pause

            "Ela deve tá treinando..."

            "Não vou atrapalhar ela."

            show treino_fenju fenju3 with dissolve

            pause

            show treino_fenju fenju4 with dissolve

            pause

            if s5_ajudou:

                "Espero que ela teja bem depois daquele dia que a gente fugiu da Cidade Chinesa."

                "Se aquela treinadora descobriu de alguma forma, não quero nem pensar o que ela faria com a coitada."

                "Espero que ela fique bem."

        elif fenju_evento == 1:

            $ fenju_treino = True
            $ fenju_evento += 1

            "Será que a [fen] tá treinando hoje de novo?"

            scene chinatown treino_fenju with Dissolve(1.0)

            pause

            "Olha ela lá."

            show treino_fenju fenju5 with dissolve

            pause

            "Ela deve tá meditando... sozinha."

            "Não vejo nem a [s] e nem a treinadora com ela. Já é a segunda vez."

            "Eu queria poder fazer alguma coisa por ela."

            "Preciso pensar numa forma... Mas agora não dá."

            "Só posso torcer por ela por agora. Força [fen]!"

            "..."

        elif fenju_evento == 2:

            $ fenju_treino = True


            "Acho que a [fen] tá treinando de novo."

            "..."

            scene chinatown treino_fenju with Dissolve(1.0)

            pause

            mc envergonhado "Pra variar..."

            show treino_fenju fenju1 with dissolve

            pause

            show treino_fenju fenju2 with dissolve

            pause

            show treino_fenju fenju3 with dissolve

            pause

            show treino_fenju fenju4 with dissolve

            pause

            show treino_fenju fenju5 with dissolve

            pause

            "..."

            "..."

            "Pelo jeito ela vai ficar aí amanhã inteira."

            "Força, [fen]. E confie em mim. Eu ainda vou ajudar você e a [s]."

            "..."

        $ tempo += 1

        jump cenario_templo

    "Acho que é o peso do passado..."

    mc zerado "O que eu tô falando?"

    "Deixa eu voltar."

    if bao_evento == 4 and xiangu_evento == 2 and tempo == 3:

        scene chinatown templo_lateral with vpunch

        "{i}GATCHINK!{/i}"

        mc desconfiado "Hã?"

        "{i}SWEPT!{/i}"

        "Que barulho é esse? Parece que tá vindo do centro do templo."

        "Primeira vez, desde que eu vi a [s] treinando, que eu escuto alguma coisa além do vento."

        "..."

        mc surpreso "!"

        scene xiangu templo with Dissolve(2.0)

        pause

        "QuêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊêÊê?!"

        "É a [xu]!"

        window hide

        pause

        "O que ela tá fazendo lá em cima?"

        "Melhor... como ela foi parar lá em cima?"

        "Quanto mais eu vejo ela, menos a vida faz sentido..."

        "Pera! A marca nas costas!"

        "Preciso focar na imagem..."

        "Hmmm..."

        scene xiangu templo_close with Dissolve(2.0)

        pause

        "O que é aquilo?"

        "Não consigo ver direito. Tá longe e tá escuro..."

        window hide

        pause

        "Parece uma flor..."

        "Essa flor... o que será que ela quer dizer?"

        "O [chi] disse que é a marca de quem foi tocado pelos deuses. Mas pra mim parece uma tatuagem como qualquer outra."

        "Eu preciso saber mais sobre essa flor..."

        if xiang_flor:

            "Calma!"

            "Essa flor... É a mesma flor que tem nas costas daquela [i] eu acho..."

            "Não tenho certeza... mas parece bastante..."

            "Será que elas tão ligadas de alguma forma? Eu preciso falar com aquela [i] no Distrito."
        else:


            "Se o [chi] não sabe sobre ela, então não adianta eu perguntar pra pessoas da Cidade Chinesa."

            "Talvez alguém de {b}outro lugar{/b} saiba. Alguém que esteja ligado ou ligada a coisas obscuras."

            "Quem sabe até alguém que {b}seja chinês, mas não viva na Cidade Chinesa{/b}."

            "Hmmm..."

        "Não adianta eu ficar aqui. É melhor eu sair daqui antes que ela me veja."

        scene black with dissolve

        "..."

        $ xiangu_evento = 3
        $ xiangu_flor = True
        $ tempo += 1

        jump call_cidade

    elif xiangu_evento == 3 and tempo == 3 and dia < dia_xiangu:

        "Opa..."

        scene xiangu templo with Dissolve(2.0)

        pause

        "A [xu] tá aqui de novo..."

        "Mas eu acabei de ver ela lá no portal... como ela já tá aqui?"

        "E o que raios ela tá fazendo ali em cima?"

        mc desconfiado "..."

        "Preciso descobrir alguma coisa sobre a tatuagem nas costas dela."

        if xiang_evento < 4:

            "Tenho que encontrar um chinês que viva fora da Cidade Chinesa... sinto que esse é o caminho..."
        else:


            "Eu conversei com a [i] e ela disse que a história da [xu] é falsa."

            "Eu preciso dar um jeito de fazer a [xu] confessar essa mentira, mas não tenho como fazer isso agora."

            "Vou ter que pensar em um jeito e volto aqui depois."

            show black with dissolve

            p rindo "A história da [i], [xu], [chi] e da Liling continua nas próximas atualizações."

            p "Fique de olho nas nossas redes sociais para saber quando a história continua."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("final_china_xiangu","xiangu","personagem")

            hide black with dissolve

        "Tá tarde. Deixa eu voltar pra ilha."

        $ tempo += 1

        jump call_cidade

    $ tempo += 1

    jump cenario_templo

label bao_historia:

    mc normal "Eu queria saber mais sobre a Cidade Chinesa."

    chi "Este velho viveu tempo demais aqui. Mas talvez seja cedo demais para você saber certas coisas, jovem."

    mc envergonhado "Entendo."

    chi "E o que você quer saber?"

    menu:

        "O que você pode me falar sobre He Xiangu?" if xiangu_evento == 2 and bao_evento == 2:

            mc desculpa "É... você sabe algo sobre a He Xiangu?"

            chi "Você diz... a lenda da imortal He Xiangu?"

            mc normal "Isso."

            chi "Hmmm..."

            "O que será que ele tá pensando?"

            chi "Bom... esse é um assunto delicado."

            python:
                if renpy.android:
                    bao_pontos = PythonSDLActivity.pegaBao()

            if bao_pontos >= 5:

                chi "Mas depois de todos esses dias trabalhando juntos, você conquistou minha confiança."

                mc feliz "..."

                chi "Você deseja que eu conte a história toda dela?"

                mc envergonhado "Não exatamente. Acho que essa parte eu posso pesquisar na biblioteca."

                mc "Eu queria que você me falasse mais sobre a He Xiangu que vive aqui na Cidade Chinesa."

                chi "A jovem do portal de pedra..."

                mc charmoso "Isso mesmo."

                chi "..."

                chi "Você pelo jeito está passando tempo demais neste lugar, [mc]."

                chi "Foi a [li] que te falou sobre ela, não foi?"

                mc normal "Sim. Eu tenho visitado o banho dela, e me interessei sobre toda essa história."

                chi "Então... qual a SUA opinião sobre o que descobriu?"

                mc envergonhado "Com todo respeito a [li] e até a garota espadachim... mas pra mim não passa de conversa pra boi dormir."

                mc desconfiado "Como é possível que aquela jovem seja realmente a verdadeira [xu] da lenda? Que vive há milhares de anos..."

                show bao pensando with dissolve

                chi "..."

                chi "Você é um jovem cético e inteligente. É natural que você tenha essa reação."

                chi "Só que as coisas não são tão simples."

                mc "Pra mim certas coisas são bem simples. É óbvio que ela tá enganando os moradores daqui."

                chi "..."

                show bao falando with dissolve

                chi "Você ainda não conhece como a Cidade Chinesa funciona. Existem grandes poderes em movimento. Um poder benevolente, mas opressivo."

                mc serio "O que isso quer dizer?"

                chi "{b}Os Oito Imortais{/b}."

                mc desconfiado "O-oito... imortais?"

                chi "Exatamente. Os Oito Imortais são um grupo de pessoas de alto renome na Cidade Chinesa. A [xu] que você conheceu faz parte desse círculo."

                chi "Eles estão no comando de todo o bairro desde a fundação da capital. Eles foram os primeiros, os fundadores da Cidade Chinesa."

                chi "E continuam comandando o lugar desde então, passando o poder de geração a geração dentro do grupo. Ninguém entra, ninguém sai."

                mc serio "E a garota do portal recebeu como herança um lugar nesse círculo de poder."

                show bao pensando with dissolve

                chi "Na verdade, é dito que essa 'garota' é uma das fundadoras da capital."

                mc surpreso "Quê?!"

                chi "Eu sei que você não acreditará no que estou dizendo, mas tudo indica que a garota que você viu no portal é a verdadeira [xu]."

                mc envergonhado "Não é possível que você acredite nisso, [chi]..."

                show bao normal with dissolve

                chi "Eu acredito no que meus olhos podem ver e meus ouvidos podem ouvir."

                chi "Mas, como lhe disse, é mais complicado do que você imagina."

                show bao pensando with dissolve

                chi "Acho que está bom por hoje."

                chi "Continuaremos a história dela uma outra hora."

                mc triste "Mas-"

                chi "Sem 'mas'. Eu tenho lámen para preparar. Continue me ajudando e conversamos mais uma outra hora."

                mc desculpa "Ok... E obrigado por toda a explicação."

                chi "Não há o que agradecer. Com licença."

                hide bao with dissolve

                "Hmmm... então até mesmo o [chi] acredita nessa história de [xu]..."

                "Será que essas pessoas receberam uma lavagem cerebral? Porque não é possível..."

                "Tenho que continuar ajudando ele com os lámens. E preciso continuar vendo a [li] no banho se eu realmente quiser chegar ao fundo disso."

                $ dia_bao = dia + 1
                $ bao_evento = 3

                jump chinatown_lamen
            else:


                show bao pensando with dissolve

                chi "Você ainda não está pronto pra esta conversa, jovem."

                mc preocupado "Só que e-"

                chi "Sem 'mas'. Trabalhe mais e podemos conversar sobre isso uma outra hora."

                mc desculpa "Certo..."

                "Droga... O [chi] ainda não confia em mim o suficiente pra revelar o segredo da [xu]."

                "Preciso continuar ajudando ele na preparação dos lámens e talvez ele confie em mim cada vez mais."

                "Eu tenho que chegar ao fundo dessa história."

                "{b}Você precisa atingir 5 pontos de confiança com o [chi] para liberar o resto da história{/b}"

                jump bao_menu

        "Eu sei que a [xu] tem um segredo. E o senhor sabe muito bem." if banho_evento == 6 and bao_evento == 3:

            mc serio "[chi], eu achei que você tivesse me contado tudo o que sabia sobre a [xu]."

            mc "Mas você escondeu um fato. Uma informação importante sobre ela. Por que?"

            show bao pensando with dissolve

            chi "..."

            python:
                if renpy.android:
                    bao_pontos = PythonSDLActivity.pegaBao()

            if bao_pontos >= 15:

                chi "Sua curiosidade não tem limites mesmo..."

                mc envergonhado "..."

                chi "Eu sabia que uma hora você chegaria nisso. Só não imaginei que seria tão rápido."

                chi "Bom..."

                show bao falando with dissolve

                chi "Realmente, eu omiti um detalhe sobre a [xu] quando conversamos da outra vez."

                mc triste "Por que?!"

                chi "Você estava apenas começando na arte de preparar o lámen e... perdão por falar assim... mas eu ainda não tinha confiança em você."

                mc desculpa "..."

                chi "Não me leve a mal, [mc]. Você está entrando em um território muito perigoso. Um verdadeiro vespeiro."

                chi "É como revirar um baú velho cheio de facas. Cedo ou tarde você acabará cortando os dedos."

                mc "Só que eu tô pronto. Eu quero saber mais sobre tudo isso."

                chi "..."

                chi "Escute bem."

                scene bao mc_conversando with Dissolve(2.0)

                pause

                chi "A garota que protege o portal de pedra, no pé do monte Penglai, possui uma marca em suas costas."

                chi "Uma marca única, presente nos discípulos dos deuses. Somente os que foram {b}tocados pelos deuses{/b} possuem essa marca."

                mc "Tocados pelos deuses... O que isso significa?"

                chi "Estou falando no sentido literal. Apenas os que literalmente foram tocados pelos deuses e se tornaram imortais possuem essa marca."

                mc "De novo essa história de vida eterna..."

                chi "..."

                mc "E que marca é essa?"

                chi "..."

                mc "[chi]? Vai esconder isso de mim também?"

                chi "Eu..."

                chi "Não sei."

                mc "Quê?!"

                chi "Eu nunca vi. Na verdade, poucas pessoas viram. Realmente poucas."

                mc "Essa marca... é a pista que eu precisava. Mas se nem o senhor viu..."

                chi "Não desista antes de tentar, jovem."

                chi "Eu estou certo que você vai conseguir descobrir o que precisa, contanto que você não desista."

                mc "Obrigado pelo voto de confiança. Eu vou dar um jeito."

                chi "Eu sei que vai."

                mc "Depois venho te ajudar com os lámens, [chi]."

                chi "Volte mesmo. Este velho precisa de ajuda sempre que possível."

                mc "Até."

                chi "Zaijian."

                scene chinatown lamen with Dissolve(1.0)

                "Uma marca... nas costas dela. Eu preciso saber que marca é essa."

                "Essa é a única pista que eu tenho. É isso ou desistir. E depois do que o [chi] disse, eu não vou arregar."

                "Seja o que for... eu sei que tem algo a ver com o {b}Templo{/b}. Tudo gira em torno disso."

                "A [xu] fica no portal de pedra o dia todo, mas ela é uma espadachim, samurai, ninja, que seja... Ela precisa treinar e, pelo que a [s] contou, elas treinam no templo."

                "Talvez eu deva {b}visitar o templo em vários horários{/b} e ver se eu encontro algo sobre ela."

                mc serio "Eu vou dar meu jeito. Espere e veja, fake [xu]."

                $ dia_bao = dia + 1
                $ bao_evento = 4

                jump chinatown_lamen
            else:


                show bao pensando with dissolve

                chi "Você ainda não conquistou esse direito, [mc]."

                mc preocupado "Só que e-"

                chi "Sem 'mas'. Trabalhe mais, aprenda mais a arte do lámen e podemos conversar sobre isso uma outra hora."

                mc desculpa "Certo..."

                "Droga... O [chi] ainda não confia em mim o suficiente pra revelar tudo o que ele sabe sobre a [xu]."

                "Preciso continuar ajudando ele na preparação dos lámens e talvez ele confie em mim o suficiente."

                "Eu tenho que chegar ao fundo dessa história."

                "{b}Você precisa atingir 15 pontos de confiança com o [chi] para liberar o resto da história{/b}"

                jump bao_menu

        "Eu ouvi a [li] e a [ka] discutindo. Você pode me falar sobre elas?" if banho_evento == 9 and bao_evento == 4:

            mc desculpa "Eu queria saber mais sobre a [li] e a [ka]."

            chi "Por que elas?"

            mc "A garota... a [ka]... ela tava me dando algumas dicas sobre a questão da [xu]. Só que ela e a [li] brigaram e agora não posso mais falar com ela."

            chi "Entendo... e você quer se intrometer nessa história também?"

            mc envergonhado "..."

            chi "..."

            python:
                if renpy.android:
                    bao_pontos = PythonSDLActivity.pegaBao()

            if bao_pontos >= 30:

                show bao falando with dissolve

                chi "[mc], você está entrando cada vez mais nesse buraco chamado Cidade Chinesa."

                chi "Esta é a segunda vez que eu vejo alguém de fora tentando se meter aqui. E a primeira vez não acabou bem."

                chi "Você tem certeza do que você tá fazendo?"

                mc zerado "Depois dessa ameaça quem pode ter certeza de qualquer coisa?"

                chi "Não veja como uma ameaça, mas como um alerta de alguém que se preocupa com você."

                mc desculpa "Eu sei. Malz, [chi]. Mas é que eu realmente quero chegar ao fim de tudo isso."

                mc "Eu sinto que desvendar essa história vai me ajudar de várias formas."

                chi "O que tem nisso pra você?"

                mc "Primeiro que é meu trabalho como paparazzo descobrir essas coisas e depois publicar na revista. Preciso de todas as pautas que eu puder."

                mc charmoso "E segundo que eu acho que vou entender melhor a situação da [s], da [fen] e talvez até da [i] e da [xu]."

                show bao pensando with dissolve

                chi "Esse seu jeito, [mc]... de pensar nos outros, ainda pode trazer um destino inesperado para você."

                mc normal "Surpresas são boas, não são?"

                chi "Nem todas."

                mc preocupado "..."

                chi "Mas se é o que você deseja, eu posso te ajudar."

                scene bao mc_conversando with Dissolve(2.0)

                chi "A [li] nasceu e cresceu na Cidade Chinesa. Ela conquistou um excelente renome entre a comunidade do bairro, principalmente por trazer pessoas de fora pra cá."

                mc "Como assim 'de fora'?"

                chi "Pessoas de toda a capital vêm aproveitar as maravilhas do banho de saúde e beleza. Nosso bairro ficou mais conhecido graças a ela."

                mc "Eu não pensei que a [li] era vista de uma forma tão positiva assim."

                chi "Mas ela é. Muito mais do que eu e de que a grande maioria dos chineses."

                mc "Ela é uma {b}escolhida{/b}?"

                chi "Não, não. A [li] é tida em alta estima, mas perante os cidadãos comuns da Cidade Chinesa. Os escolhidos estão em uma categoria própria."

                mc "E o que são esses escolhidos?"

                chi "Não estamos aqui para falar deles, estamos?"

                mc "Acho que não..."

                chi "Vamos deixar isso para outra oportunidade. Enfim..."

                chi "A [li], por esse motivo, acabou ganhando alguns privilégios. E um desses 'privilégios' foi a [ka]."

                mc "Privilégio?"

                chi "Obviamente você reparou que a [ka] não é chinesa."

                mc "V-verdade..."

                chi "A relação delas é muito mais complexa do que uma relação familiar ou de amizade ou até mesmo profissional."

                chi "A ligação delas representa o que tem de mais obscuro, não apenas na Cidade Chinesa, mas em toda a capital."

                chi "A guerra entre as facções está presente desde os maiores eventos até os mais triviais, como a relação das duas."

                mc "Guerra... das facções..."

                chi "Lembre-se sempre disso, [mc]. Essa é a essência da sua ilha e da capital como um todo. Tudo gira em torno de poder e influência."

                chi "A [li] e a [ka] são apenas mais duas peças nessa grande máquina que move a cidade."

                chi "Continue indo nos banhos, desvende tudo o que puder sobre elas, e você entenderá melhor não apenas a Cidade Chinesa, como tudo que acontece por aqui."

                chi "Mas tome cuidado. Tome cuidado com as engrenagens que você irá mexer."

                chi "Essa máquina opera por muitos anos, décadas, talvez até séculos e pará-la não é tarefa para uma pessoa. Você não é um herói e nem tem que ser."

                chi "Lute pelos que você ama e com certeza você terá feito sua parte no grande esquema das coisas."

                chi "..."

                scene chinatown lamen with Dissolve(1.0)

                mc desconfiado "É isso?"

                show bao pensando with dissolve

                chi "Sim."

                mc zerado "Mas você não me falou nada de concreto..."

                chi "Apenas uma parte da vida é concreta, [mc]. O essencial é invisível aos olhos."

                mc angustiado "Mas!"

                show bao soco with dissolve

                chi "Força! Energia e força de vontade são essenciais! Não desista agora!"

                mc concentrando "Droga..."

                chi "E não esqueça de continuar trabalhando comigo. Temos muito ainda que servir nesta vida."

                mc "Pode deixar..."

                chi "Pense nisso tudo e venha falar comigo quando precisar de algo."

                mc normal "Ok. Muito obrigado, [chi]."

                hide bao with dissolve

                "Esse velho... ele deve ter feito curso com o mestre dos magos..."

                "Não vai ter jeito. O único jeito agora é esperar a [li] se resolver com a [ka]."

                "De vez em quando vou dar uma passada no banho e ver se tem algo de diferente. Mas por hora é isso."

                "Não tem mais nada que eu possa fazer a não ser esperar por elas."

                "Mas óbvio que não vou desistir. Mesmo estranhas, as palavras do [chi] falaram sobre algo muito importante."

                "Sobre essa guerra. Eu preciso entender isso muito bem."

                mc bravo "Força, [mc]!"

                $ dia_bao = dia + 1
                $ bao_evento = 5

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("cidade_chinesa_v2_fim","bao","personagem")

                jump chinatown_lamen
            else:


                show bao pensando with dissolve

                chi "Você ainda não está pronto, [mc]."

                mc preocupado "Só que e-"

                chi "Sem 'mas'. Trabalhe mais, aprenda mais a arte do lámen e podemos conversar sobre isso uma outra hora."

                mc desculpa "Certo..."

                "Droga... O [chi] ainda não confia em mim o suficiente pra revelar o que ele sabe sobre a [li] e a [ka]."

                "Preciso continuar ajudando ele na preparação dos lámens e talvez ele confie em mim o suficiente."

                "Eu tenho que chegar ao fundo dessa história."

                "{b}Você precisa atingir 30 pontos de confiança com o [chi] para liberar o resto da história{/b}"

                jump bao_menu

        "Eu descobri que a [ka] foi vendida. Eu quero salvar ela!" if banho_evento == 14 and bao_evento == 5:

            mc serio "Eu descobri tudo sobre a [ka]. Foi ela mesma que contou. Ela foi vendida pra [li]. E tráfico de pessoas é crime!"

            chi "Então finalmente você entendeu a gravidade da relação das duas... e por que isso toca no pior ponto da Cidade Chinesa."

            mc "Agora eu quero salvar ela! Ela tá se prostituindo pra juntar dinheiro, [chi]! Pra pagar e deixar de ser uma escrava!"

            chi "Isso é frustrante e eu vejo sua fúria, jovem. Mas, como eu disse. As coisas não apresentam apenas um lado."

            mc irritado "Eu cansei dessas charadas! Fala logo como eu salvo ela!"

            python:
                if renpy.android:
                    bao_pontos = PythonSDLActivity.pegaBao()

            if bao_pontos >= 45:

                show bao pensando with dissolve

                chi "Muito bem... você trabalhou comigo tempo suficiente para entender a arte do lámen."

                mc zerado "Ok... lámen... pode pular essa parte."

                chi "Tenha calma, [mc]. Cada coisa a seu tempo. Respire três vezes antes de cotinuarmos."

                mc concentrando "..."

                mc concentrando ".."

                mc concentrando "."

                chi "Melhorou?"

                mc desculpa "Só fala logo... a [ka] continua sendo abusada pela [li]... e tem a [i] também."

                mc "E eu sei que é o mesmo que acontece com a [s] e a Fen Ju. Todos estão envolvidos nesse mesmo bolo horrível."

                chi "Exatamente. Eu te ensinei tudo o que podia sobre fazer lámen. E agora você precisa usar esse conhecimento."

                mc desconfiado "Como?"

                chi "Como você irá usar esse conhecimento é sua tarefa descobrir. Mas eu estou certo que você entenderá na hora certa."

                mc zerado "Você tá me enrolando de novo..."

                mc irritado "Eu vim com um pedido bem específico! Eu quero saber da [ka]!"

                chi "Muito bem. Vamos falar sobre isso também. Escute."

                scene black with dissolve

                scene bao mc_conversando2 with Dissolve(1.0)

                chi "Você é um verdadeiro paparazzo. Descobriu um dos maiores segredos da Cidade Chinesa. A ligação dela com o tráfico."

                mc serio "Eu só me aproximei da [ka]. Ela me contou."

                chi "E esse é seu poder, [mc]. Do seu jeito, você penetra o coração das pessoas e elas se sentem seguras e protegidas."

                chi "E esse é um poder que vem com uma grande responsabilidade."

                mc "Q-que responsabilidade?"

                chi "Quando alguém te conta algo, ainda mais segredos obscuros da alma, elas colocam em você um peso."

                chi "Carregar esse peso é a responsabilidade de quem ouve o segredo. Você entende?"

                mc preocupado "E o que o senhor acha que eu devo fazer com isso?"

                chi "Fazer ou não fazer? Salvar ou não salvar? Essa é sua responsabilidade. Saber o que fazer com o peso."

                chi "Mas não esqueça de uma coisa. Sempre coloque a pessoa que te contou em primeiro lugar, ou seja, na sua frente."

                chi "Segredos revelados não devem ser usados em benefício de quem ouviu, pois podem ser a última lágrima de quem contou."

                mc "..."

                chi "Portanto, se você se lembrar deste preceito, tenho certeza que você fará a coisa certa."

                mc desconfiado "Então... colocar a pessoa na frente. Pensar sempre primeiro nela. E não pensar primeiro em mim. É isso?"

                chi "Se é o que você aprendeu com minhas palavras, então é pra isso que elas existiram."

                mc zerado "Caralho... nem pra confirmar o baguio."

                scene bao mc_conversando3 with Dissolve(1.0)

                chi "Agora, você se lembra quando falamos sobre 'o chinês fora da Cidade Chinesa'?"

                mc normal "Sim. A [i]. Eu encontrei ela. Eu queria poder ajudar ela também. Ela também foi... nossa..."

                chi "Era o que eu queria que você percebesse. O triângulo passa por elas. E ainda tem mais uma."

                mc desconfiado "Mais uma?"

                chi "O triângulo precisa de três lados e três pontas. Qual será a terceira?"

                mc preocupado "Hmmm..."

                chi "Preste atenção, pois serei direto com você agora. Como você sempre pediu."

                mc "S-sim."

                chi "Para salvar a [ka] você precisa destruir o feitiço que recai sobre a Cidade Chinesa."

                mc zerado "Feitiço? De novo isso?"

                chi "Exatamente. Feitiço extremamente poderoso e duradouro, que perdura milhares de anos."

                mc serio "Eu não acredito em magia."

                chi "[mc]... eu sou um velho sábio. Eu vi e vivi muito nesta vida. E lhe garanto que você não é o mais inteligente."

                mc zerado "Como é?"

                chi "Achar que seus olhos viram tudo e sua mente apreendeu tudo é um erro por diversos motivos. Esteja aberto para o desconhecido."

                chi "Antes de me tornar um cozinheiro, meu nome era Zhang Guolao e eu aconselhava os Escolhidos."

                mc surpreso "Q-quêÊ?!"

                chi "Você já devia ter uma ideia sobre isso. O que interessa, entretanto, é que eu deixei aquela vida. Eu sou outro hoje."

                chi "Mas eu sei coisas que mais ninguém sabe. Ainda mais sobre esse o feitiço da Cidade Chinesa."

                chi "Um feitiço que favorece os interesses de um seleto grupo de pessoas. Que se beneficiam desse segredo."

                mc desculpa "Certo. Mas o que isso tem a ver comigo?"

                chi "Para romper esse feitiço de todos, você precisa romper o elo na base da corrente. O elo que mantém a corrente."

                chi "Você precisa levar a luz aos olhos daquela que mantém todos enfeitiçados por milhares de anos."

                chi "Se ela ver o reflexo da verdade, todos vão ver com ela e assim a Cidade Chinesa estará livre para sempre do feitiço."

                chi "Você entendeu sua missão?"

                menu:
                    "Eu entendi. Vou quebrar o feitiço.":


                        mc charmoso "Claro! Eu vou quebrar esse feitiço e salvar a [ka], a [s] e todos da Cidade Chinesa!"

                        chi "Muito bem. Energia você tem, só precisa saber agir."

                        mc "Pode deixar."
                    "Claro que não. Entendi foi nada!":


                        mc zerado "Claro que não. Até agora eu não acredito que exista um feitiço de verdade."

                        chi "Não perca tempo com as pequenas coisas. Foque no que importa. Que é salvar quem você quer salvar."

                        mc desculpa "O-ok..."

                chi "Você precisa trazer a chinesa de fora de volta para dentro. E colocar frente a frente realidade e reflexo."

                chi "Apenas a verdadeira poderá fazer o que ela pode fazer. O reflexo não existe, portanto não consegue."

                mc desconfiado "Chinesa de fora pra dentro. Você tá falando de trazer a [i] de volta. Ok... mas como eu faço isso?"

                chi "Essa é sua missão, não a minha. O meu dever eu fiz. Eu te preparei para este momento."

                chi "Use o que eu te ensinei e salve a todos, [mc]. Cumpra o destino que lhe foi reservado."

                mc surpreso "A-ah..."

                chi "Agora vá. Reflita e coloque tudo em prática."

                mc "T-tá. Até."

                chi "Zaijian."

                scene black with dissolve

                scene chinatown lamen with Dissolve(1.0)

                "Caraca... o [chi]... acho que esse nem é o nome dele... vomitou um monte de coisa agora."

                "Teve lição de moral, informações úteis, história, fantasia... mano... esse cara tinha que escrever um livro."

                "Mas agora eu sei o que eu tenho que fazer. Eu tenho que tirar a [i] do Distrito e trazer ela de volta."

                "Reflexo... colocar de frente... acho que eu entendi o que ele quis dizer. Eu preciso juntar elas."

                "Se tem alguém lá no Distrito que pode me ajudar com isso é a Celeste."

                "Ela já me ajudou com uma pauta e eu sei que ela tá de olho em cacoalhar as coisas. Eu acho que eu posso confiar nela."

                "Se ela não tivesse do meu lado ela não ia entregar a pauta do diretor do banco. Além de que é a única pessoa lá dentro que eu confio de verdade."

                "Nem o Black Cash... ele é amigo demais da [nora] que aprisiona a [i]. Ele nunca ia me ajudar a tirar ela de lá."

                "Então é isso. A Celeste... eu preciso ir lá um dia que ela tiver. E evoluir as coisas com ela até eu poder falar com ela."

                "Certeza que vai dar alguma merda. Certeza..."

                $ dia_bao = dia + 1
                $ bao_evento = 6

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("cidade_chinesa_055_fim","bao","personagem")

                jump chinatown_lamen
            else:


                show bao pensando with dissolve

                chi "Eu não confio em você ainda pra isso, [mc]."

                mc irritado "Q-quê?!"

                chi "Não interessa quanto isso te afetou, eu não me importo com seu sofrimento. Eu não confio em você."

                mc zerado "F-falando na lata assim?"

                chi "Nossa relação supera as trivialidades da boa vizinhança. Serei direto com você."

                mc serio "M-mas..."

                chi "Continue fazendo lámens e aprenda que até as atividades mais mundanas podem guardar grandes experiências."

                "Droga... O [chi] ainda não confia em mim o suficiente..."

                "Preciso continuar ajudando ele na preparação dos lámens até ele me contar a verdade sobre elas."

                "Eu preciso descobrir como salvar a [ka]!"

                "{b}Você precisa atingir 45 pontos de confiança com o [chi] para que ele conte o segredo{/b}"

                jump bao_menu
        "Não tenho nada pra perguntar agora.":


            mc envergonhado "Pensando bem, não tenho nada pra perguntar agora hehe..."

            chi "Quando tiver algo que queira saber sobre a Cidade Chinesa, por favor me pergunte."

            chi "Mas você ainda não tá pronto pra saber sobre tudo o que acontece aqui."

            mc normal "Entendo."

            chi "Me ajude com o lámen e fale com outros moradores e você vai conhecer mais sobre este incrível bairro."

            mc "Com certeza."

            jump bao_menu

label chinatown_bao:

    $ chinatown_area = "bao"

    hide screen chinatown_tela

    if dia < dia_bao:

        "Eu já fui no carrinho de lámen hoje."

        "Amanhã eu volto lá se pá."

        jump chinatown_lamen

    show bao normal with Dissolve(1.0)

    chi "Olá, jovem."

    if not v11_fim:

        mc normal "Oi, senhor. Você vende comida aqui?"

        chi "O melhor lámen que você já comeu em sua vida. Uma experiência única por apenas C$ 20."

        "Quê?! C$ 20 por um miojo? Só pode tá brincando comigo..."

        mc envergonhado "Talvez numa próxima, beleza?"

        chi "Claro. Fique à vontade para vir quando quiser."

        mc normal "Valeu. Até."

        show black with dissolve

        p rindo "Olá!"

        p "Você precisa avançar na história da [sc] antes de poder saber mais sobre o senhor do lámen."

        if sayuri_evento1_check:

            p "Encontre a [s] no Templo e aprofunde sua relação com ela, sendo um bom amigo (ou talvez algo mais), e você saberá mais sobre esse senhor."
        else:


            p "Continue vendo a [s] e uma hora você poderá saber mais sobre esse senhor."

        p "Talvez ele até te chame pra cozinhar lámen com ele. Seria bem interessante, não acha?!"

        p "Bom jogo e boa sorte!"

        hide black with dissolve

        $ dia_bao = dia + 1

        jump chinatown_lamen

    if bao_evento == 0:

        chi "Como tem passado?"

        mc normal "Eu tô legal."

        chi "E como vai minha querida Ai Fen?"

        mc envergonhado "Acredito que bem também. A gente não se fala taaaanto."

        chi "Entendo. Mas saiba que ela gosta muito de você."

        mc "Como o senhor pode dizer isso?"

        show bao pensando with dissolve

        chi "Hmm... como é seu nome mesmo?"

        mc normal "[mcc]."

        chi "Então, [mc]. Quando a gente chega em uma certa idade, a gente olha para as pessoas e enxerga coisas que antes a gente não via."

        chi "Eu posso ver nos olhos da Ai Fen que ela nutre uma grande admiração e um grande carinho por você."

        mc envergonhado "A é?"

        chi "..."

        mc normal "Você com certeza tem um grande carinho por ela também. Você é alguma coisa dela?"

        show bao falando with dissolve

        chi "..."

        chi "Eu posso ver nos seus olhos que você é um bom jovem. E tem grande interesse em ajudar a Ai Fen."

        mc desconfiado "Como é?"

        chi "Só que as coisas não são simples."

        mc envergonhado "Não precisa falar desse jeito. Eu já sou um adulto."

        chi "..."

        show bao normal with dissolve

        chi "O que você acha de aprender a fazer lámen?"

        mc desconfiado "Como?"

        chi "Eu estou ficando velho e não tenho filhos que possam me ajudar. O que acha de aprender a arte de preparar o verdadeiro lámen?"

        "O rumo da conversa mudou completamente..."

        mc envergonhado "Não sei... é um pouco diferente de tudo o que eu planejei... sei lá..."

        chi "Pense o tempo que precisar e volte quando tiver uma resposta."

        chi "Aprender uma nova arte nunca é desperdício de tempo."

        mc "Ok. Até outra hora então, [chi]."

        chi "Até, [mc]."

        hide bao with dissolve

        "Hmm... trabalhar fazendo lámen... seria algo interessante até."

        "Se eu puder fazer quando eu puder, vai ser mais um bico."

        "E provavelmente eu conheceria mais o [chi] e também saberia mais sobre a Cidade Chinesa e talvez até sobre a [s]."

        "Vou pensar mais um pouco e depois eu respondo ele."

        $ dia_bao = dia + 1
        $ bao_evento = 1

        jump chinatown_lamen

    elif bao_evento == 1:

        $ bao_evento = 2

        mc normal "Oi, [chi]."

        mc "Eu pensei sobre sua proposta. E contanto que eu possa trabalhar somente quando eu tiver tempo, eu gostaria."

        chi "Sem problemas. Pode vir qualquer dia, nos {b}turnos da manhã ou da tarde{/b}."

        chi "O salário será pouco. Posso te pagar somente {b}C$ 1{/b} por lámen que você fizer perfeitamente. Se errar algum ingrediente não ganha."

        chi "Você ficará responsável por separar os ingredientes e então cozinhar tudo e montar na tigela."

        mc surpreso "Eu que vou cozinhar?!"

        show bao falando with dissolve

        chi "Obviamente, [mc]. Meu objetivo é que você aprenda a arte do preparo."

        chi "Enquanto você cozinha, eu atenderei os clientes, anotando os pedidos e levando os pratos que você preparar para eles."

        mc envergonhado "Se você acha que eu vou saber fazer, eu topo."

        show bao normal with dissolve

        chi "Perfeito. Agora eu vou te falar sobre os ingredientes e como preparar seu primeiro lámen."

        label bao_explicacao:

            chi "Vai daquele lado do carro. Vou te explicar sobre os ingredientes."

            mc normal "Ok."

            scene bao mc_lamen with Dissolve(1.0)

            chi "Se acostume com o local de trabalho. Existe uma grande tábua de madeira a sua frente, onde você irá cortar os ingredientes."

            chi "Do seu lado esquerdo fica o fogo, onde você poderá ferver água e cozinhar os ingredientes."

            chi "Mantenha a tábua sempre limpa e com espaço para preparar o próximo lámen."

            mc "Certo..."

            chi "Ok. Vamos começar com seu espaço de trabalho."

            chi "Limpe a tábua de preparo."

            mc "Ok. Pronto."

            $ renpy.choice_for_skipping()

            scene lamen_mesa with Dissolve(1.0)

            pause

            chi "Sua mesa está de acordo. Mantenha ela sempre em ordem."

            mc "Pode deixar."

            chi "Agora pegue uma tigela limpa e veja se ela está impecável. Na culinária, apresentação é tão importante quanto o sabor."

            mc "Opa. Achei aqui."

            show lamen_tigela with dissolve

            mc "Pronto."

            chi "É nessa tigela que você servirá o lámen pronto."

            chi "Agora vamos para os ingredientes."

            chi "O primeiro deles é o {b}Chasyu{/b}."

            mc desconfiado "Cha o quê?"

            $ renpy.choice_for_skipping()

            chi "{b}Chasyu{/b}. É uma tira de carne de porco preparada no churrasco. Pegue uma porção e coloque sobre a tábua."

            mc charmoso "Ok."

            show lamen_chasyu with dissolve

            mc normal "Assim?"

            chi "Exatamente."

            $ renpy.choice_for_skipping()

            chi "O próximo ingrediente que usamos é o {b}Men{/b}, que é o macarrão."

            chi "Pode separar ele na tábua."

            show lamen_men with dissolve

            mc normal "Aqui está."

            chi "Perfeito."

            chi "Agora, rapidamente, os outros três ingredientes são estes:"

            chi "{b}Naruto{/b}, que é uma pasta de peixe tratada."

            show lamen_naruto with dissolve

            pause

            chi "{b}Nitamago{/b}, ovo cozido especialmente para lámen."

            show lamen_nitamago with dissolve

            pause

            chi "E finalmente {b}Yakumi{/b}. Assim que chamamos as pequenas especiarias que darão sabor ao lámen."

            show lamen_yakumi with dissolve

            pause

            chi "Esses são os cinco ingredientes. Tudo certo até aqui?"

            mc envergonhado "É complicado gravar os nomes."

            chi "Não se preocupe que você vai pegar com o tempo. Não fique assustado."

            mc normal "Valeu."

            chi "Bom. Para adicionar os ingredientes, use os compartimentos que estão no lado direito da mesa."

            show lamen_exemplo with dissolve

            mc normal "Ah. Estou vendo aqui."

            chi "Eles estão na ordem {b}Chasyu{/b}, {b}Men{/b}, {b}Naruto{/b}, {b}Nitamago{/b} e {b}Yakumi{/b}."

            mc normal "Então o primeiro de cima é Chasyu e o último é o Yakumi. É isso?"

            chi "Muito bem."

            chi "Quando estiver cozinhando, eu vou te passar uma receita que vai pedir um número certo de cada ingrediente."

            chi "Daí é só colocar a quantidade como pedida na receita e então {b}Cozinhar{/b}. O resto é comigo."

            chi "Caso você tenha alguma dúvida, basta me perguntar."

            mc normal "Ok."

            scene chinatown lamen with Dissolve(1.0)

            show bao falando with dissolve

            chi "E é isso."

            mc normal "Muito obrigado pela aula."

            chi "É possível que seus primeiros lámens saiam com algo errado, mas prestando atenção muito em breve você pegará o jeito."

            chi "Não tenha medo de errar. Prática leva à perfeição."

            mc charmoso "Pode deixar comigo."

            if lamen_rever:

                $ lamen_rever = False

                return

            chi "Vá para casa e pense nisso. Amanhã você pode começar."

            mc normal "Ok. Não vejo a hora."

            chi "Até depois, [mc]."

            mc "Até, [chi]."

            $ dia_bao = dia + 1

            jump chinatown_lamen

    mc normal "Oi, [chi]. Como o senhor tá hoje?"

    chi "Vou bem, [mc]. Veio para escutar as histórias deste velho sobre a Cidade Chinesa ou para trabalhar?"

    label bao_menu:

        menu:
            "Trabalhar preparando lámen":


                "Tô louco pra ajudar o [chi] no carrinho de lámen."

                jump lamen_trabalho
            "Quero saber mais sobre a Cidade Chinesa":


                if bao_evento == 6:

                    chi "Tudo o que eu podia te ensinar eu te ensinei, [mc]."

                    chi "Você ganhou toda minha confiança e se mostrou um homem digno de interferir em nosso povo."

                    chi "Só espero que isso não seja demais pra você como foi para um certo alguém..."

                    if celeste_conversa < 3:

                        "Eu tenho que falar com a Celeste no Distrito agora, até eu ter uma ideia de como tirar a Xiang de lá."

                    elif xiang_escape == 6:

                        chi "Inclusive, você foi essencial pra coloca juízo na cabeça das duas garotas."

                        chi "Não apenas a protetora do portal, mas a antiga candidata também. Eu só tenho a lhe agradecer."

                    chi "Posso ajudar com mais alguma coisa?"

                    jump bao_menu

                jump bao_historia
            "Voltar outro dia":


                mc normal "Só vim dar um alô mesmo e ver se você tava bem."

                chi "Não se preocupe com este velho. Ainda tenho uma missão antes de deixar este mundo."

                mc charmoso "Um dia você vai me falar que missão é essa?"

                chi "Quem sabe... quem sabe..."

                mc normal "Até a próxima, [chi]."

                chi "Até, [mc]."

                $ dia_bao = dia + 1

                jump chinatown_lamen

    label lamen_trabalho:

        $ renpy.choice_for_skipping()

        call anuncio from _call_anuncio

        mc feliz "Pronto pra mais um dia de trabalho, [chi]!"

        $ renpy.choice_for_skipping()

        $ proibido_salvar = True
        $ show_quick_menu = False

        call checa_tempo from _call_checa_tempo

        $ renpy.choice_for_skipping()

        python:
            if renpy.android:
                tltempo = PythonSDLActivity.checkTLtempoNext()

        "..."

        if not tltempo:

            $ proibido_salvar = False
            $ show_quick_menu = True

            chi "Calma, [mc]. Eu falei para você descansar um pouco antes de voltar. Ainda não deu o tempo."

            mc envergonhado "É que eu tô ansioso."

            chi "Haha. Tenha calma, jovem. Tudo a seu tempo."

            mc "Ok..."

            show black with dissolve

            p rindo "O [mc] pode trabalhar uma vez a cada {b}3 horas do mundo real{/b}."

            p "Ou você pode liberar agora mesmo usando Celebrity Coins."

            python:
                if renpy.android:
                    persistent.coins = PythonSDLActivity.pegaMoedas(0)

            if persistent.coins >= 500:

                p "Liberar o trabalho no carrinho de lámen usará {b}500 Celebrity Coins{/b}."

                menu:
                    "Liberar trabalho":


                        python:
                            if renpy.android:
                                PythonSDLActivity.avancaTLTempo()

                        $ renpy.block_rollback()

                        play sound "extra/carta.mp3"

                        p "Você usou 500 Celebrity Coins para liberar o trabalho no carrinho de lámen."

                        p "Vou levar o [mc] para o passado para ele continuar os afazeres dele."

                        hide black with dissolve

                        $ renpy.block_rollback()

                        jump lamen_trabalho
                    "Agora não. Vou esperar o tempo.":


                        p "Ok!"

                        hide black with dissolve

                        jump bao_menu
            else:


                p lecionando "Você precisa de ao menos 500 Celebrity Coins para adiantar o trabalho."

                p rindo "Você pode comprar Celebrity Coins com dinheiro do {b}seu{/b} mundo."

                p "Assim você pode continuar a história agora mesmo e ainda colabora com o desenvolvimento de CH."

                menu:
                    "Ok. Quero comprar.":


                        "..."

                        call comprar_coins from _call_comprar_coins

                        p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                        hide black with dissolve

                        jump bao_menu
                    "A vida é dura. Tô sem grana pra isso agora.":


                        p rindo "Não tem problema."

                        p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais."

                        hide black with dissolve

            p rindo "Vá com calma que você vai conseguir ganhar o respeito do [chi]!"

            p "Use o app Relógio no celular do [mc] para ver quando o próximo turno de trabalho estará disponível."

            p "Até!"

            jump chinatown_bao

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("trabalho_lamen","bao","personagem")

        python:
            if renpy.android:
                PythonSDLActivity.setTLtempoNext()

        chi "Quanto entusiasmo..."

        mc feliz "Claro. Talvez eu tenha encontrado minha verdadeira vocação."

        chi "Haha! Então vamos ao trabalho!"

        $ pratos_preparados = 0
        $ lamen_certo = 0

        jump lamen_minigame

        label lamen_minigame:

            $ chasyu = 0
            $ men = 0
            $ naruto = 0
            $ nitamago = 0
            $ yakumi = 0

            hide screen lamen_tela

            scene lamen_mesa with Dissolve(1.0)

            if pratos_preparados < 3:

                if pratos_preparados == 0:

                    chi "Certo. Vou pegar os pedidos e levo nas mesas. Você prepara a comida. Pronto?"

                    chi "O primeiro cliente está vindo."
                else:


                    chi "Não dá pra descansar."

                    chi "Aí vem o próximo cliente."

                call escolhe_prato from _call_escolhe_prato

                chi "Ele vai querer um {b}[prato_escolhido]{/b}!"

                $ renpy.block_rollback()

                jump lamen_minigame_prato
            else:


                jump lamen_minigame_fim

            label lamen_minigame_prato:

                show lamen_tigela with dissolve

                call lamen_ingredientes from _call_lamen_ingredientes

                pause

            label lamen_minigame_fim:

                chi "Acabaram os clientes. É isso por hoje, [mc]."

                mc concentrando "Ufa..."

                scene chinatown lamen with Dissolve(1.0)

                if lamen_certo == 3:

                    show bao soco with dissolve

                    chi "Hoje você foi incrível, [mc]. Seus lámens ficaram perfeitos. Parabéns."

                    mc feliz "Obrigado, mestre."

                    chi "Continue com o bom trabalho."

                    mc "Pode deixar."
                else:


                    show bao pensando with dissolve

                    chi "Hoje seu trabalho não foi perfeito, [mc]. Você precisa manter a concentração."

                    mc desculpa "Desculpa, [chi]. Eu prometo que vou me esforçar."

                    chi "Lembre-se. Marque mentalmente quanto de cada ingrediente deve ter em cada lámen e daí coloque a quantidade correta."

                    chi "Preste atenção nas receitas e tome muito cuidado."

                    mc normal "Pode deixar. Vou melhorar a cada dia."

                    chi "Assim que se fala."

                mc normal "Mas e os próximos clientes do dia?"

                chi "Pode deixar que os próximos eu cuido sozinho. Graças a você eu dei uma boa descansada."

                mc "Beleza."

                label lamen_minigame_finalizar:

                    $ tl_cash = lamen_certo * 5
                    $ tl_moral = lamen_certo

                    python:
                        if renpy.android:
                            PythonSDLActivity.ganhaCash(tl_cash)
                            PythonSDLActivity.addBao(tl_moral)

                    $ renpy.block_rollback()

                    if lamen_certo > 0:

                        chi "Aqui está sua parte pelo trabalho de hoje."

                        show black with dissolve

                        play sound "extra/carta.mp3"

                        "{b}[mc] recebeu C$ [tl_cash]. A reputação com [chi] também aumentou em [tl_moral] pontos.{/b}"
                    else:


                        chi "Como hoje você não fez nenhum lámen da forma correta, não há o que eu te dar."

                        mc desculpa "Eu sei. Vou me esforçar mais nas próximas."

                        chi "Eu sei que vai."

                        show black with dissolve

                    "{b}É possível ajudar [chi] novamente daqui 3 horas. Use o app Relógio no celular para saber quando for a hora.{/b}"

                    $ proibido_salvar = False
                    $ show_quick_menu = True

                    $ renpy.block_rollback()

                    hide black with dissolve

                    mc charmoso "Beleza. Até a próxima, [chi]."

                    chi "Zaijian."

                    "..."

                    $ lamen_trabalhou += 1
                    $ tempo += 1
                    $ dia_bao = dia + 1

                    jump cidade_chinesa

    pause

label escolhe_prato:

    $ randlamen = renpy.random.randint(1,21)

    if randlamen == 1:

        $ prato_escolhido = "Sumimasen"
        $ chasyu_target = 1
        $ men_target = 2
        $ naruto_target = 2
        $ nitamago_target = 1
        $ yakumi_target = 1

    elif randlamen == 2:

        $ prato_escolhido = "Shio"
        $ chasyu_target = 0
        $ men_target = 4
        $ naruto_target = 2
        $ nitamago_target = 2
        $ yakumi_target = 3

    elif randlamen == 3:

        $ prato_escolhido = "Tonkotsu"
        $ chasyu_target = 4
        $ men_target = 3
        $ naruto_target = 1
        $ nitamago_target = 0
        $ yakumi_target = 2

    elif randlamen == 4:

        $ prato_escolhido = "Miso"
        $ chasyu_target = 1
        $ men_target = 1
        $ naruto_target = 4
        $ nitamago_target = 1
        $ yakumi_target = 0

    elif randlamen == 5:

        $ prato_escolhido = "Shoyo"
        $ chasyu_target = 3
        $ men_target = 1
        $ naruto_target = 4
        $ nitamago_target = 4
        $ yakumi_target = 4

    elif randlamen == 6:

        $ prato_escolhido = "Sapporo"
        $ chasyu_target = 2
        $ men_target = 3
        $ naruto_target = 3
        $ nitamago_target = 0
        $ yakumi_target = 4

    elif randlamen == 7:

        $ prato_escolhido = "Hakata"
        $ chasyu_target = 1
        $ men_target = 2
        $ naruto_target = 1
        $ nitamago_target = 4
        $ yakumi_target = 0

    elif randlamen == 8:

        $ prato_escolhido = "Kitakata"
        $ chasyu_target = 4
        $ men_target = 4
        $ naruto_target = 0
        $ nitamago_target = 3
        $ yakumi_target = 4

    elif randlamen == 9:

        $ prato_escolhido = "Wakayama"
        $ chasyu_target = 4
        $ men_target = 0
        $ naruto_target = 0
        $ nitamago_target = 2
        $ yakumi_target = 1

    elif randlamen == 10:

        $ prato_escolhido = "Onomichi"
        $ chasyu_target = 2
        $ men_target = 4
        $ naruto_target = 4
        $ nitamago_target = 0
        $ yakumi_target = 4

    elif randlamen == 11:

        $ prato_escolhido = "Nagoya"
        $ chasyu_target = 2
        $ men_target = 2
        $ naruto_target = 1
        $ nitamago_target = 2
        $ yakumi_target = 2

    elif randlamen == 12:

        $ prato_escolhido = "Okinawa"
        $ chasyu_target = 3
        $ men_target = 3
        $ naruto_target = 4
        $ nitamago_target = 4
        $ yakumi_target = 4

    elif randlamen == 13:

        $ prato_escolhido = "Hakodate"
        $ chasyu_target = 1
        $ men_target = 1
        $ naruto_target = 3
        $ nitamago_target = 3
        $ yakumi_target = 1

    elif randlamen == 14:

        $ prato_escolhido = "Kurume"
        $ chasyu_target = 4
        $ men_target = 1
        $ naruto_target = 3
        $ nitamago_target = 2
        $ yakumi_target = 4

    elif randlamen == 15:

        $ prato_escolhido = "Kagoshima"
        $ chasyu_target = 0
        $ men_target = 1
        $ naruto_target = 2
        $ nitamago_target = 3
        $ yakumi_target = 4

    elif randlamen == 16:

        $ prato_escolhido = "Nagasaki"
        $ chasyu_target = 4
        $ men_target = 3
        $ naruto_target = 2
        $ nitamago_target = 1
        $ yakumi_target = 0

    elif randlamen == 17:

        $ prato_escolhido = "Shoyo"
        $ chasyu_target = 3
        $ men_target = 1
        $ naruto_target = 4
        $ nitamago_target = 4
        $ yakumi_target = 4

    elif randlamen == 18:

        $ prato_escolhido = "Tsukemen"
        $ chasyu_target = 2
        $ men_target = 4
        $ naruto_target = 1
        $ nitamago_target = 3
        $ yakumi_target = 0

    elif randlamen == 19:

        $ prato_escolhido = "Tokyo"
        $ chasyu_target = 0
        $ men_target = 1
        $ naruto_target = 1
        $ nitamago_target = 0
        $ yakumi_target = 3

    elif randlamen == 20:

        $ prato_escolhido = "Asahikawa"
        $ chasyu_target = 4
        $ men_target = 4
        $ naruto_target = 4
        $ nitamago_target = 2
        $ yakumi_target = 4

    elif randlamen == 21:

        $ prato_escolhido = "Champon"
        $ chasyu_target = 0
        $ men_target = 1
        $ naruto_target = 0
        $ nitamago_target = 1
        $ yakumi_target = 0

    return

label lamen_ingredientes:

    hide screen lamen_tela

    "Pelo que eu me lembro, pro [prato_escolhido] a quantidade de cada ingrediente é a seguinte..."

    "Chasyu: [chasyu_target]"

    "Men: [men_target]"

    "Naruto: [naruto_target]"

    "Nitamago: [nitamago_target]"

    "Yakumi: [yakumi_target]"

    mc charmoso "Agora é fazer!"

    show screen lamen_tela

    pause

label lamen_cozinhar:

    hide screen lamen_tela

    "Eu separei [chasyu] Chasyu, [men] Men, [naruto] Naruto, [nitamago] Nitamago e [yakumi] Yakumi."

    if chasyu == 0 and men == 0 and naruto == 0 and nitamago == 0 and yakumi == 0:

        "Espera... eu não separei ingrediente nenhum..."

        mc zerado "O que eu tô fazendo?"

        show black with dissolve

        p rindo "Você precisa apertar nos botões do lado direito da tela na mesma proporção que a receita manda."

        p "Caso você não se lembre dos ingredientes, aperte o botão {b}Rever Ingredientes{/b}."

        p "Anote a quantidade correta de cada ingrediente e aperte no botão do ingrediente o mesmo número de vezes pedido na receita."

        p "Muito complicado? Talvez seja hora de começar a prestar atenção na escola."

        hide black with dissolve

        mc serio "Tenho que me concentrar e fazer um bom trabalho para impressionar o [chi]."

        show screen lamen_tela

        pause

    "Hmm... Cozinhar estes ingredientes?"

    menu:
        "Está certo. Cozinhar.":


            $ renpy.block_rollback()

            mc charmoso "A receita está certa. Vai ficar uma delícia."

            scene lamen_cozinhando at treme_vertical with dissolve

            $ renpy.pause(delay=3, hard=True)

            "Opa! Tá pronto."

            scene lamen_mesa with dissolve

            "Agora é só montar tudo no prato com muito cuidado."

            "Eeee...."

            show lamen_completo with Dissolve(1.0)

            pause

            mc feliz "Incrível!"

            mc "O [prato_escolhido] tá pronto, [chi]!"

            chi "Perfeito!"

            scene bao mc_lamen with Dissolve(1.0)

            chi "Obrigado, jovem. Pode me dar aqui que eu levo."

            chi "Um [prato_escolhido] saindo!"

            "..."

            $ renpy.block_rollback()

            if chasyu == chasyu_target and men == men_target and naruto == naruto_target and nitamago == nitamago_target and yakumi == yakumi_target:

                $ lamen_certo += 1

                "Eu acho que eu acertei em cheio nesse lámen!"
            else:


                "Pensando bem... tô com a impressão que errei alguma coisa nesse lámen."

            $ pratos_preparados += 1

            jump lamen_minigame
        "Espera... deixa eu ver melhor.":


            "Ixi. Agora não tenho certeza."

            "Só um segundo."

            show screen lamen_tela

            pause

label lamen_desistiu:

    hide screen lamen_tela

    "Não tô conseguindo colocar meu espírito no trabalho hoje..."

    menu:
        "Desistir do trabalho":


            $ renpy.block_rollback()

            "Não quero estragar tudo com o [chi]. Melhor não fazer do que fazer de qualquer jeito."

            "..."

            scene chinatown lamen with Dissolve(1.0)

            mc desculpa "Oi, [chi]. Queria avisar que hoje não tô conseguindo me concentrar. Acho que vou pra casa."

            show bao pensando with dissolve

            chi "Não se preocupe. Posso dar conta do movimento sozinho."

            mc "Obrigado."

            chi "Não tem por que agradecer. Você fez o certo."

            chi "É importante estarmos sempre em nosso melhor quando vamos atender alguém."

            chi "Pode ser que você sinta que está fazendo algo que não vale o esforço, como atender outras pessoas ou só fazer um lámen."

            chi "Mas todo trabalho dignifica o homem. Quando fazemos algo bem feito, não importa o quê, nosso espírito cresce."

            chi "Por isso, por mais banal e insignificante que você ache uma tarefa, sempre dê o seu melhor. O que importa está dentro de você."

            mc normal "Obrigado pela aula."

            show bao normal with dissolve

            chi "Haha. São só as bobagens de um velho."

            jump lamen_minigame_finalizar
        "Não posso desistir!":


            "Não posso desistir! Tenho que dar meu melhor!"

            show screen lamen_tela

            pause

label lamen_recomecar:

    hide screen lamen_tela

    $ chasyu = 0
    $ men = 0
    $ naruto = 0
    $ nitamago = 0
    $ yakumi = 0

    show screen lamen_tela

    pause

screen lamen_tela():
    tag lamen

    predict False
    zorder 100
    modal True

    if chasyu >= 0:

        if chasyu >= 1:

            add "lamen_chasyu.png"

        if chasyu >= 2:

            add "lamen_chasyu.png":
                xpos 50

        if chasyu >= 3:

            add "lamen_chasyu.png":
                xpos 100

        if chasyu >= 4:

            add "lamen_chasyu.png":
                xpos 150

        if men >= 1:

            add "lamen_men.png"

        if men >= 2:

            add "lamen_men.png":
                xpos 50

        if men >= 3:

            add "lamen_men.png":
                xpos 100

        if men >= 4:

            add "lamen_men.png":
                xpos 150

        if naruto >= 1:

            add "lamen_naruto.png"

        if naruto >= 2:

            add "lamen_naruto.png":
                xpos 50

        if naruto >= 3:

            add "lamen_naruto.png":
                xpos 100

        if naruto >= 4:

            add "lamen_naruto.png":
                xpos 150

        if nitamago >= 1:

            add "lamen_nitamago.png"

        if nitamago >= 2:

            add "lamen_nitamago.png":
                xpos 50

        if nitamago >= 3:

            add "lamen_nitamago.png":
                xpos 100

        if nitamago >= 4:

            add "lamen_nitamago.png":
                xpos 150

        if yakumi >= 1:

            add "lamen_yakumi.png"

        if yakumi >= 2:

            add "lamen_yakumi.png":
                xpos 50

        if yakumi >= 3:

            add "lamen_yakumi.png":
                xpos 100

        if yakumi >= 4:

            add "lamen_yakumi.png":
                xpos 150

    if chasyu <= 3:

        imagebutton auto "images/china/chasyu_%s.png":
            xalign 0.99
            yalign 0.04
            action SetVariable("chasyu", chasyu + 1)

    if men <= 3:

        imagebutton auto "images/china/men_%s.png":
            xalign 0.99
            yalign 0.23
            action SetVariable("men", men + 1)

    if naruto <= 3:

        imagebutton auto "images/china/naruto_%s.png":
            xalign 0.99
            yalign 0.42
            action SetVariable("naruto", naruto + 1)

    if nitamago <= 3:

        imagebutton auto "images/china/nitamago_%s.png":
            xalign 0.99
            yalign 0.61
            action SetVariable("nitamago", nitamago + 1)

    if yakumi <= 3:

        imagebutton auto "images/china/yakumi_%s.png":
            xalign 0.99
            yalign 0.80
            action SetVariable("yakumi", yakumi + 1)

    if chasyu == 0 and men == 0 and naruto == 0 and nitamago == 0 and yakumi == 0:

        imagebutton auto "images/china/desistir_%s.png":
            xalign 0.05
            yalign 0.95
            action Call("lamen_desistiu")

    else:

        imagebutton auto "images/china/recomecar_%s.png":
            xalign 0.05
            yalign 0.95
            action Call("lamen_recomecar")

    imagebutton auto "images/china/cozinhar_%s.png":
        xalign 0.46
        xanchor 0.5
        yalign 0.95
        action Call("lamen_cozinhar")

    imagebutton auto "images/china/ingredientes_%s.png":
        xalign 0.78
        xanchor 0.5
        yalign 0.95
        action Call("lamen_ingredientes")

label chinatown_portal:

    $ chinatown_area = "portal"

    hide screen chinatown_tela
    hide screen chinatown_tela2

    scene chinatown portal with Dissolve(1.0)

    pause

    if xiangu_evento == 0:

        "Este caminho não tem fim..."

        "Eu tô contornando o pé da montanha faz mais de uma hora e não chego em lug-"

        mc surpreso "Que isso?!"

        "Uma escada... e um portal de pedra. Parece um lugar abandonado."

        "Lá no topo eu consigo ver uma parede vermelha. Até que parece bem conservada olhando daqui."

        "Que lugar estranho."

        "Esta montanha deve ser a mesma que eu subo pra chegar no templo. Mas este caminho deve levar para outro lugar."

        "Já que eu tô aqui eu vou subir."

        mc concentrando "Deuses da China me deem seu poder pra aguentar mais alguns quilômetros..."

        "..."

        scene chinatown portal_xiangu with Dissolve(2.0)

        pause

        xu "Não."

        mc desconfiado "Quem diss-"

        scene chinatown portal_xiangu with hpunch

        mc surpreso "!"

        $ xu_nome = "Espadachim"

        xu "É proibido subir por este caminho."

        "Tem uma mina ali encima!"

        "Calma... é impressão minha ou ela tá com uma espada na cintura?"

        "Essa... ela é..."

        menu:
            "Espadachim":


                $ xu_nome = "Espadachim"
            "Samurai":


                $ xu_nome = "Samurai"
            "Ninja":


                $ xu_nome = "Ninja"

        "Só pode ser uma... [xu_nome]... Certeza!"

        mc normal "Olá. Meu nome é [mcc]. Muito prazer."

        xu "..."

        "Não vai facilitar as coisas aparentemente..."

        mc normal "O que tem no final desta escadaria? Aquele lugar com o paredão vermelho."

        xu "..."

        xu "Um local sagrado."

        mc desconfiado "Sagrado... E por que não posso visitar?"

        xu "Apenas os escolhidos podem visitar o {b}Jardim{/b}."

        "Jardim? Tudo isso aqui tá ficando mais louco quanto mais eu falo com ela. Vou voltar outra hora."

        mc normal "Ok. Obrigado. Até outra hora."

        xu "..."

        scene chinatown portal with Dissolve(1.0)

        "Tudo isso é muito estranho."

        "Eu sabia que esse povo da Cidade Chinesa era meio diferentão, mas isso aqui extrapola um pouco o bom senso."

        "Talvez eu devesse falar com o [chi] sobre esse portal e essa escadaria."

        "Quem sabe ele não sabe algo até sobre essa... espadachim... ninja... samurai..."

        $ xiangu_evento = 1
        $ dia_xiangu = dia + 1

        jump chinatown_caminho

    menu:
        "Se aproximar do portal":


            if dia < dia_xiangu:

                "Não quero ver a cara de cuíca daquela... [xu_nome] de novo hoje..."

                "Deixa eu sair daqui."

                jump chinatown_caminho

            if sayuri_e9 == "evento":

                "Eu preciso ver se a [xu] falou sobre mim pra Mestra Jidao."

                if xiang_escape < 6:

                    if not xiang_fim:

                        "Só que eu ainda não resolvi o problema da Xiang... será que não era melhor resolver isso antes?"

                "Podem ter outros assuntos na Cidade Chinesa antes desse momento final..."

                menu:
                    "Não importa. Vou tentar ver a Mestra agora.":


                        jump sayuri_evento9_parte2
                    "Eu preciso resolver outras coisas antes.":


                        "Melhor deixar a Mestra pra depois. Eu tenho que resolver outro pepino antes."

            if sayuri9_contra and not sayuri_fim:

                "Eu não posso deixar a Mestra continuar controlando a Cidade Chinesa."

                "A [s], a [fen], a [xu]... todo mundo sofre por causa dela. Aposto que a cidade toda se beneficiaria com o fim dessa mulher."

                "Eu vou resolver isso agora?"

                menu:
                    "Acabar com a Mestra Jidao agora.":


                        if xiang_escape < 6:

                            "Não adianta eu encarar ela sozinha. O Bao Chang disse que eu preciso das duas Flor-de-Lótus."

                            "Ou seja... eu tenho que resolver o assunto com a Xiang e com a He Xiangu antes. As duas com a tatuagem da flor."

                            "Quando eu terminar de resolver as coisas das duas... eu volto aqui."
                        else:


                            "A Xiang e a He Xiangu se encontraram... e com a ajuda do Bao a verdade veio à tona."

                            "Eu tô pronto pra trazer a [i] e acabar com a Mestra Jidao de uma vez por todas."

                            show black with dissolve

                            "{i}Você chama a Xiang e os dois voltam para o Portal de Pedra{/i}"

                            hide black with dissolve

                            jump sayuri9_final2
                    "Tenho que resolver algo antes.":


                        pass

            if xiang_fim:

                "Eu não tirei a Xiang do Distrito... eu não tenho mais porque tentar alguma coisa nessa lugar."

                jump chinatown_caminho

            if xiang_escape == 6:

                "Tudo o que eu podia fazer pela [xu] eu fiz. Agora é com ela."

                if banho_evento < 20:

                    "Talvez eu devesse dar uma olhada no banho de saúde e beleza da Liling e da Kaira."

                    "Elas também precisam da minha ajuda."

                jump chinatown_caminho

            elif xiangu_evento == 4:

                if xiang_escape == 5:

                    $ xiang_escape = 6

                    jump xiang_escape4

                if xiangu_promessa:

                    "Eu prometi pra [xu] que eu vou voltar aqui com a [i]. Eu preciso dar um jeito de tirar ela do Distrito."

                    "Se eu voltar aqui sem ela, minha cabeça vai acabar fora do corpo. Deus me livre."
                else:


                    "Eu não quero mais saber desse povo louco. Eu decidi não apostar minha vida e graças aos céus não perdi a cabeça."

                    "Eles que se fodam."

                jump chinatown_caminho

            if xiangu_evento == 3:

                "Aqui é o portal onde a [xu] fica."

                "..."

                mc normal "[xu]. Tudo bem?"

                show xiangu normal with dissolve

                xu "Olá. O que foi?"

                mc envergonhado "Só queria confirmar se n-"

                xu "Não. Apenas escolhidos podem passar pelo portal de pedra."

                if banho_evento < 14:

                    mc "Ok..."

                    mc "Até a próxima."

                    hide xiangu with dissolve

                    xu "..."

                    "Eu preciso continuar tomando banhos na [li] e falando com o [chi] pra descobrir alguma coisa."

                    jump chinatown_caminho

                $ xiangu_promessa = False

                "A [ka] me disse que a [xu] é só uma garota que foi enganada pelos Escolhidos da Cidade Chinesa."

                "Criaram essa história pra manter as pessoas na mão deles. Ela mesma acredita em tudo como se fosse verdade."

                "Por isso que ela ficou tão cheteada quando eu falei que ela tava mentindo."

                "Eu preciso tentar falar a verdade pra ela. É o único jeito."

                mc desculpa "[xu]... eu preciso conversar com você sobre um negócio. É um lance sério."

                xu "O quê?"

                mc "Vai ser complicado pra você. E seu primeiro impulso vai ser cortar minha cabeça fora com essa espada."

                xu "..."

                mc "Mas, por favor, me escuta antes."

                xu "De novo essa história... querendo falar que é tudo uma mentira..."

                mc envergonhado "Não... e sim ao mesmo tempo."

                xu "Você promete que é a última vez que vai falar sobre isso?"

                "Merda... última? Quer dizer... que tem que ser agora ou nunca?"

                mc normal "Ok. Mas então nós vamos sentar e conversar com calma. Você vai ouvir tudo o que eu tenho pra falar."

                xu "Você tem 10 minutos e só."

                mc angustiado "Nossa última conversa e só 10 minutos?!"

                xu "Exatamente. Eu sou [xu] e não devo ser vista trocando palavras com infiéis."

                mc zerado "Infiel..."

                mc normal "Tá bom. Que seja. Agora vem sentar aqui."

                xu "..."

                scene black with dissolve

                scene xiangu_mc_sentados with Dissolve(1.0)

                pause

                xu "Era isso que você queria? Me ver sentada, inofensiva? Despida de autoridade?"

                mc "Não faço ideia do que você tá falando. Só queria conversar."

                xu "Você fala como os espíritos das raposas que atormentam meu povo há milênios."

                mc "Espírito da raposa?"

                xu "Húli jīng. Normalmente elas se fazem de lindas mulheres para seduzir e enganar homens."

                xu "Mas aqui poderia ser o contrário. Será que você é uma raposa?"

                menu:
                    "Claro que não.":


                        mc "Claro que não. Eu sou só um cara normal."

                        xu "Isso é o que um húli jīng diria com certeza."

                        mc "[xu]... você precisa acreditar em mim."

                        xu "Isso dependerá das suas próximas palavras. Mas ficarei de olhos bem abertos."

                        mc "..."
                    "Você tá falando que eu sou lindo?":


                        mc "Você tá querendo dizer que eu sou lindo e tô tentando seduzir você? É isso?"

                        xu "C-claro que não! Você é feio e quer me enganar. É isso que eu tô falando."

                        mc "Mas você disse que as raposas se transfor-{nw}"

                        xu "Eu sei o que eu disse! Agora esqueça isso. Você só tem 10 minutos, lembra?"

                        mc "Verdade."

                mc "Bom. O que eu preciso falar é que... olha... talvez você não seja a [xu] da lenda."

                "É agora que ela acaba comigo."

                xu "..."

                mc "?"

                xu "..."

                mc "Oi?"

                xu "Oi o quê? Fala o que você tem pra falar? O tempo tá passando."

                mc "A-ah! Ok."

                mc "Eu conversei com uma garota chamada [ka] que vive com a [li] que trabalha no banho."

                xu "Eu sei quem é a senhora [li]. Não precisa me falar sobre meu próprio povo."

                mc "Desculpa. Então... essa garota [ka]... ela me falou sobre os Escolhidos e como eles criaram essa farsa pra controlar o bairro."

                mc "Eu queria falar mais devagar com você, mas eu não tenho tempo. Eu tenho que ir direto ao ponto."

                mc "Essa mentira não é culpa sua. Você é só mais uma vítima de toda essa história. Os culpados são os cabeças."

                mc "Essa história de Imortais, de [xu] e Escolhidos... eles colocam isso na cabeça de vocês desde que vocês nascem."

                mc "Vocês vão se encontrar com eles e escutam isso. Seus pais falam disso, seus amigos falam disso."

                mc "Todos nós crescemos ouvindo coisas que acabam se tornando verdade pra gente... mesmo não sendo..."

                mc "Os encontros nos templos... as palavras que vêm dos deuses... tudo parece fazer sentido. Mas pensa, realmente faz?"

                mc "Você acha que existem pessoas imortais de verdade? Milagres inexplicáveis? Você acha que os deuses querem o dinheiro da pessoas?"

                mc "Eles falam que a gente tem que acreditar na palavra dos deuses ou somos infiéis? Não parece agressivo demais?"

                mc "Pense se você não acha uma coisa aqui ou ali estranha. Não ignore os sinais que tem coisa esquisita acontecendo."

                mc "Pense com sua cabeça. A cabeça da mulher sentada do meu lado, não a de uma [xu] que falaram que existiu."

                mc "Se voc-{nw}"

                xu "Acabou seu tempo. Era isso?"

                mc "Acho que sim... não sei se deu pra entender..."

                xu "Eu entendi tudo. Eu acho que você falou de forma bem clara. E eu tinha pensado sobre isso antes... faz muito sentido..."

                mc "Que bom! Eu pensei que você iria querer cortar minha cabeça. O que você acha? O que a gente pode fazer?"

                xu "Eu sei o que eu vou fazer."

                mc "Hm?"

                scene chinatown xiangu_ameaca with vpunch

                xu "Saia daqui, infiel!"

                mc angustiado "X-xiangu!"

                xu "Essas palavras são dos espíritos das sombras! Essa língua de fogo que não merece ser ouvida em nosso solo sagrado!"

                xu "Se você não sair daqui agora, eu vou matar você! Sua presença profana este local sagrado!"

                mc concentrando "Eu tinha uma esperança que você ia me ouvir... Mas parece que você tá enterrada demais nisso tudo."

                xu "Eu estou 'enterrada'?! Eu sou [xu], a tocada pelos deuses. A lótus em minhas costas é a marca de uma deusa!"

                xu "Quem dera outra pudesse tomar meu lugar, mas apenas eu carrego a marca dos deuses. Apenas eu posso fazer isso."

                mc desconfiado "Apenas você?"

                xu "Claro! Apenas a verdadeira [xu] carrega a marca da lótus, o meu símbolo."

                mc "E se existisse outra garota... com a mesma marca que a sua?"

                xu "Impossível!"

                mc "Não... eu conheci uma garota com a mesma marca que a sua. Exatamente a mesma tatuagem."

                xu "Tatuagem... você realmente não tem nenhum apreço pelo que é sagrado."

                mc "Mas-{nw}"

                xu "Tudo bem. Se tudo o que você diz é verdade, então me traga essa garota. Deixe-me ver outra tocada pelos deuses."

                xu "Se você não é um então faça isso."

                mc charmoso "Ok. Eu vou fazer isso."

                xu "Mas, se você não conseguir... então você pagará com a vida."

                mc angustiado "Q-quê?!"

                xu "Jure! Agora! Jure pela sua vida que essa mulher existe! E se você não conseguir, pagará com sua vida pela sua insolência!"

                "Jurar pela minha vida... com certeza essa garota vai cobrar se eu não conseguir..."

                "Eu vou ter que tirar a [i] do Distrito se eu quiser trazer ela aqui... como eu vou fazer isso?"

                "Mas é o único jeito. Se eu não aceitar, vai parecer que tudo o que eu falei é mentira. Mas se der errado... ela vai me matar."

                "O que eu faço?!"

                menu:
                    "Eu juro pela minha vida.":


                        $ xiangu_promessa = True

                        mc serio "Eu juro."

                        xu "S-sério?"

                        mc "Sim. O que eu tô falando é verdade, Xiangu. Eu vou provar pra você."

                        xu "E-então eu vou esperar você voltar. Da próxima vez que você vier, é bom ela estar com você."

                        xu "E a marca precisa ser idêntica. Parecida não será suficiente."

                        mc charmoso "Pode deixar. Eu vou trazer ela aqui e você vai perceber que tem cachorro nesse mato."

                        xu "Vou te esperar. Agora vai."

                        mc angustiado "O-ok!"

                        scene black with dissolve

                        "Ufa... ela não cortou minha cabeça... ainda..."

                        "Não tem jeito. Agora eu vou ter que tirar a [i] do clube de BDSM e trazer ela aqui."

                        "Se eu voltar aqui sem ela, é morte na certa."

                        "Uma outra pessoa com a marca... como será que a [xu] vai ficar quando ver a [i]?"

                        "Agora... pensando aqui... onde eu fui me meter?"
                    "Eu não vou jurar nada.":


                        mc envergonhado "Tá doida? Eu não vou jurar nada."

                        xu "Eu sabia. Você é fraco e fala sem pensar. Típico arauto dos espíritos cheios de artimanhas."

                        mc "Você tá indo longe demais. Eu só não quero colocar minha vida em risco por causa de vocês."

                        mc "Quer continuar acreditando nessa baboseira? Faça o que te der na telha. Falous."

                        xu "..."

                        scene black with dissolve

                        "Eu não vou colocar minha vida na reta. Isso é demais pra mim."

                        "Eu vou esquecer esse povo da Cidade Chinesa e dar o fora enquanto eu posso."

                        "Desculpa pessoal, mas isso é demais pra mim. Eu quero só ter uma vida boa."

                scene black with dissolve

                $ xiangu_evento = 4
                $ dia_xiangu = dia + 1

                jump chinatown_caminho

            if xiangu_evento == 1 and banho_evento == 4:

                "A [li] disse que a He Xiangu fica o dia todo protegendo este portal."

                "E aquela... [xu] fica aqui o dia todo também... Devem ser a mesma pessoa."

                "Não custa tentar."

                "A não ser que ela corte alguma parte do meu corpo."

                mc zerado "O que eu tô pensando? Essas pessoas tão começando a me afetar. É impossível que aquela mina realmente consiga cortar alguma coisa com aquela espada."

                "Enfim... quem não arrisca não petisca."

                "..."

                scene chinatown portal_xiangu with Dissolve(2.0)

                pause

                "Ela tá ali como eu imaginava."

                xu "Não."

                mc zerado "Eu sei..."

                mc normal "Mas hoje eu não vim pra passar pelo portal de pedra."

                mc charmoso "Eu vim por sua causa."

                xu "?!"

                "Parece que eu peguei ela de surpresa agora."

                mc "Eu quero falar com você, He Xiangu."

                xu "{i}Kh!{/i}"

                mc "Não precisa se assustar. Eu descobri seu nome e quero conversar com você."

                xu "..."

                mc "Você pode descer pra gente se falar?"

                xu "..."

                label xiangu_e2_menu:

                    "Hmmm... e agora?"

                menu:

                    "Eu quero saber mais sobre sua lenda." if not xiangu_p_lenda:

                        $ xiangu_p_lenda = True

                        mc normal "Me falaram que você pode pular por montanhas e traz frutas especiais para os moradores."

                        mc "Você poderia me falar mais sobre isso?"

                        xu "..."

                        "Ela não comprou a ideia..."

                        jump xiangu_e2_menu

                    "Você realmente é imortal?" if not xiangu_p_imortal:

                        $ xiangu_p_imortal = True

                        mc normal "É verdade que você recebeu o poder dos deuses há milhares de anos?"

                        mc "Você realmente é imortal?"

                        xu "..."

                        "Nada... é impossível chamar a atenção dela."

                        jump xiangu_e2_menu
                    "Pare de mentir para os chineses!":


                        mc bravo "Eu sei que essa história de He Xiangu é balela! Pare de mentir pros chineses!"

                        xu "!!!"

                        scene chinatown xiangu_ameaca with vpunch

                        mc angustiado "!!!"

                        window hide

                        pause

                        xu "O que você disse?"

                        mc preocupado "E-eu disse... disse..."

                        mc desculpa "Eu disse que é impossível você ser imortal."

                        mc "Você... tá enganando o povo da Cidade Chinesa com essa história."

                xu "Você não sabe nada sobre mim."

                mc "Tem razão."

                mc envergonhado "Mas se tem algo que eu sei é que você não tem o dom da vida eterna."

                xu "Como você pode saber isso?"

                mc serio "Não se faça de burra. Isso já tá cansando."

                mc "Não existem pessoas imortais no mundo. Isso contraria toda a ciência. Eu... eu nem deveria ter que falar isso! Essa conversa é maluca!"

                xu "Você não sabe nada sobre o mundo."

                $ xu_nome = "He Xiangu"

                xu "Eu sou [xu]. Sou a virgem imortal. Minha lenda é passada de geração a geração por milhares de anos."

                "Não é possível que essa garota tá falando sério. Ela deve tá de brincadeira comigo."

                mc envergonhado "..."

                xu "..."

                mc "Sério mesmo? Você vai continuar falando isso?"

                xu "Eu só falo a verdade."

                mc desculpa "{size=15}Você é só uma maluca...{/size}"

                xu "O que disse?"

                mc envergonhado "Nada, não."

                mc "Acho que vou indo nessa."

                xu "..."

                mc "Como era mesmo? Zaijian."

                xu "..."

                scene chinatown portal with Dissolve(1.0)

                "Essa deve ser a coisa mais louca que eu já vi na vida."

                "Será que ela é uma cosplayer se fazendo de um personagem?"

                "Hmmm... ela até parece um personagem..."

                "Será que o [chi] sabe alguma coisa dessa doida?"

                "..."

                $ xiangu_evento = 2
                $ dia_xiangu = dia + 1

                jump chinatown_caminho

            if xiangu_evento == 2 and xiang_evento == 6:

                "A [i] disse que a [xu] tá mentindo..."

                mc zerado "Isso qualquer pessoa de bom senso saberia..."

                "Mas ela disse também que a [xu] não é uma má pessoa. Que ela não tá enganando as pessoas por querer. Que ela própria não sabe."

                "Como isso é possível?"

                "..."

                scene chinatown portal_xiangu with Dissolve(1.0)

                "Claro que ela continua ali. O dia todo, todos os dias... como pode?"

                mc envergonhado "Oi..."

                xu "Você de novo..."

                xu "Você ainda não entendeu que não pode passar por aqui?"

                if v24_fim:

                    mc "Você sabe que eu passei aqui com a [s], né?"

                    xu "..."

                    xu "Foi um caso especial. Não pode passar sozinho."

                    mc zerado "Ok..."

                mc normal "Mas eu não quero passar. Eu só quero falar com você."

                xu "F-falar? De novo? Você vai me caluniar novamente? Falar que eu estou mentindo para as pessoas?"

                "Não é possível que ela realmente ache que é verdade..."

                mc concentrando "Não. Eu não acho mais que você tá mentindo."

                xu "Sério?!"

                scene chinatown xiangu_ameaca with vpunch

                mc preocupado "Uou..."

                xu "Você está brincando comigo?"

                mc "N-não! É verdade."

                xu "..."

                mc desculpa "Eu conversei com outras pessoas aqui do bairro e minha conclusão é que você não tá mentindo."

                xu "Sé-sério?!"

                mc normal "Sim."

                scene chinatown portal with Dissolve(1.0)

                xu "U-ufa..."

                show xiangu normal with dissolve

                xu "Fico feliz que você tenha visto a verdade."

                mc envergonhado "Que bom, né?"

                "Puxa. Que diferença. Ela parece bem mais calma agora."

                mc normal "Será que agora eu posso passar?"

                xu "Obviamente não."

                mc envergonhado "Imaginei..."

                xu "Apenas {b}os escolhidos{/b} podem entrar na vila e nas outras localidades proibidas."

                "Localidades proibidas... o que será isso?"

                mc normal "Entendi. E como eu posso conseguir ir para esses lugares?"

                xu "Infelizmente é impossível pra você. Apenas descendentes chineses podem ser escolhidos."

                mc desculpa "Que coisa..."

                xu "..."

                mc normal "Deixa eu te perguntar outra coisa."

                xu "Diga."

                mc normal "Eu não conheço a sua lenda. Como você se tornou imortal?"

                xu "Essa é uma história muito comum na Cidade Chinesa. Você pode conversar com outras pessoas para descobrir."

                mc envergonhado "T-tá."

                xu "O importante é que eu continue usando minhas habilidades para o bem de todos que vivem aqui."

                mc desconfiado "'Habilidades'? Você pode fazer outras coisas além de ser imortal?"

                xu "Sim. Mas não quero falar sobre isso. Meus dons foram conferidos pelos deuses quando me tocaram. Eu sou apenas uma arma em suas mãos."

                mc "..."

                xu "..."

                mc envergonhado "A- ok..."

                xu "Agora tenho que ir."

                mc desconfiado "O que você vai fazer?"

                xu "Proteger o portal."

                mc zerado "..."

                mc "Tá."

                mc "Até mais, [xu]."

                hide xiangu with dissolve

                "Quem vê parece que ela é muito ocupada."

                "Essa conversa não serviu praticamente pra nada. Pareceu a conversa com uma doida."

                "Bom... pelo menos ela tá menos agressiva comigo. Mas realmente não vai ter como passar por esse portal assim."

                "O plano da [i] também não vai funcionar. A [xu] realmente acredita que ela é imortal e com outras habilidades ainda por cima."

                "Ela nunca vai admitir pra ninguém que é mentira, sendo que ela mesma acredita que é verdade."

                "Talvez o [chi] possa me ajudar. Preciso falar com ele."

                $ xiangu_evento = 3
                $ dia_xiangu = dia + 1

                jump chinatown_caminho

            "..."

            scene chinatown portal_xiangu with Dissolve(2.0)

            pause

            "Ela tá ali de novo..."

            xu "Não."

            mc zerado "Eu sei..."

            if tempo >= 3:

                mc desconfiado "Até de noite você tá aqui? Você não faz nada da vida, não?"

                xu "Eu não fico aqui. Eu venho quando vejo alguém se aproximando."

                mc "Sei..."

            if xiangu_evento == 2:

                mc envergonhado "Você continua com essa besteira de que realmente é a [xu] da lenda?"

                scene chinatown xiangu_ameaca with vpunch

                pause

                xu "A única besteira aqui é sua incapacidade de discernir a verdade da mentira."

                xu "Eu sou [xu], a verdadeira e única [xu] que existiu!"

                mc envergonhado "Ok... ok..."

                if tempo < 3:

                    mc "Tenha um bom dia."
                else:


                    mc "Tenha uma boa noite."

            "Deixa eu sair daqui."

            $ dia_xiangu = dia + 1

            jump chinatown_caminho
        "Voltar para a Cidade Chinesa":


            "Não quero ver a cara de cuíca daquela... [xu_nome] de novo..."

            "Deixa eu sair daqui."

            jump chinatown_caminho

    show screen chinatown_tela2

    pause

label chinatown_caminho:

    $ chinatown_area = "caminho"

    hide screen chinatown_tela
    hide screen chinatown_tela2

    scene chinatown caminho with Dissolve(1.0)

    pause

    show screen chinatown_tela2

    pause

label chinatown_entrada:

    $ chinatown_area = "entrada"

    hide screen chinatown_tela
    hide screen chinatown_tela2

    scene chinatown entrada with Dissolve(1.0)

    pause

    show screen chinatown_tela2

    pause

label chinatown_esquina:

    $ chinatown_area = "esquina"

    hide screen chinatown_tela
    hide screen chinatown_tela2

    scene chinatown esquina with Dissolve(1.0)

    show screen chinatown_tela2

    pause

label chinatown_rua:

    $ chinatown_area = "rua"

    hide screen chinatown_tela
    hide screen chinatown_tela2

    scene chinatown rua with Dissolve(1.0)

    show screen chinatown_tela

    pause

label chinatown_superior:

    $ chinatown_area = "superior"

    hide screen chinatown_tela

    scene chinatown superior with Dissolve(1.0)

    show screen chinatown_tela

    pause

    label chinatown_banho:

        $ proibido_salvar = False
        $ show_quick_menu = True

        hide screen chinatown_tela

        if tempo >= 3:

            "O banho não abre durante a noite."

            "Amanhã bem cedo eles já devem estar funcionando."

            jump chinatown_superior

        elif dia < dia_banho:

            "Já relaxei demais por um dia..."

            "Outra hora eu volto aqui."

            jump chinatown_superior

        elif banho_evento == 4 and xiangu_evento <= 1:

            "Eu realmente podia dar uma relaxada agora..."

            "Só que primeiro preciso ir até o Portal de Pedra e descobrir quem raios é essa He Xiangu."

            jump chinatown_superior

        elif xiangu_evento == 2 and bao_evento < 3:

            "Antes de falar com a [li] de novo, eu preciso saber um pouco mais sobre a [xu]."

            "Como ela acredita muito nessa lenda, provavelmente ela só vai me falar coisas sem noção."

            jump chinatown_superior

        elif banho_evento == 6 and bao_evento == 3:

            "Agora eu preciso focar no [chi]. Preciso que ele me conte um fato 'importante' sobre a [xu]."

            "Pelo menos foi o que a menina estranha de cabelo vermelho me disse."

            "Não tenho nenhuma outra pista. Preciso acreditar nela."

            jump chinatown_superior

        elif banho_evento == 6 and xiangu_evento == 2:

            "Antes de falar com a [li] de novo, eu preciso saber um pouco mais sobre a [xu]."

            if xiang_evento == 6:

                "A [i] me disse que eu preciso convencer a [xu] a admitir a verdade."

                "Mas não sei como fazer isso ainda. Mas o único jeito é falando com a garota do portal."

                "Tenho que falar com ela e descobrir a verdade."
            else:


                "Talvez eu consiga algo com a chinesa do Distrito."

            jump chinatown_superior

        elif banho_evento == 9:

            "Não adianta eu ir pro banho agora. A [li] não vai deixar eu falar com a [ka]."

            "Preciso esperar as coisas entre elas se resolverem."

            if bao_evento == 4:

                "Talvez eu devesse falar com o [chi] e descobrir mais sobre a relação delas."

                jump chinatown_superior

            elif bao_evento == 5:

                "O [chi] me contou um pouco sobre as duas. Nada de concreto infelizmente... Agora eu preciso ver como usar isso ao meu favor."

                "Ele disse que a relação delas representa o que tem de mais perverso na capital. Do que será que ele tá falando?"

                "É duro saber, mas o banho é minha maior chance. Eu tenho que continuar."

                scene black with dissolve

        elif banho_evento > 9 and banho_evento <= 13:

            "Preciso continuar pegando informações no banho."

            "A [ka] com certeza sabe muita coisa."

        elif banho_evento == 14:

            "Eu consegui muita coisa com a [ka]. Mais do que eu imaginava."

            if xiang_escape == 6:

                "Agora que a gente plantou a dúvida na cabeça da [xu], acho que isso vai ajudar com a [ka] também."





                "O próximo passo é falar com a Liling e fazer ela entender que a He Xiangu não é imortal de verdade."

                "Se ela perceber que eles foram todos enganados, talvez ela consiga ver que o lance com a Kaira tá totalmente errado."
            else:


                "Agora eu tenho que ver o que fazer com o [chi] e a [xu]."

                "Depois eu volto aqui e vejo como salvar ela."

                jump chinatown_superior

        elif banho_evento == 20:

            "Eu prometi pra Liling que ia conseguir de volta o que ela entregou pros Imortais."

            "Mesmo sem saber o que é... e como eu vou fazer isso... cada uma que eu me meto..."







            show black with dissolve

            p rindo "Para continuar essa história, você precisa avançar a história de vários personagens principais."

            p "Você precisará terminar a história da Sayuri, Júlia, Diana e Nathan."

            p "Quando chegar no final da história da Sofia, você precisará escolher saber a verdade."

            p "Boa sorte! Sua aventura em CH é imensa e MUITA coisa está te esperando! Curta cada momento!"

            hide black with dissolve

            jump chinatown_superior

        elif banho_evento > 14:

            "Eu tenho que continuar vindo aqui até convencer a Liling e salvar a Kaira."

        scene banho_zen entrada with Dissolve(1.0)

        if not china_banho_1vez:

            $ china_banho_1vez = True

            "Este lugar..."

            li "Ô! Ô! Fazendo?!"

            mc desconfiado "Que?"

            show liling normal with Dissolve(1.0)

            li "Tá atrapalhando."

            mc preocupado "Estou atrapalhando algo? Desculpa."

            li "Vai querer banho?"

            mc desconfiado "Banho?"

            li "Banho que deixa imortal. Saúde e beleza."

            "Hmmm... será que é isso? Um lugar de banhos especiais."

            li "Vai querer?"

            mc normal "Quanto é o banho?"

            show liling rindo with dissolve

            li "Oh! Cliente."

            li "Bem-vindo. Banhos excelentes. Saúde e beleza."

            mc envergonhado "Entendi. Você já disse."

            "Que mudança de tratamento..."

            li "Banho só {b}C$ 50{/b}. Muito barato para pele bonita e muita saúde."

            if cash < 250:

                mc surpreso "!"

                show liling normal with dissolve

                li "Cara de pobre. Jeito de pobre."

                li "Se não tomar banho, atrapalha. Xô xô!"

                li "Pobre não toma banho de saúde e beleza e nem outras coisas."

                mc desconfiado "Outras coisas?"

                li "Pobre! Xô xô!"

                mc angustiado "Ei!"

                jump chinatown_superior
            else:


                "Cinquenta... nem é tanta coisa assim..."

                mc charmoso "Talvez eu realmente tome um banho aqui."

                li "Jeito de rico. Rico bem vindo pra tomar banho e muito mais."

                mc desconfiado "Muito mais?"

                li "Toma banho e conversamos."

                "O que será que ela quer dizer com 'muito mais'?"

                "Hmmm..."
        else:


            if banho_evento > 9:

                mc normal "Como vai, [li]?"

                scene banho_liling1 with Dissolve(1.0)

                pause

                li "Olá, senhor [mc]. Veio aproveitar banho de saúde e beleza?"

                mc charmoso "Exatamente."

            elif banho_evento == 9:

                pause

                mc normal "Oi, [li]."

                scene banho_liling1 with Dissolve(1.0)

                pause

                li "Senhor cliente voltou."

                mc normal "Sim. Vim tomar mais um banho de saúde e beleza."

                li "Senhor sabe que não pode serviços especiais."

                "Ela foi bem direta... Não adianta eu querer forçar."

            elif banho_evento > 3:

                "Eu tô começando a ficar viciado neste lugar."

            elif sayuri_e4 == "amizade" or sayuri_e4 == "namoro":

                "Eu lembro quando eu vim aqui com a [s]. Ela parecia tão relaxada..."
            else:


                "Este lugar tem uma vibe que eu nunca vi na vida."

        if banho_evento < 9:

            "..."

            show liling rindo with dissolve

        label banho_menu:

            if banho_evento > 3:

                if banho_evento < 9:

                    li "Muito bom ver você, senhor [mc]."

                    mc normal "Oi, [li]."
            else:


                li "Jovem visita banho de novo. Vai querer banho de saúde e beleza?"

                mc envergonhado "Oi..."

        menu:
            "Tomar banho de saúde e beleza por {b}C$ 50{/b}":


                $ proibido_salvar = True
                $ show_quick_menu = False

                if banho_evento < 9:

                    "Vou dar aquela relaxada. Eu mereço..."

                    mc "Isso aí."

                    li "Muito bom..."
                else:


                    "Eu preciso tirar tudo o que eu puder delas."

                    mc "Não é agora que eu vou parar, né?"

                    li "Assim que é bom."

                python:
                    if renpy.android:
                        banho_evento_db = PythonSDLActivity.pegaBanho()

                if banho_evento < banho_evento_db:

                    "{b}Você já pagou pelo banho [banho_evento_db] vezes. Mas neste gameplay você usou o banho [banho_evento] vezes.{/b}"

                    "{b}Como não é preciso pagar duas vezes pela mesma coisa, você pode continuar a história sem pagar novamente.{/b}"

                    jump banho_evento

                python:
                    if renpy.android:
                        cash = PythonSDLActivity.pegaCash()

                "Eu tô com {b}R$ [cash]{/b}..."

                $ renpy.choice_for_skipping()

                if cash >= 50:

                    "Eu tenho dinheiro suficiente."

                    menu:
                        "Pagar os {b}C$ 50{/b} e tomar banho":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.usaCash(50)
                                    PythonSDLActivity.registraEvento("banho_liling","liling","personagem")

                                renpy.block_rollback()

                            mc normal "Aqui tá o dinheiro."

                            li "Excelente!"

                            jump banho_evento
                        "Melhor deixar pra outra hora":


                            "Nem tô afim agora. Melhor deixar pra outra hora."

                            jump banho_sair
                else:


                    jump banho_pobre
            "Não quero nada agora":


                label banho_sair:

                    $ proibido_salvar = False
                    $ show_quick_menu = True

                    mc normal "Hoje não quero nada. Só vim dar um alô mesmo."

                show liling normal with dissolve

                li "Cara de pobre. Jeito de pobre."

                li "Se não tomar banho, atrapalha. Xô xô!"

                mc angustiado "Ei!"

                jump chinatown_superior

    label banho_pobre:

        "O foda é que não tenho essa grana comigo aqui."

        mc desculpa "..."

        show black with Dissolve(1.0)

        p lecionando "Ixi. O [mc] tá pobre que só ele..."

        p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

        p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

        p "Além de avançar na história agora mesmo, você ainda contribui com o desenvolvimento de CH."

        p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

        menu:
            "Sim. Tô com uma graninha sobrando aqui.":


                p rindo "Que bom!"

                call comprar_cash from _call_comprar_cash

                p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                hide black with dissolve

                jump banho_menu
            "Não. Tô pobre igual a ele...":


                p rindo "Não esquente."

                p "Trabalhe sempre que possível no bar e vá juntando seus reais. Logo logo você já vai estar com grana suficiente."

                p "Demora, mas vale a pena!"

                hide black with dissolve

                mon "E então? Vai entrar?"

                jump banho_sair

    label banho_evento:

        if banho_evento == 0:

            li "Agora sim. Jovem agora é cliente."

            $ li_nome = "Liling"

            li "Muito prazer. Nome é [li]."

            li "E você é?"

            mc envergonhado "Meu nome é [mc]."

            li "Seja muito bem vindo, [mc]. Você terá excelente experiência nosso estabelecimento."

            li "Vou preparar banho. Com licença."

            hide liling with dissolve

            "Uou... a mulher mudou completamente. Tá até falando melhor..."

            "Parece que pros clientes tudo, pro resto nada."

            "..."

            "..."

            li "Pode vir, senhor [mc]."

            mc normal "Tô indo."

            scene black with dissolve

            li "Coloque esta veste e pode deitar."

            mc envergonhado "Isto parece um pouc-"

            li "Vamos, tire roupa."

            mc surpreso "E-ei! Eu posso tirar sozinho."

            li "..."

            "..."

            mc envergonhado "Obrigado."

            li "Agora deite e acomode."

            mc "Valeu."

            li "Vou dar licença. Qualquer coisa chame."

            mc "Ok."

            "Vamos ver se esse banho realmente vale a pena."

            "..."

            scene banho_chines mc1 with Dissolve(2.0)

            pause

            "Aahh... delícia..."

            "Esse banho... tem algo mágico aqui... não é possível."

            "Eu sinto meu corpo esquentando, meus músculos... parece que eu tô sendo massageado no corpo todo."

            "..."

            "Que delícia..."

            "Será que esse banho realmente vai me deixar mais bonito?"

            "Seria excelente pra eu me dar melhor com as celebridades. Talvez ganhar uns pontos extras..."

            "..."

            show black with dissolve

            hide black with dissolve

            "Opa. Acho que eu pesquei."

            li "Senhor, [mc]."

            mc "Oi?!"

            li "Seu tempo de uma hora acabou."

            mc "Já?!"

            mc "Ok. Tô saindo."

            scene black with dissolve

            "..."

            scene banho_zen entrada with Dissolve(1.0)

            mc feliz "Uou. Foi muito bom."

            show liling rindo with dissolve

            li "Sim, sim. Banho de saúde e beleza sem dúvidas é incrível."

            li "Espero ver senhor [mc] outras vezes por aqui."

            mc envergonhado "Com certeza. Preciso pensar na grana, mas assim que der eu volto."

            li "Dinheiro é pouco. Banho é incrível. Mas banho não é tudo. Tem outras coisas na casa de banho."

            mc desconfiado "Que coisas?"

            li "Deixar outro dia. Zaijian, senhor [mc]."

            mc "Até a próxima."

        elif banho_evento == 1:

            "Vou preparar tudo e aviso."

            mc normal "Obrigado."

            hide liling with dissolve

            "Aquele banho que eu tomei no outro dia foi incrível. Não vejo a hora de curtir novamente."

            "É bom ter uma graninha sobrando pra poder aproveitar tudo o que a cidade oferece."

            "..."

            li "Senhor, [mc]. Pode vir."

            mc "Opa!"

            scene c_chinesa ofuro with Dissolve(1.0)

            show liling rindo with dissolve

            li "Roupa está ali. Pode vestir e aproveitar."

            mc charmoso "Obrigado."

            hide liling with dissolve

            "Tomara que esteja bom igual da outra vez."

            scene banho_chines mc1 with Dissolve(2.0)

            pause

            "Delícia..."

            "Esse efeito que a água tem no meu corpo é muito estranho. O que será que ela coloca aqui?"

            "Bom... vou relaxar..."

            show black with dissolve

            hide black with dissolve

            "Opa! Acho que cochilei de novo."

            "Só falta ter acabado o tempo de novo..."

            "..."

            show black with Dissolve(1.0)

            "..."

            scene banho_chines mc2 with Dissolve(2.0)

            "Hmmm..."

            "Acho que ela me esqueceu aqui desta vez."

            "Opa. Nunca tinha reparado naquela estátua de Buddha. Eu pensei que o budismo fosse da Índia..."

            "Acho que vou perguntar pra [li] sobre isso outra hora."

            "Pensando bem... eu não sei muito sobre os chineses. A [s] até me falou algumas coisas, mas realmente é uma cultura muito diferente."

            "Isso é até algo estranho. Porque a China tá virando uma potência tão grande e é o país mais populoso do mundo."

            "Por que será que a gente sabe tão pouco sobre eles?"

            "A Cidade Chinesa é tipo uma 'mini China'. Parece que eles tentam manter várias características da cultura deles preservada."

            "Acho que é até algo raro poder aproveitar uma coisa tão diferente como este banho."

            "..."

            "O que eu tô pensando? Tô parecendo um cientista, sei lá."

            "Acho que o banho tá me deixando mais inteligente."

            mc "Até parece..."

            "..."

            li "Senhor [mc]. Seu tempo chegou ao fim."

            mc "Opa! Tô saindo!"

            scene banho_zen entrada with Dissolve(1.0)

            mc normal "Foi incrível."

            show liling rindo with dissolve

            li "Banho de saúde e beleza é incrível. Senhor tem que voltar."

            mc charmoso "Vou voltar com certeza."

            li "Senhor [mc] é cliente bom. Pode voltar quando quiser."

            mc "Obrigado. Até mais, [li]."

            li "Zaijian."

            mc desconfiado "Zai o quê?"

        elif banho_evento == 2:

            li "Você volta aqui novamente. É grande cliente do banho de saúde e beleza."

            mc normal "Seu banho tem feito maravilhas. Tô me sentindo muito mais ativo ultimamente."

            li "Banho especial garante vida eterna e muita energia. Senhor [mc] vai ter saúde."

            "Vida eterna, é?"

            mc envergonhado "Sei..."

            show liling falando with dissolve

            li "Senhor não acredita?"

            mc "Não é por nada, mas 'vida' eterna é um pouco demais."

            li "Senhor [mc] conhece a lenda de He Xiangu?"

            mc desconfiado "Lenda? He Xian..."

            li "He Xiangu é de grande renome na China. História de He Xiangu são contadas de pais para filhos há milhares de anos."

            li "Só que agora vou preparar banho. Conversamos mais outra hora."

            hide liling with dissolve

            "He Xiangu... Vida eterna..."

            "Parece que existem fanáticos em todas as culturas..."

            "..."

            scene c_chinesa ofuro with Dissolve(1.0)

            mc surpreso "Opa!"

            show kaira nervosa with dissolve

            "Garota" "Ah.. ah..."

            li "Xô! Pra dentro!"

            "Garota" "S-sim!"

            hide kaira with moveoutleft

            "Acho que ela não tinha me chamado ainda... Que fora..."

            show liling normal with dissolve

            li "Senhor [mc]. Banho ainda não está pronto."

            mc envergonhado "Desculpa. Eu..."

            show liling rindo with dissolve

            li "Não tem problema."

            mc normal "Quem era essa?"

            li "Garota trabalha aqui."

            mc desconfiado "Hmm..."

            li "Não pense nela. Banho está pronto agora."

            mc normal "Valeu."

            li "Bom banho."

            hide liling with dissolve

            "..."

            scene banho_chines mc2 with Dissolve(2.0)

            pause

            "Aaahhhh... que saudades de sentir a mágica disto aqui..."

            "..."

            "E quem será aquela garota? E por que ela tava com aquela roupa?"

            "Parece que a [li] não gostou da gente ter se encontrado."

            "Bom... não vou causar com isso. O banho é relaxante demais..."

            "..."

            li "Senhor [mc]?"

            "Hâ? Já acabou?"

            mc "Oi?"

            li "Posso chegar perto?"

            mc "Cl-claro."

            "Deixa eu me ajeitar."

            "..."

            scene banho_chines liling_conversando with Dissolve(2.0)

            pause

            mc "O-oi."

            li "Só queria ter certeza. Está tudo certo?"

            mc "Sim. Uma delícia."

            li "Bom bom..."

            mc "O que você coloca neste banho? Pra dar esse efeito."

            li "Ervas trazidas por He Xiangu."

            mc "A da lenda que você falou?"

            li "Sim."

            mc "E o que tem nessas ervas? Como-"

            li "He Xiangu pula por montes e montanhas, coletando ervas e frutas. Ela distribui para todos da Cidade Chinesa."

            mc "Calma... quer dizer que realmente existe uma He Xiangu?"

            li "Claro, senhor [mc]. He Xiangu visita Cidade Chinesa cada semana. É garota muito bonita e bondosa."

            mc "[li]... você não tá pregando uma peça em mim, tá? Só porque eu não sou daqui..."

            li "Não! Não! Claro que não, senhor [mc]."

            mc "Mas-"

            li "Banho de saúde e beleza é para relaxar. Não se preocupe. Termine seu banho e conversamos."

            mc "Ok..."

            scene black with dissolve

            "Ela tem razão. Às vezes eu me empolgo demais."

            "..."

            "..."

            scene banho_zen entrada with Dissolve(1.0)

            show liling normal with dissolve

            li "Conseguiu relaxar?"

            mc concentrando "Sim. Acho que até dormi um pouco."

            li "Isso. Banho de saúde e beleza serve para relaxar e energizar. Não pode se preocupar."

            mc envergonhado "Ok."

            show liling rindo with dissolve

            li "Vamos falar mais próximo banho."

            mc normal "Ok. Até a próxima."

            li "Zaijian."

            mc desconfiado "Calma ae. O que é isso? Zai..."

            show liling falando with dissolve

            li "Hã?"

            mc envergonhado "Isso que você falou no final."

            li "Ah! Zaijian é mesmo que falar 'tchau', só que chinês."

            mc surpreso "Ahhh! Legal!"

            mc envergonhado "Então tá. Tchau."

        elif banho_evento == 3:

            li "Já chamo então."

            mc normal "Ok."

            hide liling with dissolve

            "Acho que hoje vou querer saber mais sobre essa história da He... esqueci o nome da criatura."

            "E também tem aquela garota que eu vi da outra vez..."

            "Será que eu tento xeretar o que elas tão fazendo no banho sem ser visto?"

            menu:
                "Melhor eu ficar quieto aqui. Não tenho nada com isso.":


                    "..."

                    "..."
                "Sou curioso demais pra não xeretar.":


                    mc envergonhado "Sou curioso demais..."

                    "Não aguento ficar aqui. Preciso dar uma olhada."

                    "..."

                    scene c_chinesa ofuro with Dissolve(1.0)

                    "A garota tá lá de novo..."

                    show kaira nervosa at entra_esquerda with dissolve

                    ka "Só que-"

                    li "Não! Senhor ainda não está pronto."

                    ka "Mas eu quer-"

                    show liling normal at entra_direita with dissolve

                    li "Garota agora gosta de fazer isso?!"

                    li "Não é você que chorava todo dia por causa disso?!"

                    li "Agora não vê hora de pegar neles?!"

                    ka "É que... ok..."

                    li "Xô que tô preparando banho."

                    ka "Tá."

                    hide kaira with dissolve

                    hide liling with dissolve

                    "Que conversa estranha..."

            li "Senhor [mc]! Banho está pronto!"

            "..."

            scene c_chinesa ofuro with Dissolve(1.0)

            mc normal "Obrigado, [li]."

            show liling rindo with dissolve

            li "Tudo para bom cliente."

            mc envergonhado "Deixa eu aproveitar então e pedir. Você pode conversar comigo enquanto eu relaxo no banho?"

            show liling falando with dissolve

            li "Banho de saúde e beleza é melhor quando sozinho e em paz."

            mc normal "É que eu queria que você me falasse mais sobre a lenda da Xe..."

            li "He Xiangu?"

            mc normal "Essa mesmo."

            li "Certo. Se senhor deseja assim."

            mc concentrando "Obrigado."

            "..."

            scene black with dissolve

            "Me trocar e pronto."

            scene banho_chines liling_conversando with Dissolve(2.0)

            pause

            li "Que senhor quer saber?"

            mc "Você tava me falando que a He Xiangu visita a Cidade Chinesa toda semana. Como assim?"

            mc "Ela não é a personagem de uma lenda chinesa?"

            li "Isso. He Xiangu é de {b}Oito Imortais{/b}. Ela possui dom de vida eterna e pode saltar por montanhas."

            li "He Xiangu é jovem pura que foi abençoada por deuses e vive até hoje trazendo saúde a chineses."

            mc "E você tá dizendo que essa mesma He Xiangu, da lenda, existe de verdade, aqui, agora."

            li "Exatamente, senhor [mc]. Por que é tão difícil de acreditar?"

            "Será que ela tá falando sério?"

            "Bom... retrucar parece que não vai me levar a lugar nenhum. Então... como diz o ditado... se não pode vencer, junte-se a eles."

            mc "Depois da sua explicação eu acredito!"

            li "Ah! Sim!"

            scene banho_chines liling_conversando2 with Dissolve(2.0)

            pause

            li "Senhor é esperto. Acredita que digo verdade."

            mc "Claro."

            li "He Xiang é incrível. Ela é linda. Cabelos negros e compridos. Pele lisa e perfeita. Expressão séria e bondosa."

            li "Ela vive há milhares de anos. Ser linda para sempre. Sonho de qualquer mulher."

            li "..."

            "Olha só quem se empolgou agora..."

            menu:
                "...":


                    "..."
                "Você é linda também, [li].":


                    mc "Você também é linda, [li]."

                    li "Ah? Senhor [mc] muito gentil. [li] é velha."

                    mc "De forma alguma. Eu acho você incrível."

                    li "Não seja bobo, senhor."

            li "Agora vou deixar senhor relaxar. Aproveite banho de saúde e beleza."

            mc "Ah! [li]. Eu queria muito poder encontrar a He Xiangu. Como eu faço isso?"

            li "He Xiangu protege o pé do Monte Penglai durante o dia todo."

            li "Siga direção para templo e quando ver arcos vermelhos pegue direita. Você verá portal de pedra e caminho para jardim."

            li "He Xiangu protege {b}Portal de Pedra{/b}."

            if xiangu_evento > 0:

                "Espera... portal de pedra? Aquela garota! Ela fica lá o dia todo! Igual a [li] tá falando!"

                "Não é possível! Será que a aquela garota estranha da espada é a da lenda?!"

            mc "E-entendi..."

            mc "Então vou passar lá depois."

            li "Mande beijos de [li] para He Xiangu, por favor."

            mc "Pode deixar."

            li "Agora relaxe, senhor [mc]. Deixe banho de saúde e beleza fazer mágica."

            mc "Ok..."

            "..."

            scene banho_chines mc1 with Dissolve(1.0)

            "A [li] parece acreditar piamente nessa lenda. Será que os outros moradores da Cidade Chinesa são assim também?"

            "Tenho que admitir que este lugar tem uma vibe muito diferente do resto da cidade."

            "Mas magia? Uma espécie de deusa que vive eternamente? Isso já vai além do aceitável."

            "..."

            scene black with dissolve

            "..."

            "..."

            scene banho_zen entrada with Dissolve(1.0)

            mc normal "Só tenho a agradecer como sempre, [li]."

            show liling rindo with dissolve

            li "Se gostou é que importa."

            mc "E obrigado pela história também. Com certeza vou visitar o Portal de Pedra e procurar a He Xiangu."

            li "Boa sorte, senhor [mc]. Depois volte aqui para outro banho de saúde e beleza."

            mc normal "Pode deixar."

            "Como é mesmo?"

            menu:
                "Zaijian":


                    $ renpy.block_rollback()

                    mc envergonhado "Zaijian, [li]."

                    li "Zaijian"
                "Ziajin":


                    $ renpy.block_rollback()

                    mc envergonhado "É... Ziajin."

                    li "É Zaijian, senhor [mc]."

                    mc "Ah! Isso aí!"

        elif banho_evento == 4:

            li "Vou preparar o banho."

            mc envergonhado "[li]!"

            show liling normal with dissolve

            li "Que foi, senhor [mc]?"

            mc "Posso preparar o banho com você hoje?"

            li "..."

            show liling rindo with dissolve

            li "Claro. Venha."

            mc normal "Legal."

            hide liling with dissolve

            "..."

            scene c_chinesa ofuro with Dissolve(1.0)

            li "Fique à vontade."

            mc normal "Ok."

            mc envergonhado "Então... Eu conversei com a [xu] e disse pra ela que você mandou um beijo."

            li "Muito obrigada!"

            "Eu nem tenho vergonha de mentir assim na cara dura..."

            mc normal "Também conversei com o [chi] e ele me disse que ela realmente é a [xu] da lenda."

            li "Viu só. Eu te disse, senhor [mc]."

            mc "É..."

            show liling falando with dissolve

            li "Agora calma. Banho está pronto. Relaxe."

            mc envergonhado "Ah, ok..."

            mc "É... você pode me fazer companhia de novo? Igual da outra vez?"

            li "..."

            li "Só se senhor prometer que vai relaxar enquanto conversa."

            mc charmoso "Combinado."

            li "Se apronte e entre no banho."

            hide liling with dissolve

            mc envergonhado "O-ok..."

            "Sei lá o que ela pensa, mas não é fácil tirar a roupa e colocar aquela sunguinha na frente dela..."

            "..."

            mc "Vou entrar."

            scene banho_chines liling_conversando2 with Dissolve(1.0)

            pause

            mc "Aaahh...."

            mc "Já tava com saudades, [li]. Seu banho mágico é incrível..."

            li "Banho de saúde e beleza é melhor que existe."

            "Eu sinto que a gente tá conversando cada vez mais naturalmente, mas ainda não é o suficiente."

            "Quero encher ela de perguntas sobre a [xu]. Preciso descobrir quando ela conheceu a garota. Tenho que descobrir quando tudo isso começou."

            "Como aquela garota conseguiu fazer que todos acreditassem que ela é imortal e vive há milhares de anos..."

            mc "Hmmmm...."

            "Acho que eu tive uma boa ideia."

            mc "[li]."

            li "Senhor?"

            mc "Você aceitaria tomar um banho comigo?"

            scene banho_chines liling_conversando with vpunch

            li "Senhor [mc]?!"

            "Meu principal objetivo aqui, além de relaxar, é conseguir informações sobre a [xu]."

            "Mas se pintar uma chance com a [li], será que eu aproveito?"

            menu:
                "Sim. Quero algo mais com a [li]":


                    $ liling_seducao = True

                    "Obviamente não vou perder a chance."

                    mc "Eu adoraria ter sua companhia aqui comigo."

                    li "Senhor [mc]..."

                    mc "Você deixaria seu cliente muito mais satisfeito..."

                    li "..."
                "Não. Só quero as informações.":


                    mc "Não-não! Não é o que você tá pensando!"

                    mc "Só quero que você relaxe um pouco também. É o pedido de um cliente."

                    li "..."

            li "Ok... Se senhor quer..."

            if liling_seducao:

                mc "Eu adoraria. Aliás, qualquer homem iria querer a companhia de uma mulher como você."

                li "Você é muito cavalheiro, senhor [mc]."

                mc "Só tô falando a verdade."

            li "Vou me preparar."

            scene black with dissolve

            "..."

            li "Posso entrar?"

            mc charmoso "Claro."

            scene banho_chines liling_banheira with Dissolve(2.0)

            pause

            li "Hmmmm..."

            li "Incrível."

            if liling_seducao:

                "Uou... ela colocou esse biquini estranho. É realmente bem sexy."

                "Tenho que fazer ela me ver como algo mais que cliente se eu quiser algo com ela."
            else:


                "Uou, esse biquini é bem ousado."

            mc "Esqueceu como seu próprio banho é bom?"

            li "Fazia tempo que eu não tomava banho de saúde e beleza."

            if liling_seducao:

                mc "Você nem precisa. Saúde e beleza tão sobrando."

                li "Ai, senhor [mc]. Não fale essas coisas."

                mc "Não precisa me chamar de senhor. Só [mc] tá excelente."

                li "Não posso. Clientes são senhores."

                mc "..."

            mc "Então aproveite o banho. Porque eu com certeza vou."

            li "Hmmm..."

            "Ótimo. Era isso mesmo que eu queria. Quanto mais ela ficar à vontade comigo, maior a chance dela me contar o que eu preciso."

            "[xu]... A história dessa garota deve ser o maior mistério que eu já vi. Tão estranho... tão... de outro mundo."

            li "Senhor [mc]."

            mc "O-oi!"

            li "Você é melhor cliente de banho."

            mc "Haha. Sou o melhor cliente?"

            li "Sim. Senhor tem vindo bastante tomar banho de saúde e beleza."

            mc "É verdade. Mas é que o banho é incrível."

            li "Continue vindo."

            mc "Pode deixar, [li]."

            "..."

            li "Acho que banho acabou. Mas vamos ficar mais tempo."

            mc "Opa! Com certeza."

            "..."

            li "Agora temos que sair. Ficar tempo demais não é bom."

            mc "Sério? Qual o problema?"

            li "Magia de banho de saúde e beleza pode virar problema se ficar tempo demais."

            mc "Entendo..."

            "..."

            scene c_chinesa ofuro with Dissolve(1.0)

            mc "Vou indo nessa."

            li "Zaijian, senhor [mc]."

        elif banho_evento == 5:

            li "Eu adorei nosso banho aquele dia."

            mc charmoso "Eu também. O que acha da gente fazer de novo?"

            show liling falando with dissolve

            li "..."

            li "De novo?"

            if liling_seducao:

                mc charmoso "Eu adorei dividir a banheira com você."

                mc safado "Ainda mais com aquele biquini que você usou."

                li "Fundoshi roupa certa para tomar banho de saúde e beleza."

                mc "Você ficou incrível nele. Não sei se você ou a água estava mais gostosa..."

                show liling rindo with dissolve

                li "Senhor [mc] me elogia demais."

                mc charmoso "..."
            else:


                mc normal "Claro. Você não gostou?"

                li "Gostei, mas-"

                mc "Não esquente demais. Fui eu que pedi."

                show liling rindo with dissolve

                li "Certo."

            mc charmoso "Então vou querer companhia na banheira novamente, hein."

            li "Tá."

            li "Vou me preparar e preparar banho."

            mc "Perfeito."

            hide liling with dissolve

            "As coisas estão caminhando muito bem com ela. Hoje vou aproveitar e perguntar sobre a [xu]."

            "..."

            li "Senhor [mc]. Pode vir."

            "..."

            show c_chinesa ofuro with Dissolve(1.0)

            mc surpreso "!"

            show liling f_envergonhada with dissolve

            li "..."

            if liling_seducao:

                mc safado "Você está maravilhosa, [li]."

                li "Obrigada."

                mc "Não vejo a hora de entrar na banheira com você."

                li "..."
            else:


                mc envergonhado "Esse biquini é bem diferente."

                "Que vergonha... eu consigo ver quase tudo..."

                li "Fundoshi é roupa certa para tomar banho de saúde e beleza."

                mc "Entendo..."

            li "Se troque e vamos entrar."

            mc charmoso "Vamos."

            hide liling with dissolve

            "..."

            scene banho_chines liling_banheira with Dissolve(1.0)

            pause

            li "Estava com saudades de banho de saúde e beleza."

            li "Magia é incrível... só é possível graças a [xu] que traz ervas do monte Penglai."

            mc "Ah! Já que você tá falando sobre ela..."

            mc "Quando você conheceu a [xu] pela primeira vez?"

            li "Hmmm... faz algum tempo que conheci [xu]. Não muito, mas alguns anos."

            mc "Faz pouco tempo que você mora na Cidade Chinesa?"

            li "Não, não. Eu nasci aqui."

            mc "Então como você só conheceu a [xu] há apenas alguns anos?"

            li "[xu] é imortal que viaja por montes e montanhas. Ela voltou para Cidade Chinesa alguns anos atrás."

            mc "Ela ficou por décadas fora da cidade?"

            li "Sim. Eu vi ela quando era criança, e depois só agora, há alguns anos."

            "Então ela esteve fora por décadas..."

            "Só que o mais incrível é que ela viu a [xu] quando era criança, e depois de décadas..."

            mc "[li]."

            li "Senhor?"

            mc "Você viu a [xu] quando era criança e depois de décadas, certo?"

            li "Isso."

            mc "Ela tava exatamente igual?"

            li "Sim. A aparência dela nunca mudou, desde que foi visitada por deus que transformou ela em imortal."

            mc "Entendi."

            "Haha! Devo tá ficando louco. Não é possível que a aparência de uma pessoa não mude depois de dezenas de anos."

            li "Hmmm!"

            li "Adorei banho, senhor [mc]. Obrigada pelo convite."

            if liling_seducao:

                mc "Mas já? Não aceita uma massagem?"

                li "Nã-não, senhor. Não posso. Mas obrigada pelo convite."

                mc "Uma pena. Eu adoraria poder massagear você."

                li "..."

            li "Aproveite resto de banho de saúde e beleza."

            mc "Opa."

            "..."

            scene banho_chines mc2 with Dissolve(1.0)

            "Tudo que eu escuto... as histórias... os depoimentos de cada morador da Cidade Chinesa."

            "Tudo aponta pra que a garota do portal de pedra é a verdadeira [xu] da lenda."

            "Só que eu não vou comprar essa loucura. Isso contraria a ciência completamente. Deve ter alguma sacada. Alguma coisa que não tô vendo."

            "Mas não tenho mais a quem recorrer."

            "Não ten-"

            "???" "Psiu!"

            mc "Ah?"

            "???" "Aqui."

            show c_chinesa ofuro with Dissolve(1.0)

            mc desconfiado "Quem é?"

            show kaira nervosa with dissolve

            ka "Oi."

            mc surpreso "!"

            "Essa garota!"

            ka "Não acredite em nada que ela fala."

            mc desconfiado "A [li]?"

            ka "Sim. Ela é louca. Todos eles são loucos."

            mc "Como assim?"

            ka "Não posso falar muito agora. Só que a senhora e todos os outros chineses. Eles são malucos."

            ka "Eles acreditam que a garota é um tipo de deusa. Mas isso é mentira."

            ka "Tem que ser..."

            mc desculpa "Você tem toda a razão. 'Tem que ser' loucura. Mas tudo tá indicando que não é."

            ka "O velho do lámen!"

            mc desconfiado "[chi]?"

            ka "Ele mesmo. Fale com ele. Ele sabe uma coisa importante. Eu escutei ele falando uma vez."

            "O [chi] sabe alguma coisa..."

            mc desculpa "Ok. Obrigado pela dica. Vou falar com ele."

            ka "Depois que descobrir as coisas, volte aqui. Eu preciso de você."

            mc desconfiado "Hã?"

            li "Senhor [mc]! Seu tempo!"

            ka "A senhora!"

            hide kaira with dissolve

            mc "..."

            mc normal "Obrigado pelo aviso, [li]."

            "Então eu preciso falar com o [chi] sobre isso. Ele tá escondendo algo de mim."

            "Ou melhor... ele não falou alguma coisa importante sobre a [xu] quando eu perguntei pra ele."

            "Preciso falar com ele de novo. Provavelmente, vou precisar ainda mais da confiança dele até ele se abrir comigo."

            scene banho_zen entrada with Dissolve(1.0)

            mc charmoso "Valeu por tudo."

            show liling rindo with dissolve

            li "Continue vindo para banho especial."

            mc "Com certeza."

            if liling_seducao:

                mc charmoso "Mas só se você tomar banho comigo de novo."

                li "Tá..."

                mc "E aceitar eu fazer uma massagem em você."

                li "Senhor [mc]!"

                mc charmoso "Vou continuar tentando até você aceitar."

                li "..."

            mc "Zaijian, [li]."

            li "Zaijian."

        elif banho_evento == 6:

            li "Vou preparar banho como de costume."

            if liling_seducao:

                mc charmoso "O que você acha de fazer um agrado pra mim e se vestir com aquela roupa que você tomou banho comigo?"

                li "Senhor, [mc]..."

                mc "Por favor?"

                li "Certo."

            li "Fique aqui e logo chamo."

            mc normal "Ok."

            hide liling with dissolve

            "Eu preciso dar um jeito de me encontrar com aquela menina da outra vez."

            "Ela disse que depois de eu resolver o lance da [xu] ela ia querer falar comigo. Pra que será?"

            "Certeza que ela sabe mais do que ela me disse da outra vez."

            li "Senhor, [mc]! Está pronto!"

            mc normal "Tô indo."

            "Tenho que convencer a [li] a me deixar ver ela."

            scene c_chinesa ofuro with Dissolve(1.0)

            if liling_seducao:

                mc surpreso "!"

                show liling f_envergonhada with dissolve

                li "[li] está pronta para senhor."

                mc tarado "Que bom que você tá vestida assim, porque você vai vir no banho comigo."
            else:


                show liling rindo with dissolve

                li "Banho está pronto."

                mc normal "Muito obrigado."

                mc charmoso "Mas eu quero que você venha no banho também."

            li "Ok, senhor [mc]. [li] faz tudo para clientes."

            if liling_seducao:

                mc safado "Nem vem que eu sei que você gosta de entrar lá comigo."

                li "Talvez..."

                mc "..."

            li "Cliente primeiro."

            scene banho_chines liling_banheira with Dissolve(1.0)

            mc "Aahh... uma delícia como sempre."

            li "Banho de saúde e beleza é melhor banho de todo mundo."

            mc "Concordo..."

            "..."

            "Eu tenho que puxar o assunto com ela."

            mc "Aliás... [li]... você pode me dizer uma coisa?"

            li "Ver perguntar sobre [xu] de novo?"

            mc "Haha! Não..."

            mc "Eu queria saber mais sobre a menina que trabalha aqui..."

            li "Oohh... então senhor [mc] ouviu sobre serviços especiais..."

            mc "Serviços especiais?"

            li "Serviços especiais são para bons clientes e senhor [mc] é bom cliente."

            mc "Ah..."

            "Ainda não entendi o que ela quer dizer."

            $ ka_nome = "Kaira"

            li "Vou falar com [ka] e no seu próximo banho você pode ter serviços especiais."

            mc "[ka]?"

            li "Sim, garota que você falou."

            mc "Ah! Então ela oferece serviços especiais?"

            li "Sim, sim. Banho de saúde e beleza não é único serviço de casa. Senhor vai gostar, estou certa."

            mc "Ok."

            li "Agora [li] vai sair e deixar o senhor aproveitar."

            if liling_seducao:

                mc "Mas eu aproveito muito mais você com aqui..."

                li "... [li] fica então."

                mc "Talvez você pudesse até se aproximar um pouco mais."

                li "Senhor [mc]..."

                li "Talvez em próximo banho."

                mc "Tá."
            else:


                mc "Ok. Obrigado pela companhia, [li]."

                li "Agradecida."

                scene banho_chines mc1 with Dissolve(1.0)

                "Deixa eu relaxar agora..."

            scene black with Dissolve(1.0)

            "..."

            scene banho_zen entrada with Dissolve(1.0)

            mc charmoso "Incrível, como sempre, [li]."

            show liling rindo with dissolve

            li "Fico feliz que tenha gostado, senhor [mc]."

            li "Próxima vez, se prepare para serviços especiais, tudo bem?"

            mc "Pode deixar."

            mc "Zaijian."

            li "Zaijian, senhor."

        elif banho_evento == 7:

            li "Preparado para serviços especiais hoje?"

            mc charmoso "Opa."

            li "Vou chamar [ka] e ela cuidará de você."

            mc "Ok."

            hide liling with dissolve

            "Que serviços especiais serão esses? Do jeito que ela fala parece até que ela vai chamar uma prostituta."

            mc envergonhado "Eu não sei se eu quero esse tipo de serviço..."

            li "Senhor, [mc]?"

            mc surpreso "Nã-não! É mentira! Digo! É verdade!"

            show liling falando with dissolve

            li "Senhor está bem?"

            mc envergonhado "Haha... sim."

            li "Ela está preparando cama e logo vai te atender. Pode ir para lá."

            mc surpreso "Cama?!"

            li "Sim. Onde senhor espera receber serviço especial?"

            mc envergonhado "Li-li-ling... eu não sei se eu quero esse tipo de serviço."

            li "Mas senhor [mc] disse que queria."

            if priscila_namoro or sayuri_namoro or julia_namoro or maria_namoro:

                mc "N-na verdade eu já sou um rapaz comprometido e-"

            li "Agora serviço pago e cama quase pronta. Vai logo."

            mc surpreso "[li]!"

            scene c_chinesa ofuro with Dissolve(1.0)

            mc envergonhado "O-oi..."

            show kaira nervosa with dissolve

            ka "O-oi."

            ka "O senhor tá pronto?"

            mc "Então-"

            li "E vou deixar dois sozinhos. Bom serviço, garota."

            ka "Senhor, por favor tire suas roupas para eu começar."

            mc surpreso "!"

            ka "Eu vou ajudar o senhor."

            hide kaira with dissolve

            mc "O-o que você tá fazendo?!"

            ka "O senhor parece um pouco nervoso. Mas isso é normal, ok?"

            ka "Alguns clientes preferem fechar os olhos a primeira vez."

            mc "E-eu!"

            hide black with dissolve

            mc concentrando "O-ok... Mas é que-"

            ka "Xxxiiiiuuu..."

            "Meu Deus, onde eu me meti?"

            ka "Agora deite aqui."

            mc "Ok."

            ka "Eu vou começar devagar... pegando aqui."

            mc surpreso "!"

            scene kaira_massagem1 with Dissolve(1.0)

            pause

            ka "O que o senhor tá achando?"

            mc "Hm?"

            ka "Da massagem. Está doendo ou desconfortável?"

            mc "Ah! Está boa..."

            ka "Que bom. Você vai ver que a massagem especial do banho da [li] é a melhor do mundo."

            "Haha! Então era disso que elas tavam falando..."

            "Que idiota que eu fui."

            if mc_massagem > 0:

                mc "Ah. Quero só ver. Eu estudei massagem também."

                ka "Verdade? Isso é interessante."

                mc "Minha professora é uma doida lá, mas ela parece conhecer bastante."

                ka "Entendi."
            else:


                mc "Eu tô gostando bastante. Você tá mexendo nos pontos certos."

                ka "Que bom."

            mc "Então sua função no banho é fazer massagem?"

            ka "Sim. Alguns clientes, igual o senhor, que se tornam frequentes no banho ganham esse serviço especial."

            mc "Tenho que te falar que eu pensei que era outra coisa haha..."

            ka "Sei..."

            mc "Mas a massagem tá realmente boa."

            ka "Que bom."

            "Tá boa de verdade..."

            "Hmm..."

            show black with dissolve

            hide black with dissolve

            "Opa."

            ka "Acordou?"

            mc "Como?"

            ka "O senhor dormiu por uns 20 minutos."

            mc "QUÊ?! Eu só pisquei os olhos."

            ka "Isso é normal. Pode se levantar."

            scene c_chinesa ofuro with Dissolve(1.0)

            "Mano... como assim eu dormi?"

            show kaira nervosa with dissolve

            ka "Venha mais vezes, senhor."

            mc desconfiado "Aquele lance que você me falou. O [chi] acabou me ajudando."

            mc "Tudo parece muito estranho, mas a [xu] realmente acredita que ela é uma lenda de verdade."

            ka "..."

            ka "Venha e da próxima vez conversamos."

            mc normal "Ok. E obrigado pela massagem."

            ka "!"

            ka "D-de nada..."

            hide kaira with dissolve

            "O que deu nessa garota?"

            scene banho_zen entrada with Dissolve(1.0)

            mc normal "Pronto, [li]."

            show liling normal with dissolve

            li "Muito bem, senhor [mc]? [ka] te tratou bem?"

            mc charmoso "Sim, ela foi incrível."

            show liling rindo with dissolve

            li "Isso isso. Menina precisa aprender fazer bem para clientes. Ela aprende."

            mc normal "Depois eu volto pra outro banho."

            li "Sim, volta. Serviços especiais vão te esperar."

            mc normal "Até."

        elif banho_evento == 8:

            li "Hoje senhor vai querer banho de saúde e beleza ou serviços especiais?"

            mc concentrando "Hmmm..."

            "Acho melhor eu continuar falando com a [ka]. Eu preciso ter certeza que ela não sabe mais nada sobre a [xu]."

            "Qualquer coisa que me ajude a pressionar o [chi] a falar. Porque eu estou certo que ele sabe de algo."

            mc normal "Vou querer serviços especiais."

            li "Muito bem. Chamarei [ka] e ela prepará tudo."

            mc "Ok."

            hide liling with dissolve

            "Da primeira vez que a gente conversou, a [ka] disse que ouviu a [li] e o [chi] conversando. Ela pode ter escutado alguma outra coisa."

            mc angustiado "Eu espero..."

            li "Senhor [mc]. Garota está pronta."

            mc surpreso "Opa!"

            scene c_chinesa ofuro with Dissolve(1.0)

            li "Vou deixar vocês."

            mc normal "Oi, [ka]."

            show kaira nervosa with dissolve

            ka "Oi. Pronto?"

            mc "Sim."

            ka "Pode se deitar por favor."

            scene kaira_massagem1 with Dissolve(1.0)

            pause

            mc "Eu adoro sua massagem."

            ka "Que bom."

            "Tenho que tomar cuidado pra não apagar igual da outra vez."

            mc "[ka], eu queri-"

            ka "Senhor, por favor. Podemos conversar depois da massagem. Pra mim é importante que o senhor receba os benefícios do serviço especial."

            mc "T-tá."

            mc "Vou tentar relaxar."

            ka "Isso."

            "Na verdade não precisa de muito pra relaxar neste lugar..."

            "Eu só tenho que ficar quieto e tentar não... pensar..."

            show black with dissolve

            pause

            scene kaira_massagem0 with hpunch

            li "{size=17}Já disse que não!{/size}"

            "Uou! O que aconteceu?!"

            ka "{size=17}Por que não?{/size}"

            li "{size=17}Eu sei que você tá tramando alguma, menina.{/size}"

            "Parece que a [li] e a [ka] tão brigando."

            "Mas ela tava aqui comigo até agora. Eu só pisq..."

            "Então eu realmente dormi... Mas como?"

            ka "{size=17}E-eu não tô tramando nada, senhora.{/size}"

            li "{size=17}Não posso provar, mas eu sei. Sei que você anda fazendo coisas com clientes.{/size}"

            ka "{size=17}Coisas?{/size}"

            li "{size=17}Não se faça de burra, garota! Eu sei! Clientes falam coisas estranhas. Você tá fazendo coisa que não pode com eles!{/size}"

            ka "{size=17}Não tô! Isso é mentira!{/size}"

            li "{size=17}Senhor [mc] é excelente cliente e não quero que você faça nada com ele. Estou de olho em você!{/size}"

            ka "{size=17}A senhora não pode se intrometer no serviço especial. Isso vai acabar com tudo!{/size}"

            ka "{size=17}Foi a senhora que me ensinou isso!{/size}"

            li "{size=17}Sei... mas não confio mais em você. Mesmo que atrapalhe, vou estar sempre de olho.{/size}"

            ka "{size=17}Isso não é justo! Eu te odeio!{/size}"

            li "{size=17}Não importa. Eu não comprei você pra você gostar. Agora pare de gritar ou você vai acordar senhor [mc].{/size}"

            ka "{size=17}DROGA!{/size}"

            "..."

            ka "Senhor?"

            "Melhor eu fingir que tava dormindo."

            mc "O-oi... Eu dormi de novo?"

            ka "Sim, senhor. Você pode levantar?"

            mc "Claro."

            scene c_chinesa ofuro with Dissolve(1.0)

            mc desconfiado "Aconteceu alguma coisa?"

            show kaira nervosa with dissolve

            ka "Eu queria saber se o senhor deseja receber {b}massagens especiais{/b}..."

            mc "Como assim?"

            ka "Nós temos um serviço de massagem especial... onde eu faço massagem em outros lugares ao invés das costas..."

            mc envergonhado "[ka]... é o que eu tô pensando que é? Tipo uma massagem com final feliz?"

            ka "N-não sei do que o senhor está falando..."

            mc desconfiado "Certo..."

            ka "Se você quiser, fale pra senhora [li] que você deseja os serviços especiais da próxima vez e daí conversamos."

            mc preocupado "Você tá legal? Você não parece normal."

            ka "Ah! E-eu tô... Só faça isso por favor. Agora vai antes que ela venha aqui."

            mc desculpa "Ok. Conversamos mais da próxima vez."

            ka "Tá."

            hide kaira with dissolve

            "O que será que foi isso agora?"

            scene banho_zen entrada with Dissolve(1.0)

            mc envergonhado "Estou de volta."

            show liling rindo with dissolve

            li "Senhor [mc]. Espero que tudo tenha sido muito bom."

            mc normal "Foi sim. A [ka] está fazendo um excelente trabalho."

            li "Muito bom. Só que esse foi seu último serviço especial infelizmente."

            mc desconfiado "Como assim? Eu fiz algo de errado?"

            show liling falando with dissolve

            li "Não, não, senhor [mc]. De forma alguma."

            li "A [ka]... ficará tempo sem prestar serviço e por isso não ofereceremos serviços especiais por enquanto."

            mc desculpa "Entendi... que coisa."

            show liling rindo with dissolve

            li "Mas voltaremos assim que possível. E banho de saúde e beleza sempre estará aqui para senhor."

            mc normal "Ok. Obrigado, [li]. Zaijian."

            li "Zaijian, senhor [mc]."

            scene chinatown superior with Dissolve(1.0)

            "Hmmm..."

            "Com certeza aconteceu alguma coisa. Alguma coisa com elas."

            "Não adianta eu voltar aqui só pelo banho. Preciso dar um jeito de falar com a [ka]."

            "{b}Talvez o [chi] possa me ajudar{/b}. Ele deve saber alguma coisa sobre a relação dessas duas. Ele sabe de tudo que acontece aqui."

            "Só espero que ele não venha com graça de que eu ainda não estou pronto."

        elif banho_evento == 9:

            $ banho_liling = False
            $ banho_kaira = False

            "Eu vou tomar o banho normal. É o jeito."

            "Por mais que eu queira falar com a [ka]... eu tenho que convencer a [li] antes."

            "Claro que ela tá escondendo alguma coisa aqui. O [chi] também não quis me contar. Que porra será que tá rolando?"

            "Mas antes a [li]. Ou é melhor eu entrar lá e durante o banho procurar a [ka]? Parece uma boa opção também..."

            li "Senhor? Perdeu fala?"

            mc surpreso "N-não!"

            li "Muito bem. Vou preparar banho de saúde e beleza. Chamo logo mais."

            if liling_seducao:

                mc charmoso "Você vai entrar comigo de novo, né?"

                li "S-senhor [mc]..."

                mc "Meu banho não vai ser a mesma coisa sem você lá, [li]."

                li "Senhor impossível... [li] vai pensar."

            mc charmoso "Ok. Quando tiver pronto, pode me chamar."

            scene banho_zen entrada with Dissolve(1.0)

            "Certo... eu preciso chegar até a [ka]. Esse precisa ser meu maior objetivo aqui."

            if liling_seducao:

                "Se bem que tomar banho com a [li] não é assim uma meta ruim, não... talvez mudança de planos?"

                "Não! Preciso me concentrar!"

            "Eu tenho duas formas de procurar a [ka]. Pelo menos que vem na minha cabeça agora."

            "A primeira é convencendo a [li]. Eu pediria pra ela ir pra banheira comigo, eu fazia um charme com ela e tento convencer ela."

            "A outra possibilidade é não chamar ela... fingir que eu tô tomando banho e tentar procurar a [ka]."

            "Qual das duas estratégias será que é melhor?"

            li "Senhor [mc]. Banho de saúde e beleza está pronto."

            mc normal "Opa! Tô indo."

            scene black with dissolve

            "..."

            scene banho_chines liling_conversando2 with Dissolve(1.0)

            pause

            li "Banho bom?"

            mc "Uma delícia, igual sempre."

            li "Muito bom."

            "E agora? O que eu faço? Qual caminho eu escolho?"

            menu:
                "Eu quero que você venha comigo.":


                    $ banho_liling = True

                    mc "Vem aqui deitar comigo."

                    li "Não sei, senhor [mc]..."

                    mc "Eu tô pagando por esse banho. Eu quero a experiência completa."

                    li "Desde quando [li] faz parte?"

                    mc "Pra mim você virou o principal."

                    li "Senhor [mc]..."

                    li "Tudo bem. [li] vai entrar."

                    mc "Opa! Por favor."

                    scene black with dissolve

                    "..."

                    scene banho_chines liling_banheira with Dissolve(1.0)

                    pause

                    mc "Agora sim... esse é o banho que eu queria tomar."

                    li "Banho bom."

                    mc "E eu consigo sentir você aqui no meio também..."

                    li "Senhor!"

                    mc "Você é uma delícia... mais gostosa ainda que o banho, [li]."

                    li "Senhor [mc] bom cliente, bom homem."

                    mc "Obrigado."

                    li "Hmm..."

                    mc "[li]... agora que você tá descansada... posso te perguntar uma coisa?"

                    li "Que foi?"

                    mc "Eu trabalho numa revista bem grande aqui da capital. E eu queria falar sobre seu banho."

                    li "Ohh!"

                    mc "Isso atrairia muitas pessoas pra cá. Acho que seria muito legal pra você e pra Cidade Chinesa."

                    li "Sim. Muito bom. Muito bom."

                    mc "Mas eu precisava saber mais sobre os serviços especiais. Eu tenho que passar todas as informações pros meus leitores."

                    li "[li] disse não..."

                    "O banho realmente relaxou ela..."

                    mc "Mas você vai perder essa matéria então?"

                    li "Ora..."

                    li "Garota [ka] perigosa. Difícil saber que ela vai falar..."

                    mc "Entendo... mas eu prometo que eu não vou fazer nada que seja ruim pra você. Eu quero que o banho continue."

                    mc "E eu quero impressionar você também..."

                    li "Ora ora... banho de saúde e beleza pode ter me amolecido... era tudo plano, senhor [mc]?"

                    mc "Opa! Você vai concordar?"

                    li "[li] vai concordar..."

                    mc "Boa!"

                    li "Mas com condição... você fica com [li]. Não pode proteger [ka]."

                    mc "Combinado. Não se preocupe, que eu não quero nada com a garota."

                    li "Então hora de banho..."

                    if not nathan_namoro:

                        "Perfeito. Vou aproveitar pra passar a mão nela... a [li] tá entrando na minha."
                    else:


                        "Perfeito!"

                    "Agora na próxima é só falar com a [ka]. Eu prometi ficar do lado da [li]..."

                    "Como assim ficar do lado dela? O que será que ela quer dizer?"

                    "Bom... bora descansar."
                "Está tudo bem. Vou relaxar agora.":


                    $ banho_kaira = True

                    mc "Eu tô bem aqui. Vou tomar um banho sozinho e relaxar."

                    li "Excelente ideia, senhor cliente. Qualquer coisa que precisar, chame [li]."

                    mc "Pode deixar. Vou chamar, sim."

                    li "Até mais."

                    scene banho_chines mc1 with Dissolve(1.0)

                    pause

                    "Ok... ela foi embora. Agora eu preciso achar a [ka]."

                    "Ela deve tá por aqui em algum lugar."

                    "Tem uma porta ali que é onde as pessoas trocam de roupa. Eu nunca entrei ali."

                    "Deve ser por lá que os funcionários entram. Se eu conseguir chegar até ali e chamar a [ka]... talvez dê certo..."

                    "Eu tenho que tentar."

                    scene c_chinesa ofuro with Dissolve(1.0)

                    pause

                    mc "É aqui..."

                    mc "[ka]! [ka]!"

                    "..."

                    mc "[ka]! Tá me ouvindo!?"

                    li "Senhor [mc]?! Tá me chamando?!"

                    mc "Q-quê? N-não... tô quase dormindo aqui."

                    li "Desculpa, senhor. [li] vai ficar quieta."

                    mc "V-valeu..."

                    ka "Tem alguém me chamando?"

                    mc "Sou eu! O cara que você falou no outro dia."

                    ka "Era... Heleniano?"

                    if mcpnome == "Heleniano":

                        mc "Isso! Você lembrou meu nome!"

                        ka "Não acredito que seu nome é Heleniano mesmo..."
                    else:


                        mc "Isso! Quer dizer! Não! [mc]!"

                        ka "Verdade..."

                    ka "O que você quer? A [li] me proibiu de atender os clientes."

                    mc "Eu quero os serviços especiais... mesmo sem ela saber."

                    ka "Você tá louco?"

                    mc "É sério. Deixa a cama preparada pra mim. E fica esperta que eu vou chamar você."

                    ka "Ma-mas... você sabe que eu vou cobrar, né? Mais ainda por causa disso."

                    mc "Cobrar? Mais?"

                    ka "Se a [li] me pegar eu tô fodida."

                    mc "Ok. Mas eu vou querer saber tudo sobre você e o que tá rolando aqui."

                    ka "Tá bom. Eu te conto tudo."

                    mc "Então tá. A gente se fala. Agora eu vou voltar pro banho."

                    ka "Você é louco..."

                    mc "Tchau!"

                    scene banho_chines mc2 with hpunch

                    mc "Ufa!"

                    li "Senhor [mc]?!"

                    mc "Q-quê?!"

                    li "Tudo bem?"

                    mc "Sim! Acho que eu acordei do nada."

                    li "Ok. Seu tempo acabou."

                    mc "Ah tá."

            scene black with dissolve

            "..."

            scene banho_liling1 with Dissolve(1.0)

            pause

            li "Gostou do banho?"

            mc "Foi perfeito, [li]. Obrigado como sempre."

            mc "Eu volto assim que der."

            li "Isso. Senhor [mc] bom cliente. Volte sempre."

            scene black with dissolve

            "Ok. Consegui um jeito de falar com a [ka]."

            "Da próxima vez eu vou descobrir o que tá rolando aqui."

        elif banho_evento == 10:

            $ ka_p1 = False
            $ ka_p2 = False
            $ ka_p3 = False
            $ kaira_especial = False
            $ kaira_especial2 = False

            if banho_liling:

                li "Você realmente vai querer os serviços especiais?"

                mc charmoso "Foi o que a genhte combinou da outra vez, certo?"

                li "Hmm... sim."

                li "Ok. Vou chamar a [ka] e pedir pra ela te atender."

                mc "Obrigado."
            else:


                li "Vou preparar banho pra você. Volto logo."

                mc "Combinado."

                li "Não ligue que a [ka] deixou o equipamento pra fora. Ela disse que precisava limpar."

                mc "Tudo bem. Eu não ligo."

                scene black with dissolve

                "..."

                li "Está pronto, [mc]."

                "Perfeito. Agora eu tenho que me livrar dela e chamar a [ka]."

                "Se a [li] me pegar eu tô ferrado."

                mc "Valeu, [li]. Pode deixar que eu me viro. Tô precisando de uma paz."

                li "Vou deixar o senhor em paz."

                mc "Obrigado."

                scene c_chinesa ofuro with Dissolve(1.0)

                "É agora."

                mc "[ka]. Vem aqui. [ka]!"

                ka "[mc]?"

                mc "Ufa. Vem."

            scene black with dissolve

            "..."

            scene banho_kaira_mc with Dissolve(1.0)

            pause

            mc "Oi. Finalmente a gente pode conversar."

            ka "Pois é..."

            if banho_liling:

                ka "Como você convenceu ela?"

                mc "Eu tenho meus jeitos."

                ka "Hmm..."
            else:


                mc "A gente tem que tomar muito cuidado."

                ka "Difícil ela vir pra cá. Só a gente não exagerar."

                mc "Beleza."

            ka "Agora... por que todo esse esforço? Só pra falar comigo? Ou você quer sua massagem especial mesmo?"

            mc "Massagem... t-talvez.... mas eu tô interessado de verdade no que tá rolando aqui."

            ka "Por que você quer tanto saber disso? Qual é sua intenção insistindo tanto assim?"

            mc "Tem pessoas que eu gosto que tão envolvidas nesse rolo da Cidade Chinesa."

            mc "Eu queria poder liberar elas disso."

            ka "Hmm..."

            mc "E não é só isso. Eu sou um jornalista. Meu trabalho é descobrir coisas e levar pras pessoas."

            ka "Tudo bem... você tem suas coisas então."

            mc "Sim. E aí? O que você pode me falar? Não foi fácil e nem barato chegar aqui. Eu preciso de alguma informação."

            ka "Se eu souber de alguma coisa eu te falo. O que você quer saber?"

            mc "Cara... tem tanta coisa que eu quero saber."

            ka "Tipo?"

            mc "Sua relação com a [li] por exemplo."

            ka "Eu não quero falar sobre isso."

            mc "Mas voc-{nw}"

            ka "Não. Isso não. Nada que tem a ver comigo."

            label kaira_perguntas:

                pass

            if banho_evento < 13:

                mc "Ok... Deixa eu pensar..."

                "Eu tenho que ver o que é mais importante pra mim agora."

                "O que eu pergunto?"

            menu:
                "Eu quero saber sobre você e a [li].":


                    if ka_p1 and ka_p2 and ka_p3:

                        ka "Sério que você tá perguntando isso outra vez?"

                        mc "É sério. E hoje eu quero uma resposta."

                        ka "Não sei, [mc]... não sei o que você quer fazer com isso."

                        mc "Eu só quero saber. Meu trabalho na revista é descobrir as coisas. Só isso."

                        ka "Você é só um xereta então? Essa é sua profissão?"

                        mc "Não é assim... bom... pensando bem até que faz sentido. Mas é porque é de interesse público."

                        ka "O que minha vida tem de interesse público?"

                        mc "Por isso que eu tenho que saber."

                        ka "Muito engraçado."

                        mc "É sério... a verdade é que o [chi] disse que você vivia uma situação complicada com a [li]."

                        ka "Ele disse?"

                        mc "Sim. Depois que ele falou isso aí eu fiquei pensando que tinha que saber o que era. Que iria me ajudar a entender tudo."

                        ka "Então... talvez você tenha razão..."

                        ka "Bom..."

                        scene banho_kaira1 with Dissolve(1.0)

                        pause

                        ka "A verdade é que eu não sou filha da [li]. Acho que dá pra perceber, né?"

                        ka "Desde criança eu vivo aqui. Eu sempre pensei que a [li] fosse minha mãe adotiva ou alguma coisa assim."

                        ka "Eu sempre estive aqui, mas era bem diferente dela. Só que ela nunca me explicou como que eu cheguei até aqui."

                        ka "Daí um dia eu escutei uma conversa dela com alguém que eu não sabia quem era. Não era da Cidade Chinesa."

                        ka "Era uma mulher ruiva. Ela tava de óculos escuros e eu nunca tinha visto ela antes. E tipo ela nunca veio aqui de novo."

                        ka "Ela brigou com a [li] por um tempão. Ela queria alguma coisa daqui. Ela disse que queria trocar alguma coisa de volta."

                        ka "Eu tentei de tudo pra descobrir o que aquela mulher tinha dado pra [li]. Mas eu não achei nada."

                        mc "Hmm..."

                        ka "Depois de um tempo... eu acho que eu descobri. Foi conversando com o [chi]."

                        ka "EU era a coisa que a mulher ruiva queria de volta."

                        mc "Quê?!"

                        ka "É! Eu acho que... ela era minha mãe, [mc]..."

                        mc "[ka]... como assim?"

                        ka "Não sei. Mas parece que minha mãe me deu pra [li]. Eu acho que ela se arrependeu e tentou me pegar de volta, mas daí era tarde."

                        ka "Bom... é essa a história."

                        mc "[ka]... valeu por me contar, mas... não é permitido uma pessoa 'negociar' outra desse jeito."

                        ka "Eu sei... mas é onde eu cheguei. Eu ouvi outras conversas da [li]. E teve o que o [chi] falou também."

                        ka "Não vai dar tempo de eu te contar tudo, mas pode acreditar em mim. Eu fui vendida... certeza que a [li] me comprou de algum jeito."

                        mc "Isso é muito sério, [ka]. Isso é contra a lei. A gente não pode aceitar isso assim."

                        ka "Eu sei. Mas eu tô dando meu jeito. Eu ainda quero conhecer a minha mãe, [mc]."

                        mc "[ka]..."

                        scene chinatown banho_kaira2 with Dissolve(1.0)

                        ka "Eu quero falar com ela e descobrir porque ela me deu pra [li]. Esse é meu sonho. Nem que seja falar com ela só uma vez."

                        mc "E como você vai fazer isso?"

                        ka "A [li] me disse que seu conseguir juntar C$ 30.000 ela ia deixar eu fazer o que quiser da minha vida."

                        ka "Eu tô juntando todos os dias que eu posso. Eu vou juntar essa grana e sair daqui."

                        mc "..."

                        "Não acredito que essa garota tá se vendendo com esses 'serviços especiais' pra juntar dinheiro pra sair daqui."

                        if kaira_especial:

                            "E eu idiota me aproveitei dela também. Eu sou um porco."

                        mc "Eu... nem sei o que falar, [ka]. Desculpa..."

                        ka "Você não fez nada, bobo. Pode ter certeza que eu ainda vou sair daqui. Você vai ver."

                        mc "Eu sei que você vai. Você é uma mulher obstinada."

                        ka "Valeu. Ah! E não vai abrir a boca por aí."

                        mc "Não se preocupe que seu segredo tá bem guardado comigo. Agora eu realmente entendo melhor tudo o que tá rolando aqui."

                        ka "Não sei como. Talvez você seja um gênio, porque pra mim não muda nada."

                        mc "Haha..."
                    else:


                        ka "De novo você tá perguntando isso? Eu já disse que não quero de falar isso com você."

                        ka "Eu nem te conheço direito..."

                        "Não adianta perguntar isso pra ela ainda... ela não quer falar sobre isso mesmo."

                        jump kaira_perguntas

                "A história da He Xiangu é verdade?" if not ka_p1:

                    $ ka_p1 = True

                    mc "Me fala o que você sabe sobre a [xu]."

                    ka "A verdadeira [xu] ou a doida que fica lá perto do templo?"

                    mc "Como é? Doida?"

                    ka "É. A garota realmente acredita que é a reencarnação de um tipo de deusa chinesa de milhares de anos atrás."

                    mc "Então... ela não é a [xu] de verdade? Ela não é imortal?"

                    ka "Você acreditou mesmo nessa baboseira?"

                    mc "Eu sei que é difícil... mas vai que, né? É bom ter certeza antes de falar alguma coisa."

                    scene banho_kaira1 with Dissolve(1.0)

                    pause

                    ka "Eu pensei que você fosse um cara inteligente..."

                    mc "Ei... a própria [li] disse que viu ela quando era pequena e agora vê ela e é igual."

                    ka "A [li]... ela tem os motivos dela pra aceitar essa tramoia."

                    mc "Então ela também faz parte? Ela tá enganando todo mundo?"

                    ka "Sim. A [li] pode não ser uma das escolhidas, mas ela com certeza tá do lado deles."

                    mc "Eles são aquelas pessoas que vivem na área reservada lá, né?"

                    ka "São eles que mandam no bairro. Eles que praticamente decidem o que vai acontecer com todo mundo aqui."

                    ka "As pessoas pagam pra eles 'administrarem' o bairro. Todo mundo aceita essa desgraça."

                    mc "Por que você acha que tão aceitando essa situação?"

                    ka "Eles usam a história da [xu] pra isso. Enquanto a galera comprar essa idiota de que tem gente enviada pelos deuses..."

                    mc "... eles vão aceitar a palavra deles como se fosse dos próprios deuses."

                    ka "Isso aí. E por isso que eles precisam manter a farsa viva."

                    ka "Se as pessoas descobrirem que não tem essa história da palavra dos deuses, eles vão parar de dar o dinheiro deles."

                    ka "O grupo ia perder a influência na hora. E a fonte de renda deles também."

                    mc "Esses caras são malucos..."

                    ka "E não adianta você querer se meter nisso. Eles vão te chamar de mentiroso. É muito tempo ouvindo a mesma história."

                    mc "Eu vou falar com a [xu] no portal. Ela tem que me ouvir."

                    ka "Só se você for mais maluco do que ela."

                    mc "Eu tenho que tentar pelo menos. Ela não parecia ser uma má pessoa."

                    ka "Complicado... não sei se ela tá no meio da mutreta ou se tá sendo enganada também."

                    ka "Só que mesmo assim, se você for atrás dela, é possível que ela acabe cortando sua cabeça fora."

                    mc "Q-quê?!"

                    ka "Pois é. Ela pode não ser a [xu] de verdade, mas eu ouvi falarem que ela é boa com a espada de verdade."

                    mc "Eita..."

                    ka "Mas a gente acabou falando demais já. Sua hora deve tá acabando."

                    mc "Verdade..."

                "Quem é a mulher que treina a [s]?" if not ka_p2:

                    $ ka_p2 = True

                    mc "Eu quero saber sobre a mulher que treina a [s]. Ela chama ela de Mestra. Não sei o nome dela."

                    ka "Sei."

                    mc "Como você sabe? Nem falei um nome."

                    scene banho_kaira_mc2 with Dissolve(1.0)

                    pause

                    ka "A [s] é super conhecida aqui, [mc]. Não é sempre que um bairro tem posse de uma campeã olímpica."

                    mc "Não é bem posse, né?"

                    ka "Eu sei. Mas ela é daqui. E ela é conhecida no mundo inteiro. A maior ginasta do país."

                    mc "Pois é. A [s] é incrível mesmo."

                    ka "E ela serve como propaganda também. Quem não quer ter um filho bem sucedido igual a [s]? É uma excelente promessa."

                    mc "Acho que eu entendi. É tipo colocar uma semente de girassol na frente de um rato pra ele ficar correndo na rodinha."

                    ka "É. Só que nesse caso o ratinho nunca vai pegar a semente. Não tem espaço e nem dinheiro pra todo mundo."

                    ka "Essa história do templo é só um jeito de fazer as pessoas fazerem o que eles querem. Coisas absurdas às vezes..."

                    mc "Caralho... parece um lance bem foda mesmo."

                    ka "Pode botar foda nisso."

                    mc "E a Mestre? Qual o papel dela nisso?"

                    ka "Eu não sei exatamente... mas eu escutei a [li] falando com algumas pessoas e alguns clientes comentarem também."

                    ka "Essa mulher teve uma carreira boa até na ginástica. Mas ela é boa mesmo em colocar a molecada na linha."

                    mc "Colocar na linha é o que eu tô pensando que é?"

                    ka "Se você tá pensando em porrada, negar comida, e todas essas coisas horríveis... então é."

                    mc "Meu Deus... tadinha da [s]... Por que os chineses fazem isso?"

                    ka "Olha, [mc]... eu sinto que isso não tem nada a ver com ser chinês."

                    mc "Não?"

                    ka "Tem muitos chineses legais aqui. Inclusive tem uma galera que nem concorda com as coisas que são feitas aqui."

                    mc "É. Pensando assim, o [chi], a [s], a [fen]... elas não parecem horríveis."

                    ka "A maioria não é. Por isso que eu acho que não tem a ver com a China ou os chineses. Pra mim, isso tem mais a ver com poder."

                    ka "Tipo, essa foi a forma que eles acharam de se manter como 'escolhidos', mandando e desmandando aqui."

                    mc "Faz sentido..."

                    ka "E essa treinadora do templo tá lá em cima. Ela manda em muita coisa aqui."

                    ka "Se você tá pensando em alguma loucura pra salvar esse povo..."

                    mc "Claro que eu tô."

                    ka "Sabia. Então você vai ter que encarar a velha uma hora ou outra. E ela é casca grossa. Pode deixar que eu vou no seu enterro."

                    mc "Ei..."

                    mc "Então a Mestra é uma das cabeças dos Escolhidos. E ela fez coisas horríveis com a [s]... Essa mulher não vai ser fácil."

                "Como o [chi] sabe tanto sobre tudo? Ele é algo aqui?" if not ka_p3:

                    $ ka_p3 = True

                    mc "Hoje eu quero que você me fale do [chi]. Ele sabe tudo o que acontece aqui. Quem é ele? E como ele sabe de tudo assim?"

                    ka "Esse velho... ele deve ser o cara mais legal que eu conheci nesse lugar..."

                    mc "Sério?"

                    scene chinatown banho_kaira2 with Dissolve(1.0)

                    pause

                    ka "Ele é bem legal mesmo."

                    mc "Essa parte eu entendi..."

                    ka "Ah, malz! É que acho que eu nunca vi alguém tratar os outros tão bem igual ele."

                    mc "Tá. Mas quem é ele?"

                    ka "Não sei... Acho que ninguém aqui sabe direito. O [chi] parece que veio antes de todo mundo."

                    ka "Todo mundo no bairro conhece ele e o carrinho de lámen, mas no fundo, ninguém sabe de onde ele veio."

                    ka "Tipo, ele tava aqui antes da [li]... e aparentemente até antes da Mestra. O velho é velho mesmo."

                    mc "Nossa... e ele nunca contou pra ninguém?"

                    ka "Eu já atendi alguns caras que trocaram ideia com ele, mas parece que ele é super reservado sobre a vida pessoal dele."

                    ka "Uma vez eu conversei com ele... ele tentou me ajudar uma vez... a fugir daqui."

                    mc "Fugir?"

                    ka "É. Mas lembra do que eu falei? Nada de falar sobre mim. E nem da [li] porque ela tem a ver comigo."

                    mc "Tá bom. Então o velho é velho. Bela informação."

                    ka "Calma. Eu não falei que eu acabei. Eu só não sei se eu quero falar dele pra você."

                    mc "Como assim? É o nosso acordo."

                    ka "Eu sei, pô. Mas é que eu não confio em você. E se você fizer alguma coisa contra ele?"

                    mc "Eu som bonzinho!"

                    ka "Foi o que o lobo mau falou pra vovó."

                    mc "Haha... verdade..."

                    menu:
                        "Eu prometo que não vou fazer nada.":


                            mc "Eu prometo que eu não vou fazer nada que vai prejudicar ele. É promessa mesmo."

                            ka "Eu vou lembrar disso, [mc]. Se você fizer alguma coisa, eu nunca vou confiar em você."

                            mc "Pode deixar. Eu prometo."

                            ka "Eu já tentei confiar em alguém antes e deu merda. Então acho bom você não me ferrar também."

                            mc "Pode deixar."
                        "É nosso acordo. Se vira.":


                            mc "A gente combinou que eu ia te pagar se você me desse as informações que eu precisava."

                            mc "Se você não vai falar, então eu não vou te dar nada."

                            ka "Espera! Não! Eu realmente preciso da grana!"

                            mc "Então..."

                            ka "Tá bom. Mas por favor não faz nada contra ele..."

                            mc "..."

                    scene banho_kaira_mc2 with Dissolve(1.0)

                    ka "O que eu sei é que... o [chi] já foi um dos Escolhidos também."

                    mc "Sério?!"

                    ka "Isso as pessoas mais velhas sabem, igual a [li]. Eu já ouvi ela comentando que ele fez parte, inclusive era um dos cabeças."

                    mc "Ele parece tão humilde... nunca pensei que fosse parte de alguma coisa assim."

                    ka "Eu também fiquei assim depois de pensar que talvez tenha sido ele que... deixa pra lá."

                    mc "Que ele o quê? Fala."

                    ka "Tipo... e se foi ele que começou tudo isso?"

                    mc "Você tá falando do lance dos Escolhidos e talz?"

                    ka "É... e se foi ele que começou tudo isso e daí se arrependeu? Daí pulou fora."

                    mc "Porra..."

                    ka "Mas ele é um cara legal, [mc]. Não vai fazer cagada, mesmo que seja alguma coisa assim."

                    mc "Eu vou ver, [ka]. Eu não acho o [chi] horrível, mas se ele é a causa disso tudo..."

                    ka "..."

            scene banho_kaira_mc with Dissolve(1.0)

            if banho_evento == 10:

                ka "Imagino que você vai querer o serviço especial agora..."

                mc "Se eu quiser, vou ter que pagar mais?"

                ka "Como assim? Você vai ter que pagar de qualquer jeito. O valor é pelo papo."

                "Serviços especiais... é um lance sexual com certeza..."

                "Será que eu vou querer isso?"

                menu:
                    "Vou querer com certeza.":


                        $ kaira_especial = True

                        mc "Já que eu vou pagar de qualquer jeito... claro que eu vou querer."

                        ka "Eu vou cuidar bem de você, [mc]."

                        mc "É o que eu tô esperando, [ka]."

                        ka "Pode deitar."

                        scene black with dissolve

                        "Opa..."

                        scene kaira_massagem1 with Dissolve(1.0)

                        pause

                        mc "Isso tá muito bom..."

                        if mc_massagem > 2:

                            mc "Tá até me lembrando uma amiga..."

                        ka "Valeu. Só que isso é só o começo. As coisas vão melhorar a partir de agor-{nw}"
                    "Não quero isso dela.":


                        mc "Deixa quieto. Não precisa."

                        ka "Sério mesmo? Valeu, [mc]. Você é... legal, sei lá."

                        mc "Não é nada... só não quero me aproveitar demais de você."

                        ka "Tá... mas você vai ter que pagar do mesmo jeito."

                        mc "Ouch."

                        mc "Ok... tá aqui."

                li "Senhor cliente!"

                mc "O-oi!"

                li "O tempo acabou!"

                mc "T-tá! Tô saindo!"

                ka "Ops. Melhor a gente continuar na próxima."

                mc "..."

                scene black with dissolve

                "..."

                scene banho_liling1 with Dissolve(1.0)

                li "Gostou?"

                mc charmoso "Adorei, [li]. Assim que der eu volto."

                li "Vou esperar senhor [mc]. Zaijian."

                mc normal "Zaijian."

            elif banho_evento == 11:

                if kaira_especial:

                    mc "E agora? Bora pros serviços especiais?"

                    ka "Sim. Mas antes o pagamento."

                    mc "Ai... vou ter que passar o resto do mês no miojo assim. O salário daquela revista mal paga as contas, guria."

                    ka "Fala menos e paga mais. Eu fiz minha parte."

                    scene black with dissolve

                    mc "Tá certa... Toma."

                    ka "Pode deitar."

                    scene kaira_massagem1 with Dissolve(1.0)

                    pause

                    ka "Hoje eu vou acelerar aqui atrás pra eu poder cuidar da sua frente."

                    mc "Da frente?"

                    ka "Vira que eu vou te mostrar."

                    mc "{i}gulp{/i}"

                    scene black with dissolve

                    scene chinatown kaira_massagem2 with Dissolve(1.0)

                    pause

                    mc "A-ah! K-kaira!"

                    ka "Calma... eu vou cuidar bem de você."

                    mc "..."

                    ka "Assim, isso... fica calmo."

                    mc "Você até que leva jeito."

                    ka "Obrigada."

                    mc "M-mais um pou-"

                    ka "Shiu..."

                    mc "!"
                else:


                    ka "Então você não vai querer mesmo os serviços especiais, né?"

                    mc "Não."

                    ka "Pode me passar a grana então."

                    mc "Ai... vou ter que passar o resto do mês no miojo assim. O salário daquela revista mal paga as contas, guria."

                    ka "Fala menos e paga mais. Eu fiz minha parte."

                    mc "Tá certa..."

                li "Senhor [mc]! Acabou tempo!"

                scene black with hpunch

                mc "A-ah! Ok!"

                ka "Melhor você ir logo."

                mc "J-já tô saindo!"

                if kaira_especial:

                    mc "Que foi isso..."

                    ka "Volte que tem mais pra você da próxima."

                    mc "Uou..."

                scene banho_liling1 with Dissolve(1.0)

                li "Senhor cliente gostou?"

                mc "Nem precisa perguntar mais, [li]. Eu sempre gosto."

                li "Muito bom. Até próxima vez, senhor [mc]."

                mc "Até."

            elif banho_evento == 12:

                if kaira_especial:

                    mc "É... serviços especiais agora?"

                    ka "Depois da grana, eu prometo que eu dou um jeito em você."

                    mc "Informações e um agrado? Isso é dinheiro bem gasto."

                    ka "Então passa logo."

                    scene black with dissolve

                    mc "Ai meu dinheirinho..."

                    ka "Vou fazer valer à pena. Pode deitar."

                    scene chinatown kaira_massagem2 with Dissolve(1.0)

                    pause

                    ka "Era isso que você tava esperando?"

                    mc "A-ah! Sim."

                    ka "Só não vai se empolgar demais que hoje eu tenho outra surpresa..."

                    mc "Outra?"

                    ka "Acho que você tá pronto pro prato principal."

                    window hide

                    pause

                    scene black with dissolve

                    scene kaira_massagem3 with Dissolve(1.0)

                    pause

                    mc "K-kaira..."

                    ka "Agora que você perguntou tudo o que você queria... a gente tem que fechar com chave de ouro."

                    mc "Você ainda não falou nada sobre você e a [li]."

                    ka "E nem vou falar. Agora fica quietinho que eu vou massagear você com outra coisa."

                    mc "Como que eu vou ficar quieto assim? Será que é uma boa?"

                    ka "Você quem escolhe."

                    menu:
                        "Aceitar a massagem da [ka]":


                            $ renpy.block_rollback()

                            $ kaira_especial2 = True

                            mc "Pode massagear ele..."

                            ka "Pode deixar. Você vai adorar essa massagem."

                            ka "Vou fazer bem devagarzinho... bem gostoso..."

                            mc "A-ah... você tá roçando bem aí."

                            ka "Sim. Essa é a graça, bobo."

                            mc "Eu gostei..."

                            ka "Todo mundo gosta. Mas não pode se mexer."

                            mc "Sim, senhora."

                            ka "Assim mesmo."

                            window hide

                            pause
                        "Melhor parar por aqui":


                            $ renpy.block_rollback()

                            mc "Acho melhor a gente parar por aqui, [ka]."

                            ka "Certeza?"

                            mc "É. Não quero abusar."

                            ka "Tudo bem... Valeu, [mc]. Eu prefiro assim também."

                            ka "Normalmente isso pra mim é só um trabalho. Não rola nada emocional..."

                            mc "Sei..."

                            ka "Mas depois da gente sentar e conversar tanto... acho que você é a pessoa que mais se aproxima de um amigo."

                            mc "[ka]..."

                            ka "E não ter que fazer essas coisas com você me deixa mais à vontade, sabe?"

                            mc "Falando assim, até parece que eu fiz o certo de negar isso. Mesmo já tando pago..."

                            ka "Você é meio estranho, [mc]. Mas é muito legal."

                            mc "Já virou moda me chamarem de estranho, sabia?"

                            ka "Haha... não é difícil de imaginar. Você é estranho mesmo."

                            mc "Tá bom. Já sei."
                else:


                    ka "Certeza que você não vai querer os serviços especiais mesmo?"

                    mc "É. Não quero abusar de você. Pra mim, você é uma amiga, sei lá."

                    ka "Tudo bem... Valeu, [mc]. Eu prefiro assim também."

                    ka "Normalmente isso pra mim é só um trabalho. Não rola nada emocional..."

                    mc "Sei..."

                    ka "Mas depois da gente sentar e conversar tanto... acho que você é a pessoa que mais se aproxima de um amigo."

                    mc "[ka]..."

                    ka "E não ter que fazer essas coisas com você me deixa mais à vontade, sabe?"

                    mc "Falando assim, até parece que eu fiz o certo de negar isso. Mesmo já tando pago..."

                    ka "Você é meio estranho, [mc]. Mas é muito legal."

                    mc "Já virou moda me chamarem de estranho, sabia?"

                    ka "Haha... não é difícil de imaginar. Você é estranho mesmo."

                    mc "Tá bom. Já sei."

                li "Senhor [mc]! Banho acabou!"

                mc "Ok, [li]! Tô saindo!"

                ka "Até outro dia."

                mc "Até, [ka]."

                scene black with dissolve

                "..."

                scene banho_liling1 with Dissolve(1.0)

                li "Senhor cliente parece renovado."

                mc "Sim. Esses 'banhos' tão sendo bem... iluminadores."

                li "Assim eu gosto. Volte sempre."

                mc "Vou voltar, sim. Até a próxima."

            elif banho_evento == 13:

                li "Senhor! Banho acabou!"

                mc "Droga... a [li]..."

                mc "Acho que eu não vou voltar aqui por um tempo, [ka]. Mas tá aqui o valor dos serviços de hoje."

                ka "Mas eu nem fiz nada."

                mc "Você me deu a informação que eu queria. E olha, eu não vou deixar as coisas assim."

                mc "Eu ainda vou voltar. E você vai ver sua mãe, seja lá quem ela for. Eu prometo."

                ka "Você fala igual os caras de filme."

                mc "Haha... mas é sério. Agora deixa eu ir antes que ela venha pra cá."

                ka "Adeus, [mc]."

                mc "Não é adeus. É só até logo!"

                scene black with dissolve

                "..."

                mc "Até mais, [li]."

                li "S-senhor! Volte sempre!"

                $ tempo += 1

                scene chinatown superior with Dissolve(1.0)

                "Caramba... essa história da [ka] me derrubou, mano. Vendida? Isso é possível mesmo?"

                "Essa não é a primeira vez que eu escuto sobre isso. Então... será que é verdade?"

                "Quem venderia a própria filha? Teria que ser alguém muito sem coração... ela falou de uma mulher ruiva..."

                "Sei lá. Eu tenho que pensar em tudo isso pra ver se eu entendo direito."

                "Ah! Se tem alguém que pode me ajudar com certeza é o [chi]. Se eu falar pra ele tudo o que eu descobri..."

                "Talvez ele acabe me contando alguma coisa a mais."

                "Eu sei que a [xu] é falsa. Eu sei que o [chi] já foi um dos Escolhidos. Eu sei sobre a Mestra... nossa... eu descobri tanta coisa."

                "Eu tenho que falar com o velho e ele precisa esclarecer isso tudo pra mim."

                "Eu tô muito perto de desvendar isso tudo. Eu tô sentindo! Bora, [mc]!"

                $ tempo -= 1

        elif banho_evento == 11:

            if banho_liling:

                li "Vou pedir para garota arrumar tudo e te atender direito."

                mc charmoso "Obrigado, [li]. Da outra vez ela foi muito bem."

                li "Sei... sei de que vocês gostam."

                mc envergonhado "N-não sei do que você tá falando..."

                li "Hmf!"
            else:


                li "Deixarei tudo perfeito para senhor cliente. Banho de saúde e beleza será incrível."

                mc charmoso "Valeu, [li]. Você é a melhor."

                li "Coisas da [ka] ainda estão fora, não ligue por favor."

                mc envergonhado "Pode deixar..."

            li "Volto logo."

            scene black with dissolve

            "..."

            if not banho_liling:

                mc "[ka]! Vem logo..."

                ka "[mc]?"

                mc "Isso."

                ka "Tô indo..."
            else:


                li "Cuide bem dele, garota."

                ka "Pode deixar."

            scene banho_kaira_mc with Dissolve(1.0)

            pause

            ka "Então você voltou mesmo."

            mc "Ainda tem coisas que eu preciso saber com você."

            ka "Se você diz..."

            if kaira_especial:

                mc "E tem o serviço especial também. Eu tô ansioso pra isso."

                ka "Hah. Imagino... a maioria dos rapazes adora. Até as garotas..."

                mc "Tô ansioso..."

            mc "Só que antes, o que importa."

            jump kaira_perguntas

        elif banho_evento == 12:

            if banho_liling:

                li "Vou pedir para garota arrumar tudo pra você de novo."

                mc charmoso "Valeu, [li]. Tô ansioso pela massagem de novo."

                li "Oferecemos melhor serviço para corpo e cabeça."

                mc safado "Concordo."

                li "Hoho..."
            else:


                li "Vou preparar tudo para o senhor se acalmar. Oferecemos melhor serviço para corpo e cabeça."

                mc charmoso "Obrigado, [li]."

                li "Depois tenho que falar para guria arrumar coisas dela... ela deixa todo dia pra fora agora."

                mc envergonhado "Não tem problema."

            li "Já chamo."

            scene black with dissolve

            "..."

            if not banho_liling:

                li "Tudo pronto, [mc]. Quando acabar [li] avisa."

                mc "Pode deixar."

                "..."

                mc "Psiu! [ka]! Vem logo..."

                ka "[mc]?"

                mc "Isso."

                ka "Eu não sou um cachorro pra você chamar assim!"

                mc "Tá bom! Desculpa! Só não faz barulho!"
            else:


                li "Cuide bem dele, garota."

                ka "Pode deixar."

            scene banho_kaira_mc with Dissolve(1.0)

            pause

            ka "Olha você aí de novo."

            mc "Não terminei de fazer todas as perguntas."

            ka "Você realmente parece um jornalista assim..."

            mc "Mas eu SOU um jornalista!"

            if kaira_especial:

                mc "E tem o serviço especial também. Eu gostei muito do outro. Quero de novo."

                ka "Hoje a gente vai um pouco mais longe..."

                mc "A-aí, sim! Mas antes disso, vamos falar rapidinho de outra coisa."
            else:


                ka "Tô ligada. Quando você recusou os serviços deu pra ver que você não tava aqui só pra zoar."

                mc "É o que eu tô falando desde o começo!"

                ka "Ops..."

            jump kaira_perguntas

        elif banho_evento == 13:

            "Pensando bem... só falta eu perguntar uma coisa. E é sobre o que o [chi] falou pra mim da última vez."

            "'A relação da [li] e da [ka] representa o que tem de pior aqui'. Foi mais ou menos o que ele falou."

            "É a última coisa que eu preciso tirar aqui do banho. Mas a [ka] não quis falar."

            li "Senhor [mc]? Tudo bem?"

            mc surpreso "S-sim."

            if banho_liling:

                li "Você tem vindo bastante atrás de serviços especiais de [ka]. Vocês tão tramando alguma?"

                mc charmoso "Claro que não. Eu falei que ia ficar do seu lado nessa."

                li "Acho bom. Você bom cliente. Bom rapaz."

                mc charmoso "Obrigado. E você boa mulher. Mulher boa também."

                li "Senhor..."

                li "Vou pedir para ela arrumar tudo para você."

                mc "Ok. Vou esperar."
            else:


                li "Vou deixar a água para meu cliente preferido."

                mc envergonhado "Você fala isso pra todos, né?"

                li "Só para meu preferido."

                mc "Sei..."

                li "Hoje é último dia que deixo garota não guardar mesa de massagem."

                mc envergonhado "Eu já falei que não tem problema."

                li "Garota tem que aprender boas maneiras."

                mc "Ixi..."

            li "Já chamo senhor."

            scene black with dissolve

            "..."

            "..."

            scene banho_kaira_mc2 with Dissolve(1.0)

            pause

            mc "E aí?"

            ka "Achei que você não fosse voltar mais."

            mc "Ainda tem uma última coisa que eu tenho que saber."

            ka "Hm. Que que é?"

            jump kaira_perguntas

        elif banho_evento == 14:

            "Agora que eu salvei a Xiang e descobri que a He Xiangu não é aquela da lenda e foi enganada pelos Escolhidos, minha história com a Liling muda."

            "A Liling foi a primeira a me falar de toda essa história. Sempre pareceu que ela acredita completamente nessa história."

            "O que vai acontecer se eu falar pra ela que tudo não passa de uma mentira?"

            "Será que de algum jeito isso muda como ela trata a Kaira?"

            li "Senhor [mc] está nas nuvens? Melhor esperar banho de saúde e beleza para viajar."

            mc envergonhado "Haha... verdade..."

            if liling_seducao:

                "Quando eu comecei a conversar com a Liling eu decidi que se pintasse a chance eu ia querer ter alguma coisa a mais com ela."
            else:


                "Quando eu comecei a conversar com a Liling eu decidi nã ia querer nada com ela."

                "Depois de tudo isso... será que eu realmente não vou querer dar uma aproveitada nessa mulher?"

                menu:
                    "Não quero nada com ela mesmo":


                        "Nah. Eu continuo achando nada a ver ter um lance com ela aqui. Ela é só a dona do banho e eu um cliente."
                    "Não vou perder a oportunidade":


                        $ liling_seducao = True

                        "Pensando bem... não tem por que não aproveitar, né?"

                        "Quem sabe não rola alguma coisa..."

            if banho_liling:

                "Eu e a Liling tomamos banho juntos... e se as coisas assim, com certeza as coisas podem evoluir."

            li "Tá pensando besteira, senhor [mc]?"

            mc envergonhado "E-eu? N-não..."

            li "[li] conhece cara de safado de longe."

            mc zerado "Safado... não é assim que se trata um cliente."

            li "Pode ser... mas tava pensando besteira."

            mc charmoso "Ok... você me pegou."

            li "Liling vai preparar banho e já te chama."

            mc "Valeu."

            scene black with dissolve

            scene banho_zen entrada with dissolve

            if liling_seducao:

                "Eu vou chamar ela pra entrar comigo. É a chance que eu tenho de fazer as coisas esquentarem entre a gente."

                "E talvez numa conversa dessas eu consiga falar pra ela da He Xiangu."
            else:


                "Mesmo não querendo nada com ela, se eu conseguir levar ela no banho comigo, provavelmente ela vai tá bem mais relaxada."

                "E talvez numa hora dessas eu consiga falar pra ela da He Xiangu."

            "Vai ser um lance delicado, porque é uma coisa que ela acredita há tantos anos... talvez ela nem acredite em mim logo de cara."

            "Mas não tem como conseguir todo o dinheiro que a Kaira precisa. E eu também não sei como fugir com ela daqui."

            "Salvar a Xiang já foi demais pro meu coração. Eu não quero passar por isso de novo por um bom tempo."

            "O jeito mais tranquilo seria a Liling perceber logo o absurdo e só liberar ela..."

            "E o único jeito vai ser mostrar como os Escolhidos tão enganando todo mundo e ela não pode fazer parte desse esquema errado."

            "A Liling sempre foi de boa comigo. Ela é focada nos negócios, mas nunca pareceu uma pessoa ruim. Ela só tá sendo enganada igual os outros."

            li "O banho está pronto."

            mc normal "Opa!"

            scene black with dissolve

            scene banho_zen ofuro with dissolve

            mc normal "Parece incrível como sempre."

            li "E é."

            mc charmoso "Você vai vir comigo."

            li "C-com o senhor?"

            mc "Não é a primeira vez que a gente fala disso, né?"

            li "..."

            mc "Eu quero você tranquila... relaxada..."

            li "Senhor... Liling pode fazer isso porque é cliente de primeira."

            mc "É disso que eu tô falando, Liling. Você vai colocar aquela roupa especial?"

            li "Isso também?"

            mc "Claro."

            li "Liling já volta... não quero tirar tempo de senhor [mc]."

            mc "Então bora gogogo!"

            show black with dissolve

            hide black with dissolve

            "Parece que ela tá aceitando fácil. Se as coisas continuarem assim, não vai demorar muito agora..."

            "Opa... aí vem ela."

            scene liling_new1 with Dissolve(1.0)

            pause

            li "Liling tá pronta."

            menu:
                "Valeu por aceitar.":


                    mc normal "Valeu mesmo por ter aceitado."

                    li "Liling quer agradar bons clientes."
                "Você tá gostosa.":


                    mc charmoso "Caralho, Liling... você tá gostosa."

                    li "Senhor [mc]... não diga bobagens para senhora Liling."

                    mc "É sério. Eu não me canso de ver você assim."

            li "Vamos entrar?"

            mc normal "Com certeza. Mas antes... é... Liling, lembra quando você me contou da lenda da He Xiangu?"

            li "Faz tempo isso."

            mc "Pois é. Você foi a primeira a me falar dela. Que ela era imortal e uma lenda aqui no bairro."

            li "Sim..."

            mc envergonhado "Você... é... já parou pra pensar que uma pessoa imortal desafiaria a ciência?"

            li "Que você fala, senhor [mc]?"

            mc "Não existe pessoal imortal pra ciência. Essa é a única certeza que a gente tem. Que um dia a gente vai morrer."

            li "Mas He Xiangu não tem nada com ciência. Xiangu é escolhida por deuses para abençoar chineses de mundo todo."

            mc "Eu sei... mas..."

            li "Se senhor [mc] ficar falando bobagens banho vai esfriar e não será de saúde e beleza perfeitas."

            mc "O-ok... vamos logo pro banho."

            "Não foi dessa vez... mas eu dei um passinho... na próxima..."

        elif banho_evento == 15:

            mc charmoso "Tava ansioso para meu próximo banho com você, Liling."

            li "Senhor [mc] vai insistir nisso todas vezes agora?"

            mc "Com certeza."

            menu:
                "O banho fica melhor com você.":


                    mc normal "O banho vai ficar melhor com você comigo. Você é uma boa companhia, Liling."

                    li "Agradeço senhor."
                "Ver você com aquela roupa...":


                    mc tarado "Só de pensar que você vai vestir aquela roupa... hmm..."

                    li "Fundoshi é roupa normal para banho de saúde e beleza. Não é especial."

                    mc "Você nele é bem especial pra mim."

                    li "Ah, senhor [mc]..."

            mc normal "Então bora. Vamos arrumar tudo isso e ir logo pro banho. E já se veste."

            li "Liling vai obedecer... porque senhor é bom cliente."

            mc "Isso isso."

            scene black with dissolve

            scene banho_zen entrada with dissolve

            "Da outra vez eu consegui iniciar uma conversa sobre a He Xiangu, mas o argumento da ciência não resolveu nada."

            "Talvez o único jeito seja realmente contar sobre a Xiang, sobre o Distrito e tudo o mais."

            "Mas essa é minha última cartada. Será que eu já uso ela assim?"

            li "Banho pronto, senhor [mc]."

            mc "Tô indo."

            scene black with dissolve

            scene liling_new1 with Dissolve(1.0)

            mc charmoso "Você já se vestiu, igual eu falei."

            li "Sim. Liling quer que senhor aproveite máximo de banho de saúde e beleza."

            mc "Então vem comigo. Se ajeita na banheira."

            li "A Liling?"

            mc "É. Quero que você fique suave."

            li "Mas banho é pra senhor [mc]."

            mc "Eu sei. Depois eu vou entrar também. Mas agora eu quero que você se ajeite."

            li "Hmm... se senhor diz..."

            mc "Eu tô falando. Se ajeita aqui."

            scene black with dissolve

            scene mc_liling1 with Dissolve(1.0)

            pause

            li "Só [mc] mesmo pra pedir algo assim pra Liling."

            mc "Normalmente seus clientes não pedem pra você tomar banho no lugar deles?"

            li "Claro que não, senhor... hohoho..."

            mc "Esse povo não tem consideração, Liling. Você merece um banho especial também. Você é uma ótima anfitriã."

            li "Oh... obrigada."

            "O clima tá bem bacana."

            if liling_seducao:

                "Eu podia dar em cima dela... aposto que ia ser uma excelente hora... mas eu tenho outros objetivos."

            "Eu tenho que aproveitar pra falar sobre a He Xiangu com ela. É minha chance de salvar a Kaira."

            mc "Liling... sabia que eu conversei com a He Xiangu?"

            li "Hm?!"

            mc "É... eu fui várias vezes no portal de pedra e vi ela lá. Até no templo a gente se viu uma vez."

            li "Incrível, senhor [mc]. Nem todos temos chance de conversar assim com lenda."

            mc "Pois é... foi bem legal mesmo. Eu-"

            li "Senhor... se permite... como ela estava?"

            mc "Estava igual sempre. Sentada lá haha..."

            li "Não. Digo, como He Xiangu estava? Ela estava bem?"

            mc "Hmm..."

            "Por que ela tá me perguntando isso?"

            mc "Pra falar a verdade, Liling... ela não tá tão bem agora."

            scene liling_new2 with Dissolve(1.0)

            li "Sério?! Que aconteceu?!"

            mc "Ah... é... ela tá bem de saúde. Ela só tá em dúvida sobre umas coisas."

            li "Por que dúvida?"

            "É agora ou nunca."

            mc "Talvez os Imortais tenham enganado ela..."

            li "Não!"

            li "Você não devia falar algo assim! É errado!"

            mc "Não sou eu que tô falando... foi ela quem comentou..."

            li "I-isso não parece certo, senhor [mc]. Tem certeza?"

            mc "Tenho."

            li "Tudo isso parece errado. Eu tenho que ver que tá acontecendo. Por favor, saia de banho, vou fechar."

            mc "S-sério?"

            li "Peço desculpas."

            if liling_seducao:

                menu:
                    "Tudo certo. Sem problemas.":


                        mc "Relaxa. Vai fazer suas coisas."

                        li "Obrigada, senhor. Liling vai se retirar então."
                    "Você me recompensa na próxima.":


                        mc "Então você me recompensa na próxima, né?"

                        li "Recompensa? De que tipo, senhor [mc]?"

                        mc "Do melhor tipo que tem."

                        li "Ah... Sei muito bem..."

                        li "Vou pensar... senhor é bom cliente e eu gosto de bons clientes."

                        mc "Você sabe mesmo como agradar, Liling. Vou esperar minha compensação por hoje então."

                        li "Certo... na próxima. Agora vou indo."

            mc "Tudo certo. Até a próxima."

            scene black with dissolve

            scene banho_zen ofuro with dissolve

            "Por que será que a Liling ficou desse jeito?"

            "Pensando agora... a Liling que começou essa história da He Xiangu comigo."

            "E se... foi ela que... impossível. Isso é de mais de anos. Não pode ser ela."

            "Tem alguma coisa cheirando muito estranho nisso aí. Meu faro de jornalista tá apitando."

        elif banho_evento == 16:

            "Da outra vez a Liling saiu correndo depois que eu falei da He Xiangu..."

            mc "E aí? Deu tudo certo?"

            li "Sim... Peço desculpas por minha reação, senhor [mc]."

            mc charmoso "Calma. Vamos conversar melhor na banheira."

            li "É o mínimo que eu posso fazer..."

            mc "Então bora."

            scene black with dissolve

            scene liling_new2 with Dissolve(1.0)

            li "Que fiz de última vez foi inaceitável. Não profissional."

            menu:
                "Por que você saiu?":


                    mc "Por que você saiu daquele jeito?"

                    li "Nada importante. Tinha assuntos pra resolver."

                    mc "Era sobre a He Xiangu?"

                    li "Sim..."

                    mc "O que você tem com ela?"

                    li "Eu... eu só me preocupo com ela. Todos de bairro chinês são assim."

                    "Não sei se é bem assim..."
                "E minha reparação?":


                    mc "Eu tô mais interessado no que eu vou ganhar em troca. As coisas não podem só ficar assim, certo?"

                    li "Senhor quer mesmo que eu pague pelo meu erro com senhor?"

                    mc "Claro."

            if liling_seducao:

                "Se eu quero alguma coisa com ela, essa é a melhor hora."
            else:


                "Eu decidi que não quero nada com ela, então vou levar a situação na boa."

            mc "Eu não quero que você fique triste por causa disso, ok? Se estica melhor aí."

            li "Obrigada."

            scene mc_liling1 with Dissolve(1.0)

            mc "Bem melhor assim."

            if liling_seducao:

                mc "Mas agora a gente vai falar da minha reparação."

                li "E como eu posso fazer isso?"

                mc "Eu acho que a gente podia... sei lá... posso sentar do seu lado?"

                li "Do meu lado?"

                mc "É. Daí eu falo o que eu quero."

                li "Senhor... tudo bem... pode vir."

                "Boa!"

                scene black with dissolve

                mc "Vou sentar aqui. Você senta comigo?"

                li "S-senhor [mc]? Entendi... tudo bem..."

                scene mc_liling2 with Dissolve(1.0)

                pause

                li "Era isso que você queria?"

                mc "Era bem isso mesmo."

                li "Não acredito que velha como eu ainda chama atenção."

                mc "Você chama muito mais atenção do que você imagina."

                li "Senhor [mc]... e agora?"

                mc "Eu não queria parar aqui. O que você acha?"

                li "Pena... Não posso beijar senhor agora."

                mc "Aww... Por quê?"

                li "Fui casada com senhor e não posso gostar de outro homem depois dele."

                mc "Faz tempo?"

                li "Muitos anos. Quando filha de Liling nasceu."

                mc "E mesmo depois de todo esse tempo... você nunca ficou com mais ninguém?"

                li "Não. Não posso agora também."

                mc "Você ainda é jovem, Liling. Tem muita coisa pra viver. Tem certeza que você vai desistir do prazer pra sempre assim?"

                li "Não ligo. Sou feliz de outros jeitos. Tenho a- digo... Banho de saúde e beleza é tudo na vida."

                mc "É um baita desperdício... isso eu posso falar."

                li "Hoho... agradeço elogio."

                li "Sentar assim repara senhor [mc] pela vez passada?"

                mc "Hmm... não completamente. Mas se você sentar assim comigo da outra vez também..."

                li "Aceito. Mas só sentar."

                mc "Só sentar... por enquanto..."

                li "Senhor [mc]... seu tempo acabou."

                mc "Que pena..."
            else:


                li "Obrigada por não deixar de vir no banho. Senhor [mc] é bom cliente."

                mc "Relaxa. Eu não ia parar só por isso."

                mc "Mas você não pensou em devolver meu dinheiro também?"

                li "Claro que não. Liling nunca devolve dinheiro."

                mc "..."

            scene black with dissolve

            mc "Depois eu volto."

            li "Banho e Liling vão estar esperando senhor."

        elif banho_evento == 17:

            if liling_seducao:

                "Da outra vez eu fiquei de graça com a Liling e não consegui nem falar direito sobre a He Xiangu."
            else:


                "Nem consegui falar com ela direito sobre a He Xiangu."

            "Mas deu pra ver que tem algum lance estranho da Liling com essa história."

            "Por que ela ficou tão agitada quando eu disse que a He Xiangu tava em dúvida sobre as coisas?"

            "Será que essa farsa da He Xiangu ajuda a Liling de algum jeito? Será que tem mais coisa nisso pra ela do que a Kaira?"

            li "Senhor [mc] parece mais viajado que normal esses tempos."

            menu:
                "É um mistério...":


                    mc envergonhado "É um mistério que eu tô tentando decifrar."

                    li "Parece interessante essa vida de paparazzo."

                    mc "E é mesmo."
                "É você que tá mais bonita.":


                    mc charmoso "Acho que é culpa sua. Você tá mais bonita esses dias, sabia?"

                    li "Oh, senhor... não diga coisas assim."

                    mc "Espero que você não se incomode. Eu falo com todo o respeito."

                    li "Você é galanteador."

            mc normal "Então vamos pro banho?"

            if liling_seducao:

                mc safado "Eu quero continuar o que a gente começou da última vez."

                li "Senhor não vai parar mesmo?"

                mc "Só quando eu tirar o que eu quero de você."

                li "Oh..."
            else:


                li "Vamos. Agradeço por continuar me chamando. Normalmente não tenho tempo para banho de saúde e beleza."

                mc normal "Fico feliz. E você faz companhia pra mim. Bora."

            scene black with dissolve

            if liling_seducao:

                scene mc_liling2 with Dissolve(1.0)

                li "Era aqui que estávamos, certo?"

                mc "Bem aqui..."

                "Eu devia tá falando com ela sobre a Kaira... mas eu sempre acabo indo pra esse lado."

                "Bom... curtir um pouco antes de deixar ela nervosa não tem problema... certo?"

                mc "Hoje você vai aceitar?"

                li "Expliquei que não posso. Não seria certo com morto."

                menu:
                    "Mas o morto tá morto!":


                        mc "Mas o morto já morreu mesmo!"

                        li "Hoho... não fale assim dele, senhor [mc]."

                        li "Corpo de ex-marido pode estar sob terra, mas memória dele continua."

                        mc "Eu não entendo isso muito bem. Eu acho que a gente tem que aproveitar o agora."

                        li "Sei que senhor acha, mas não é tão simples para Liling."
                    "Eu entendo...":


                        mc "Tudo bem... eu entendo se você não quer..."

                        li "Certeza?"

                        mc "Eu sou um cavalheiro. Eu não vou querer que você quebre sua palavra só pra eu poder aproveitar."

                        li "Você é homem bom, senhor [mc]."

                mc "Bom... talvez você não possa ficar comigo... mas talvez tenha uma forma de eu aproveitar você."

                li "Oh?"

                mc "Só de sentir você assim é bom pra caramba... quem sabe... se eu pudesse ver você?"

                li "Ver..."

                mc "Se eu não posso ter você, eu posso pelo menos ver... o que me diz?"

                li "Entendi."

                li "Sabe, senhor [mc]... posso contar segredo pra você?"

                mc "Claro. Que foi?"

                li "Fazia tempo que Liling não tinha contato com homem assim. Muitos anos mesmo. Desde morte de marido."

                li "Foi bom ter você cortejando assim."

                mc "Não foi nada. Você é bem gata e merece."

                li "Antes eu escutava muito isso. Trabalhava fazendo serviços especiais para dona de banho."

                mc "S-sério? Antes de você virar dona aqui... você trabalhava... fazendo..."

                li "Sim. Não gostava de ter que fazer essas coisas e marido não sabia."

                li "Não era bom e nem fácil, mas era único jeito."

                mc "Entendo... o começo não foi fácil."

                li "Até que dia chegou e eu virei dona de banho de saúde e beleza."

                li "Depois nunca mais trabalhei com serviços especiais. Pena que marido acabou morrendo nisso."

                mc "Pelo menos você conseguiu uma vida que não precisa mais fazer o que você queria."

                menu:
                    "Então foi assim...":


                        pass
                    "Como você virou dona?":


                        mc "E como você virou dona do banho?"

                        li "Oh... não foi fácil. Liling teve que pagar com coisa muito valiosa."

                        mc "Sei... não deve ter sido barato conseguir tudo isso aqui."

                        li "Foi bem complicado."

                mc "Então essa é sua história..."

                li "Sim."

                mc "Começou servindo no banho até virar dona. É uma história bacana, Liling. Parabéns."

                li "Obrigada. Mas não é história bonita."

                mc "Ah... eu achei..."

                li "Contei isso porque teve algo que eu sempre fiz... mesmo com marido vivo."

                mc "Hm?"

                li "Senhor [mc]... quer serviço especial?"

                mc "V-verdade?!"

                li "Faz tempo, mas ainda sei como satisfazer homem."

                "A Liling tem o lance do marido dela... e mesmo assim ela quer fazer isso pra mim."

                "Eu vou aceitar ou não?"

                menu:
                    "A gente não precisa disso.":


                        mc "Quer saber? Eu não quero que você volte pra aquele tempo que você fazia isso."

                        mc "Você já me deixou feliz o suficiente, sabe?"

                        li "Senhor [mc]..."

                        mc "É sério. Eu tava mesmo afim de me divertir com você, mas ter você comigo aqui foi o suficiente. Valeu."

                        li "Senhor é realmente homem bom."

                        jump banho17_depois
                    "Claro que eu quero!":


                        mc "C-claro que eu quero!"

                        li "Era que Liling queria ouvir."

                scene black with dissolve

                li "Deixa Liling cuidar de você."

                mc "A-ah..."

                scene mc_liling3 with Dissolve(1.0)

                pause

                mc "Ah..."

                li "São boas?"

                mc "Seus melões são incríveis, Liling... tão macios..."

                li "Pode usar, senhor [mc]. Eles vão satisfazer você."

                mc "Já tão."

                li "Sei muito bem que vocês adoram massagem assim."

                mc "Sim. Continua espremendo meu pau, Liling."

                mc "Tá muito bom."

                li "Calma, senhor [mc]... aproveite cada momento."

                "Ah... que delícia... não sei quanto tempo eu vou aguentar."

                li "Seu membro já tá quente."

                mc "T-tá!"

                li "Agora aumentar pressão."

                mc "Isso!"

                scene mc_liling4 with Dissolve(1.0)

                pause

                li "Assim que você gosta, certo?!"

                mc "Sim, Liling! Eu vou gozar nos seus peitos!"

                li "Pode gozar, garoto. Goza."

                mc "Ah! Ahh!!"

                scene mc_liling4 with vpunch

                li "Incrível!"

                mc "Aahh!"

                mc "{i}puf puf{/i}"

                mc "Sensacional... mesmo depois dos anos... você continua incrível..."

                li "Bom saber disso, senhor [mc]."

            label banho17_depois:

                mc "Agora bora se ajeitar e tomar um banho... que o tempo tá correndo."

                li "Não se preocupe. Vou dar tempo extra hoje."

                mc "Uhul!"

                scene black with dissolve

                scene mc_liling1 with Dissolve(1.0)

            li "Últimas vezes você não pediu serviços especiais da Kaira. Ela te desagradou?"

            mc "Não. Não é isso."

            li "Hm..."

            mc "É que eu queria falar com você mesmo."

            li "Sobre He Xiangu?"

            mc "Como você sabe?"

            li "Outra vez senhor [mc] falou dela."

            mc "E tudo legal pra você?"

            li "Não. Não quero falar da senhorita He Xiangu. Não com você."

            mc "P-por quê?"

            li "Não leve a mal. Só não sinto vontade."

            li "Aliás, melhor você tomar resto de banho de saúde e beleza sozinho. Vou sair."

            mc "L-liling!"

            scene black with dissolve

            "Droga... ela saiu mesmo..."

            "Da próxima. Da próxima não pode passar."

            "Agora deixa eu aproveitar um pouco isso aqui... não é barato esses banhos..."

            "..."

        elif banho_evento == 18:

            mc normal "E aí, Liling? Tudo ok?"

            li "Como sempre, senhor [mc]."

            mc charmoso "Vamos lá?"

            li "Sinto muito, mas hoje não poderei acompanhar. Inclusive, chamei Kaira para fazer companhia."

            mc desconfiado "Sério?"

            li "Afazeres administrativos."

            mc "Entendi..."

            li "Pode esperar ela no banho, que ela vai arrumar tudo."

            mc "Ok. Tô indo lá."

            scene black with dissolve

            scene banho_zen ofuro with dissolve

            "Quase certeza que ela tá me evitando por causa da conversa sobre a He Xiangu."

            "No começo eu achei que ela só tava sendo manipulada igual os outros, mas agora eu não sei..."

            "Parece que ela tá mais dentro disso do que os outros. Como se ela tivesse se aproveitando dessa história também."

            "Eu lembro que o Bao disse que ela era muito bem vista pelos Escolhidos porque ela atraia pessoas pra cá."

            "Será que pode ser que a Liling também faça parte dos Imortais? Como ela virou dona desse banho?"

            ka "Ei. Acorda."

            mc desconfiado "Hm?"

            scene black with dissolve

            scene kaira_new1 with Dissolve(1.0)

            pause

            ka "Olá."

            mc "O-oi."

            ka "Alguém tinha minha dito que era um 'até logo' e não um 'adeus'. Mas pareceu bem adeus pra mim."

            mc "N-não."

            ka "Se a Liling não tivesse feito você vir falar comigo, eu ia continuar esquecida."

            menu:
                "Eu ainda não tive tempo.":


                    mc "Eu não deixei você de lado. Eu ainda não consegui convencer ela a te tirar daqui."

                    ka "Se você fosse aparecer só quando convencesse ela, então você nunca ia aparecer, mano."

                    ka "Você não tem ideia do tanto que eu falei com ela. Ela nunca vai voltar atrás!"

                    mc "Eu não sou você. Eu tenho um plano."

                    ka "Idiota..."
                "Eu não devo nada a você.":


                    mc "Não sei do que você tá falando. Eu não sou obrigado a cumprir nada com você."

                    ka "Calma aí, garotão. Eu só tô falando o que você disse. Não precisa ser um cuzão."

                    mc "Eu disse que eu vou tirar você daqui, não disse? Agora vê se espera."

                    ka "Tá legal, tá legal... se você diz..."

            ka "Só não imagino como você pretende fazer isso."

            mc "Eu usei a sua dica sobre a He Xiangu. Ela era falsa mesmo. E eu tinha que mostrar isso pra ela."

            ka "E como foi? Imagino que terrível. Ouvi dizer que só a Liling é mais cabeça dura que ela."

            mc "Não foi perfeito... mas foi melhor do que você imagina."

            ka "Não engulo isso."

            mc "É sério. Ela ficou bem em dúvida. Disse que tinha que descobrir por ela própria, mas ela tá bem abalada."

            ka "Uou... se é sério mesmo, como você fez isso?"

            mc "Eu encontrei a outra 'He Xiangu'. Ela tava no Distrito. Com a mesma tatuagem e tudo, sendo escravizada lá."

            ka "Uau... que pesado."

            mc "Não é muito diferente do seu caso..."

            ka "É... parace que sim..."

            mc "Se eu consegui tirar ela de lá, dá pra fazer a mesma coisa com você."

            ka "O salvador de garotas escravizadas? É isso?"

            mc "É sério, Kaira. Eu não entendo como a Liling não vê como tudo isso é errado."

            mc "Quando que a gente começou a achar normal uma coisa dessas?"

            ka "Não vem com esses pensamentos pra cima de mim. Eu só quero viver minha vida."

            mc "O único problema pro meu plano é que a Liling se recusa a falar comigo sobre a He Xiangu."

            mc "Se eu conseguir mostrar pra ela que tudo isso é uma mentira, então ela vai sair desse feitiço."

            ka "Ah! Agora entendi. Você acha que falando a verdade pra ela, ela vai quebrar igual a louca do portal."

            mc "Mais ou menos isso... pelo menos que ela repense essa história e veja que tá errado manter você aqui."

            ka "Quem sabe..."

            menu:
                "A Liling parece do bem.":


                    mc "A Liling não me parece uma pessoa ruim. Ela é meio gananciosa talvez..."

                    ka "Porque ela não te obriga a trabalhar de graça pra ela."

                    mc "Tem razão... desculpa..."

                    ka "É brincadeira. Eu nem ligo mais."

                    mc "O que eu tava querendo dizer é que eu acredito que ela vai entender quando eu explicar tudo pra ela."

                    ka "..."
                "Se não funcionar só resta a força.":


                    mc "Eu tô contando com a razão da Liling. Mas se ela não aceitar, a única solução é tirar você daqui na força."

                    ka "A é? E como você pretende fazer isso, Rambo?"

                    mc "Não sei. Mas eu já salvei uma. Só sair correndo."

                    ka "Parece um plano e tanto... só que não."

                    mc "Acho bom você ajudar, porque é pra você tudo isso aqui."

                    ka "..."

            li "O tempo tá acabando, senhor [mc]!"

            mc "Opa... na próxima eu vou falar com ela."

            ka "Se ela te mandar aqui de novo e não quiser falar contigo, eu tenho uma ideia."

            mc "Boa. A gente se fala."

            ka "Sim. Até."

        elif banho_evento == 19:

            mc "Tudo bem, Liling? Será que hoje a gente pod-"

            li "Kaira vai atender senhor [mc] novamente hoje."

            mc "Liling... eu preciso falar com você!"

            scene liling_new3 with Dissolve(1.0)

            pause

            li "Senhor vem aqui tomar banho e ter serviços especiais. Quero que você use bem serviços de banho de saúde e beleza."

            mc "Eu sei que a Cidade Chinesa acredita na lenda da He Xiangu e dos outros Imortais, mas e se não for bem assim?"

            li "Que senhor está falando?"

            mc "E se tudo isso foi criado pra que vocês aceitassem tudo o que é dito aqui? E se for uma armação?"

            li "Não diga bobagens, senhor [mc]. Lendas de bairro são muito velhas. Muito mesmo."

            mc "Eu sei. Mas talvez essa lenda... ela tenha começado quando a verdadeira He Xiangu morreu!"

            li "Como senhor saberia algo assim?"

            mc "Não tenho certeza... mas a Xiang teve um tipo de visão, sei lá, e eu acho que era sobre isso."

            li "Sei que você é paparazzo e procura histórias para revista, mas não existe história aqui. Tudo aqui é verdade."

            mc "Você precisa acreditar em mim, Liling!"

            li "Senhor [mc]... essa conversa não vai acabar bem. Existem coisas muito grandes acontecendo aqui."

            mc "Hm?"

            "E-ela até mudou o tom da voz."

            li "Eu sei que você quer salvar Kaira."

            mc "S-sabe?!"

            li "Mas Kaira não precisa disso. Ela está bem aqui em banho de saúde e beleza."

            li "Kaira ajuda Liling e todos de bairro. Ela aprende ser responsável e talvez dia compre saída."

            mc "Então... você também sabe do dinheiro que ela tá juntando?"

            mc "Liling... você não vê que isso é errado? A Kaira é escrava aqui!"

            li "Escrava? Salvei garota trazendo ela aqui. Ela come, dorme e vive bem em banho."

            mc "Mas é contra as leis manter alguém em um lugar contra a vontade dela! A pessoa precisa receber o que tá na lei e tudo!"

            li "Liling segue leis de bairro. Liling ganhou banho e Kaira e faz que quer com garota!"

            mc "G-ganhou?"

            li "São regras de bairro chinês. Senhor [mc] nunca vai entender nossa vida."

            mc "O Bao... ele me disse uma vez que ia ser difícil entender tudo se eu visse só com meus olhos."

            mc "Que eu ia ter que me esforçar pra ver as coisas... mas isso claramente é errado!"

            li "..."

            mc "Você é uma mulher boa e batalhadora, Liling! Por que você quer ir por esse caminho?"

            li "Esse é caminho que Liling escolheu lá atrás. Troquei duas coisas importantes por tudo isso aqui."

            li "Agora eu não posso desistir de recompensa porque senhor [mc] vem me falar que é errado."

            menu:
                "O que é certo é certo.":


                    mc "Liling... independente do que é melhor pra gente, não muda o que é certo e o que é errado."

                    mc "Se a gente colocar a gente na frente do que a gente sabe que tá errado, a gente só tá escolhendo a vida fácil."

                    li "Todos fazem isso, senhor [mc]. Você também."

                    mc "E-eu sei..."
                "O que você trocou?":


                    mc "Liling... você disse que trocou duas coisas importantes. Do que você tá falando?"

                    if liling_seducao:

                        mc "Quando você falou que pagou caro pelo banho... eu achei que você tava falando de grana."

                    mc "Não parece que você tá se referindo a dinheiro..."

                    li "Dinheiro? Quanto mais você tem dinheiro, senhor [mc], mais você percebe que ele não vale de nada."

                    li "Dinheiro é importante pra quem não tem, mas depois que você tem mínimo, não compra cabeça e coração."

                    li "Que perdi foi mais que dinheiro... mais que qualquer coisa que eu tive nesse mundo."

            li "Bairro chinês tirou tudo de mim e agora você quer tirar resto? Nunca."

            "Ela tem razão... é fácil pra mim vir aqui e falar em 'salvar' a Kaira sendo que eu nem sei como as coisas chegaram nisso."

            "O Bao disse que eu tinha que olhar com outros olhos. Talvez eu precise olhar com os olhos da Liling nessa situação."

            "Ela perdeu coisas muito importantes pra ter isso aqui. Será que..."

            mc "Você tem razão, Liling... é fácil pra mim chegar aqui e cagar regra pra você. Vamos fazer de outro jeito."

            li "Hm?"

            mc "Não teria como você conseguir de novo? O que você deu pra Cidade Chinesa?"

            li "Conseguir... de novo?"

            mc "É. Recuperar aquilo que você trocou pelo banho. E assim você poderia pelo menos liberar a Kaira."

            li "Nunca... nunca atrevi a pensar isso, senhor [mc]."

            mc "Por quê? É algo tão impensável assim?"

            li "Com certeza. Eu... nem deveria estar falando isso com você."

            li "Mas jeito diferente do senhor [mc], parece que sempre quis melhor pra Liling e banho de saúde e beleza. E até para Kaira."

            li "Então eu sinto que posso falar... mas é informação séria e perigosa. Senhor quer mesmo saber?"

            menu:
                "Nessa altura do campeonato? Claro!":


                    mc "Depois de tudo isso? Claro que eu quero! Certeza que isso vai ser uma pauta. E uma das big bigs!"
                "Mas é p-perigoso?":


                    "Sério mesmo, [mc]?! Depois de tudo isso você vai ficar com medinho?! Tenha santa paciência, homem!"

                    mc "C-claro que eu quero saber."

                    "Bem melhor..."

            li "Se você realmente quer..."

            li "Tudo isso que estamos falando diz respeito a grupo que comanda bairro chinês."

            mc "Os Escolhidos?"

            li "Sim... eles fizeram proposta para Liling. Aceitei e fiz minha parte e eles a deles."

            mc "E nessa troca você conseguiu o banho."

            li "Sim. Não quero falar coisas trocadas, mas agora senhor [mc] entende."

            li "As duas coisas que perdi são impossíveis de conseguir de volta."

            li "Primeira delas se foi... outra seguiu caminho sem volta."

            li "Se senhor conseguisse recuperar... aceitaria trocar de volta. Ela por Kaira."

            mc "Fica difícil se eu nem sei o que eles pegaram de você."

            li "Senhor [mc] teria que ir contra Oito Imortais e derrubar sistema de bairro chinês. Nem adianta tentar."

            mc "Destruir essa mentira que existe aqui é a melhor forma de salvar a [s], a Fen Ju, vocês e a He Xiangu."

            li "A-até ela você quer salvar?"

            mc "Claro. Nenhum de vocês merece viver nesse emaranhando que existe só pra satisfazer alguns poderosos."

            mc "Eles usaram a fé de vocês pra criar uma mentira e manter todos fazendo o que eles queriam."

            mc "Dizendo que eram lendas, deuses e sei lá o quê, eles fizeram vocês aceitarem o que eles queriam, e que não tem nada de divino."

            mc "É só a ganância humana de sempre. E de pensar que isso pode ter começado há séculos atrás..."

            li "Você vai mesmo enfrentar Mestra e outros?"

            mc "Se eu não morrer antes, pode ter certeza que eu vou."

            scene banho_liling1 with Dissolve(1.0)

            li "Liling vai estar esperando seu retorno. E não se preocupe. Vou cuidar bem de Kaira enquanto isso."

            mc "Valeu, Liling."

            li "Se tudo der certo... você terá banhos de graça para sempre."

            mc "Uou!"

            menu:
                "Eu vou querer!":


                    mc "Pode ter certeza que eu vou aproveitar!"

                    li "Vai ser mínimo por que tá fazendo."

                "E serviços especiais?" if liling_seducao:

                    mc "É... e quem sabe uns serviços especiais? C-com todo o respeito, claro."

                    li "Senhor cabeça suja..."

                    mc "Isso é um não?"

                    li "Não."

                    mc "Não que não vai ter serviço ou não que não não vai ter... é..."

                    li "Isso mesmo."

                    mc "Hmm... Bom..."
                "Não precisa. Eu quero pagar.":


                    mc "Não precisa. Eu vou gostar de pagar."

                    li "E não vou recusar dinheiro de bom grado."

                    mc "Haha..."

            mc "Agora eu vou nessa. Até."

            li "Zaijian."

            scene black with dissolve

            pause

            scene liling_new4 with Dissolve(1.0)

            pause

            li "Parece que precisávamos de alguém de fora para mostrar que talvez coisas foram longe demais."

            li "Tenho certeza que tudo começou pensando bem... mas tempo estragou nossa casa e olhe onde estamos agora..."

            li "Se esse rapaz realmente conseguir colocar luz nos olhos de Mestra... talvez ainda teremos salvação."

            li "Deuses... verdadeira He Xiangu... esteja de lado de senhor [mc]."

            li "Final deve ser triste, mas tem pequena chance de acabar bem."

            li "Agora é com ele."

            li "Ah... e ele esqueceu de entrar em banho mesmo pagando... agora é tarde. Liling não devolve dinheiro."

        scene black with dissolve

        play sound "extra/carta.mp3"



        "{b}[mc] se sente purificado e energizado pelo tratamento no banho de saúde e beleza{/b}"





        python:
            if renpy.android:
                banho_evento_db = PythonSDLActivity.pegaBanho()
                if banho_evento == banho_evento_db:
                    PythonSDLActivity.addBanho()

            banho_evento += 1

            dia_banho = dia + 1
            tempo += 1

            renpy.block_rollback()

        jump chinatown_superior

label chinatown_lamen:

    $ chinatown_area = "lamen"

    hide screen chinatown_tela

    scene chinatown lamen with Dissolve(1.0)

    show screen chinatown_tela

    pause

label chinatown_vista:

    hide screen chinatown_tela

    scene c_chinesa entrada_chinatown with Dissolve(1.0)

    if china_negra:

        menu:
            "Descer até a entrada da China Negra":


                jump chinatown_entrada
            "Deixar para outra hora":


                jump cidade_chinesa

    elif s4_chinatown_visita:

        pause

        "Ali é a entrada pra aquele lugar onde eu fui com o [chi]."

        "É como se fosse uma cidade secreta embaixo da Cidade Chinesa."

        "Uma das coisas mais misteriosas que eu já vi. Provavelmente a mais misteriosa que eu já vi..."

        "Loucura."
    else:


        pause

        "Que lugar estranho..."

        "Parece que ali tem uma grande saída do esgoto, mas o rio parece limpo."

        "E aquele corredor... parece que é a entrada pra algum lugar."

        "Talvez eu devesse dar uma olhada lá depois."

    jump cidade_chinesa

label chinatown_voltar:

    "Deseja voltar para a cidade?"

    menu:
        "Sim.":


            $ tempo += 1

            jump call_cidade
        "Não.":


            jump cidade_chinesa

screen chinatown_tela2():
    tag chinatown

    predict False
    zorder 100
    modal True

    if not chinatown_area == "rua":

        imagebutton auto "images/china/rua_%s.png":
            xalign 0.05
            yalign 0.95
            action Call("chinatown_rua")


    if not chinatown_area == "esquina":

        imagebutton auto "images/china/esquina_%s.png":
            xalign 0.15
            yalign 0.95
            action Call("chinatown_esquina")

    else:

        add "images/china/esquina_hover.png":
            xalign 0.15
            yalign 0.95

    if not chinatown_area == "entrada":

        imagebutton auto "images/china/entrada_%s.png":
            xalign 0.25
            yalign 0.95
            action Call("chinatown_entrada")

    else:

        add "images/china/entrada_hover.png":
            xalign 0.25
            yalign 0.95

    if not chinatown_area == "caminho":

        imagebutton auto "images/china/caminho_%s.png":
            xalign 0.35
            yalign 0.95
            action Call("chinatown_caminho")

    else:

        add "images/china/caminho_hover.png":
            xalign 0.35
            yalign 0.95

        imagebutton auto "images/china/templo_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("cenario_templo")

        imagebutton auto "images/china/portal_%s.png":
            xalign 0.15
            yalign 0.75
            action Call("chinatown_portal")

screen chinatown_tela():
    tag chinatown

    predict False
    zorder 100
    modal True

    if not chinatown_area == "geral":

        imagebutton auto "images/china/china_%s.png":
            xalign 0.05
            yalign 0.95
            action Call("cidade_chinesa")

    else:

        imagebutton auto "images/mapa/ilha_%s.png":
            xalign 0.05
            yalign 0.95
            action [ Hide("chinatown_tela"), Jump("chinatown_voltar") ]

        imagebutton auto "images/china/caminho_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("chinatown_caminho")

        imagebutton auto "images/china/vista_%s.png":
            xalign 0.15
            yalign 0.75
            action Call("chinatown_vista")

    if not chinatown_area == "superior":

        imagebutton auto "images/china/superior_%s.png":
            xalign 0.25
            yalign 0.95
            action Call("chinatown_superior")

    else:

        add "images/china/superior_hover.png":
            xalign 0.25
            yalign 0.95

        imagebutton auto "images/china/banho_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("chinatown_banho")

    if not chinatown_area == "rua":

        imagebutton auto "images/china/rua_%s.png":
            xalign 0.15
            yalign 0.95
            action Call("chinatown_rua")

    else:

        add "images/china/rua_hover.png":
            xalign 0.15
            yalign 0.95

        imagebutton auto "images/china/esquina_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("chinatown_esquina")






    if not chinatown_area == "lamen":

        if tempo < 3:

            imagebutton auto "images/china/lamen_%s.png":
                xalign 0.35
                yalign 0.95
                action Call("chinatown_lamen")


    else:

        add "images/china/lamen_hover.png":
            xalign 0.35
            yalign 0.95

        imagebutton auto "images/china/bao_%s.png":
            xalign 0.05
            yalign 0.75
            action Call("chinatown_bao")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
