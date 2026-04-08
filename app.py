from flask import Flask, render_template, make_response, json
import os

port = int(os.environ.get("PORT", 10000))  
app = Flask(__name__, static_folder='public', static_url_path='/')
app.secret_key = os.environ.get("SECRET_KEY", "dev")  

# statically defined list of images (no os.listdir)
IMAGE_FILES = [
    "image1.png", "image2.png", "image3.png", "image4.png",
    "image5.png", "image6.png", "image7.png", "image8.png",
    "image9.png", "image10.png", "image11.png", "image12.png"
]

# helper function to wrap responses with edge caching headers
def cache_response(template_name, **context):
    response = make_response(render_template(template_name, **context))
    
    response.headers['Cache-Control'] = 'public, s-maxage=3600, stale-while-revalidate=86400'
    
    return response

@app.route("/")
def index():
    # load everything, let client handle the filtering
    with open("repos.json") as f:
        all_repos = json.load(f)

    all_tags = sorted({tag for repo in all_repos for tag in repo.get("tags", [])})

    return cache_response("index.html", repos=all_repos, all_tags=all_tags)

@app.route("/art")
def art():
    return cache_response('art.html', image_files=IMAGE_FILES)

@app.route("/contact")
def contact():
    return cache_response("contact.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)