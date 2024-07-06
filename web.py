from flask import Flask, request, jsonify
from .embed import Embed

app = Flask(__name__)

@app.route('/generate_embed', methods=['POST'])
def generate_embed():
    data = request.json
    title = data.get('title')
    description = data.get('description', '')
    colour = data.get('colour', '')
    url = data.get('url', '')
    author_name = data.get('author_name', '')
    author_icon_url = data.get('author_icon_url', '')
    thumbnail = data.get('thumbnail', '')
    hide_url = data.get('hide_url', False)

    embed = Embed(title, description, colour, url)
    if author_name:
        embed.set_author(author_name, author_icon_url)
    if thumbnail:
        embed.set_thumbnail(thumbnail)

    embed_url = embed.generate_url(hide_url=hide_url)
    return jsonify({"embed_url": embed_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
