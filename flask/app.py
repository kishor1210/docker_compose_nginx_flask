from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store notes
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
    return redirect(url_for('index'))

@app.route('/note/<int:index>')
def view_note(index):
    if 0 <= index < len(notes):
        note = notes[index]
        return render_template('note.html', note=note, index=index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

