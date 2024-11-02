# Project_1

1. Краткое описание программного обеспечения
Это программное обеспечение предназначено для визуализации графов, представленных матрицами смежности. Пользователь может задать матрицу смежности и метки для узлов, после чего программа отобразит граф, расположив узлы по кругу.

2. Инструкция по установке
Для работы программы необходимо установить Python и несколько библиотек.

    скопируйте или скачайте проект:

git clone https://github.com/MegaCraTex/Project_1
cd graph-visualization.py
    Установите зависимости с помощью pip:

pip install numpy networkx matplotlib
Все необходимые зависимости установлены.

3. Инструкция по сборке
Сборка приложения не требуется, так как это скрипт на Python, который можно запустить напрямую.
python graph_visualization.py

4. Документация
Функции и их описание:
    draw_graph(adj_matrix, labels) — главная функция для создания и отображения графа.
    Параметры:
    adj_matrix — двумерный массив, представляющий матрицу смежности, где каждая строка и столбец соответствует узлу.
    labels — словарь, задающий метки для каждого узла, где ключ — это индекс узла, а значение — его метка.
    Описание процесса:
    Функция создает граф на основе матрицы смежности.
    Узлы графа размещаются по кругу для лучшей визуализации.
    Граф отображается с цветными узлами, настройкой размера, шрифта и цвета ребер.
    Пример использования:
    Пример матрицы смежности и меток узлов представлен ниже. Выполнив данный код, вы получите граф:

python
Копировать код
adj_matrix = [
    [0, 1, 0, 0, 0, 1],  # узел а
    [1, 0, 1, 0, 0, 0],  # узел б
    [0, 1, 0, 1, 0, 0],  # узел в
    [0, 0, 1, 0, 1, 0],  # узел г
    [0, 0, 0, 1, 0, 1],  # узел д
    [1, 0, 0, 0, 1, 0]   # узел е
]

labels = {0: "а", 1: "б", 2: "в", 3: "г", 4: "д", 5: "е"}

draw_graph(adj_matrix, labels)
Запуск этого примера отобразит граф, где узлы и их связи визуализированы в круговой диаграмме.

5. Инструкция по совместной работе (Contribution)
Если у вас есть идеи или предложения, пожалуйста, следуйте этим шагам:

1.Сделайте форк репозитория.
2.Клонируйте репозиторий на свой компьютер:

git clone https://github.com/MegaCraTex/Project_1
3.Создайте новую ветку для своей функции или исправления:

git checkout -b feature-name
4.Внесите изменения и добавьте их с помощью команды git add.
5.Закоммитьте изменения:

git commit -m "Добавлено: -----"
6.Отправьте изменения на GitHub:

git push origin feature-name
Откройте Pull Request (PR) и опишите свои изменения.
6. Информация об авторских правах и лицензировании
Вы можете использовать, копировать, изменять и распространять код.
Выполнил: Гродников Михаил. Группа: 22ИСП7.
