import hashlib
import os

import instaloader
import requests
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST'])
def profile():
    username = request.form['username']
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    profile_pic_url = profile.profile_pic_url
    img_filename = None

    try:
        response = requests.get(profile_pic_url, stream=True)
        if response.status_code == 200:
            # Create an MD5 hash of the URL to use as the filename
            img_hash = hashlib.md5(profile_pic_url.encode('utf-8')).hexdigest()
            img_filename = f"{img_hash}.jpg"
            img_path = os.path.join('static/profile_pics', img_filename)
            
            with open(img_path, 'wb') as img_file:
                for chunk in response.iter_content(1024):
                    img_file.write(chunk)
    except requests.RequestException:
        img_filename = None

    profile_info = {
        "username": profile.username,
        "full_name": profile.full_name,
        "profile_pic_url": img_filename,
        "biography": profile.biography,
        "followers": profile.followers,
        "followees": profile.followees,
        "mediacount": profile.mediacount
    }

    return render_template('profile.html', profile=profile_info)

@app.route('/static/profile_pics/<filename>')
def profile_pic(filename):
    return send_from_directory('static/profile_pics', filename)

if __name__ == '__main__':
    os.makedirs('static/profile_pics', exist_ok=True)
    app.run(debug=True)
