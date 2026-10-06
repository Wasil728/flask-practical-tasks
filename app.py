from flask import Flask, redirect, url_prefix, url_for
from tasks.task2_shopping_cards.routes import task2_bp

app = Flask(__name__)
app.secret_key = 'flask-practical-tasks-secret-key'

# Register blueprint for task 2
app.register_blueprint(task2_bp, url_prefix='/task2')

@app.route('/')
def index():
    return redirect(url_for('task2.index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
