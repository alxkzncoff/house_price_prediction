# Предсказание цен на недвижимость в Санкт-Петербурге

## Задача

Разработать модель, предсказывающую цены на недвижимость в г. Санкт-Петербург. 

### Данные

В этой работе данные были собраны самостоятельно.

## Этапы работы

### Сбор данных

Для сбора данных был использовал фреймворк **scrapy**. Данные были собраны с сайт **domofond**.

### Отчистка данных

После парсинга данные содержали лишнюю информацию и мусор. Все ненужное было удалено и почищенно, данные привиденые к читабельному виду. Так же были добавлены новые фичи.

### EDA

Здесь была проведена большая часть работы. Проанализирован каждый признак. Проведен объемный анализ числовых признаков. Убраны данные, которые больше всего были похоже на выбросы или в отличии от других не имели никакой закономерности. Например, я удалил данные которые имели слишком большую площадь (большее 400 м2) или данные, которые при большой площади имели слишком маленькую цену и наоборот. Ноут боук содержит много графиков и промежуточных выводов.

### Model

На это этапе построил три модели:

- Наивную модель. Самая простая модель, от которой можно отталкиваться дальше. Помогает понять, в сторону улучшения или ухудшения движется работа. Лучший результат по метрике MAPE **20.72%**.
- scikit-learn LinearRegression. Для этой модели воспользовался методом One Hot Encode для категориальных данных. Удалось улучшить результат относительно наивной модели. Лучший - **13.92%**.
- CatBoostRegressor. Одно из приемущество CatBoost - это то, что он способен работать с категориальными данными без предворительной обработки. Для подбора лучших параметров воспользовался встроенным в CatBoost методом grid_search(). Удалось улучшить результат почти в два раза. Лучший - **7.05%**.