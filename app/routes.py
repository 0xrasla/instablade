from flask import Blueprint, redirect, render_template, request, send_file, url_for
from .Insta import video_downloader, picture_download

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.htm', title='Home')

@routes.route('/download_video', methods=["GET","POST"])
def download_video():
    print(request.method)
    if(request.method == "POST"):
        url = request.form['url']
        response = video_downloader(url, "video")
        return send_file(response, as_attachment=True)
    return redirect(url_for("routes.index"))

@routes.route('/download_image', methods=["GET","POST"])
def download_image():
    print(request.method)
    if(request.method == "POST"):
        url = request.form['url']
        response = picture_download(url, "image")
        return send_file(response, as_attachment=True)
    return redirect(url_for("routes.index"))
