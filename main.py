from flask import Flask, render_template, request
from werkzeug.utils import redirect

from config import Configuration
from game_of_life import GameOfLife

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        width, height = request.form.get('width'), request.form.get('height')
        width = int(width) if width else 25
        height = int(height) if height else 25

        GameOfLife(width, height)
        return redirect("/live", code=302)
    return render_template('index.html')


@app.route('/live')
def live():
    field = GameOfLife()
    if field.counter > 0:
        field.form_new_generation()
    field.counter += 1
    return render_template('live.html', field=field, live=field.counter)


if __name__ == '__main__':
    app.run()
