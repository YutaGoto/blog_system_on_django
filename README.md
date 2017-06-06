# blog_system_on_django

Djangoでブログシステムを作ってみるの会

Yuta GotoがDjangoの練習のため、いろいろいじっているブログ投稿システムです。

## Setup

### Precondition

#### Docker, Docker Compose

Dockerをダウンロードしてインストールする。

<https://www.docker.com/>

### Git

Gitをダウンロードしてインストールする。Windowsの場合コマンドプロンプトで使えるようにインストールする。

<https://git-scm.com/>

## Git Clone

プロジェクトをクローンしてくる

```bash
$ git clone git@github.com:YutaGoto/blog_system_on_django.git
$ cd blog_system_on_django
```

### Docker Build

プロジェクトのセットアップと起動をする

```bash
$ docker-compose build
$ docker-compose run --rm web python manage.py migrate
$ docker-compose run --rm web python manage.py loaddata dump.json # Seedデータ
$ docker-compose up
```
