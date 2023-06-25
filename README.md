[flaskチュートリアル](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html) を以下で構築したもの。

* docker
* Mysql
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

# 実行方法

## git clone

```
$ git clone https://github.com/m5151128/flask-tutorial.git
```

## docker環境構築

```
$ docker-compose up -d
```

## セットアップ

```
$ docker-compose exec app_flaskr bash
$ pip install -r requirements.txt
$ python manage.py db upgrade
$ export FLASK_APP=manage.py
$ export FLASK_ENV=development
$ flask run --host=0.0.0.0
```

http://localhost:5001 にアクセス


## mysql接続

```
$ docker-compose exec db_flaskr mysql -u root -proot flaskr
```
