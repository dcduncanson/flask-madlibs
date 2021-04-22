from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'derek'

debug = DebugToolbarExtension(app)


@app.route('/')
def get_answers():
    """Show Form to ask for words for the story."""

    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)


@app.route('/story')
def show_story():
    """Show the entire story"""

    text = story.generate(request.args)
    return render_template('story.html', text=text)
