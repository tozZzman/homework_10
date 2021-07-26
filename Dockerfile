FROM ubuntu:20.04

# переменные окружения через которые можно передать ключи для запуска тестов
ENV BROWSER='chrome'
ENV URL='https://demo.opencart.com/'
ENV EXECUTOR='192.168.31.145'
ENV BROWSER_VER='92'
ENV VNC='--vnc'
ENV VIDEO=''
# переменная для выбора тестов, которые следует запустить (например: -e "TEST=-k test_currency")
ENV TEST=''

# создание директория для тестов
RUN mkdir tests_opencart

# смена рабочего директория
WORKDIR /tests_opencart

# копирование файла окружения с хоста
COPY requirements.txt .

# установка всех необходимых зависимостей
RUN apt update && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install python3.8 -y && \
    apt install pip -y && \
    pip install -r requirements.txt

# копирование всех тестов с хоста
COPY . .

# смена рабочего директория
WORKDIR /tests_opencart/tests

# запуск тестов в зависимости от установок в переменных окружения
CMD pytest -v --tb=short --url=${URL} --browser=${BROWSER} --bversion=${BROWSER_VER} --executor=${EXECUTOR} ${VNC} ${VIDEO} ${TEST}