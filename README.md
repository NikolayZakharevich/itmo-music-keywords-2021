# Сервисы для работы с музыкой

## Сервис для предсказания эмоций

Находится в папке `emotions`

Настройки задаются в
файле [config.yml](https://github.com/NikolayZakharevich/music-keywords/blob/master/emotions/config.yml) `fonts/config.yml`
, по умолчанию разворачивается на порту `8080`, название метода — `music-emotions` (то есть сервис будет доступен по
адресу `0.0.0.0:8081/demo/music-emotions`):

```yaml
app:
  port: 8080
  host: "0.0.0.0"
  thread_pool: 5
  tmp_dir: "tmp/"
  method_name: "music-emotions"
```

Скрипт для развертки:

```sh
cd emotions
docker build -t "music-emotions:Dockerfile" .
docker run --publish 8081:8080 music-emotions:Dockerfile
```

## Сервис для предсказания шрифта

Находится в папке `fonts`

Настройки задаются в
файле [config.yml](https://github.com/NikolayZakharevich/music-keywords/blob/master/fonts/config.yml) `fonts/config.yml`
, по умолчанию разворачивается на порту `8080`, название метода — `music-fonts` (то есть сервис будет доступен по
адресу `0.0.0.0:8082/demo/music-fonts`):

```yaml
app:
  port: 8080
  host: "0.0.0.0"
  thread_pool: 5
  tmp_dir: "tmp/"
  method_name: "music-fonts"
```

Скрипт для развертки:

```sh
cd emotions
docker build -t "music-fonts:Dockerfile" .
docker run --publish 8082:8080 music-fonts:Dockerfile
```

## Сервис для предсказания ключевых слов

Находится в папке `keywords`

Настройки задаются в
файле [config.yml](https://github.com/NikolayZakharevich/music-keywords/blob/master/keywords/config.yml) `keywords/config.yml`
, по умолчанию разворачивается на порту `8080`, название метода — `music-keywords` (то есть сервис будет доступен по
адресу `0.0.0.0:8083/demo/music-keywords`):

```yaml
app:
  port: 8083
  host: "0.0.0.0"
  thread_pool: 5
  tmp_dir: "tmp/"
  method_name: "music-keywords"
```

Скрипт для развертки:

```sh
cd emotions
docker build -t "music-keywords:Dockerfile" .
docker run --publish 8083:8080 music-keywords:Dockerfile
```