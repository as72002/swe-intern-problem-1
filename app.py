# Added for SafeDep Intern Assignment - Atharva

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "commands.db"

# Initialize DB
def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL
            );
        ''')

@app.route('/api/v1/commands', methods=['POST'])
def store_command():
    command = request.form.get("command")
    if not command or len(command.strip()) < 3:
        return jsonify({"error": "Command is missing or too short (at least need 3 chars)"}), 400

    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO commands (command) VALUES (?);", (command.strip(),))
    return jsonify({"status": "saved"}), 201

@app.route('/api/v1/commands', methods=['GET'])
def search_commands():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400

    with sqlite3.connect(DB) as conn:
        cur = conn.execute("SELECT command FROM commands WHERE command LIKE ?;", (f"%{keyword}%",))
        results = [row[0] for row in cur.fetchall()]
    return jsonify(results)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)

# adding comment to solve a problem
# adding comment to solve a problem
# adding comment to solve a problem
