[flaskチュートリアル](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html) を以下で構築したもの。

* docker
* Mysql
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

# 実行方法

```
$ docker-compose up -d
$ docker-compose exec app_flaskr flask db upgrade
```

http://localhost:5001 にアクセス

## mysql接続

```
$ docker-compose exec db_flaskr mysql -u root -proot flaskr
```
