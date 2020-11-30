[flaskチュートリアル](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html) を以下で構築したもの。

* docker
* Mysql
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

# 実行方法

## git clone

```
% git clone https://github.com/m5151128/flask-tutorial.git
```

## docker環境構築

```
% docker-compose up -d
```

## もろもろインストール

```
% docker-compose exec app pip install -r requirements.txt
```

## migration実行

```
# docker-compose exec app flask db init
# docker-compose exec app flask db upgrade
```

## flask環境実行

```
# docker-compose exec app export FLASK_APP=flaskr/manage.py
# docker-compose exec app export FLASK_ENV=development
# docker-compose exec app flask run --host=0.0.0.0
```

http://0.0.0.0:5000/ にアクセス
