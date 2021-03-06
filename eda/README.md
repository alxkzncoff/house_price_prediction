# EDA

## Признаки.

**price (Target)** - Цена жилого помещения. Наш таргет.

**page** - ссылка на объявление.

**description** - описание из объявления, составленное пользователем (риэлтор или собственик).

**flat_type** - тип жилого помешения.

**object_type** - тип здания, в котором находится жилое помещение.

**rooms** - количество комнат.

**floors** - этаж, на котором находится жилое помещение.

**total_floors** - общее количество этажей в доме.

**square** - общая площадь жилого помещения.

**kitchen_square** - площадь кухни.

**live_square** - жилая площадь, т.е. без учета кухни и санузла.

**build_matireal** - материал, из которого сделано здание.

**public_date** - дата публикации объявления.

**update_date** - дата последнего обновления объявления.

**district_rating** - рейтинг района, в котором находится жилое помещение.

**district** - район в котором находится жилое помещение.

**underground** - расстояние до ближайщей станции метро.

**metro_station** - ближайщая станция метро.

**eco_rating** - экологический рейтинг района.

**clear_rating** - рейтинг чистоты района.

**gkh_rating** - рейтинг ЖКХ района.

**neighbor_rating** - рейтинг соседей.

**kids_rating** - рейтинг условия для детей.

**sport_rest_rating** - рейтинг спорта и отдыха.

**shop_rating** - рейтинг магазинов.

**traffic_rating** - рейтинг транспорта.

**secure_rating** - рейтинг безопасности.

**life_price_rating** - рейтинг стоимости жизни.

**Числовые признак (4):** price, square, kitchen_square, live_square

**Категориальные признаки (24):** page, description, flat_type, object_type, rooms, floors, total_floors, build_matireal,
public_date, update_date, district_rating, district, underground, metro_station, eco_rating, clear_rating, gkh_rating,
neighbor_rating, kids_rating, sport_rest_rating, shop_rating, traffic_rating, secure_rating, life_price_rating.

## EDA Reports

### Pandas Profiling

- [Сырые данные.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_PANDAS_PROFILING_REPORT.html)
- [Объявления площадью до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_400M2_PANDAS_PROFILING_REPORT.html)
- [Объявления площадью до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_130M2_PANDAS_PROFILING_REPORT.html)
- [Откорректированные категориальные признаки до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_CAT_COR_FLATS_400M2_PANDAS_PROFILING_REPORT.html)
- [Откорректированные категориальные признаки до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_CAT_COR_FLATS_130M2_PANDAS_PROFILING_REPORT.html)
- [Новые признаки до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/NEW_FEATURES_400M2_PANDAS_PROFILING_REPORT.html)
- [Новые признаки до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/NEW_FEATURES_130M2_PANDAS_PROFILING_REPORT.html)

### Sweetviz

- [Сырые данные.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_SWEETVIZ_REPORT.html)
- [Объявления площадью до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_400M2_SWEETVIZ_REPORT.html)
- [Объявления площадью до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_FLATS_130M2_SWEETVIZ_REPORT.html)
- [Откорректированные категориальные признаки до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_CAT_COR_FLATS_400M2_SWEETVIZ_REPORT.html)
- [Откорректированные категориальные признаки до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/EDA_CAT_COR_FLATS_130M2_SWEETVIZ_REPORT.html)
- [Новые признаки до 400 м2.](https://alxkzncoff.github.io/house_price_prediction/NEW_FEATURES_400M2_SWEETVIZ_REPORT.html)
- [Новые признаки до 130 м2.](https://alxkzncoff.github.io/house_price_prediction/NEW_FEATURES_130M2_SWEETVIZ_REPORT.html)

Здесь была проведена большая часть работы. На вход подаем [flats.csv](https://github.com/alxkzncoff/house_price_prediction/blob/master/data/flats.csv), на выходе получаем [df.csv.](https://github.com/alxkzncoff/house_price_prediction/blob/master/data/df.csv)

В процессе был проанализирован каждый признак. 
Убраны данные, которые больше всего были похоже на выбросы или в отличии от других не имели никакой закономерности.
Например, я удалил данные которые имели слишком большую площадь (большее 400 м2) или данные, которые при большой площади имели слишком маленькую цену и наоборот.
Максимально, насколько это было возможно привел все числовые признаки к нормальному виду. Построил матрицу корреляций числовых признаков и таргета, 
а также провел регрессионный анализ. В процессе анализа старался как можно больше делать промежуточных выводов, сопровождая их графиками.
