## Описание проекта

Task Manager — это веб-приложение, где пользователи могут cоздавать, редактировать и удалять задачи. Управлять статусами задач. 

## Автор

Бондаренко Алексей Олегович
- Telegram: [@alovsemprivet](https://t.me/alovsemprivet)
- GitHub: [Pr1ority](https://github.com/Pr1ority)

## Технологический стек

- Backend: Django, Django REST Framework
- Database: PostgreSQL
- CI/CD: Jenkins
- Контейнеризация: Docker + docker-compose
- Автоматизация развертывания: Ansible
- Язык программирования: Python 3

## Как развернуть проект с помощью Ansible

1. Установите Ansible на локальную машину.
2. Создайте и настройте `inventory.ini` и `ansible_playbook.yml`, указав путь к проекту и нужные параметры:

**inventory.ini:**
```ini
[web]
localhost ansible_connection=local
```

**ansible_playbook.yml:**

```yaml
- hosts: web
  become: true
  tasks:
    - name: Установить Docker
      apt:
        name: docker.io
        state: present
        update_cache: yes
    - name: Установить docker-compose
      apt:
        name: docker-compose
        state: present
        update_cache: yes
    - name: Запустить контейнеры
      command: docker-compose up -d
      args:
        chdir: "/путь/к/проекту/task_manager"
```

3. Выполните команду для запуска Ansible Playbook:
```bash

ansible-playbook -i inventory.ini ansible_playbook.yml -K
```

## Как развернуть репозиторий на сервере

1. Клонируйте репозиторий
```bash
git clone https://github.com/Pr1ority/task_manager.git
```
2. Перейдите в корневую директорию
```bash
cd task_manager
```
3. Настройте виртуальное окружение
```bash
python -m venv venv
```
Для macOS/Linux
```bash
source venv/bin/activate
```
Для Windows
```bash
source venv/Scripts/activate
```
4. Заполните .env
Пример:
```example.env
SECRET_KEY=your_secret_key
```
5. Поднимите контейнеры в Докере
```bash
docker-compose up -d
```
6. Подготовьте базу данных
```bash
docker-compose exec task_manager python manage.py migrate
```
```bash
docker-compose exec task_manager python manage.py createsuperuser
```
8. Запустите сервер
```bash
docker-compose exec task_manager python manage.py runserver 0.0.0.0:8000
```
## Как развернуть репозиторий локально
1. Клонируйте репозиторий
```bash
git clone https://github.com/Pr1ority/task_manager.git
```
2. Перейдите в корневую директорию
```bash
cd task_manager
```
3. Настройте виртуальное окружение
```bash
python -m venv venv
```
Для macOS/Linux
```bash
source venv/bin/activate
```
Для Windows
```bash
source venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
4. Заполните .env
Пример:
```example.env
SECRET_KEY=your_secret_key
```
5. Подготовьте базу данных

```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
7. Запустите сервер
```bash
python manage.py runserver
```
