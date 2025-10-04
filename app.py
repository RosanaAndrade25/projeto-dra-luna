from flask import Flask, render_template, jsonify
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(os.path.join(app.instance_path, 'questions.db'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    result = []
    for q in questions:
        options = conn.execute('SELECT * FROM options WHERE question_id = ?', (q['id'],)).fetchall()
        result.append({
            'id': q['id'],
            'text': q['text'],
            'image_url': q['image_url'],
            'options': [{'id': o['id'], 'text': o['text'], 'is_correct': o['is_correct'], 'feedback': o['feedback']} for o in options]
        })
    conn.close()
    return jsonify(result)

# Em app.py
if __name__ == '__main__':
    app.run(port=5001)