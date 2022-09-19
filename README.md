# Файл utils.py
Данная программа предназначена для внесения изменений в базу данных электронного дневника. В файле содержится три функции:  
1. Удаляет замечания от учителей
2. Меняет оценки 2 и 3 на 5
3. Случайным образов выбирает предмет, который проходит ученик в данном классе, случайным образом выбирает учителя из списка учителей, 
которые ведут данный предмет и публикует случайно выбранную фразу для похвалы ученика.  

## Как установить

1. Скачиваем файл `utils.py` и текстовый файл `commendations.txt` из репозитория
1. Помещаем их рядом с файлом `manage.py`
3. Переходим в папку проекта электронного дневника:  
```
$ cd project_folder
```
4. Запускаем виртуальное окружение:  
```
$ python manage.py shell
```
5. Прописываем в файле `manage.py` импорт `import utils`, сохраняем изменения:  
6. Запускаем функцию с ФИО ученика:  
```
$ function('Иванов Иван Иванович')
```
## Файл commendations.txt
В файле находится список фраз для похвалы от учителя. Можно добавить в него свои варианты с новой строки. Скрипт будет случайным образом выбирать фразы из данного файла.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

 

 
