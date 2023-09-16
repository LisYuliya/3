# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
text = '''Жизнь в сети



 Каждая перемена – это новая возможность.

    Джек Уэлч, президент компании General Electric

 Многое изменилось в Интернете с тех пор, как Джеф Безос основал свою компанию. Тогда, в 1995 году, Интернет был тем абсолютным новшеством, которое могло изменить структуру всего бизнеса. На этот счет была сделана пародийная реклама сети бистро Wendy’s – в очереди стоит пустая бочка с названием сайта.
 Кризисная ситуация в Сети началась в конце 1999-го, разгар пришелся на 2000 год и продолжался в 2001-м. Тяжелые времена для тех, кто занимается сетевым бизнесом, грозят затянуться на год-полтора. К тому времени, по прогнозам исследований журнала  Forrester , 50 % сетевых компаний разорятся.
 Зато те, кто выживет, заметно укрепят свои позиции. Это произойдет в случае, если их концепция ведения бизнеса окажется максимально эффективной. Появятся также и новые компании, но уже совершенно другого толка.
 Что явилось причиной возникновения кризиса? Финансовые затруднения, дополнившие плохо продуманные бизнес-технологии. Практически полное отсутствие финансовых барьеров для входа в сетевой бизнес позволило слишком многим захватить определенную долю рынка, что привело к неэффективной конкуренции, когда компаниям стало невыгодно поддерживать качество услуг и сохранять низкие цены. Сайты с удачной идеей в основе также поддались искушению легкой наживы и быстро разрослись, начав заниматься не свойственными им направлениями, как, например, Priceline, которая сначала продавала авиабилеты, а потом занялась продуктами питания и бензином.
 Причиной разразившегося кризиса могло явиться в том числе и то, что многие сетевые компании были не в состоянии удовлетворить потребности и запросы пользователей, заглянувших на сайт просто ради любопытства и быстро разочаровавшихся. Исследования показали, что, когда все еще только начиналось, пользователи были более терпимыми к погрешностям в обслуживании, например – к необеспеченным заказам. Сегодня покупатели гораздо требовательнее, и этот факт отрицательно сказался на репутации и благосостоянии многих сетевых фирм, а также на настроении инвесторов, что в конечном итоге породило сомнения в целесообразности существования сетевой торговли.
 Есть уверенность в том, что Amazon выйдет из кризиса победителем. Конечно, компания совершала ошибки (например, продавала оружие, инструменты и даже автомобили). Однако теперь Amazon стала более уверенной и стабильной, чем несколько лет назад. Заглянув на их сайт, можно также увидеть, что и сам бизнес компании изменился. Это по-прежнему компания, занимающаяся торговлей через Интернет, но исходная – чисто интернетовская база, которая теперь стала слишком уязвима, – переросла в реально существующий бизнес. В результате тесного сотрудничества с другими компаниями Amazon вышла за пределы Интернета.

 Гибриды

 11 апреля 2001 года Amazon заключила сделку с компанией Borders Group, второй по величине компанией по продаже книг в США, для которой Amazon теперь стала осуществлять продажу, так как собственный сайт Borders с этим не справлялся. Примерно за год до этого Amazon начала сотрудничать с Toys «R» Us, с которой они вместе продавали игрушки, видеоигры и товары для детей. Теперь сайт Borders начинает продавать не только книги, но и аудио– и видеопродукцию, а также диски. Эта компания будет заниматься поставкой товаров на склад и составлять график продаж. В обязанности же Amazon будет входить обслуживание клиентов, содержание сайта и подобные задачи. Borders будет получать часть прибыли с продаж на сайте Borders.com и платить Amazon за управление сайтом. «Мы потратили много времени и денег, чтобы покупателям было легко пользоваться нашим сайтом, – говорил представитель Amazon, – затем мы постарались, чтобы и клиенты других компаний тоже смогли использовать эти преимущества. Мы стали сотрудничать с Apple, у которых мы приобрели лицензию на использование более удобной технологии, а также с Toyrus.com – компанией, очень похожей на нас».
 Новый сайт компании Borders присоединится к Amazon, а не наоборот. Пользователи Borders.com смогут заходить на сайт через Amazon. «Мы хотим, – пояснил представитель компании, – чтобы наши пользователи смогли помимо товаров, которые они могут приобрести на сайте Borders, узнать и о другой продукции, предлагаемой нами».
 Таким образом, на пути к расширению сферы деятельности компания стремительно увеличила капитализацию и превратилась в одну из самых успешных сетевых фирм.
 Amazon стала конкурентоспособной не только на сетевом, но и на реальном рынке, от чего покупатели только выиграли. Это подтверждает верность высказывания Теодора Левитта о том, что цель любого бизнеса – найти клиента и суметь его удержать. Возможно, такая конкуренция вынуждает повышать уровень обслуживания, но не стоит также забывать и о прибыли, компенсирующей вложенные средства.
 В будущем успех будет сопутствовать тем сетевым компаниям, которые будут вести бизнес как в Сети, так и за ее пределами. К примеру, сотрудничество компании Micronpc.com и Best Buy позволило покупать компьютеры прямо у производителя – Micron Electronics через сайт Best Buy. Продукция крупнейших супермаркетов Wal-Mart стала доступнее, так как теперь товары компании можно приобрести на сайте сетевой компании AOL. Это партнерство принесло выгоду обеим компаниям – доступность в Интернете в обмен на расширившийся ассортимент.
 Как пишет Элан Битан, специалист Ernst & Young, слияние сетевых и реальных компаний приносит выгоду обоим партнерам. У компаний с обычной реально существующей инфраструктурой теперь появилась возможность легкого и относительно дешевого доступа в Интернет через сетевые компании, которые могут предложить быстрый выход на покупателя, а взамен воспользоваться более совершенной системой логистики.
 Означает ли это, что сетевая форма бизнеса некоторых компаний напоминает издание рекламного проспекта или каталога для совершения покупок не выходя из дома? Я бы в этом усомнилась, но похоже, что это действительно так. По крайней мере, для многих фирм Интернет – одна из форм дистрибуции товаров.

 Правильно поставленная цель

 В то время как Джеф Безос идет на любые ухищрения, защищаясь от нападок инвесторов и конкурентов, его обвиняют в отсутствии определенной цели. Возможно, он действительно потерял чувство целостности в отношении своего бизнеса и конечно же забыл свои собственные наставления.
 Когда Безос только начинал, он учил своих соратников никогда не терять из виду долгосрочную перспективу и равняться на нее независимо от сиюминутных изменений конъюнктуры. За год до обрушившегося на весь Интернет кризиса Безос предупреждал инвесторов о том, что «урожайная пора» (так он окрестил период полной окупаемости и получение прибыли) наступит не ранее чем через десять лет. Но в начале 2001 года, чтобы развеять страхи вкладчиков, он пообещал добиться прибыли до завершения текущего года. В результате он не только поплатился доверием своих коллег с Уолл-Стрит, но и испортил свою репутацию «славного парня» среди сотрудников, предпринимая разумные, но жесткие меры.


Что нужно, чтобы сайт был успешным

 Многие сайты потерпели неудачу и прекратили свое существование. Вот несколько правил, которые нужно знать, чтобы избежать их участи.
  1. Никакие деньги не спасут плохую идею.  Основные правила бизнеса распространяются и на Интернет. Чтобы сетевая компания развивалась, необходимо продавать то, что будут покупать. Конечно, здесь может сыграть эффект новизны, но если товар по сути своей бесполезен, если есть лучшая ему альтернатива, его очень скоро перестанут покупать.
  2. Чудеса техники не всегда упрощают ведение бизнеса.  Предположим, вам пришлось потратить 15 минут, чтобы тщательно выбрать необходимые товары, и вот, сделав выбор, вы покидаете сайт, как вдруг происходит технический сбой, и ваша тележка с покупками оказывается пустой. Что вы будете делать? Воспользуетесь более привычным способом – по телефону или по почте.
  3. Покупателям нужны реальные, а не виртуальные товары.  Да, они покупают товары виртуально, но это настоящие товары, и покупатели хотят получить их в указанный срок. В противном случае ваш доход тоже окажется в области виртуального.
 В начале своего повествования я упоминала о важности хорошего знания Интернета в таком деле, как сетевой бизнес. Именно это знание и помогло Безосу сделать свою компанию одной из лучших и известных среди пользователей. Для того чтобы пользоваться успехом, сайт должен предоставлять информацию о своих продуктах и услугах в увлекательной, удобной и интерактивной форме. В отличие от пульта телевизора, мышка позволяет быстрее переключиться с неинтересного сайта на другой и никогда уже больше не возвращаться на не понравившийся сайт. А вот если пользователь заинтересовался, он задержится надолго.
 Чтобы сделать сайт полезным для посетителей, нужно прежде всего знать, что это за пользователи. Вы должны знать свою целевую аудиторию и, что не менее важно, понимать, что ценного вы можете предложить данному клиенту и как сможете его привлечь. Сущность предлагаемой услуги или продукции сформирует определенную клиентскую базу и в дальнейшем определит стратегию компании в работе с покупателями. Несмотря на то что вы работаете в Интернете, не лишним будет дать рекламу на радио или телевидение, дабы привлечь внимание более широкого круга потенциальных клиентов.
 Оформление сайта играет важную роль. На нем обязательно должна присутствовать интересная графика, общая информация о сайте, удобная система поиска. Нельзя забывать и о другом важном моменте – логистике. Если вы хотите заниматься сетевой торговлей, хорошая система навигации просто необходима.
 Эти основные принципы, важные для создания успешного сайта, не менялись в течение последних десяти лет. Успех в Сети зависит не только от хорошей идеи. Сама идея может быть гениальной, революционной, но, воплощая ее в жизнь, нужно учитывать все те же неизменные правила. Можно привести множество примеров сайтов с неясным содержанием, плохо организованной информацией, но дело не в этом; достаточно всего лишь понять суть того, что явилось причиной кризиса сетевых компаний. Джон Мариотти, президент и создатель The Enterprise Group, автор книги «Маркетинг с умом», пришел к следующему выводу в ходе анализа деятельности многих сетевых фирм: «Они (сетевые компании) не соблюдали основные принципы ведения бизнеса, от которых, в сущности, зависит, будет ли у этого бизнеса будущее. Эти правила, подобно закону тяготения, невозможно обойти, и рано или поздно с ними придется столкнуться».
 Изжила ли себя система создания сайтов в Интернете? Вовсе нет. Прогнозы  Forrester предсказывают рост прибыли сетевых компаний с 7 млрд в 2001 году до 40 млрд в 2005-м. Эти компании, как, например, Amazon, ждет процветание, поскольку они обладают не только эффективной стратегией, но и грамотным руководителем наподобие Безоса, который не боится искать новых путей и применять не опробованные ранее технологии.
 Сможет ли Безос сдержать свое обещание и сделать компанию доходной к концу 2001 года? Да, если учесть, что обещание касалось планируемой прибыли, т. е. прибыли, зафиксированной на бумаге, а не в виде реальных долларов. Зачем же требовать от сетевой компании еще чего-то? Конечно же, время в Интернете течет быстрее, чем в реальной жизни, но и понятие прибыльности имеет отношение к бизнесу в широком смысле, а не к маркетингу. И в особенности это касается торговли.
 Amazon станет успешной компанией и надежным партнером обычных реальных фирм, если будет неизменно следовать правилу, о котором писал Левитт: «Цель бизнеса заключается в соблюдении интересов клиента, а не аналитиков с Уолл-Стрит или инвесторов».

 Возможности Интернета

 Правила правилами, но что вам делать, если вы новичок в этом деле и собираетесь предпринять первые шаги? Или вы уже в Сети, но собираетесь бросить это дело. Сейчас самое время, чтобы остаться и продолжать развиваться в Сети, – инвестиции есть, кадры имеются, компания основана. Теперь самое главное – продумать стратегию увеличения клиентской базы.
 Если вы захотите опробовать свой бизнес-план для сетевой компании, помните, что вам придется иметь дело с более низкими прибылями, чем в реальной жизни. Впрочем, постепенно система может измениться к лучшему для вашей компании, и клиентов у вас станет больше.
 Следует также учесть, что в сетевой торговле наиболее важную роль играет выбор надежной транспортной компании, а не красочное оформление сайта, – ведь важно то, что стоит за этим оформлением. Согласно наблюдениям  Business Week : «Как оказалось, основополагающую роль в сетевой коммерции играет налаженная система логистики, а не организация информации». По поводу соотношения затрат на создание крупной стабильной сетевой компании в отчете Майкла Мэндела и Роберта Хофа сказано следующее: «Необходимые затраты на Интернет колеблются в районе 15–25 млн долларов. А вот на создание склада уйдет не менее 150 млн». Авторы также цитируют Гэри Ришаля, исполнительного директора одного инвестиционного банка: «Непосредственно на саму Интернет-систему уходит порядка 10 % вкладываемых средств. Все остальное приходится на создание инфраструктуры».
 По мнению автора, спрос становится все более чувствительным к изменениям цен. Как считает профессор экономики Чикагского университета Остен Гулсби, «прибыли в сетевом бизнесе будут стремительно уменьшаться, так как конкуренция неизбежно приведет к снижению цен, что превратит весь сетевой бизнес в низкодоходный».
 Так что следует лишний раз подумать, прежде чем начать заниматься торговлей в Сети.


Как привлечь покупателя в сети

 Торговля через Интернет продолжает свое существование, но делать бизнес в Сети стало гораздо сложнее. На первый план выходит проблема зарабатывания денег. Это не означает, что вопрос привлечения клиентов потерял актуальность. По-прежнему важно не только привлечь покупателей, но и превратить их в постоянных. Вот семь правил, следуя которым можно повысить привлекательность сайта для посетителей. Правила составлены в результате исследований Дейла Троппито и Доны Пейтон, специалистов Gantry Group, консультативной организации, составляющей бизнес-планы для сетевых организаций.
  1. Неусложняйтежизньпользователям . Доступ и навигация на сайте должны быть максимально удобными и простыми, загрузка не должна превышать восьми секунд.
  2. Поощряйтеклиентов . Это будет лишним поводом для покупателя зайти на ваш сайт.
  3. Найдитепартнера . Расширяйте ваш сайт, сотрудничая с другими компаниями, торгующими сходными товарами.
  4. Создайтебезупречнуюсистемуобслуживания . Сейчас предъявляются все большие требования к качеству услуг как в Интернете, так и за его пределами. Покупатели хотят иметь доступ к информации о состоянии своих счетов, а также совершать покупки 24 часа в сутки. Нужно создать интегрированную систему доступа к любому виду информации, касающейся вашей компании.
  5. Советуйтепокупателю . Используя опыт прошлых продаж, постарайтесь заинтересовать покупателя, найти подход к каждому.
  6. Идитенавстречуклиенту . Постарайтесь понять, какая именно услуга ценится вашими клиентами больше всего, и постарайтесь предоставить ее в полном объеме.
  7. Уважайтеклиентов . Ваши клиенты должны быть осведомлены о том, какую информацию о них вы фиксируете, и быть уверенными, что эта информация будет строго конфиденциальна.
'''


text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_words[:10]

for word, count in top_10:
    print(f'{word}: {count}')