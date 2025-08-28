from os import environ, path


class Config:

    DB_USER = environ.get("DB_USER")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_DATABASE = environ.get("DB_DATABASE")
    SECRET_KEY = environ.get("SECRET_KEY")


    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "assets")     #postgres_db
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_DATABASE}"

    FLASK_ADMIN_SWATCH="Flatly"