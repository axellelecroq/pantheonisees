from ..app import *
from . import user, pantheonisees

from werkzeug.utils import secure_filename

class Images(db.Model):
    __tablename__ = "Images"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pers_id = db.Column(db.Integer, db.ForeignKey("Pantheonises.id"))
    portrait_path = db.Column(db.Text)
    portrait_desc = db.Column(db.Text)
    date = db.Column(db.Text)
    tomb_path = db.Column(db.Text)

    def __init__(
        self,
        id,
        pers_id,
        portrait_path,
        portrait_desc,
        date,
        tomb_path,
    ):
        self.id = id
        self.pers_id = pers_id
        self.portrait_path = portrait_path
        self.portrait_desc = portrait_desc
        self.date = date
        self.tomb_path = tomb_path

    @staticmethod
    def upload_image(file):
        """
        Méthode permettant de télécharger un fichier
        dans le dossier prévu pour les images de l'application.
        :param file : file
        """
        try:
            file.save(os.path.join(img, secure_filename(file.filename)))
        except Exception as E:
            print(E)
            flash(
                "Une erreur est survenue lors de l'enregistrement de l'image.",
                category="error",
            )

    @staticmethod
    def add_data_images(id: int, infos: dict):
        """
        Méthode permettant d'ajouter les données concernant
        les images dans la base de données
        :param id : int
        :param infos : dict
        """
        p = Pantheonises.query.filter(Pantheonises.id == id).first()
        count = Images.query.filter(Images.id).count()

        if p.image_id:
            p.image_id.portrait_path = infos["p_path"]
            p.image_id.portrait_desc = infos["p_desc"]
            p.image_id.date = infos["p_date"]
            p.image_id.tomb_path = infos["t_path"]

            db.session.commit()

        else:
            img = Images(
                id=count + 1,
                pers_id=id,
                portrait_path=infos["p_path"],
                portrait_desc=infos["p_desc"],
                date=infos["p_date"],
                tomb_path=infos["t_path"],
            )

            try:
                db.session.add(img)
                db.session.commit()
                return True
            except Exception as E:
                print(E)
                return False


db.session.commit()
db.create_all()
