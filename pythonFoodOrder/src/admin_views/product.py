from src.admin_views.base import SecureModelView
from src.config import Config

from flask_admin.form import ImageUploadField
from os import path
from uuid import uuid4
from markupsafe import Markup


def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"


class ProductView(SecureModelView):
    create_modal = True
    edit_modal = True

    column_editable_list = ("name", "price", "description")
    column_filters = ["price",]

    column_formatters = {
        "name": lambda v,c,m,n: m.name if len(m.name) < 24 else m.name[0:24] + "...",
        "image": lambda v,c,m,n: Markup(f"<img src='/static/assets/{m.image}' width=64/>")
    }

    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }