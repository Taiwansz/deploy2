from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/')
def home():
    projects = [
        {'title': 'Projeto 1', 'description': 'Portfolio feito com HTML, CSS, FLASK', 'image': 'PORTCAPA.png'},
        {'title': 'Projeto 2', 'description': 'Portfolio feito com HTML, CSS, FLASK e Bootstrap.', 'image': 'img.png'},
        {'title': 'Projeto 3', 'description': 'Em breve.', 'image': 'CAUTION.png'},
    ]
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
