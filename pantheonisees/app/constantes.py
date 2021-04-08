from warnings import warn

LIEUX_PAR_PAGE = 2
SECRET_KEY = "JE SUIS UN SECRET !"
API_ROUTE = "/api"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)


class _TEST:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    SQLALCHEMY_DATABASE_URI = "sqlite:///./db_test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    SQLALCHEMY_DATABASE_URI = "sqlite:///./db_pantheonises.db"
    SECRET_KEY = "JeSuisUnSecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG = {"test": _TEST, "production": _PRODUCTION}
