from flask import Flask, render_template

app = Flask(__name__)

# def layout(template_name):
#     def decorator(view_func):
#         def wrapper(*args, **kwargs):
#             return render_template('layout.html', content=view_func(*args, **kwargs), template_name=template_name)
#         return wrapper
#     return decorator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
  