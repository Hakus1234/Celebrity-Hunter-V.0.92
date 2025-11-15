label naru_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("y1_save", extra_info="y1_save")

    $ estou_na_cidade = False
    $ iconchefe += 1

    $ naru_e1 = "evento"

    $ naru_beijo1 = False
    $ naru_ape = False

    "Uaaaahhhh... é tão cedo... não queria ir ter que trabalhar agora."

    scene black with dissolve

    scene trabalho geral with Dissolve(1.0)

    pause

    "Desde que a [w] chegou eu tô vindo bem mais pra redação. Conseguir pautas não é mais o suficiente."

    "Agora ela quer que todo mundo leia e cheque matérias, informações, pra ver se tudo bate."

    "Ela disse que não quer mais nada que não seja 100%% verdade na revista. E claro que isso só dá mais dor de cabeça."

    w "[mc]. Que bom que você veio."

    mc "Tive que vir, né..."

    scene so4_sofia_redacao1 with Dissolve(1.0)

    w "Vai ter um evento hoje no centro e preciso mandar alguém pra lá pra cobrir um dos participantes."

    mc "Hm? Evento? Participante?"

    w "Você foi escolhido após um processo justo de escolha."

    mc "Como foi esse processo? Quando aconteceu?"

    w "Aconteceu faz 10 minutos. E o processo foi uma partida legal de jokenpô, também conhecido como 'pedra, papel e tesoura'."

    mc "Eu sei o que significa. Mas eu acabei de chegar. Não participei de nada disso."

    w "Eu sei. Eu joguei no seu lugar e perdi. Me perdoe."

    mc "Você jogou no meu lugar, perdeu e agora eu tenho que ir nesse evento?"

    w "Exatamente. Mais alguma pergunta?"

    mc "Quê?!"

    w "É melhor você participar sabendo de tudo. Por isso, pode perguntar o que quiser."

    "Mas que jeito incrível de passar o dia."

    scene so4_sofia_redacao2 with Dissolve(1.0)

    label naru_e1_perguntas:

        mc "É..."

    menu:
        "Que evento é esse?":


            mc "Que evento é esse aí?"

            w "Eu não sei exatamente, mas é um encontro de quem gosta de mangás, animes, cosplay e games. Chama Ganime Expo."

            mc "Ganime expo..."

            w "Isso. Tem palestras, exibição de animes, tem stands de lojas vendem mangás, concursos de cosplay, campeonato de games..."

            mc "Isso é outro mundo pra mim. Eu no máximo jogo aí um pouco..."

            w "Não importa se você gosta ou não, você precisa saber das coisas, [mc]. Pelo menos por cima."

            mc "Ok, ok..."

            w "Ainda mais que você vai ter que falar com uma pessoa desse mundo. E um bocado ainda. Quero só ver..."

            mc "Tô ferrado..."

            w "Mais alguma pergunta?"

            jump naru_e1_perguntas
        "Que horas começa?":


            mc "Quando começa e até que horas eu tenho que ficar lá?"

            w "Começa daqui uma hora. O evento dura o dia todo."

            mc "Mas eu não tenho que ficar todo esse tempo lá, né?"

            w "Não, você precisa ficar só até o final do concurso de cosplay, que é onde ela vai se apresentar."

            mc "Certo. E quando que é isso?"

            w "É a última atração."

            mc "Mas só pode ser brincadeira..."

            w "..."

            w "Mais alguma pergunta?"

            jump naru_e1_perguntas
        "Quem é a celebridade?":


            mc "Quem é essa celebridade? É um proplayer? Aqueles jogadores profissionais?"

            w "Não. É uma moça na verdade. Ela é cosplayer e tem um canal com centenas de milhares de seguidores no YouTube."

            mc "Cosplayer... que que é isso mesmo?"

            w "Cosplayers são pessoas que confeccionam e vestem fantasias de personagens de filmes, animes, games etc."

            w "Alguns deles também interpretam o personagem. Acho que ela vai fazer isso. Depois do concurso ela vai se apresentar lá."

            mc "Então ela vai se vestir de um personagem e é isso? Ela ganha rios de dinheiro assim?"

            w "A garota tá virando um fenômeno online. O Instagram dela tá crescendo muito. Ela posta praticamente o dia todo."

            w "Além do dinheiro com os vídeos, ela já tem marcas que anunciam nos perfis dela. Vale à pena pra revista com certeza."

            mc "Caramba, [w]... o que eu vou falar com essa garota?"

            w "Dá seus pulos."

            w "Mais alguma coisa?"

            jump naru_e1_perguntas
        "Eu já sei o que eu preciso.":


            mc "Não, tá bom."

    w "A gente recebeu um release do evento que tem todas essas informações. Fala sobre ela também. Dá uma boa lida antes de chegar lá."

    mc "Tá bom, pode deixar."

    w "Agora pode ir. Até você pegar o ônibus e chegar lá vai demorar."

    mc "Bem que podia rolar um carro pra gente usar aqui. Impossível que as outras equipes de notícia tenham que ir de busão."

    w "É normal que se tenha carros de reportagem."

    mc "Isso que eu tô falando."

    w "Mas a diretoria não quer gastar com isso. Então é bom você se apressar."

    mc "Tudo mão de vaca..."

    w "Tchau, [mc]."

    mc "Tô indo, tchau..."

    scene black with Dissolve(1.0)

    "Muquiranas..."

    call locomocao from _call_locomocao_20

    scene rua_japonesa with Dissolve(1.0)

    pause

    "Sorte que o motorista do ônibus sabia onde era. Eu não venho muito pra esse lado aqui."

    "Não sabia que tinha um bairro japonês aqui na capital. Aparentemente tem de tudo nessa cidade."

    "Agora, deixa eu procurar..."

    mc surpreso "Ah?!"

    "Tem uma fila pra lá! Caralho! Tá dando a volta no quarteirão! Impossível que exista tanta gente estranha..."

    "Pessoas de todas as idades... criança, adulto, adolescente... não dá pra imaginar que tenha tanta gente envolvida nisso."

    "Tomara que eu não tenha que pegar essa fila."

    "Opa. Tem uma mulher que deve ser da organização."

    mc normal "Bom dia."

    scene y1_garota1 with Dissolve(1.0)

    pause

    "Garota" "Olá!"

    mc "Eu vi você ajeitando a fila. Você é da organização?"

    "Garota" "Sou, sim! Você precisa comprar a entrada ali e depois ir pro fim da fila. Tá um pouquinho grande... Gomen!"

    mc envergonhado "Sem querer dar carteirada, mas eu sou da revista da ilha. Eu vim cobrir o evento."

    "Garota" "Você é da imprensa! Oh! Sugoi!"

    mc "Hehe..."

    "Garota" "Eu vou ajudar você a entrar. Quer que eu te leve pra alguma área específica?"

    "Garota" "A gente tem a área gamer, os stands, o palco principal e o palco do concurso de cosplay."

    mc charmoso "Se você puder me deixar onde os cosplayers estão eu agradeceria bastante."

    "Garota" "Os cosplayers ficam andando pelo evento até começar as apresentações do concurso."

    mc normal "Entendi... eu tô procurando... é... uma garota chamada Naru."

    "Garota" "AAH! Kawaii! A Naru é a grande atração do dia! Nem acredito que eu vou poder ver ela hoje!"

    mc "Ela é tão bacana assim?"

    "Garota" "Claro! Eu sigo ela no Insta, no Face, no YouTube, tô no server do Discord dela e tudo!"

    mc envergonhado "Caraca..."

    "Garota" "Eu não sei se ela já chegou, mas a gente pode perguntar! Eu levo você."

    mc charmoso "Valeu."

    "Garota" "Nossa... o evento tá meio forte hoje, né?"

    mc normal "Verdade."

    "Garota" "Só faltava bater um vento bem forte e levantar minha sai-"

    scene y1_garota2 with hpunch

    "Garota" "Ayyeeeeee!"

    mc surpreso "!"

    "Garota" "Olha pra esse vento!"

    mc safado "Verdade..."

    "Garota" "Você tá olhando pra minha calcinha?!"

    menu:
        "Claro que não!":


            mc preocupado "Não! Eu só me assustei com seu grito!"

            "Garota" "Então tá! Vamo sair desse vento!"

            mc "Ok!"

            scene black with Dissolve(1.0)
        "É impossível não olhar!":


            mc tarado "Eu tenho que olhar! É impossível não ver com a saia assim!"

            "Garota" "Tarado!"

            mc angustiado "N-não!"

            scene black with hpunch

            "{i}Kapow!!!{/i}"

            mc "Ai!"

    "..."

    "Garota" "Por aqui."

    "..."

    scene stage_geral with Dissolve(1.0)

    pause

    "Garota" "Aqui é onde vai acontecer a apresentação dos cosplayers. A gente vai abrir com o show da Naru."

    mc normal "Obrigado. A apresentação dos cosplayers vai ser a última, né?"

    "Garota" "Sim. Vai demorar um pouco até lá. Acho que vale à pena você ver as outras áreas do evento."

    "Garota" "Agora eu vou lá senão as filas viram uma bagunça."

    mc charmoso "Tá legal. Muito obrigado por toda a ajuda. Você foi muito bacana."

    "Garota" "Que isso... Ja ne!"

    mc desconfiado "Já o que?"

    "..."

    "Ok, o que será que eu faço aqui?"

    "Minha tarefa é colar nessa Naru, então é melhor eu não me aventurar por aí."

    "O foda é o que será que eu vou falar com ela? Será que eu só pergunto as coisas tipo uma entrevista?"

    "'Como é ser uma sensação da internet?' Nossa... horrível. Talvez se eu mudar um pouco a forma..."

    "Talvez algo mais casual, tipo 'Como vai a tropa?'..."

    mc zerado "Nem eu sei o que isso significa."

    "Olhando aqui a seção de comentários do Youtube eu tô achando que congelei no tempo. Nem sei o que metade das coisas quer dizer."

    "Tô fodido... apenas."

    "Agora é só esperar ela. Deve demorar um bocado..."

    show black with dissolve

    "..."

    hide black with dissolve

    "Afe... deve fazer mais de uma hora que eu tô aqui e nem sinal de qualquer alma viva."

    "Será que vale à pena dar uma andada? Eu podia ir falar com a garota da entrada."

    "Ela era bem... interessante..."

    menu:
        "É mais seguro eu ficar esperando.":


            $ naru_amizade += 2

            "Melhor eu ficar aqui e esperar ela."

            mc zerado "Mesmo que seja um saco."

            "..."

            "Nem sinal dela ainda..."

            "Dá pra ouvir o barulho do pessoal no evento. Essa galera parece ser super animada."

            "Eu tenho a impressão de ter visto uma galera com uma plaquinha 'querendo abraço'. Será que eu li certo?"

            y "Acabei de chegar, meus fofos! O evento tá incrível!"

            mc desconfiado "Hm?"

            scene y1_evento1 with Dissolve(1.0)

            pause

            y "Não vejo a hora de mostrar tudo pra vocês! Vai ser incrível!"

            y "A Ganime Expo deste ano vai ser demais! E eu tô suuuuper ansiosa de encontrar meus fofos aqui hoje!"

            y "Eu sei que tem muita gente que tá vindo me ver. Quero tirar foto com todos vocês!"

            y "Pra quem não conseguiu vir, fiquem de olho que eu vou postar tudo nos stories e no meu canal, claro!"

            y "Kisu!!!"

            "Só pode ser ela..."

            mc normal "Olá."

            y "Só um segundinho... tá publicando... foi."

            y "Vou sentar. Vem aqui comigo."

            mc envergonhado "Tá."
        "Acho que vou lá fora conversar com a mina.":


            "Foda-se, vou lá falar com ela. Se a tal da Naru chegar ela que espere."

            scene black with Dissolve(1.0)

            "..."

            mc normal "Oi."

            "Garota" "Oi!"

            scene y1_garota1 with Dissolve(1.0)

            "Garota" "Aconteceu alguma coisa?"

            mc charmoso "Não, eu só tava dando uma olhada no evento e acabei saindo pra tomar um ar."

            "Garota" "A tá."

            mc "Desculpa, aquela hora a gente tava meio correndo, nem falei meu nome. Eu sou [mc], prazer."

            "Talita" "Ah! Eu sou a Talita"

            mc "Que nome bonito."

            "Talita" "Verdade?"

            mc "Sim. Você é muito simpática, Talita. Você tem muito jeito pra trabalhar com eventos. Parabéns."

            "Talita" "Ai, obrigada. Você também é simpático..."

            mc "Valeu. Você vai ficar aqui o evento todo?"

            "Talita" "Sim. E você? Ah, você vai ficar até a apresentação dos cosplayers, né?"

            mc "Isso. Vou ter que ficar, coisas do trabalho."

            "Talita" "Que inveja poder conversar tanto com a Naru!"

            mc "Quer que eu mande um beijo seu pra ela?"

            "Talita" "Sério?! Claro!"

            mc "Pode deixar que eu mando. Agora eu vou voltar lá. Não quero perder quando ela chegar."

            "Talita" "Tá! Obrigada."

            mc "Mas algum dia a gente podia sair. Você podia me falar como é cuidar de um evento e eu te falo da Naru."

            "Talita" "Parece legal! Você mora por aqui?"

            mc "Sim. Mas na ilha."

            "Talita" "Que chique..."

            mc "Posso anotar seu telefone? Daí te mando uma mensagem?"

            "Talita" "P-pode..."

            scene black with dissolve

            "..."

            mc charmoso "Foi legal conversar com você, Talita. Depois eu te escrevo."

            "Talita" "Tá. Tchau, [mc]."

            "..."

            scene stage_geral with Dissolve(1.0)

            "Tá vazio aqui ain-"

            "Opa! Tem uma garota de cabelo roxo sentada ali..."

    scene y1_evento2 with Dissolve(1.0)

    pause

    "Com esse cabelo, essa roupa... gravando alguma coisa no celular... só pode ser ela."

    mc envergonhado "Com licença. Você é a Naru, né?"

    y "Só um minuto fofo, vou gravar."

    y "{i}cof cof{/i}"

    y "{i}puuuuuuft{/i}"

    $ y_nome = "Naru"

    y "Ohayo, fofos! Aqui é a [y] direto da Ganime Expo! Eu já tô aqui pronta pra encontrar vocês!"

    y "Eu sei que muita gente veio pra cá pra me ver, mas quem não tem problema nenhum!"

    y "Aqui no canal vai ter uma stream completinha pra você ver ao vivo a [y] inteirinha de arlequina!"

    y "Queria agradecer a Akio Cosplays pelo mimo! Eu adorei o cosplay! Ficou perfeito na [y], né, fofos?!"

    y "E o pessoal da Ganime Expo também merece muito amor de vocês! É a primeira vez que eles me chamaram!"

    y "A [y] vai dar o melhor pra que tudo seja perfeito pra vocês!"

    y "A gente se vê logo loguinho, fofos! Kisu!"

    menu:
        "...":


            $ naru_amizade += 1

            "Melhor eu ficar na minha."

            "..."

            y "Tenho que escolher um nome... 'Ganime Expo: Tô Aqui!'."

            y "Agora as tags... uma thumb..."

            y "Tomara que o pessoal fique empolgado!"
        "Você parece bem animada.":


            mc envergonhado "Puxa, você tem bastante energia. Parece bem animada."

            y "Só um segundinho..."

            mc "Desculpa."

            y "Hm-hm-hmmm..."

    y "Publicando..."

    y "Prontinho."

    mc normal "O que você publicou?"

    y "Tava postando sobre o evento. Se eu não postar nos stories o pessoal vai ficar bravo comigo."

    mc "Entendi."

    y "Aliás, o que você tá fazendo aqui? O evento vai demorar um pouco pra começar ainda."

    mc "Ah. Meu nome é [mc]. Eu sou o jornalista que vai te acompanhar hoje."

    scene y1_evento3 with Dissolve(1.0)

    pause

    y "Ah. Que estranho..."

    mc "Que foi?"

    y "Achei que iam mandar alguém mais novo."

    mc "Mais novo?"

    y "Não é por nada! Mas normalmente quem cobre essas coisas são mais jovens..."

    menu:
        "Eu sou novo o suficiente.":


            $ naru_amizade += 1

            mc "Não esquente, eu sou novo o suficiente."

            y "Haha! Eu juro que não falei pra criticar! Você não é velho nem nada!"

            mc "Eu entendi. Prometo que não me ofendeu."

            y "Ok."
        "A verdade é que eu perdi uma aposta.":


            mc "A verdade é que eu perdi uma aposta lá na revista e sobrou pra mim."

            y "Sério? Ninguém queria vir?"

            mc "Não é nada com você ou o evento. Falou em trabalhar o dia todo, acho que ninguém gosta."

            y "Hmm..."

    y "Eu sei que esse é um mundo bem diferente. Não é pra qualquer um."

    mc "Vou ser sincero com você, eu praticamente não manjo nada disso. É o primeiro evento que eu venho."

    mc "No máximo eu jogo um pouco no console em casa quando dá tempo. Mas assim, é nível iniciante haha..."

    y "Eu tava prevendo isso... você é meio normal..."

    mc "Eu sou velho e agora 'normal'?"

    scene y1_evento4 with Dissolve(1.0)

    pause

    y "Hihi... quando falaram que alguém da revista ia vir pra me acompanhar, eu achei que ia ser um maninho de óculos e cabelo tigelinha."

    mc "Entendi. Eu não correspondi às suas expectativas de estilo?"

    y "Foi uma surpresa boa, vai. Você parece legal."

    mc "Eu vou mostrar que até um velho normalzão pode te acompanhar."

    y "Hahaha para! Ouvir isso dá vergonha alheia! Eu não tava te trollando!"

    mc "Tá beleza. Mas acho que eu vou precisar mesmo de um pouco de ajuda pra entender tudo isso."

    mc "Eu dei uma olhada nos seus perfis, mas você com certeza sabe muito mais do que eu."

    y "Tudo bem. O que você quer saber?"

    mc "Primeiro de tudo, me fala que lance é esse de ser uma estrela do Youtube."

    y "Que pergunta mais de jornalista..."

    mc "Eu sabia que você ia pensar isso, só que vamos começar devagar."

    y "Tá... não é nada de mais. Eu comecei um canal faz uns anos e de uns tempos pra cá ele cresceu bastante."

    y "Minha vida continua a mesma coisa. Eu só faço mais vídeos agora. E tenho também o Instagram que eu posto minhas fotos e vídeos."

    menu:
        "E isso dá muito dinheiro?":


            mc "E esse trabalho dá bastante dinheiro?"

            y "Não quero falar de dinheiro, mas é o suficiente pra eu poder viver e trabalhar só com isso."

            y "Eu amo trabalhar com isso e, nossa, sou super agradecida por poder fazer disso minha profissão."

            mc "Entendi... é estranho pensar que uma pessoa ganha a vida com isso."

            y "Porque você não conhece. Tem gente que fica milionária com redes sociais."

            mc "Interessante..."
        "Por que você acha que te seguem?":


            $ naru_amizade += 1

            mc "Por que você acha que todas essas pessoas te seguem e te assistem?"

            y "Essa é uma boa pergunta... é... eu também não sei direito!"

            mc "Haha... se você tivesse que chutar alguma coisa."

            y "Eu acho que eles gostam de mim. Gostam do que eu faço e do meu dia-a-dia. Acho que é isso."

            y "Eu sou uma pessoa verdadeira e acho que eu passo uma boa vibe."

            y "Eu também tô sempre em eventos e falo sobre cosplays, como fazer, faço reacts e até canto de vez em quando."

            mc "Conteúdo bem variado."

            y "Sim. Mas eu realmente acho que tem mais a ver com meu jeito do que com o que eu faço. As pessoas gostam do jeito que eu sou."

            mc "Certo."
        "Chega de perguntas.":


            jump naru_e1_depois

    mc "Agora, eu quero saber mais sobre essas pessoas que seguem você."

    y "Tá. Ah! Só um instantinho."

    mc "Que foi?"

    scene y1_evento5 with Dissolve(1.0)

    pause

    y "Esqueci de postar no feed. O bom é que já manda direto pro Face e pro Twitter."

    y "Daí já aproveito pra responder uns comentários."

    window hide

    pause

    "Esse sorriso dela é meio estranho... será que seria falta de educação perguntar sobre isso?"

    "Ela é tão bonita. Acho que a descendente de japonesa mais linda que eu já vi."

    "Só que essa sorriso... é como se tivesse alguma coisa errada, sei lá."

    "Agora... Será que rolaria alguma coisa entre a gente? Nah... acho que eu não faço o tipo dela."

    mc "Então você responde comentários? Dá tempo?"

    y "Eu adoro interagir com a comunidade. A maioria é super bacana e tá sempre me colocando pra cima."

    y "Tem uns tarados também e os haters, claro. Tem uns que comentam coisas negativas em TODA POSTAGEM."

    mc envergonhado "Esses são os maiores fãs pelo jeito."

    y "Parece mesmo... bando de desocupado."

    menu:
        "Você não acha que essa roupa é sexy demais?":


            $ naru_amizade += 2

            mc "Você falou de tarado. Você não acha essa roupa sexy demais? Não atrai esse público?"

            scene y1_evento6 with Dissolve(1.0)

            y "É. Eu sei que é um pouco culpa minha, mas é um preço pequeno. A maioria só olha e não fala nada. São poucos que são ignorantes."

            mc "E por que você optou por esse cosplay mais... sensual?"

            y "Você atrai muito mais público com roupa provocante, sabe? As meninas gostam de um roupa bonita, mas os garotos querem ver meu corpo mesmo..."

            y "Meus pais nunca deixaram eu usar roupa assim antes de fazer 18. Mas agora eles dizem que eu que tenho que decidir."

            y "Eu não me sinto mal vestida assim. Eu gosto de ser sexy. Só queria que os rapazes fossem menos idiotas e ficassem na deles."

            mc envergonhado "Às vezes nós homens exageramos..."

            y "Igual eu falei, a maioria é super boazinha, mas tem uns que vou falar... fico com vontade de banir na hora."

            mc normal "E o pessoal que acha que isso é errado? Tipo, 'imoral'?"

            y "Isso eu nem ligo, de verdade. Quando a 'moral' dessas pessoas pagar minhas contas eu escuto o que elas têm pra falar."

            mc "Haha... boa resposta."
        "Melhor não perguntar isso.":


            "Vou só ficar na minha. Vai que ela não gosta da pergunta."

    label naru_e1_depois:

        pass

    mc "Não vou ficar te enchendo de perguntas também. Só queria saber como vai ser daqui pra frente."

    mc "Como é o futuro de alguém que, igual você falou, meio que apareceu do nada?"

    scene y1_evento7 with Dissolve(1.0)

    pause

    y "Isso... é uma coisa meio incerta, né?"

    y "Essa coisa na internet é igual um... sei lá, uma bomba. Você aparece do nada, mas é fácil perder tudo também."

    y "Hoje em dia as pessoas não querem mais ser astronauta. Elas querem fazer sucesso no Youtube, no Instagram."

    y "As pessoas fazem de tudo pra aparecer. Por isso que tem muita garota aí quase nua e moleque que nem dorme streamando."

    mc desculpa "Acaba sendo uma grande pressão pra você."

    y "Sim. Eu preciso tá sempre tendo ideias pra movimentar meus perfis. E claro que eu não posso sumir. É todo dia postando."

    y "Se eu ficar um dia sem postar, talvez meu público vá procurar em outro lugar e encontrar a próxima celebridade deles pra seguir."

    mc normal "Mas você ganha o suficiente pra juntar se acontecer o pior?"

    y "Não. Claro que a gente ganha um dinheiro, mas é menos do que as pessoas acham."

    mc envergonhado "Entendi. Mas se serve de consolo, minha situação tá bem pior que a sua. Isso eu posso garantir."

    y "Essa conversa até já deu uma ansiedade. Deixa eu gravar outra coisa rapidinho aqui."

    scene y1_evento8 with Dissolve(1.0)

    pause

    y "Oi, fofos! O evento começa daqui a pouco! Vocês tão empolgados?!"

    y "Eu tô muuuuuito empolgada! Já tô aqui onde vai ter o concurso de cosplay e o lugar é bacana! Dá pra sentar ou ver de pé."

    y "Vocês vão ver a melhor Arlequina do mundo, hein?!"

    y "A gente se fala daqui a pouquinho! Kisu!"

    y "Postando..."

    y "Pronto."

    y "Acho que ficou bem legal."

    menu:
        "O pessoal vai gostar.":


            mc normal "Seus seguidores vão gostar."

            y "Tomara... tá quase na hora do evento. Eu quero que eles vejam a stream."

            mc envergonhado "O que é stream mesmo?"

            y "É um vídeo ao vivo. Hoje em dia tem vários sites de streams. Tem muito de gente jogando, mas tem de outras coisas também."

            mc normal "Entendi. Tô ligado."
        "Você fica no celular o dia todo?":


            $ naru_amizade += 1

            mc envergonhado "Você fica com o celular o tempo todo?"

            y "Claro. Tenho que ficar. Eu tô o dia todo gravando conteúdo."

            mc "E não cansa?"

            scene y1_evento6 with Dissolve(1.0)

            y "Às vezes eu nem quero mais olhar pro celular. Mas é minha profissão. Aposto que você não faz só o que você quer."

            mc envergonhado "Realmente... desde que eu comecei na revista, eu só tô vivendo doideira. Nem sempre acaba como eu quero."

            y "Isso é normal. Eu ainda trabalho fazendo vídeo de mim. Nem sei se isso é trabalho de verdade..."

            mc desconfiado "Por que não seria?"

            y "Sei lá... não quero falar sobre isso."

            mc desculpa "Beleza."

    y "Pra mim é importante que dê bastante visualizações. É a primeira vez que a Ganime Expo me chamou pra participar."

    mc normal "Daí se seu conteúdo der bastante visibilidade, eles te chamam de novo?"

    y "Tipo isso. O que eu faço depende das pessoas gostarem. Se elas não curtirem e não assistirem, é fim da linha."

    mc desculpa "Parece bem tenso."

    y "É, mas é tranqui-"

    "Garoto" "Atenção! As portas vão abrir em 10 minutos! Tá cheio de gente esperando então vão entrar com tudo!"

    y "Ah! Olha a hora. Eu tenho que me preparar. Vou repassar as linhas e ver com o pessoal do som."

    mc normal "Beleza."

    scene y1_evento9 with Dissolve(1.0)

    pause

    y "E aí? Foi interessante?"

    menu:
        "É um mundo diferente, mas eu tô interessado.":


            mc "Sendo bem sincero, eu cheguei aqui sem saber quase nada sobre isso, mas eu fiquei interessado em saber mais."

            mc "Esse mundo é algo super rápido e envolve bastante gente. Acho que é importante saber mais sobre isso."

            y "É o futuro, né?"
        "Acho que eu tô velho demais pra tudo isso.":


            $ naru_amizade += 2

            mc "Acho que eu entendo melhor agora, mas você tinha razão. Acho que eu tô velho demais pra tudo isso."

            y "Sérião? Eu achei que você foi bem. Eu esperava menos depois que vi você com essa camiseta branca e calça jeans."

            mc "Nada... acho que eu estraguei tudo. Eu devia ter pesquisado mais sobre seu trabalho."

            y "Eu não posso falar sobre seu trabalho, mas eu acho que ser velho não tem a ver com idade, sabe?"

            mc "O importante é que o coração sustente a juventude que nunca morrerá?"

            y "Usar referências dos anos 90 não ajuda no seu caso, mas tem uma coisa que eu falo pros meus pais quando eles não entendem o que eu faço."

            mc "O quê?"

            y "Ser velho demais é quando a gente desiste de aprender coisas novas e fica preso no que a gente acha bom e tá acostumado."

            y "Se você é velho demais pra me acompanhar você que vai decidir. Eu acho que você leva jeito."

            mc "Valeu. Isso foi bem legal agora."

    y "Minha apresentação vai começar daqui a pouco. Presta atenção."

    mc "Eu vou. Com certeza."

    y "Depois, se você tiver afim, a gente pode conversar mais um pouco... eu tô com a noite livre."

    mc "Opa. Seria legal, sim. Vou tá aqui esperando."

    y "É interessante como você tem paciência... não sei se é exatamente isso, mas, sei lá."

    mc "Como assim? Paciência com o quê?"

    y "Meus vídeos e stories têm poucos minutos. Se eu fizer maior que isso, as pessoas param de ver no meio."

    y "Parece que se a gente não for interessante o suficiente as pessoas só te abandonam..."

    y "Mas, mesmo com você falando sobre um monte de coisa que você não entende e nem se interessa tanto..."

    y "Mesmo assim... você continuou me ouvindo... foi um sentimento bacana, sabe?"

    y "Mas é seu trabalho também, né? Desculpa por falar essas coisas. É super cringe."

    mc "Haha... não pensa demais nisso. Foi bacana. Boa sorte na sua apresentação. Eu vou tá aqui."

    y "Tá... até depois."

    scene black with Dissolve(1.0)

    scene stage_geral with Dissolve(1.0)

    "Acho que até aqui as coisas foram melhores do que eu imaginava."

    "Ainda não descobri nada bombástico suficiente pra revista, mas a [y] é uma garota interessante com certeza."



    "E eu acho que ela curtiu nossa conversa. Eu acho... não foi perfeita. MAS! Ela até falou de conversar depois."

    "Agora vou dar uma olhada nessa apresentação dela e talvez depois a gente converse mais um pouco."

    "Se bem que já faz horas que eu tô aqui. Sei lá se eu tô afim de ficar aqui mais do que eu preciso."

    "Garoto" "Tô abrindo as portas!"

    mc zerado "Ixi, lá vem a galera."

    scene black with vpunch

    "{i}Dump dump dump{/i}"

    "Garoto" "Não precisa correr! Cuidado!"

    "Caraca, tem muita gente mesmo. O pessoal parece louco pra ver a [y]."

    "Apresentadora" "Olá, pessoal! Tá todo mundo pronto?!"

    "Público" "Siiim! Começaaa!!"

    "Apresentadora" "Como todo mundo sabe, esse ano a Ganime Expo tem uma companhia muito especial!"

    "Apresentadora" "A Arlequina mais fofa, linda e doidinha do país!"

    scene y1_stage1 with Dissolve(2.0)

    pause

    $ y_nome = "Arlequina"

    y "Hahaha! Então todos meus fofos estão aqui?!"

    y "Fugir do Asilo Arkham e da polícia não é fácil, mas eu precisava ver vocês e deixar algumas pérolas de sabedoria!"

    "Jovem" "Linda! Naru eu te amo! Tira uma selfie comigo!"

    "Garota" "Eu te amooo!"

    y "Tenham calma, fofos! Prestem muita atenção porque eu só vou falar uma vez!"

    scene y1_stage2 with Dissolve(1.0)

    pause

    y "Só confie em alguém que consiga ver estas três coisas em você, fofos!"

    y "A dor por trás do seu sorriso, o amor por trás da sua raiva e a razão por trás do seu silêncio!"

    y "É o que eu sempre falo! Não importa o quão insano você é, existe sempre alguém para completar a sua insanidade!"

    scene y1_stage3 with Dissolve(1.0)

    pause

    y "O meu amor pelo Coringa era mais forte que as paredes de um asilo! Isso todos vocês sabem, né?!"

    y "Não agora! Nunca mais! Acabou a obsessão, acabou a loucura, acabou o Coringa!"

    y "Finalmente eu vejo o que ele é! Vocês não conseguem ver?! Ele não passa de um assassino, manipulador que nunca irá mudar!"

    "Garota" "Você merece coisa melhor, [y]!"

    "Jovem" "Isso! Fica comigo!"

    scene y1_stage4 with Dissolve(1.0)

    pause

    y "Eu sei que vocês me amam, fofos! Mas eu não tô procurando alguém que questione minha loucura, e sim alguém que faça parte dela."

    y "Será que vocês aguentam? Me trate como um jogo e eu lhe mostro como se joga!"

    "A [y] é muito carismática. A molecada tá ficando louca com ela."

    "E todas essas falas. Devem ser tudo frases da personagem mesmo. Não é só roupa, mas esse jeito de falar e até o que é falado."

    "Deve dá um trabalhão decorar tudo isso e ainda por cima a fantasia e as publicações. Ela deve correr pra caramba."

    y "Calma, meus fofos, não digam uma palavra, mamãe vai matar o mundo inteiro por vocês, queridos."

    y "Eu amo vocês aqui! Eu amo quem me vê de casa, do trabalho! Eu vou fazer tudo por vocês!"

    y "Agora... me passa aqui um negócio!"

    scene y1_stage5 with Dissolve(1.0)

    pause

    y "Você acha que dá medo? Tá vendo isso aqui?! Eu já conheci o medo, e você não tem o sorriso dele!"

    y "Não importa quem magoou você ou partiu seu coração, o que importa é quem fez você sorrir de novo."

    y "Não ligue pra quem não te ama, fofos! Às vezes você precisa juntar duas pessoas loucas pra ter uma relação normal, entende?!"

    scene y1_stage6 with Dissolve(1.0)

    pause

    y "Deixe de se estressar por pessoas que não valem a pena. É a dica que eu dou pra vocês!"

    y "Porque se eu ficar brava com você, isso significa que ainda me importo. Preocup quando eu não ficar brava."

    scene y1_stage7 with Dissolve(1.0)

    pause

    y "Agora, pra acabar, eu quero que vocês encontrem algo que vocês amem e deixem que isso mate vocês."

    y "Pode ser o Coringa, pode ser eu. Eu amo todos vocês, fofos!"

    "Público" "Linda! Gata! A gente te ama!"

    y "Eu também amo vocês, meus amores! Me acompanhem no Insta e no canal! Tem vídeo novo todos os dias!"

    y "Um abraço, Ganime Expooo! A gente se vê! Kissu!!!"

    scene black with Dissolve(1.0)

    mc normal "Uou. Foi bem legal."

    "Acho que eu vou seguir ela. Ela foi por uma porta ali do lado."

    "..."

    $ y_nome = "Naru"

    mc normal "[y]! Oi!"

    y "Oi!"

    scene y1_evento10 with Dissolve(2.0)

    pause

    mc charmoso "Ou eu chamo você de Arlequina?"

    y "O que você achou?"

    menu:
        "Meio vergonha alheia, mas é assim mesmo, né?":


            mc envergonhado "Eu fiquei um pouco com vergonha alheia haha... mas não por sua causa. Foi tudo. Eu nunca tinha visto alguma coisa assim."

            y "Você não entende nada disso, né? Deve ser bem estranho mesmo."

            mc "Pois é... mas deu pra ver que eles gostaram."
        "Foi bem legal. O pessoal adorou.":


            $ naru_amizade += 1

            mc normal "Eu achei bem legal. Você decorou as falas dela e o pessoal ficou louco. Foi um sucesso."

            y "Você achou mesmo?"

            mc charmoso "Com certeza. Você não viu como eles tavam gritando? Tava esperando alguém te pedir em casamento."

    y "Eles são sempre assim. São uns fofos. Tantos os meninos como as meninas. Eles são tudo pra mim."

    mc charmoso "Dá pra ver mesmo o carinho que você sente por eles."

    y "Agora eu vou pro hotel. O pessoal da produção vai me deixar lá. Você tá afim de ir comigo?"

    mc surpreso "P-pro seu quarto no hotel?!"

    y "Calma! Não tô querendo insinuar nada, bobo. Eu nem lembro seu nome..."

    mc zerado "É [mc]."

    y "Isso! Eu só achei que... talvez você quisesse conversar um pouco mais. Conhecer minha rotina fora dos eventos."

    y "Eu pensei que os paparazzi fizessem isso..."

    mc envergonhado "Então..."

    "Será que ela só tá me chamando pra uma conversa mesmo? Mas chamar assim um cara que ela nem conhece..."

    "E se eu for um assassino? Que mulher descuidada... se bem que eu sou da revista, deve passar mais segurança."

    "Bom... meu trabalho era só até o fim do evento, né? Eu não tenho que seguir ela."

    "Inclusive se a [w] souber que eu fui até o apê dela, vai ficar putassa com certeza. Mas ela não precisa saber..."

    "Assim, a [y] é bonita, ela é inteligente, tem uma vibe meio doidinha, mas bem legal..."

    "Quem sabe podia até rolar alguma coisa, né? Só nós dois no apê dela... uma coisa mais casual..."

    y "Alô? Tá aí?"

    mc envergonhado "Desculpa. Tava pensando..."

    y "Se você não quiser, não tem problema. Pode falar, eu não sou a Arlequina de verdade. Não vou te explodir."

    mc "Haha... ufa, agora eu tô mais de boa."

    menu:
        "Eu aceito. Vamos lá.":


            mc charmoso "Vai ser uma boa. Eu aceito, sim."
        "Acho melhor eu não ir. É mais profissional.":


            mc envergonhado "Valeu pelo convite, mas eu acho que é mais profissional se eu não for."

            y "Mas eu que tô convidando. Vem!"

            "Bom... se ela que tá chamando... será que eu vou?"

            menu:
                "Não vou. Prefiro não me envolver com ela.":


                    mc desculpa "Mesmo assim, minha chefe não vai gostar se eu for. Eu prefiro manter as coisas aqui. Quem sabe em outra oportunidade."

                    y "Tudo bem... se é melhor assim, foi legal até aqui. Até mais."

                    mc normal "Até mais, [y]. Boa sorte no seu trabalho!"

                    y "Você também."

                    scene rua_japonesa with Dissolve(1.0)

                    jump naru_e1_final
                "Tudo bem, eu vou. Você venceu.":


                    mc envergonhado "Tá legal, você ganhou. Eu vou com você."

    $ naru_ape = True

    y "Legal! Eu tô ficando em um hotel aqui no centro da capital mesmo. Dá uns 15 minutos e eles vão levar a gente."

    mc normal "Tudo bem. Eu te sigo."

    y "Tá. Vou ver se eles já podem ir."

    scene black with Dissolve(1.0)

    "..."





    y "Meu quarto é esse aqui."

    scene naru_ape_geral with Dissolve(2.0)

    pause

    y "Você se importa se eu tomar um banho? Eu tô com essa roupa desde cedinho."

    mc charmoso "Tudo bem, claro. Eu espero aqui."

    y "Obrigada. Fique à vontade."

    mc "Pode deixar."

    "É... eu realmente tô aqui. Sozinho com ela..."

    "O que meus amigos iam pensar se eles soubessem que eu tô sozinho no quarto de hotel de uma gata dessas?"

    "Do jeito que as coisas tão caminhando... pode muito bem rolar alguma coisa entre a gente aqui."

    "Eu preciso pensar direito se isso é uma boa."

    if priscila_namoro or sayuri_namoro or julia_namoro or maria_namoro or diana_namoro or nathan_namoro:

        $ namorando = True

        "Eu já tô em um relacionamento sério."

        "Pensando assim, eu nem deveria ter aceitado vir pra cá."
    else:


        "Eu não tenho nada sério com ninguém até agora. Tá de boa se eu tiver algum lance com ela."

    "Mas ela é tão fofa... ela tem bem o estilo petite. Ela é mais moleca, magrinha, bem bonequinha mesmo."

    "Além de ser famosa. Imagina sair no Insta namorando uma mina dessas? Os fãs dela iam querer me matar."

    "Assim, eu nem conheço ela direito ainda. Talvez seja melhor eu não decidir nada agora. Vamos agir naturalmente. Só isso."

    "Só uma conversa entre dois adultos, curtindo uma companhia agradável e querendo se conhecer melhor. É isso. Nada mais que isso."

    "Mas e se ela ten-"

    y "[mc]? É [mc], né?"

    mc surpreso "O-opa!"

    scene y1_ape1 with Dissolve(1.0)

    pause

    y "Terminei o banho. Desculpa a demora."

    mc charmoso "Relaxa. Foi rápido."

    y "O que você achou do quarto?"

    mc "Bem legal. Deve ser caro um quarto desse aqui bem no centro. Você tá escondendo o ouro fala aí."

    y "A organização do evento que pagou tudo. Se dependesse de mim... ia dormir na rodoviária."

    mc charmoso "Eles realmente queriam que você viesse."

    y "Sim. Mas é normal. Quando me chamam pra eventos, normalmente eles oferecem um valor, daí a viagem e a acomodação na faixa."

    menu:
        "Tá só se aproveitando dos caras, hein?":


            mc tarado "Tá só se aproveitando da fama, hein? Os produtores ficam loucos correndo atrás."

            y "Não acho que seja abusar... é só o que acontece sempre."

            mc envergonhado "Tô só tirando sarro. Se eles tão dispostos, bom pra você."
        "Não tá errado.":


            $ naru_amizade += 1

            mc charmoso "Não tá errado. Você tá aproveitando o lado bom da coisa. Se eles querem você aqui, eles que lutem."

            y "Verdade. Essa é a hora de aproveitar, né? Vai saber quanto que vai durar."

            mc "Pelo que eu vi hoje lá na apresentação, acho que bastante."

            y "Tomara!"

    mc "Então você não é aqui da capital?"

    scene y1_ape2 with Dissolve(1.0)

    pause

    y "Não. Eu venho do interior. Não é uma cidadezinha tão pequena. Tem mais de um milhão de habitantes, mas não se compara com a capital."

    mc charmoso "Entendi."

    y "Mas eu sempre quis vir pra cá. Por isso fiquei tão animada com esse convite deles."

    mc "E por que essa vontade de vir pra cá?"

    y "Aqui é o centro, né? É onde tá a inovação, o crescimento. A maioria das empresas de tecnologia tão aqui. É muito melhor pra networking."

    y "Assim que eu juntar uma grana eu pretendo mudar pra cá. Quero ficar mais perto de onde tá quente."

    mc envergonhado "Eu não sei se a capital é tudo isso. Eu já ouvi umas histórias aí que desanima qualquer um..."

    y "Ah. Mas isso acho que qualquer lugar, né? Sei lá. Eu quero vir pra cá. Já decidi isso."

    mc charmoso "Bom, se você tá decidida, tomara que dê tudo certo então."

    y "Sim! Tomara!"

    y "Agora dá só uma licencinha que eu vou dar uma olhada aqui no que o pessoal tá falando de hoje."

    mc desconfiado "Já vai pro celular?"

    y "Eu tava dando uma olhada no banheiro, mas são muitos e eu quero ver tudo."

    y "Rapidinho."

    scene y1_ape3 with Dissolve(1.0)

    pause

    y "Fique à vontade. Tem coisa no frigobar no quarto. Pode beber que eles tão pagando."

    mc envergonhado "Valeu, tô de boa."

    mc "Só tava pensando aqui. Você não vai descansar, não? Com viagem e tudo deve ter sido um dia meio corrido."

    y "Nem fala... mas se eu não responder agora ninguém vai ver."

    y "As postagens trocam super rápido. Daí se eu não comento agora, o pessoal vai pra outra."

    y "Amanhã à tarde ninguém liga mais pra Ganime Expo. As pessoas já vão tá em outra."

    mc "O negócio não para mesmo."

    y "Ah, mano... se você enrola, não tem como. A galera tá aí online 24 horas por dia, só esperando pra pegar seu lugar."

    mc "Welcome to the jungle..."

    y "Bem isso."

    "Ela parece bem confortável comigo. Tá com uma roupinha bem de boa... até meio curta demais..."

    "Será que ela tá me chamando pra alguma coisa? Acho que não... o jeito dela não parece isso."

    "Se eu avançar o sinal daí que tá tudo perdido mesmo. Uma conversa entre adultos, [mc], lembra? Só isso..."

    y "É... bastante gente viu a stream, mas podia ter sido mais..."

    mc preocupado "Foi menos do que você tinha pensado?"

    y "Não. Foi mais. Mas eu sei que tinha potencial pra ser maior que isso. Tomara que eles achem um bom resultado."

    menu:
        "Mas você tá querendo demais. Precisa ajustar a expectativa.":


            $ naru_amizade += 1

            mc envergonhado "Se foi melhor do que você esperava, então foi melhor do que você esperava. Acho que você tá exagerando."

            y "Não é assim. Se você não cresce, as pessoas começam a deixar de seguir e você só acaba."

            mc normal "Mas você disse que cresceu."

            y "É... só que... sei lá. Você entendeu."

            mc charmoso "Eu acho que você tá um pouco ansiosa. Não tem problema ficar assim um pouco, mas se você não tomar cuidado, vai sofrer à toa."

            y "Pode ser..."
        "Eu acho que eles vão querer, sim.":


            mc normal "Eles vão querer, sim."

            y "Tomara..."

    y "Agora eu vou responder uns negócios aqui. Senta e fica de boa."

    mc envergonhado "..."

    scene y1_ape4 with Dissolve(1.0)

    pause

    y "Meus seguidores são muito fofos... eles tão fazendo memes com minhas fotos e as frases da Arlequina!"

    mc normal "Que legal..."

    y "'Eu queria que o decote fosse um pouco maior pra eu ver melhor essa delícia de peito'... ai, que nojento."

    y "Será que os caras acham mesmo que alguma mulher vai gostar deles quando eles fazem esses comentários?"

    mc zerado "Impossível alguém achar que alguma garota vai gostar disso. Eles só querem zoar."

    y "Sei lá... tem muita gente sem noção na internet."

    menu:
        "É. O pior é que tem mesmo.":


            $ naru_amizade += 1

            mc envergonhado "Isso tem. Tem muita gente que fala o que quer na internet, mas quando tá cara a cara não solta um piu."

            y "É... São os revoltadinhos da internet. A maioria desses zé roelas que falam merda... se uma garota chegar neles... gagueja."

            mc "Por isso que eu não falo nada..."

            y "Você é... bacana. Até meio tímido... eu achei."

            mc "Sério?"

            y "Eu gostei. Homem que não se mostra tanto tem um... mistério. Agora quem fala demais parece papagaio."

            mc "Parece que você tem um tipo de homem também..."

            y "Dá pra ver que eu caio... é... no grupo dos que falam demais, né? Se deixar... eu não paro."
        "Sua roupa também, né?":


            mc envergonhado "Bom... sua roupa também não ajuda, né?"

            y "Ah! Vai cagar você também... Então eu vou te chamar de idiota porque eu... eu acho que você tem cara de... idiota?"

            y "A pessoa precisa ter... o mínimo de respeito e não... vomitar merda."

            mc "Haha... acho que você tá certa."

            y "Óbvio..."

            mc "Não é qualquer cara que vai ter chance com você pelo jeito."

    y "Assim... eu nem tenho tempo pra namorar... MAS, se eu fosse namorar... eu queria encontrar um cara bacana."

    mc envergonhado "Eu acho que você não tem tempo pra viver, isso sim."

    y "Hm? Quê?"

    mc "[y]... você não consegue nem olhar pra mim enquanto a gente tá conversando. Você nem completa as frases sem dar uma pausa."

    mc "É que você tá acostumada. Eu nem sei como você consegue terminar suas ideias desse jeito."

    y "Você tá exagerando..."

    mc zerado "Você ainda nem tá olhando... aliás, você lembra a última coisa que a gente conversou?"

    y "Claro... é... não lembro..."

    mc envergonhado "Não disse? Você acha que isso tá certo? Você tá tentando prestar atenção e tudo e não vivendo nada no fim."

    y "Só que..."

    scene y1_ape5 with Dissolve(1.0)

    pause

    y "Tá tudo acontecendo aqui. Meus fãs tão aqui, a comunidade que eu criei tá aqui. Meu trabalho, meu dinheiro..."

    y "Sem essa pequena coisinha eu perco tudo... tudo o que eu consegui com meu esforço..."

    y "Qualquer hora pode aparecer alguém e roubar todos eles de mim... por isso que eu preciso fazer isso."

    y "Você não entende nada disso... por isso que você não entende... nada disso. Eu preciso!"

    "Ela tem razão... eu realmente não entendo muito desse mundo. Muito menos que ela com certeza..."

    "Será que é melhor eu não me meter?"

    menu:
        "Eu vou me meter. Pelo menos falar o que eu acho.":


            mc desculpa "[y]... olha... solta isso um pouco. Só um segundinho."

            y "Você não ouviu o que eu d-"

            mc "Vai logo."

            y "Ai, que mala!"
        "Eu não quero me meter nisso. Foda-se as coisas dela.":


            "Ela tem razão. É melhor eu não me meter nisso. Eu não tenho nem vontade, nem tempo e nem sei exatamente o que ela tá passando."

            mc "Você tem razão. Você sabe melhor do que eu tudo isso. Só torço pra você curtir um pouco o lado bom também às vezes."

            y "..."

            scene y1_ape6 with Dissolve(1.0)

            pause

            y "Valeu. Desculpa, eu esqueci seu nome de novo..."

            mc "[mc]..."

            y "Isso. Eu sei que eu sou meio distraída, mas eu prometo que eu vou dar meu melhor pra ser uma boa celebridade."

            mc "Não é bem isso que eu tava falando... mas acho que você vai dar seu jeito."

            y "Vou, sim, [mc]."

            jump naru_e1_depois_ape

    scene y1_ape7 with Dissolve(1.0)

    pause

    y "Pronto. Feliz? Minha atenção é toda sua agora. É isso que você queria?"

    mc charmoso "Eu só quero que você pare pra respirar um pouco. Não quero que você desista do seu sonho."

    y "Parece que você quer. Parece meu pai falando pra sair do celular."

    y "Você é igualzinho ele! Não entende que não foi fácil chegar aqui! Acha que o que eu faço é brincadeira!"

    mc desculpa "Nã-"

    y "Claro que é! Acham que eu tô me divertindo aqui. Que eu sou 'v i c i a d a' em celular. Não entendem como funciona e falam MERDA!"

    mc "..."

    y "Eu sei que é isso... ninguém respeita o que eu faço..."

    mc preocupado "[y]..."

    y "Vai! Fala agora!"

    mc desculpa "Desculpa."

    y "Hm? 'Desculpa' pelo quê?"

    mc "Foi mal se pareceu que eu não reconheço seu trabalho. Depois de hoje, eu tenho certeza que o que você faz é trabalho."

    mc "Mais trabalho inclusive do que muita gente que levanta cedo e tem uma rotina 'normal'."

    scene y1_ape8 with Dissolve(1.0)

    pause

    y "Você tá falando sério?"

    mc "Tô. Eu acho que... foi você que não entendeu o que eu quero dizer. Posso explicar?"

    y "Pode..."

    mc "Eu acho que as pessoas não tão prontas pra entender seu trabalho. Pra elas, celular é diversão. Elas não entendem que isso pode ser profissão."

    mc "Você teve que lutar com isso por muito tempo, né? Ter que provar pras pessoas que o que você fazia era sério."

    y "Óbvio... ninguém entende."

    mc "É. Dá pra ver. Você lutou tanto à ponto de chegar nesse estado. Nessa ansiedade toda de que sua vida parece um castelo de cartas."

    mc "Qualquer coisa que acontecer pode derrubar tudo isso."

    y "..."

    mc "Será que... talvez não seja você que não vê que seu trabalho é trabalho?"

    y "Eu?"

    mc "Que 'trabalho certo' a pessoa fica o dia todo trabalhando, chega em casa, e tem que trabalhar? Que não tem folga?"

    mc "Que trabalho a pessoa não tem nenhuma segurança? Que precisa ficar com medo a todo momento, sem nenhuma garantia?"

    mc "É esse trabalho que você quer? Você acha isso certo? Essa é sua visão de trabalho de verdade?"

    y "Claro que não..."

    mc "Muitas pessoas passam por isso. Mas isso não tá certo. Todo mundo precisa descansar e precisa se sentir pelo menos um pouco seguro."

    mc "E você é sua chefe. Você que organiza tudo no seu negócio. E você mesma não tá te dando esse tempo. Você é uma chefe horrível."

    scene y1_ape9 with Dissolve(1.0)

    pause

    y "Não... eu só tô fazendo o que eu tenho que fazer."

    mc "Não. Você tá deixando seu medo tomar conta do seu negócio. Isso pode tá dando certo agora, mas logo isso vai ruir."

    mc "Você vai ficar doente, vai encher o saco e querer jogar tudo pra cima. O que você tanto ama vai virar um inferno."

    y "Não vai, não..."

    mc "Pode não parecer agora, mas esse medo, esse desespero, essa ansiedade vai acabar virando asco."

    mc "Claro que cada pessoa é uma, mas tem chance. Tem chance de uma hora isso que você construiu se virar contra você. E daí sim vai ser o fim do sonho."

    y "..."

    y "Por que... você tá falando isso? Por que tá sendo mau desse jeito comigo?"

    mc "Eu não tô sendo mau. Eu só..."

    "É verdade. Por que eu tô falando tudo isso pra ela? Será que eu me importo com a [y]? Eu nem conheço essa garota direito..."

    menu:
        "Eu quero te ajudar a ser uma profissional.":


            scene y1_ape6 with Dissolve(1.0)

            pause

            mc "Eu só... quero que você seja uma boa profissional. Eu sou um pouco mais velho que você. Acho que eu posso ajudar."

            y "Falando desse jeito você parece BEM mais velho do que eu."

            mc "Não exagere. Eu tava na faculdade até um tempo atrás."

            y "Mas você entrou na faculdade com quantos anos?"

            mc "Não interessa."

            y "Tá vendo?"
        "Eu me importo com você.":


            $ naru_amizade += 2

            scene y1_ape6 with Dissolve(1.0)

            pause

            mc "Eu só... me importo com você. Não sei. Acho que é isso. Eu queria que você fosse feliz, mais tranquila. Sei lá!"

            y "[mc]... você se importa com mulheres que você conheceu em uma tarde?"

            mc "Parece que sim... mas também não fique se achando muito. Não vou morrer se você tiver um ataque cardíaco aí."

            y "É mais fácil você ter, já que é velho desse jeito."

            mc "Eu? Velho? Da onde tu tirou isso?"

            y "Da... sei lá. Desse seu jeito de dar sermão! Quantos anos você tem?!"

            mc "Não interessa. Mais que você, mas não muito."

            y "Hmmm..."

    scene y1_ape10 with Dissolve(1.0)

    pause

    y "Mas por que você não quer me falar? Será que você tá querendo alguma coisa comigo?"

    mc "Você tá deduzindo demais já. E tá se achando também."

    y "Você não negou... negou?"

    mc "E-eu não tenho que te responder isso."

    y "Ficou nervoso..."

    mc "Para de ficar tentando me interpretar. A gente só tá conversando, só isso."

    $ renpy.notify("Naru está lembrando das suas ações...")

    y "Só uma conversa, né?"

    mc "Isso."

    if naru_amizade >= 12:

        pass
    else:


        y "Tem razão. E foi uma boa você ter vindo. Fazia tempo que eu não conversava assim."

        mc "Sério? Conversar no Insta não vale?"

        y "Vale... mas não é a mesma coisa. A gente é meio diferente, mas foi divertido ter alguém físico pra conver. Valeu."

        mc "Não é pra agradecer. Eu também curti."

        "Sinto que faltou alguma coisa... acho que eu poderia ter impressionado mais ela... mas beleza. Não é como se desse pra voltar no tempo."

        jump naru_e1_depois_ape

    y "Você... tá saindo com alguém?"

    mc "Eu? É..."

    y "É uma pergunta simples."

    if namorando:

        "Ixi... essa pergunta... a [y] parece uma mulher que não gosta de encrenca. Se eu falar que tô vendo alguém provavelmente já era."

        "Mas sei lá se eu quero alguma coisa com ela. Talvez eu queira só ver onde essa conversa vai dar..."

        "Eu devo tá com uma cara de tonto. O que eu falo?"

        menu:
            "Sim. Eu tô enrolado com alguém.":


                mc "Na verdade eu tô comprometido com alguém. Por quê?"

                y "Era só pra saber mesmo. Você é um cara bacana, [mc]."

                mc "Lembrou meu nome?"

                y "Pois é... tomara que sua namorada cuide bem de você."

                if nathan_namoro:

                    mc "É um namorado."

                    y "Ah! Que legal. Fico feliz por vocês."

                y "Valeu por ter sido tão bacana comigo. Eu nem lembrava seu nome, mas você foi um amigo e tanto, pelo menos hoje."

                y "Fazia tempo que eu não passava tempo desse jeito com alguém."

                mc "Só com os fãs?"

                y "É... é diferente falar com alguém de carne e osso, escutando a voz de verdade e não comprimida no mp3 do WhatsApp."

                mc "Haha... verdade."

                jump naru_e1_depois_ape
            "Não. Nada sério no momento.":


                mc "No momento nada sério. Tô aí de boa no mundo."
    else:


        "Eu não tô enrolado com ninguém agora. Não tenho porque mentir pra ela."

        mc "Não. Não tô vendo ninguém. Por quê?"

    $ naru_beijo1 = True

    y "Sei... então não tem problema se eu fizer isso aqui."

    mc "O quê?"

    scene black with dissolve

    y "Isso aqui."

    scene y1_ape11 with Dissolve(1.0)

    pause

    "{i}smack{/i}"

    mc "N-naru?!"

    y "Hmmm..."

    window hide

    pause

    scene y1_ape12 with Dissolve(1.0)

    pause

    mc "O q-que foi isso?"

    y "Um beijinho."

    mc "Eu sei, mas..."

    y "Hoje você foi muito legal comigo, [mc]."

    mc "Lembrou meu nome?"

    y "Pois é..."

    y "Eu achei que você merecia depois de hoje."

    mc "Eu fui tão legal que eu mereci um beijo de uma e-girl famosa assim?"

    y "Você nem deve saber o que é uma e-girl e fala desse jeito."

    mc "Depois de você falar assim eu tô meio inseguro..."

    y "É incrível como você tenta."

    mc "Eu sou incrível mesmo. Mas do que você tá falando?"

    y "Você faz uma mulher se sentir especial quando você tenta fazer parte do mundo dela desse jeito."

    y "Ouvindo problemas de uma garota que você nem conhece... e dando dicas ainda por cima."

    y "Mesmo não sabendo quase nada, isso não impediu você de se interessar pelo meu mundo."

    mc "Não foi nada. Eu só queria poder conversar com você sem parecer um idiota."

    y "Talvez não seja muito mesmo, mas foi o suficiente pra você ganhar um beijinho..."

    menu:
        "Só um? Não posso ganhar mais um?":


            mc "Eu acho que foi pouco. Não mereço mais um? Dessa vez por aqui... mais no meio do rosto..."

            y "Hmmm..."

            scene y1_ape13 with Dissolve(1.0)

            pause

            y "Não. Chegou perto... bem perto mesmo... mas pra ganhar um beijinho aí você precisa de mais pontos."
        "Foi uma boa recompensa.":


            mc "Até que foi uma boa recompensa. Não foi aquela nooooosssaaaaa que RECOMPENSA, mas tá bom."

            scene y1_ape13 with Dissolve(1.0)

            pause

            y "Se você soubesse quantas pessoas iriam querer ganhar essa sua recompensa..."

            mc "Mas eu sei, só que eu não sou igual essa criançada. Meu passe tá caro."

            y "O beijinho subiu na cabeça? Endoidou?"

            mc "Haha... tô me fazendo de difícil."

            y "Você é exigente... entendi..."

    y "Talvez uma próxima vez você consiga o score necessário pra passar de fase e ganhar uma recompensa maior."

    mc "Você tá achando que isso aqui é um jogo, é?"

    y "E não é?"

    mc "Haha... então quem sabe na próxima?"

    y "Na próxim... talvez."

    mc "Vou ter que seguir as regras do jogo fazer o quê."

    y "Isso. Se você não usar cheat, você chega lá. Agora, [mc]..."

    label naru_e1_depois_ape:

        y "Hoje foi um dia bem cansativo. Acho que eu vou dar uma deitada agora."

    mc "Sério?"

    y "Eu queria conversar mais, só que eu lembrei que o avião sai amanhã cedo. Eu tô quebradinha..."

    mc "Tudo bem. Acho que deu pra eu conhecer um pouco mais sua rotina."

    y "É quase sempre assim. Evento, hotel, smartphone, dormir... acordar e repetir."

    y "Ah! Tem uma coisa que eu queria fazer se você não achasse ruim."

    mc "O quê?"

    y "Tirar uma selfie com você."

    mc "Sério? Você sabe que a celebridade aqui é você, né?"

    y "Haha... eu sei. Mas, sei lá, eu queria guardar o dia de hoje. O que você acha?"

    menu:
        "Tudo bem. Bora tirar.":


            mc "Tudo bem, ué. Nada contra."

            y "Legal! Então vem aqui atrás de mim que você é mais alto."

            mc "Tá."

            scene y1_ape14 with Dissolve(1.0)

            pause

            y "Pronto?"

            mc "Mais bonito que isso não dá."

            y "Você precisa de umas aulas de selfie, mas tudo bem. É sua primeira vez."

            y "Agora prepara..."

            y "XIS!"

            show white with Dissolve(0.2)

            hide white with Dissolve(0.2)

            pause

            y "Ficou legal! Posso postar?"

            mc "Pode. Não vou negar um pouco de fama."
        "Melhor não, desculpa.":


            mc "Olha, [y], sem querer ser chato e tudo, mas eu não gosto de tirar foto. Não me sinto à vontade."

            y "Aaah..."

            mc "Mas não se preocupe que você não vai esquecer de mim nunca mais."

            y "Tudo bem..."

    y "Foi um dia interessante... acho que vou sentir saudades da capital."

    mc "Ela vai continuar aqui. Pode vir quando quiser."

    y "Você deixa?"

    mc "Minha convidada de honra."

    y "Obrigada. Mas eu acho que a gente não vai se ver mais. Não sei se o pessoal da Ganime Expo vai me chamar ano que vem."

    mc "Seria uma pena... mas não desista cedo assim. Tem muito chão ainda."

    mc "E mesmo que a gente não se veja mais, eu te achei uma garota muito interessante e gente boa. Bonita desse jeito também... você vai longe."

    mc "Daqui a pouco você vai ser entrevistada naqueles programas nacionais. Eu prometo que mando uma pergunta por telefone."

    y "Não é mais por telefone, velho... hoje em dia é pelas hashtags do Twitter. Tá entregando a idade..."

    mc "Foda-se. E veja se agora descansa."

    y "Tá."

    scene y1_ape3 with Dissolve(1.0)

    y "Eu só vou responder uns comentários e gravar um boa noite... mas depois eu vou dormir."

    mc zerado "Sei..."

    mc charmoso "Boa noite, [y]."

    if naru_beijo1:

        mc "E valeu pelo presente. Ainda tô sentindo o quentinho."

        y "De nada. Mas não fica sem lavar o rosto por causa disso."

        mc "Exagerada."

    mc "Tchau."

    y "Kisu... é... como é seu nome mesmo?"

    mc zerado "Mano..."

    y "É [mc]! Tô brincando! Kisu, [mc], seu fofo!"

    mc envergonhado "..."

    scene black with Dissolve(1.0)

    label naru_e1_final:

        "Caraca... que dia."

    if naru_ape:

        scene mc onibus_noite with Dissolve(1.0)

        "Foi muito bacana esse tempo no apê dela. A [y] tem bastante energia. É muito bom tá na flor da idade, mano."

        "E aquela roupinha que ela tava usando... cara... eu não conseguia tirar os olhos dela."

        "Mas é bom ela maneirar no trabalho ou vai acabar infartando com 20 anos, certeza."

        "Espero que eu tenha conseguido ajudar ela de alguma forma com o que eu falei. Queria que ela se desse bem. Ela é uma boa garota, merece."

        if naru_beijo1:

            "E aquele beijo..."

            "Foi só uma bitoquinha na bochecha, né... mas mesmo assim foi bom demais. Deu pra ver que ela gostou de mim."

            "Quem sabe a gente se reencontra um dia. Eu ia gostar bastante."

            "Uma garota sexy dessas... novinha assim e famosa ainda por cima. É pra deixar qualquer homem doido."
        else:


            "Não rolou nada entre a gente, mas paciência. Nem sei se ia ser uma boa mesmo."

            "Pode até ser que a gente se veja um dia... até que eu ia gostar."

            "Vamos ver o que rola mais pra frente."
    else:


        "Eu resolvi não ir no apê da [y], mas foi melhor. Eu não queria nada com ela e não corro risco de levar esporro da [w]."

        "Mas me chamar pro apê assim... será que ela queria alguma coisa comigo? Talvez eu tenha perdido uma chance..."

        "Cala a boca, [mc]. Para de pensar coisa nada a ver."

    "Uma pena que eu não consegui uma pauta... todo esse lance de acompanhar o evento era pra isso e acabou não virando."

    "Será que eu fiz alguma coisa de errado?"

    "Agora eu tô pensando... será que eu vou encontrar ela de novo?"

    "A [y] não é daqui e ela não sabe se eles vão chamar ela pro evento ano que vem... então talvez a gente nunca mais se veja."

    "Eu gostei bastante dela. Ela tinha uma energia bacana e com certeza era muito bonita, além de tá mega sexy com aquela roupa."

    "Acho que eu vou seguir os perfis dela... quem sabe um dia a gente se tromba de novo..."

    "Mesmo que a gente não se veja mais, valeu à pena. Torço pra que ela tenha sucesso aí na carreira e cada vez mais seguidores."

    if naru_beijo1:

        "Quanto mais famosa ela for... mais o beijo dela vai valer."

        "Morram de inveja, idiotas! Vocês ficam babando ovo, mas quem ganhou o beijinho foi eu!"

        "HAH!"

    "Agora bora dormir que amanhã tenho que ir na redação conversar com a [w]. Bora ver o que ela vai inventar."



    $ v39_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v39_fim","final","local")

    scene black with Dissolve(3.0)

    $ tempo = 4

    call checa_final from _call_checa_final_19

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
