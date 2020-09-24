# author : Trenton Stiles
# name   : shopper.py
# desc   : POC of setting up e-commerce webapp tied to stripe for
#          card processing.


import json
import config
import os
import database
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


@app.route("/shop", methods=["GET", "POST"])
def shop():
    if request.method == "GET":
        pass


@app.route("/checkout")
def checkout():
    return "Hello"


@app.route("/admin")
def admin():
    # SECURITY NOTE : need to setup authentication to access this page
    products = database.get_products()
    return render_template("admin.html", products=products)


@app.route("/admin/product-upload", methods=["GET", "POST"])
def product_upload():
    if request.method == "POST":
        error_flag = False

        if "file" not in request.files:
            flash("file required for upload.")
            error_flag = True

        # get form data
        product_name = request.form["product_name"]
        try:
            product_price = float(request.form["product_price"])
        except ValueError:
            flash("price is not a real number.")
            error_flag = True

        if product_name == "":
            flash("must enter product name.")
            error_flag = True

        file = request.files["file"]

        # ensure file is not empty filename
        if file.filename == "":
            flash("file required for upload.")
            error_flag = True

        if error_flag:
            return redirect("/admin")

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        # add product to the database
        database.add_product(product_name, product_price, filename)
        flash("successfully added a product!")
    # SECURITY NOTE : need to setup authentication to access this page
    return redirect("/admin")


@app.route("/admin/delete/<int:product_id>", methods=["POST"])
def admin_delete(product_id):
    # removes the product from the listing
    product = database.get_product_by_id(product_id)
    product_imagename = product[3]
    abs_image_dir_path = os.path.join(os.getcwd(), "static/images")
    abs_image_path = os.path.join(abs_image_dir_path, product_imagename)

    os.remove(abs_image_path)
    database.delete_product(product_id)

    # TODO write function to also delate the image saved on server
    return redirect("/admin")


if __name__ == "__main__":
    app.config["UPLOAD_FOLDER"] = config.upload_folder
    app.config["SECRET_KEY"] = os.urandom(24)
    app.run(debug=True)
