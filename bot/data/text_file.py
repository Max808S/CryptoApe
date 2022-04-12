# А file with all the necessary text commands for the bot to work


main_text = (
    "<b>CryptoApe:</b>\n\n"
    "Что бы получить цену любой интересующей вас "
    "криптовалюты достаточно написать её название: "
    "\n/bitcoin или /btc\n\nТак же можете воспользоватся поиском "
    "написав в чат монету которую ищете"
)

help_text = (
    "<b>CryptoApe Help Menu:</b>\n\n"
    "/coins - посмотреть монеты\n"
    "/categories - посмотреть категории\n"
    "/trend - топ7 поиска <a href='https://www.coingecko.com/ru/'>CoinGecko</a>\n"
    "/gas - текущая цена на газ gwei (eth)\n"
    "/restart - перезагрузить бота\n"
)

coins_text = (
    "Что бы получить цену любой интересующей вас "
    "криптовалюты достаточно написать её название: "
    "\n/bitcoin или /btc\n\nТак же можете воспользоватся поиском "
    "написав в чат монету которую ищете"
)

trend_text = (
    "Топ 7 самых популярных монет на <a href='https://www.coingecko.com/ru/'>CoinGecko</a> по поиску "
    "пользователей за последние 24 часа в порядке убывания популярности:"
)

category_text = (
    "Категории ранжируются по <b>рыночной капитализации</b> или <b>изменению цен за 24 часа</b>.\n"
    "Примечание: некоторые криптовалюты могут попадать сразу в несколько категорий."
)

market_cap_change_24h_category_text = (
    "<b>Ведущие категории криптовалют по росту цен за 24 часа</b>"
)

market_cap_category_text = (
    "<b>Ранг категории криптовалют основан на ее рыночной капитализации.</b>"
)

disclaimer = (
    "⚠️ <b>ВАЖНЫЙ ДИСКЛЕЙМЕР:</b> \nКонтент, представленный в боте, "
    "получен из сторонних источников и предназначен исключительно "
    "для информационных целей. Мы не даем гарантий в отношении этого "
    "контента, в том числе в отношении его актуальности и достоверности. "
    "\n\nЭти материалы не следует воспринимать в качестве финансовых или "
    "юридических советов. Используйте их на свой страх и риск только после "
    "тщательного анализа, исследования и проверки. Содержимое бота не "
    "может считаться предложением или руководством к действию. "
    "\n\n<b>Powered by</b> <a href='https://www.coingecko.com/ru/'>CoinGecko</a>"
)

btc_text = (
    "<b>Биткоин</b> — пиринговая платёжная система, использующая одноимённую "
    "единицу для учёта операций. Для обеспечения функционирования и защиты "
    "системы используются криптографические методы, но при этом вся информация "
    "о транзакциях между адресами системы доступна в открытом виде. \nТаким "
    "образом, он может работать без необходимости в центральном органе, таком "
    "как банк или компания. Это не похоже на выпущенные государством или фиатные "
    "валюты, такие как доллары США или евро, в которых они контролируются "
    "центральным банком страны. Децентрализованный характер позволяет ему "
    "работать в одноранговой сети, в которой пользователи могут отправлять "
    "средства друг другу, минуя посредников."
)

eth_text = (
    "<b>Ethereum</b> — криптовалюта и платформа для создания децентрализованных "
    "онлайн-сервисов на базе блокчейна, работающих на базе смарт контракта, "
    "программного кода в котором прописаны условия выполнения контракта, когда "
    "они выполнены — автоматически происходит транзакция."
)

bnb_text = (
    "<b>Binance Coin (BNB)</b> — это биржевой токен, созданный и выпущенный "
    "криптовалютной биржей Binance, хотя в 2017 году компания начинала только "
    "как криптобиржа, сегодня Binance распространила свои услуги на множество "
    "различных сфер. Согласно веб-сайту компании, ее миссия — стать поставщиком "
    "инфраструктурных услуг для всей экосистемы блокчейна."
)

sol_text = (
    "<b>Solana</b> – это продвинутый блокчейн-проект с открытым исходным кодом, "
    "который стремится использовать несколько прорывных технологий для следующего "
    "поколения DApps. Разработчики  утверждают, что его блокчейн способен поддерживать "
    "более 50 000 транзакций в секунду (TPS) при пиковой нагрузке, что делает его, "
    "пожалуй, самым быстрым блокчейном работающим в настоящее время. Для сравнения: "
    "это почти в 1 000 раз быстрее Bitcoin (~ 5-7 TPS) и более чем в 3 000 раз "
    "быстрее Ethereum (~ 15 TPS)."
)

ada_text = (
    "<b>Cardano (ADA)</b> — это децентрализованная платформа, которая позволяет "
    "выполнять сложные программируемые трансферы ценностей безопасным и масштабируемым "
    "образом. Cardano разрабатывает платформу смарт-контрактов с более продвинутым "
    "функционалом, чем любой из ныне существующих протоколов. Сообщается, в основе "
    "протокола лежит многоуровневый программный блокчейн стэк, который будет гибким, "
    "масштабируемым и разрабатывается с учетом самых строгих академических и "
    "коммерческих стандартов ПО в отрасли."
)

xrp_text = (
    "<b>XRP</b> был создан Ripple как быстрая, менее затратная и более масштабируемая "
    "альтернатива как другим цифровым активам, так и существующим платформам денежных "
    "платежей, таким как SWIFT. Реестр RippleNet поддерживается глобальным сообществом "
    "XRP, активным участником которого и является компания Ripple. \nXRP Ledger обрабатывает "
    "транзакции примерно каждые 3-5 секунд, или всякий раз, когда независимые узлы-валидаторы "
    "приходят к консенсусу в отношении порядка и действительности транзакций XRP. Этим он "
    "отличается от proof-of-work майнинг процесса Bitcoin (BTC). Валидатором Ripple может "
    "стать каждый. В настоящее время список состоит из Ripple, а также университетов, "
    "финансовых учреждений и других."
)

luna_text = (
    "<b>Terra</b> — это блокчейн-протокол, стремится выделиться за счет использования "
    "стейблкоинов с привязкой к фиату, заявляя, что она сочетает безграничные преимущества "
    "криптовалют с ежедневной стабильностью цен на фиатные валюты. Он поддерживает "
    "привязку «один к одному» с помощью алгоритма, который автоматически регулирует "
    "предложение стейблкоинов в зависимости от спроса. Это достигается путем стимулирования "
    "держателей LUNA к обмену LUNA и стейблкоинов по выгодным обменным курсам по мере "
    "необходимости, чтобы либо увеличить, либо сократить предложение стейблкоинов в "
    "соответствии со спросом."
)

dot_text = (
    "<b>Polkadot</b> — это многоцепочечный протокол сегментирования (sharding "
    "multichain protocol) с открытым исходным кодом, который облегчает кроссчейн "
    "передачу любых данных или типов активов, а не только токенов, и таким образом "
    "обеспечивает совместимость широкому спектру блокчейнов друг с другом. Такая "
    "операционная совместимость (interoperability) нацелена на создание полностью "
    "децентрализованной частной сети, управляемой пользователями, а также на "
    "упрощение создания новых приложений, систем и сервисов."
)

avax_text = (
    "<b>Avalanche</b> — самая быстрая платформа смарт-контрактов в индустрии блокчейнов, "
    "если судить по времени до завершения. Avalanche невероятно быстр, дешев и "
    "экологичен. Любое приложение с поддержкой смарт-контрактов может превзойти "
    "своих конкурентов, развернув его в Avalanche. AVAX — собственный токен Avalanche. "
    "Это дефицитный актив с жестким ограничением, который используется для оплаты "
    "комиссий, защиты платформы посредством ставок и обеспечения базовой единицы учета "
    "между несколькими подсетями, созданными в Avalanche."
)

doge_text = (
    "<b>Dogecoin (DOGE)</b> основан на популярном интернет-меме «doge» и имеет на "
    "своем логотипе сиба-ину. Отличается от протокола проверки работоспособности "
    "биткойн несколькими способами, одним из которых является использование технологии "
    "Scrypt. У альткоина также есть время блока 1 минута, а общий запас не ограничен, "
    "что означает, что количество Dogecoin, которое можно добыть, не ограничено. "
    "Использовался в основном как система чаевых на Reddit и Twitter для вознаграждения "
    "за создание или распространение качественного контента."
)

matic_text = (
    "<b>Polygon (ранее Matic Network)</b> — первая хорошо структурированная и простая в "
    "использовании платформа для масштабирования Ethereum и развития инфраструктуры. "
    "Polygon может похвастаться до 65 000 транзакций в секунду в одной боковой цепочке, а "
    "также приличным временем подтверждения блока менее двух секунд. \nФреймворк также "
    "позволяет создавать глобально доступные децентрализованные финансовые приложения на "
    "единой базовой цепочке блоков. MATIC, собственный токен Polygon, представляет собой "
    "токен ERC-20 , работающий на блокчейне Ethereum. Токены используются для платежных "
    "услуг в Polygon и в качестве расчетной валюты между пользователями, "
    "работающими в экосистеме Polygon."
)

link_text = (
    "<b>Chainlink</b> представляет собой уровень абстракции блокчейна , который позволяет "
    "использовать универсально связанные смарт-контракты. Через децентрализованную сеть "
    "оракулов Chainlink позволяет блокчейнам безопасно взаимодействовать с внешними потоками "
    "данных, событиями и способами оплаты, предоставляя критически важную информацию вне сети, "
    "необходимую для сложных смарт-контрактов, чтобы стать доминирующей формой цифрового соглашения. "
    "\nСеть Chainlink управляется большим сообществом поставщиков данных с открытым исходным "
    "кодом, операторов узлов , разработчиков смарт-контрактов, исследователей, аудиторов "
    "безопасности и многих других. Компания уделяет особое внимание обеспечению децентрализованного "
    "участия для всех операторов узлов и пользователей, желающих внести свой вклад в сеть."
)

near_text = (
    "<b>NEAR Protocol</b> — это блокчейн первого уровня , который был разработан как "
    "управляемая сообществом платформа облачных вычислений и устраняет некоторые "
    "ограничения, мешающие конкурирующим блокчейнам, такие как низкая скорость транзакций, "
    "низкая пропускная способность и плохая совместимость. Это обеспечивает идеальную среду "
    "для DApps и создает удобную для разработчиков и пользователей платформу."
)

ltc_text = (
    "<b>Litecoin (LTC)</b> — это криптовалюта, разработанная для обеспечения быстрых, "
    "безопасных и недорогих платежей за счет использования уникальных свойств технологии "
    "блокчейн. Его основное преимущество заключается в скорости и экономичности. Транзакции "
    "Litecoin обычно подтверждаются всего за несколько минут, а комиссия за транзакцию "
    "практически незначительна. Это делает его привлекательной альтернативой btc в развивающихся "
    "странах, где плата за транзакции может быть решающим фактором при выборе криптовалюты."
)

trx_text = (
    "<b>TRON</b> — это операционная система на основе блокчейна, целью которой является "
    "обеспечение пригодности этой технологии для повседневного использования. В то время как "
    "Биткойн может обрабатывать до шести транзакций в секунду, а Эфириум — до 25, TRON "
    "утверждает, что его сеть имеет пропускную способность до 2000 транзакций в секунду. "
    "\nTRON позиционирует себя как среду, в которой создатели контента могут напрямую "
    "общаться со своей аудиторией. Этот проект лучше всего описывается как децентрализованная "
    "платформа, ориентированная на обмен контентом и развлечения — и с этой целью одним из "
    "его крупнейших приобретений стал сервис обмена файлами BitTorrent еще в 2018 году."
)

xlm_text = (
    "<b>Stellar</b> — это открытая сеть, позволяющая перемещать и хранить деньги. Когда он "
    "был выпущен в июле 2014 года, одной из его целей было расширение доступа к финансовым "
    "услугам за счет охвата людей в мире, не имеющих доступа к банковским услугам, но "
    "вскоре после этого его приоритеты сместились на помощь финансовым фирмам в установлении "
    "связей друг с другом с помощью технологии блокчейн. \nСобственный токен сети служит "
    "мостом, который делает трансграничную торговлю активами менее затратной. Все это "
    "направлено на то, чтобы бросить вызов существующим платежным системам, которые часто "
    "взимают высокую плату за аналогичную услугу."
)

vet_text = (
    "<b>VeChain</b> — блокчейн-платформа для работы со смарт-контрактами, которая "
    "существует, чтобы разрушить традиционные бизнес-модели, и наиболее известен своей "
    "работой в цепочке поставок — отрасли, которая мало изменилась за десятилетия. "
    "Его работа по обеспечению децентрализованного уровня доверия для многосторонних "
    "экосистем уже добилась значительных успехов в работе с высокопоставленными клиентами "
    "и государственными органами. \n<b>VET</b> — это токен Proof of Authority (PoA), "
    "требующий относительно низкой вычислительной мощности для обеспечения сетевой "
    "безопасности по сравнению с таким протоколом, как биткойн. Недавний отчет CTI "
    "показал, что годовой углеродный след VeChain невероятно мал и составляет всего "
    "2,4% от выбросов при майнинге одного биткойна, что делает PoA невероятно "
    "эффективным механизмом консенсуса для защиты сети."
)

sand_text = (
    "<b>The Sandbox</b> представляет собой виртуальный мир на основе блокчейна, позволяющий "
    "пользователям создавать, покупать и продавать цифровые активы в форме игры. "
    "Объединяя возможности децентрализованных автономных организаций (DAO) и не "
    "взаимозаменяемых токенов (NFT), песочница создает децентрализованную платформу для "
    "процветающего игрового сообщества. \nОсновная миссия платформы Sandbox — успешно "
    "внедрить технологию блокчейна в массовые игры. Платформа фокусируется на содействии "
    "творческой модели «играй, чтобы заработать», которая позволяет пользователям "
    "одновременно быть и создателями, и игроками. Песочница использует возможности "
    "технологии блокчейна, вводя служебный токен SAND, который облегчает транзакции на платформе."
)

gala_text = (
    "<b>Gala Games</b> стремится направить игровую индустрию в другое русло, вернув игрокам "
    "контроль над своими играми. Миссия Gala Games — создавать «блокчейн-игры, в которые вам "
    "действительно захочется играть». Проект хочет изменить тот факт, что игроки могут тратить "
    "сотни долларов на внутриигровые активы и бесчисленные часы, проведенные за игрой, которые "
    "можно отнять у них одним нажатием кнопки. Компания планирует вновь привнести творческое "
    "мышление в игры, предоставив игрокам контроль над играми и внутриигровыми активами с помощью "
    "технологии блокчейн . Токен GALA работает на Ethereum и блокчейне Binance Smart Chain (BSC). "
    "Сеть защищена собственным набором узлов, называемых узлами основателя. Gala Games указывает "
    "не более 50 000 узлов Founder, которые проверяют внутриигровые транзакции и защищают сеть."
)

oasis_text = (
    "<b>Oasis Network (ROSE)</b> поддерживает высокий уровень масштабируемости, низкую "
    "плату за газ и монетизацию токенов. Он также направлен на улучшение функций "
    "конфиденциальности, чтобы облегчить использование конфиденциальных данных в DeFi. "
    "Он обеспечивает масштабируемость за счет разделения консенсуса и выполнения, что "
    "позволяет нескольким ParaTimes обрабатывать транзакции параллельно и предотвращает "
    "замедление более простых транзакций более сложными."
)

gas_text = (
    "За проведение любой транзакции и действия в блокчейне Ethereum "
    "взимается комиссия, которую получает майнер. \nМайнеры сети подтверждают "
    "транзакции и решают, какие из них войдут в новый блок сети. \nКомиссия за "
    "транзакцию исчисляется в газе, а оплачивается в эфире. \nИз чего выходит, "
    "что <b>газ — это «топливо» сети Ethereum</b>, которое используется для проведения "
    "транзакций, выполнения смарт-контрактов и запуска DApps, "
    "а также для оплаты хранения данных."
)