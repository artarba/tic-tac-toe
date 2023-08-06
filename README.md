# tic-tac-toe

### Запуск:

```bash
docker build -t tic-tac-toe .
```

```bash
docker run -d -p 8000:8000 tic-tac-toe
```

#### Перейти на [localhost:8000/docs](http://localhost:8000/docs)
- ##### Открывается Swagger -> Жмем по "Try it out" -> Загружаем своё изображение -> Execute

### Дополнительная информация:
- Замечен местами некорректный результат для некоторых шрифтов. В тестировании использовались шрифты:
  - Comic Sans MS
  - DejaVu Sans
- В папке **img** лежит несколько вариантов с использованием шрифтов, которые указаны выше.