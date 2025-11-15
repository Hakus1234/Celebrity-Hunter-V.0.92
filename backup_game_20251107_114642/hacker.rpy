label nona_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("h1_save", extra_info="h1_save")

    $ estou_na_cidade = False

    $ nona_e1 = "evento"

    "Eu já tô um bom tempo aqui na ilha."

    scene ape_chuveiro with Dissolve(1.0)

    "Quando tudo começou... eu tinha me formado e começado minha carreira como jornalista na revista. Um trabalho que minha mãe arranjou."

    "Só que quando entrei era uma bela merda. Não conseguia falar com ninguém, não descobri porra nenhuma pra poder passar pro chefe."

    "E daí quando eu conheci a [c] tudo deu uma super reviravolta."

    "Tipo... Até minha relação na revista mudou."

    scene ape_tv with Dissolve(1.0)

    "Hoje eu falo com a [j], com a [w] e até o Ronaldo fala comigo de vez em quando."

    "E não só aqui. Eu conheci tanta gente na ilha e no continente também. Tantas pessoas que eu acabei trocando ideia..."

    "É estranho como esse lugar é diferente, sei lá. Eu sinto que tem alguma coisa acontecendo aqui na ilha."

    "O jeito que a [j] fala e até o apresentador da Faux News também."

    "E é o tipo de coisa que pode me ferrar muito. Mexer com as pessoas erradas..."

    if stifler_e1 != "nada":

        "O [us] disse que eu tenho um tipo de 'poder', de influência."

        "Será que trabalhar na revista e poder tornar as coisas públicas é assim tão perigoso pra certas pessoas?"

    "Eu queria ter uma vida tranquila e viver nesse mundo especial que é essa ilha paradisíaca."

    "Só que não importa o que eu faço, eu sempre conheço pessoas que tão envolvidos em alguma coisa estranha..."

    "Acho que eu vo-"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    mc "Hm? Tem alguém ligando."

    mc "Número não identificado?"

    scene ape_celular with Dissolve(1.0)

    mc "Alou?"

    "???" "Boa tarde, senhor [mcc]?"

    mc "Quem fala?"

    $ gi_nome = "Gevanni"

    gi "Meu nome é [gi], sou diretor financeiro da agência do Novo Banco Central aqui na ilha."

    if n3_gravou:

        gi "Se não me engano, nos vimos na redação da sua revista certo dia junto da [j]."

        mc "Ah! Eu me lembro!"

        "Aquele cara todo chique de terno."

    gi "Desculpe ligar assim, mas é um assunto urgente."

    mc "O que aconteceu?"

    gi "Gostaria de falar com o senhor aqui em meu escritório se for possível, mas, apenas para adiantar, é sobre um dinheiro que o senhor recebeu."

    mc "Eu recebi?"

    gi "Você tem o aplicativo do seu banco?"

    mc "Tenho."

    gi "Por favor, veja um extrato ou seu saldo atual. Você vai notar que existe um novo valor em sua conta."

    mc "Quer que eu veja agora?"

    gi "Sim. Eu espero."

    "Deixa eu ver aqui."

    python:
        if renpy.android:
            persistent.coins = PythonSDLActivity.pegaMoedas(0)
            cash = PythonSDLActivity.pegaCash()
            mc_fisico = PythonSDLActivity.pegaFpontos()
            bao_pontos = PythonSDLActivity.pegaBao()
            
            if userlogado:
                useremail = PythonSDLActivity.pegaEmail()

    $ novo_cash = cash + 300000

    show screen celular_mc_copia

    pause

    mc "{i}PFFFFFFFFFFFUUUUUU{/i}"

    "I-I-I-Isso é sério?! [novo_cash]!?"

    "Eu nem sei que número é esse!"

    mc "A-acho que eu entendi... realmente tem um dinheiro na minha conta e talz."

    gi "Exatamente. Gostaria de conversar com o senhor sobre esse valor, mas não por telefone. Seria possível o senhor passar aqui na agência hoje?"

    mc "Onde fica?"

    gi "Aqui mesmo na ilha. O senhor está na ilha, não está?"

    mc "Sim."

    gi "Perfeito. Fica logo ao lado da praça."

    "Bem aqui do lado... É um pulo até lá."

    mc "Ok. Eu passo aí hoje, [gi]."

    gi "Muito obrigado, senhor [mc]. Até breve."

    "{i}Tu tu tu...{/i}"

    "MANO! Como assim?! Que dinheiro é esse?! Deixa eu ver de novo..."

    show screen celular_mc_copia

    pause

    "Cara! Tudo isso! Minha vida vai mudar completamente!"

    if compra_casa_evento and not casa_comprada:

        "Eu vou ter grana pra pagar os papéis pra Gina passar a casa pro meu nome!"

    "Eu nunca mais vou precisar trabalhar no bar ou se pá posso até mudar de emprego!"

    "Velho, isso é muito dinheiro! Eu tô resolvido por um bom tempo!"

    "Mas como tudo isso veio parar na minha conta?"

    "Com certeza aconteceu alguma coisa errada. Tipo... provavelmente alguém errou a conta ou alguma coisa assim."

    "Mas agora que a grana tá comigo, acho que já era. A grana é minha e pronto. Ninguém pode querer o dinheiro de volta."

    "Merda... o que eu faço?"

    menu:
        "Foda-se o que aconteceu. Agora a grana é minha.":


            $ h1_dinheiro = True

            mc "Não importa como esse dinheiro veio parar comigo, agora ele é meu."

            "Eu posso fazer muita coisa com isso. Minha vida vai mudar muito."

            "Não importa o que aconteça, eu não devolvo de jeito nenhum."
        "A grana não é minha, tenho que achar de quem é.":


            mc "Não adianta eu ficar me iludindo. Esse dinheiro não é meu..."

            "Tenho que descobrir de quem é a grana e ver porque isso veio parar na minha conta."

    "E se essa merda for ilegal? Deixa eu ver quem mandou o dinheiro..."

    "Ué... não tem quem fez a transferência pra minha conta."

    "Como que pode? Uma conta {b}não identificada{/b}? É a primeira vez que eu vejo isso."

    "Não adianta ficar pensando muito também até chegar no banco."

    "Espero que esse [gi] realmente me ajude e não esteja só de olho na grana."

    "Acho que vou dar um pulo lá agora."

    scene black with dissolve

    scene ilha parque2 with Dissolve(1.0)

    "Ele falou que fica do lado da praça. Acho que tô vendo."

    scene black with dissolve

    "Só pode ser aqui."

    scene banco_geral with Dissolve(1.0)

    pause

    "Então essa é a agência do Banco Central... e aqui fica o diretor financeiro do banco."

    "Esse cara parece ter um cargo bem importante. Por que será que ele fica aqui na ilha e não, sei lá... na sede, não sei."

    "{i}Blá blá blá blá{/i}"

    "Tem várias pessoas aqui. Mas eu nunca tinha reparado nesse lugar, mesmo ficando do lado da revista."

    "O que será que rola aqui? E como eu vou fa-"

    "???" "Senhor [mcc]?"

    mc desconfiado "Oi?"

    "???" "Bom dia, senhor."

    mc surpreso "!"

    scene hacker_banco with Dissolve(1.0)

    pause

    "Q-que é isso?!"

    h "Tudo bem, senhor?"

    menu:
        "Uou... mais do que bem...":


            mc tarado "Uou... depois que você chegou... tá tudo mais do que bem."

            h "Senhor [mc]... não me deixe sem jeito."

            mc charmoso "Desculpa, mas é que você realmente é muito bonita."

            h "Obrigada. O senhor é um cavalheiro."

            mc charmoso "..."
        "S-sim...":


            $ hacker_amizade += 1

            mc envergonhado "S-sim... Tudo legal."

            h "O que foi? Algum problema?"

            mc "Não, nada... é que você me chamou pelo nome, daí meio que me assustei."

            h "Ah, sim. Desculpa."

            mc normal "Relaxa."
        "Quem é você?":


            $ hacker_amizade += 2

            mc desconfiado "Ah. Oi... Quem é você?"

            h "Desculpa chegar assim, não queria assustar."

            mc "Tudo bem..."

    $ h_nome = "Carla"

    h "Meu nome é [h] e eu sou assistente do senhor [gi]. Ele me pediu para que eu esperasse você chegar."

    mc normal "Ah!"

    "Caraca... ele deixou essa mina me esperando?"

    "Pensando bem... olha pra roupa dessa garota. Será que ela trabalha aqui assim?"

    "E não é só a roupa. A tatuagem dela... bem diferente. Não é um lance que você espera de uma pessoa que trabalha no banco."

    "O que será que rola aqui?"

    h "..nhor [mc]? Oi?"

    mc surpreso "Oi! Desculpa!"

    h "O senhor parecia meio absorto em pensamentos. Algum problema?"

    menu:
        "Ah, não foi nada.":


            mc envergonhado "Ah... não foi nada. Só tava pensando aqui que eu nunca tinha vindo nessa agência."

            h "Entendo. O Novo Banco Central trata de questões monetárias diferentes de um banco comum."

            h "A maioria das pessoas nunca precisarão vir aqui."

            mc desconfiado "Hmm..."
        "Essa tatuagem sua...":


            $ hacker_amizade += 2

            mc normal "Essa sua tatuagem... me chamou bastante a atenção."

            h "Não é pra menos. Eu preferiria cobrir meus braços, mas eu uso a roupa que o senhor [gi] me pede para usar."

            mc "Entendi. E de onde veio essa tatuagem? Sem querer ser intromedido."

            h "Ah... nada em especial. Eu só gostei da imagem."

            mc envergonhado "É uma tatuagem que cobre bastante..."

            h "Eu sei. Mas eu gosto dela."

            mc normal "É bem legal mesmo."

            h "Obrigada."
        "Com todo o respeito, essa sua roupa...":


            $ hacker_amizade += 1

            mc envergonhado "Desculpa por ser intrometido, mas essa é a roupa que você trabalha?"

            h "Pior que sim..."

            mc "É qu-"

            h "Ela mostra um pouco demais, né?"

            mc "Um pouco... não que tenha problema!"

            h "Não precisa ficar assim, senhor. Eu entendo. Mas dificilmente as pessoas me veem usando ela."

            mc desconfiado "Como assim?"

            h "Eu trabalho somente para o senhor [gi], como secretária pessoal. Por isso eu dificlmente desço aqui falar com o público."

            mc normal "Entendi."

            h "Eu queria usar uma roupa mais normal, mas ele insistiu que eu usasse essa aqui..."

            mc envergonhado "..."

            h "Ah! Mas por favor não pense que ele é um chefe ruim. Ele nunca tentou nada desse tipo."

            mc "Não pensei em nada, não."

            "Mentiroso..."

            h "Desculpa, eu só queria deixar claro, porque pode parecer alguma coisa que não é. Ele é bem respeitoso, só faz umas brincadeiras..."

    mc desconfiado "Bom... A gente vai falar com ele?"

    h "Sim. Ele me falou do seu caso. Na verdade, fui eu que notei a transação."

    mc "Você?"

    scene hacker_banco_close with Dissolve(1.0)

    h "Eu sou responsável por algumas tarefas, como monitoramento. Na verdade, não é bem minha função, mas eu gosto de fazer."

    mc desconfiado "Hmm..."

    h "Minha responsabilidade é cuidar do senhor [gi], mas eu acabo fazendo outras coisas pois quero que ele veja minha qualidade."

    h "Eu quero um dia atingir um lugar grande aqui no banco. Seria um sonho realizado."

    menu:
        "É bacana você ter esse sonho.":


            $ h1_sonho = True

            mc charmoso "É legal você ter esse sonho."

            h "O senhor acha?"

            mc "Acho bacana ter um sonho profissional."

            mc envergonhado "Eu mesmo não sei direito o que eu quero da vida."

            h "Logo o senhor vai encontrar."

            mc "Tomara..."
        "Trabalhar em um banco é seu sonho?":


            $ hacker_amizade += 1

            mc desconfiado "Seu sonho é trabalhar no banco?"

            h "O que foi? O senhor não concorda?"

            mc envergonhado "N-não é isso! Mas sei lá, normalmente as pessoas sonham em ser atriz ou jogador de futebol."

            h "Nós já somos adultos, né? Esses sonhos são pra crianças."

            mc "Tem razão..."

    h "Mas então, sobre seu caso. Eu tava observando as transações, e nosso sistema mostrou uma transferência de grande valor."

    mc desconfiado "Foi assim que você viu?"

    h "É. O Novo Banco Central tem acesso a todas as transferências realizadas em bancos públicos ou privados praticamente em tempo real."

    h "Quando o senhor recebeu o dinheiro, logo apareceu no sistema, e como eu estava de olho..."

    mc "Entendi... e o que pode acontecer agora? Você sabe o que o [gi] quer falar comigo?"

    h "Hmm... olha... provavelmente ele vai querer saber quem transferiu o dinheiro e porquê."

    mc envergonhado "E se eu não souber?"

    h "Como assim?"

    mc "Só perguntando..."

    h "Olha, senhor [mc]. Eu nem deveria falar isso para você assim. Mas eu estaria um pouco preocupada se fosse você."

    mc preocupado "Como é?"

    h "Não quero te assustar, mas receber uma quantia dessa sem motivo levanta suspeitas."

    h "Se você não conseguir explicar para o senhor [gi] o que está acontecendo, provavelmente ele vai pedir uma investigação."

    mc "Caraca... isso parece sério."

    h "O senhor pode, por favor, entrar no aplicativo do seu banco e me emprestar o celular para eu te mostrar uma coisa?"

    mc "Só um segundo... aqui."

    h "Obrigada. Vou te mostrar uma área especial no seu aplicativo que a maioria dos clientes não conhece. Rapidinho."

    "..."

    h "Veja."

    scene hacker_banco with Dissolve(1.0)

    mc desconfiado "O que é esse número?"

    h "Essa tela mostra informações detalhadas sobre as contas envolvidas em uma transação. Só que no caso dessa transferência, não existe informações."

    mc desconfiado "Acho que entendi..."

    h "Mas o senhor estava falando só por curiosidade, né? Você sabe como recebeu o dinheiro."

    menu:
        "...":


            $ hacker_amizade += 1

            mc envergonhado "..."

            h "Hmm..."
        "Claro...":


            mc envergonhado "Haha... claro."

            h "Eu sabia."

            mc "Heh..."

    h "Vamos lá então?"

    mc serio "Vamos."

    scene black with Dissolve(1.0)

    scene banco_vip with Dissolve(1.0)

    mc desconfiado "Essa parte aqui já é bem diferente."

    h "Verdade. Aqui fica o pessoal do administrativo. Não tem atendimento ao público aqui."

    mc "Mas então por que eu-"

    h "Seu caso é bem especial, senhor [mc]."

    mc envergonhado "Entendi..."

    "A coisa tá parecendo séria. O que será que eu fiz que eu recebi esse dinheiro?"

    "Das pessoas que eu conheço... quem pode ter sido?"

    "Acho que a [c] é a pessoa mais rica que eu conheço... Mas ela não ia me dar dinheiro assim sem avisar."

    "Quem mais seria? Tipo... espero que não seja dinheiro roubado, desviado, sei lá."

    h "Vamos subir, senhor [mc]?"

    mc surpreso "C-claro! Vamos."

    scene black with Dissolve(1.0)

    "..."

    h "Senhor [gi], estamos aqui."

    gi "Por favor entrem."

    mc normal "Com licença."

    scene gevanni_hacker_mesa with Dissolve(1.0)

    pause

    gi "Olá, senhor [mc]."

    mc envergonhado "O-olá."

    if n3_gravou:

        gi "Desde que a gente se encontrou na redação aquele dia, eu sabia que a gente se veria de novo."

        mc "Verdade?"

        gi "Sua aliança com a [j] vai te trazer muitas coisas boas. Essa é uma dica de quem está com ela há muitos anos."

        mc "Entendo... obrigado. Mas ela me dá um pouco de medo haha..."

        gi "Relaxe. Eu e ela sabemos diferenciar aliados de inimigos. Você só precisa estar do lado certo."
    else:


        gi "Não precisa ter vergonha. Logo você vai ver que eu sou um cara muito acessível."

        gi "Inclusive, você devia sair mais com a [j]. Você trabalha com ela na revista, certo?"

        mc normal "Sim. Mas ela me dá um pouco de medo haha..."

        gi "Relaxe. Eu e ela sabemos diferenciar aliados de inimigos. Você só precisa estar do lado certo."

    mc envergonhado "Ok..."

    "Esse homem me passa segurança e uma ameaça ao mesmo tempo. Com certeza ele não tá brincando aqui."

    gi "Então você já conheceu a [h]."

    mc normal "Sim. Ela foi me esperar lá na entrada."

    gi "É uma boa garota. Tem grande potencial."

    h "Obrigada, senhor [gi]. Você sabe o quanto eu quero uma carreira aqui no banco."

    gi "E você vai conseguir. Pode ter certeza. Contanto que você continue seguindo todas as ordens que eu te dou, igual sempre."

    h "É o que eu pretendo, senhor..."

    gi "Ela é ou não uma bela assistente, [mc]?"

    mc envergonhado "É..."

    menu:
        "Uma BELA assistente, com certeza.":


            mc tarado "Só um cego pra não ver. Com certeza, uma BELA assistente."

            gi "Ah, vejo que você é um homem de cultura também."

            h "Eu tô ouvindo vocês, garotos..."

            gi "Só estamos elogiando, [h]."

            h "Sei..."
        "Ela parece saber bastante sobre o banco.":


            $ hacker_amizade += 1

            mc normal "Ela me explicou bastante e parece bem interessada no banco. Tenho certeza que vai ser uma boa profissional."

            h "O-obrigada, senhor [mc]..."

            gi "Não era bem isso que eu queria dizer..."

            mc desconfiado "Hm?"

            h "Senhor [gi]... eu entendi muito bem..."
        "Não faço ideia.":


            $ hacker_amizade += 2

            mc zerado "Não conheço ela. Não faço a mínima ideia."

            gi "Hahaha... tenha calma, senhor [mc]. Era só uma brincadeira. Você precisa relaxar um pouco."

            mc envergonhado "É que eu tô meio preocupado com a situação."

            gi "Olha pra [h]. É uma visão que vai tirar os problemas da sua cabeça."

            h "Senhor [gi]..."

    mc envergonhado "Haha..."

    scene gevanni_hacker_mesa_close with Dissolve(1.0)

    gi "Eu sabia que ela ia se dar bem como assistente quando ela aceitou o uniforme que eu comprei exclusivamente pra ela."

    h "Podia ser um pouco maior, né?"

    gi "Mas onde estaria a graça nisso? Eu quero diferenciar você das outras."

    "Será que esse cara sabe que isso é assédio?"

    h "Bom... você é meu chefe. O que eu posso fazer?"

    gi "Tá vendo, [mc]? Quando você for contratar alguém, procure uma pessoa com essa mentalidade."

    mc envergonhado "Sei..."

    gi "E não tem problema nenhum, porque ela praticamente fica só na minha sala. Ninguém vai ver ela assim, certo, [h]?"

    h "Sim. Só o senhor que me vê assim."

    gi "É o melhor."

    h "Mas agora que o senhor [mc] conseguiu um expressivo valor bancário, ele poderia vir para o banco."

    gi "Hmm... acho bom falarmos sobre isso. Você pode nos dar licença, [h]?"

    h "Eu gostaria de ouvir a conversa, se vocês não se importarem."

    "Eu não sei o que esse dinheiro quer dizer. Será que é uma boa eu incluir ela na conversa? Pode complicar minha vida depois."

    "Só que foi ela mesma que achou. Ela já sabe. Então talvez não tenha problema..."

    menu:
        "Acho que é melhor falarmos só nós dois.":


            mc serio "Não é por nada, [h], mas como parece um negócio sério, eu prefiro que a gente fale só entre nós."

            h "Ok... vou dar licença para os senhores então."

            gi "Obrigado, [h]."

            scene gevanni_mesa1 with Dissolve(1.0)

            gi "Também acho melhor que ela não ouça, mas não queria ter que falar pra ela. Obrigado, [mc]."

            mc serio "Até eu saber direitinho o que tá acontecendo, quanto menos pessoas envolvidas melhor."

            gi "Muito sensato de sua parte."
        "Por mim ela pode ficar.":


            $ hacker_amizade += 1

            mc normal "Por mim tudo bem. Pode ficar e ouvir."

            h "Eu sei a gravidade do assunto. Podem confiar em mim. Eu só quero ganhar experiência."

            gi "[h]..."

            h "Senhor?"

            gi "Eu prefiro falar a sós com o [mc]. Você sabe que eu confio em você, mas eu prefiro."

            h "Mas, sen-"

            gi "Você ouviu o que eu disse?"

            h "... Ouvi. Com licença..."

            scene gevanni_mesa1 with Dissolve(1.0)

            gi "Eita... o que deu nessa garota?"

            mc normal "Ela leva o banco bem à sério mesmo, hein?"

            gi "Até demais às vezes... ela não pode esquecer o lugar dela."

    gi "Bem... pra falar a verdade eu esperava ver você um pouco mais... efusivo, entusiasmado, depois de receber o dinheiro que recebeu."

    if h1_dinheiro:

        "Eu decidi que essa grana é minha, não importa o que tenha acontecido."

        mc serio "O dinheiro tá na minha conta então é meu, mas antes quero saber porque você me chamou."

        gi "Entendo."
    else:


        "Eu decidi que não vou contar com o dinheiro antes da hora."

        mc serio "É um grande valor. Até entender direitinho o que tá rolando, não vou fazer nada."

        gi "Um sujeito precavido. É a melhor opção mesmo."

    gi "A última coisa que eu quero é te assustar sem necessidade. Esta é uma conversa informal, e pode ficar tranquilo que nada irá acontecer ainda."

    mc desconfiado "Ainda?"

    gi "Tenha calma, [mc]! Haha... é importante você ter noção de que estamos falando de uma grande quantia. 300 mil não é uma transação comum."

    mc desculpa "Imagino..."

    gi "Vamos começar pelo começo."

    gi "Eu te chamei aqui pois essa transação de um detalhe incomum. A {b}transferência tem origem desconhecida{/b}."

    mc desconfiado "O que isso quer dizer?"

    gi "Toda vez que uma transação bancária é efetuada, ela tem origem em uma conta e é destinada a outra conta. Ou seja, uma entidade repassando um valor a outra."

    gi "Entretanto, neste caso, a conta de origem não pode ser identificada. Isso é algo extremamente raro."

    gi "O único órgão que poderia fazer algo assim seria o NBC, mas nós não fazemos isso, só em casos extremos. Isso quer dizer que tem algo de errado."

    menu:
        "Você acha que é um dinheiro ilegal?":


            mc preocupado "Você quer dizer que é dinheiro ilegal?"

            gi "Não exatamente. Normalmente, dinheiro ilegal deve ser lavado por sucessivas transferências. Muitos usam paraísos fiscais."

            gi "Outro caminho do dinheiro ilegal é nunca permitir que ele chegue ao banco. Ou seja, ele permanece em espécie e é usado devagar."

            gi "Em princípio, este caso foge à regra."

            mc "Acho que eu entendi."
        "E o que isso tem a ver comigo?":


            mc preocupado "Entendi. Mas o que isso significa pra mim?"

            gi "Primeiro que todo dinheiro precisa ser rastreado, de uma forma ou de outra. Se você recebeu esse valor, precisamos saber sobre isso."

            gi "O banco tem prerrogativa para isso. E nós do Novo Banco Central podemos requerer intervenção tanto em bancos públicos como privados."

            gi "Nós não queremos ferrar você ou qualquer coisa assim. Só precisamos ter certeza do que tá acontecendo."

            gi "Se você colaborar com a gente, nada de ruim vai acontecer."

            mc desculpa "Certo."

    gi "Você vai ver como é simples. Primeiro passo, por favor me fale quem fez a transferência pra você."

    "Só tem uma coisa que posso responder... não adianta inventar moda agora."

    mc desculpa "Não sei."

    gi "Como?"

    mc "É sério. Eu sei tanto quanto vocês."

    scene gevanni_mesa2 with Dissolve(1.0)

    pause

    gi "[mc]... como eu disse, não quero complicar sua situação. Mas você precisa me ajudar a te ajudar."

    gi "Se você complicar minha vida, eu vou complicar a sua. Nós somos aliados aqui, ok?"

    mc desculpa "Eu tô falando sério com você. Não sei de onde veio esse dinheiro."

    if h1_dinheiro:

        mc serio "Só sei que agora esse dinheiro é meu."
    else:


        mc "Por isso mesmo que eu tô falando que tô tomando todo o cuidado. Nada disso é meu por enquanto."

    gi "Se o dinheiro tá na sua conta, é seu. A não ser que seja provado judicialmente ser roubado ou fruto de ilegalidades."

    gi "A melhor forma de garantir que você vai continuar tendo sua vida normal aqui na ilha é colaborar."

    gi "É bom você tomar {b}cuidado com o que vai responder{/b}."

    gi "Você tem alguma ideia quem pode ter transferido esse dinheiro?"

    "Alguém que eu conheço que pode ter transferido esse dinheiro..."

    "A [c] tem dinheiro. O chefe tem dinheiro. Talvez o cara da Faux News? A [j]?"

    if priscila_namoro:

        "Eu tô namorando com a [c]... talvez foi uma surpresa... Impossível. Ninguém faria isso desse jeito."

    "Só que... é dinheiro demais. Por que qualquer um deles faria isso?"

    gi "E então, [mc]?"

    mc serio "Hmmm..."

    menu:
        "Talvez o chefe da revista.":


            $ h1_responsavel = "chefe"

            mc "Talvez o chefe da minha revista. Ele é o editor chefe e é uma das poucas pessoas que eu conheço que deve ter isso de grana."

            gi "Sei... eu conheço ele. A [j] já me falou do sujeito."
        "Talvez a modelo [cc].":


            $ h1_responsavel = "priscila"

            mc "Eu conheço a [cc], a modelo teen. Ela teria dinheiro pra transferir isso, mas não sei porque ela faria isso."

            gi "Nenhuma razão?"

            if priscila_namoro:

                "Melhor eu não falar do nosso namoro."

            mc "Nada que eu poderia te dizer."

            gi "Certo."
        "Talvez o Luca Alighieri.":


            $ h1_responsavel = "luca"

            mc "Eu conversei com o tal do Luca Alighieri da Faux News. Ele me fez uma pro-"

            gi "Entendi entendi."
        "Talvez a própria [j].":


            $ h1_responsavel = "cassia"

            mc "Não acho que a [j] daria o dinheiro dela pra mim, mas talvez ela te-"

            gi "Com certeza não."

            mc "S-se você diz."
        "Não faço a mínima ideia":


            $ hacker_amizade += 2

            $ h1_responsavel = "ninguem"

            mc "Eu realmente não sei. Não posso falar um nome aqui assim."

            gi "Preciso que você faça um esforço, [mc]."

            mc desculpa "Desculpa, mas eu não tenho como falar. Eu imaginei que vocês iam me falar."

            gi "Se eu pudesse, não teria te chamado, concorda?"

            mc "..."

    gi "Isso é muito pouco."

    mc desculpa "Eu queria poder ajudar mais. Eu quero mesmo."

    scene gevanni_mesa3 with Dissolve(1.0)

    gi "Olha, [mc]. Sua situação não tá fácil. Eu vou pedir pra você ir agora, mas se não descobrirmos nada, a coisa vai complicar."

    mc preocupado "Pra mim? Complicar como?"

    gi "Eu vou ter que pedir uma investigação legal do caso. Vou passar para as autoridades e daí não vai ser mais comigo que você vai conversar."

    gi "Pense no que {b}você fez no passado{/b}. Alguma coisa levou você a receber esse dinheiro."

    gi "Não é todo mundo que recebe uma grana dessas assim do nada. Você tem que ter feito alguma coisa."

    "O que será que eu fiz? Eu preciso pensar..."

    gi "Esta ilha não é uma zona. Tudo aqui foi construído com um propósito. Não foi fácil chegarmos onde chegamos, entende?"

    gi "Não podemos deixar que pessoas de fora façam alvoroço neste lugar. Se tem dinheiro errado aqui, temos que descobrir."

    menu:
        "Isso não me importa. Eu não tenho nada com isso.":


            $ hacker_amizade += 1

            mc desculpa "O que rola aqui na ilha não me interessa. Eu tenho minhas próprias coisas."

            gi "Seria inteligente de sua parte se aliar às pessoas certas, [mc]. É a dica que eu te dou."

            mc desconfiado "..."
        "Eu juro que não fiz nada de errado. Pode confiar em mim.":


            mc preocupado "Eu tô falando sério, [gi]. Eu não fiz nada. Eu quero que você confie em mim."

            gi "É o que eu quero fazer, [mc]. É o que eu quero..."

    gi "Existem vários tipos de pessoas, [mc]. E algumas realmente me irritam. Elas querem mudar as coisas."

    mc desconfiado "Mudar o quê?"

    gi "Esses desgraçados não têm respeito pelo que nós criamos aqui. A capital não nasceu do dia pra noite. Muito menos esta ilha."

    scene gevanni_mesa1 with Dissolve(1.0)

    gi "Algumas pessoas deram suas vidas por isso aqui. Esse lugar que você tá pisando agora mesmo. Este é um símbolo."

    "O que será que ele tá falando? Eu só consigo pensar no que eu vou comprar com essa grana."

    "Ou será que é melhor eu não fazer nada por enquanto?"

    gi "Mas algumas pessoas insistem em alterar a ordem das coisas. Insistem em desfazer o que nós fizemos."

    gi "Esses porcos que vivem de migalhas que jogamos. Eles acham que podem algo contra nós, mas estão enganados."

    gi "É por isso que você precisa escolher bem seus aliados, [mc]. Você vai querer ficar do lado vencedor."

    $ nona_e1 = "continua"

    $ renpy.vibrate(1)

    "Opa! Mensagem!"

    "Deixa eu dar uma olhada rápida enquanto ele fala."

    show screen celular_hacker

    pause

    mc desconfiado "Hm?"

    gi "... então... Algum problema, [mc]?"

    mc "Só um segundo, deixa eu ver uma coisa aqui."

    show screen celular_mc

    pause

    mc surpreso "!"

    gi "O que foi?"

    mc desconfiado "O dinheiro desapareceu da minha conta."

    gi "Isso é sério?"

    mc "Sim, não tá mais aparecendo no saldo da conta. Acabei de acessar o app do banco."

    gi "E no extrato. O que tá falando?"

    mc "Nada. Não existe mais a transferência."

    gi "Você pode esperar lá em baixo por favor? Eu vou falar com a [h] e assim que eu confirmar algumas coisas ela te avisa o que deu."

    mc preocupado "O-ok."

    scene black with Dissolve(1.0)

    scene banco_geral with Dissolve(1.0)

    "..."

    "O que tá acontecendo? Cadê a grana?"

    h "Senhor [mc]?"

    mc preocupado "O-oi."

    scene hacker_banco with Dissolve(1.0)

    h "Eu tenho boas notícias para o senhor."

    mc normal "Sério? O que foi?"

    h "Aparentemente a transferência que o senhor recebeu foi apenas um erro do banco."

    mc preocupado "Como assim erro do banco? Eu perdi o dinheiro?!"

    h "Na verdade o senhor nunca recebeu o dinheiro. Deve ter sido apenas um erro de exibição."

    mc "Afe..."

    h "Eu sinto muito, mas pelo menos o senhor sabe que está livre de qualquer problema."

    if h1_dinheiro:

        mc bravo "Isso é sério! Eu já tava contando com essa grana, garota! Como assim sumiu?!"

        scene hacker_banco_close with Dissolve(1.0)

        h "Me desculpe, senhor. Mas é como as coisas são."

        mc irritado "Eram 300 mil, você entende?!"

        h "O senhor está passando vergonha... era tudo o que eu podia te falar. Tenha uma boa tarde."

        mc "EI!"
    else:


        $ hacker_amizade += 1

        mc concentrando "{i}Pfff{/i}..."

        mc envergonhado "Pra falar a verdade, desde o começo eu fiquei em alerta. Eu sabia que tava estranho demais."

        h "Isso é bom, senhor [mc]. Eu achei que você não ia levar assim na boa."

        mc desconfiado "Hm?"

        h "Com isso resolvido, você não tem mais pendências no NBC. Tenha uma boa tarde."

        mc concentrando "Boa tarde."

    scene banco_geral with Dissolve(1.0)

    mc desculpa "Então eu realmente perdi tudo... Que merda..."

    "A [h] sumiu, o [gi] nem se despediu nem nada..."

    "Acho que no fundo eles não tavam nem aí pra mim. O que eles queriam era outra coisa..."

    "Agora essa coisa desapareceu, toda a hospitalidade sumiu com ela."

    mc envergonhado "Bando de putos..."

    $ nona_e1 = "banco"

    $ renpy.vibrate(1)

    "Opa. Meu celular..."

    "Quem será que é agora?"

    show screen celular_hacker

    pause

    "Que merda é essa? Quem é esse cara que tá falando comigo agora?"

    "Vem me encontrar aqui? {b}De noite{/b}?"

    "{b}Onde os invasores espaciais ficam dentro de uma caixa{/b}."

    "Invasores espaciais? Dentro de uma caixa?"

    mc preocupado "Tomara que seja uma metáfora..."

    "Enfim... seja lá o que for, eu tenho que ir no {b}centro da capital de noite{/b}. Lá na parte continental. Vou de busão e procuro o lugar."

    "Agora deixa eu sair desse banco que tudo isso me deixou puto pra caralho."

    $ tempo = 2

    jump call_cidade

label nona_evento1_final:

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ nona_e1 = "final"

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você vai ter que desafiar os poderosos da capital. Ir contra o status quo, o establishment."

        p "Você quer eles como seus inimigos? Se você aceitar, terá a pauta, e a chance de conquistar a donzela mais radical do mundo."



    "O fliperama..."

    "Antigamente as pessoas tinham que vir aqui pra jogar... antes dos games virarem algo que tá em casa... e agora na palma da mão."



    mc charmoso "Será que é isso que ela quis dizer?"

    "..."

    "{size=17}Será que é isso que ela quis dizer?{/size}"

    mc desconfiado "?"

    "Parece que eu escutei minha voz."

    "{size=19}Será que é isso que ela quis dizer?{/size}"

    mc surpreso "!"

    $ h_nome = "???"

    h "Não foi tão difícil assim, né?"

    mc bravo "Quem tá aí?!"

    scene hacker_fliperama with Dissolve(1.0)

    pause

    h "E aí, [mc]? Tudo bem?"

    mc bravo "... Foi você quem me mandou a mensagem?"

    h "Não."

    mc "..."

    h "Mas foi legal você vir aqui. Eu queria mesmo falar com você."

    "Essa mina... eu já vi ela antes. Eu tenho certeza."

    menu:
        "Quem é você?":


            mc "Quem é você?"

            h "Sou só uma garota que gosta de games antigos."

            mc "Só isso?"

            h "Ninguém é SÓ uma coisa, [mc]. Nem um ladrão é só ladrão. Ele é filho, ele é morador, ele pode ser gay ou hétero. Tantas coisas..."

            mc "Você entendeu o que eu quis dizer."
        "O que você quer falar comigo?":


            mc "Como assim queria falar comigo? O que você quer?"

            h "Pra que tanta agressividade?"

            mc "Eu não tô gostando disso tudo aqui. Fala logo o que você quer falar comigo."

            h "Calma, tio."

    h "Primeiro... olha bem pra mim. Você não tá me reconhecendo?"

    "A tatuagem nos braços!"

    show gevanni_hacker_mesa_close with dissolve

    pause

    "O cabelo tá diferente... os óculos são outros... mas a tatuagem é idêntica."

    "É a mina do banco!"

    hide gevanni_hacker_mesa_close with dissolve

    $ h_nome = "Carla"

    mc desconfiado "Você é a [h]... do banco."

    h "Aleluia."

    mc "O que isso significa? Não tô entendendo o que tá rolando."

    h "Haha... achei que você fosse um pouco mais esperto, [mc]."

    mc zerado "Ei..."

    mc serio "Então foi você quem me mandou a mensagem mesmo. É a única explicação. Você me trouxe aqui."

    scene hacker_fliperama_costas with Dissolve(1.0)

    h "Eu já disse que não mandei."

    mc bravo "Pode parar de mentir."

    h "Então me mostra a mensagem que eu mandei."

    mc desculpa "Eu não consigo acessar ela... Ela sumiu."

    h "Ela não sumiu. Na verdade, você nunca recebeu ela, porque nem eu e nem ninguém te mandou."

    mc "..."

    h "Seu celular foi hackeado, [mc]. Só isso."

    mc angustiado "Meu celular?! Quando?!"

    h "Eu não tô aqui pra te explicar isso. Pense um pouco e você vai saber."

    mc "..."

    h "O que importa é que eu sei tudo o que acontece com você. Eu tenho acesso à sua vida."

    menu:
        "E por que você fez isso?":


            $ hacker_amizade += 1

            mc concentrando "Tá. Vou pensar que você tem seus motivos pra tudo isso. O que você quer?"

            h "Indo direto ao ponto?"

            mc envergonhado "Acho que eu cansei de entender o começo. Vamo logo pro fim."

            h "..."
        "Isso é um absurdo!":


            mc bravo "Isso é um absurdo. Eu posso te denunciar por isso."

            h "Claro que pode, mas se você soubesse a quantidade de processos que eu enfrento, ia desistir da ideia."

            mc desculpa "{i}Hmf{/i}... Q-quem é você?"

            h "Eu sou meio diferente. Só isso..."

    scene hacker_fliperama_seria with Dissolve(1.0)

    h "Meu objetivo é diferente do seu e da maioria das pessoas."

    h "Eu olho pra esta cidade e fico pensando o que raios aconteceu que as coisas acabaram assim."

    mc desconfiado "?"

    h "O [gi] é um nojento, mas ele não é o único. Ele controla o dinheiro, mas e os que controlam o resto?"

    h "Pense. O Barão, o prefeito, a Faux News e até sua revista... vocês controlam tudo."

    mc envergonhado "Quem dera eu controlasse alguma coisa."

    h "Você é igual a eles, [mc]. Você quer dinheiro, mulheres, fama, poder."

    menu:
        "Eu quero mesmo. Foda-se.":


            mc charmoso "E daí? É o que eu quero mesmo."

            h "Tá vendo? Você não vê que tá ferrando as pessoas nessa sua jornada pelo sucesso?"

            mc preocupado "Ferrando? Como assim?"

            h "Olhando só pro seu umbigo, você tá passando por cima dos outros. Você não vê que tem merda acontecendo nessa cidade?"

            mc desculpa "..."
        "Você não sabe nada de mim.":


            $ hacker_amizade += 2

            mc bravo "Você não sabe nada de mim. Não é porque você viu umas mensagens no meu celular que você me conhece."

            h "Você não faz parte do clubinho deles?"

            mc "Não."

            h "..."

    h "Eu não confio em você. E além disso, eu sempre trabalhei sozinha."

    h "Mas dessa vez eu cheguei em uma encruzilhada. Não posso fazer o que eu preciso sozinha."

    h "E por mais que eu não ache você o cara mais confiável do mundo, você é o melhorzinho entre as opções que eu tenho."

    mc desconfiado "..."

    h "O que eu quero dizer é o seguinte..."

    h "Se você fizer algo por mim, a gente pode fazer um tipo de aliança."

    mc serio "Uma aliança..."

    h "Mesmo que a gente não tenha os mesmos objetivos, eu acho que a gente pode se ajudar."

    "Essa mina... parece que ela tá falando de algo muito sério. Mas tá tudo meio atropelado. Eu nem sei quem é ela."

    mc serio "Eu nem sei seu nome. Aposto que não é [h]."

    scene hacker_fliperama_bracos with Dissolve(1.0)

    pause

    mc surpreso "!"

    "Até que ela é bonita..."

    $ h_nome = "Nona"

    h "Eu não vou falar meu nome, mas a galera dos fóruns me chama de [h]."

    mc desconfiado "[h]? Tipo um número?"

    h "Ache o que você quiser."

    mc zerado "..."

    h "Eu trabalho sozinha, mas eu não estou sozinha, [mc]. Tem algumas pessoas na capital que não querem que as coisas fiquem como estão."

    h "Nós vamos limpar a cidade desse povo que acha que aqui é o fliperama deles. Que eles podem comandar a gente igual um jogo."

    h "Se você vai ou não me ajudar é com você. Mas se você realmente for ajudar a gente, saiba que você vai estar comprando briga com o status quo."

    h "Vai chegar uma hora que você vai ter que escolher. Eles ou nós."

    mc desculpa "Eu não sei se eu entendi exatamente o que isso quer dizer."

    h "Não dá pra te explicar tudo agora. Preste atenção em coisas estranhas que acontecem do seu lado, [mc]."

    mc "Tá, vou tentar... mas o que você quer que eu faça?"

    scene hacker_fliperama_costas with Dissolve(1.0)

    h "Certo... sobre isso. Eu consegui informações sobre a construção do aeroporto da cidade."

    h "Eu tenho certeza que a obra foi superfaturada pelo prefeito. Ele tá de rolo com a construtora."

    h "A licitação foi feita de forma obscura."

    mc desconfiado "Mas é assim fácil desse jeito? Não tem nenhum órgão de olho nisso?"

    h "Tem. Sabe qual? O Novo Banco Central."

    mc surpreso "Como assim?!"

    h "O NBC é um órgão público da cidade que monitora transferências, inclusive da prefeitura. Eles validam esse tipo de transação."

    h "Mas obviamente o {b}grupo{/b} tem alguém lá dentro."

    mc bravo "O [gi]."

    h "Óbvio. Ele valida tudo o que o Donatello manda. Eu tenho certeza que eles tão juntos nessa. Mas não tenho como provar."

    h "O que eu posso provar é que a obra foi superfaturada. Eu tenho todos os dados da transação."

    h "Mas na minha mão isso não quer dizer nada. Eu preciso que você publique isso na sua revista."

    mc surpreso "Uma pauta!"

    scene hacker_fliperama_seria with Dissolve(1.0)

    h "E aí? Posso contar com você?"

    mc desculpa "..."

    "Espera... se o que essa [h] tá falando é verdade... então tudo isso é um lance muito grande."

    "Se eu mexer nesse ninho de vespa, eu posso me ferrar. E muito."

    "O [gi] me disse pra escolher o lado certo. De um lado, os ricos e poderosos da ilha. Do outro, essa [h]..."

    "Será que realmente vale à pena? Se o [gi] tá com a Faux News, então eles querem assumir minha revista e eu ganho com isso se eu tiver do lado deles."

    "Sinto que essa é uma das {b}decisões mais determinantes que eu já tive que tomar desde o começo{/b}."

    "O que eu faço?"

    menu:
        "Aceitar a proposta da [h] e receber a pauta":


            $ nona_e1 = "aceitou"

            "Eu vou mesmo me juntar com essa desconhecida e enfrentar esse grupo de gente que comanda a capital?"

            "Isso parece doideira demais, mas alguma coisa tá me falando que isso é o certo."

            "Eu não quero deixar esses caras fazerem o que quiserem."

            "O bom é que eu vou ganhar uma pauta tambem. Isso é muito importante."

            "E com certeza eu vou poder me aproximar mais dessa [h]. Ela é uma gata, isso é certeza. Um excelente bônus."

            mc concentrando "Não sei se é a melhor decisão pra mim... mas eu vou aceitar."

            h "Sério?!"

            mc desconfiado "Sério. Mas como você conseguiu esses dados?"

            scene hacker_fliperama_feliz with Dissolve(1.0)

            h "Não é óbvio? Eu sou a assistente coitada do [gi] que sonha em ter uma carreira no banco. Idiota."

            mc envergonhado "Verdade! Ele nem imagina..."

            h "É estranho como a maioria dos homens é assim. Eles acham que as mulheres são coitadas."

            h "Só dar um pouco de bola pra eles e eles acham que a gente tá na mão. Ficam tudo mansinho como se fosse gado."

            mc zerado "Ei... eu sou um homem também."

            h "A é? Não tinha percebido."

            mc "Isso não é um elogio..."

            h "Claro que é. Não sei qual é a vantagem de ser homem..."

            h "Mas eu já deixei todas as informações que eu consegui no seu celular. Vai parecer como se você tivesse tirado as fotos."

            mc envergonhado "Quer dizer que você não quer se envolver."

            h "Eu trabalho nas sombras, [mc]. Nas sombras que eles mesmos criaram pra mim."

            mc desconfiado "Hmm..."
        "Negar a proposta e sair fora":




            $ nona_e1 = "negou"

            "Se eu não aceitar, provavelmente ela não vai querer nada comigo. É uma pena, porque essa [h] é bonita mesmo."

            "Mas não dá pra pensar sempre com a cabeça de baixo. Me aliando ao grupo do [gi] eu ganho bem mais."

            mc desculpa "Olha, [h]. Eu tô ligado do que você tá falando, mas pra mim não vai rolar. Eu não quero treta com eles."

            scene hacker_fliperama_costas with Dissolve(1.0)

            h "Foi o que eu achei mesmo. Você é só mais um deles."

            mc desculpa "Não é bem assim... Eu acho que a gente tem que saber as lutas que a gente pode comprar."

            h "Então é por covardia mesmo."

            mc "Pode ser. Mas antes de tudo eu tenho que pensar em mim. E o melhor caminho pra eu me dar bem aqui é esse."

            h "Tomara que você consiga dormir à noite sabendo que você tá ferrando os outros."

            h "Ter esse poder todo que esse grupo tem não é de graça. Eles fodem muita gente pra manter essa roda girando, [mc]."

            h "E pode ter certeza que eles não vão pensar duas vezes antes de te entregar se for preciso."

            h "Mas aproveite bem o sucesso. Espero que você seja bem rico e famoso e isso te traga bastante mulher e muita felicidade."

            mc "..."

            h "Agora dá o fora."

            mc "Falous."

            scene cidade fliperama with Dissolve(1.0)

            "Claro que ela ia ficar puta. Mas foi a decisão que eu escolhi. Tenho que pensar em mim."

            "Era isso que o senhor Luca Alighieri tava falando aquele dia. Às vezes a gente precisa pensar em nós."

            "Eu quero me aliar às pessoas certas e estar do lado dos vencedores. A [h], coitada. Vai ser soterrada cedo ou tarde."

            "A máquina é grande demais pra alguém querer parar sozinha. Por um lado bate até uma tristeza..."

            "Tomara que ela fique bem."

            jump hacker_e1_finalizar

    h "Eu sei que não é fácil confiar em alguém em assim do nada. Pra mim não foi fácil escolher você também."

    h "Mas eu deixei tudo no seu celular. Pode entregar pro seu chefe. Certeza que ele vai publicar, se ele não estiver envolvido."

    "Será que o chefe tá envolvido?"

    scene hacker_fliperama_bracos with Dissolve(1.0)

    $ renpy.notify("Nona está olhando diretamente em seus olhos")

    h "Eu queria poder te falar mais... mas não sei até que ponto você realmente é um cara diferente, [mc]."

    menu:
        "Faz o que eu tô falando. Confia em mim.":


            mc charmoso "Tô falando pra você confiar em mim. Faz isso que vai dar bom."
        "Não precisa me contar. Você sabe o que tá fazendo.":


            $ hacker_amizade += 2

            mc concentrando "Beleza. Você sabe o que tá fazendo. Se você acha melhor não falar nada agora, eu entendo."

    h "Hmm..."

    if hacker_amizade >= 11:

        $ h1_seducao = True

        h "Não é nada que seja interessante pra você."

        mc envergonhado "Olha... tudo isso tem sido tão doido pra mim que se você me falar que a chuva é molhada acho que vou achar interessante."

        h "Sei... É que depois de ficar tanto tempo tratando todo mundo como inimigo, é complicado confiar nos outros."

        mc desculpa "..."

        h "Mas depois de ver como você é estranho, acho que até me deu um pouco de coragem."

        mc zerado "Estranho?"

        h "E não é? Eu tava olhando pra você hoje durante o dia e você falou umas coisas que eu não imaginava."

        h "Você é bem diferente do [gi]."

        mc envergonhado "Você acha?"

        h "Upa."

        scene hacker_fliperama_sentada with Dissolve(1.0)

        pause

        "Acho que ela tá ficando mais à vontade comigo."

        h "O [gi] é o típico homem que eu odeio. Ele acha que ser chefe, ter dinheiro e uma fala mansa faz dele um imã de mulheres."

        mc envergonhado "E ele tá errado?"

        h "Não."

        mc zerado "Não? Então-"

        h "Tem muita mulher que gosta disso no homem. Elas gostam de sentir segurança. E com um homem rico e confiante você tá protegida de tudo."

        mc desconfiado "Até agora não entendi se você gosta ou não..."

        h "Eu odeio."

        mc "Não parece..."

        h "Olha, [mc]. Você é um jornalista. Você conhece pessoas, você fala com elas. Eu acho que você tem um dom pra entender o ser humano."

        h "Eu vi isso lendo suas mensagens no celular."

        mc zerado "Não tem nem vergonha de falar..."

        h "Você é um paparazzo. Você também já deve ter xeretado muito."

        mc envergonhado "Não vem ao caso."

        h "Quando você olha pra mim, o que você vê?"

        mc surpreso "O-o que eu vejo?"

        h "Sim."

        mc concentrando "Eu..."

        menu:
            "Eu vejo uma garota rebelde.":


                mc charmoso "Eu vejo uma garota rebelde, que quer ir contra o sistema."
            "Eu vejo uma moça com medo.":


                mc charmoso "Eu vejo uma moça com medo de relações verdadeiras com as pessoas."
            "Eu vejo uma mulher confiante.":


                mc charmoso "Eu vejo uma mulher confiante que não tem medo de fazer o que acha certo."

        h "..."

        scene hacker_fliperama_deitada with Dissolve(1.0)

        pause

        h "Talvez eu seja isso mesmo."

        mc surpreso "N-n-nona!"

        h "Talvez eu seja outra coisa totalmente diferente."

        h "Você lembra de mim lá no banco? E eu de alguns minutos atrás? E eu agora?"

        h "Sua opinião sobre mim continua a mesma desde o começo?"

        menu:
            "Sim.":


                mc envergonhado "Acredito que sim."

                h "Não sei se eu acredito em você..."
            "Não.":


                mc envergonhado "Não..."

                h "Será que você mudou ou eu que mudei?"

        mc "Não sei o que posso falar..."

        h "A vida não é igual um game, [mc]. Não tem barra, não tem coraçãozinho, nem piscadinha na tela pra saber se você acertou ou não."

        h "Não tem como responder o 'melhor' pra ganhar pontos. E sabe por que eu acho isso?"

        h "Porque às vezes nem quem pergunta sabe a resposta. E também nem sabe por que tá perguntando."

        mc zerado "Assim fica complicado mesmo..."

        scene hacker_fliperama_deitada_close with Dissolve(1.0)

        pause

        h "Então eu te falo. Seja sincero e responda o que vier na cabeça. Não tenha medo de ser você."

        h "É o que eu faço pelo menos."

        mc envergonhado "E tem dado certo?"

        h "Não."

        mc zerado "Não?"

        h "Eu vivo sozinha, nunca namorei, meus amigos estão todos do outro lado do mundo. Você acha que isso é dar certo?"

        mc normal "Bom... falando assim parece que não... mas eu acho que no fundo depende de cada um."

        h "Aleluia você falou uma coisa certa."

        mc zerado "..."

        h "Acho que eu acertei em te contar tudo."

        mc desconfiado "Como assim? Você não me contou nada sobre o prefeito, ou sobre o aeroporto ou sobre o que você faz."

        h "E daí? Nada disso importa, [mc]. Você não tá aqui pra me pegar? Então... eu te dei armas pra você usar contra mim."

        "O que tá acontecendo aqui?"

        mc envergonhado "Não sei..."

        h "Pense bem sobre o que eu falei."

        scene black with Dissolve(1.0)
    else:


        h "Acho melhor deixarmos como está por agora. Entregue a pauta e conversamos mais outro dia."

        mc envergonhado "Ok..."

        "Sinto que não consegui fazer ela confiar em mim. O que será que eu falei?"

    h "E não vai esquecer disso, [mc]."

    mc desconfiado "O que?"

    scene hacker_fliperama_mc with Dissolve(1.0)

    pause

    mc "O-opa..."

    h "Esses caras são perigosos... Diferente de mim, você é quase um homem público. Seu nome até aparece em revistas."

    h "Você acaba virando um alvo fácil. Não dê bandeira, não saia falando pro mundo tudo o que você acha."

    h "A gente não pode ter medo, mas tem que saber lutar. Se entregar pro inimigo não é coragem, é idiotice."

    mc "P-pode deixar."

    h "Até que você fica fofo com vergonha."

    mc "Hahaha..."

    h "Depois que você entregar a pauta eu vou esperar a hora certa e daí te chamo. Não vai trocar de celular."

    h "Ah! Enquanto isso, preste atenção no seu chefe e nas pessoas que você fala. Descubra o que cada uma delas quer."

    h "Ninguém é santo nesse mundo. Todo mundo quer alguma coisa. Até eu."

    h "Beijinho."

    scene black with Dissolve(1.0)

    scene cidade fliperama with Dissolve(1.0)

    mc concentrando "Ufa... Ela foi embora."

    "Quem é essa mina? Bom... nessa altura eu já devia ter me acostumado com esse povo estranho."

    "Será que só eu sou normal nessa ilha?"

    "Não é a primeira vez que eu escuto sobre esse tal de grupo. Será que isso realmente existe?"

    "Parece coisa de maluco achar que o prefeito e pessoas importantes fazem parte de um lance Illuminati. E se essa mina só é doida?"

    "Às vezes eu tenho a impressão que por mais que eu decida o que quero da vida, tudo vai pro mesmo lugar de uma forma ou de outra."

    "Será que é isso que chamam de destino?"



    $ pautas += 1
    $ hacker_p1 = True

    label hacker_e1_finalizar:

        pass





    scene black with Dissolve(3.0)

    $ tempo = 3

    $ v30_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v30_fim","final","local")

    call checa_final from _call_checa_final_12

    jump call_cidade

label nona_evento2:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("h2_save", extra_info="h2_save")

    $ estou_na_cidade = False
    $ iconchefe += 1

    $ nona_e2 = "evento"

    $ no2_evento = False
    $ no2_ape = False
    $ no2_especial = False

    if nona_e1 == "aceitou":

        $ nona_aceitou = True
    else:


        $ nona_aceitou = False

    ron "Ei, [mc]."

    mc desconfiado "Opa. Fala, [ron]."

    scene no2_ronaldo1 with Dissolve(2.0)

    pause

    if hacker_atencao > 0:

        ron "Me pediram pra escrever a matéria sobre o aeroporto que você entregou. Parabéns mesmo por ter conseguido esse dossiê."

        mc "Você deu uma olhada?"

        ron "Sim. O chefe me passou a pauta e tô apurando tudo. Não imaginei que esse tipo de informação existia."

        ron "Isso aí deve ter vindo direto do Novo Banco Central. Alguém lá de dentro deve ter pego."

        mc "Hmm..."

        ron "Relaxa. Não vou perguntar da sua fonte."

    elif nona_aceitou:

        ron "Sabe aquele lance do aeroporto?"

        mc "Tô ligado. Ainda é segredo, mas eu tô com as infos disso aqui pra uma pauta. Só não passei pro chefe ainda."

        ron "Sério? Vou ficar de olho. Quero escrever sobre isso."

        ron "Aliás, eu acho que esse lance já tá rolando por aí, viu? Se eu fosse você não segurava muito."

        mc "Hmm..."
    else:


        mc "Qual lance?"

        ron "Sobre a obra do aeroporto que foi superfaturada."

        mc "Sei..."

        "Aquela mina do fliperama queria me dar essa pauta, mas eu não peguei."

        ron "Então, eu consegui as infos pra ela e o chefe já me deu pra escrever. Vai sair alguma coisa logo."

        menu:
            "Parabéns, cara.":


                mc "Massa, cara. Parabéns. Essa matéria vai ser quente."

                ron "Valeu, [mc]."
            "Você conseguiu com uma garota de tatuagem?":


                mc "Você conseguiu essa info com uma garota morena de tatuagem nos braços?"

                ron "Pô, [mc]. Aí você quebra minhas pernas. A gente não pode revelar as fontes."

                mc "Eu sei, malz."

                ron "Se bem que pelo seu comentário bem específico... sim, foi ela. Você conhece a garota?"

                mc "Sim. Toma cuidado com ela, [ron]."

                ron "Beleza, valeu."

    ron "Eu só queria avisar você, porque o que mexe com o Donatello e esse povo da prefeitura dá merda."

    mc "Com certeza é coisa delicada, mas dá merda como? Já aconteceu alguma coisa real com alguém?"

    ron "Então... você tá aqui há menos tempo, não sei se você ouviu, mas já aconteceu de um jornalista desaparecer durante uma investigação."

    mc "S-sério?!"

    ron "Faz tempo já. Foi antes de eu começar a trabalhar aqui. E o cara que sumiu não era aqui da revista, era de um jornal."

    mc "Falando nisso, além do jornal da Faux News, hoje em dia não tem mais, né?"

    ron "Verdade. Quando a família Donatello assumiu, eles criaram uma espécie de órgão regulador. Ficou foda abrir outras agências na capital."

    ron "A Faux também é muito grande. É duro competir com eles no hard news. Daí outros jornais acabam até esquecendo a capital."

    mc "Mas que bela exclusividade eles arranjaram, hein?"

    ron "Pra mim, meio que uma mão lava a outra. A prefeitura deixa a Faux livre de concorrência e a Faux meio que cobre os Donatello."

    scene no2_ronaldo2 with Dissolve(1.0)

    pause

    ron "Mas claro que é só conspiração minha haha. É duro provar essas coisas."

    "Então será que é essa a relação da prefeitura com o [lu] e a Faux?"

    menu:
        "Isso é meio conspiração demais pra mim.":


            mc "Haha... pra mim isso é meio conspiração demais. Parece coisa de gente doida. Com todo o respeito, claro."

            ron "Hah! Tá tudo certo. Eu sei que é meio viajado, mas tem alguma coisa aí que não cheira bem."

            mc "Bom, a gente aqui tem que tá sempre de olho."

            ron "É o que eu acho."
        "Eu acho que tem base isso aí.":


            mc "Pensando aqui... faz bastante sentido até. Uma mão lava a outra."

            ron "Exatamente. Eles têm muito a ganhar juntos. Mas não vai ficar pensando muito nisso. Podem te chamar de maluco haha..."

            mc "Pode deixar."

    ron "Olha... então eu vou juntar tudo o que eu conseguir sobre o aeroporto. O lançamento tá super perto. Qualquer dia desses eles devem anunciar."

    mc "Beleza. Vou ficar esperto também. Qualquer coisa eu te falo, ok?"

    ron "Valeu. Sabe, [mc]... um tempo atrás eu achava que você era só um mulherengo que dava sorte com as minas e pegava informações delas."

    mc "Que loucura..."

    ron "Mas acho que não. Você parece que tem um bom senso, viu?"

    mc "Ah. Valeu."

    ron "Desculpa se eu fui direto demais. Mas é que você sempre conseguiu umas pautas de várias minas, daí né..."

    mc "Relaxa. Se realmente fosse isso, será que seria tão ruim assim?"

    ron "É... acho que por isso que eu tava invocado. Essa é uma vida que todo mundo que curte mulheres ia querer, hein?"

    mc "Verdade..."

    ron "Um dia desses a gente podia beber um goró e você me ensina como chegar nos outros assim."

    mc "Haha... como se eu soub-"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "{i}Trrr trrr{/i}"

    mc "Opa. É o meu."

    ron "Vou deixar você atender. A gente se fala."

    mc "Valeu. Até depois, [ron]."

    scene trabalho angulo with Dissolve(1.0)

    mc desconfiado "Oi. Quem é?"

    $ h_nome = "Carla"

    h "Olá. Aqui é a [h], secretária do senhor [gi] do Novo Banco Central. Tudo bem?"

    mc "Tuudo..."

    h "O senhor lembra de mim, senhor [mc]?"

    menu:
        "Eu lembro. Você é a moça do banco.":


            $ hacker_amizade += 1

            mc "Tô ligado. Você é aquela moça que me levou pra conversar com o [gi] no outro dia."

            gi "Isso... Nós tivemos uma conversa aqui na agência da ilha do NBC."

            mc "Sim, sim. O que você precisa?"
        "Você não é a Nona do fliperama?":


            $ hacker_amizade += 2

            mc "Você já revelou pra mim no fliperama que seu nome não é [h]. Que era pra eu te chamar de Nona. Foi esses dias."

            h "Não sei do que o senhor está falando. A gente se viu no banco, não em qualquer outra lugar."

            mc preocupado "Ma-"

            h "Senhor! Por favor, preste atenção. Essa pessoa parece ser bem interessante, mas não sou eu."

            mc zerado "Ok... Sei, eu lembro que a gente conversou no banco também."

            h "Que bom que você lembra de mim."

            mc "Tá bom. O que foi?"
        "Desculpa, mas não lembro.":


            mc envergonhado "Desculpa aí, mas não tenho ideia de quem é."

            h "Nós conversamos no NBC há uns dias. Eu te perguntei sobre aquele dinheiro que tinha entrado na sua conta."

            mc surpreso "AAH! Aqueles 300 mil, né?"

            h "Isso."

            mc zerado "Que depois desapareceram..."

            h "O que foi uma boa coisa para o senhor."

            mc "... Tá. O que você quer?"

    h "O motivo da minha ligação é que eu gostaria que o senhor viesse em nossa agência novamente."

    mc envergonhado "Será que são mais 300 mil?"

    h "Felizmente não. É uma visita especial e gostaríamos que o senhor visse como uma pesquisa de trabalho."

    mc desconfiado "Pra revista você diz?"

    h "Isso mesmo. Queremos que o senhor venha conhecer nosso trabalho. Veja de perto nossa rotina."

    mc envergonhado "Sinceramente, não sei se a rotina de um banco seria interessante suficiente pra ser públicada na nossa revista."

    h "Eu acredito que vale à pena o senhor conferir e julgar pelos seus próprios olhos. Nunca se sabe o que pode virar pauta."

    mc desconfiado "Hmmm..."

    h "O que você acha? Prometo que poucas horas da sua atenção serão suficientes."

    "Essa mulher... eu tenho certeza que ela é encrenca."

    if nona_aceitou:

        "Ela me deu a pauta do aeropoto, que foi excelente. Mas ela tá brigando com o grupo que manda na ilha."

        "Quanto mais eu me meter nessa, mais eu viro alvo desses caras."
    else:


        "Eu já recusei a pauta que ela queria me dar. Eu sabia que aquele dossiê era encrenca."

        "Agora ela me chama pra isso? Se bem que ela é a secretária do [gi], talvez ele me queira lá..."

    "Não sei se seria uma boa eu entrar de cabeça nessa. Minha vida tá meio sem noção ultimamente, mas eu não sou burro também."

    "Sem dúvidas essa [h] ou Nona, sei lá, é uma pitchula. Às vezes vale à pena arriscar a mão de olho no pote. Hmm..."

    "Essa não tá fácil. O que eu faço?"

    menu:
        "Ok. Posso dar uma passada sem compromisso.":


            $ no2_evento = True

            mc "Beleza. Acho que eu posso acompanhar o dia de vocês, mas sem compromisso."

            h "De acordo! Era só isso que eu queria de você, [mc]. Conhecer o banco e tirar suas conclusões."

            h "E também é uma oportunidade para a gente conversar, certo?"

            "O que ela quer dizer com isso?"

            mc envergonhado "Verdade..."

            h "Então te espero aqui no banco."

            mc normal "Ok. Tô passando aí agora."
        "É melhor eu não me meter com essa mina.":


            "{b}Escolhendo esta opção, você perderá o restante do encontro e ele prosseguirá para o final. Não é recomendado se é sua primeira vez jogando.{/b}"

            "{b}Se quiser ver o evento, use o botão VOLTAR para escolher a outra opção.{/b}"

            "Eu não tenho por que me meter com essa mulher. Ela é cheia dos trambiques e mexe com gente grande."

            "Se eu quero me dar bem na ilha eu tenho que seguir a recomendação do chefe e pensar bem as lutas que eu vou comprar."

            mc desculpa "Valeu, [h], mas é melhor eu ficar de fora dessa."

            h "M-mas, [mc] e-"

            mc "É só isso mesmo. Se eu precisar de algo do banco eu aviso. Tenha um bom dia."

            h "E-"

            "{i}gatchack{/i}"

            "Chega de dar mole pra esse povo problemático. Eles que se virem."

            "Pode ser a mina mais gata da cidade. Entrar nessas é pedir pra se ferrar bonito. Eu tô fora."

            "Vamos ver o que a cidade guarda pra mim. Tem muita coisa boa pra curtir aqui!"

            mc charmoso "Agora deixa eu trabalhar e ganhar uns pontos com a [w]."

            ron "Gado!"

            mc zerado "..."

            scene black with Dissolve(1.0)

            "..."

            jump nona_e2_final

    mc zerado "Que os céus me ajudem com essa garota..."

    scene black with Dissolve(1.0)

    "..."

    scene hacker_banco with Dissolve(1.0)

    h "Olá, [mc]. Que bom que você veio. Nossa visita vai ser muito interessante. Aposto que será mais emocionante do que você imagina."

    menu:
        "Opa. Se você tá falando.":


            $ hacker_amizade += 1

            mc charmoso "Se você tá falando eu vou acreditar. Mas, sinceramente, não sei o que pode ter de emocionante aqui."

            h "É justamente isso que eu quero que você veja. Como tudo acontece aqui."
        "Sei lá... meio difícil, né?":


            mc envergonhado "Olha... não dá pra acreditar muito... sem querer ser mala."

            h "Você não tá sendo mala, mas garanto que você vai se impressionar até o fim."

    mc "Bom... Ok. Vamos lá então."

    h "Eu só preciso terminar de passar uma coisinha aqui pro pendrive e já começamos."

    mc normal "De boa."

    h "..."

    h "Ok. Resolvido."

    h "Nosso passeio começa lá em cima, porque tem um gerente que quer conversar um instante com você."

    mc desconfiado "Hm? O [gi]?"

    h "Isso. Na verdade tudo isso aqui foi ideia dele."

    mc envergonhado "Ah. Imaginei que podia ser mesmo."

    h "Ele leva sua revista bastante à sério. Quer ter certeza que você tenha a impressão certa sobre o NBC. Vamos lá então?"

    mc normal "Claro. Você primeiro."

    scene black with Dissolve(1.0)

    h "[gi]?"

    gi "Opa, [h]. Podem entrar."

    scene no2_gevanni1 with Dissolve(1.0)

    pause

    gi "Obrigado por ter vindo, [mc]."

    mc normal "Não precisa agradecer. Faz parte do meu trabalho."

    gi "Eu não sei o que a [h] te disse pra te trazer aqui, mas essa garota consegue tudo o que ela quer. É impossível."

    gi "Aliás, espero que ela não tenha te oferecido nada impróprio."

    h "Senhor [gi]!"

    mc envergonhado "N-não!"

    gi "Eu quero que você guarde essas ofertas pra mim, [h]. É o nosso trato."

    h "Senhor..."

    gi "Haha! É brincadeira, viu [mc]! Por favor, não coloque isso na sua matéria. Seria um desastre!"

    menu:
        "Pode deixar. Eu sei que é brincadeira":


            mc charmoso "Pode ficar tranquilo que eu sei separar o que é brincadeira do que é sério."

            gi "Será? Haha... brincadeira. Claro."

            mc desconfiado "..."
        "Mas esse é o tipo de coisa que as pessoas gostam!":


            $ hacker_amizade += 1

            mc charmoso "[gi], é isso que as pessoas querem ver. Se eu f-"

            gi "Pode parar por aí! Não quero nem ouvir uma coisa dessas!"

            h "Por favor, [mc]. É só uma brincadeira."

            mc envergonhado "Eu sei. Estou brincando também."

            gi "Hahaha! Ufa..."

    scene no2_gevanni2 with Dissolve(1.0)

    gi "Enfim. Antes de irmos pro prato principal deste encontro. E eu não tô falando da [h], obviamente. Só queria deixar algo claro."

    gi "Não quero que sua presença aqui pareça que estamos querendo influenciar você de alguma forma."

    gi "Isso é algo muito importante e precisa ficar claro."

    mc charmoso "Eu entendo. Você quer uma visão imparcial do local."

    gi "Isso! Você sabe como encarar as coisas."

    mc "Acontece bastante quando temos que lidar com situações delicadas. Principalmente agora com uma nova chefe nossa."

    gi "Ela é encardida?"

    mc envergonhado "Bota encardida nisso... mas ela tá dando uma boa acertada na revista. Mais trabalho, claro, mas no geral acho que vale à pena."

    gi "Eu fico impressionado vendo mulheres em posições de chefia, sabia?"

    mc desconfiado "Por quê?"

    gi "Eu acho que mulheres não sabem muito bem como liderar. Elas são incertas e emocionais demais. Elas são terríveis e agem pelas costas."

    mc envergonhado "..."

    gi "Você entende que isso não é depreciativo, certo, Carlinha? Você é demais no seu trabalho."

    h "Eu sei, senhor. Eu concordo com você. Nós somos meio indecisas e preferimos que um homem diga o a que gente tem que fazer. É mais simples."

    gi "Tá vendo, [mc]? Por isso eu amo essa gatinha."

    gi "Agora venha, sente aqui."

    scene no2_gevanni3 with Dissolve(1.0)

    pause

    gi "Bom. Depois de todo esse rodeio, chegou a hora da verdade."

    mc envergonhado "Você precisa começar me explicando o que se trata isso aqui, porque eu não sei direito o que tá rolando."

    gi "Eu pedi pra [h] levar você para conhecer nosso trabalho."

    mc charmoso "Certo. Essa parte eu tô sabendo. Mas o que é isso 'aqui', agora."

    gi "Ah! Eu pensei que uma boa forma da gente começar seria com você fazendo algumas perguntas que você achar interessantes."

    gi "Talvez você queira saber algo sobre o banco. Alguma coisa específica."

    menu:
        "O que o NBC faz exatamente?":


            mc "Eu queria que você me explicasse o que o NBC faz na sua visão. O que ele é e qual a importância da instituição?"

            gi "O Novo Banco Central é uma instituição municipal ligada à prefeitura e foi criada por pedido dos vereadores."

            gi "É um órgão de controle e fomento. Nosso trabalho principal é checar os gastos do prefeito e ver se está de acordo com o Plano Diretor."

            mc "Certo. Então você confere se a prefeitura tá gastando o dinheiro de acordo com o planejado."

            gi "Isso. É bom você escrever isso de forma simples, senão o povo não entende nada."
        "Não. Eu prefiro descobrir tudo olhando a rotina.":


            mc charmoso "Eu acho melhor não ter uma conversa direta, mas só olhar mesmo."

            gi "Tem certeza?"

            mc "Sim. Pra mim está de bom tamanho."

            jump no2_depois_perguntas

    scene no2_gevanni4 with Dissolve(1.0)

    gi "Mais alguma coisa que você queira saber?"

    menu:
        "Quem trabalha aqui?":


            mc "Quem é que trabalha aqui?"

            gi "A maioria são funcionários públicos concursados. Mas algumas posições, como a da [h] aqui, são indicações."

            h "Isso. O senhor [gi] foi muito legal comigo me dando esta posição."

            gi "Aquele email que você me mandou pedindo uma posição foi incrível. Eu lembro até hoje quando ela disse que faria tudo por isso."

            gi "Eu preciso de funcionárias com esse tipo de determinação."

            h "E até hoje eu estou."

            gi "Eu sei, [h]. Eu vejo."

            mc "E você? Como conseguiu a diretoria?"

            gi "Bom, meu caso foi diferente, pois foi uma indicação dos próprios vereadores. Eu já tinha uma carreira no sistema bancário."

            gi "Eu também não tinha nenhum laço com o grupo político do prefeito, então eu fui sabatinado e escolhido por votação na Câmara."

            mc "Entendi. Era isso que eu queria saber."

            gi "Muito bom."
        "Não. Aquela pergunta foi o suficiente.":


            mc charmoso "Não. Está tudo certo. Era só aquela mesmo."

            gi "Tem certeza?"

            mc "Sim. Pra mim está de bom tamanho."

            jump no2_depois_perguntas

    label no2_depois_perguntas:

        scene no2_gevanni5 with Dissolve(1.0)

        gi "Então estamos acertados. Só uma coisa que eu queria que você entendesse."

        gi "Talvez você escute alguma coisa estranha sobre nosso trabalho e a prefeitura, mas isso não passa de falcatrua."

        gi "Como que as pessoas falam hoje em dia? Fake News. É tudo fake news."

        mc "O que por exemplo?"

    gi "Nada que mereça sua atenção. Só estou alertando caso você escute alguma coisa. Pode ter certeza que são fake news."

    mc serio "Entendi. Vou ficar de olho aberto."

    gi "Esse é o tipo de coisa que nem merece nossa atenção, entende? Não perca tempo da sua vida com mentiras."

    mc "Pode deixar."

    gi "Ufa. Acho que tivemos uma conversa produtiva. Certo, [h]?"

    h "Com certeza senhor. Posso levar o [mc] então?"

    gi "Com certeza. Fiquem à vontade para conhecer nossas instalações. É algo pacato, como qualquer instituição séria deve ser."

    h "Então vamos, [mc]."

    mc normal "Claro."

    scene black with Dissolve(1.0)

    scene banco_visao with Dissolve(2.0)

    pause

    h "A conversa com o senhor [gi] demorou mais do que eu esperava. Não quero te prender demais aqui."

    mc charmoso "Não esquenta. Eu tirei o dia pra fazer isso."

    h "Não não. Temos que acelerar."

    mc desculpa "Espera, por favor. A gente precisa falar sobre o que tá rolando aqui."

    h "'O que está rolando?'"

    mc "É. Nós já passamos por tudo isso aqui da outra vez. A história da '[h]', a conversa com o [gi]... eu sei quem você é."

    scene no2_conversa1 with Dissolve(1.0)

    pause

    h "O que você tá falando, [mc]? Sinceramente, não sei o que você quer dizer."

    menu:
        "Ok, entendi. Deixa quieto. Vamos logo com isso.":


            $ hacker_amizade += 2

            mc zerado "Tá bom, ok, entendi tudo. Mas depois eu vou querer saber de tudo."

            h "Venha, vamos por aqui."

            "Essa garota... às vezes eu sinto que eu sou um nada pra ela."

            "Ela beija os pés daquele ridículo mas não tem um minuto pra falar comigo. Que saco."

            jump nona_e2_conversa
        "Eu não vou te expor. Só quero uma explicação.":


            $ hacker_amizade += 1

            mc "Eu sei que você precisa manter essa fachada. Mas eu preciso conversar com você."

            mc "Eu não quero continuar andando pelo banco como um jornalista fazendo uma matéria. Eu sei que não se trata disso."

            h "Isso não é simples pra mim. Se alguém pegar a gente e ver o que estamos falando, vai tudo pro buraco."

            mc "Eu sei. Prometo que vou seguir suas recomendações."
        "Foda-se que aqui é o banco. Eu quero conversar.":


            mc bravo "Chega. Cansei dessa palhaçada. Você precisa me explicar o que tá rolando."

            h "E-está bem. Calma."

            mc desculpa "Não quero ferrar você, mas, poxa, eu não vou aceitar ficar de fora desse jeito."

            h "Tudo bem. Respira. Isso aqui é importante pra mim, [mc]. Você não pode estragar tudo."

            if not nona_aceitou:

                h "Eu sei que você não aceitou minha proposta, mas você não precisa ser meu inimigo."
            else:


                h "Você aceitou lutar do meu lado, então eu te vejo como um companheiro."

            mc "Minha intenção não é te ferrar, [h]. Eu só quero que você me explique essa porra toda."

    h "Tudo bem. Eu vou meio repetir o que eu disse no fliperama. Senta aqui."

    mc surpreso "A-aí?!"

    h "A gente já tá ferrado mesmo. Vão perguntar o que a gente tá conversando, grande coisa a agente sentar aqui."

    mc envergonhado "O-ok."

    scene no2_conversa2 with Dissolve(1.0)

    pause

    h "Só cuidado pras câmeras não filmarem sua boca. Elas ficam ali."

    mc "Ah. Pode deixar."

    h "Certo. Eu tô aqui pra ficar de olho no [gi] e no NBC. A prefeitura tá cheia de gente que acha que manda na cidade."

    mc "Eu lembro que você falou. Mas nossa cidade é super boa. Não é isso que importa? Será que o prefeito é tão corrupto assim?"

    h "A cidade não é tão ruim, é isso que você quer dizer. Realmente, tem emprego e a taxa de pobreza é menor que a média."

    h "Mas isso é o suficiente? Com o dinheiro que a gente tem, tudo poderia ser melhor."

    menu:
        "Acho que você tem razão.":


            $ hacker_amizade += 2

            mc "Acho que você tá certa. A gente não pode se contentar com pouco. Esses caras têm a obrigação de fazer o melhor possível."

            h "Vai muito além disso inclusive. Eles tão lá pra servir o povo e não eles mesmos. Enquanto a gente não fizer nada, eles só vão continuar."
        "Você não quer demais não?":


            $ hacker_amizade += 1

            mc "Tudo pode ser melhor. Querer que seja tudo perfeito parece um pouco inocente demais."

            h "Não interessa. Eu não vou ficar esperando eles fazerem o que querem e me darem migalhas. Se você tá contente com isso, azar o seu."
        "Eu não me interesso por política.":


            mc "Sendo bem sincero, não tô nem aí pra política."

            h "Então eu tenho dó de você. A política tá aí decidindo tudo o que acontece com você. Só ignorar tudo é coisa de criança."

    mc "Tudo bem, mas por que você entrou nessa? Por que aguentar o [gi] por isso?"

    h "Por quê? V-você acha que eu quero ser tipo uma Joana d'Arc do século XXI? Que eu tô brincando aqui?"

    mc "Eu não disse nada disso. Eu tô justamente tentando entender."

    h "E o que isso tem a ver com você? Meus motivos."

    mc "Sei lá. Eu só quero saber."

    h "..."

    scene no2_conversa3 with Dissolve(1.0)

    pause

    h "O que eu sei é que você é xereto mesmo. Tá na profissão certa."

    menu:
        "Você é jovem, gata... por que gastar a vida assim?":


            $ hacker_amizade += 1

            mc "Você é linda, sexy, e tá perdendo seus dias sendo escrava desse idiota. Tem muita coisa melhor pra você viver, Nona!"

            h "Idiota... cala a boca que vão te ouvir."

            mc "Ops..."

            h "Eu sei o que eu faço, [mc]. Você precisa ficar esperto com as SUAS coisas."
        "Obrigado. Mas a pergunta continua.":


            mc "Obrigado por validar minha posição profissional, mas ainda quero saber o que tem nisso pra você."

            h "Não interessa, [mc]. Me deixa. Mesmo que a gente fosse amigos, sei lá se eu ia te responder isso."

            mc "Por quê? Será que nem você sabe direito?"

            h "..."

    mc "Tá, entendi. Mas é que eu me preocupo um pouco com você. Queria sair com você em outras condições."

    h "Você às vezes parece inteligente, mas tem vez que é... tipo... bem simplório mesmo. Parece que sua cabecinha tem o tamanho de uma caixinha de fósforo."

    mc "Valeu, mas isso nem existe mais..."

    h "Não vou aqui falar que você tá errado. A vida realmente pode ser um pouco mais fácil se você só deixar ela correr."

    h "Nem sei por que eu tô falando isso pra você, mas às vezes eu penso como a vida seria se eu só abandonasse tudo isso."

    mc "É isso que eu tô falando, garota!"

    h "Mas isso não é pra mim. Sei lá... eu sou inteligente demais pra esse tipo de coisa, sabe?"

    mc "Humildade tá batendo no teto..."

    h "É sério. Se eu quisesse ganhar dinheiro, seria muito fácil. Mas uma vida comum... acho que isso só não é pra mim."

    mc "Acho que você nem sabe isso. Precisa pelo menos dar uma chance. Se você quiser, eu te ajudo."

    h "Você é tão normal que consegue passar essa normalidade pros outros? É isso?"

    mc "Não! Quero dizer que a gente pode fazer uma coisa normal um dia."

    h "Tá me chamando pra um encontro?"

    mc "É..."

    h "[mc], levanta."

    mc "Opa."

    scene no2_conversa4 with Dissolve(1.0)

    h "Eu agradeço por você querer que eu seja feliz e normal, mas isso não é só sobre mim."

    h "Eu já disse pra você que tem outras pessoas que dependem do que eu faço aqui. É uma coisa importante."

    h "Quem sabe quando um dia a cidade estiver livre desses parasitas a gente possa fazer alguma coisa."

    mc angustiado "Mas isso vai ser nunca!"

    h "Você não confia em mim e nos meus amigos?"

    mc preocupado "..."

    h "Eu sei que parece impossível... eu sei disso."

    if nona_aceitou:

        h "E você também aceitou entrar nessa com a gente. Com você ajudando a gente, temos mais chance."

    h "Se a gente se esforçar, a gente vai conseguir. A gente não pode só fechar os olhos e viver nossa vida."

    h "Pra mim, é fácil doar dinheiro quando a gente tem sobrando. Esses ricos aí que doam 1%% do que eles têm... isso não vale nada."

    h "Eu não vou ser igual eles. Não vou dar o que eu tenho de sobra."

    mc desculpa "Puxa..."

    menu:
        "Você tá perdendo sua vida por nada.":


            mc desculpa "Ainda acho que você tá jogando uma parte da sua vida fora, mas a vida é sua."

            h "Obrigada pela preocupação, mas eu sei o que eu tô fazendo."
        "Até que essa cabeça dura é meio sexy.":


            $ hacker_amizade += 1

            mc charmoso "Não dá pra negar que essa sua cabeça dura é até meio sexy."

            h "Você sabe que falar que a cabeça dura de alguém é sexy tem vários significados, né?"

            mc zerado "Ei..."

            h "É um paspalho mesmo."

    h "Upa."

    scene banco_visao with Dissolve(1.0)

    h "Nossa. Agora a gente tá atrasado de verdade."

    label nona_e2_conversa:

        h "Vamos adiantar nosso passeio. Eu vou pular a parte chata e vamos pro interessante de uma vez."

        mc envergonhado "Ok."

    scene no2_conversa5 with Dissolve(1.0)

    pause

    h "Esta é uma área restrita. É depois daqui que fica a sala de segurança e depois o dinheiro."

    mc surpreso "A g-gente vai entrar aí?!"

    h "Claro, [mc]. Eu quero que você veja tudo."

    h "O NBC além de checar todas as transações públicas municipais, ele também serve como fomentador."

    mc desconfiado "Que quer dizer..."

    h "Nós emprestamos dinheiro para a sociedade. Toda essa área de atendimento é pra receber donos de pequenos, médios e grandes negócios."

    h "Às vezes um empresário precisa de dinheiro para movimentar seu negócio. Nós emprestamos com um juros bem abaixo dos bancos privados."

    mc normal "Parece bem interessante."

    h "Com certeza."

    scene no2_conversa6 with Dissolve(1.0)

    h "A partir daqui eu preciso de sua total discrição e cuidado. Igual eu disse, é uma área restrita que o senhor [gi] está liberando especialmente pra você."

    mc normal "Pode deixar."

    "Não tô entendendo qual a necessidade de eu entrar nessa área. E o pior nem é isso."

    "O que eu tô fazendo aqui? A [h], digo, a Nona nem trabalha aqui de verdade. Por que ela tá preocupada com o que eu penso do lugar?"

    "Será que ela tá fazendo tudo isso pelo [gi]? O que ela quer de verdade? E qual é a dele também? Por que essa visita?"

    "Tenho certeza que tem alguma coisa aqui que não tá batendo e eu tô ficando nervoso com isso."

    h "[mc]? Tá me ouvindo?"

    mc surpreso "A-ah! S-sim!"

    h "Você apaga bem na hora que eu peço pra você prestar atenção?"

    mc envergonhado "Talvez eu só estivesse prestando atenção demais."

    h "Vamos."

    "Doideira."

    scene black with Dissolve(1.0)

    h "Depois desta porta fica o corredor que vai para o cofre."

    mc surpreso "O cofre?!"

    h "Só que antes eu quero que você veja uma outra sala. Por aqui."

    "..."

    scene no2_monitores1 with Dissolve(2.0)

    pause

    h "Esta é a sala dos monitores. É de onde os policiais acompanham o movimento na entrada do cofre."

    mc charmoso "Caraca, bem massa."

    "Policial" "Boa tarde, senhorita [h]."

    h "Oi! Você tá trabalhando aqui hoje?"

    po "Sim. A prefeitura me remanejou pra cá. Eu vou ajudar vocês com o passeio do senhor [mc]."

    h "Ah! Que bacana!"

    mc normal "Obrigado."

    h "Depois vamos explicar melhor, [mc], mas aqui é o máximo que chegamos perto do cofre, né?"

    po "Isso. Todo o sistema é controlado remotamente. Ele tem uma trava manual também, mas nunca foi usada."

    h "As câmeras dão toda a visão que a segurança precisa para garantir que nada de errado está acontecendo."

    po "Isso é importante, porque olha, nenhum criminoso pode fazer alguém de refém. A gente fica protegido aqui."

    po "E ninguém pode entrar aqui também."

    h "É verdade. Este é um caso especial. Vai ser rápido e é apenas pra você entender tudo."

    mc envergonhado "Caraca, vocês realmente tão se esforçando por mim. Valeu."

    h "Queremos que você veja tudo o que é possível e fique tranquilo da segurança e idoneidade do nosso trabalho."

    h "Eu quero que você veja as câmeras agora. É um pouco apertado, mas cabe.{w} Vem por aq-{nw}"

    scene no2_monitores2 with vpunch

    pause

    h "AAAH!"

    mc surpreso "N-nonaa!"

    po "S-senhorita!"

    h "AI! Tô bem, tô bem!"

    mc preocupado "Certeza?"

    po "A senhorita precisa de ajuda?"

    scene no2_monitores3 with Dissolve(1.0)

    h "Não. Eu tô legal. Obrigada vocês dois."

    h "Por favor, mostre pro [mc] como as câmeras funcionam enquanto eu me ajeito."

    po "P-pode deixar."

    po "Então, senhor. Pode olhar aqui nas câmeras que você vai ver como funciona."

    "Nossa, a Nona tomou um tombão cabuloso agora. Tadinha..."

    mc normal "Opa. Deixa eu dar uma olhada."

    po "Olha pra este monitor aqui primeiro."

    scene no2_monitores4 with Dissolve(1.0)

    pause

    po "Essa visão é da câmera 2. Ela fica bem ao lado da porta."

    show black with Dissolve(0.3)

    hide black with Dissolve(0.3)

    "Opa. Parece que deu uma piscada."

    po "Dá pra ver que qualquer coisa que acontecer ali a gente vai ficar de olho. É impossível a gente não ver."

    po "A outra câmera mostra a chegada na sala, então a gente tem visão de todos os ângulos. Não existe um ponto cego."

    mc "Parece bem seguro mesmo."

    po "É coisa de primeira linha."

    po "Agora olha aqui."

    scene no2_monitores5 with Dissolve(1.0)

    pause

    po "Esta é a câmera que tem dentro do cofre. Dá pra ver em tempo real tudo o que acontece lá dentro."

    mc "Essas gavetas... por que tem números nelas?"

    h "As gavetas também estão conectadas na rede. Elas são abertas eletronicamente."

    po "Isso. É tudo automático hoje em dia."

    mc "E os números?"

    h "Ah! São só identificação mesmo. Aqui não é igual nos filmes que cada cliente tem sua gaveta pra guardar coisas."

    mc "Já era o que eu tava pensando haha..."

    h "Não, não. O NBC não é esse tipo de banco. Mas mesmo assim usamos o sistema de identificação por gavetas."

    h "A maioria delas tem dinheiro, mas não é só dinheiro também. Elas guardam documentos, objetos e várias outras coisas."

    mc "E é tudo do banco?"

    h "Na verdade, não. Pelo fato do NBC ser muito bem protegido, membros do poder público acabam guardando coisas aqui também."

    h "É mais seguro deixar aqui do que na própria prefeitura ou na câmara. Como tudo é do município, tanto faz."

    mc "Entendi."

    h "Bom, acho que era isso, certo?"

    po "Sim. Agora vamos pra sala do cofre."

    h "O cofre é nossa última parada."

    scene black with Dissolve(1.0)

    h "Por este lado, [mc]."

    mc normal "Opa."

    h "Chegamos."

    scene no2_cofre1 with Dissolve(2.0)

    pause

    mc normal "Orra, é maior do que parecia nas câmeras."

    h "Eu pensei a mesma coisa da primeira vez."

    po "Acho que todo mundo por isso aqui."

    mc "Aquela câmera na direita é a câmera 2 que a gente tinha visto lá na sala dos monitores."

    po "Essa mesmo."

    po "Venham mais perto."

    scene no2_cofre2 with Dissolve(1.0)

    pause

    mc desconfiado "Então quer dizer que não fica ninguém protegendo o cofre aqui."

    po "Não. A gente da guarda municipal que faz a proteção, só que a gente vai até a sala dos monitores."

    po "Se alguém tentar alguma coisa, ele vai aparecer na câmera e daí tomamos as providências. Mas até hoje nunca tentou nada."

    mc charmoso "Deve dar medo mesmo."

    h "Será que você pode nos mostrar como funciona a tranca?"

    po "Claro, se aproximem."

    scene no2_cofre3 with Dissolve(1.0)

    pause

    h "Até eu me interessei. Nunca soube como funciona isso."

    po "É até bem simples. Tão vendo estas três rodas aqui? Você precisa acertar a sequência."

    h "Então é só girar?"

    po "Isso. Elas são extremamente leves. Até você aguentaria, senhorita [h]."

    h "Você tá me chamando de fraca?"

    po "N-não! É como um elogio. A s-senhorita é uma figura bem f-feminina!"

    h "Ok..."

    mc envergonhado "..."

    mc "É... e quem tem a senha?"

    scene no2_cofre4 with Dissolve(1.0)

    pause

    po "Apenas o diretor financeiro e outros diretores têm esse acesso."

    po "O segredo é trocado todos os dias. Eles recebem essa nova senha todos os dias logo cedo."

    mc normal "Interessante. Parece até coisa de filme."

    h "Agora. O que acontece se alguém tentar abrir e errar?"

    po "Isso eu nunca vi acontecendo. Mas pelo que eu sei, a porta é travada até o próximo reset."

    mc desconfiado "Que acontece todos os dias logo cedo?"

    po "Isso. Ela fica presa até ser gerada uma nova senha no dia seguinte."

    h "Só errar uma vez?"

    po "Sim, errar uma vez já trava tudo."

    mc charmoso "É realmente bem complicado roubar vocês."

    po "Bota complicado nisso. Por isso ninguém nunca nem tentou. Sorte desses ladrões, porque com certeza seriam pegos."

    scene no2_cofre5 with Dissolve(1.0)

    h "Bom, acho que é isso que precisávamos saber. Obrigada."

    po "Eu posso ficar aqui com vocês se vo-"

    h "Eu agradeço, mas acho que vimos tudo o que precisávamos, certo, [mc]?"

    menu:
        "A gente não pode ver dentro do cofre?":


            mc tarado "A gente não pode ver DENTRO do cofre?"

            h "Que pergunta é esse, senhor [mc]?"

            po "Haha. Infelizmente essa vamos ficar devendo senhor."

            mc envergonhado "Tô brincando."
        "Sim. Mais do que eu imaginava.":


            $ hacker_amizade += 1

            mc normal "Curti muito conhecer essa área aqui. Foi mais que o suficiente."

            po "Legal."

            h "Que bom que você gostou."

    h "Então pode voltar para os monitores que já vamos saindo em seguida, ok?"

    po "Combinado."

    h "Nem vou passar pela sala. Vou levar ele direto pra fora."

    po "Tá certo. Vou tá de olho nas câmeras. Até outro dia, senhorita [h]."

    h "Ah! E manda um alô pra [na] lá na prefeitura. Faz tanto tempo que não vejo ela."

    po "Pode deixar. Ela é meio na dela, mas vou tentar passar seu recado."

    h "Ela é assim mesmo. Se não der tudo bem. Até outro dia."

    scene black with Dissolve(1.0)

    scene no2_cofre6 with Dissolve(1.0)

    pause

    h "E então? Chegamos ao fim. O que achou?"

    "É. Meio que acabou rápido o passeio. Mas não imaginei que a gente realmente viria até o cofre. Tô meio me sentindo o Brad Pitt."

    menu:
        "Foi interessante, mas nem tanto.":


            mc envergonhado "É algo que eu nunca tinha visto, mas era meio esperado, né? Cofre, banco, seguranças..."

            h "É. Acredito que você tenha razão mesmo. Talvez eu tenha vendido o peixe caro demais."

            mc "..."
        "Eu curti bastante. Mais do que imaginava.":


            $ hacker_amizade += 1

            mc normal "Não pensei que a gente chegaria até aqui. Fiquei bem impressionado em como tudo funciona."

            mc "Vou ser honesto e admitir que eu esperava menos."

            h "Que bom. Achei mesmo que você ia se surpreender."

    h "Mas nosso passeio ainda não acabou. Tenho uma última surpresa pra você."

    mc normal "O quê?"

    h "Antes de tudo, quero que você saiba que tudo vai ficar bem."

    mc desconfiado "Hm?"

    if nona_aceitou:

        h "Você disse lá no fliperama que ia me ajudar, certo?"

        mc "S-sim..."

        h "Você ainda pretende ajudar a gente?"

        menu:
            "Sim. Pode contar comigo.":


                $ hacker_amizade += 2

                if renpy.variant("mobile"):
                    $ renpy.block_rollback()

                mc charmoso "Sim. Pode contar comigo."

                h "Muito bem. Que eu vou precisar de uma coisinha de você hoje."
            "Com a pauta, mas só isso.":


                if renpy.variant("mobile"):
                    $ renpy.block_rollback()

                mc charmoso "Eu disse que iria ajudar com a pauta."

                h "Uma pena... é que eu queria só te pedir um outro favor."
    else:


        h "Lá no fliperama você não aceitou me ajudar com a pauta... eu fiquei bem decepcionada."

        mc envergonhado "Você entende que não é pessoal, né? Eu só não quero me meter com as pessoas erradas."

        h "Eu entendo. É que eu queria te pedir uma outra coisinha hoje."

    mc desconfiado "O quê?"

    h "Não me odeie. Com licença.{nw}"

    scene no2_cofre7 with vpunch

    pause

    "Q-quê?!"

    mc "Akh!"

    scene black with dissolve

    scene no2_cofre8 with Dissolve(1.0)

    pause

    h "Isso vai te apagar por uns minutos. É tudo o que eu preciso de você."

    mc "N-no..."

    scene black with dissolve

    scene no2_cofre9 with Dissolve(1.0)

    pause

    h "Adeus, [mc]."

    mc "N-nã-"

    scene black with Dissolve(3.0)

    "{cps=5}................{/cps}"

    "Ai... o que acont-"

    scene black with dissolve

    scene no2_cofre10 with vpunch

    pause

    mc "N-nona!"

    "Que merda aconteceu? Pera... Ela me bateu!"

    "E o que eu tô fazendo aqui? O c-cofre! Tá aberto?! Por que o caralho do cofre da aberto?!"

    "Meu Deus... tá tudo uma bagunça. E cadê a Nona?"

    mc "C-carla? Oi?"

    "Será que ela que fez tudo isso? Quanto tempo eu apaguei? Acho que não foi muito. Ela deve tá aqui dentro ainda."

    scene black with dissolve

    "Olha só pra isso..."

    scene no2_cofre11 with Dissolve(1.0)

    pause

    mc "Todo esse dinheiro..."

    "Só pode ter sido a Nona. Mas o que eu tenho a ver com isso? Por que eu tô aqui?"

    "Será que eu posso pegar esse dinheiro pra mim?"

    "Você tá louco, [mc]?! Você não fez nada de errado! Se você tocar em qualquer coisa aqui..."

    "Mas é tanto dinheiro... se algumas notas sumirem quem vai perceber?"

    "S-será?"

    menu:
        "Pegar algumas notas de 100 espalhadas.":


            if renpy.variant("mobile"):
                $ renpy.block_rollback()

            "Acho que ninguém vai sentir falta disso aqui."

            "Vou pegar só algumas e esconder essa aqui{nw}"
        "Não tocar em nada.":


            if renpy.variant("mobile"):
                $ renpy.block_rollback()

            "Melhor não mexer em nada. Eles não podem provar que eu fiz qualquer coisa."

            "Mas se minhas digitais estiverem aqui, eu tô ferr-"

    scene no2_cofre12 with hpunch

    pause

    po "Você! Parado!"

    mc "E-eu!"

    po "Desde quando?! O que tá acontecendo aqui?!"

    mc "Eu s-"

    po "Eu disse PARADO!"

    mc "Eu não tenho nada a ver com is-"

    scene no2_cofre13 with hpunch

    pause

    po "Eu mandei você não se mover!"

    mc "AAAARGH!"

    menu:
        "Não tenho nada a ver com isso!":


            mc "Eu não tenho na-"

            po "QUIETO! Você será detido por tentativa de furto!"

            mc "NÃ- AAARRGH! Tá machucando!"
        "Melhor eu ficar quieto.":


            mc "Ugh..."

            po "Você vai responder por tentativa de furto de bem público."

    po "Você vai ter que explicar como conseguiu abrir o cofre!"

    po "Atenção! Preciso de reforços!"

    mc "E-eu não consigo respirar direito!"

    po "Esse é o menor dos seus problemas, ladrão!"

    scene black with vpunch

    mc "Não!"

    "Guarda" "Você vai ficar aqui até descobrirmos tudo!"

    scene no2_prisao1 with hpunch

    pause

    mc "Mas eu não fiz nada!"

    "Como as coisas acabaram assim?! Por que eu tô aqui!?"

    "Parece que passou nem cinco minutos... que merda... como assim, mano?!"

    $ h_nome = "Nona"

    "Eu tava fazendo um passeio pelo banco. Daí do nada a [h] me bateu e eu apaguei."

    "Eu acho que fiquei, sei lá, 2 minutos apagado e quando eu acordei já tava a porta do cofre aberta e aquela bagunça."

    "Como que o cara desmaiado virou culpado?"

    "Só pode ter sido a [h]. Isso é certeza. Ela deve ter planejado tudo pra jogar a culpa em mim."

    "Mas como que ela conseguiu abrir o cofre? Ela fez isso só no tempo que eu apaguei?"

    "Será que eu fiquei capotado mais tempo? E se passou uma hora? Impossível... foi tão rápido."

    "Saco..."

    scene no2_prisao2 with Dissolve(1.0)

    pause

    "Eu tô fodido. Minha vida vai acabar."

    "Tudo o que eu avancei com a [c] e todas as outras..."

    if priscila_namoro or sayuri_namoro or julia_namoro or maria_namoro or nathan_namoro:

        "E bem agora que eu tô namorando..."

    "Minha vida mudou tanto nos últimos meses. Mas vir pra prisão vai ferrar tudo isso."

    "Claro que o chefe vai me mandar embora. Quem vai acreditar em mim depois disso?"

    "Será que querer conhecer um monte de garotas interessantes e lindas precisa ter um preço?"

    "E o preço é perder minha própria liberdade? Como um ritual satânico? Vendendo minha alma..."

    "[mc]... faz cinco minutos que você tá preso e já tá pensando merda. Só cala a boca."

    po "Ei!"

    mc "Hm?"

    po "Vem aqui, ladrãozinho."

    scene no2_prisao3 with Dissolve(1.0)

    pause

    menu:
        "Ladrão é o caralho!":


            mc "Ei! Ladrão é o caralho! Não fale o que você não sabe!"

            po "Você vai falar assim com um policial mesmo?! Você é louco, ladrão?!"

            mc "Eu já falei que eu não sou ladrão!"

            po "Continue repetindo isso, talvez você acredite mesmo um dia."
        "Eu não roubei nada.":


            mc "Eu não roubei nada. Não fui eu que abriu a porta do cofre."

            po "Isso você vai ter que explicar direitinho pro delegado."

            mc "Eu explico. Não tenho nada pra esconder."

            po "Haha..."
        "...":


            mc "..."

            po "Não gostou? Tá com medo da prisão, é, ladrão?"

    mc "Tá bom. Mas o que vai acontecer comigo agora?"

    po "É meio óbvio, né? Estão investigando o que você fez lá no banco."

    po "Você pode até ter essa cara de idiota, mas não me engana."

    mc "Tadinho de mim querer roubar um lugar desse. Vocês tão me dando muita moral."

    po "Pode ser. Mas eu já vi muitas pessoas que você não dá nada serem grandes gênios do crime."

    po "Às vezes são os mais submissos, os quietinhos, que tão sempre pensando no que vão fazer."

    mc "Vocês tão com meus documentos, né? Eu sou paparazzo da revista da ilha."

    po "Hmmm... então você é famoso."

    scene no2_prisao4 with Dissolve(1.0)

    po "Vai ser mais legal ainda. Seu nome vai sair no meio da matéria e não no crédito."

    mc "Isso é muito sem noção."

    po "O delegado e quem tá investigando é que vão decidir isso."

    mc "Mas quanto tempo eu vou ficar aqui?"

    po "Mano, faz 10 minutos que você chegou aqui. Tem um pouco de paciência, tá bom?"

    po "Talvez você fique dias aqui. Semanas dependendo do caso."

    mc "Semanas?! I-isso é impossível!"

    po "Da próxima vez você não rouba um banco. Ou é inteligente suficiente pra não ser pego."

    mc "Mas eu n-"

    po "Cala a boca. Para de falar a m-"

    "???" "[po]! Cale o senhor a sua boca!"

    po "Hm?! Quem você pensa que é?!"

    scene no2_prisao5 with hpunch

    eli "Quem você pensa que eu sou?!"

    po "J-juíza Richter! O-o que a Vossa Exelência faz aqui?!"

    if v20_fim:

        "Essa mulher... a juíza do caso do [n]... O que ela tá fazendo aqui?!"

    eli "Recebi uma ligação falando que tentaram roubar o NBC! Esse homem é quem estava no lugar?"

    po "Isso mesmo."

    eli "Essa história está muito mal contada, oficial. Eu já falei com o delegado, eu quero que você solte ele agora mesmo."

    mc surpreso "Q-quê?!"

    po "Como assim, senhora?!"

    eli "Você não ouviu?!"

    po "Mas-"

    scene no2_prisao6 with Dissolve(1.0)

    pause

    eli "Vocês não podem manter ele preso dessa forma. Não sob meu olhar."

    po "Senhora... ele é o único suspeito."

    eli "Olhe para a expressão desse sujeito, policial. Ele não passa de um desafortunado. Um coitado que tava no lugar errado na hora errada."

    eli "Eu já expliquei para o delegado que ele poderá trazê-lo para depor caso seja necessário, mas não prendê-lo de forma indefinida."

    po "Mas e se ele fugir?! Isso é um absurdo!"

    eli "Não entendo de onde vem tanta coragem para levantar sua voz dessa forma."

    po "P-perdão, Vossa Excelência."

    eli "Agora seja um bom garoto e libere o homem. Eu e o delegado checamos os registros. Ele não tem nenhuma passagem."

    po "Mas eu nunca vi a senhora aqui fazendo isso antes. Por que dessa vez?"

    eli "Você realmente quer que ele escreva sobre nossa força policial na revista dele?"

    eli "Mantido em prisão sem qualquer convicção dos investigadores?"

    po "..."

    eli "Não me faça repetir. Obedeça."

    po "S-sim, senhora..."

    eli "Venha. Vamos pegar suas coisas e sair daqui."

    mc "O-ok..."

    scene no2_prisao7 with Dissolve(1.0)

    pause

    mc "Senhora..."

    eli "Diga."

    mc "Você pode me falar uma coisa?"

    eli "Se você me pedir com jeito, talvez."

    mc "A s-senhora pode, por favor, me responder um negócio?"

    eli "Pergunte."

    mc "Por que a senhora veio me ajudar?"

    if v20_fim and not juiza_fotos:

        eli "Talvez pelos velhos tempos."

        mc "S-sei..."

        eli "Eu adoro ter um garotinho me devendo uma. Você sabe quem te tirou daqui, né?"

        mc "A s-senhora..."

        eli "Muito bem. Não esqueça disso."

        mc "T-tá..."

    elif juiza_fotos:

        eli "Eu ainda não esqueci que você tentou me ameaçar aquela vez. Mas não é por você que eu estou aqui."

        mc "Não?"

        eli "Isso não interessa, garoto. Saiba que você é muito pequeno perante isso tudo."

        eli "Cale sua boca, entenda seu lugar, e agradeça."

        mc "..."
    else:


        eli "Não é por você que eu estou aqui."

        mc "Não?"

        eli "Claro que não. Saiba que você é muito pequeno perante isso tudo."

        eli "Quanto antes você entender seu lugar melhor para você."

        mc "Certo..."

    eli "Vamos pegar suas coisas."

    if nona_aceitou:

        eli "Você ainda tem um compromisso hoje à noite."

        mc "Compromisso? Qual compromisso?"

        eli "Alguém quer falar com você. O motorista vai te deixar lá."
    else:


        eli "Ainda não sei por que se preocupam tanto com você, mas me pediram para te deixar na ilha."

        eli "O motorista vai te deixar lá e você se vira."

        mc "Ok. Mas-"

    eli "Agora pare de fazer perguntas e vamos. Eu gosto de garotos comportados."

    mc "..."

    scene black with Dissolve(1.0)

    if not nona_aceitou:

        "..."

        "Motorista" "Aqui está bom para o senhor?"

        mc serio "Sim. Consigo chegar à pé."

        "Motorista" "Perfeito. Pode sair."

        mc "V-valeu."

        jump nona_e2_final
    else:


        "..."

        "Motorista" "Chegamos."

        mc serio "Que lugar é esse aqui?"

        "Motorista" "Suba até o décimo segundo andar. Apartamento 124. Só isso."

        mc desconfiado "O-ok..."

        "Motorista" "A porta está aberta. Agora vai."

        "..."

    "O que será que tá rolando aqui? Que lugar é esse?"

    "Eu tô com um frio na barriga. Um negócio estranho..."

    mc preocupado "124... é esse aqui."

    "Tô com medo. Será que vale à pena entrar aqui?"

    "Talvez o melhor seja só eu dar o fora e ir pra casa. Tudo isso tá estranho demais."

    "Bosta! O que eu faço?!"

    menu:
        "Dar meia volta e ir pra casa":


            "É melhor eu dar o fora daqui. Isso aqui é perigoso demais."

            "Vou pegar o ônibus e voltar pra ilha."

            "..."

            scene mc onibus_noite with Dissolve(1.0)

            "Sem dúvidas esse foi um dos dias mais loucos da minha vida."

            "..."

            jump nona_e2_final
        "Abrir a porta e entrar":


            $ no2_ape = True

            mc serio "Agora não tem mais volta. Tenho que saber que merda que foi toda essa hoje."

            "Certeza que quem me chamou aqui tem tudo a ver com isso."

            "Talvez o Gustav... alguém da máfia ou o velho da Faux..."

            "Eu sei que é alguém que quer me foder."

            "..."

            "A porta tá aberta."

    scene no2_ape1 with Dissolve(1.0)

    pause

    mc surpreso "!"

    h "Chegou?"

    "Essas tatuagens..."

    mc "N-nona?!"

    h "A [eli] me falou que deu tudo certo. Eu pedi pra ela te mandar pra cá."

    menu:
        "Q-que tudo isso quer dizer?!":


            mc bravo "O que toda essa porra significa!?"

            h "Eu achei mesmo que você ia ficar bravo..."

            mc "Claro que eu fiquei! Eu fui parar na cadeia!"

            h "Tá, tá... mas já saiu."

            mc "E daí?! Por que tudo isso?! Achei que a gente fosse parceiros!"

            h "Foi por isso que eu falei pra você vir. Eu vou explicar."
        "A juíza trabalha com você?":


            $ hacker_amizade += 1

            mc desconfiado "Então quer dizer que a juíza trabalha com você?"

            h "Sim. A [eli] é uma das minhas amigas."

            mc envergonhado "Como pode..."

            h "Eu disse que não trabalhava sozinha. Foi pra isso que eu te chamei."

    h "Eu quero que não fique nada de errado entre a gente."

    mc desculpa "Meio difícil depois do que aconteceu hoje."

    scene no2_ape2 with Dissolve(1.0)

    pause

    h "Eu sei... você tem todo direito de ficar puto comigo."

    mc serio "Então foi você que planejou tudo isso?"

    h "Não."

    mc desconfiado "Não? Então quem?"

    h "Eu não faço nada sozinha, [mc]. Você ajudou muito a gente."

    mc desconfiado "Hm? Eu?"

    h "Mais do que você imagina."

    mc envergonhado "Sei lá. Acho que perdi alguma coisa."

    h "É mais fácil do que pode tá parecendo. É só você pensar com calma."

    h "A matéria sobre o aeroporo, a preocupação do [gi], o passeio, a sala dos monitores..."

    mc "Você quer dizer que tudo isso foi planejado? Desde aquele encontro no fliperama?"

    scene no2_ape3 with Dissolve(1.0)

    pause

    h "Meus amigos são incríveis, não são?"

    menu:
        "Acho que você devia ME agradecer depois de hoje.":


            $ hacker_amizade += 2

            mc charmoso "O que eu acho é que depois de hoje você tinha que ME agradecer."

            h "C-com certeza. E não foi só por hoje, [mc]. Você ajuda a gente por um bom tempo."

            h "Eu sabia que você ia ser muito importante pra gente."

            h "Desculpa se eu não te contei tudo, mas você não podia negar. A gente foi pelo mais certo."

            mc envergonhado "Com certeza eu não ia aceitar se eu soubesse o que ia rolar hoje."

            h "Acho que ninguém ia aceitar. Por isso eu não falei nada."
        "Eu acho vocês uns pau no cú.":


            mc serio "Vocês são uns filhos da puta, isso sim."

            mc "Usar as pessoas desse jeito. E olha que eu disse que ia te ajudar. Imagina se a gente fosse inimigos."

            h "Eu sei... mas se eu tivesse te falado você ia ajudar mesmo assim?"

            mc zerado "Óbvio que não."

            h "Haha... você é sincero mesmo."

            mc "Quem vai ser preso pelos outros?"

    h "Eu sei que a gente pediu demais de você. Mas isso envolvia muita coisa."

    mc envergonhado "Ok... que seja. Só espero que isso não volte pra me ferrar mais pra frente."

    h "A [eli] vai proteger você. Nada deve acontecer."

    mc normal "Certeza?"

    h "Não, mas provavelmente vai."

    mc zerado "Bom saber..."

    scene no2_ape4 with Dissolve(1.0)

    h "Foi pra isso que eu te chamei aqui... pra pedir que a gente continue sendo amigos."

    mc serio "Depois de hoje?"

    h "Sim. Você entendeu? Eu já te expliquei! As coisas tinham que acontecer assim. Se você se negasse iria tudo pro saco."

    h "Esse plano envolvia muito tempo, muitas pessoas. Você disse que ia me ajudar!"

    mc desculpa "Sem comentários, [h]. É impossível você achar que isso tá certo. Usar uma pessoa assim."

    h "Mas a gente tinha que faz-"

    mc bravo "NONA! Escuta!"

    h "?!"

    mc "Não me interessa seu plano e dos seus AMIGOS. Foda-se. Em algum momento você perguntou o que EU queria?"

    h "N-não..."

    mc "Colocar as pessoas no seu rolo não tá certo. Não importa o quão importante você ache que ele é."

    mc desculpa "Cada um tem suas coisas. E daí se você quer salvar o mundo? Talvez eu queira só beijar alguém e curtir a vida."

    mc "Usar alguém só porque você acha que seu objetivo é 'maior' ou 'melhor', é uma baita desumildade."

    h "[mc]..."

    mc concentrando "Espero que você entenda isso..."

    h "É que..."

    mc desculpa "Que foi?"

    h "Essa palavra 'desumildade' não existe."

    mc zerado "Foi nisso que você prestou atenção? Você tem problema?"

    h "..."

    mc desculpa "Você podia pelo menos me contar o que tá rolando, né?"

    $ renpy.notify("Nona está lembrando das suas ações...")

    h "N-não sei... não sei se eu posso..."

    mc "Será que eu não mereço depois de hoje?"

    h "Isso..."

    mc desculpa "Se você realmente espera contar comigo pra qualquer outra loucura, acho bom você falar."

    h "..."

    h "Tá."

    scene no2_ape5 with Dissolve(1.0)

    pause

    h "Eu falei que essa cidade é podre, né? Esses prédios todos cheio de luz é pra esconder a merda que tem nas bibocas."

    h "Não me vem com taxa de pobreza e o caralho. Eu não acredito nesses dados tudo forjado. Você nunca assistiu Tropa de Elite?"

    h "O que eu sei é que tem gente morrendo no hospital bosta, sem comida, e o caralho. Tudo isso porque uns aí querem tudo pra eles."

    mc desculpa "E o que a gente vai fazer? Botar fogo em tudo?"

    h "Eu não respeito uma lei que não serve pra mim. Que só protege quem não precisa de proteção."

    h "Se eu pudesse eu colocava fogo nisso tudo mesmo."

    mc envergonhado "Metaforicamente, né? Né?"

    scene no2_ape6 with Dissolve(1.0)

    pause

    h "Às vezes eu olho pros prédios lá longe... tudo parece tão claro, tão feliz. Mas eu tô sozinha aqui."

    h "Daí eu olho pro outro lado, naquela parte escura, e tem um bêbado coberto de papelão morrendo de frio."

    h "Sabia que eu perguntei pra ele por que ele bebia?"

    mc "Por que ele bebia?"

    h "Porque quando ele tava bêbado ele sentia menos dor de ficar deitado no chão duro."

    mc desculpa "Que foda..."

    h "Sabe, [mc]. Acho que a gente esquece que tem gente se fodendo todo dia aí. Da nossa casa bonita e quentinha... como a gente vai lembrar?"

    h "Só quando a água molha nossa bunda que a gente lembra que esse mundo tá fodido."

    h "É quando uma coisa horrível acontece com alguém que a gente ama que a gente vê que tudo tá uma merda. Mas daí é meio tarde demais."

    mc desculpa "..."

    h "Eu sempre gostei da luz. Eu moro aqui por causa do neon, sabia? O cara que vivia aqui vendeu porque ele não aguentava mais a luz."

    h "Mas eu gosto dela. Eu me sinto bem."

    "Ela tá mó depressiva... o que eu falo?"

    menu:
        "Posso ver as luzes do seu lado aí na janela?":


            mc normal "Ei. Será que eu posso ver a janela aí também do seu lado?"

            h "..."
        "Não importa. Não pense demais nisso, [h].":


            mc desculpa "Olha, [h]. Eu sei que tudo isso parece fodido pra caramba, mas tente não pensar demais nisso."

            mc "O mundo é uma desgraça, mas é o que é. Ficar depressiva por isso não vai resolver nada."

            h "Acho que sim... Acho que você tá certo. Deixa eu sair daqui."

            jump nona_e2_pre_final

    if hacker_amizade >= 19:

        $ no2_especial = True

        h "Ah? P-pode..."

        h "Não sei se você vai achar elas assim tão legais... a-acho que eu exagero um pouco."

        mc charmoso "Tudo bem. Eu quero ver porque eu quero."

        h "T-tá."

        scene no2_ape7 with Dissolve(1.0)

        pause

        mc "É..."

        h "Você não precisa... é... falar nada, [mc]."

        mc "Eu sei. Calma. É o seguinte."

        mc "Tudo isso que você falou é super sério. E dá pra ver que isso é muito forte pra você."

        mc "Eu acho isso bem incrível. E tenho que falar que ver as luzes em você assim na janela... ficou bem poético."

        h "Poético? Q-que... bosta..."

        mc "Eu sei. Mas é qu-"

        h "Quem fala pra uma garota que ela é 'poética'?"

        mc "Espera, [h]. Foca no que eu tô falando. Esquece a palavra."

        h "Mas é que é meio quebra clima. Essa não é a palavra certa, [mc]."

        mc "Tá bom. Mas presta atenção."

        scene no2_ape8 with Dissolve(1.0)

        pause

        mc "Deve ser bem complicado passar o dia naquele banco com o idiota e depois voltar pra cá e ficar sozinha."

        h "Eu tô acostumada... n-não é nada de mais."

        mc "Eu quero ser seu amigo."

        h "Amigo? Eu já tenho amigos."

        mc "Não. Não quero ser um 'amigo de trabalho'. Não quero fazer uma missão louca com você de saque ao banco. Nem um mega plano contra o prefeito."

        mc "Eu só quero ser seu amigo. Quero que você me ligue quando tiver sozinha e me conte as merdas que o [gi] fez."

        h "M-mas... pra que isso?"

        mc "Você gosta de games?"

        h "S-sim... Mas faz tempo que eu não jogo."

        mc "E se a gente fosse no fliperama um dia desses? O perdedor paga um mega hamburguer pro outro."

        h "Eu não sou mais criança, [mc]... eu não quero jogar e comer hamburguer de graça..."

        mc "Certeza? Eu deixo até você escolher o jogo."

        scene no2_ape9 with Dissolve(1.0)

        pause

        h "V-vai ser fácil demais pra mim assim."

        mc "Eu também sou bem com games. Sempre que dá eu jogo."

        h "Não é só treinar, [mc]. Pra jogar você precisa ter reflexo e técnica. Uma competição envolve muito mais coisas."

        mc "Você tá me chamando de casual?"

        h "Claro que você é casual."

        mc "Então você topa? Melhor de três valendo um mega burguer premium no combo."

        h "F-fechad-{nw}"

        h "N-não! E por que você tá tão perto?!"

        scene black with vpunch

        h "Dá licença. Deixa eu sentar pra lá."

        mc "N-nona..."
    else:


        h "N-não. Acho melhor a gente parar por aqui. Desculpa."

        mc desculpa "Poxa..."

        h "Não fica pensando nisso. Eu só, sei lá. Passou."

    label nona_e2_pre_final:

        pass

    scene black with Dissolve(1.0)

    pause

    scene no2_ape10 with Dissolve(1.0)

    pause

    h "A gente ainda vai se ver, [mc]. A cidade é pequena. A ilha então... mais ainda."

    h "Você pode até curtir seu tempo lá. Aproveita as garotas, a fama da revista. Tem muita coisa legal por aí."

    h "Mas uma hora a coisa vai esquentar. Lembra que eu falei? Você vai ter que escolher qual é seu lugar nisso tudo."

    mc charmoso "Quando a hora chegar eu vejo o que eu faço."

    mc "Eu não cheguei aqui ontem. Você pode achar que tá aí na crista da onda, mas eu tenho chão aqui na capital."

    mc envergonhado "Eu vi muita coisa aqui. Mais do que eu queria ter visto até."

    h "Tomara que você ainda esteja com a gente na próxima."

    mc desculpa "Vamos ver... Tchau, [h]."





    h "Tá bom... até outro dia, [mc]."

    mc "..."



    label nona_e2_final:

        scene black with Dissolve(2.0)

    "..."

    mc "Ufa..."

    scene mc_ilha_polvo with Dissolve(1.0)

    pause

    if no2_evento:

        "Ainda não tô acreditando no que aconteceu hoje..."

        "Aquele passeio no banco. Mano! Eu fui até preso! E agora eu tô aqui... como se nada tivesse acontecido."

        "É duro saber o que essa merda de prisão vai afetar minhas coisas. Espero que ninguém fique sabendo."

        "Aquela juíza que ainda me tirou daquele jeito lá. Que porra foi aquela?"

        if no2_ape:

            "E depois sorte que eu fui pro apê com a [h]. Tudo tinha sido um plano dela e dos 'amigos' dela. Quem será que são esses?"

            "Eu sei que a juíza doida é um deles. Mas deve ter mais. Pessoas malucas que nem ela que estão por trás da [h]."

            "Planejar um assalto a banco daquele jeito não é fácil. Certeza que tem gente pesada nesse meio aí."

            "Preciso pensar sobre isso... descobrir quem faz parte desse grupo e o que eles querem."

            if no2_especial:

                "E depois na janela... a conversa acabou indo pra outro lado."

                "Dá pra ver que tem alguma coisa errada com a [h]. Ela tava super triste lá olhando pra cidade."

                "Eu queria poder fazer algo por ela. Dá uma aliviada nessa coisa pesada que parece que ela sente."

                "Quem sabe... a gente até..."

                mc "Quem sabe..."

                "O problema é tudo isso que ela tá metida."

        "Nem quero pensar na próxima que essa maluca vai inventar."

        mc "Onde você se meteu, [mc]?"
    else:


        "Acho que eu fiz o certo não indo naquele banco. Essa Nona é doida pra caramba. E eu lá quero coisa com essa mina?"

        "Ela tá numa briga com esses cabeças da ilha e certeza que ela ia me meter nessa furada também."

        "Vou ficar na minha e curtir o que a cidade tem. Vou me aliar com as pessoas que realmente têm poder aqui."

        "A vida é boa."



    $ v38_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v38_fim","final","local")

    scene black with Dissolve(3.0)

    call checa_final from _call_checa_final_13

    jump call_cidade

label nona_evento3:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("h3_save", extra_info="h3_save")

    $ estou_na_cidade = False
    $ iconchefe += 1

    $ nona_e3 = "evento"

    $ nona_interrogatorio = 0
    $ no3_confessa = False
    $ no3_tony = False
    $ nona_interesse = False

    pause

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Esta é uma das pautas mais difíceis em todo o jogo. Por isso, preste atenção no que eu vou te dizer."

        p "Para conseguir, você precisa ficar do lado do brutamontes e contar a verdade para ele. Trair a garota."

        p "Mas, tome cuidado... se você mostrar preocupação com ela, o tiro pode sair pela culatra."

        p "Entendeu? Não, né? Agora... se você preferir deixar a pauta e salvar ela... eu posso ajudar..."

        menu:
            "Eu quero. Como eu salvo ela?":


                p "Não é simples. Você precisa ter sangue frio. Fica na sua, por pior que pareça. Eu não vou dizer nada. E você?"
            "Eu não preciso da sua ajuda.":


                p "Muito bem. Boa sorte."

    $ renpy.vibrate(1)

    "{i}Brrr{/i}"

    mc angustiado "Nossa! Que calafrio..."

    mc zerado "Faz tempo que eu não sentia uma coisa ruim dessas. Deixa eu sentar..."

    scene mc_ilha_polvo2 with Dissolve(1.0)

    pause

    "Hmm..."

    "Talvez isso seja um aviso que eu tô me metendo em coisa que eu não devia."

    "Até uns meses atrás, eu era só um cara tentando fazer a vida. E olha agora... eu fui até preso por suspeita de assalto a um banco!"

    "Como que as coisas chegaram nisso?"

    "Tirando o fato que aquela maldita da [h] armou essa arapuca pra mim... eu acho que não dá pra colocar todo o problema nela."

    "Foi com as outras que eu fui me metendo em vários buracos. Por que eu não consigo encontrar ninguém 'normal' nessa cidade?"

    "Ou será que o anormal sou eu? Será que o normal é ter uma vida fodida cheia de gente querendo te ferrar?"

    "Eu tenho o chefe... e a [j]... que tão sempre querendo me ferrar também..."

    "Mas ser preso é demais. E se eu não tomar cuidado, a tendência é as coisas irem piorando. Eu não acho que a [h] vai parar nisso."

    menu:
        "Eu preciso dar uma freada no carango":


            mc "A verdade é que eu tenho que maneirar ou as coisas vão sair do controle. Eu tô entrando demais nos problemas dos outros."

            "Eu preciso manter a cabeça no lugar. As pessoas vão precisar de mim e eu não posso ter controle total da minha vida, eu sei disso..."

            "Mas ter o sangue frio e saber onde pisa é essencial. Eu quero viver aqui por muito tempo, e me arriscar demais só vai contra isso."
        "É de confusão que eu gosto mesmo!":


            "Eu tenho que parar de me fazer de vítima. Essa vida é a melhor. O que adianta tá no fervo da capital e ficar de boa?"

            "O lance é aproveitar mesmo todas esses lances que tão rolando. E entrar de cabeça mesmo."

            "Eu vou matar no peito o que vier e aproveitar. Quando eu tiver morto eu descanço."

    mc "Ou o contrário... sei lá... acho que as duas alternativas têm seus pontos fortes e fra---{nw}"

    "???" "Lorde [mc]!"

    mc "?"

    "???" "Nobre senhor!"

    mc "Só uma pessoa na ilha fala desse jeito..."

    scene black with dissolve

    gar "Senhor. Por favor, venha comigo."

    mc desconfiado "Que foi?"

    gar "Venha, senhor. Temos de parlar no conforto de meu humilde antro de prazer carnal."

    mc zerado "..."

    "..."

    scene no3_img1 with Dissolve(1.0)

    pause

    mc "Que foi? Não tô muito afim de lavar prato hoje..."

    gar "Perdão, senhor [mc]. Não foi o intento deste humilde servo preocupar vossa senhoria com tal pensamento."

    menu:
        "Você pode falar igual uma pessoa normal?":


            mc "Você pode tentar falar igual a gente por favor? Pelo menos um pouco..."

            gar "Meu intento é sempre servir, senhor."

            mc "..."
        "Por que você fala desse jeito?!":


            mc "[gar]... por que você fala desse jeito?! Eu perco metade do que você fala!"

            gar "Ora, tamanha falta de tato teria de ser penalizada em níveis insuportáveis para mim, senhor."

    mc "Você tá me trollando de propósito?"

    gar "Nunca faria isso, senhor."

    mc "Tá bom. Nem começou a conversa e eu já tô ficando cansado. Por que você me chamou?"

    gar "Meu senhor... estou sendo tomado por grande preocupação."

    mc "Não parece..."

    gar "Pois, veja, nobre companheiro. Uma amiga de grande estima não atende as minhas tentativas de contato."

    mc "Que que tem? Se pá ela nem acordou ainda."

    gar "Aprecio a tentativa de acalmar este meu falível coração, no entanto, o corrido não é comum."

    gar "Nós não nos costumamos trocar mensagens, entretanto, quando há necessidade iminente, mantemos total presteza."

    gar "É deveras preocupante ela não retornar, em vista ser a primeira ocorrência de infortúnio de tamanha angústia."

    mc "Tá... deixa eu ver se eu entendi."

    mc "Sua amiga não respondeu sua mensagem pela primeira vez."

    gar "Exatamente."

    mc "Você podia ter dito isso."

    gar "Veja, senhor [mc], ser prolixo é um dos meus dons. Não digo que seja um dos mais úteis, porém, é algo do qual não posso me desfazer."

    mc "Ok... ok..."

    menu:
        "Quem é sua amiga?":


            mc "E quem é sua amiga?"

            gar "Interessado? Honestamente, não acredito que a senhorita tenha pretendente, ao menos pelos meus conhecimentos."

            mc "Não é isso que eu tô perguntando..."

            gar "Está certo quanto a isso?"
        "E o que eu tenho a ver com isso?":


            mc "Tudo bem. Mas o que isso tem a ver comigo? Por que você me chamou?"

            gar "É um honesto pedido de ajuda, de socorro, vindo de um humilde servo... o qual não tem outra escolha à vista."

    mc "Por que eu tento perguntar as coisas pra você? Só quero saber o que eu tô fazendo aqui."

    scene no3_img2 with Dissolve(1.0)

    pause

    gar "A missão a qual lhe incubo, senhor [mc], é de ter comprovação da saúde e bem-estar de minha prestigiosa conhecida."

    gar "Eu considerarei este um grande favor, o qual deverá ser reavido em igual quantidade e intensidade por mim."

    mc "E por que você mesmo não vai lá?"

    gar "O bar abrirá em breve, e devo estar pronto para receber minha inestimável clientela. Faz-se mister as mesas do fundo estarem impecáveis."

    mc "Tem razão... uma vez você me falou de umas festas que acontecem aqui, né?"

    gar "Oh, sim. Acontecem..."

    mc "Será que um dia você vai me convidar pra uma delas?"

    gar "Seria um tanto quanto imprudente de minha parte, lorde [mc]. Participar destes magnânimos encontros com certeza influenciaria sua vida."

    mc "Se não quer me chamar, só fala de uma vez."

    gar "Deixemos este assunto para momento futuro, é o que lhe peço. Estou preocupado com a moça."

    mc "Se você tá preocupado desse jeito, por que fica me enrolando?"

    gar "Infelizmente, não tenho capacidade para entender as palavras exprimidas."

    mc "Ah!"

    gar "Posso contar com o senhor para a realização de tarefa de importância incalculável para aquele que lhe fala?"

    "Eu quero mesmo me meter nessa? Ainda tô lembrando daquele calafrio que eu tive mais cedo..."

    "Se bem que aturar o [gar] já é uma coisa ruim. Talvez fosse isso."

    "Ter ele me devendo um favor não seria ruim... o [gar] com certeza sabe de muita coisa. Ele poderia me pagar com uma pauta."

    "Ou quem sabe aquela bebida dele de graça? Pra quem eu daria ela..."

    "Melhor parar de viajar. O que eu faço?"

    menu:
        "Ok. Eu quebro essa pra você.":


            mc "Eu vou quebrar essa pra você."
        "Eehh... melhor não.":


            mc "Olha... não é que eu não gosto de você nem nada, [gar]. Você é um cara estranho, mas é bacana."

            mc "Só que eu tô com um pressentimento ruim sobre isso. Acho melhor eu pular fora. Desculpa."

            gar "O senhor é um homem precavido, um dom muito raro quando usado de forma correta. Não há motivo para emendas."

            gar "Entretanto, há algo a apostar. Eu lhe prometo, o que há de receber pelo seu suporte, será benéfico para sua casa."

            mc "Você acha que eu sou fácil de comprar assim?"

            gar "O senhor? Nunca. Porém, estou certo de que é um homem de grande inteligência e astúcia."

            mc "Hmmm..."

            "Esse [gar] é danado. Mas talvez ele tenha razão... será que eu tô pensando demais?"

            menu:
                "Tudo bem. Eu vou fazer.":


                    mc "Ok. Você me convenceu. Eu vou fazer essa pra você."
                "Nah. Não quero. Valeu.":


                    $ nona_e3 = "desistiu"

                    mc "Valeu, mas eu não vou querer mesmo."

                    gar "É uma pena, senhor [mc]. Darei um jeito. Estou eternamente agradecido pelo seu tempo em vir me ouvir."

                    mc "Relaxa. Até mais, [gar]."

                    scene black with dissolve

                    "Eu sinto que essa foi a melhor decisão. E-eu acho..."

                    "Tomara que ele consiga dar um jeito."

                    jump nona_e3_final

    gar "Meus mais sinceros agradecimentos, lorde [mc]."

    mc "Mas eu só quero ver o que você vai ter pra mim depois."

    gar "Será uma recompensa como nunca antes imaginada. É uma garantia que dou."

    mc "Esse seu jeito não passa muita confiança..."

    gar "Muito bem... este é o endereço dela. Fica no décimo segundo andar. Apartamento 124."

    if no2_ape:

        "Esse número... acho que eu já ouvi esse endereço antes."

    mc "Fica no centro. Beleza."

    gar "Por clemência, tenha cuidado, senhor [mc]. Estou certo de que algo aconteceu naquele lugar."

    mc "Ela deve tá sem bateria e você fica todo assim aí. Mulheres às vezes tem as coisas delas. Você tá sendo machista."

    gar "Senhor... não perca tempo aqui. É o que lhe peço."

    mc "De novo isso... ok. Tô indo nessa."

    gar "Muito obrigado."

    scene black with dissolve

    call locomocao from _call_locomocao_13

    scene black with dissolve

    scene cidade_centro13 with Dissolve(2.0)

    pause

    "O lugar fica por aqui..."

    if no2_ape:

        "Engraçado... eu tenho quase certeza que eu já vi esse lugar."

        "Esse prédio... esses corredores..."

    "Apartamento 124... acho que é... esse aqui?"

    mc desconfiado "Hm? A porta tá meio aberta..."

    scene black with dissolve

    mc preocupado "Com licença..."

    scene no3_img3 with Dissolve(1.0)

    pause

    mc angustiado "!"

    mc "O q-que aconteceu aqui?!"

    "O lugar tá todo destruído! Parece que até queimaram as paredes. O prédio é meio velho, mas é impossível que fosse assim..."

    "Acho que o [gar] tava certo... alguma coisa aconteceu com a amiga dele."

    if no2_ape:

        "Cara... essa poltrona..."

        "E esse móvel em baixo da janela com esse vazo... eu tô quase lembrando..."

        "Pera!"

        show no2_ape1 with dissolve

        pause

        mc surpreso "!"

        "É a casa da [h]! Eu sabia! Eu sabia que eu já tinha vindo aqui! O número do apartamento!"

        "Daquela vez foi o motorista que me trouxe, por isso eu não lembrei, mas agora que eu tô vendo é óbvio!"

        "A amiga do [gar] é aquela doida?! Pensando bem, faz todo o sentido. Os dois são super alternativos."

        "Acho que o [gar] é um pouco mais que alternativo... mas que seja, né?"

        hide no2_ape1 with dissolve

    "Eu tenho que avisar ele do que aconteceu aqui. A gente tem que ir na polícia e avisar. E se ela foi raptada ou outra coisa horrível?!"

    mc desconfiado "Hm?"

    "Tem alguma coisa aqui na poltrona."

    "Um recado?"

    "{i}Se você conhece a moradora deste apartamento, estamos procurando qualquer informação sobre ela.{/i}"

    "{i}Toda família está preocupada. Por favor, se souber algo sobre ela, venha até a Pizzaria Alighieri com este papel em mãos.{/i}"

    "{i}Agradecemos imensamente a sua ajuda neste momento difícil.{/i}"

    "A família dela tá procurando por ela... então tudo mundo já sabe que rolou alguma coisa aqui.."

    "Será que fazem dias que aconteceu? O [gar] disse que eles se falavam raramente... então se pá faz tempo que ela tá desaparecida."

    "Pizzaria... Alighieri... esse lugar..."

    if no2_ape:

        "Eu podia jurar que a [h] tinha alguma coisa CONTRA esse povo da pizzaria."

        "Será que no fim ela tá lutando contra a própria família?"

    "A pizaria fica aqui perto, no centro mesmo. É bem rápido daqui."

    "Acho que vou dar uma passada lá."

    if no2_ape:

        if nona_aceitou:

            "Eu prometi pra [h] que ia ajudar ela nisso tudo. Eu aceitei a pauta do aeroporto, eu participei do assalto no banco..."

            "Eu não posso abandonar ela assim agora."

            "Tá na cara que alguma coisa aconteceu. Eu só não tenho noção do que é ainda. Mas eu tenho que descobrir."

            "É perigoso, mas não dá pra resistir. Eu só preciso torcer pra que eles não tenham nada contra mim."
        else:


            "Eu não aceitei a proposta de ajudar ela com o aeroporto, mas acabei sendo envolvido no lance do banco."

            "Se ela mexeu com as pessoas erradas e agora ferraram ela, eu não tenho nada com isso."

            "Se alguém lá vier falar qualquer coisa, é só falar que eu não tenho nada a ver com ela."

            "Posso até ganhar uns pontos com os poderosos..."

    "Então tá decidido. Eu vou lá. E vou levar esse bilhete aqui."

    "Só espero que não dê uma merda muito grande."

    scene black with dissolve

    "..."

    $ tempo = 3

    scene pizzaria_out_noite with Dissolve(1.0)

    pause

    "Certo. Eu tô aqui. O bilhete tá na mão também."

    "Vamo entrar."

    scene pizzaria_out_italiano with Dissolve(1.0)

    pause

    "Esse cara tá aqui..."

    mc "Boa noite."

    to "Boa noite, jovem. Hm. Isso na sua mão..."

    menu:
        "É só um bilhete.":


            mc "Isso aqui? É só um bilhete que eu encontrei."

            to "Encontrou?"

            mc "Tinha um apartamento aberto aqui perto. A curiosidade acabou falando mais alto e eu resolvi vir aqui."

            to "Você conhece a mulher que mora no apartamento?"

            if no2_ape:

                mc "Sim. Já nos falamos antes, mas pouco."

                to "É uma hacker que assina como [h]."

                mc "Essa mesmo."
            else:


                mc "Não sei quem mora lá, por isso mesmo que eu conheça, não poderia te falar."

                to "É uma hacker, ela assina como [h]."

                mc "Sério?! [h]?!"

                "Aquela mina que me jogou na prisão mora lá?! Então é ela?!"

                "Ela tinha me falado sobre uma pauta do aeroporto..."

                if nona_aceitou:

                    "Eu recusei a oferta dela. Eu não queria me meter nisso."
                else:


                    "Eu aceitei a pauta, mas não quis entrar no apartamento dela naquele dia do banco."

                "Então é ela... não acredito..."

            to "Interessante saber que você a conhece. Justo você."

        "É um recado que deixaram pra minha amiga." if no2_ape:

            mc "É. Deixaram isso aqui na casa de uma amiga minha. Daí resolvi ver o que era."

            to "Uma amiga sua, você diz..."

            mc "É. Acho que tá mais pra conhecida, mas a gente já se falou algumas vezes. Ela morava lá."

            to "Então é isso."

    mc desconfiado "Hm?"

    to "Você poderia vir comigo, [mc]? Quero falar com você sobre esse assunto."

    mc "Agora?"

    to "Sim. Não deve demorar muito."

    menu:
        "Ok.":


            mc normal "Tá bom."

            to "Obrigado. Realmente não pretendo usar muito do seu tempo."
        "Pra onde?":


            mc desconfiado "Pra onde você tá falando?"

            to "Eu tenho um local mais privado aqui ao lado. Vizinho ao restaurante mesmo."

            to "Prometo que não usará tanto do seu tempo."

            "Não sei se eu tô gostando muito dessa história. Mas agora que eu tô aqui..."

            mc "Tudo bem."

            to "Perfeito."

    to "Venha atrás de mim."

    scene black with dissolve

    "..."

    scene no3_img4 with Dissolve(1.0)

    pause

    mc desconfiado "Esse lugar..."

    to "Este é um bar especial que criei para atender clientes especiais da Pizzaria Alighieri."

    to "Acredito que esse assunto pode ser interessante para você também."

    mc "Entendi..."

    if v43_fim:

        "Foi aqui que eu vim aquela vez com a [d]."

        "Eu e o Barão trocamos uma ideia também. Então foi o [to] que levantou isso aqui."

        to "Eu sei que você já esteve aqui. Desculpe se eu acabar falando algo que você já sabe."

        mc envergonhado "Relaxa. É um lugar que dá orgulho mesmo."

        to "Você me entende."

    to "Esta é minha criação. Minha primeira criação."

    mc serio "E a pizzaria? Não vai me dizer que você é segurança lá."

    to "Segurança? Não... mas também não foi uma obra minha. A Pizzaria Alighieri é um legado da família da minha falecida esposa."

    mc desculpa "Ah. Desculpa."

    to "Mesmo não sendo o dono da pizzaria, eu a administro. E usei este anexo para criar este local."

    menu:
        "É um lugar e tanto. Incrível.":


            mc charmoso "Você tem um lugar e tanto aqui. Tem classe."

            to "Agradeço. Foi um projeto pessoal no qual não poupei esforços... ou dinheiro."

            mc "Valeu o investimento."

            to "Com certeza foi um valor bem gasto. Este lugar já foi o palco de grandes acontecimentos."
        "E o que acontece aqui?":


            mc desconfiado "E qual é o motivo deste lugar? Não parece um local aberto pra atender os clientes da pizzaria."

            to "Como eu disse, são clientes diferenciados. Mas não são, necessariamente, clientes da pizzaria."

            to "A famiglia Alighieri não trabalha apenas com comida. Os italianos não são conhecidos somente pela pizza."

            mc "Hmmm..."

            to "Este bar é um local onde posso tratar deste outro negócio que desenvolvemos com mais privacidade."

    mc envergonhado "Parece que bares são locais onde as coisas acontecem..."

    to "É a bebida, [mc]. A bebida deturba os sentidos e tornam coisas impossíveis, possíveis."

    to "Os homens se fazem de lobos, mas, no fundo, o que eles buscam é uma caverna para se sentirem seguros."

    to "O álcool é como uma lareira na sala de estar. Deixa o ambiente mais quente e torna a casa mais confortável."

    mc "E quando a pessoa se sente em casa..."

    to "Essa é a hora certa de fazer o que deve ser feito."

    mc preocupado "{i}gulp{/i}"

    scene no3_img5 with Dissolve(1.0)

    pause

    to "Sabe... alguns homens acham que violência e demonstração de força são a chave para dominar e mostrar poder."

    to "Eles gritam, apontam armas, compram brigas, na tentativa de dizer 'me respeite'. Os italianos fizeram isso por centenas de anos."

    to "O que a famiglia Alighieri descobriu é que o verdadeiro poder não deve ser visto. Ele acontece sob a cortina do espetáculo."

    to "Os bobos da corte falam e aparecem lindos sob o holofote, nos jornais, depois na televisão e agora nas redes sociais."

    to "Eles possuem milhões de seguidores, milhares de curtidas, uma verdadeira falange de fãs, que os seguem como líderes do novo mundo."

    to "O que poucos sabem, é que o poder não está lá. Ele está fora da mídia, em bares como este, escondido e mantendo o velho mundo como sempre foi."

    to "E é pra isso que este local foi levantado."

    to "Desculpe por essa fala tediosa."

    mc envergonhado "Não achei."

    to "Ela foi necessária para que eu pudesse te fazer uma pergunta."

    mc desconfiado "Hm?"

    to "O que você acha disso? O que essa versão de poder desperta em você?"

    mc "Em mim..."

    "Por que um homem como esse quer saber minha opinião sobre uma coisa dessas?"

    "Esse [to] não dá ponto sem nó. Se ele tá perguntando, alguma coisa tem."

    menu:
        "Eu quero fazer parte disso.":


            mc charmoso "Eu concordo muito com isso. Com certeza eu gostaria de fazer parte desse mundo."

            to "E quem não gostaria? Dar as cartas, mesmo que nas sombras, é o significado do verdadeiro poder."

            to "Deixe os idiotas aparecerem. Eles serão a cara do novo mundo, enquanto você, de verdade, mantém o poder onde sempre esteve."

            mc "É o que eu pretendo um dia. Chegar nesse ponto."

            to "Você claramente tem a mentalidade certa. Só precisa tomar as decisões corretas e tudo vai acabar bem pra você."

            mc "Valeu."
        "Eu não gosto nem um pouco.":


            mc serio "Eu não gosto nem um pouco disso. Do jeito que você fala, os poderosos parecem ratos no esgoto."

            mc "O que adianta mandar algo, se você não pode nem ver a luz do dia? Não é melhor só ter uma vida como outra qualquer?"

            to "..."

            mc desculpa "Não sei se falta ambição pra mim ou se eu só muito inocente, mas isso é uma coisa que não me atrai."

            to "Você, com certeza, é uma pessoa sincera. E isso também tem o seu valor."

            to "Entretanto, é importante você saber medir suas palavras. Nem tudo convém dizer."

            mc preocupado "E-eu vou lembrar disso."

    to "Mudando de assunto, tem um outro lugar que eu quero que você veja. Fica aqui nos fundos."

    mc angustiado "{i}brrr{/i}"

    "Lugar nos fundos?! N-não sei por que, mas eu senti aquele calafrio de novo. Igual hoje cedo..."

    "Só tem nós dois aqui pelo jeito... e olha o tamanho desse cara. Ele é o chefe do Marco. Se ele quiser..."

    menu:
        "Talvez seja melhor eu ir embora.":


            mc envergonhado "T-talvez seja melhor eu ir embora. Eu realmente só queria ver o lance do bilhete."

            mc "Pensando bem, acho que eu fui muito intrometido. Eu nem tenho informações sobre ela mesmo."

            to "Calma. É algo rápido. Só vamos conversar mais um pouco, mas não há necessidade de fazermos isso em pé."

            mc preocupado "Amanhã eu trabalho, ent-{nw}"

            to "Eu vou ter que insistir para que você venha. Seria uma desfeita de sua parte."

            mc "T-tudo bem. Eu posso ficar mais um pouco..."
        "Vamos lá.":


            "O que tiver que ser que seja."

            mc charmoso "Ok. Vamos lá."

    to "Por favor. Venha comigo."

    scene black with dissolve

    scene no3_img6 with Dissolve(1.0)

    pause

    to "Esta é minha sala. É aqui que eu passo quase todo o meu dia. Aqui que recebo as pessoas também."

    if diana_e6 == "barao":

        "Essa sala... foi aqui que o Barão me trouxe aquele dia. Então essa é a sala do [to]."

        "Acho que não é uma boa ele saber que eu já tive aqui."

        to "Ah. Eu sei que o Barão te trouxe aqui na outra noite."

        mc desculpa "E-ele que me chamou. Eu não sabia que..."

        to "Não tem problema. O Barão é assim. Ele é uma pessoa que não vê limites."

        to "Com o tempo você entende. Pessoas obstinadas são assim mesmo."

        mc envergonhado "Haha..."
    else:


        mc surpreso "!"

        mc "Q-que lugar..."

        to "Por favor, não repare em algumas coisas fora do lugar. É bastante corrido aqui."

        "Tem uma pilha de dinheiro ali. E cofres... e câmeras e tanta coisa..."

    "Que que acontece com esse cara?"

    to "Achei muito interessante ter sido você a encontrar o bilhete na casa da hacker."

    "Eita... Esse papo é perigoso pra mim..."

    mc envergonhado "Por que você diz isso?"

    to "Eu imaginava que alguém mais próximo dela seria o primeiro a descobrir o que tinha acontecido no apartamento dela."

    menu:
        "Ela é da sua família?":


            mc desconfiado "O papel falava que a família dela queria saber alguma informação... pra trazer aqui. Vocês são conhecidos?"

            to "Você realmente não sabe nada sobre essa mulher?"

            mc "Não entendi."

            to "Hm."
        "Foi só coincidência.":


            mc envergonhado "Foi só coincidência. A porta tava aberta e quando eu olhei pro apartamento chamou a atenção. A cara não tava boa."

            to "Você mora na ilha."

            mc "Ah! Sim! Um amigo mora naquele prédio. Eu tava lá porque ele me pediu pra ir."

            "Isso não é totalmente mentira... Se esse cara me pega... não sei se eu devia mentir pra ele assim. Tô começando a ficar nervoso."

            to "Olha, só."

    to "Venha. Sente aqui comigo, [mc]."

    mc surpreso "T-tá."

    scene no3_img7 with Dissolve(1.0)

    pause

    to "Essa mulher é procurada internacionalmente."

    mc "S-sério?!"

    to "Ela é procurada pela Interpol, acusada de diversos crimes cibernéticos em vários países."

    to "A identidade dela é desconhecida. O que sabemos é que ela vive trocando de residência com a ajuda de embaixadas de países aliados."

    mc "Que país ajudaria uma criminosa internacioal?"

    to "Existem potências interessadas nos serviços que ela oferece."

    mc "E que tipo de coisa uma mulher sozinha pode fazer?"

    to "Ela é especializada em derrubar governos."

    mc "N-nossa..."

    to "Usando terrorismo cibernético, ela encontra irregularidades em administrações e coopta influenciadores e mídia locais para trazer isso à tona."

    to "Ela faz o mesmo com empresas e outras organizações, causando a demissão de CEOs e diretores."

    to "Até mesmo burlar sistemas de segurança digitais e auxiliar em assaltos. Tudo de acordo com o pedido dos contratantes, que investem milhões em seus serviços."

    mc "T-tudo isso... sozinha?"

    to "Impossível saber, mas reza a lenda que sim."

    mc "Incrível... q-quero dizer... é... bastante coisa pra uma pessoa sozinha conseguir fazer. Parece coisa de jogo de videogame."

    to "É o que eu acho. Por isso que eu acredito que dessa vez ela tem apoio."

    mc "Apoio?!"

    to "Sabe, [mc]... essa mulher participou de algo grande recentemente."

    mc "C-certo..."

    to "O último golpe dela foi um assalto a uma agência do Novo Banco Central, que fica na sua ilha."

    mc "!!!"

    to "Você ficou sabendo?"

    menu:
        "Claro... eu vi de camarote.":


            mc "Eu vi de camarote o evento. Eu tava lá no meio."

            to "Então você esteve lá com ela?"

            mc "Sim. Eu participei. Claro que eu não queria roubar nada, mas acabei no rolo."

            to "Entendo..."
        "Eu fui parar na cadeia por causa dela!":


            mc "Eu fui parar na cadeia por causa dessa mulher! Ela me envolveu no esquema sem eu saber!"

            to "..."

    to "Então foi você que acabou preso. Seu encarceramento não foi registrado nos autos."

    mc "Não?"

    to "Parece que alguém pediu pra que nada fosse registrado. Eu conversei com a polícia, mas eles estão com medo de falar."

    mc "S-sei..."

    "Então ele não sabe que foi a juíza que me tirou de lá. Ele nem sabia que eu tinha sido preso e eu entreguei de bandeja pra ele."

    scene no3_img8 with Dissolve(1.0)

    pause

    to "A operação no banco foi muito bem planejada e com certeza contou com o apoio de gente daqui da capital."

    to "Eu vou descobrir quem participou disso. E vou tomar as medidas necessárias pra proteger nossa cidade dessas pessoas."

    mc "Como você vai fazer isso?"

    to "Eu tenho meus modos. Eu não estou sentado nesta mesa por sorte. Eu não nasci em berço de ouro como outros."

    to "Nós somos parecidos nisso, [mc]."

    mc "No que você diz?"

    to "Nós dois começamos de baixo, como peões nas mãos de pessoas maiores, e com o tempo, crescemos e conquistamos nosso lugar à mesa."

    mc "Eu n-não sei se eu cheguei lá..."

    to "Você é novo. E tem um longo caminho pela frente. Mas eu sinto que você tem determinação pra isso."

    to "Todo sucesso que cai do céu não é merecido. Batalhar, falhar, errar, se reerguer pra chegar onde se quer, é a verdadeira conquista."

    to "Mas, pra isso, você precisa se relacionar com as pessoas certas. É por isso que eu preciso da sua ajuda agora."

    mc "Hm? Minha?"

    to "Exatamente. Eu não esperava que você aparecesse com o recado na mão, mas pode ter sido a melhor coisa que me aconteceu."

    to "Principalmente agora que eu sei que foi você que foi preso no assalto ao NBC."

    "Ajudar o [to]... ajudar ele é ajudar os italianos que mandam na capital."

    "É ajudar o Gustav, o Barão, o Lucca, a [j], o Gevanni, a Blergh!, o prefeito e todas essas pessoas que mandam e desmandam aqui."

    "Com certeza eles podem me dar uma vida melhor na cidade. Eu sinto que eu posso virar o novo rei da cocada preta com eles."

    "Mas aceitar tudo o que essas pessoas fizeram... e abandonar todos que lutam contra eles, igual a [w] e a própria [h]."

    "Eu preciso pensar muito no que eu vou fazer aqui hoje. Isso pode mudar completamente minha vida na capital."

    to "E então, [mc]? Posso contar com sua ajuda?"

    menu:
        "Eu não sei o que eu posso fazer.":


            mc "Olha, [to], eu não sei o que eu posso fazer pra te ajudar. Não sei se seria de alguma ajuda pra vocês."

            to "Logo você vai entender como você vai ajudar."

            mc "..."
        "Com certeza. Vou ajudar no que puder.":


            mc "Pode contar comigo. Se eu puder fazer algo, vou fazer com todo o prazer."

            to "Vai ser importante contar com você hoje. Pode ter certeza que não vou me esquecer disso."

            mc "Bom saber."

    to "Agora eu quero te mostrar um último lugar. Venha."

    scene black with dissolve

    mc angustiado "{i}brrr{/i}"

    "O que tem nessa sala escura?"

    to "Veja o que eu consegui."

    scene no3_img9 with vpunch

    pause

    mc surpreso "!"

    "N-nona! E-ela tá presa?!"

    to "Ela pensou que poderia fugir de nós pra sempre. Mas parece que é aqui que a carreira dela acaba."

    to "Ela se aproximou do [gi] e trabalhou com ele por meses, domou ele como um animal e no fim o traiu."

    to "Infelizmente, entretanto, ele não conseguiu identificar ela. Ele acha que é, mas não tem certeza."

    to "Ele diz que algumas características físicas Carla eram diferentes, os seios eram menores e o rosto era diferente. A voz era diferente."

    to "Mas as tatuagens são as mesmas. Apesar delas não serem permanentes. Ela poderia estar tentando incriminar outra pessoa."

    mc preocupado "Sério? Essa é uma opção? Realmente muda tudo..."

    to "Nós não tivemos tempo ainda pra fazer uma análise completa, mas tudo me leva a crer que é ela."

    to "O estranho é que... por que você teria tatuagens como essa se você quer se esconder? Não faz sentido."

    mc preocupado "Tem razão. E o que você pretende fazer se for ela mesmo?"

    to "Eu preciso que ela me diga com quem ela trabalha. Ela sozinha é perigosa, mas se tem alguém na capital com ela, é mais problemático ainda."

    mc "Entendi... e como você vai ter certeza?"

    to "Ela mesma vai confirmar. E vai falar quem tava com ela."

    to "Esta sala já fez muita gente abrir a boca. No fim, quando eles se metem em problema de verdade, sou sempre eu que tenho que resolver."

    to "Muito bem. Vamos começar. Saíremos daqui somente quando ela falar."

    mc preocupado "Ela tá dormindo?"

    to "Sim, mas não por muito tempo."

    mc angustiado "!"

    scene red with vpunch

    "{i}tash{/i}"

    h "Ai!"

    to "Acorda, vagabunda!"

    mc angustiado "!!!"

    scene red with hpunch

    "{i}push{/i}"

    h "HAH!"

    "Meus Deus! Ele tá batendo nela de verdade!"

    to "Você sujou minha mão..."

    scene no3_img10 with Dissolve(1.0)

    pause

    h "{i}cof cof{/i}"

    h "O que... {i}khaf{/i}... você tá fazendo, seu porco?"

    to "Parece que ficar sem comer e beber não é o suficiente pra você falar. Eu vou ter que ser... mais convincente com você hoje."

    h "Você é um filho da puta fora da lei!"

    to "Olha quem fala... a terrorista cibernética."

    h "..."

    to "Pronta pra falar?"

    h "Eu não tenho nada pra falar. Eu não sou quem você pensa que eu sou e eu não conheço ninguém que queira atacar a cidade. Eu já disse!"

    to "Você pretende continuar mentindo? Então a gente vai passar um tempo aqui."

    h "Por favor... não me bate mais. Eu juro..."

    "O que eu faço?! Eu vou ficar aqui vendo ele batendo nela?!"

    to "Ah. Hoje eu trouxe um amigo."

    h "Amigo?"

    to "Ele esteve com você no assalto ao NBC. Ele mesmo confirmou. Ele vai me ajudar a descobrir a verdade."

    h "..."

    to "Venha aqui, [mc]. Deixe ela dar uma boa olha no seu rosto."

    mc desculpa "..."

    scene no3_img11 with Dissolve(1.0)

    pause

    h "Não faço ideia de quem é esse sujeito."

    mc angustiado "!"

    "O que ela tá fazendo?! Ela não me reconhece?! Impossível! Qual o objetivo dela?"

    to "Não se faça de boba. O [mc] foi encontrado dentro do cofre do NBC no dia do assalto. Ele estava com você na visita!"

    h "Que visita? Que cofre? Eu já disse que eu não sou essa Carla! Seu próprio parceiro não soube falar!"

    to "Ele é um idiota! Mas o [mc] vai dizer a verdade."

    h "Por que esse cara?! Eu nunca vi ele na vida!"

    "Eu não posso só ficar vendo isso. Eu tenho que falar alguma coisa!"

    menu:
        "[h], não precisa me proteger.":


            $ renpy.block_rollback()

            $ nona_interrogatorio += 1

            mc preocupado "[h], não precisa sofrer por minha causa. Você precisa pensar em você."

            h "Você é maluco?! Do que você tá falando?!"

            to "Era o que eu esperava de você, [mc]. Nós não precisamos fazer ela sofrer mais, se todos colaborarem."

            mc "[to], você não pode só agredir ela dessa forma! Ela tá assustada!"

            h "Eu nunca vi ele na vida!"
        "Eu não sei se ela é a Carla.":


            $ renpy.block_rollback()

            mc "Eu não consigo confirmar se ela é a Carla mesmo. Com certeza é parecida. A tatuagem com certeza é a mesma."

            h "Cala a boca! O que você sabe?!"

            mc "Mas o cabelo dela é totalmente diferente, o rosto e o corpo parece mais gordo, e a voz dela com certeza é diferente."

            to "Mas ela está em uma situação de desespero. A voz não prova nada."

            mc "Você pode tá certo."

            h "Vocês não sabem quem eu sou! São malucos! Por favor me soltem!"
        "...":


            $ renpy.block_rollback()

            mc desculpa "..."

            to "E então?"

            mc "Não sei..."

            to "..."

            to "Eu esperava mais de você, [mc]. Diga algo!"

            mc "Eu não sei, é sério."

            h "Tá vendo?! Eu nunca vi esse cara na vida!"

    mc "..."

    "Será que não é ela? Pensando bem, talvez eu esteja sendo enganado pelo óculos e pelo cabelo. A voz realmente parece diferente."

    to "Vamos continuar."

    to "Por favor. Me dá uma licença, [mc]."

    mc preocupado "Por favor, nã-"

    scene red with hpunch

    "{i}BASH{/i}"

    h "AAAHHH!"

    mc angustiado "!!!"

    menu:
        "...":


            $ renpy.block_rollback()

            "Eu não posso falar nada... desculpa, [h]..."

            scene red with vpunch

            "{i}DUSH{/i}"

            h "UUEEGHH!"
        "Para! Tá bom!":


            $ renpy.block_rollback()

            $ nona_interrogatorio += 1

            mc angustiado "Chega, [to]! Tá bom!"

            to "{i}puf{/i}"

            if nona_interrogatorio == 2:

                mc "Você disse que não precisava machucar ela!"

                to "..."

            mc "Pergunte pra ela! Ela vai responder!"

            to "Ok..."

    scene no3_img12 with Dissolve(1.0)

    pause

    h "{i}cof ueeegh ptuch{/i}"

    "Ele tá espancando ela... se isso continuar assim ela vai morrer aqui."

    to "Eu sei que você teve ajuda de gente da capital pra conseguir assaltar o NBC."

    h "Seu porco... {i}cof{/i}"

    to "Eu quero saber quem trabalha com você. Fale e tudo acaba."

    h "Eu não posso falar... o que eu não sei... você não entende?!"

    to "Você vai continuar fingindo que não sabe de nada? Muito bem... se me dá licença, vou continuar até você mudar de ideia."

    h "Não! Por favor!"

    to "Não me venha com 'por favor não'. Eu estava disposto a perdoar o que você fez, se você confessasse."

    h "Mas eu não tenho... o que confessar..."

    to "Muito bem."

    "Não! Ele vai bater nela de novo! Eu sou vou ficar vendo?!"

    menu:
        "Chega! Eu sei quem trabalha com ela!":


            $ renpy.block_rollback()

            "Eu não tenho que proteger a juiza! Eu prefiro salvar a [h]!"

            mc angustiado "Chega! Eu sei com quem ela trabalha! Pode parar!"

            to "Sabe?"

            h "Você vai acreditar nesse cara?! Eu já disse que ele não é nada!"

            mc desculpa "Eu vou falar o que eu sei. Por favor, só pare com tudo isso."

            to "Vamos ouvir."

            h "Não!"

            jump nona_e3_confessa
        "...":


            $ renpy.block_rollback()

            "Eu não posso falar nada. Se eu abrir a boca, posso tá colocando a vida dela em risco, e a minha também."

            "Eu não sei o que o [to] vai fazer comigo se ele achar que eu tô envolvido com ela."

            if nona_aceitou:

                "Ainda mais porque eu aceitei ajudar ela com a pauta do aeroporto. Acho que agora eu também faço parte do lance dela..."

                "Se ele descobrir isso, minha cabeça vai pro saco também."

            "Você precisa aguentar aí, [h]."

    to "Eu pensei que alguém que te conhecesse apareceria depois do recado que deixei no seu apartamento."

    h "..."

    to "O que parece é que ninguém se importa com você. O único que veio foi o [mc]."

    to "Eu pensei que talvez vocês estivessem ligados de alguma forma... já que participaram juntos do assalto."

    h "Eu já disse que não sei de nada disso. E não sei quem é ele também!"

    to "Eu tentei te ajudar."

    h "Não! Por favor!"

    to "Você é uma mulher resistente. Eu já tô começando a suar."

    to "Agora fique quietinha ou eu posso acertar algum ponto perigoso."

    h "Nã-"

    scene red with hpunch

    "{i}DUSH{/i}"

    h "Ahhh!"

    scene no3_img13 with vpunch

    pause

    mc angustiado "!!!"

    to "Para de gemer e fala o que eu quero ouvir!"

    to "Você vai morrer aqui, putinha!"

    h "Ai! {i}cof ueeegh ptuch{/i}"

    h "{i}UUEEGH COF UACK{/i}"

    to "Vai engasgar com o sangue assim!"

    "Esse homem é louco!"

    "Ele vai matar ela de verdade se eu não fizer alguma coisa!"

    menu:
        "Ela vai morrer antes de falar!":


            $ renpy.block_rollback()

            $ nona_interrogatorio += 1

            mc angustiado "[to]! Ela vai morrer se você continuar!"

            to "Está preocupado com ela, [mc]?!"

            to "Essa cadela merece por tentar acabar com a minha cidade!"

            mc "Eu não aguento ver isso! Para por favor!"
        "Fale logo o que ele quer ouvir!":


            $ renpy.block_rollback()

            mc irritado "Fala logo o que ele quer ouvir, porra! Você vai se matar?!"

            h "AAH!"

            h "C-chega! Tá doendo!"

            to "Ela não vai falar, [mc]! Ela foi treinada pra ficar calada! Eles são todos assim!"

            "Ela continua calada! Ela vai morrer!"

    scene no3_img13 with hpunch

    pause

    h "{i}UUEEGH!!!{/i}"

    "Ela não vai falar sozinha. Ela vai morrer e não vai abrir o bico."

    "Eu quero que ela morra? Eu tenho a vida dela na minha mão. Eu posso acabar com isso se eu tiver coragem."

    "Se eu falar pra ele que a juíza que me soltou da prisão, talvez isso tire a atenção dele da [h]."

    "Eu também vou ajudar ele e ganhar uns pontos com os italianos."

    "Mas... e se esse não for o plano da [h]? E se ela preferir morrer do que entregar a juíza?"

    "E onde o [gar] entra nessa história?"

    "Eu preciso decidir agora. Eu posso ferrar tudo, de um jeito ou de outro."

    menu:
        "...":


            $ renpy.block_rollback()

            "Eu tenho que respeitar a decisão dela. Se ela quer morrer... não sou eu que vai estragar isso..."

            "Meu coração dói de ver ela sendo judiada desse jeito. Eu pareço fraco, impotente... é frustrante demais!"

            mc irritado "..."

            "Como pode isso acontecer na vida real?! Uma pessoa que tava de boa na vida dela, e agora sendo tratada como lixo."

            "Isso não pode tá certo! Que raiva! Eu devia ter falado alguma coisa!"
        "Eu sei quem ajudou ela! Só não mate ela!":


            $ renpy.block_rollback()

            mc preocupado "Pode parar. [to]! Eu sei quem ajudou ela!"

            to "Hm?"

            jump nona_e3_confessa
        "Eu vou ficar do lado do [to] e falar tudo":


            $ renpy.block_rollback()

            $ no3_tony = True

            "Eu ganho mais ficando do grupo. Eles mandam na cidade e eu posso mandar com eles."

            "Desculpa, [h], mas eu tenho que pensar nas minhas prioridades antes de me preocupar com você."

            mc charmoso "[to], eu tenho algo que você vai querer saber."

            to "Hm..."

            jump nona_e3_confessa

    scene no3_img13 with vpunch

    pause

    h "{i}AKH!{/i}"

    to "Cansou, né?"

    scene no3_img14 with Dissolve(1.0)

    pause

    h "..."

    to "..."

    "Ela apagou."

    to "Parece que ela não aguentou."

    mc preocupado "E a-agora?"

    to "Ela não ia falar, então pra mim não muda nada se ela está viva ou morta."

    to "Eu vou ter que encontrar outra forma de achar os comparsas dela. Nada me tira da cabeça que eles existem."

    to "E se realmente esta mulher era a [h], é um inimigo a menos para nossa cidade, não concorda?"

    menu:
        "E se não fosse ela?":


            $ renpy.block_rollback()

            mc "Mas e se não fosse ela? Então uma mulher inocente morreu."

            to "Eu sei que isso pode parecer horrível para você neste ponto, mas as formigas operárias se sacrificam pela rainha."

            to "A ovelha se subjuga ao pastor, e o animal se transforma em comida para o homem."

            to "Essa mulher fez o papel dela no grande esquema das coisas. Ela morreu com honra."

            "Incrível como ele consegue encontrar uma razão de justiça depois de matar alguém a sangue frio."

            mc desculpa "..."
        "Tem razão...":


            $ renpy.block_rollback()

            mc charmoso "Você tá certo. O que mais importa vem primeiro."

            to "Exatamente. É importante termos prioridades na vida. Focar no objetivo e não se deixar abalar durante o caminho."

            to "Fazendo o que for necessário pra ser bem sucedido, você chegará longe."

            mc "Obrigado."

    to "Eu vou voltar pra minha sala. Preciso conversar com algumas pessoas e definir o próximo passo."

    to "Agradeço pela companhia, [mc]. Ah. Pode fazer um último favor pra mim?"

    mc "O que é?"

    to "Eu vou chamar o [mar], você pode pedir pra que ele se livre dela por favor?"

    mc "T-tá..."

    to "Até uma outra oportunidade."

    scene black with dissolve

    "..."

    scene no3_img15 with Dissolve(1.0)

    pause

    mc "Desculpa... eu devia ter falado alguma coisa pra fazer ele parar."

    mc "Eu não queria jogar toda sua luta no lixo. Acho que no fim eu pensei que você fosse aguentar. Desculpa, de verdade."

    mc "Se eu tivesse uma forma de voltar no tempo, eu voltaria e faria alguma coisa diferente."

    mc "Espero que seus amigos me perdoem. Adeus."

    mc "Mas, se meu esforço vale um centavo, as coisas não vão acabar assim..."

    "Caralho. Não devia ter falado isso. Tomara que não tenha nenhuma câmera me filmando."

    "Eu queria poder me despedir com calma, mas não vai rolar. Melhor eu dar o fora daqui."

    scene black with dissolve

    pause

    "Eu tenho que voltar pro bar e avisar o [gar] o que aconteceu aqui. Ele era amigo da [h]."

    "..."

    pause

    "{i}cof{/i}"

    h "{i}cof cof{/i}"

    mc surpreso "!"

    scene no3_img15 with vpunch

    mc "[h]... você tá viva?"

    h "..."

    "Eu acho que ela tá respirando. Eu tenho que tirar ela daqui!"

    mc preocupado "Desculpa, mas eu vou ter que te balançar um pouco."

    scene black with dissolve

    "Primeiro essas amarras aqui... Pronto! Agora..."

    mc preocupado "Upa!"

    scene no3_img16 with Dissolve(1.0)

    pause

    "Que bom que ela é levinha. Mas..."

    "O que eu faço com ela?!"

    "Eu sei que eu tenho que sair daqui antes que o [mar] volte."

    "Mas não tem como sair assim com ela na rua... sorte que é bem tarde da noite."

    "Eu vou colocar minha roupa nela e torcer pro cara do Uber não fazer perguntas..."

    "É impossível entrar num ônibus com ela nesse estado."

    "Se eu esconder o sangue, acho que dá pra fingir que ela tá dormindo."

    "Mas e o cheiro?! Ela tá fedendo sangue, suor..."

    "Pode ser até perigoso pra mim se eu for pego carregando ela nesse estado."

    "Mas se eu deixar ela aqui, o [mar] vai terminar o serviço, certeza. Só eu posso salvar ela."

    menu:
        "Levar a [h] com você.":


            $ renpy.block_rollback()

            mc "Foda-se, eu tenho que tirar ela daqui. É a única chance que ela tem."
        "Deixar ela na sala e sair sozinho.":


            $ renpy.block_rollback()

            mc "Eu não tenho como sair daqui com você desse jeito. Ia ser perigoso pra mim. Desculpa, [h]."

            "Eu vou falar pra todos o quanto você lutou. Desculpa, mesmo."

            jump nona_e3_morta

    scene bar_tony1 with Dissolve(1.0)

    pause

    "Eu tenho que sair antes que o-"

    mar "[mc]? O que você tá fazendo com essa mulher?"

    "CARALHO!"

    mc envergonhado "É... ela tava sendo interrogada pelo [to]. Eu tava com ele."

    mar "O chefe pediu pra eu vir aqui. Que era algo urgente."

    mc "E-eu disse pra ele... é... ficar tranquilo que eu faria o trabalho no seu lugar."

    mar "Sério? Você tá dentro desse tipo de coisa? De verdade?"

    mc "É o que parece..."

    mar "É legal ter um parceiro no trabalho pesado. Boa sorte."

    mc "Valeu. Agora é melhor eu sair daqui."

    mar "Toma cuidado. Um passo errado nesse mundo e é o fim da linha."

    mc angustiado "V-vou lembrar disso. V-valeu! F-falou!"

    scene black with dissolve

    scene pizzaria_out_noite with Dissolve(1.0)

    "..."

    "O Uber tá chegando... Só espero que ele não pergunte nada."

    "Essa hora o bar já deve ter fechado. Se o [gar] não tiver lá, eu tô fodido."

    scene black with dissolve

    "..."

    mc "[gar]! Abre!"

    scene no3_img17 with hpunch

    pause

    $ nona_e3 = "viva"

    mc "Não acredito que eu cheguei!"

    gar "Honoráveis boas-vindas ao herói do dia, trazendo a donzela em seus braços após um dia de grande angústia!"

    mc "[gar]! Ela tá quase morrendo! Por favor!"

    gar "As agrúrias do dia serão as cantigas vitoriosas da noite! É uma honra presenciar tamanho ato de heroísmo!"

    mc "Ela é magrinha, mas segurar ela por uma hora cansa!"

    gar "O que este humilde servo pode fazer, neste momento de grande desalento, é preparar um leito de repouso pouco apropriado para a tarefa-"

    mc "Cala a boca e vai logo!"

    gar "Minhas mãos são utensílios p-"

    mc "[gar]!"

    scene black with dissolve

    gar "Por favor, repouse nossa donzela."

    mc angustiado "A-aleluia!"

    scene no3_img18 with Dissolve(1.0)

    pause

    mc "Você tinha razão, [gar]. Tinha alguma coisa acontecendo mesmo."

    gar "E o senhor a salvou, como um verdadeiro Don Quixote."

    mc "Mas dessa vez o monstro era bem real."

    mc "Não dá pra imaginar o que ela sentiu... sem comer, sem beber... presa, espancada pelo [to]..."

    mc "Até agora eu não tenho certeza se isso realmente é verdade ou só um pesadelo, sabe? Não parece uma coisa que acontece na realidade."

    gar "É uma incorrigivel, ora. Sabe muito bem o tipo de pessoa que são e resolveu viver a luta de seus sonhos."

    mc "Mesmo assim... olha aqui. Ela é só uma mulher normal."

    mc "Do jeito que o [to] falou, ela parecia uma terrorista capaz de derrubar presidentes. Mas olha agora."

    gar "Não deixe este semblante angelical engabelá-lo, senhor [mc]. Por trás dessa face penosa, reside o caos de Pandora."

    mc "Como é possível?"

    gar "Julgar livro pela capa já a findou a vida de maiores e mais prudentes que o senhor."

    mc "Tenho quese certeza que você tá me ofendendo."

    gar "A forma que você a observa, lorde [mc]... tem comparação a alguém que gostaria de vê-la feliz para sempre. Estou enganado?"

    menu:
        "Não sei... talvez eu goste dela.":


            $ hacker_amizade += 3

            mc "Não sei ainda... de verdade... mas talvez eu goste dela. Quando eu olho pra ela assim, alguma coisa nela me atrai."

            gar "Tirando a incomparável beleza?"

            mc "Talvez seja isso... a [h] é linda mesmo."

            gar "Possivelmente é o fato dela estar quase despida."

            mc "Vamos parar por aqui. Não sei se é hora de comemorar ainda."
        "Não. Eu só fiquei preocupado mesmo.":


            mc "Nada disso. Eu só fiquei preocupado com ela mesmo. De verdade."

            gar "Não há necessidade de tamanha preocupação no momento. Ela está a salvo agora."

            mc "Será? Não sei. Parece que sim, só que eu não consigo me sentir seguro ainda."

    gar "O que aconteceu hoje com certeza engravou grande pesar em seu coração. O tempo irá corroer a marca."

    mc "É o que eu espero..."

    h "Hm... hm?"

    gar "Irei deixá-los a sós. É possível que Pandora precise de sua ajuda agora quando recobrar os sentidos."

    h "Eu... quero meus óculos. E eu tô me sentindo presa. Tira essa blusa de mim."

    mc "C-calma. Eu vou ajudar você. Eu peguei seu óculos."

    scene no3_img19 with Dissolve(1.0)

    pause

    h "A gente realmente saiu de lá?"

    mc "Sim. Pode ficar mais calma agora."

    h "Eu... tava pronta pra... morrer naquela sala."

    mc "Eu sei."

    h "Eu não acreditei quando vi você lá. Como?"

    menu:
        "Eu vou explicar.":


            $ hacker_amizade += 2

            mc "Se você quer saber, eu posso te explicar."

            h "Seja rápido. Não precisa da história completa."

            mc "Ok..."
        "Você não prefere descansar agora?":


            mc "Certeza que você quer conversar? Você não prefere descansar?"

            h "Não. Só fala o que eu tô perguntando."

            mc "Se você quer..."

    mc "O [gar] tava preocupado com você, porque você não respondia as mensagens dele. Daí ele me pediu pra ir até seu apartamento."

    mc "Tinha um recado lá pedindo pra quem te conhecesse levar informações sobre você pra pizzaria."

    mc "O [to] me levou pra dentro e o resto você sabe."

    h "Eu não pensei que você ia conseguir me tirar de lá. Eu até achei que você ia acabar morrendo também."

    mc "Valeu pelo voto de confiança."

    h "Mas eu errei, né? Não é sempre que isso acontece. Você manteve a copostura lá. Mesmo vendo uma garota indefesa sendo espancada."

    mc "Desculpa... eu queria fazer alguma coisa, mas eu achei que ia ser pior."

    h "Claro que ia ser pior. Por isso que foi tão incrível sua coragem. Eu vi nos seus olhos que você queria falar e acabar com aquilo."

    h "Pra nossa sorte, você manteve a língua na boca."

    h "E pensar que você ainda me trouxe em segurança até aqui. Eu substimei você demais em minha análise."

    mc "Como um homem sábio me falou um dia, 'julgar um livro pela capa já findou a vida de pessoas mais sábias'."

    h "Heh... eu mereci essa."

    h "Pode me ajudar a levantar?"

    mc "Você precisa descansar. Beber alguma coisa, comer..."

    h "Não aqui."

    h "Hmm!"

    mc "Calma! Eu te ajudo!"

    "Que garota cabeça dura..."

    scene no3_img20 with Dissolve(1.0)

    pause

    h "Deu tontura..."

    mc "Não me diga!"

    h "Eu não quero causar. Eu ficar aqui vai colocar a sua vida e a dele em risco. Você tem certeza que eles não te seguiram?"

    menu:
        "Certeza que não seguiram.":


            mc "Eu tenho certeza que não. A gente tá seguro aqui."

            h "Hmm..."

            h "Se você diz, acho que posso demorar um pouco então."

            mc "Você precisa recuperar um pouco a energia antes de sair assim."
        "Não sei...":


            mc "Não tem como saber... eu vim de Uber com você e nem tava pensando se tavam atrás da gente."

            h "Tá vendo? Eles podem bater aqui a qualquer momento."

            mc "Mesmo assim. Você precisa descansar. Pelo menos um pouco."

    h "Talvez eu precise mesmo. Essa é a primeira vez que me pegam. Eu não tinha ideia do que fazer."

    h "Eu preciso me preparar melhor pra próxima vez não acontecer a mesma coisa."

    mc "Você tá pensando em próxima? O que aconteceu hoje não foi suficiente pra você acalmar?"

    h "Se eu parar agora, eles vão ganhar. Daí que não vai ter sido de nada mesmo."

    h "Eu não viajei até aqui pra deixar o trabalho feito pela metade. Isso é mais que um serviço, é minha reputação em jogo."

    mc "O [to] disse que você é uma terrorista cibernética. Você invade sistemas e divulga informações sigilosas."

    h "Talvez seja algo mais ou menos isso mesmo."

    mc "Você não é daqui?"

    h "Não. Eu sou bem longe daqui."

    mc "Você nem tem sotaque."

    h "Faz parte do meu trabalho me passar por moradora dos lugares onde eu atuo."

    mc "Você fala quantos idiomas?"

    h "Até agora... eu tive que aprender oito."

    mc "Caramba..."

    h "Não é difícil aprender novas línguas depois que você entende o processo. Você começa aprendendo conjunções e deixa o principal pra depois."

    mc "É um pouco demais pra mim aprender isso agora."

    h "Acho que é verdade..."

    scene no3_img21 with Dissolve(1.0)

    pause

    h "Você... não precisava ter feito aquilo, sabe?"

    mc "Hm?"

    if nona_aceitou:

        h "Você só aceitou uma pauta. Não era um pacto de sangue."
    else:


        h "Você nem aceitou minha proposta de me auxiliar aquela vez no fliperama."

    h "E eu ainda usei você sem seu consentimento no atentado ao banco."

    h "Não consigo entender por que você arriscaria sua vida tentando me tirar de lá."

    menu:
        "É o que qualquer um faria na situação.":


            mc "Eu não fiz nada de mais. Só o que qualquer pessoa faria naquela situação."

            h "Que bonotinho você achar que alguém arriscaria alguma coisa por alguém."

            mc "Não sei dos outros, mas eu não ia conseguir só deixar você lá pra morrer."
        "Você é única demais pra morrer.":


            $ hacker_amizade += 3

            mc "Eu sinto que você é especial demais pra morrer assim."

            mc "Mesmo que fosse pra ver você destruir o mundo, eu pagaria o preço pra ver você mais um pouco."

            h "!"

            h "Você tá falando sério?"

            mc "Acho que sim. Eu sei que parece meio brega, mas eu realmente quero ver você fazer o circo pegar fogo."

            mc "E se eu tiver do seu lado, vai ser mais legal ainda."

            h "Se esse é o tipo de coisa que você pensa... talvez a gente tenha até umas coisas em comum."
        "Não interessa. Eu tenho meus motivos.":


            $ hacker_amizade += 2

            mc "Eu tenho meus motivos. Você não precisa saber de tudo também."

            h "Tem razão... não é da minha conta."

    h "O que eu tô tentando falar é que você não precisava ter feito aquilo. E fez mesmo assim."

    h "Foi... legal da sua parte. Obrigada."

    mc "Valeu."

    if no2_especial:

        mc "Olha... lembra aquele lance que a gente conversou na janela do seu apê aquele dia?"

        h "Não."

        mc "Lembra, sim."

        h "Você me pegou de surpresa, eu fiquei sem jeito. Eu tava até gaguejando aquele dia. Que patético."

        mc "Não é patético, [h]. Era só uma coisa nova pra você."

        h "Hmm... que que tem?"

        mc "Aquele dia eu disse pra você ligar pra mim quando tivesse um dia ruim. Por que você não ligou?"

        scene no3_img22 with Dissolve(1.0)

        pause

        mc "U-uou."

        h "Não achei que você tivesse falando sério. Achei que... só fosse por educação."

        mc "Você não tá acostumada a contar com as pessoas. Você sempre fez tudo sozinha, não foi? Você vê todo mundo como parceiro de trabalho."

        mc "Por isso que não passa pela sua cabeça que alguém pode gostar de você por outras coisas."

        h "E você... você gosta? Isso aqui não é trabalho?"

        mc "É..."

        "Ela tem razão. O que eu tô fazendo aqui?"

        "Eu fui atencioso com ela, até dei em cima dela algumas vezes... mas eu nunca parei pra pensar no que eu sinto pela [h]."

        call namorando from _call_namorando_3

        if namorando:

            "Eu já tô namorando... eu já tenho uma pessoa especial na minha vida."

            "Mas eu não sei se eu consigo controlar o que eu sinto. A [h] também é uma garota muito especial. Quem sabe ela não é a mulher da minha vida?"
        else:


            "Eu não tô namorando ninguém. A [h] é uma garota muito especial. Quem sabe ela não é a mulher da minha vida?"

        "Ela é muito gata, é a garota mais inteligente que eu já vi. Ela tem esse monte de energia, mas é séria também."

        "Ela é maluca, eu não sei nada sobre ela, mas aposto que ia ser uma aventura viver com ela. Abrir essa Caixa de Pandora ia ser adrenalina pura."

        "Mas essa é uma decisão muito séria. Ela nunca se apaixonou eu acho... entrar nessa só pra brincar ia ser mancada."

        "O que eu quero? O que eu falo pra ela?"

        h "A-acabou a coragem? É mais do que trabalho ou não? Seja sincero."

        menu:
            "É mais do que trabalho. Muito mais.":


                $ nona_interesse = True

                mc "Eu não taria falando tudo isso pra você se fosse só trabalho. Eu quero mais de você. Eu quero você."

                h "V-você... como você tem coragem de falar esse tipo de coisa assim?"

                mc "Eu só tô sendo sincero com você. É o que eu tô sentindo de verdade."

                h "Esse negócio muito sério... é um pouco cedo pra mim."

                mc "Não tem problema. Eu espero você."

                h "Seu louco..."
            "A gente pode descobrir juntos.":


                $ nona_interesse = True

                mc "Eu não sei. Eu não sei se eu quero só tirar uma casquinha ou se é pra valer. A gente não experimentou isso ainda."

                h "Essa incerteza... ela é perigosa."

                mc "Mas não é gostoso quando a gente não sabe? A gente pode descobrir juntos o que a gente quer."

                h "Eu não gosto de coisa incerteza. Eu..."
            "Não é trabalho. É amizade.":


                mc "Não é trabalho. Eu não tenho nenhum objetivo com isso. Eu só quero ser seu amigo."

                h "Amigo? Só isso?"

                mc "É. É tão estranho assim?"

                h "Acho... que eu tenho uma visão meio deturpada dos homens. Amizade... é uma coisa diferente pra mim."

                mc "É uma coisa boa. Você vai ver."

                h "Confiar em alguém... que não quer nada em troca. Parece bom demais pra ser verdade."

                mc "Eu sei. É estranho existir uma coisa assim. Mas existe. Eu prometo que você pode confiar em mim."

                h "Eu vou tentar lembrar disso."

        if nona_interesse:

            h "Eu... eu não sei o que eu faço agora. Eu sempre sei o que eu tenho que fazer. Só que dessa vez eu não sei."

            mc "E se você só confiar em mim?"

            h "Eu não... eu não costumo fazer isso também."

            mc "Quer tentar? Me dá sua mão e fecha seus olhos."

            h "Você... eu posso confiar em você?"

            mc "Xiii... só fecha."

            scene black with dissolve

            h "E a-agora?"

            mc "Agora..."

            scene no3_img23 with Dissolve(1.0)

            pause

            h "A-ah..."

            "Ela tá tremendo. Que fofinha... como uma mina com essa idade fica tão tensa com um beijo desses?"

            "A [h] passou a vida fugindo disso. Nem acredito que eu tô podendo dar isso pra ela."

            "Eu quero fazer muito mais coisa com ela. Proteger ela e mostrar esse mundo cheio de prazer pra ela."

            h "E-eu... eu não sei fazer isso... desculpa."

            mc "Seu beijo é uma delícia. Igual você."

            h "N-não fala assim... ai..."

            mc "Deixa eu aproveitar mais um pouco."

            h "..."

            window hide

            pause

            scene no3_img22 with Dissolve(1.0)

            h "Então esse era seu objetivo..."

            mc "N-não!"

            h "Tô brincando, seu bobo. Você vai sofrer na minha mão se acreditar em tudo assim."

            mc "Eu tô vendo que vou mesmo."

            h "Bobo..."
    else:


        scene no3_img22 with Dissolve(1.0)

        pause

        h "Confiar em alguém assim não é normal pra mim, sabe?"

        mc "S-sei!"

    h "Depois de hoje, acho que eu vou ter confiar mais em você."

    mc "Pode, sim. Eu tô do seu lado. Eu não sei exatamente que você tá fazendo aqui na ilha, mas eu quero fazer o que é certo."

    mc "O que o [to] fez hoje não tá certo. Matar uma pessoa assim..."

    h "Vamos marcar com o [gar] um dia e eu vou te explicar tudo. Você agora faz parte do que a gente tá fazendo de forma oficial."

    scene no3_img24 with Dissolve(1.0)

    pause

    gar "Ora, se não é momento de celebração! Um novo membro para nossa nobre causa!"

    h "Ah, não. Eu não suporto ouvir você falando."

    gar "Peço perdão à senhorita se minha contribuição é demasiada impertinente. Nã-"

    h "Entendi. O que eu preciso é beber alguma coisa. E tomar um banho."

    gar "Tome a porta dos fundos. Leve o tempo que precisar para restaurar sua jovial e incrível aparência e energia."

    h "Eu vou lá. Boa sorte com ele."

    mc "E-ei!"

    gar "Enquanto você se desnuda em meu banho, e aquece seu corpo com o líquido refazedor, vou pegar um traje apropriado para sua figura."

    mc "Você tem roupa pra ela?"

    gar "Eis que ei de ter. Uma pessoa próxima deixou um vestido da última vez que passou aqui. Aposto que servirá adequadamente."

    h "Deixa lá no banheiro pra mim."

    gar "Farei isso."

    scene black with dissolve

    "..."

    gar "Aí vem ela."

    mc surpreso "!"

    scene no3_img25 with Dissolve(1.0)

    pause

    h "O que você tá olhando com essa cara?"

    menu:
        "Nada não...":


            mc envergonhado "Não é nada..."

            h "Quantos anos você tem?"
        "Ficou bem em você.":


            mc charmoso "Uou. Ele ficou muito bem em você."

            h "Ficou, né? Quase sem roupa sempre é melhor pelo jeito..."

            mc envergonhado "Você que tá falando."

    h "Não imaginava que sua irmã usou uma roupa assim."

    gar "É incomum realmente..."

    h "Ficou um pouco apertado aqui em baixo."

    gar "Sem dúvidas você conta com um volume um tanto mais avantajado que ela nessa região."

    h "Com certeza é melhor do que andar de calcinha e sutiã por aí."

    mc desculpa "Com certeza."

    mc charmoso "Mas é incrível que não ficou nenhuma marca. E você tirou todo o sangue."

    h "Sim. Eu fiquei surpresa também."

    mc preocupado "Mas pra onde você vai agora? Você não pode voltar pro apê."

    h "Eu vou ficar no apartamento aqui em cima do bar."

    gar "Será um prazer abrigar a senhorita."

    mc charmoso "Que bom."

    h "Vou ter que refazer o cabeamento, os roteadores, garantir que minha conexão não seja rastreável."

    h "Vou ter cuidado redobrado dessa vez."

    mc "E eu vou pra casa. Já tá quase amanhecenhdo."

    h "Vamos nos ver logo."

    mc "Vê se toma cuidado. Pensa um pouco na sua saúde também."

    h "Sim, senhor. Vou tentar."

    mc "Logo eu te chamo pra gente fazer alguma coisa."

    if nona_interesse:

        mc safado "Passar um tempo sozinho com você."

    h "A gente vai se falar."

    mc charmoso "Até a próxima."

    h "Até, [mc]..."

    gar "Estarei sempre às ordens, senhor."

    jump nona_e3_final

    label nona_e3_confessa:

        $ no3_confessa = True

        scene no3_img26 with Dissolve(1.0)

        pause

        h "Esse cara não sabe nada!"

        to "Muito bem. Vou ouvir o que você tem a dizer."

        h "Cala a boca! Para de falar como se você me conhecesse!"

        mc desculpa "Eu sei quem me tirou da prisão no dia do assalto. Isso eu posso garantir."

        to "Essa é uma informação muito valiosa. Quem foi?"

        mc serio "Foi uma juíza. O nome dela era... era [eli]."

        to "[eli] Richter. Você tem certeza?"

        mc "Tenho. Ela veio e falou com o policial. Ele não concordou muito com ela na hora. Parecia algo fora do protocolo."

        to "Isso é estranho. A juíza [eli] sempre pareceu uma mulher incorruptível. Uma das únicas que nunca conseguimos nada."

        h "..."

        to "Isso com certeza é importante pra nós."

        to "E essa aqui? É ou não a [h]? Se você puder me responder isso, vai tirar um grande peso das minhas costas."

        h "Eu nunca vi ele na vida!"

        menu:
            "Você vai poupar a vida dela?":


                $ nona_interrogatorio += 1

                mc desculpa "Se eu conseguir confirmar, você vai matar ela?"

                h "Você não pode confirmar nada! Cala a boca!"

                to "Calada. Diga e ela será poupada, [mc]. Eu não preciso matar ela. Só acabar com a rede dela é o suficiente pra mim."

                mc desculpa "Você não vai matar ela então?"

                to "Você tem a minha palavra."
            "Deixa eu pensar direito...":


                "Eu tenho certeza que é ela. Ela realmente é um pouco diferente da Carla, não sei como ela faz isso..."

                "Mas eu conheci ela como [h]. Então pra mim é óbvio que eles pegaram a mulher certa."

                "Agora... a questão é se eu quero ou não falar. Essa decisão pode mudar muita coisa."

        to "E então? É ela ou não?"

        menu:
            "Sim. É ela.":


                mc serio "Sim. Essa é a hacker chamada de [h]."

                to "Você está certo disso?"

                mc "Sim. Nós nos vimos antes, em um fliperama, quando ela se apresentou. Não tenho dúvidas disso."

                h "Ele tá inventando tudo isso! Vocês são loucos!"

                to "Era tudo o que eu precisava saber!"

                h "Não!"

                mc angustiado "[to]!"

                play sound "audio/som_17_tiro.mp3"

                scene red with vpunch

                pause

                scene no3_img14 with Dissolve(1.0)

                pause

                to "Um problema a menos."

                if nona_interrogatorio >= 3:

                    mc angustiado "Mas você disse que ia poupar a vida dela!"

                    to "Dá pra ver o quanto você se preoupa com ela, [mc]."

                    mc preocupado "Hm?"

                    to "Eu esperava que pudéssemos ser parceiros, mas você já foi cooptado."

                    mc angustiado "Eu?! E-eu não!"

                    to "É tarde demais pra qualquer coisa. Me perdoe."

                    mc "[to]! Eu não tô do lado de ninguém! Eu só quero viver uma vida aqui na cidade!{nw}"

                    play sound "audio/som_17_tiro.mp3"

                    scene red with vpunch

                    pause

                    scene black with Dissolve(3.0)

                    p "{i}tsc{/i}"

                    p "Vê se toma um pouco mais de cuidado, pelo amor..."

                    p "Eu preciso do [mc] pra conseguir toda a energia que eu preciso sem que ele fique louco."

                    p "Sabe quantas dezenas de anos eu espero por alguém que aguente manter a sanidade? Muitas!"

                    p "Então vê se toma cuidado para ele não acabar morto novamente."

                    if persistent.mc_sexo == "mulher":

                        p "É uma jogadora inútil mesmo..."
                    else:


                        p "É um jogador inútil mesmo..."

                    pause

                    $ renpy.full_restart()
                else:


                    mc desculpa "Você matou ela mesmo..."

                    to "Desculpa, mas eu sabia que você não tinha sangue frio o suficiente para entregar ela se eu falasse a verdade."

                    to "Foi sua fraqueza que me obrigou a mentir para você, não o contrário."

                    mc desculpa "..."

                    if no3_tony:

                        mc concentrando "Tem razão. No fim, o que eu queria era te ajudar mesmo. Estar do lado certo da história."

                        to "Excelente escolha, [mc]. Ficando do nosso lado, você ganhará muito. E eu tenho algo para você agora mesmo."

                        mc desconfiado "Hm?"

                        to "Venha até minha sala novamente. Vou te explicar com calma lá, enquanto peço ao [mar] para limpar a sujeira."

                        mc surpreso "O-ok!"

                        scene black with dissolve

                        "..."

                        scene no3_img27 with Dissolve(1.0)

                        pause

                        to "Eu sei o quanto é importante para vocês jornalistas ter informações quentes."

                        mc charmoso "Com certeza."

                        to "Então, eu tenho uma pra você. Uma que vai ajudar tanto nós quanto você."

                        to "Normalmente eu passaria para a Faux, mas em suas mãos ela pode ser ainda mais poderosa."

                        mc desconfiado "Você acha?"

                        to "Existem pessoas que desconfiam da ligação do prefeito com a Faux, então trazer por outra fonte pode aliviar nossa barra."

                        "Então realmente tem uma ligação entre eles..."

                        to "O Lucca é tio da minha falecida esposa e ele sempre foi muito importante para nós. Mas talvez seja hora de termos novos companheiros."

                        mc charmoso "Seria um prazer."

                        to "Muito bem, eu tenho aqui imagens e informações sobre a Cidade Chinesa. Descobrimos que eles fazem tráfico de pessoas."

                        mc preocupado "Isso é terrível."

                        to "Está na hora de isso vir a público. Tome aqui o dossiê que preparamos sobre isso. Publique quando quiser."

                        mc charmoso "Vou passar ao meu diretor e se for aprovado já vai pra revista."

                        to "Perfeito. Vamos garantir que nossa fonte na revista colabore na publicação também."

                        mc "Ok."

                        $ pautas += 1
                        $ tony_p1 = 1

                        to "Estamos encerrados por hoje. Agradeço novamente e boa sorte."

                        mc "Até mais, [to]."

                        to "E quando estiver sozinho, venha tomar uma taça de vinho comigo durante a noite na pizzaria."

                        mc "Quando der, eu apareço, sim."

                        to "Nos vemos em breve."

                        jump nona_e3_morta

                    to "Eu vou ter que encontrar outra forma de achar os comparsas dela. Nada me tira da cabeça que eles existem."

                    to "Agora temos um inimigo a menos para nossa cidade, não concorda?"

                    to "Eu vou voltar pra minha sala. Preciso conversar com algumas pessoas e definir o próximo passo."

                    to "Agradeço pela companhia, [mc]. Eu vou chamar o [mar], você pode pedir pra que ele se livre dela por favor?"

                    mc "T-tá..."

                    to "Até uma outra oportunidade."

                    jump nona_e3_morta
            "Eu não posso falar...":


                mc desculpa "Não posso confirmar isso. Eu realmente não sei..."

                to "É uma pena. Nesse caso, só me resta uma opção."

                h "Não!"

                mc angustiado "[to]!"

                play sound "audio/som_17_tiro.mp3"

                scene red with vpunch

                pause

                scene no3_img14 with Dissolve(1.0)

                pause

                to "Um problema a menos."

                mc preocupado "V-você matou ela!"

                to "Ela não ia falar, então pra mim não muda nada se ela está viva ou morta."

                to "Eu vou ter que encontrar outra forma de achar os comparsas dela. Nada me tira da cabeça que eles existem."

                to "E se realmente esta mulher era a [h], é um inimigo a menos para nossa cidade, não concorda?"

                menu:
                    "E se não fosse ela?":


                        mc "Mas e se não fosse ela? Então uma mulher inocente morreu."

                        to "Eu sei que isso pode parecer horrível para você neste ponto, mas as formigas operárias se sacrificam pela rainha."

                        to "A ovelha se subjuga ao pastor, e o animal se transforma em comida para o homem."

                        to "Essa mulher fez o papel dela no grande esquema das coisas. Ela morreu com honra."

                        "Incrível como ele consegue encontrar uma razão de justiça depois de matar alguém a sangue frio."

                        mc desculpa "..."
                    "Tem razão...":


                        mc charmoso "Você tá certo. O que mais importa vem primeiro."

                        to "Exatamente. É importante termos prioridades na vida. Focar no objetivo e não se deixar abalar durante o caminho."

                        to "Fazendo o que for necessário pra ser bem sucedido, você chegará longe."

                        mc "Obrigado."

                to "Eu vou voltar pra minha sala. Preciso conversar com algumas pessoas e definir o próximo passo."

                to "Agradeço pela companhia, [mc]. Ah. Pode fazer um último favor pra mim?"

                mc "O que é?"

                to "Eu vou chamar o [mar], você pode pedir pra que ele se livre dela por favor?"

                mc "T-tá..."

                to "Até uma outra oportunidade."

                scene black with dissolve

                scene no3_img15 with Dissolve(1.0)

                pause

                mc "Desculpa... eu devia ter falado alguma coisa pra fazer ele parar."

                mc "Eu não queria jogar toda sua luta no lixo. Acho que no fim eu pensei que você fosse aguentar. Desculpa, de verdade."

                mc "Se eu tivesse uma forma de voltar no tempo, eu voltaria e faria alguma coisa diferente."

                mc "Espero que seus amigos me perdoem. Adeus."

                jump nona_e3_morta

    label nona_e3_morta:

        $ nona_e3 = "morta"

        scene black with dissolve

        "Eu não consegui salvar ela... o [gar] não vai gostar de saber, mas foi o caminho que eu escolhi."

        "..."

        scene pub geral with Dissolve(1.0)

        "..."

        mc concentrando "E foi isso que aconteceu..."

        gar "..."

        mc "Desculpa."

        gar "O senhor devia ter contado com a ajuda deste humilde servo antes de decidir o rumo da terrível situação."

        mc "..."

        gar "No entanto, não tenho como culpar seus esforços, valiosos que foram. Estou imensamente em débito com o senhor."

        mc "Eu não fiz nada, então não vou cobrar nada de você também. Ficamos no zero a zero."

        gar "Se o senhor julga o melhor. Não tenho objeções."

        mc concentrando "Até outro dia, [gar]."

        gar "Nos veremos em breve, lorde [mc]."

        jump nona_e3_final

    label nona_e3_final:

        pass

    if nona_e3 == "desistiu":

        scene black with dissolve

        "Eu vou fazer coisa melhor da minha vida e ficar longe de problema."

        "..."

        "Passar o dia na praia! Isso sim é saber escolher!"

        "O que será que era aquela história do [gar]? Bom... deixa pra lá."
    else:


        scene mc_povo_noite with Dissolve(1.0)

        pause

        "Eu sabia que aquele calafrio não era coisa boa..."

        "Esse deve ter sido o dia mais estressante da minha vida!"

        "Eu vou precisar de um tempo pra digerir tudo o que aconteceu hoje."

        "Acho que o melhor é só eu tentar dormir e depois eu penso no resto..."

        "Depois de hoje... o que mais pode acontecer nessa merda de cidade?"



    $ tempo = 4

    $ v52_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v52_fim","final","local")

    scene black with Dissolve(3.0)

    call checa_final from _call_checa_final_14

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
