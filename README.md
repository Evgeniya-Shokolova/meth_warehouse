# Проект meth_warehouse

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## "Meth_Warehouse" - это приложение для работы со складом рулонов металла.

Рулон: id, длина, вес, дата добавления, дата удаления.

Обязательные пункты:
- добавление нового рулона на склад. Длина и вес — обязательные
параметры. В случае успеха возвращает добавленный рулон;
- удаление рулона с указанным id со склада. В случае успеха возвращает
удалённый рулон;
- получение списка рулонов со склада. Рассмотреть возможность
фильтрации по одному из диапазонов единовременно (id/веса/длины/даты
добавления/даты удаления со склада);
- получение статистики по рулонам за определённый период:
- количество добавленных рулонов;
- количество удалённых рулонов;
- средняя длина, вес рулонов, находившихся на складе в этот период;
- максимальная и минимальная длина и вес рулонов, находившихся на
складе в этот период;
- суммарный вес рулонов на складе за период;
- максимальный и минимальный промежуток между добавлением и
удалением рулона.# meth_warehouse


## Установка и запуск проекта

### Выполняем клонирование

```bash
git clone git@github.com:Evgeniya-Shokolova/meth_warehouse.git
```
Переходим в папку с проектом
```bash
cd meth_warehous
```
Создать виртуальное окружение для Windows: -
```bash
python -m venv venv
```
Команда для Linux и macOS: - 
```bash
python3 -m venv venv
```
Активировать виртуальное окружение для Windows: -
```bash
source venv/Scripts/activate
```
Для Linux и macOS: -
```bash
source venv/bin/activate
```
Обновить пакетный менеджер для Windows: -
```bash
python -m pip install --upgrade pip
```
Для Linux и macOS: -
```bash
python3 -m pip install --upgrade pip
```
Создать файл requirements.txt для управления зависимостями:
```bash
pip freeze > requirements.txt
```
Установить модули из файла requirementst.txt:`
```bash
pip install -r requirements.txt
```
Запустить приложение:
```bash
uvicorn main:app --reload
```

### Установка Docker

Скачиваем установочный файл Docker Desktop. Будет установлена программа для управления контейнерами (докер-демон) и докер-клиенты — графический интерфейс и интерфейс командной строки. 
Дополнительно к Docker устанавливаем утилиту Docker Compose:
```bash
sudo apt install docker-compose-plugin
```
Проверяем, что Docker работает:
```bash
sudo systemctl status docker
```

### Упаковка проекта в Docker-образ

Docker должен быть запущен. Открываем терминал, переходим в соответсвующую директорию backend/, frontend/, nginx/ проекта Meth_Warehouse и выполняем сборку образа:
```bash
docker build -t rools . 
```
Выполняем команду аутентификации:
```bash
docker login
```
Пушим образы на Docker Hub:
```bash
docker push username/rolls:latest
```

### Загрузка образов на Docker Hub
Собираем образы:
```bash
docker build -t username/rolls:latest
```

## Сохраняем, коммитим и пушим изменения на GitHub
```bash
git add .
```
```bash
git commit -m "Comment"
```
```bash
git push
```

### Автор:
[Евгения Шоколова](https://github.com/Evgeniya-Shokolova)
