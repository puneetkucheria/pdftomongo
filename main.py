from flask import Flask, render_template, jsonify, request
from mongodb import search_text
from find_images import get_img

app = Flask(__name__)

@app.route('/')
def main():
    output = search_text('"about DMD"')
    return jsonify(output)

@app.route('/searchtext', methods=['GET','POST'])
def search_page():
    search = ""
    output = []
    img = get_img()
    if request.method == 'POST':
        search = request.form['search']
        output = search_text(search)
#        print(output)
    return render_template('search.html', search = search, output = output, img = img)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
