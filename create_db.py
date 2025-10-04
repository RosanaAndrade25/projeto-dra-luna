import sqlite3
import os

# Cria a pasta 'instance' se não existir
os.makedirs('instance', exist_ok=True)

# Remove o banco antigo para começar do zero
db_path = os.path.join('instance', 'questions.db')
if os.path.exists(db_path):
    os.remove(db_path)

# Conecta ao banco de dados (cria um novo)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Cria a tabela de perguntas
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    image_url TEXT
)
''')

# Cria a tabela de opções
cursor.execute('''
CREATE TABLE IF NOT EXISTS options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    feedback TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions (id)
)
''')

# Lista de 20 perguntas com opções e feedbacks
questions_data = [
    {
        "text": "Ajude o polvo Pingo a fugir do tubarão! Que cor ele deve ficar para se esconder nas algas?",
        "image": "polvo.png",
        "options": [
            ("Rosa choque!", False, "Quase! Mas será que um tubarão não veria um polvo rosa choque dançando nas algas? Vamos pensar numa cor que se misture com o fundo... 🌿"),
            ("Verde e marrom, igual às algas!", True, "Isso mesmo! 🎉 O polvo é um mestre da camuflagem. Ele muda de cor para se esconder e confundir os inimigos. Parabéns, cientista!"),
            ("Azul brilhante!", False, "Uh-oh! 😄 Um polvo azul brilhante seria como uma luz de neon no fundo do mar! O tubarão viria correndo. Será que uma cor mais discreta funcionaria melhor?")
        ]
    },
    {
        "text": "A Dra. Luna encontrou uma plantinha triste. O que ela precisa para ficar forte e feliz?",
        "image": "plantinha.png",
        "options": [
            ("Um cobertor quentinho!", False, "Que fofo! 🧸 Mas plantas não sentem frio como a gente. Elas precisam de algo que vem do céu... será que é... luz? ☀️"),
            ("Luz do sol, água e terra!", True, "Exatamente! 🌞 As plantinhas são como pequenas fábricas de comida. Elas usam a luz do sol, a água e os nutrientes da terra para crescer. Você é incrível!"),
            ("Um abraço apertado!", False, "Aww, que carinho! 💖 Mas as plantas não têm braços para abraçar. Elas se alimentam de uma forma mágica, usando a luz do sol!")
        ]
    },
    {
        "text": "O camaleão Carlito está na floresta. Por que ele muda de cor?",
        "image": "camaleao.png",
        "options": [
            ("Para combinar com a roupinha que a Dra. Luna colocou nele!", False, "Interessante! 👗 Mas e se ele estiver na floresta, sem roupa nenhuma? Será que ele muda de cor pra sumir entre as folhas? 🍃"),
            ("Para se esconder dos predadores e pegar suas comidinhas!", True, "Uau! 🎯 Você entendeu tudo! O camaleão muda de cor para se camuflar, ficando invisível para os perigos e para suas presas. Genial!"),
            ("Porque ele está com vergonha!", False, "Hahaha, que gracinha! 😊 Mas os camaleões não sentem vergonha como a gente. Eles têm um superpoder: a camuflagem!")
        ]
    },
    {
        "text": "A tartaruga Teca carrega sua casinha nas costas. Para que ela serve?",
        "image": "tartaruga.png",
        "options": [
            ("Para guardar seus brinquedos!", False, "Que ideia divertida! 🧸 Mas a casca da tartaruga não é um baú. É parte do seu corpo, como um escudo! 🛡️"),
            ("Para se proteger dos perigos, como uma armadura!", True, "Isso aí! 🐢 A casca é a sua armadura natural. Quando sente medo, ela se esconde dentro dela. Você é um gênio da natureza!"),
            ("Para ficar mais bonita no desfile das florestas!", False, "Ela é linda mesmo! 💃 Mas a casca não é só enfeite. É uma proteção super importante. Será que ela serve para se esconder?")
        ]
    },
    {
        "text": "O morcego Morceguito dorme de cabeça para baixo. Por quê?",
        "image": "morcego.png",
        "options": [
            ("Porque gosta de brincar de 'mundo de ponta-cabeça'!", False, "Hahaha, deve ser divertido! 🎠 Mas tem um motivo prático: assim ele pode decolar voando rapidinho se um perigo aparecer! 🦇"),
            ("Porque suas patinhas são feitas para agarrar, não para ficar em pé!", True, "Perfeito! ✅ Suas patas traseiras são como ganchos fortes. Ele se pendura e fica pronto para voar em um piscar de olhos. Incrível, não é?"),
            ("Porque tem tontura e acha que o chão é o teto!", False, "Que história engraçada! 😄 Mas os morcegos não têm tontura. Eles são acrobatas natos e escolhem esse jeito por ser o mais seguro para eles.")
        ]
    },
    {
        "text": "As girafas têm pescoços enormes. Para que servem?",
        "image": "girafa.png",
        "options": [
            ("Para balançar como um balanço e brincar com os passarinhos!", False, "Que sonho lindo! 🎠 Mas o pescoço comprido tem uma missão muito importante... será que é para alcançar algo bem lá em cima? 🍃"),
            ("Para alcançar as folhas mais altas das árvores, onde ninguém mais chega!", True, "Isso mesmo! 🌿 Elas são as rainhas das copas das árvores. Com seu pescoço longo, comem as folhas mais fresquinhas. Você pensa como uma girafa!"),
            ("Para ficar mais perto das nuvens e ouvir as histórias que elas contam!", False, "Que poesia! ☁️ Mas as girafas são práticas. Elas usam o pescoço para uma missão deliciosa: comer! O que será que está lá em cima nas árvores?")
        ]
    },
    {
        "text": "O peixe-palhaço Nemo vive dentro de uma anêmona. Por que ele não se machuca?",
        "image": "peixepalhaco.png",
        "options": [
            ("Porque a anêmona é seu melhor amigo e faz cócegas, não machuca!", False, "Que amizade linda! 💞 Mas tem um segredo científico: o peixe-palhaço tem uma camada de muco que o protege dos ferrões da anêmona!"),
            ("Porque ele tem uma capa de herói invisível que o protege!", False, "Hahaha, herói mesmo! 🦸 Mas na verdade, ele tem uma proteção natural, um muco especial na pele que impede que a anêmona o machuque. Legal, né?"),
            ("Porque ele e a anêmona são parceiros: ele se protege, e ela ganha comida!", True, "Exatamente! 🤝 É uma parceria perfeita! O peixe se esconde dos perigos, e em troca, limpa a anêmona e afasta peixes que querem comê-la. Amigos inseparáveis!")
        ]
    },
    {
        "text": "Por que os ursos polares têm pelo branco?",
        "image": "ursopolar.png",
        "options": [
            ("Porque adoram neve e querem parecer um boneco de neve gigante!", False, "Que fofo! ⛄ Mas tem um motivo de sobrevivência: será que a cor branca ajuda ele a se esconder em algum lugar? ❄️"),
            ("Para se camuflar na neve e no gelo, ficando invisível para suas presas!", True, "Uau! 🕵️‍♀️ Você é um detetive da natureza! O pelo branco é sua camuflagem perfeita no Ártico. Assim, ele pode surpreender as focas. Sensacional!"),
            ("Porque tomou muito sorvete de baunilha e ficou todo branquinho!", False, "Hahaha, que barriga cheia! 🍦 Mas na verdade, a cor branca é uma adaptação incrível para viver onde tudo é gelo e neve. O que será que ele está tentando esconder?")
        ]
    },
    {
        "text": "As abelhas fazem mel. Mas por que elas visitam tantas flores?",
        "image": "abelha.png",
        "options": [
            ("Mandando mensagens de texto com anteninhas!", False, "Hahaha, que tecnologia! 📱 Mas elas usam um método antigo e eficiente: deixam um cheirinho no caminho para guiar as amigas!"),
            ("Para coletar néctar e, sem querer, ajudar as flores a nascerem!", True, "Isso aí! 🐝 Enquanto bebem o néctar, o pólen gruda nelas e vai para outras flores, fazendo nascerem frutos e sementes. Elas são jardineiras do mundo! Parabéns!"),
            ("Porque estão perdidas e procuram o caminho de casa!", False, "Pobrezinhas! 🏡 Mas elas sabem exatamente para onde vão. Cada flor é uma parada para coletar comida. E no caminho, elas fazem mágica com as plantas!")
        ]
    },
    {
        "text": "O sapo Cururu tem a pele úmida. Por que isso é tão importante?",
        "image": "sapo.png",
        "options": [
            ("Porque ele adora tomar banho e nunca seca!", False, "Que limpinho! 🛁 Mas a pele úmida é como se fosse um segundo pulmão. Ele respira pela pele também! Será que isso ajuda ele a viver na água e na terra?"),
            ("Para poder respirar pela pele e viver na água e na terra!", True, "Exatamente! 🐸 Os sapos são anfíbios, que vivem nos dois mundos. A pele úmida permite que o oxigênio entre, mesmo debaixo d'água. Você é demais!"),
            ("Porque ele suou muito jogando futebol com os grilos!", False, "Hahaha, que jogo animado! ⚽ Mas a pele úmida não é suor, é uma característica especial que ajuda ele a respirar fora da água também. Incrível, né?")
        ]
    },
    {
        "text": "As formigas vivem em grandes colônias. Como elas se comunicam?",
        "image": "formiga.png",
        "options": [
            ("Mandando mensagens de texto com anteninhas!", False, "Hahaha, que tecnologia! 📲 Mas elas usam um método antigo e eficiente: deixam um cheirinho no caminho para guiar as amigas!"),
            ("Deixando um rastro de cheiro com seu corpo para guiar as outras!", True, "Isso mesmo! 👃 Elas soltam um cheiro especial, um feromônio, que forma um caminho invisível. É como um GPS natural! Você é um cientista nota 10!"),
            ("Gritando bem alto: 'Ei, por aqui!'", False, "Que barulho! 📢 Mas elas são silenciosas. Usam antenas para sentir o mundo e deixam um rastro de cheiro para se comunicar. Que tal pensar em um 'mapa de cheiros'?")
        ]
    },
    {
        "text": "O beija-flor beija as flores? Por que ele voa tão perto delas?",
        "image": "beijaflor.png",
        "options": [
            ("Porque é apaixonado pelas flores e dá beijinhos nelas!", False, "Que romance! 💘 Mas ele está atrás de um tesouro: o néctar, um suco docinho dentro da flor. E no caminho, ajuda a flor a ter filhotinhos!"),
            ("Para beber o néctar e, sem querer, levar o pólen para outras flores!", True, "Perfeito! 🌺 Ele é um beija-flor, mas também um entregador de pólen! Enquanto toma seu suco, ajuda as flores a se reproduzirem. Uma parceria doce!"),
            ("Porque está brincando de esconde-esconde com as borboletas!", False, "Que brincadeira divertida! 🦋 Mas ele está focado na missão: encontrar o néctar. E nessa missão, ele faz um trabalho importantíssimo para as plantas. O que será?")
        ]
    },
    {
        "text": "O porco-espinho Espinholino tem espinhos. Para que servem?",
        "image": "porcoespinho.png",
        "options": [
            ("Para pentear o cabelo dos outros animais!", False, "Que pente fofo! 💇 Mas os espinhos são uma defesa poderosa. Quando se sente ameaçado, ele vira uma bola de espetos! Será que é para se proteger?"),
            ("Para se proteger dos predadores, virando uma bola de espetos!", True, "Isso aí! 🦔 Seus espinhos são sua armadura. Nenhum predador quer levar uma espetada! Você entendeu perfeitamente a defesa dele. Parabéns!"),
            ("Porque ele adora abraçar e os espinhos são seu jeito de carinho!", False, "Hahaha, cuidado com esse abraço! 🤗 Na verdade, os espinhos são para afastar quem quer lhe fazer mal. É seu escudo natural. Muito esperto, não é?")
        ]
    },
    {
        "text": "As baleias são enormes, mas bebem leite quando são filhotes. O que isso significa?",
        "image": "baleia.png",
        "options": [
            ("Que elas adoram tomar mamadeira com canudinho gigante!", False, "Que imagem engraçada! 🍼 Mas o leite é a primeira comida de todos os mamíferos. Sim, as baleias são mamíferos, assim como nós!"),
            ("Que as baleias são mamíferos, assim como os humanos e os cachorros!", True, "Exatamente! 🐋 Mesmo vivendo no mar, as baleias são mamíferos. Elas nascem de barriga de mãe e mamam leite. Você é um gênio da ciência!"),
            ("Que elas confundem o mar com um copão de leite achocolatado!", False, "Hahaha, que sede! 🥛 Mas não é isso. O fato de mamarem leite é a prova de que são mamíferos, não peixes. Incrível como a natureza é sábia, né?")
        ]
    },
    {
        "text": "O caranguejo Carangola tem uma casca dura. O que acontece quando ele cresce?",
        "image": "caranguejo.png",
        "options": [
            ("Ele vai à loja comprar uma casca maior, do seu tamanho!", False, "Hahaha, que compras! 🛒 Mas ele não precisa de loja. Ele faz algo incrível: troca a casca velha por uma nova, maior!"),
            ("Ele troca a casca velha por uma nova, maior, num processo chamado muda!", True, "Uau! 🦀 Você sabe tudo! Esse processo se chama 'muda'. Ele sai da casca apertada e espera a nova endurecer. É como ganhar uma armadura nova! Sensacional!"),
            ("Ele estica a casca velha com um ferro de passar roupa!", False, "Que ideia criativa! 👔 Mas a casca não estica. Ele precisa abandonar a velha e esperar a nova crescer. É um momento delicado e mágico na vida dele!")
        ]
    },
    {
        "text": "As corujas enxergam muito bem à noite. Por que os olhos delas são tão grandes?",
        "image": "coruja.png",
        "options": [
            ("Porque adoram usar óculos de sol à noite e precisam de lentes grandes!", False, "Hahaha, que estilo! 😎 Mas os olhos grandes captam mais luz, o que é essencial para caçar no escuro. Será que é por isso?"),
            ("Para captar a pouca luz da noite e enxergar perfeitamente no escuro!", True, "Isso mesmo! 🌙 Seus olhos são como telescópios noturnos. Eles captam cada raio de luz, tornando a noite clara para ela. Você tem olhos de cientista!"),
            ("Porque ficam surpresas com tudo que veem à noite e os olhos arregalam!", False, "Que sustos! 😲 Mas na verdade, é uma adaptação incrível para a vida noturna. Olhos grandes = mais luz = visão perfeita na escuridão. Incrível, né?")
        ]
    },
    {
        "text": "O jacaré Joca fica parado na água com só os olhos de fora. Por que ele faz isso?",
        "image": "jacare.png",
        "options": [
            ("Porque está brincando de 'estátua' com os peixinhos!", False, "Que jogo divertido! 🐟 Mas ele está usando uma tática de caça. Ficando quase invisível, ele surpreende sua presa. Será que é para caçar?"),
            ("Para ficar escondido e surpreender suas presas quando elas se aproximam!", True, "Exatamente! 🐊 Ele é um caçador paciente. Parece um tronco, mas está sempre alerta. Quando a presa chega perto... SURPRESA! Você é um estrategista nato!"),
            ("Porque está com calor e só quer refrescar os olhos!", False, "Que refrescante! 🌊 Mas ele está em modo de caça. Esconder o corpo é sua melhor estratégia para pegar um peixe distraído. Muito esperto, não é?")
        ]
    },
    {
        "text": "As borboletas Monarca viajam milhares de quilômetros. Como elas sabem para onde ir?",
        "image": "borboleta.png",
        "options": [
            ("Elas seguem o cheiro das flores mais bonitas do caminho!", False, "Que viagem perfumada! 🌸 Mas elas usam o sol como bússola e têm um mapa interno incrível. É uma jornada mágica e misteriosa!"),
            ("Elas usam o sol como bússola e têm um instinto de navegação incrível!", True, "Uau! 🧭 Você desvendou o mistério! Mesmo nunca tendo feito a viagem antes, elas sabem o caminho. É um instinto poderoso. Você é um navegador da natureza!"),
            ("Elas seguem um GPS que a Dra. Luna instalou nas asinhas delas!", False, "Hahaha, que tecnologia! 🛰️ Mas a natureza é mais esperta. Elas usam o sol e o campo magnético da Terra como guia. Uma jornada épica sem aparelhos!")
        ]
    },
    {
        "text": "O elefante usa a tromba para muitas coisas. Qual dessas NÃO é uma função da tromba?",
        "image": "elefante.png",
        "options": [
            ("Beber água e jogar água no corpo para se refrescar!", False, "Isso mesmo, ele faz isso! 🐘 A tromba é como um braço, nariz e chuveiro ao mesmo tempo! Mas tem uma coisa que ele NÃO faz com ela..."),
            ("Comer direto pela tromba, como se fosse um canudo!", True, "Quase! 🍃 Ele usa a tromba para pegar a comida e levar até a boca, mas não engole pela tromba. Ela é uma superferramenta, mas a comida vai para a boca! Boa tentativa!"),
            ("Cheirar, tocar e até cumprimentar outros elefantes!", False, "Exatamente! 👋 A tromba é cheia de funções. Ela é sensível e cheia de músculos. Mas ela não é usada para engolir a comida, só para pegar e levar até a boca!")
        ]
    },
    {
        "text": "Parabéns, você chegou ao fim da jornada! O que você mais gostou de descobrir hoje?",
        "image": "fim.png",
        "options": [
            ("A camuflagem dos animais!", False, "Que descoberta incrível! 🦎 A natureza é cheia de truques de mágica para se esconder."),
            ("As parcerias entre os seres vivos!", False, "Lindo, não é? 🤝 Todos se ajudam num grande quebra-cabeça da vida."),
            ("Tudo! Quero ser cientista e descobrir mais!", True, "ISSO AÍ! 🚀 Você tem o espírito de um verdadeiro explorador! Continue curioso, continue perguntando. O mundo está cheio de mistérios esperando por você, Dra. ou Dr. Cientista!")
        ]
    }
]

# Insere todas as perguntas e opções no banco de dados
for q_data in questions_data:
    cursor.execute('''
    INSERT INTO questions (text, image_url) VALUES (?, ?)
    ''', (q_data["text"], f"static/{q_data['image']}"))
    question_id = cursor.lastrowid

    for option_text, is_correct, feedback in q_data["options"]:
        cursor.execute('''
        INSERT INTO options (question_id, text, is_correct, feedback) VALUES (?, ?, ?, ?)
        ''', (question_id, option_text, is_correct, feedback))

# Salva e fecha a conexão
conn.commit()
conn.close()

print("🎉 Banco de dados criado com sucesso! 20 perguntas mágicas foram inseridas.")
print("➡️  Lembre-se de colocar as imagens na pasta 'static/':")
for q_data in questions_data:
    print(f"   - {q_data['image']}")