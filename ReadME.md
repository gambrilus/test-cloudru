#Тестовое задание для Cloud.ru

Внутри по папкам распределены этапы задания

##Playbook

В main.yml описана сама джоба
В папке inventory - файл hosts.yml с данными о хостах
В папке group_vars - файл vars.yml с основными переменными. Возможно их стоило запихать в Ansible Vault

##App

Здесь находится само приложение и Dockerfile, который его докеризует

Приложение использует Flask. В файле .flaskenv задано имя приложения, данные переменных окружения получаем через settings.py

##Manifest

Собственно манифест Kubernetes, который создает Namespace cloudru и деплоймент app с 3 репликами и пробами (liveness, readiness)

##Helm

Чарт, разворачивающий из шаблона app.yml деплоймент с определенными в values.yml переменными
replicas - определяет значение ReplicaSet
author - задает переменную окружения AUTHOR
image_name - определяет имя докер-образа