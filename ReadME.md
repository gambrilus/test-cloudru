# Тестовое задание для Cloud.ru

Внутри по папкам распределены этапы задания

## Playbook

В [main.yml](https://github.com/gambrilus/test-cloudru/blob/master/playbook/main.yml) описана сама джоба.
В папке inventory - файл [hosts.yml](https://github.com/gambrilus/test-cloudru/blob/master/playbook/inventory/hosts.yml) с данными о хостах.
В папке group_vars - файл [vars.yml](https://github.com/gambrilus/test-cloudru/blob/master/playbook/group_vars/vars.yml) с основными переменными. Возможно их стоило запихать в Ansible Vault.

## App

Здесь находится само [приложение](https://github.com/gambrilus/test-cloudru/blob/master/app/app.py) и [Dockerfile](https://github.com/gambrilus/test-cloudru/blob/master/app/Dockerfile), который его докеризует.

Приложение использует Flask. В файле [.flaskenv](https://github.com/gambrilus/test-cloudru/blob/master/app/.flaskenv) задано имя приложения, данные переменных окружения получаем через [settings.py](https://github.com/gambrilus/test-cloudru/blob/master/app/settings.py).

## Manifest

Собственно [манифест](https://github.com/gambrilus/test-cloudru/blob/master/manifest/app.yml) Kubernetes, который создает Namespace cloudru и деплоймент app с 3 репликами и пробами (liveness, readiness).

## Helm

Чарт, разворачивающий из шаблона [app.yml](https://github.com/gambrilus/test-cloudru/blob/master/helm/templates/app.yml) деплоймент с определенными в [values.yml](https://github.com/gambrilus/test-cloudru/blob/master/helm/values.yml) переменными.

-replicas - определяет значение ReplicaSet

-author - задает переменную окружения AUTHOR

-image_name - определяет имя докер-образа
