from flask import Blueprint, redirect, render_template, request, url_for
from .Insta import video_downloader, picture_download

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.htm', title='Home')

@routes.route('/download', methods=["GET","POST"])
def download():
    print(request.method)
    if(request.method == "POST"):
        url = request.form['url']
        response = video_downloader(url, "testvideo")
        print(response)
        return redirect(url_for('routes.index'))
    return redirect(url_for("routes.index"))

@routes.route('/download_pic', methods=["GET","POST"])
def download_pic():
    print(request.method)
    if(request.method == "POST"):
        url = request.form['url']
        response = picture_download(url, "testpic")
        print(response)
        return redirect(url_for('routes.index'))
    return redirect(url_for("routes.index"))

@routes.route('/about')
def about():
    return render_template('about.htm', title='About')
