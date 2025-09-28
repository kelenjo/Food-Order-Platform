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

    column_list = ["name", "price", "categories.name", "image", "description"]
    column_editable_list = ("name", "price", "description")
    column_filters = ["price", "name", "categories.name"]

    column_formatters = {
        "name": lambda v, c, m, n: m.name if len(m.name) < 24 else m.name[:24] + "...",
        "image": lambda v, c, m, n: Markup(f"""
            <a href='/static/assets/{m.image}' target='_blank'>
                <img src='/static/assets/{m.image}' width=80 style='border-radius:6px'/>
            </a>
        """)
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
    create_modal = True
    edit_modal = True
    column_list = ["name"]
    column_searchable_list = ["name"]
    column_editable_list = ["name"]


class OfferView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_list = ["title", "description", "active", "image"]
    column_editable_list = ["title", "description", "active"]
    column_formatters = {
        "image": lambda v,c,m,n: Markup(f"""
            <a href='/static/assets/{m.image}' target='_blank'>
                <img src='/static/assets/{m.image}' width=80 style='border-radius:6px'/>
            </a>
        """)
    }
    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename,
            "allow_overwrite": False
        }
    }


class CartView(SecureModelView):
    column_list = ["user_id", "product_id", "quantity"]
    column_filters = ["user_id", "product_id"]
    form_columns = ["user_id", "product_id", "quantity"]
