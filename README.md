![title](img/hpp.png)
# Предсказание цен на недвижимость в Санкт-Петербурге

## Цели и задачи проекта

**Цели проекта**:
 - Разработать модель, предсказывающую цены на недвижимость в г. Санкт-Петербург.
 - Закрепить навыки, пройдя весь цикл, от сбора данных до построения модели.
 - Получить хороший резльтат предсказаний.
 
**Задачи проекта**:
 - Научится пользоваться фреймворком scrapy.
 - Собрать данные.
 - Провести предобработку данных (избавиться от дубликатов, пропусков, выбросов).
 - Провести feature-engineering (отбор существующих признаков, синтез новых признаков, нормализация или стандартизация числовых признаков, кодирование категориальных признаков).
 - Построить несколько моделей, провести анализ результатов работы моделей (применение основных методов оценки ошибки обучения, нахождение оптимальных параметров обучения, выявление переобучения моделей).

## Структура репозитория

- [Spider](https://github.com/alxkzncoff/house_price_prediction/tree/master/domofond)
- [Data](https://github.com/alxkzncoff/house_price_prediction/tree/master/data)
- [EDA](https://github.com/alxkzncoff/house_price_prediction/tree/master/eda)
- [ML](https://github.com/alxkzncoff/house_price_prediction/tree/master/ml)

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
