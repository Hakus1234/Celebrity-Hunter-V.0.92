label daily_random:

    $ randaily = renpy.random.randint(1,100)

    if randaily <= 25:

        $ celeste_on = False
        $ stifler_on = True
        $ xiang_on = False

    elif randaily > 25 and randaily <= 50:

        $ celeste_on = False
        $ stifler_on = False

        if xiang_escape < 5:

            $ xiang_on = True
        else:


            $ xiang_on = False

    elif randaily > 50 and randaily <= 75:

        $ celeste_on = False
        $ stifler_on = True

        if xiang_escape < 5:

            $ xiang_on = True
        else:


            $ xiang_on = False

    elif randaily > 75 and randaily <= 100:

        $ celeste_on = True
        $ stifler_on = False
        $ xiang_on = False
        $ fenju_treino = False

    if randaily <= 2:

        $ lua_especial = True

    $ randtreino = renpy.random.randint(1,100)

    if randtreino <= 60:

        $ treino_sucesso = True
    else:


        $ treino_sucesso = False

    return

label comprar_cash:

    if renpy.variant("android"):

        $ userlogado = PythonSDLActivity.pegaLogado();

        if not userlogado:

            "{b}Você precisa ter feito login em uma conta para comprar{/b}"

            "{b}Ter uma conta é essencial para que seus créditos fiquem protegidos na nuvem{/b}"

            menu:
                "Fazer login":


                    call fazer_login

                    "{b}Muito bem{/b}"
                "Não quero":


                    "{b}Quando quiser comprar algo e ter sucesso rápido, basta voltar{/b}"

                    return

        if renpy.variant("android"):

            $ email = PythonSDLActivity.pegaEmail()
            $ uid = PythonSDLActivity.pegaUid()





    "{b}Você receberá os C$ comprados imediatamente após a confirmação do pagamento{/b}"

    menu:
        "Comprar {b}CR$ 250{/b} por {b}R$ 4,90{/b}":


            $ renpy.run(OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/6162f34edb7f4db7b58d'))
        "Comprar {b}CR$ 1.000{/b} por {b}R$ 17,90{/b}":


            $ renpy.run(OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/20d774d587a142c78b9a'))
        "Comprar {b}CR$ 2.000{/b} por {b}R$ 29,90{/b}":


            $ renpy.run(OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/1060ff0d8ff64c818c35'))
        "Agora não":


            return

    "{b}Viu a mensagem verde de pagamento confirmado? Você pode pegar os créditos comprados agora mesmo ou depois no menu{/b}"

    menu:
        "Opa! Passa aí!":


            call carrega_compra2
        "Eu ainda não paguei.":


            "{b}Sem problemas. Você pode pagar lá no seu navegador ou iniciar uma nova compra. O que for melhor{/b}"

            "{b}Se for pagar depois, você pode pegar elas pelo menu, apertando em LOJA e depois ATUALIZAR CRÉDITOS{/b}"

            "{b}Depois aproveite sua enorme quantidade de grana para fazer o que quiser na capital{/b}"







    return

label comprar_coins:



    if renpy.variant("android"):

        $ userlogado = PythonSDLActivity.pegaLogado();

        if not userlogado:

            "{b}Você precisa ter feito login em uma conta para comprar{/b}"

            "{b}Ter uma conta é essencial para que seus créditos fiquem protegidos na nuvem{/b}"

            menu:
                "Fazer login":


                    call fazer_login

                    "{b}Muito bem{/b}"
                "Não quero":


                    "{b}Quando quiser comprar algo e ter sucesso rápido, basta voltar{/b}"

                    return

        if renpy.variant("android"):

            $ email = PythonSDLActivity.pegaEmail()
            $ uid = PythonSDLActivity.pegaUid()





    "{b}Você receberá os Celebrity Coins comprados imediatamente após a confirmação do pagamento{/b}"

    "{b}Celebrity Coins ou o que você comprou com elas permanecem com você mesmo que você reinicie o jogo{/b}"

    menu:
        "Comprar {b}10.000 Celebrity Coins{/b} por {b}R$ 9,90{/b}":






            $ renpy.run(OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/e48c202266f44868b8ca'))
        "Agora não":


            return

    "{b}Viu a mensagem verde de pagamento confirmado? Você pode pegar os créditos comprados agora mesmo ou depois no menu{/b}"

    menu:
        "Opa! Passa aí!":


            call carrega_compra2
        "Eu ainda não paguei.":


            "{b}Sem problemas. Você pode pagar lá no seu navegador ou iniciar uma nova compra. O que for melhor{/b}"

            "{b}Se for pagar depois, você pode pegar elas pelo menu, apertando em LOJA e depois ATUALIZAR CRÉDITOS{/b}"

            "{b}Depois aproveite sua enorme quantidade de grana para fazer o que quiser na capital{/b}"

    "{b}Se você confirmou o pagamento, deve receber suas Celebrity Coins assim que nossa equipe adicionar em sua conta. Isso pode demorar de alguns minutos até algumas horas{/b}"

    "{b}Se você não receber o produto que você comprou em até 24 horas, entre em contato pelo site {a=http://www.geiko.net/suporte}celebrityhunter.com.br/suporte{/a} e resolvemos seu problema{/b}"

    "{b}Obrigado por contribuir com o desenvolvimento de Celebrity Hunter{/b}"

    return

label anuncio:

    return

    python:
        if renpy.android:
            adblock = PythonSDLActivity.pegaAnuncio()

    if not adblock:

        menu:
            "Ver anúncio e continuar":


                python:
                    if renpy.android:
                        PythonSDLActivity.loadAD()
            "Comprar removedor de anúncios":


                p rindo "Com o removedor de anúncios, você não precisará mais ver ADs em nenhum momento do jogo."

                p "Você ainda auxilia no desenvolvimento de CH pra que ele tenha mais atualizações e com mais conteúdo."

                $ iap.purchase("sem_anuncio")

                p "Se você comprou o removedor com sucesso, talvez você precise reiniciar o game para ele fazer efeito."

                p "Salve seu game antes para não perder nada, hein?"

                jump anuncio
            "Por que existem anúncios?":


                p lecionando "Celebrity Hunter é um jogo gratuito, não é? Mesmo sem cobrar nada dos jogadores pra baixar, o jogo tem seus custos."

                p "Para que o jogo seja desenvolvido, ele precisa de novos gráficos, história, programação, publicação e muitas outras coisas."

                p "Como CH é feito por uma única pessoa, todo ad que você vê ou produto que você compra, ajuda o jogo a continuar sendo atualizado."

                p "Ninguém gosta de anúncios e se ele atrapalha demais, compre o {b}Removedor de Anúncios{/b}. Ele vai melhorar muito seu gameplay."

                p rindo "Espero que tenha ficado claro. E se não ficou, azar o seu."

                jump anuncio

        return
    else:


        return

label checa_tempo:

    if not renpy.android:
        $ checatempo = True
        return

    python:
        if renpy.android:
            PythonSDLActivity.pegaTempo()

    $ renpy.pause(delay=1, hard=True)

    python:
        if renpy.android:
            checatempo = PythonSDLActivity.checaTempo()

    $ renpy.pause(delay=1, hard=True)

    if not checatempo:

        $ renpy.notify("Conectando...")

        python:
            if renpy.android:
                PythonSDLActivity.pegaTempo()

        $ renpy.pause(delay=2, hard=True)

        python:
            if renpy.android:
                checatempo = PythonSDLActivity.checaTempo()

        $ renpy.pause(delay=2, hard=True)

        if not checatempo:

            $ renpy.notify("Pegando dados do servidor...")

            python:
                if renpy.android:
                    PythonSDLActivity.pegaTempo()

            $ renpy.pause(delay=2, hard=True)

            python:
                if renpy.android:
                    checatempo = PythonSDLActivity.checaTempo()

            $ renpy.pause(delay=2, hard=True)

            if not checatempo:

                "{b}Sua conexão com o servidor está lenta. Tentando conectar novamente...{/b}"

                python:
                    if renpy.android:
                        PythonSDLActivity.pegaTempo()

                $ renpy.pause(delay=2, hard=True)

                python:
                    if renpy.android:
                        checatempo = PythonSDLActivity.checaTempo()

                $ renpy.pause(delay=2, hard=True)

                if not checatempo:

                    "{b}Não foi possível recuperar o horário do servidor.{/b}"

                    "{b}Confirme se você está conectado a internet e logado em sua conta e tente novamente em instantes.{/b}"

                    return
                else:


                    return
            else:


                return
        else:


            return
    else:


        return

label checa_logado:

    python:
        if renpy.android:
            userlogado = PythonSDLActivity.pegaLogado();

    if not userlogado:

        "{b}Você precisa estar conectado à internet e logado em sua conta para jogar este conteúdo.{/b}"

        "{b}Conecte-se agora e vamos tentar fazer login em sua conta.{/b}"

        "{b}...{/b}"

        python:
            if renpy.android:
                PythonSDLActivity.abreLogin()

        "{b}...{/b}"

        "{b}...{/b}"

        python:
            if renpy.android:
                userlogado = PythonSDLActivity.pegaLogado();

        if userlogado:

            "{b}Você logou em sua conta com sucesso. Bem vindo!{/b}"

            if renpy.variant("android"):

                $ email = PythonSDLActivity.pegaEmail()
                $ uid = PythonSDLActivity.pegaUid()
            else:


                $ uid = 'bVbI097gRCOHp1Mh2M9zgZJQ2of2'
        else:


            "{b}Não conseguimos te conectar à sua conta. Tente novamente mais tarde.{/b}"

    return

label ganha_daily:

    call checa_tempo from _call_checa_tempo_7

    python:
        if renpy.android:
            daily = PythonSDLActivity.checkDailyNext()

        renpy.notify("Checando se você já pode pegar moedas")

        renpy.pause(delay=2, hard=True)

    if daily:
        python:
            if renpy.android:
                PythonSDLActivity.setDaily()
                PythonSDLActivity.addCoins(50)
                PythonSDLActivity.registraEvento("recebeu_daily","ganhou","daily")

        $ renpy.notify("Parabéns! Você recebeu 50 Celebrity Coins! Volte daqui 24 horas para pegar novamente.")
    else:


        $ renpy.notify("Você já recebeu suas moedas diárias. Volte em 24 horas para pegar novamente.")

    $ renpy.block_rollback()

    call screen menu_lojacartas

    return

label avanca_massagem:

    if persistent.coins >= 300:

        python:
            if renpy.android:
                PythonSDLActivity.liberaAulaMas()
                persistent.coins = PythonSDLActivity.usaMoedas(300)
                PythonSDLActivity.registraEvento("comprou_aula_massagem","massagem","aula")

        $ renpy.block_rollback()

        play sound "extra/carta.mp3"

        "{b}Você usou 300 Celebrity Coins{/b}"

        $ renpy.notify("Próxima aula liberada com sucesso.")
    else:


        p "Infelizmente você não tem {b}Celebrity Coins{/b} suficientes para liberar a próxima aula."

        p "Você pode conseguir moedas facilmente vendo vídeos na {b}Loja de Cartas{/b} ou comprando na nossa {b}Loja{/b}."

        show seta with vpunch

        p "Só clicar no botão {b}Menu{/b} aqui no canto inferior direito."

        p "Você também pode esperar as {b}8 horas{/b} terminarem. Ainda estaremos por aqui!"

        hide seta

    jump karli_curso

    return

label fazer_login:

    python:
        if renpy.android:
            PythonSDLActivity.abreLogin()

    if userlogado:

        if renpy.variant("android"):

            $ email = PythonSDLActivity.pegaEmail()
            $ uid = PythonSDLActivity.pegaUid()

    return

label fazer_login_menu:

    hide screen menu_loja with Dissolve(0.5)

    python:
        if renpy.android:
            PythonSDLActivity.abreLogin()

    "{b}Entrando na sua conta...{/b}"

    python:
        if renpy.android:
            userlogado = PythonSDLActivity.pegaLogado();

        else:
            
            userlogado = True

    if userlogado:

        "{b}Você entrou em sua conta com sucesso!{/b}"

        if renpy.variant("android"):

            $ email = PythonSDLActivity.pegaEmail()
            $ uid = PythonSDLActivity.pegaUid()

    show screen menu_loja with Dissolve(0.5)

    pause

    return

label login_convidado:





    return

label checar_celular:

    if iconchefe >= 5:

        $ hora_pauta = True

    if not priscila_cel_msg1 and not priscila_cel_msg2:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ priscila_cel_msg2 = True
        $ priscila_cel_msg2_n = True
        $ quem_ligou = "priscila"

    elif julia_e6 == "passeio" and not ligacao_ativa:

        $ julia_e6 = "passeio_inicia"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v17_fim and not v18_fim and j4_roupa and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif not sayuri_evento1_check and sayuri_cel_msg1_resposta_check and not sayuri_cel_msg1 and not ligacao_ativa:

        $ sayuri_cel_msg1 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "sayuri"

    elif cassia_aceitou and not cassia_cel_msg1 and not ligacao_ativa:

        $ cassia_cel_msg1 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "cassia"

    elif dia >= dia_cassia and not cassia_aceitou and not cassia_cel_msg2 and not ligacao_ativa:

        $ cassia_cel_msg2 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "cassia"

    elif dia >= dia_sayuri and not ligacao_ativa and not julia_cel_msg1:

        $ julia_cel_msg1 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "julia"

    elif v4_fim and priscila_e3_check == "nada" and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ priscila_e3_check = "iniciado"

    elif not julia_e1 == "nada" and not sayuri_cel_msg3 and not ligacao_ativa:

        $ sayuri_cel_msg3 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "sayuri"

    elif ( sayuri_cel_msg3_r != "nada" or not sayuri_e3 == "nada" ) and not sayuri_e3 == "horrivel" and not julia_cel_msg3 and tempo < 3 and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ julia_cel_msg3 = True
        $ julia_cel_msg3_evento = True
        $ quem_ligou = "julia"

    elif julia_cel_msg3 and julia_e2 == "nada" and not ligacao_ativa:

        $ julia_e2 = "iniciando"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif (cassia_nathan_naoajudou or cassia_nathan_entregou) and v4_fim and tempo == 1 and not ligacao_ativa and not cassia_cel_msg3:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ cassia_cel_msg3 = True
        $ quem_ligou = "cassia"

    elif v6_fim and priscila_e4_check == "nada" and not ligacao_ativa:

        $ priscila_e4_check = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v8_fim and not sayuri_cel_msg4 and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ sayuri_cel_msg4 = True
        $ quem_ligou = "sayuri"

    elif v11_fim and julia_e3 == "nada" and not ligacao_ativa:

        $ julia_e3 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif diana_e1 == "aceitou" and cassino_evento == "nada" and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ cassino_evento = "iniciado"

    elif diana_atencao == 1 and not diana_cel_msg1 and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ diana_cel_msg1 = True
        $ quem_ligou = "diana"

    elif diana_e2_roupa and not diana_e2_roupa_evento and not v13_fim and not ligacao_ativa:

        $ diana_e2_roupa = False
        $ diana_e2_roupa_evento = True
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v9_fim and dia >= dia_cassia and nathan_e3 == "nada" and tempo < 3 and not ligacao_ativa:

        $ nathan_e3 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v10_fim and not priscila_cel_msg6 and not ligacao_ativa:

        $ priscila_e5 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "priscila"

    elif v12_fim and sayuri_e5 == "nada" and tempo == 1 and not ligacao_ativa:

        $ sayuri_e5 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v17_fim and julia_e4 == "nada" and not ligacao_ativa:

        $ julia_e4 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v14_fim and dia >= dia_cassia and not nathan_cel_msg3 and tempo < 3 and not ligacao_ativa:

        $ nathan_numero = True
        $ nathan_cel_msg3 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "nathan"

    elif v16_fim and not priscila_cel_msg7 and tempo == 1 and not ligacao_ativa:

        $ priscila_e6 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ priscila_cel_msg7 = True
        $ quem_ligou = "priscila"

    elif v17_fim and not sayuri_cel_msg5 and tempo == 1 and not sayuri_e5 == "badending" and not ligacao_ativa:

        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ sayuri_cel_msg5 = True
        $ quem_ligou = "sayuri"

    elif v18_fim and not julia_cel_msg6 and tempo == 3 and not ligacao_ativa:

        $ julia_cel_msg6 = True
        $ julia_e5 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "julia"

    elif (persistent.gadgetbeta or gadgetbeta) and (persistent.gadgetalfa or gadgetalfa) and (persistent.gadgetgama or gadgetgama) and not gadget_final and v23_fim and not ligacao_ativa:

        $ cena_gadget = True
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v23_fim and not priscila_e6_ligacao_check and tempo != 1 and not ligacao_ativa:

        $ priscila_e6_ligacao_check = True
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v19_fim and diana_e4 == "nada" and not ligacao_ativa:

        $ diana_e4 = "comecou"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v20_fim and not nathan_cel_msg4 and tempo == 2 and not ligacao_ativa:

        $ nathan_numero = True
        $ nathan_cel_msg4 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "nathan"

    elif v28_fim and nona_e1 == "nada" and tempo == 1 and not ligacao_ativa:

        $ nona_e1 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif priscila_e6_ligacao_check and priscila_e7 == "nada" and tempo == 1 and not ligacao_ativa:

        $ priscila_e7 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v24_fim and sayuri_e7 == "nada" and tempo == 1 and not ligacao_ativa:

        $ sayuri_e7 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v25_fim and julia_e6 == "nada" and tempo == 1 and not ligacao_ativa:

        $ julia_e6 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v26_fim and diana_e5 == "nada" and tempo == 3 and not ligacao_ativa:

        $ diana_e5 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v27_fim and not nathan_cel_msg5 and not ligacao_ativa:

        $ nathan_numero = True
        $ nathan_cel_msg5 = True
        $ celular_notificacao = True
        $ ligacao_ativa = True
        $ quem_ligou = "nathan"

    elif v30_fim and nona_e2 == "nada" and tempo == 1 and not ligacao_ativa:

        $ nona_e2 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif sofia_e1 != "nada" and naru_e1 == "nada" and tempo == 1 and not ligacao_ativa:

        $ naru_e1 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v31_fim and dia >= dia_priscila and priscila_e8 == "nada" and tempo < 3 and not ligacao_ativa:

        $ priscila_e8 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v32_fim and sayuri_e8 == "nada" and tempo == 1 and not ligacao_ativa:

        $ sayuri_e8 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v33_fim and julia_e7 == "nada" and tempo == 1 and not ligacao_ativa:

        $ julia_e7 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v34_fim and diana_e6 == "nada" and tempo == 3 and not ligacao_ativa:

        $ diana_e6 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v35_fim and nathan_e7 == "nada" and tempo < 3 and not ligacao_ativa:

        $ nathan_e7 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v37_fim and natasha_e4 == "nada" and tempo == 1 and not ligacao_ativa:

        $ natasha_e4 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v38_fim and nona_e3 == "nada" and tempo == 1 and not ligacao_ativa:

        $ nona_e3 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v40_fim and dia >= dia_priscila and priscila_e9 == "nada" and tempo < 3 and not ligacao_ativa:

        $ priscila_e9 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v52_fim and dia >= dia_priscila and priscila_e9 == "evento" and tempo == 1 and not ligacao_ativa:

        $ priscila_e9 = "iniciado2"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v53_fim and not v54_fim and tempo == 1 and not ligacao_ativa:

        $ priscila_e9 = "iniciado3"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v41_fim and sayuri_e9 == "nada" and tempo == 1 and not ligacao_ativa:

        $ sayuri_e9 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v33_fim and v42_fim and v54_fim and julia_v8 == "nada" and not ligacao_ativa:

        $ julia_v8 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif julia_v8 == "evento" and tempo == 3 and not ligacao_ativa:

        $ julia_v8 = "iniciado2"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif not julia_final3 and caio_prometeu > 0 and not julia_final1 and not ligacao_ativa:

        $ julia_v8 = "final3"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif not julia_final3 and julia_segredo and not julia_final1 and not julia_completo and not ligacao_ativa and tempo < 3:

        $ julia_v8 = "final2_final"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif v43_fim and diana_e7 == "nada" and (julia_final3 == True or julia_final2 == True) and not ligacao_ativa:

        $ diana_e7 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif premium and v45_fim and nathan_e8 == "nada" and (diana_final3 == True or diana_final2 == True) and tempo < 3 and not ligacao_ativa:

        $ nathan_e8 = "iniciado"
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif premium and v45_fim and sofia_evento6 == 0 and (nathan_final3 == True or nathan_final2 == True) and tempo < 3 and not ligacao_ativa:

        $ sofia_evento6 = 1
        $ celular_notificacao = True
        $ ligacao_ativa = True

    elif premium and v45_fim and sofia_evento6 == 2 and tempo < 3 and not ligacao_ativa:

        $ sofia_evento6 = 3
        $ celular_notificacao = True
        $ ligacao_ativa = True







    return

    label mostra_video:

        python:
            if renpy.android:
                PythonSDLActivity.loadVID()

        call screen mostra_video

        return

    label compra_carta:






        $ randnum = renpy.random.randint(1,100)

        if randnum <= 80:

            $ carta_estrela = "1estrela"
            $ carta_1estrela_max = 1015

            $ carta_escolhida = renpy.random.randint(1001,carta_1estrela_max)

        elif randnum >= 81 and randnum <= 97:

            $ carta_estrela = "2estrelas"
            $ carta_2estrelas_max = 510

            $ carta_escolhida = renpy.random.randint(501,carta_2estrelas_max)

        elif randnum >= 98:

            $ carta_estrela = "3estrelas"
            $ carta_3estrelas_max = 5

            $ carta_escolhida = renpy.random.randint(1,carta_3estrelas_max)



        $ carta_nome_1 = "Pixie: Voando em Fadolândia"
        $ carta_nome_2 = "Sayuri: Não consigo dormir"
        $ carta_nome_3 = "Priscila: Vida de celebridade"
        $ carta_nome_4 = "Karli: Minha vez de ser massageada"
        $ carta_nome_5 = "Celebrity Hunter: Um alô de todos!"
        $ carta_nome_501 = "Priscila: Baixa Tolerância"
        $ carta_nome_502 = "Celebrity Hunter: Capa Alternativa"
        $ carta_nome_503 = "Sayuri: Por favor me segure"
        $ carta_nome_504 = "Júlia: Não pare agora"
        $ carta_nome_505 = "Sayuri: Minha lição de casa"
        $ carta_nome_506 = "Nathan: Drinque Especial"
        $ carta_nome_507 = "Priscila: E meu amor verdadeiro?"
        $ carta_nome_508 = "Júlia: Palestra chata"
        $ carta_nome_509 = "Karli: Massagem completa"
        $ carta_nome_510 = "Priscila: Um alô dos céus"
        $ carta_nome_1001 = "Chefe: Cadê a Pauta?!"
        $ carta_nome_1002 = "Sayuri: Dançando no Templo"
        $ carta_nome_1003 = "Priscila: Meu Teste"
        $ carta_nome_1004 = "Priscila: Será que ele vai gostar?"
        $ carta_nome_1005 = "Sayuri: Você realmente veio!"
        $ carta_nome_1006 = "Priscila: Toca em mim"
        $ carta_nome_1007 = "Nathan: Rei do Bar"
        $ carta_nome_1008 = "Priscila: E agora o que eu faço?"
        $ carta_nome_1009 = "Pixie: A fada mais sexy do mundo"
        $ carta_nome_1010 = "Mensagens e mais mensagens"
        $ carta_nome_1011 = "Júlia: Só pra você"
        $ carta_nome_1012 = "Cássia: Eu mando em você"
        $ carta_nome_1013 = "Karli: Pode começar com o Kita"
        $ carta_nome_1014 = "Priscila: Eu amei minha bolona!"
        $ carta_nome_1015 = "Priscila: O por do sol da verdade"



        if carta_escolhida == 1:

            $ persistent.card_1 = True
            $ carta_nome = carta_nome_1

        elif carta_escolhida == 2:

            $ persistent.card_2 = True
            $ carta_nome = carta_nome_2

        elif carta_escolhida == 3:

            $ persistent.card_3 = True
            $ carta_nome = carta_nome_3

        elif carta_escolhida == 4:

            $ persistent.card_4 = True
            $ carta_nome = carta_nome_4

        elif carta_escolhida == 5:

            $ persistent.card_5 = True
            $ carta_nome = carta_nome_5

        elif carta_escolhida == 501:

            $ persistent.card_501 = True
            $ carta_nome = carta_nome_501

        elif carta_escolhida == 502:

            $ persistent.card_502 = True
            $ carta_nome = carta_nome_502

        elif carta_escolhida == 503:

            $ persistent.card_503 = True
            $ carta_nome = carta_nome_503

        elif carta_escolhida == 504:

            $ persistent.card_504 = True
            $ carta_nome = carta_nome_504

        elif carta_escolhida == 505:

            $ persistent.card_505 = True
            $ carta_nome = carta_nome_505

        elif carta_escolhida == 506:

            $ persistent.card_506 = True
            $ carta_nome = carta_nome_506

        elif carta_escolhida == 507:

            $ persistent.card_507 = True
            $ carta_nome = carta_nome_507

        elif carta_escolhida == 508:

            $ persistent.card_508 = True
            $ carta_nome = carta_nome_508

        elif carta_escolhida == 509:

            $ persistent.card_509 = True
            $ carta_nome = carta_nome_509

        elif carta_escolhida == 510:

            $ persistent.card_510 = True
            $ carta_nome = carta_nome_510

        elif carta_escolhida == 1001:

            $ persistent.card_1001 = True
            $ carta_nome = carta_nome_1001

        elif carta_escolhida == 1002:

            $ persistent.card_1002 = True
            $ carta_nome = carta_nome_1002

        elif carta_escolhida == 1003:

            $ persistent.card_1003 = True
            $ carta_nome = carta_nome_1003

        elif carta_escolhida == 1004:

            $ persistent.card_1004 = True
            $ carta_nome = carta_nome_1004

        elif carta_escolhida == 1005:

            $ persistent.card_1005 = True
            $ carta_nome = carta_nome_1005

        elif carta_escolhida == 1006:

            $ persistent.card_1006 = True
            $ carta_nome = carta_nome_1006

        elif carta_escolhida == 1007:

            $ persistent.card_1007 = True
            $ carta_nome = carta_nome_1007

        elif carta_escolhida == 1008:

            $ persistent.card_1008 = True
            $ carta_nome = carta_nome_1008

        elif carta_escolhida == 1009:

            $ persistent.card_1009 = True
            $ carta_nome = carta_nome_1009

        elif carta_escolhida == 1010:

            $ persistent.card_1010 = True
            $ carta_nome = carta_nome_1010

        elif carta_escolhida == 1011:

            $ persistent.card_1011 = True
            $ carta_nome = carta_nome_1011

        elif carta_escolhida == 1012:

            $ persistent.card_1012 = True
            $ carta_nome = carta_nome_1012

        elif carta_escolhida == 1013:

            $ persistent.card_1013 = True
            $ carta_nome = carta_nome_1013

        elif carta_escolhida == 1014:

            $ persistent.card_1014 = True
            $ carta_nome = carta_nome_1014

        elif carta_escolhida == 1015:

            $ persistent.card_1015 = True
            $ carta_nome = carta_nome_1015

        python:
            if renpy.android:
                PythonSDLActivity.ganhaCarta(carta_escolhida)
                persistent.coins = PythonSDLActivity.usaMoedas(10)
                PythonSDLActivity.registraEvento("carta_sorteada","compra","carta")

        play sound "extra/carta.mp3"

        call screen compra_carta

        return

    label mostrar_janelas:

        window show
        $ show_quick_menu = True

        $ renpy.rollback()

        return

label musica_play:





    play music "extra/music_1.mp3"



    return

label musica_stop:

    stop music

    call screen menu_celular_musica



label salvar_jogo:

    python:
        if renpy.android:
            PythonSDLActivity.salvaHist()

    return

    label carregar_jogo:

        $ persistent.loading = True
        $ renpy.load("continue")

    label call_cidade:

















        scene black with dissolve

        call checar_celular from _call_checar_celular

        $ proibido_salvar = False
        $ show_quick_menu = True
        $ fundo_especial = False

        stop sound
        stop music

        $ renpy.free_memory()
        $ renpy.stop_predict("cidade *")
        $ renpy.stop_predict("images/mapa/*.*")
        $ renpy.stop_predict("extra/*.*")
        $ renpy.stop_predict("/extra/*.*")
        $ renpy.stop_predict("celular/*.*")
        $ renpy.stop_predict_screen( "menu_celular" )
        $ renpy.stop_predict_screen( "menu_sidebar" )
        $ renpy.stop_predict_screen( "menu_novidades" )
        $ renpy.stop_predict_screen( "menu_album" )
        $ renpy.stop_predict_screen( "cidade_tela" )
        $ renpy.stop_predict_screen( "celular_mc" )

        if renpy.variant("mobile"):

            if cidade_vez >= 4:





                $ cidade_vez = 0

            $ cidade_vez += 1

        $ chovendo = False

        $ rand_musica = renpy.random.randint(1,100)

        if rand_musica >= 91:

            $ chovendo = True

        if tempo < 3:

            if rand_musica > 0 and rand_musica <= 45:

                play sound "audio/som_11_cidadedia_1.mp3"

            elif rand_musica >= 46 and rand_musica <= 90:

                play sound "audio/som_11_cidadedia_2.mp3"

            elif rand_musica >= 91:

                play sound "audio/som_11_cidadedia_3.mp3"

            if tempo == 1:



                scene ilha base with Dissolve(1.0)

            if tempo == 2:



                scene ilha base with Dissolve(1.0)
        else:


            play sound "audio/som_5_cidadenoite.mp3"



            scene ilha base with Dissolve(1.0)

        $ estou_na_cidade = True

        call screen cidade 

    label dormir:

        $ estou_na_cidade = False

        if not dormir_em_casa:

            if tempo < 3:

                scene mapa cidade
            else:


                scene mapa cidade_noite

            mc triste "Meu Deus, olha a hora..."

            mc concentrando "Não consigo fazer mais nada. Preciso ir pra casa antes que eu capote na rua."

            "..."

        if casa:

            pass
        else:




















            scene apartamento cama with Dissolve(1.0)

            mc concentrando "A cama tá chamando..."

        "..."

        scene black with Dissolve(2.0)

        "z{size=20}{i}z{/i}{/size}{size=18}{i}z{/i}{/size}{size=16}{i}z{/i}{/size}{size=14}{i}z{/i}{/size}{size=12}{i}z{/i}{/size}{size=10}{i}z{/i}{/size}"

        $ dormir_em_casa = False
        $ tempo = 1
        $ karli_evento_dia = False
        $ xiang_evento_dia = False
        $ aviso_chefe = True
        $ dia += 1
        $ lua_especial = False





        jump acordar

    label acordar:

        menu:
            "Visitar a [p] em Fadolândia":


                call cenario_fadolandia from _call_cenario_fadolandia
            "Acordar":


                pass

        call daily_random from _call_daily_random

        $ renpy.save("None-continue", extra_info="None-continue")

        python:
            if renpy.android:
                renpy.block_rollback()

        call anuncio from _call_anuncio_6

        if casa:

            scene ap quarto with dissolve
        else:


            scene apartamento cama with Dissolve(2.0)

        "..."

        $ proibido_salvar = False
        $ show_quick_menu = True

        if nathan_cel_msg1 and not nathan_cel_msg1_r:

            $ nathan_cel_msg1_r = True

            "Caraca... o que aconteceu ontem?"

            mc triste "Não consigo me lembrar de nada..."

            mc "E minha cabeça tá me matando."

            "Opa... Parece que eu tenho uma mensagem nova."

            scene apartamento cama_celular with dissolve

            "É uma mensagem do Nathan."

            "Como todo mundo consegue meu número?"

            "Deixa eu ver o que é."

            $ nathan_cel_msg1_r = True
            $ nathan_numero = True

            show screen celular_nathan

            "..."

            "Meu Deus... Eu lembro da gente conversando. E tudo o que aconteceu depois que eu bebi aquela maldição é um buraco na minha cabeça."

            "O que será que a gente fez?"

            if n1_ajuda:

                $ pautas += 1
                $ nathan_p1 = True

                "Caraca... É verdade. Eu fiquei de ver o que fazer com as informações que ele me passou."

                $ resultado_encontro = "nathan"

                show screen menu_pontos with Dissolve(0.5)

                "Ontem o [n] me passou todas as informações sobre o contrato dele. Isso com certeza dá uma excelente pauta para o chefe."

                "Mas eu também tenho meu problema com a [j]..."

                "E agora?"

                "Dependendo do que eu fizer com essa informação, minha vida vai mudar para um lado diferente."

                "Desde que a [c] apareceu na minha vida e eu comecei a conhecer as celebridades, estou precisando tomar decisões difíceis."

                "Não é fácil ter que escolher essas coisas."

                "Por um lado quero continuar vivendo aqui, mas entregar essas informações para meu chefe e agora talvez pra [j] também..."

                "Isso é horrível."

                "Bom... A vida não é fácil. E eu não quero desistir. Muitas coisas legais estão acontecendo também."

                "Preciso pensar muito bem no que eu vou querer fazer com o caso do [n]."

                hide screen menu_pontos
                with dissolve
            else:


                "Ele queria que eu ajudasse ele com o lance da [j] e eu recusei."

                "Será que eu devia ter negado isso? Ele parecia tão desesperado."

                "Mas não posso tomar uma decisão dessas por ele. É a carreira dele, mais ainda, a vida dele está em jogo."

                "Você não pode passar essa responsabilidade para alguém dessa forma."

                "Mas agora não tenho informação nenhuma pra dar pra [j]..."

                "[mcpnome]" "Será que ela vai publicar a matéria sobre mim e a [c]?"

                "[mcpnome]" "Tenho que falar com ela o mais rápido possível. Ela deve tá na redação..."

            "Mas agora vamos levantar. Vou tomar um banho e me trocar que um novo dia me aguarda!"

            $ aviso_chefe = True

            $ estou_na_cidade = True

            jump call_cidade

        show mc acordando with dissolve

        "Uaahh..."

        "O sono dos justos..."

        "Vamos ver o que o dia nos reserva hoje!"

        hide mc with dissolve

        if casa:

            if karli_casa:

                $ randh = renpy.random.randint(1,2)

                if randh == 1:

                    scene ap_karli mc_sala1 with Dissolve(1.0)

                    pause
                else:


                    scene ap_karli mc_sala2 with Dissolve(1.0)

                    pause

                mc "[m], já tá acordada?"

                m "Acabei de levantar."

                mc "Vou dar uma saída."

                m "Ok, bom trabalho."

                mc "Valeu."

                if dia >= dia_karli and not karli_morou:

                    $ karli_morou = True
                    $ karli_casa = False

                    call karli_despedida from _call_karli_despedida
            else:


                scene ap sala with dissolve

                mc charmoso "Um novo dia. Uma nova conquista."

            $ aviso_chefe = True

            jump call_cidade
        else:



            scene apartamento geral with dissolve

            mc normal "Certo! Como vou começar o dia?"

            menu:
                "Ir para o centro da cidade":


                    $ aviso_chefe = True
                    $ estou_na_cidade = True

                    jump call_cidade

label namorando:

    if priscila_namoro or sayuri_namoro or maria_namoro or julia_namoro or diana_namoro or nathan_namoro or sofia_namoro:

        $ namorando = True

    return

label checa_eventos:

    if sayuri_e7 == "pre":

        "Eu prometi pra [s] que ia procurar pela [fen] na cidade. Ela desapareceu de {b}manhã{/b} em algum lugar do centro."

        "Tenho que {b}pegar o ônibus até o centro da cidade{/b}, na parte da {b}manhã{/b} e procurar por ela."

    if sofia_e3 == "pre":

        "Eu tenho que encontrar a [w] na Faux News na parte da {b}tarde{/b}, lá no centro da cidade."

        "Tenho que ir de busão e depois andar até a Faux. Quando eu chegar lá, vou poder continuar nossa conversa."

    if julia_e6 == "pre":

        "Eu tenho que encontrar a Carol na {b}biblioteca do museu{/b}, lá no centro. E precisa ser de {b}manhã{/b}. Não é fácil chegar lá."

        "Vou de busão até o centro. Daí ando até o museu, entro, e daí ainda tenho que chegar até a biblioteca lá dentro. Mas vai valer à pena!"

    if not v15_fim and sofia_e1_count == 2 and dia >= dia_sofia:

        "Eu preciso conversar com a [w]. Ela tá se ferrando cada vez mais lá na redação."

        "Talvez eu consiga encontrar ela de {b}noite no trabalho{/b}. Mas precisa ser de noite na redação, quando ela deve estar sozinha."

    if natasha_evento >= 8 and natasha_e3 == "nada" and stifler_conheceu and stifler_e1 != "desistiu":

        "Eu tô com uma vonta de ir no {b}Distrito{/b}... eu devia dar um pulo lá quando der."

        "Parece que eu tô ficando mais safado cada dia que passa... mas eu realmente acho que eu devia dar um pulo lá."

    if n8_roupa == 1:

        "Quando eu tiver pronto pra ir na festa da Blergh!, eu tenho que falar com o Fabrício no bar e comprar a roupa."

    return



label checa_final:

    if v54_fim and v42_fim and v30_fim and v43_fim and v47_fim and v38_fim:

        show tela continua with Dissolve(2.0)

        pause

        call end_a from _call_end_a

    return

label end_priscila:

    play sound "audio/som_4_fadolandia.mp3"

    scene fadolandia geral with Dissolve(3.0)

    show pixie provocando with dissolve

    p "Oi! Aqui é a [p]! Lembra de mim?"

    p "Parece que você chegou ao final atual da história da [c]."

    p "Mas não esquente que a história dela ainda vai continuar."

    p "{b}Celebrity Hunter{/b} é atualizado todos os meses, desde 2018. Já são mais de 4 anos de trabalho aqui. O que deu um jogo de mais de 50 horas!"

    p "Deixe o app instalado para receber notificações com notícias sobre a próxima atualização."

    show pixie animada with dissolve

    p "Você viu que estamos sorteando C$ (dinheiro do jogo) no {a=https://www.instagram.com/geikogames/}Instagram{/a} e no {a=https://www.facebook.com/celebrityhuntergame}Facebook{/a}?"



    p "Se junte a mais de 50 mil seguidores nas redes e faça parte da nossa comunidade! Fique por dentro!"

    menu:
        "Instagram":


            $ renpy.run(OpenURL('https://www.instagram.com/geikogames/'))
        "Facebook":


            $ renpy.run(OpenURL('https://www.facebook.com/celebrityhuntergame/'))
        "Twitter":


            $ renpy.run(OpenURL('https://twitter.com/GeikoGames'))
        "Talvez depois":


            p "De boa!"

    p "Esses links também estão no menu caso você queira ver depois!"

















    p "Também não esqueça de indicar aos seus amigos e amigas e falar com o desenvolvedor nas redes sociais."









    call checa_final from _call_checa_final_15

    show pixie sorrindo with dissolve

    p "Mas vamos ao que interessa. Tem muitas coisas para você fazer ainda."

    p "Existem muitos outras pessoas para você conhecer."

    menu:
        "Eu posso transar com elas?":


            show pixie provocando with dissolve

            p "Com certeza. Inclusive, eu adoraria..."

            mc tarado "Eu também..."
        "Eu posso ser amigo delas?":


            p "Claro que pode. Mas não teria tanta graça..."

            mc envergonhado "Você gosta é de-"

            p "De diversão. É disso que eu gosto."
        "Eu posso ignorar elas completamente?":


            show pixie detetive with dissolve

            p "Pode, mas eu não recomendo..."

            mc zerado "Por que?"

            p "Porque o criador do jogo teve um trabalhão pra criar todas elas, você só vai ignorar?"

            mc "Criador? Como assim."

            p "Não interessa. Só vai falar com elas!"

            mc "..."

    p "Mas então."

    p "Você já conheceu a massagista? E a atleta olímpíca [s]? E também a garçonete, aquela atrevidinha!"

    p "Tem também a continuação da história da [j] e do Nathan. A cantora [d], a Natasha, a galera do Distrito, da Cidade Chinesa."

    p "Todos eles estão te esperando com suas próprias histórias, cheias de emoção e sedução como a [c]."

    p "Aliás, deixa eu te ensinar algo interessante."

    show guia_memorias with Dissolve(1.0)

    p "Apertando no botão MENU."

    show seta with dissolve

    p "Esse aqui embaixo."

    p "Você pode abrir a aba MEMÓRIAS. Ela permite que você descubra quais personagens você já conheceu e quais ainda falta conhecer."

    p "Olhando para o meu aqui, ainda falta MUITA gente para eu encontrar. Se o seu estiver assim também, ainda tem muita história pela frente."

    hide seta with dissolve

    p "Nesse caso, você precisa andar pela cidade, conhecer novas pessoas. Celebrity Hunter tem uma cidade muito grande."

    p "E pessoas aparecem em certos lugares dependendo do horário."

    p "Aparecem personagens no parque de manhã e a noite, na praia de manhã, no ponto de ônibus durante a noite e assim por diante."

    p "Dessa forma você libera novas histórias e pessoas para você encontrar e se relacionar."

    p "Nunca se sabe, pode ser amor à primeira vista."

    hide guia_memorias with Dissolve(1.0)

    p "Inclusive, eu posso te ajudar a encontrar novas histórias agora mesmo."

    p "O que você quer fazer?"

    menu:

        "Conhecer a atleta e a garçonete." if sayuri_evento1_check:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p3_after_sayuri","sayuri","after")

            p "Combinado!"

            p "Ela está no templo bem agora."

            p "A [s] é uma garota tímida, mas se você for um verdadeiro amigo ela vai se derreter por você."

            p "Conhecendo a [s], você também libera a garçonete."

            p "Agora vai lá."

            scene black with Dissolve(2.0)

            $ dia += 1
            $ tempo = 1

            jump sayuri_evento1

        "Conhecer a massagista." if not massagista_parque:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p3_after_karli","karli","after")

            p "Excelente escolha!"

            p "A massagista é uma garota estranha e ela vai te cansar um pouco antes até de falar com você."

            p "Você vai ter que encontrar ela duas vezes na cidade antes dela te atender no salão."

            p "Eu vou te mandar pro parque, mas depois você vai ter que encontrar ela em outro lugar. Boa sorte procurando ela!"

            p "Não desanime e vá até o fim! Ela é uma garota incrível!"

            scene black with Dissolve(2.0)

            $ dia += 1
            $ tempo = 3

            jump cenario_parque

        "Conhecer a cantora [dc]." if diana_e1 == "nada":

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p3_after_diana","diana","personagem")

            p "Legal! Ela é um mulherão e ainda por cima uma artista ambiciosa!"

            p "É o meu tipo de garota."

            p "Eu vou fazer o [mc] dormir e daí mandar ele direto para a praia! Assim você pode encontrar a [d]!"

            p "Boa sorte com ela!"

            $ dia += 1
            $ tempo = 1

            scene black with Dissolve(2.0)

            play sound "audio/som_13_praia.mp3"

            scene mc praia_dia with Dissolve(1.0)

            jump diana_evento1
        "Só quero voltar pra cidade.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p3_after_cidade","cidade","after")

            p "Vai resolver as coisas sozinho?"

            p "Ok!"

            p "Se precisar de alguma coisa, é só me encontrar quando dormir."

            $ tempo += 1

            jump call_cidade

label end_a:

    $ versao = "0.54.5"
    $ prox_versao = "0.55"
    $ dia_prox_versao = "15 de Outubro de 2020"

    play sound "audio/som_4_fadolandia.mp3"

    scene fadolandia geral with Dissolve(3.0)

    show pixie animada with dissolve

    p "Oi, bb! O tempo voa, hein? Você chegou ao fim da atualização atual de CH."

    p "Mas você não precisa parar aqui. Apoiadores têm acesso à continuação do jogo meses antes dos outros jogadores."

    p "Além de CH, temos vários outros games adultos: Nautilus 05, N10, N20, Encontros, Nova Fantasia e agora NFC +18 também"

    p "Acesse o site dos apoiadores e saiba mais sobre todas as vantagens. É apenas R$ 10, seguro e o melhor em jogos adultos em português!"

    menu:
        "Acessar site de apoiador":


            $ renpy.run(OpenURL('https://www.apoia.se/geiko'))
        "Talvez outra hora":


            p "Sem problemas. Quando tiver afim de fazer parte do nosso clube exclusivo, basta acessar www.apoia.se/geiko"



    p "Veja os outros jogos adultos do criador de CH {a=https://www.geiko.net/jogos/}{b}apertando aqui{/b}{/a}."

    p "Participe de sorteios e veja dicas no {a=https://www.instagram.com/geikogames/}Instagram (aperte aqui){/a} e no {a=https://www.facebook.com/celebrityhuntergame}Facebook (aperte aqui){/a}!"



    p "Se junte a mais de 50 mil seguidores nas redes e faça parte da nossa comunidade! Fique por dentro!"

    menu:
        "Instagram":


            $ renpy.run(OpenURL('https://www.instagram.com/geikogames/'))
        "Facebook":


            $ renpy.run(OpenURL('https://www.facebook.com/celebrityhuntergame/'))
        "Twitter":


            $ renpy.run(OpenURL('https://twitter.com/GeikoGames'))
        "Talvez depois":


            p "De boa!"

    p "Esses links também estão no menu caso você queira ver depois!"

    menu:
        "O que você tá fazendo aqui?":


            p "Eu vim conversar com você que está jogando."

    p "É que você chegou ao fim da história principal da versão atual."

    show pixie bonitinha with dissolve

    p "As histórias principais são as histórias que envolvem a {b}Priscila{/b}, a {b}Sayuri{/b} e {b}Júlia{/b}, o {b}Nathan{/b} e a {b}Cássia{/b}, {b}Sofia{/b}, {b}Diana{/b}, {b}Natasha{/b} e a {b}Nona{/b}."

    menu:
        "Isso quer dizer que o jogo acabou pra sempre?":


            p "Não. Na verdade estamos apenas no começo! O jogo {b}continua na próxima versão{/b}."

    p "{b}Celebrity Hunter{/b} é atualizado todos os meses, para que você avance a história e encontre novas celebridades."

    p "No momento ele está sendo atualizado para os apoiadores da Geiko."

    p "A gente vai se encontrar de novo em breve!"

    menu:
        "Então eu preciso esperar alguns dias pra continuar jogando?":


            show pixie explanando with dissolve

            p "Mais ou menos. Para continuar as histórias principais, você precisa esperar a próxima atualização."

    p "Mas você não precisa parar aqui. Apoiadores têm acesso à continuação do jogo um mês antes dos outros jogadores."

    p "Para continuar sua história agora mesmo, {a=https://apoia.se/geiko}{b}aperte aqui{/b}{/a} e conheça nosso plano de apoio no {a=https://apoia.se/geiko}{b}apoia.se/geiko{/b}{/a}."

    p "E tem MUITAS outras coisas pra fazer enquanto isso."

    p "Você já foi me visitar enquanto eu durmo? Quer dizer... Enquanto o [mc] dorme? Eu tenho uma história própria! Não esqueça de mim!"

    p "Você pode trabalhar no bar com o [gar] pra ganhar um dinheiro. Eu recomendo que você pegue o máximo possível."

    p "A massagista também tem uma história muito interessante! E você ainda vai aprender a fazer massagens!"

    p "Tem o pessoal no Distrito, na Cidade Chinesa, a garota do mercado e muitos outros {b}eventos secretos{/b} espalhados!"



    p "Existem muitas {b}coisas escondidas no jogo{/b}! Cabe a você jogar e descobrir tudo isso!"





    p "E o que acontece se você fizer escolhas diferentes? Eu tenho certeza que você vai encontrar muitos segredos se você tentar."

    p "Use o menu {b}Encontros{/b} pra jogar novamente encontros específicos."

    p "Se você deixar o aplicativo instalado, você recebe notificações com notícias da próxima versão e sorteios de Celebrity Reais."

    p "Fazemos sorteios todas as semanas no {a=https://www.instagram.com/geikogames/}Instagram{/a} ou no {a=https://www.facebook.com/celebrityhuntergame}Facebook{/a}."

    p "Acesse nosso {a=http://www.celebrityhunter.com.br/whatsapp}grupo do WhatsApp{/a} ou no Discord para discutir o game com outros jogadores!"

    p "Os links pras nossas redes sociais estão no Menu."







    menu:
        "Por que tenho que esperar vários dias pra continuar?":


            show pixie provocando with dissolve

            p "Você sabia que o jogo inteiro é feito por uma {b}única{/b} pessoa?"

    p "Texto, imagens, programação, publicação, correção de bugs, marketing, análise de dados, respostas de mensagens e outras coisas."

    p "É trabalho para caramba. Por isso que o desenvolvedor precisa de um tempo para atualizar o jogo."

    menu:
        "Se eu quiser ajudar, como eu faço?":


            p "Se você gostou de {b}Celebrity Hunter{/b} e deseja que o desenvolvimento continue, você pode ajudar de várias formas."





    p "Divulgue para suas amigas e amigos, peça para seu streamer preferido jogar, faça vídeos e poste imagens nas suas redes."

    p "Com seu apoio, {b}Celebrity Hunter{/b} vai ficar mais conhecido! E isso garante que ele continue sendo atualizado!"

    p "Comprar C$ ou Celebrity Coins na Loja no Menu ajuda bastante. Não precisa de cartão, você pode comprar com PIX."

    p "Se cada um ajudar com um pouquinho, teríamos atualizações mais rápidas e o desenvolvedor teria mais recursos pra fazer um jogo melhor!"

    p "Quem sabe com animações, vozes e muito mais! Tudo isso custa dinheiro, então a colaboração de cada um é importante."

    p "Veja imagens exclusivas da próxima atualização no {a=https://www.instagram.com/geikogames/}Instagram{/a} ou no {a=https://www.facebook.com/celebrityhuntergame}Facebook{/a}."

    menu:
        "E esse cara que criou o jogo não tem outros jogos?":


            show pixie animada with dissolve

            p "Ah! Que bom que você me lembrou! Ele pediu para avisar que ele lançou vários jogos desde que ele começou em 2018."

            p "Você pode jogar agora {a=https://www.geiko.net/jogos/}{b} apertando aqui e visitando a página com os jogos{/b}{/a}."

            p "Tem muita coisa legal, jogos no futuro, em ambientes medievais e muito mais!"

            p "Se quiser saber mais, é só {a=https://www.geiko.net/jogos/}{b}apertar aqui{/b}{/a}."



    menu:
        "O que vai acontecer agora?":


            p "Agora você vai voltar para a cidade para viver todas as histórias opcionais do jogo!"

    p "Boa diversão procurando todos os segredos do game!"

    p "Até a próxima atualização!"

    $ aviso_final = True

    jump call_cidade

label mensagem_premium:

    show black with dissolve

    p rindo "Ops! A próxima cena é exclusiva para a versão premium do game. Para quem apoia a Geiko com R$ 10."

    menu:
        "Como é que é?":


            p "Algumas cenas +18 de CH são exclusivas para os apoiadores. Elas não mudam o enredo, mas aprofundam a história com emoção e erotismo explícito."

            p "Você pode perder algumas cenas bem quentes e com detalhes sobre os personagens, mas elas não vão mudar o final da sua história. Pode relaxar."

            p "Caso você queira ver essas cenas, você pode apoiar a Geiko com R$ 10 e ter acesso a elas e a muitos outros benefícios."

            p "Além de cenas +18 exclusivas, apoiadores recebem a atualização meses antes e têm outras vantagens em TODOS os jogos que o RB criou!"

            p "Você vai curtir muito mais Nautilus 05, N10, N20, NFC e NF também! Além de outros jogos que ainda serão lançados!"

            p "Além de ter grupos oficiais para tirar dúvidas e interagir com outros jogadores que são muito fãs de CH!"

            p "E tudo isso por apenas R$ 10! Ouvi falarem que hoje em dia isso não compra nem uma Coca 2L... essa inflação..."

            menu:
                "Acessar o site de apoiadores":


                    p rindo "Boa! Estou abrindo aqui. Não vai assustar!"

                    $ renpy.run(OpenURL('https://www.apoia.se/geiko'))

                    p rindo "Conseguiu dar uma olhada? O que achou? Não esqueça de baixar a versão premium e instalar por cima desta pra ver tudo!"
                "Outra hora":


                    p rindo "Ok! Espero que você possa apoiar um dia e ver todas as cenas adultas que CH tem a oferecer!"
                "Esse desenvolvedor é um mercenário!":


                    p lecionando "Quê?! Você tá falando que o desenvolvedor é um salafrário que só pensa em dinheiro e tudo devia ser grátis?"

                    p "Bom... talvez ele seja mesmo. Eu não vou discutir com você por causa disso. Eu não estou nem aí."

                    p "Mas talvez ele precise da grana para continuar fazendo os jogos. Vocês humanos precisam de comida, não precisam?"

                    p "Se cada jogador ajudar com um pouco não pesa para ningém e o game continua sendo melhorado e ampliado!"

                    p "R$ 10 é tanta grana assim que não vale a pena investir em uma diversão que você curte?"

                    p "E ainda colabora com a pessoa que gasta horas e horas trabalhando pra trazer tudo isso com uma versão grátis pras pessoas?"

                    p "Pense nisso! Sem essa grana eu não estaria aqui também... Então acho bom você pagar logo! Passa a grana!"
        "Beleza.":


            p rindo "Ok! Espero que você possa apoiar um dia e ver todas as cenas adultas que CH tem a oferecer!"

    hide black with dissolve

    return

label premium_gratis:

    p rindo "Opa. Essa próxima cena era exclusiva da versão premium, mas o RB deixou grátis nesta atualização."

    p rindo "O safado sabe que se você curtir, vai querer ver as outras que são exclusivas pra apoiadores."

    p rindo "Então faça bom proveito! E se você curtir mesmo, não esqueça que o apoio é apenas R$ 10 e dá acesso a TUDO!"

    p rindo "Não apenas em CH, mas em TODOS os jogos da Geiko!"

    return

label aviso_chefe_dias:

    $ aviso_chefe = False

    mc normal "Ufa... Ainda tenho alguns dias até precisar entregar uma pauta para o chefe."

    if aviso_chefe_1vez:

        $ aviso_chefe_1vez = False

        mc normal "Para eu ver direitinho quantos dias faltam pro meu deadline, só ver a cara do chefe no meu celular."

        mc serio "Quanto mais bravo ele estiver, mais perto do último dia eu estou."

    mc normal "Tenho que pensar bem o que vou fazer hoje."

    jump call_cidade

label aviso_chefe:

    $ aviso_chefe = False

    mc triste "Ixi... Olha o dia..."

    mc "Amanhã o chefe vai me chamar pra me despedir. Eu vou ter que entregar uma pauta pra ele de qualquer jeito."

    if pautas > 1:

        mc concentrando "No momento eu tenho [pautas] pautas que eu posso revelar pra ele..."

        mc "Qual eu devo entregar?"

        mc "Com certeza minha relação vai complicar com a celebridade que eu dedurar pra revista."

        mc serio "Também tenho que tomar cuidado para não entregar a mesma celebridade muitas vezes."

        mc "Quanto mais vezes eu dedurar o mesmo famoso, mais ele vai descofiar de mim."

    elif pautas == 1:

        mc desculpa "Droga, só tenho uma única pauta pra entregar..."

        mc triste "Tenho que tomar cuidado para não entregar a mesma celebridade muitas vezes seguidas ou ela pode desconfiar de mim."
    else:


        mc angustiado "Droga! Não tenho nenhuma pauta pra ele."

        mc triste "Preciso encontrar uma pauta hoje, ou amanhã ele vai me demitir..."

        mc incomodado "Se eu perder esse emprego vou voltar a morar com meus pais."

        mc angustiado "Por favor! Tudo menos isso!"

    jump call_cidade

label baixar_nuvem:

    if not renpy.can_load("None-continue"):

        python:
            if renpy.android:
                PythonSDLActivity.baixarNuvem()

        $ renpy.full_restart()
    else:


        $ renpy.notify("Você já tem um jogo iniciado. Apague os dados do aplicativo nas configurações do celular e tente novamente")

        $ renpy.pause(delay=3, hard=True)

        $ renpy.full_restart()

label avaliacao_gplay_1:

    show pixie sonhadora
    with dissolve

    p "Oi!"

    p "..."

    p "Alouuu?"

    menu:
        "Tá falando comigo?":


            p "Claro! Com quem mais seria?"

    p "O [mc] está dormindo agora. Ele vai chegar no meu reino daqui a pouco. Queria aproveitar esse tempinho pra falar com você a sós."

    p "Primeiro, queria te dar os parabéns por completar seu primeiro dia. Ele é como... vocês chamam de... tutorial, eu acho? Você lidou bem com a [c]."

    p "A partir de agora, você será muito mais livre para escolher onde ir e com qual celebridade conversar."

    p "Só não vai esquecer de mim, tá?"

    p "Ah! Antes de você continuar, só queria te pedir um favorzão."

    p "Quando tiver um tempinho, você poderia avaliar o jogo com {b}5 estrelas{/b} na Google Play?"

    p "Como é apenas uma pessoa que faz o jogo, sem grana pra investir em propaganda, sua avaliação é ainda mais importante."

    p "Quanto melhor"

    p "Agora eu vou me preparar pra receber o [mc]..."

    $ persistent.gplay_1 = True

    p "Bom jogo!"

    return



    show seta with vpunch

    p "Primeiro. Você já apertou o botão MENU ali em baixo pra ver o que acontece?"

    menu:
        "Sim e dei uma olhada nas abas.":


            p "Certo..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_menu_sim","primeira","pesquisa")
        "Sim, mas não vi o que tinha.":


            p "Certo..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_menu_naogostei","primeira","pesquisa")
        "Não apertei.":


            p "Certo..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_menu_nao","primeira","pesquisa")

    hide seta with dissolve





























    p "Segunda pergunta. O que você mais espera encontrar neste jogo?"

    menu:
        "Uma história legal e original com bons personagens.":


            p "Entendi..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_objetivo_historia","primeira","pesquisa")
        "Ver conteúdo adulto.":


            p "Entendi..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_objetivo_adulto","primeira","pesquisa")
        "Viver um romance com o personagem que eu escolher.":


            p "Entendi..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_objetivo_romance","primeira","pesquisa")
        "Nenhuma destas opções.":


            p "Entendi..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_objetivo_nenhum","primeira","pesquisa")





























    p "Última pergunta."

    p "Se você pudesse mudar uma coisa no jogo entre estas três opções, o que você mudaria?"

    menu:
        "Saber se minhas escolhas aumentam amizade ou sedução.":


            p "Ok..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_mudanca_escolhas","primeira","pesquisa")
        "Jogar a mesma história, mas controlando uma garota.":










            p "Ok..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_mudanca_garota","primeira","pesquisa")
        "Remover todos os anúncios.":


            p "Ok..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_mudanca_anuncio","primeira","pesquisa")
        "Nenhuma destas três.":


            p "Ok..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("p1_mudanca_nenhuma","primeira","pesquisa")

    p "Muito obrigada pelas suas respostas. Isso ajuda muito a gente saber sua opinião e podemos deixar o jogo cada vez melhor!"







    p "Agora eu vou me preparar pra receber o [mc]..."

    $ persistent.gplay_1 = True

    p "Bom jogo!"

    return

label tutorial_cards:

    scene black with Dissolve(2.0)

    "..."

    show pixie explicando with dissolve

    p "Olá! Tudo bem com você?"

    p "Faz um tempinho que a gente não se vê..."

    p "E aí? Tá gostando da história?"

    p "Desculpa interromper você, mas é que eu queria te explicar algo legal que tem no nosso jogo."

    p "Eu acho que você nem viu ainda, por isso eu queria te mostrar."

    p "Hmmm... acho que eu vou sair da sua frente pra você poder enxergar direitinho."

    hide pixie with dissolve

    p "Vai acompanhando minha voz, ok?"

    show seta with vpunch

    p "Tá vendo esse botão MENU logo aqui? Mas não aperte nele ainda. Vou te ensinar tudo antes."

    p "Clicando nele, você vai abrir nosso lindo menu."

    scene painel inicial with dissolve

    p "Aqui você pode ler novidades sobre o jogo. É o cara que faz o jogo que escreve, por isso não precisa dar muita bola. Ele gosta de escrever."

    p "Mas não é por isso que viemos aqui. Tá vendo o botão {b}Álbum{/b}?"

    p "Deixa eu marcar pra você..."

    show seta album with hpunch

    p "Acho que isso foi um pouco exagerado..."

    p "Enfim... Clicando ali você verá todos os cards que você já pegou."

    scene painel album with dissolve

    p "Provavelmente seu álbum vai estar mais vazio. É que eu sou meio sortuda."

    p "Quando a carta está virada pra baixo, com o desenho preto mostrando, quer dizer que você ainda não pegou ela."

    p "Para pegar cartas, você deve clicar no botão {b}Loja de Cartas{/b}."

    show seta loja with dissolve

    p "Esse aqui."

    p "Me desculpe por ser um pouco óbvia, mas uma fada precisa aprender a ser didática. Tem muita gente burra nesse mundo."

    p "Continuando..."

    scene painel loja with dissolve

    p "É aqui que você vai testar sua sorte e pegar cartas para completar seu álbum."

    p "Clique no botão {b}Abrir Pacote{/b} e você receberá uma carta aleatoriamente."

    p "Vamos ver qual eu pego..."

    scene painel carta with dissolve

    p "Que sortuda! Uma carta com 3 estrelas! Essas são realmente raras e sempre têm cenas inéditas."

    p "Pegar uma carta gasta 10 {b}Celebrity Coins{/b}. Então precisamos ganhar mais moedas para sortear mais cartas."















    scene painel album with dissolve

    p "Depois de pegar uma carta e ela aparecer no seu álbum, você pode apertar nela para ver ela em tela cheia."

    scene sayuri carta with dissolve

    p "A [s] tá realmente linda nessa foto..."



    scene black with Dissolve(1.0)

    show pixie explicando with dissolve

    p "Agora eu vou deixar você voltar para a história."

    $ persistent.tutorial_cards = True

    p "Bom jogo!"

    hide pixie with dissolve

    return

label reiniciar_jogo:

    $ renpy.full_restart()

    return

label locomocao:

    if carro:

        play sound som_35_passos

        scene black with dissolve

        pause 1.0

        scene carro_estacionamento with Dissolve(1.0)

        pause 1.0

        play sound som_roupas

        scene black with dissolve

        scene carro_estacionamento3 with Dissolve(1.0)

        mc "Vamo lá, garoto."

        play sound som_carro

        pause 1.0

        scene black with dissolve

        scene carro_mc_cidade1 with Dissolve(1.0)

        pause 2.0

        scene black with dissolve
    else:


        "..."

        if tempo >= 3:

            scene cidade onibus_noite with Dissolve(3.0)
        else:


            scene cidade onibus with Dissolve(1.0)

        call cena_onibus from _call_cena_onibus_7

    return

label cena_onibus:

    "..."

    play sound "audio/som_14_onibus.mp3"

    if tempo >= 3:

        scene onibus parado_noite with Dissolve(3.0)
    else:


        scene onibus parado with Dissolve(3.0)

    pause

    mc "Finalmente chegou..."

    $ randbus = renpy.random.randint(1,3)

    if randbus == 1:

        mc "Fala aí!"

        "Motorista" "Opa, jovem. Pode subir."

        mc "Beleza!"

    elif randbus == 2:

        mc "E aí, senhor? Tudo bem hoje?"

        "Motorista" "Tudo em cima. E contigo?"

        mc "Tudo beleza. Bora dá um passeio, né."

        "Motorista" "Faz bem pro coração."

    elif randbus == 3:

        mc "E aí? Tá quente hoje hein?"

        "Motorista" "Nem fala. Será que o frio tá chegando?"

        mc "Acho que o frio não gosta muito da nossa cidade."

        "Motorista" "É uma pena..."

    "Motorista" "Pode pagar aqui pra mim."

    $ renpy.pause(delay=3, hard=True)

    mc "Valeu."

    "Motorista" "Nada."

    "..."

    scene black with Dissolve(1.0)

    "..."

    stop sound

    return

label carro_antes:

    hide screen ap_tela with Dissolve(0.5)

    if tempo > 2:

        "Hoje tá tarde. Melhor resolver isso amanhã."

        show screen ap_tela with Dissolve(0.5)

        pause

    if carro_evento == 1:

        "Ok... eu tô pronto pra tomar minha decisão?"

        "Vou desistir do carro pra sempre ou vou aceitar a proposta da Gina?"

        menu:
            "Eu aceito. Eu quero o carro.":


                $ carro_gina = 1

                mc "Vou ficar com o conversível. Não sou idiota."

                scene black with dissolve

                scene ap mc_cel_falando with Dissolve(1.0)

                mc "Gina?"

                gina "Oi, querido! Decidiu aceitar o presente?"

                mc "Sim. Tô indo aí, ok?"

                gina "Com certeza, amor. Vou estar aqui com a camisola que você gostou."

                mc "Ok..."
            "Eu não vou aceitar. Eu desisto do carro.":


                $ carro_gina = 3

                "Eu decidi que não quero ele. Vou ligar pra ela e avisar."

                scene black with dissolve

                scene ap mc_cel_falando with Dissolve(1.0)

                mc "Gina?"

                gina "Oi, querido! Decidiu aceitar o presente?"

                mc "Eu fico muito feliz com o agrado, de verdade. Mas não me sinto bem."

                gina "Você tem certeza? É um conversível. E é completamente de graça."

                mc "Sim. Igual eu falei. É tentador, mas acho que você tá indo longe demais. Não me sinto bem."

                gina "Não é uma proposta que eu farei de novo, entende? Eu te adoro, mas não darei outra chance."

                mc "Eu sei. Muito obrigado, Gina."

                gina "Hmf... adeus, garoto."

                "Vou ficar sem o carro, mas não vou me vender pra essa senhora."

                "Eu mantenho minha alma limpa e também não ferro as coisas com a Karli."

                jump call_cidade
            "Preciso pensar mais":


                show screen ap_tela with Dissolve(0.5)

                pause
    else:


        "Vou lá ver o lance do carro com a Gina."

    scene black with dissolve

    call locomocao

    scene black with dissolve

    scene mansao entrada with Dissolve(1.0)

    pause

    mc "Gina? Posso entrar?"

    "???" "O portão vai abrir, garoto."

    scene black with dissolve

    scene gina_carro1 with Dissolve(1.0)

    pause

    mc "Oi!"

    gina "Oi, meu amor. Vamos lá no carro?"

    mc "Ok."

    scene black with dissolve

    scene gina_carro5 with Dissolve(1.0)

    pause

    gina "E aí?"

    jump compra_carro

label compra_carro:

    if carro_evento == 0:

        $ carro_evento = 1

        play sound "audio/som_3_celular.mp3"

        $ renpy.vibrate(1)

        pause 2.0

        mc "Hm? Esse número."

        scene black with dissolve

        scene ap mc_cel_falando with Dissolve(1.0)

        mc "Gina?"

        gina "Oi, meu amor."

        gina "Como tão as coisas com você? Aproveitando o apartamento que eu te dei?"

        menu:
            "Muito. A senhora sabe dar presente, viu?":


                mc "Adorei."

                gina "Fico muito feliz de ouvir isso, amor. Você merece isso e muito mais."
            "Ainda é cedo. Nem curti direito.":


                mc "Mas tô empolgado."

                gina "Aposto que você ainda vai aproveitar muito ele. Você tem saúde."

                mc "Hehe... obrigado."

        if gina_massagem:

            gina "Depois daquela massagem que você me deu, isso é o mínimo que eu podia fazer."
        else:


            gina "Mesmo você não me dando aquela massagem, eu sei cuidar de rapazes como você, viu?"

            mc "Sabe, né?"

            gina "Uhum... os anos trazem experiência. Eu sei do que você gosta."

        gina "Mas eu te liguei porque tenho outro presente pra você."

        mc "Verdade?!"

        gina "Você sabe onde fica minha mansão, certo? Por que você não vem aqui?"

        "A Karli não vai gostar nada disso."

        "Mas se ela me deu um apartamento... o que será que ela vai me dar agora?"

        "Vale à pena pelo menos saber o que é."

        mc "Ok. Eu vou."

        gina "Pode ser hoje mesmo? Eu estou com muita vontade de te ver."

        mc "B-bom... se a senhora quer... eu vou."

        gina "Vou estar esperando. Beijos."

        mc "Beijos..."

        "Bora ver o que essa mulher quer..."

        scene black with dissolve

        call locomocao

        scene black with dissolve

        scene mansao entrada with Dissolve(1.0)

        pause 2.0

        mc "Alô?"

        "???" "Quem é?"

        mc "É o [mc]. Eu vim falar com a sen-"

        "???" "Pode entrar."

        mc "T-tá."

        "Povo rico é outra coisa..."

        play sound som_25_passos3

        scene black with dissolve

        scene gina_carro1 with Dissolve(1.0)

        pause

        gina "Meu bem! Que felicidade te ver!"

        mc "O-oi! Já tô chegando! Seu quintal é um pouquinho grande, senhora."

        gina "Você sabe que não precisa me chamar de senhora. Apenas Gina por favor."

        mc "Sim, se- digo... Sim, Gina."

        gina "Era pra você tá acostumado numa hora dessas, certo?"

        gina "Meu dia se alegra toda vez que você vem me ver, sabia?"

        gina "Às vezes eu fico o dia todo na cama esperando a vida acontecer. É uma chatisse ter tudo."

        gina "Mas saber que você vem me anima completamente. Você é um raio de luz pra mim."

        mc "Que bom..."

        mc "Ufa. Com licença."

        gina "Toda, meu amor. Vem cá."

        scene black with dissolve

        scene gina_carro2 with Dissolve(1.0)

        pause

        mc "S-senhora!"

        gina "Que foi?"

        menu:
            "Nada, não. A senhora está linda.":


                mc "Adorei o estilo..."

                gina "Gostou? Eu me sinto à vontade ficando assim."
            "A camisola que você tá usando...":


                mc "Com todo o respeito, eu consigo ver..."

                gina "Algum problema, querido? Esse é o tipo de roupa que eu costumo usar quando fico em casa."

                gina "Posso me trocar se você não estiver confortável."

                mc "Não... por mim está tudo bem..."

                gina "Que bom."

        gina "Eu sei que não tenho mais a idade que a maioria das modelos tem."

        menu:
            "Não fala isso. A senhora tá perfeita.":


                mc "Não deixa nada a desejar para nenhuma mulher mais nova."

                gina "Você acha mesmo?"

                mc "Com certeza."
            "Precisamos lidar com cada etapa da vida.":


                mc "Aposto que esta nova etapa também vai ter muita coisa para a senhora."

                gina "Sem 'senhora' eu disso."

                mc "Perdão."

                gina "Mas eu ainda não quero saber dessa 'nova etapa'. Eu gosto da etapa antiga."

                mc "Gosta..."

                gina "Muito."

        gina "Eu prezo muito pela minha aparência. Eu invisto grandes quantias em tratamentos estéticos."

        gina "Como você pode ver, meu corpo foi esculpido por diversas mãos habilidosas."

        gina "E ter um parceiro como você me faz me sentir melhor ainda."

        mc "Sei..."

        gina "Um novinho igual a você traz a vida de volta, entende?"

        mc "Com certeza."

        gina "E você me deixa tão feliz que eu fico com vontade de te dar alguns presentes."

        menu:
            "Muito obrigado pela casa.":


                pass

        mc "Falando nisso, não posso deixar de agradecer pelo apartamento."

        gina "Eu e meu marido temos diversas propriedades. Não seria um problema para nós presentear uma para um parceiro como você."

        mc "M-mesmo assim. É muita generosidade."

        gina "Olha aqui, meu amor."

        mc "O-oi."

        scene black with dissolve

        scene gina_carro3 with Dissolve(1.0)

        pause

        gina "Não precisa se sentir agradecido. Eu só fiz o que eu quis. Que foi paparicar um pouco meu rapaz."

        gina "Mas se você se sente na necessidade de retribuir, o que você acha de você aceitar outro presente?"

        mc "O-outro? M-mas..."

        gina "Você tá olhando pra mim, não tá?"

        mc "S-sim..."

        gina "O que você acha de outro presente? Um ainda melhor do que aquele apartamento?"

        "Ela tá falando... do que eu tô pensando?"

        if namorando:

            "M-mas eu tô namorando..."

        menu:
            "Eu vou adorar, Gina.":


                mc "Seria... demais, Gina..."

                gina "Assim que eu gosto de ouvir, mocinho."
            "Acho melhor, não...":


                mc "Eu já abusei da sua generosidade, Gina... melhor..."

        gina "Vem. Eu vou te mostrar."

        gina "Melhor ainda. Fecha os olhos. Vou preparar tudo pra você."

        mc "O-ok... m-mas..."

        gina "Confia em mim... me dá sua mão e fecha os olhos."

        scene black with dissolve

        mc "{i}gulp{/i}"

        mc "Pronto."

        gina "Agora me segue. Cuidado cair."

        play sound som_25_passos3

        window hide

        pause 2.0

        gina "Pode abrir."

        "Minha nossa... ela vai tá..."

        scene black with dissolve

        scene gina_carro4 with Dissolve(1.0)

        pause

        gina "O que você acha?"

        menu:
            "Você tá falando do carro?!":


                pass

        mc "E-esse conversível aí?!"

        gina "Claro, meu bem. Do que eu estaria falando?"

        gina "O que você acha de ter um carro como esse aqui?"

        mc "Você quer dizer... que ele seria meu? De verdade?"

        gina "Eu disse que eu sei dar presentes, não disse? Principalmente para um garoto como você."

        mc "Gina... não entendo... o que eu fiz... tipo... esse conversível deve custar meio milhão!"

        gina "Eu já te disse. Não se preocupe com dinheiro. Eu tenho o suficiente para presentear quem eu quero."

        gina "E você... bom... você tem sido a luz do meu dia."

        if gina_massagem:

            gina "Aquela massagem que você me fez... hmmm..."

            gina "Ela merece ser recompenada."

            mc "Hmm..."
        else:


            gina "Claro... você poderia ter sido ainda mais bonzinho comigo..."

            gina "Mas você vai ter uma nova chance de me agradar."

        mc "E-então é isso..."

        scene black with dissolve

        scene gina_carro5 with Dissolve(1.0)

        pause

        gina "Hoje eu acordei com uma vontade enorme de fazer uma boa ação."

        gina "E eu estou disposta a te dar este brinquedinho se você aceitar."

        gina "Ficaria muito feliz se você aceitasse."

        "Não tem nenhuma dúvida aqui."

        "Ela tá querendo dizer que vai me dar o carro em troca de atender os desejos dela."

        "A Gina tá afim de um novinho pra deixar o dia dela mais animado... e vai me mimar bastante se eu aceitar."

        "Só que nada é de graça neste mundo parece..."

        "Um carro desses em troca de ficar com ela..."

        "Pensando bem..."

        "Será que eu consigo aceitar... pegar o carro... e depois negar ela na hora?"

        "Ela não pode me segurar se eu não quiser..."

        "Porque... se eu ficar com ela... minha relação com a Karli vai pro saco."

        "A Karli é lésbica e provavelmente não vai rolar nada entre a gente. Mas eu perderia até a amizade dela."

        "Mas um carro desses... minha nossa... quem negaria algo assim?!"

        gina "Tudo isso é você pensando, meu amor? Não achei que fosse uma decisão tão difícil... aceitar um conversível de graça."

        mc "É..."

        menu:
            "Eu aceito. Vamos resolver isso agora.":


                $ carro_gina = 1

                jump carro_evento1
            "Não quero... obrigado, mas é gentileza demais.":


                $ carro_gina = 3

                mc "Eu fico muito feliz com o agrado, de verdade. Mas não me sinto bem."

                gina "Você tem certeza? É um conversível. E é completamente de graça."

                mc "Sim. Igual eu falei. É tentador, mas acho que você tá indo longe demais. Não me sinto bem."

                gina "Não é uma proposta que eu farei de novo, entende? Eu te adoro, mas não darei outra chance."

                mc "Eu sei. Muito obrigado, Gina."

                gina "Hmf... adeus, garoto."

                "Vou ficar sem o carro, mas não vou me vender pra essa senhora."

                "Eu mantenho minha alma limpa e também não ferro as coisas com a Karli."
            "Preciso pensar. Não quero abusar de você.":


                $ carro_gina = 2

                mc "É generosidade demais. E eu fico muito feliz. Mas não sei se vou me sentir bem."

                mc "Eu poderia... pensar por favor?"

                gina "Hmm... não pensei que isso seria algo para se pensar... um carro de graça."

                gina "Mas se você precisa... tudo bem... eu queria muito resolver isso hoje..."

                gina "Tudo bem... talvez a espera deixe tudo melhor, certo?"

                mc "Hm? Ok... então... vou pensar e te aviso, tá?"

                gina "Vou ficar te esperando, querido. Tchau tchau."

                mc "Até. E obrigado de novo pela oportunidade, Gina."

                "Eu preciso pensar se vale à pena eu me vender por um carro."

                "Um conversível desses é incrível! Mas o que a Gina quer em troca... eu posso imaginar."

                "Como a Karli vai ficar com isso? E a..."

                "Melhor eu voltar. Quando eu tiver pronto eu aviso ela."

        scene black with dissolve

        $ tempo += 2

        jump call_cidade

    elif carro_evento == 1:

        label carro_evento1:

            pass

        $ carro_evento = 2

        mc "Eu tô MUITO interessado nele."

        gina "Fico muito feliz em saber, meu bem. Um presente desses a gente não pode recusar."

        mc "Com certeza."

        mc "E eu não vou ter que pagar nada mesmo? Esse conversível é caríssimo, Gina..."

        gina "Pra mim, o único pagamento que você tem que dar é um sorriso. Nós estamos aqui para nos ajudar, certo?"

        gina "Você deixa esta velha se sentir viva de novo. Então eu quero ser um raio de luz pra você também."

        mc "Poxa..."

        gina "Ah. Assim como o apartamento, só vou pedir que você providencie a documentação."

        mc "Ah, sim, claro... você já tá me dando o carro, pelo menos os documentos eu me viro."

    elif carro_evento == 2:

        label carro_evento2:

            pass



        mc "Não consigo parar de pensar nele..."

        gina "Um desses a gente não esquece mesmo..."

        mc "Só preciso da documentação, né?"

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()
            carro = PythonSDLActivity.pegaCarro()

    gina "Isso mesmo. Para ajeitar tudo você vai precisar de {b}C$ 2.000{/b}. Essa é a taxa que o despachante vai pedir. Só isso."

    mc "Certo..."

    "Um carro desses... no meu nome... por apenas {b}C$ 2.000{/b} é uma oportunidade que poucos têm na vida."

    if carro:

        "{b}Como você já comprou o carro em outro gameplay, não precisa pagar por ele novamente{/b}"

        jump carro_comprado

    if cash >= 2000:

        "Eu tenho o dinheiro suficiente comigo! Boa, [mc]!"

        mc "Sem problema. Eu tenho a grana comigo. Faço o PIX pra você na hora se quiser."

        gina "Não tem pressa. Então você vai querer mesmo? Posso dar entrada na papelada?"

        menu:
            "Sim. Vou ficar o carro.":


                python:
                    if renpy.android:
                        cash = PythonSDLActivity.pegaCash()
                        
                        if cash >= 2000:
                            
                            PythonSDLActivity.compraCarro()

                $ renpy.block_rollback()

                mc "Com certeza."

                play sound "extra/carta.mp3"

                "{b}Você usou {b}C$ 2.000{/b} e pagou para ter o CARRO{/b}"

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("comprou_carro","mc","personagem")

                show black with dissolve

                "{b}Seu carro fica salvo no aparelho, se você fez login, ele também fica salvo online na sua conta{/b}"

                "{b}Você não precisará pagar por ele novamente, mesmo que reinicie o jogo do zero{/b}"

                "{b}Entretanto, se você recomeçar, você precisa voltar neste ponto da história para poder pegar ele novamente{/b}"

                hide black with dissolve

                if carro:

                    label carro_comprado:

                        play sound "extra/carta.mp3"

                        "{b}Você liberou o CARRO novamente{/b}"

                mc "Então vou transferir o dinheiro pra você."

                $ carro_evento = 3

                gina "Ok, amor. Demora uns dias pra sair tudo, mas a partir de agora ele já é seu."

                gina "Por que você não vem aqui e senta no teu carro novo?"

                mc "É pra já."

                scene black with dissolve

                scene gina_carro6 with Dissolve(1.0)

                pause

                mc "Uau..."

                gina "Nossa digo eu... você parece ainda mais interessante assim... hmm..."

                mc "Tá falando sério?"

                python:
                    if renpy.android:
                        carro = PythonSDLActivity.pegaCarro()

                gina "Com certeza, garoto. Num desses... hmmm... dá uma coisa diferente olhando pra você."

                "Será que ela tá falando sério? Só de ter um carro assim vão me olhar diferente?"

                "Nem acredito que eu consegui... eu sou muito foda!"

                gina "Eu poderia ficar olhando para você assim o dia todo. Essa cara de felicidade."

                mc "Haha... valeu, Gina. Uma casa e agora um conversível... você é a pessoa que mais me presenteou na vida."

                gina "Ah... eu fico muito contente de ouvir isso, querido. Você é um garoto tão bom."

                gina "Quem dera você fosse meu filho..."

                "A Gina é mãe da Karli... e elas tão brigadas."

                "A Gina parece tão legal. Por que ela não aceita que a Karli seja lésbica?"

                "Se a gente ama nossos filhos, a gente precisa aceitar eles como são..."

                gina "[mc]? O que você tá pensando?"

                menu:
                    "Você também fica linda no carro.":


                        mc "Que você também fica uma delícia no carro... com todo o respeito..."

                        gina "Ai, querido... eu não mereço um elogio desses. Sou só uma velha."

                        mc "Você é uma mulher fantástica."

                        gina "São seus olhos..."
                    "Você se acertou com aquela inquilina...":


                        "Melhor eu jogar o verde aqui... ela não preisa saber o que eu sei."

                        mc "Aquela inquilina que a gente falou da outra vez..."

                        gina "Ah... aquela garota não tem jeito."

                        gina "Acho que é impossível nós nos entendermos."

                        gina "Somos de tempos diferentes. E temos visões diferentes da vida."

                        gina "Prefiro evitar pensar naquele assunto. Tenho coisas mais interessantes para pensar, sabe..."

                gina "Agora, sendo sincera, fico tão feliz que você esteja curtindo seu novo brinquedinho."

                mc "Nem sei como te agradecer..."

                gina "Eu já disse que não faço isso para ter algo em troca."

                scene black with dissolve

                scene gina_carro7 with Dissolve(1.0)

                pause

                gina "Eu só quero que você seja feliz. E continue me alegrando igual você sempre fez."

                mc "Gina... você quer que eu te alegre?"

                gina "Hmm... sempre, meu amor..."

                gina "Você não é obrigado a fazer nada. Mas sua companhia sempre me faz feliz."

                gina "Se você me fizer companhia, você estaria fazendo o dia desta velha muito melhor..."

                gina "Você não sabe como eu esperei para estar com você sozinha neste carro. Só nós dois..."

                mc "Companhia..."

                gina "Sim... uma companhia..."

                "Eu acredito na Gina. Não acho que ela vá me forçar a fazer alguma coisa. Acho que ela realmente gosta de mim."

                "Mas depois desses presentes... eu acho que eu devia dar algo pra ela em troca..."

                "E com esses comentários dela... eu sei bem o que ela quer..."

                "Mas a Karli... se ela de algum jeito descobrir isso... é o fim..."

                if namorando:

                    "Tirando que eu taria traindo... porque eu já tô namorando."

                "O que eu faço?"

                menu:
                    "Você me presenteou... quero te deixar feliz também.":


                        $ carro_evento = 4

                        mc "Eu quero ser legal contigo... e acho que a gente podia se alegrar..."

                        gina "Tá vendo? Você merece tudo de bom. É uma luz na nossa vida mesmo."

                        mc "Você que me mima demais..."

                        gina "Vou mimar muito mais agora."

                        mc "Vai?"

                        gina "Abaixa essas calças."

                        mc "Gina..."

                        gina "Só obedece, querido."

                        mc "S-sim..."

                        play sound som_roupas

                        scene black with dissolve

                        scene gina_carro8 with Dissolve(1.0)

                        pause

                        mc "A-ah..."

                        gina "Hmmm... o que você acha desse mimo aqui, hein?"

                        mc "Eu gosto..."

                        gina "Quer dizer que você ganha um carro e um carinho ainda por cima?"

                        mc "Hmmm... é o que tá parecendo."

                        gina "Quero ver você feliz... e bem animado pra mim..."

                        mc "G-gina... mas... não tem problema? A gente tá bem no meio da mansão."

                        gina "Sshh... não tem nenhum problema. Meu marido tá fora. Trabalhando em algum filme ou fugindo da justiça."

                        mc "C-como é?"

                        scene black with dissolve

                        scene gina_carro9 with Dissolve(1.0)

                        pause

                        gina "Foca no meu pezinho, foca..."

                        mc "Ahh..."

                        gina "Quero ver nosso amigo bem grandão... pra dar cabo de mim..."

                        gina "Eu esperei tanto pra finalmente ver ele assim... sentir ele assim..."

                        gina "Vou me divertir bastante com ele... quero sentir com o pé, com a mão, com a boca... com outras partes..."

                        mc "Eu também quero sentir tudo..."

                        gina "Você vai usar toda essa energia comigo. Essa energia que só um novinho assim tem."

                        mc "Eu vou fazer você se sentir uma novinha safada de novo."

                        gina "Ahnn... tô gostando... de ver você animado assim."

                        gina "Pula pro banco de trás. Vai ser melhor pra você me comer gostoso."

                        mc "Com certeza."

                        scene black with dissolve

                        scene gina_carro10 with Dissolve(1.0)

                        pause

                        gina "Olha como eu tô."

                        mc "Que delícia."

                        gina "Você não liga de comer uma buceta mais velha?"

                        mc "Aposto que é ainda mais gostosa."

                        gina "Depois que você experimentar você vai poder falar."

                        menu:
                            "Deixa eu lamber essa buceta então.":


                                pass

                        mc "Me dá ela aqui."

                        gina "Ahh... só de pensar na tua boquinha nela eu fico arrepiada."

                        mc "Então vem, danada."

                        scene black with dissolve

                        scene gina_carro11 with Dissolve(1.0)

                        pause

                        gina "Aahh... assim..."

                        gina "Vem e passa a língua em tudo."

                        mc "Vou sentir tudinho. Seu gostinho doce de melzinho."

                        gina "Aahh... esse jeito que você fala... por isso que eu adoro um garoto igual você."

                        mc "Aqui tem energia de sobra, senhora."

                        gina "Sim... aah...."

                        mc "Tá gostando?"

                        gina "Hmmm... muito..."

                        gina "Mas eu quero mais... só vou ficar satisfeita com seu meninão dentro de mim."

                        mc "Eu tô aqui pra te agradecer, senhora. Teu pedido é uma ordem."

                        scene black with dissolve

                        scene gina_carro12 with vpunch

                        pause

                        mc "Se você quer pica, você vai ter! Nghh!"

                        gina "Aahhh!"

                        gina "Assim que eu quero! Com força, com energia! Energia que só você tem, gatinho!"

                        mc "Vai tomar muita energia!"

                        gina "Agnnhh... me beija!"

                        mc "Vou chupar, beijar, morder!"

                        gina "Nngnhhh! Você é melhor na cama que eu tinha pensado, safado!"

                        mc "Você queria um garoto safado, não queria?! Pra apagar esse fogo!"

                        gina "Ssiimmmm! Eu continuo tendo vontades!"

                        mc "E eu vou satisfazer tudo!"

                        gina "Nnghhh!"

                        gina "Assim!!! AAHH!!!"

                        scene black with dissolve

                        scene gina_carro13 with Dissolve(1.0)

                        pause

                        mc "TOMAA!"

                        gina "NNGHHH!"

                        gina "Tem cuidado com a sua senhora!"

                        mc "Você não quer cuidado! Você quer com força, não quer?!"

                        gina "Aghhnn! Você tá animando demais!"

                        menu:
                            "É melhor eu ir com calma":


                                mc "Vou com jeitinho até a senhora gozar."

                                gina "Aahh... ahnnn... assim..."
                            "Eu sei que você quer com força!":


                                mc "Não mente, safada! Você queria assim desde o começo!"

                                scene black with dissolve

                                scene gina_carro14 with Dissolve(1.0)

                                pause

                                gina "Aahhh! Eu provoquei! Aahhnnn!"

                        mc "Você vai gozar rapidinho!"

                        gina "Aahhnn... você que vai gozar desse jeito!"

                        mc "Você é gostosa demais, velha tesuda!"

                        gina "Aahnn! Hmmmm!"

                        mc "Vou gozar na senhora!"

                        gina "Aahnnnn! Gozaaaaa! Me enche, [mc]!"

                        mc "AAAHHHH!!!"

                        scene black with dissolve

                        scene gina_carro15 with vpunch

                        pause

                        mc "AAAHHHH!"

                        mc "CARALHOOO!"

                        gina "Aahhhhh! Hnnn... aah..."

                        mc "Toda a porra pra você..."

                        gina "Hmmmmm..."

                        gina "Meu Deus... hmmmm..."

                        gina "Era bem isso que eu queria..."

                        mc "Ahhh... eu gostei muito também..."

                        gina "Gostou? Então hoje você recebeu dois presentes."

                        gina "Agora vou tomar um banho. Quem sabe a gente não se encontre de novo."

                        mc "Eu... ufa... vou adorar, senhora..."

                        mc "Valeu de novo pelo carro."
                    "Vou indo. Tô ansioso pra curtir meu carro.":


                        mc "T-talvez a gente pudesse combinar outro dia. Pra gente... sei lá."

                        mc "Agora eu tô muito afim de sair dirigindo esse calango aqui."

                        gina "Mas, amor..."

                        mc "Você me deixou muito empolgado, Gina!"

                        gina "Minha nossa, parece uma criança com um brinquedo novo..."

                        mc "Posso dirigir ele?"

                        gina "Ai ai... tudo bem... quem sabe a gente não se vê de novo um dia, certo?"

                        mc "Com certeza!"

                gina "Faça bom proveito, querido."

                gina "E... vê se coloca um pouco de juízo naquela garota. Ela precisa entender como as coisas certas são."

                mc "Haha... vou tentar ajudar ela a ser feliz. Pode contar comigo."

                gina "Feliz... e correta, natural, como as coisas foram feitas pra ser."

                mc "Vamos ver. Até mais, Gina!"

                gina "Beijos, querido!"

                play sound som_carro

                scene black with dissolve

                pause 2.0

                scene carro_mc_cidade1 with Dissolve(1.0)

                pause

                "Caralho! Olha pra isso aqui, mano!"

                "Vida de busão, nunca mais! Agora só ando de conversível!"

                "Se o pessoal da minha cidade me visse com isso aqui, iam pagar pau DEMAIS, cara!"

                "Finalmente coisas boas acontecendo pra mim neste inferno aqui!"

                mc "BORAAAAAAAAAAAAAAAA!"

                play sound som_carro

                scene black with dissolve

                pause 2.0

                jump call_cidade
            "Eu preciso pensar... eu quero... mas não hoje.":


                pass
    else:


        "Merda... não tenho grana..."

        "Infelizmente, mesmo sendo pouco pra um carro desses, dois pau é muito pra mim agora."

        "Vou ter que dar um jeito de trabalhar e conseguir essa grana antes."

        show black with Dissolve(1.0)

        p lecionando "Ixi. O [mc] tá pobre que só ele..."

        p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

        p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

        p "Além de garantir este carrão, você ainda contribui com o desenvolvimento de CH."

        p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

        menu:
            "Sim. Tô com uma graninha sobrando aqui.":


                p rindo "Que bom!"

                call comprar_cash

                p "Deu tudo certo no site?"

                p "Se você confirmou o pagamento, assim que a equipe adicionar em sua conta, você receberá um email."

                p "Daí, é só continuar a história daqui e garantir seu vrum vrum turbinado!"

                p "Agora pode continuar."

                hide black with dissolve

                jump carro_evento2
            "Não. Tô pobre igual a ele...":


                p rindo "Não esquente."

                p "Trabalhe sempre que possível no bar e vá juntando seus Celebrity Reais. Logo logo você já vai estar com grana suficiente."

                p "Demora, mas vale a pena!"

                hide black with dissolve

    mc "Vou precisar de um tempinho pra bater o martelo, tá?"

    gina "Hmf... se você precisa... vou continuar te esperando..."

    gina "Dizem que quem é apressada como cru... então... vou dar o tempo meu menino precisa."

    mc "Valeu, Gina. Você é muito boa comigo."

    gina "Você merece, meu amor. Quando quiser, só voltar aqui e continuamos."

    mc "Pode deixar. Fica bem."

    gina "Você também... Um beijo."

    mc "Beijos."

    scene black with dissolve

    $ tempo += 1

    jump call_cidade



label comprar_milreais:

    $ iap.purchase("cr1000")

    $ renpy.block_rollback()

    return

label comprar_250reais:

    $ iap.purchase("cr250")

    $ renpy.block_rollback()

    return

label dados_essenciais:

    if premium:

        $ desp = False

        python:
            if renpy.android:
                
                persistent.apoiador = PythonSDLActivity.pegaBacker()


        if renpy.variant("android") and not persistent.apoiador:

            jump nao_apoiador





    call namoro_priscila2 from _call_namoro_priscila2

    python:
        if renpy.android:
            persistent.banned = PythonSDLActivity.pegaBanned()

    if persistent.banned:
        $ persistent.banned = False

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()
            persistent.coins = PythonSDLActivity.pegaMoedas(0)





    if cash > 39999:
        $ cash = 39999

    if persistent.coins > 30001:
        $ persistent.coins = 30000

    return

label carrega_compra:

    hide screen menu_loja with Dissolve(0.5)

    python:
        if renpy.android:
            PythonSDLActivity.carregaJogo()

    $ renpy.notify("Atualizando...")

    $ renpy.pause(delay=7, hard=True)

    python:
        if renpy.android:
            persistent.coins = PythonSDLActivity.pegaMoedas(0)
            cash = PythonSDLActivity.pegaCash()

    show screen menu_loja with Dissolve(0.5)

    pause

    return

label carrega_compra2:

    python:
        if renpy.android:
            PythonSDLActivity.carregaJogo()

    $ renpy.notify("Atualizando seus dados...")

    $ renpy.pause(delay=5, hard=True)

    python:
        if renpy.android:
            persistent.coins = PythonSDLActivity.pegaMoedas(0)
            cash = PythonSDLActivity.pegaCash()

    "{b}Seus dados foram atualizados com as informações da nuvem{/b}"

    return

label menu_prepara:

    $ renpy.notify("Seu jogo foi salvo no seu aparelho")

    return

label final_free:

    p rindo "E aí, tchutchuquinho! Gostando de CH, né?"

    show ad4 with dissolve

    p "A história da versão gratuita acaba neste ponto. {b}Ela continua grátis nos próximos meses{/b}."

    p "O desenvolvedor gosta de mandar uma versão grátis no começo de CADA MÊS. De CH ou de outro jogo da Geiko."

    p "Então siga a Geiko nas redes sociais para sempre ser avisado quando sair a próxima versão grátis."

    p "Não quer esperar? Quer continuar jogando agora mesmo?! Quer ver TODO O FINAL DA DIANA?!"

    p "É possível jogar a continuação agora mesmo. Essa é uma das vantagens de apoiar a Geiko!"

    p "Se você gostou de CH, pode continuar jogando ele agora mesmo ou qualquer um dos outros 9 jogos da Geiko por apenas R$ 10."

    p "É esse apoio que permite a Geiko continuar criando jogos adultos de qualidade. Quem não curte uma safadeza, certo?"

    p "E em troca desse apoio de R$ 10, os apoiadores ganham vantagens exclusivas. Como jogar as atualizações vários meses antes da versão gratuita!"

    p "Além disso, você joga games que ainda não foram lançados, ganha mais dinheiro, espera menos tempo, vê cenas extras e muito mais!"

    p "Venha dar uma olhada! E se você curtir, apoie e continue sua jornada!"

    menu:
        "Saber mais no site":


            $ renpy.run(OpenURL('https://www.apoia.se/geiko'))
        "Talvez outra hora":


            p "Sem problemas. Quando tiver afim de fazer parte do nosso clube exclusivo, é só falar."

    p "Você pode saber tudo sobre a continuação de CH e os outros jogos da Geiko nas nossas redes sociais."

    p "Se junte a mais de 50 mil jogadores nas redes e faça parte da nossa comunidade! Fique por dentro!"

    menu:
        "Instagram":


            $ renpy.run(OpenURL('https://www.instagram.com/geikogames/'))
        "Facebook":


            $ renpy.run(OpenURL('https://www.facebook.com/celebrityhuntergame/'))
        "Twitter":


            $ renpy.run(OpenURL('https://twitter.com/GeikoGames'))
        "Talvez depois":


            p "De boa!"

    p "Deixe o jogo instalado para receber novidades nas notificações e não perca a continuação."

    show ad2 with dissolve

    hide ad4

    p "Se você gostou do game, temos outros para você! Como o jogo adulto pós-apocalíptico {a=https://www.geiko.net/n05/}Nautilus 05{/a}."

    p "É um jogo de escolhas incrível com pegação e cenas adultas também! E tem 3 finais! Você viu todos?!"

    menu:
        "Baixar Nautilus 05":


            $ renpy.run(OpenURL('https://www.geiko.net/n05/'))
        "Outros jogos +18 da Geiko":


            $ renpy.run(OpenURL('https://www.geiko.net/jogos'))
        "Agora não":


            p "Tranquilo."

    show ad6 with dissolve

    hide ad2

    p "Quer jogar mais do mundo de CH? Veja Encontros, que seria praticamente uma continuação deste jogo aqui."

    p "Você vai poder xavecar e levar várias personagens de CH pra cama, como a Priscila, a Tatá, a Miranda, a Ágata e até novas personagens!"

    menu:
        "Baixar Encontros":


            $ renpy.run(OpenURL('https://www.geiko.net/en/'))
        "Outros jogos +18 da Geiko":


            $ renpy.run(OpenURL('https://www.geiko.net/jogos'))
        "Quem sabe outra hora...":


            t "Ok..."

    show ad3 with dissolve

    hide ad6

    p "Minha última recomendação é o Nova Fantasia Clicker +18, um RPG adulto bem diferente do que você já viu."

    p "Você tem a opção de lutar contra várias inimigas ou vencer elas levando elas pra cama."

    p "É algo bem diferente que você só encontra nos games da Geiko. Vale a pena experimentar!"

    menu:
        "Baixar NFC +18":


            $ renpy.run(OpenURL('https://www.geiko.net/nfc/'))
        "Outros jogos +18 da Geiko":


            $ renpy.run(OpenURL('https://www.geiko.net/jogos'))
        "Numa próxima talvez":


            p "Legal."

    p "Ufa... Acho que acabei! Maldito RB faz eu ficar fazendo anúncio! Que puto! Falou, carinha!"

    hide ad3 with dissolve

    return

label textos:







    "Ufa... consegui entrar. Agora preciso encontrar esse cofre."



    "A Roxane disse que a Zaza se importa muito com ela. Que ela é como uma filha pra Zaza."

    "Será que... será que a senha do cofre tem algo a ver com a Roxane?"



    "A Roxane me disse que ela nasceu em 1998. Vou tentar 1998 como senha."

    "O protagonista digita 1998 no teclado. O cofre emite um som e a porta se abre."

    "Deu certo!"



    "Agora preciso encontrar o Nathan."



    mc "Nathan! Consegui!"

    n "Sério?! Você é o cara!"

    mc "Vamos dar o fora daqui."

    n "Sim! Vamos!"






















    mc "Zaza, eu preciso entender. Por que você quer tanto fazer parte do Grupo?"

    za "Porque eu quero poder."

    mc "Poder para quê?"

    za "Poder para fazer a diferença."

    mc "Mas você já faz a diferença. Você tem a Blergh!, você tem a Roxane..."

    za "Isso não é suficiente."

    mc "Por que não?"

    za "Porque eu quero mais. Eu quero poder para mudar as coisas. Para tornar a Capital um lugar melhor."

    mc "E você acha que o Grupo vai te ajudar a fazer isso?"

    za "Sim. Eles têm o poder e a influência que eu preciso."

    mc "Mas eles também são corruptos. Eles exploram as pessoas."

    za "Eu sei. Mas eu posso mudar isso. Eu posso ser a voz da razão dentro do Grupo."

    mc "Você acha mesmo?"

    za "Eu tenho que tentar."

    mc "Mas e a sua consciência? Você não se sente mal por se aliar a pessoas como o prefeito Donatello?"

    za "A consciência é um luxo que nem todos podem ter."

    mc "O que você quer dizer com isso?"

    za "Quero dizer que, às vezes, para fazer o bem, é preciso fazer o mal."

    mc "Você está disposta a sacrificar seus princípios para conseguir o que quer?"

    za "Se for para o bem da Capital, sim."

    mc "E quem decide o que é o bem da Capital?"

    za "Eu."



    mc "Eu não sei se concordo com você."

    za "Eu não espero que você concorde. Mas eu espero que você entenda."

    mc "Eu... eu vou tentar."

    za "Obrigada."



    za "Eu me sinto responsável por todas as mulheres que sofrem nas mãos dos homens."

    mc "Como assim?"

    za "Eu já vi muita coisa nessa cidade. Já vi mulheres sendo exploradas, abusadas, maltratadas."

    za "E eu quero poder para mudar isso. Eu quero poder para proteger as mulheres."

    mc "Mas o Grupo... eles maltratam mulheres."

    za "Eu sei. Mas eu posso mudar isso. Eu posso ser a voz das mulheres dentro do Grupo."

    mc "Você acha mesmo que pode mudar o Grupo?"

    za "Eu tenho que tentar."

    mc "Mas e se você não conseguir? E se eles te corromperem?"

    za "Eu não vou deixar isso acontecer."

    mc "Mas e se você não conseguir salvar todas as mulheres?"

    za "Eu sei que não posso salvar todas. Mas vou ajudar o máximo que eu puder."



    za "Eu vou fazer com que as mulheres sejam respeitadas."





    mc "Cássia?"

    j "Pombinho."

    mc "Posso me sentar?"

    j "Se você quiser."



    mc "Você está bem?"

    j "Estou."

    mc "Você parece... pensativa."

    j "Só estou cansada."

    mc "De tudo isso?"

    j "De tudo."

    mc "Você aprendeu muito com a Zaza, não é?"



    j "Sim. Aprendi."

    mc "Ela te ensinou a ser... como você é?"

    j "Ela me ensinou a ser forte. A ser independente. A não depender de ninguém."

    mc "E a usar as pessoas?"



    j "O mundo é dos fortes, pombinho. Se você não usar as pessoas, elas vão usar você."

    mc "Mas... e a sua consciência?"

    j "A consciência é um luxo que nem todos podem ter."

    mc "A Zaza... ela me disse a mesma coisa."

    j "É porque é verdade."

    mc "Mas... como você chegou a esse ponto?"



    j "Eu não tive uma vida fácil."

    mc "Você já me falou isso também."

    j "Mas você não sabe o que eu passei."

    mc "Então me conta."



    j "Eu fui criada em um orfanato."

    mc "Eu sinto muito."

    j "Não precisa sentir pena de mim."

    mc "Não é pena. É... empatia."

    j "Empatia?"



    j "Você não sabe o que é ter uma vida difícil."

    mc "Talvez você não saiba o que é ter a minha vida."



    j "Você quer saber como eu conheci a Zaza?"

    mc "Se você quiser me contar."

    j "Eu fugi do orfanato quando era adolescente. Eu não aguentava mais aquele lugar."

    j "Eu vim para a Capital em busca de uma vida melhor. Mas eu não tinha nada. Eu não tinha ninguém."

    j "Eu acabei me envolvendo com pessoas erradas. Pessoas que me usaram."

    j "Até que eu conheci a Zaza."

    mc "E ela te salvou?"

    j "Não. Ela me mostrou que eu não era vítima. Não precisava ser salva. Eu precisara era tomar as rédeas da vida com minhas próprias mãos."

    j "Ela me ensinou a sobreviver. Ela me ensinou a ser forte. Ela me ensinou a usar as pessoas antes que elas me usassem."

    mc "E você acha que isso é certo?"

    j "Não existe certo ou errado nesse mundo, pombinho. Só existe o que funciona."

    mc "Mas..."

    j "Você não entende. Você é um jovem inocente. Vive na sua realidade. Acha que o mundo é um lugar justo."

    j "Mas o mundo não é justo. O mundo é cruel. E se você não for forte, você será esmagado."

    mc "..."



    j "Eu sei que você não concorda comigo. Mas eu não me importo."

    j "Eu fiz o que tinha que fazer para sobreviver. E eu não me arrependo de nada."

    menu:
        "E a sua filha?":


            pass



    j "Como você sabe da minha filha?"

    mc "Eu... eu ouvi você falando com a Zaza."



    j "Você não deveria ter ouvido essa conversa."

    mc "Eu sinto muito. Mas... o que você sente por ela?"

    j "Eu... eu não sei."

    mc "Você não a ama?"

    j "Eu... eu não sei o que é amor."

    mc "Mas... ela é sua filha."

    j "Eu sei. Mas... eu não a criei. Eu não a conheço."

    mc "Mas você só a entregou? Pra quem?"

    j "Eu fiz o que era melhor para ela."

    mc "Você acha mesmo?"



    j "Eu não sei."

    mc "Você se arrepende?"

    j "Não. Eu fiz o que tinha que fazer."

    mc "Mas você parece triste."

    j "Eu já disse... só estou cansada."



    mc "Cássia... você não precisa ser forte o tempo todo."



    j "Eu... eu não sei o que você quer dizer."

    mc "Você pode ser vulnerável. Você pode mostrar seus sentimentos."

    j "Eu não posso."

    mc "Por que não?"

    j "Porque se eu mostrar meus sentimentos, eu serei fraca."

    mc "Ser vulnerável não é ser fraco. É ser humano."



    j "Eu... eu não sei."

    mc "Você quer que eu vá embora?"

    j "Não."

    mc "Então... o que você quer?"



    j "Eu... eu quero um abraço."



    j "Eu sinto tanta falta dela..."

    mc "Eu sei."

    j "Eu fui uma péssima mãe..."

    mc "Não. Você fez o que achou que era melhor para ela."

    j "Mas... e se eu estiver errada?"

    mc "Você não está errada. Você só está com medo."

    j "Medo de quê?"

    mc "Medo de ser vulnerável. Medo de mostrar seus sentimentos."



    j "Eu não posso ser vulnerável."

    mc "Você pode."

    j "Não. Eu não posso."







    mc "Zaza, posso te perguntar uma coisa?"

    za "Claro."

    mc "É sobre a Cássia."



    za "O que você quer saber sobre ela?"

    mc "Eu... eu quero saber qual é a sua relação com ela."

    za "A Cássia... ela foi minha pupila."

    mc "Pupila?"

    za "Sim. Eu a ensinei tudo o que sei sobre o mundo."

    mc "E por que você fez isso?"

    za "Porque eu vi potencial nela. Ela é inteligente, ambiciosa e determinada."

    mc "Mas... ela parece tão diferente de você."

    za "Sim, ela é. Ela decidiu seguir seu próprio caminho."

    mc "E você se orgulha disso?"

    za "Claro que sim. Eu quero que ela seja feliz."

    mc "Mas... ela parece tão... implacável."

    za "A vida não é fácil, [mc]. Para chegar ao topo, é preciso ser forte."

    mc "Mas... e os seus princípios?"

    za "Às vezes, para fazer o bem, é preciso fazer o mal."

    mc "Você acha que a Cássia está fazendo o bem?"

    za "Eu não sei. Mas eu sei que ela está lutando por uma vida melhor."

    mc "E você? Você também está lutando por uma vida melhor?"

    za "Todos nós estamos, [mc]. Todos nós queremos ser felizes."

    mc "Eu... eu quero saber sobre o passado dela."

    za "O passado da Cássia... é complicado."

    mc "Você pode me contar?"



    za "A Cássia... ela foi criada em um orfanato."

    mc "Eu sinto muito."

    za "Não precisa sentir pena dela. Ela é uma sobrevivente."

    za "Eu a conheci quando ela era adolescente. Ela tinha fugido do orfanato e estava vivendo nas ruas."

    za "Ela era... diferente. Ela tinha essa... fome de poder. Essa ambição."

    za "Eu vi potencial nela. E decidi ajudá-la."

    mc "Você a ensinou tudo o que ela sabe?"

    za "Eu a ensinei sobre o mundo da moda. Eu a ensinei a ser forte, a ser independente."

    za "Mas... ela também aprendeu outras coisas. Coisas que eu não a ensinei."

    mc "Como o quê?"

    za "Como usar as pessoas. Como manipular. Como conseguir o que ela quer, não importa o custo."

    mc "E você se arrepende de ter ajudado ela?"

    za "Não. Eu não me arrependo. A Cássia é quem ela é. E ela é responsável por suas próprias escolhas."

    mc "Mas... e a revista? Por que ela virou joralista?"

    za "A Cássia... ela quer poder. E ela vê a revista como um trampolim para conseguir esse poder."

    za "Ela quer usar a revista para se tornar famosa, para ter influência. E ela não se importa com quem ela precisa pisar para chegar lá."

    mc "E você? Você concorda com isso?"

    za "Eu quero que a Blergh! seja um sucesso. Eu quero que as mulheres se sintam fortes e poderosas quando usam minhas roupas."

    za "Mas... eu não quero que isso aconteça às custas dos outros."

    mc "E o que você vai fazer?"

    za "Isso não é da sua conta."













    za "Cássia, preciso falar com você. A sós."

    "Cássia raises an eyebrow, but dismisses her admirers with a wave of her hand."

    j "Claro, Zaza. O que foi?"

    "Zaza takes a deep breath."

    za "Estou frustrada. O Barão não me deu a resposta que eu esperava."

    j "(Sipping her champagne) Eu te avisei que não seria fácil. O Grupo é uma organização muito... tradicional."

    za "(Sharply) Tradicional? Ou machista?"

    "Cássia sets down her glass and looks at Zaza with a cool gaze."

    j "Você sabe que eu não tenho paciência para esse tipo de discurso, Zaza."

    za "(Frustration creeping into her voice) Eu sei, eu sei... mas é difícil não me sentir... desprezada."

    j "(Softly) Eu entendo."

    za "(Turning away) Eu construí a Blergh! do zero. Eu a transformei em uma força a ser considerada. E ainda assim, eles me tratam como... como se eu fosse uma criança."

    "Cássia steps closer to Zaza and places a hand on her arm."

    j "Você não é uma criança, Zaza. Você é uma mulher forte e inteligente. Você merece estar no Grupo."

    za "(Turning back to Cássia, her eyes filled with doubt) Mas como? Se eles não me aceitam?"

    j "(A sly smile playing on her lips) A gente precisa encontrar uma forma de convencê-los."

    za "(Hope flickering in her eyes) Você tem alguma ideia?"

    j "(Meeting Zazas gaze) Sim. Mas preciso que você confie em mim."

    "Zaza hesitates for a moment, then nods."

    za "Eu confio em você, Cássia."

    "Cássia leans in close to Zaza and whispers in her ear."

    j "Ótimo. Então me escute..."



    "Eu ouvi a conversa da Cássia com a Zaza. A Cássia tem um plano para ajudar a Zaza a entrar no Grupo. Mas eu não confio na Cássia. Ela é manipuladora e só pensa em si mesma. E se eu usasse a Zaza e a Blergh! contra o prefeito? Isso poderia enfraquecer o Grupo. A Zaza é ambiciosa e quer poder. Se eu a convencer de que o prefeito está usando ela, ela pode se voltar contra ele. E a Blergh! é uma empresa em ascensão. Se eu conseguir que a Zaza use a Blergh! para atacar o prefeito, isso poderia causar um grande dano à imagem dele. Mas como isso afetaria a mim, ao Nathan, à Sofia, à Natasha e à revista? Eu: Se eu conseguir jogar a Zaza contra o prefeito, isso me colocaria em uma posição de poder. Eu teria informações que ninguém mais tem. E eu poderia usar essas informações para me beneficiar. Nathan: Se a Zaza se voltar contra o prefeito, isso poderia prejudicar a Blergh!. Mas também poderia libertar o Nathan do controle do Grupo. Sofia: Se a revista publicar uma matéria sobre a Zaza e o prefeito, isso poderia aumentar a circulação da revista e ajudar a Sofia a alcançar seus objetivos. Mas também poderia colocar a revista em risco. Natasha: Se a Zaza se voltar contra o prefeito, isso poderia prejudicar a Natasha, que é a secretária do prefeito. Mas também poderia ser uma oportunidade para ela se libertar do controle do Grupo. Revista: Se a revista publicar uma matéria sobre a Zaza e o prefeito, isso poderia aumentar a circulação da revista e ajudar a revista a se tornar mais influente. Mas também poderia colocar a revista em risco."














    mc "Zaza, Cássia, obrigado por me receberem."

    za "Você disse que tinha algo importante para nos falar."

    mc "Sim. Eu ouvi a conversa de vocês na festa."

    j "E o que você ouviu?"

    mc "Eu ouvi que você quer entrar para o Grupo, Zaza. E que o prefeito Donatello não está disposto a te aceitar."

    za "Isso é verdade."

    mc "Eu também sei que a Cássia tem um plano para te ajudar."

    j "E como você sabe disso?"

    mc "Eu tenho meus métodos."

    mc "Mas o que eu queria falar é que talvez vocês estejam sendo usadas."

    za "Usadas? Como assim?"

    mc "O prefeito Donatello e o Grupo estão usando a Blergh! para ganhar dinheiro e influência. Mas eles não estão dispostos a dar a você o respeito que você merece, Zaza."

    j "E o que você sugere que façamos?"

    mc "Eu sugiro que vocês se voltem contra o prefeito."

    za "Se voltar contra o prefeito?"

    mc "Sim. Usem a Blergh! para atacar a imagem dele. Exponham a corrupção dele e do Grupo."

    j "Isso é... arriscado."

    mc "É. Mas também é uma oportunidade."

    za "Uma oportunidade para quê?"

    mc "Uma oportunidade para vocês tomarem o poder."

    mc "O prefeito Donatello está vulnerável. Ele está em campanha para a reeleição. E ele tem um segredo que pode destruir a carreira dele."

    j "Que segredo?"

    mc "Ele tem uma filha ilegítima."

    za "!"

    j "!"

    mc "Se vocês exporem esse segredo, isso pode acabar com a carreira dele. E com o Grupo."

    za "Mas... e o Nathan?"

    mc "O Nathan pode ser libertado do controle do Grupo. E a Blergh! pode se tornar ainda mais poderosa."

    j "E o que você ganha com isso?"

    mc "Eu ganho poder. Eu teria informações que ninguém mais tem. E eu poderia usar essas informações para me beneficiar."

    za "Você está nos pedindo para confiar em você."

    mc "Sim."

    za "..."

    j "..."

    za "Eu aceito."

    j "Eu também."

    mc "Ótimo. Então vamos começar..."

    mc "Eu sei que vocês duas já sofreram muito nas mãos do Grupo."
    za "O que você quer dizer com isso?"
    mc "Eu sei sobre a filha da Cássia."
    "Cássia tenses."
    j "Como você sabe disso?"
    mc "Eu ouvi a conversa de vocês na festa. E eu sei que você teve que desistir dela para entrar no Grupo."
    j "Isso foi... há muito tempo."
    mc "Mas ainda te machuca, não é?"
    "Cássia looks away."
    mc "O Grupo trata as mulheres como objetos. Eles as usam para seus próprios fins e depois as descartam."
    za "É assim que o mundo funciona."
    mc "Não precisa ser assim. Vocês podem ter poder sem se submeter a eles."
    za "Como?"
    mc "Usem a Blergh! para construir seu próprio império. Um império que valorize as mulheres e as trate com respeito."
    j "Isso é... um sonho bonito."
    mc "Não é só um sonho. É possível. Vocês são mulheres fortes e inteligentes. Vocês podem fazer isso."
    mc "Olhem para a Diana. Ela foi corajosa o suficiente para desafiar o Barão. E ela está livre agora."
    mc "Olhem para o Nathan. Ele está em dúvida se continua com a Blergh! ou se foge para outro país."
    mc "Vocês podem dar a ele e a outras pessoas a oportunidade de viverem suas vidas com dignidade."
    mc "Vocês podem ser a mudança que a Capital precisa."
    "Zaza and Cássia remain silent, their expressions thoughtful."
    mc "Eu sei que isso é arriscado. Mas eu acredito em vocês."




    "O Distrito é uma área da Capital onde se concentram os bordéis e outros estabelecimentos de entretenimento adulto. É uma área controlada por uma organização criminosa conhecida como Os Carcamanos."
    "Black Cash é um dos líderes dos Carcamanos. Ele é um homem poderoso e influente, e tem uma relação próxima com Roxane."
    "Não está claro qual é a natureza exata da relação entre Black Cash e Roxane. Ele a chama de mana, o que sugere que ele a vê como uma irmã ou figura familiar. No entanto, também é possível que haja algo mais entre eles."
    "Black Cash está preocupado com Roxane e quer tirá-la da Blergh!, pois acredita que ela está sendo explorada pelo Grupo. Ele pede ao MC para ajudá-lo a resgatá-la, mesmo que isso signifique destruir a Blergh!."
    "Não está claro se Roxane quer ser resgatada. Ela parece gostar de ser modelo e está determinada a fazer sucesso."
    "O MC terá que decidir se ajuda Black Cash a resgatar Roxane, se tenta convencê-la a sair da Blergh! por conta própria, ou se fica de fora dessa situação."





    mc "Roxane, eu preciso falar com você sobre o Distrito."
    ro "O Distrito? O que tem?"
    mc "O Black Cash... ele quer que você volte."
    "Roxane looks away."
    ro "Eu não quero voltar."
    mc "Mas por que não? Você sabe que ele se preocupa com você."
    ro "Eu sei. Mas eu não quero viver aquela vida."
    mc "Mas você não está feliz aqui na Blergh!. Você está sendo usada pelo Grupo."
    ro "Eu sei o que o Grupo faz. Mas eu não me importo. Eu quero ser uma modelo de sucesso. E a Blergh! está me dando essa oportunidade."
    mc "Mas você está sacrificando sua felicidade por isso."
    ro "Eu não vejo dessa forma. Eu estou fazendo o que eu quero fazer. E eu estou feliz."
    mc "Você não está feliz. Você está com medo."
    ro "Medo? De quê?"
    mc "Medo do Grupo. Medo do que eles podem fazer com você se você desobedecer."
    "Roxane stands up and walks to the window."
    ro "Eu não tenho medo deles. Eu sei como eles funcionam. E eu sei como me proteger."
    mc "Você não pode se proteger deles. Eles são muito poderosos."
    ro "Eu sou mais poderosa do que você pensa."
    "Roxane turns to face MC, a defiant look in her eyes."
    ro "Eu sei como usar o meu corpo. Eu sei como usar o meu charme. Eu posso conseguir o que eu quiser."
    mc "Mas você não está feliz. Você está se vendendo."
    ro "Eu não me importo. Eu quero ser famosa. Eu quero ser rica. E eu vou conseguir isso, não importa o que eu tenha que fazer."
    mc "Mas você não precisa fazer isso. Você pode ter uma vida melhor. Uma vida com dignidade."
    ro "Dignidade? O que é dignidade? É ter que trabalhar em um emprego que você odeia para pagar as contas? É ter que se submeter a homens como o Barão?"
    ro "Eu não quero essa vida. Eu quero uma vida de luxo. Eu quero ser uma estrela."
    mc "Mas você pode ser uma estrela sem se vender."
    ro "Como?"
    mc "Você pode usar seu talento para o bem. Você pode usar sua voz para ajudar as pessoas."
    "Roxane laughs."
    ro "Você é tão ingênuo, [mc]. Você realmente acha que o mundo funciona assim?"
    mc "Eu sei que não é fácil. Mas é possível."
    ro "Talvez. Mas eu não estou disposta a arriscar tudo por um sonho."
    mc "Mas você está arriscando tudo ficando com o Grupo."
    ro "Eu sei o que estou fazendo."
    mc "Você não sabe. Você está sendo usada."
    ro "Eu não me importo. Eu vou conseguir o que eu quero."
    mc "Mas você não será feliz."
    ro "Eu serei feliz quando eu for rica e famosa."
    mc "Isso não é felicidade. Isso é... vazio."
    "Roxane looks at MC for a long time, her expression unreadable."
    mc "Roxane... eu não sei se essa é a verdadeira você. Ou se você é apenas mais uma mulher moldada pela Zaza."
    ro "O que você quer dizer com isso?"
    mc "Você está disposta a negar suas origens? O Distrito? Seus irmãos?"

    "Roxanes eyes flash with anger."

    ro "Onde estava a lealdade do Distrito quando eu fui entregue à Zaza ainda criança?"
    ro "Onde estava a minha família quando eu precisei deles?"
    ro "Eu não devo nada ao Distrito. Eu devo tudo à Zaza."
    mc "Mas a Zaza faz parte do Grupo. Ela está te usando."
    ro "Eu não me importo. Ela é a única família que eu já tive."
    mc "Mas você pode ter uma família de verdade. Você pode ter uma vida de verdade."
    ro "Eu tenho uma vida de verdade. Eu sou uma modelo de sucesso. Eu tenho tudo o que eu sempre quis."
    mc "Mas você não está feliz."
    ro "Eu serei feliz quando eu for rica e famosa."
    mc "Roxane... você está se iludindo."
    ro "Eu não me importo. Eu vou seguir meu caminho."
    mc "Eu espero que você mude de ideia. Mas eu respeito sua decisão."



    "Eu tenho três opções."
    "A primeira opção é roubar a Zaza e fugir com o Nathan. Isso nos daria a grana que a gente precisa para começar uma nova vida em outro lugar. Mas eu estaria estragando a vida da Zaza, da Cássia e da Roxane."

    "A segunda opção é tentar fazer com que a Zaza e a Cássia se voltem contra o prefeito. Isso poderia enfraquecer o Grupo e ajudar o Nathan a ser modelo sem o apoio deles. Mas isso é arriscado. Se eu não conseguir convencê-las, elas podem se voltar contra mim."
    "A terceira opção é ficar do lado do Grupo e deixar tudo como está. Isso seria o mais seguro para mim. Mas eu não sei se consigo viver com a consciência tranquila, sabendo o que eles fazem."
    "Eu não sei o que fazer."
    "Eu quero ajudar o Nathan. Ele é um cara legal e não merece ser usado pelo Grupo. Mas eu também não quero prejudicar a Zaza, a Cássia e a Roxane."
    "E eu tenho que pensar em mim também. Se eu fizer a coisa errada, eu posso acabar morto."
    "Eu não sei qual é a escolha certa."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
