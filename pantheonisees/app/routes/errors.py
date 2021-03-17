from flask import render_template
from ..app import *

#  .errorhandler() pour retourner une page erreur,
#  si le code de la réponse HTTP renvoyé est 404 (Not Found) ou 500 (Internal Server Error)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("errors/500.html"), 500
