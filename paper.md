﻿# Исследование путей автоматизации процесса проверки студенческих научных статей в рамках курса "Основы подготовки научных публикаций"

Ключевые слова: текст, научный стиль, автоматизация, сервис, текстовый анализ.

## Аннотация 

В данной статье были рассмотрены способы автоматизации уже существующего сервиса для проверки студенческих работ в рамках курса "Основы подготовки научных публикаций". Для достижения цели был поставлен ряд задач, таких как определение желаемой работы веб-сервиса и проектирование сценария действий сервиса. Выявлены причины актуальности автоматизации текстового анализатора, проведён анализ схожих по применению сервисов и выявлены критерии, необходимые для автоматизации работы с текстовым анализатором. В ходе сравнения аналогичных сервисов были обнаружены их недостатки, в связи с которыми сформулированы требования для автоматизированного сервиса. В результате проделанной работы был разработан вариант автоматизации сервиса проверки студенческих работ с помощью веб-сервиса GitHub и его встроенных модификаций, таких как GitHub Actions, также было принято решение по расширению используемого сервисом словаря с помощью добавления в него жаргонизмов. 

## Введение
Научная публикация — важный аспект в карьере учёных, например, кандидата наук или профессора. Благодаря научным статьям растёт их профессионализм и статус в коллективе, повышается квалификация. Статьи могут содержать интересную для читателей информацию и являться достоверным источником знаний и опорой для других публикаций на смежные тематики. Не только те, кто читает лекции для студентов, нуждаются в научных статьях: для учащихся вузов это будет несомненный большой плюс, так как наличие у студента научных публикаций позволяет ему претендовать на гранты в университетах, а также является поддержкой различных проектов, дипломов и диссертаций.

Однако, написание научной статьи требует соблюдения ряда правил и требований, чтобы статься имела статус "научной". В ходе написания работы может оказаться, что в её содержании допущен ряд ошибок, которые не позволяют "пропустить" публикацию. В связи с этим был создан сервис для проверки научных публикаций студентов в рамках курса "Основы подготовки научных публикаций", который позволяет избавиться от ручной проверки статьи и предоставить работу компьютеру [1]. Данный сервис будет полезен не только студентам данного курса, но и другим научным деятелям, желающим проверить свою работу на корректность. К сожалению, данный сервис не автоматизирован и требует ввода ряда настроек, которые можно и нужно избежать, а также не позволяет распознать и проверить какие-либо отдельные части публикации.

Объектом исследования является проверка студенческих работ в рамках курса "Основы подготовки научных публикаций", предметом исследования - автоматизация процесса проверки вышеуказанных работ. Целью данной работы является автоматизация имеющегося сервиса для процесса проверки студенческих работ в рамках курса "Основы подготовки научных публикаций".

Для достижения цели необходимо решить следующие задачи:
1. Ознакомиться с требованиями по оформлению научных публикаций.
2. Проанализировать, каким образом происходит работа с сервисом по проверке публикации.
3. Определить, каким образом будет происходить диалог между сервисом и пользователем.
4. Продумать варианты представления результатов работы сервиса (например, краткий и быстрый ответ, и развёрнутый и медленный).
5. Спроектировать и автоматизировать работу с сервисом, избавившись от лишних действий и настроек.

## Обзор предметной области
Для сравнения отбирались аналоги, предоставляющие свободный доступ к автоматизированному (автоматическому) SEO-анализу текста и его результатам и работающие в режиме онлайн. Ниже представлено краткое описание отобранных для сравнения аналогов:

1. **Главред** - сервис для улучшения текста [2]. Помогает находить в тексте языковой мусор, рекламные и журналистские штампы, признаки плохого синтаксиса, иными словами, данный сервис помогает определить соответствие текста информационному стилю.

2. **Тургенев** - сервис для стилистической проверки текста [3]. Помогает выявить языковой мусор, а также потенциальные и явные стилистические проблемы.

3. **ADVEGO** - сервис для семантического анализа текста [4]. Результатом анализа является статистика по словам в тексте, водность и количество грамматических ошибок.

4. **Istio** - сервис для семантического анализа текста [5]. Позволяет получить статистику по словам в тексте, водность и орфографические ошибки.

5. **Text.ru** - сервис для семантического анализа текста [6]. Предоставляет статистику по словам в тексте, процент водности* и проверяет наличие орфографических ошибок.

* Водность - это процент содержания в тексте ничего не значащих, не несущих полезной информации слов (стоп-слов).

Для сравнения вышеперечисленных аналогов были выбраны следующие критерии:

### Развёрнутость текстового анализа
Возможность получить понятный и краткий анализ, разбор конкретных ошибок и примеры их устранения.

### Способность корректно анализировать научный стиль текста
В рамках курса "Основы подготовки научных публикаций" в основной рассматриваются статьи на тему естественных и точных наук, что может накладывать некоторые ограничения на проверку.

### Возможность сохранения предыдущих результатов анализа
Зачастую пользователю необходимо не просто анализировать статью, но и сравнить её с предыдущей версией, или, например, просмотреть сводную таблицу результатов анализа нескольких проанализированных раннее статей и сохранить их.

Результаты сравнения аналогов по отобранным критериям представлены в таблице ниже (см. табл. 1).

Символ "+" соответствует наличию заданного критерия у аналога, "-", соответственно, его отсутствие.

Таблица 1 - Сравнение аналогов

|                                                               |  Главред  |  Тургенев  |  ADVEGO  |  Istio  | Text.ru  |
| ------------------------------------------------------------- | --------- | ---------- | -------- | ------- | -------- |
| Развёрнутость текстового анализа                              |     +     |      +     |     -    |    -    |     -    |
| Способность корректно анализировать научный стиль текста      |     -     |      +     |     -    |    -    |     -    |
| Возможность сохранения предыдущих результатов анализа         |     -     |      -     |     -    |    -    |     -    |

Проведя анализ сравнения аналогов, можно сделать вывод, что среди всех представленных сервисом наилучшим является сервис "Тургенев", однако ни один из аналогов не позволяет сохранять результаты предыдущих анализов текстов. Также было выявлено, что не все аналоги способны корректно распознать научный стиль текста, из-за чего статься впоследствии может содержать стилистические ошибки.


## Выбор метода решения
В ходе обзора существующих текстовых анализаторов было выяснено, что:

- не все сервисы предоставляют полную и развёрнутую информацию в результате анализа текста;
- рассмотренные аналоги не предоставляют возможности сохранять результат работы с текстом;
- в данных сервисах не предусмотрен доступ к просмотру результатов предыдущих анализов;
- большинство сервисов не способно различить научный стиль текста.

Все вышеперечисленные проблемы могут сильно повлиять на конечный результат, например, игнорирование научного стиля текста влечёт за собой необнаружение каких-либо стилистических ошибок и наличие в итоговом варианте статьи неверной лексики.

Таким образом, можно выявить следующие требования к решению данной задачи: 

1. Сервис должен предоставлять доступ к предыдущим результатам анализа.
2. Сервис должен давать возможность пользователю сохранить результаты.
3. Сервис должен быть ориентирован на научный стиль текста.
4. Анализ текста должен давать полную и чёткую информацию об ошибках.

## Описание метода решения
В результате сравнения аналогов были показаны недостатки их работы в связи с тем, что данные сервисы не способны производить различные манипуляции с результатами анализа текста, а также производят анализ не на основе научного стиля.

Для того, чтобы результаты каждого анализа сохранялись и их можно было бы сохранить локально, можно воспользоваться веб-сервисом для хостинга IT-проектов GitHub [7]. Процесс обработки научной статьи может выглядеть следующим образом:
	- создан репозиторий для курса "Основы подготовки научных публикаций",
	- для того, чтобы отправить работу на проверку, необходимо создать Pull Request со статьёй,
	- автоматизированная программа проверяет работу на основные грубые ошибки согласно требованиям,
	- после всех соответствующих исправлений, исправленная работа отправляется проверяющему для более глубокого и детального анализа. 

То есть, решение может представлять собой автоматизированного робота на вышеупомянутой платформе, который в автоматическом режиме будет выполнять предварительную проверку текстов перед передачей их непосредственно в руки человеку. В таком режиме решается проблема сохранения предыдущих результатов и доступа к ним, так как все Pull Request'ы сохраняются в истории репозитория. Для реализации роботизированной проверки можно обратиться к одной из встроенных функций GitHub'а, имеющей название GitHub Actions [8]. GitHub Actions позволяет автоматизировать рабочие процессы непосредственно в репозитории GitHub без использования серверов для автоматизации (например, Jenkins). 

Существующий сервис может распознавать научный стиль благодаря трём числовым критериям: уровень ключевых слов в тексте, процентное соотношение стоп-слов и общего количества слов в тексте, значение отклонения текста статьи от идеальной кривой по Ципфу [9]. Для того, чтобы улучшить работу сервиса по отношению к научному стилю, необходимо расширить используемый словарь, добавив в него часто используемые жаргонизмы, присущие работникам в научной и IT сфере, либо создать ещё один, где будут содержаться исключительно подобные слова в русском и английском вариантах. Так как окончательная проверка в любом случае осуществляется человеком, дополнять словарь всеми существующими жаргонизмами необходимости нет.

## Заключение
В результате работы были сформулированы требования, необходимые для автоматизации проверки научных статей, приведён сравнительный анализ аналогичных сервисов, позволяющих выполнить проверку текста в целом, но неспособных распознать научный стиль текста и проделывать манипуляции с результатами анализов. В связи с этом, было предложено решение, связанное с созданием автоматизированного робота, реализованного на платформе GitHub, который будет осуществлять предварительную проверку работ перед передачей её проверяющему человеку. Также для выполнения одного из требований было принято решение расширить используемый для проверки статей словарь, дополнив его жаргонизмами, присущими в использовании работниками в научной и технической сфере деятельности.

В дальнейшем планируется программно автоматизировать ранее разработанный веб-сервис, выполняющий проверку студенческих работ в рамках курса "Основы подготовки научных публикаций".

## Список литературы
1. Веб-сервис автоматизированной проверки наиболее частых ошибок в научных текстах. Режим доступа: https://github.com/EduardBlees/Master-s-thesis (дата обращения: 19 декабря 2019)
2. Сервис проверки текста на соответствие информационному стилю "Главред". Режим доступа: https://glvrd.ru/ (дата обращения 4 декабря 2019)
3. Сервис оценки качества текста "Тургенев". Режим доступа: https://turgenev.ashmanov.com/ (дата обращения 4 декабря 2019)
4. Сервис оценки качества текста "ADVEGO". Режим доступа: https://advego.com/text/seo/ (дата обращения 4 декабря 2019)
5. Сервис оценки качества текста "Istio". Режим доступа: https://istio.com/rus/text/analyz/ (дата обращения 4 декабря 2019)
6. Сервис оценки качества текста "Text.ru". Режим доступа: https://text.ru/seo (дата обращения 4 декабря 2019) 
7. Веб-сервис для хостинга IT-проектов и их совместной разработки GitHub. Режим доступа: https://github.com/ (дата обращения 18 декабря 2019)
8. Документация GitHub Actions. Режим доступа: https://help.github.com/en/actions/automating-your-workflow-with-github-actions (дата обращения: 18 декабря 2019)
9. Блеес Э.И., Заславский М.М. Экспериментальное исследование критериев соответствия текста научному стилю. – 2018.