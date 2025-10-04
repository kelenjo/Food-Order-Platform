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

    column_list = ["id", "name", "price", "categories.name", "image", "description"]
    column_editable_list = ("name", "price", "description")
    column_filters = ["price", "name", "categories.name"]
    column_searchable_list = ["name", "description"]

    column_formatters = {
        "name": lambda v, c, m, n: m.name if len(m.name) < 24 else m.name[:24] + "...",
        "image": lambda v, c, m, n: Markup(f"""
            <a href='/static/assets/{m.image}' target='_blank'>
                <img src='/static/assets/{m.image}' width=80 style='border-radius:6px'/>
            </a>
        """) if m.image else ""
    }

    form_columns = ['name', 'description', 'price', "category_id", 'image']
    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename,
            "allow_overwrite": False
        }
    }
    form_ajax_refs = {
        'categories': {'fields': ['name']}
    }


class CategoryView(SecureModelView):
    create_modal = False
    edit_modal = False
    column_list = ["id", "name"]
    column_searchable_list = ["name"]
    column_editable_list = ["name"]
    column_formatters = {}  # no inherited formatters
    form_columns = ["name"] # only real column


class OfferView(SecureModelView):
    create_modal = True
    edit_modal = True

    column_list = ["id", "title", "description", "active", "image"]
    column_editable_list = ["title", "description", "active"]
    column_searchable_list = ["title", "description"]

    column_formatters = {
        "image": lambda v, c, m, n: Markup(f"""
            <a href='/static/assets/{m.image}' target='_blank'>
                <img src='/static/assets/{m.image}' width=80 style='border-radius:6px'/>
            </a>
        """) if m.image else ""
    }

    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename,
            "allow_overwrite": False
        }
    }
