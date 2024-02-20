from flask import Flask, redirect, render_template, request
from Main import reachbox

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/CreateUser', methods=["POST", 'GET'])  # Corrected 'method' to 'methods'
def CreateUser():
    if request.method == "POST":
        username = request.form.get('Username')
        gmail = request.form.get('Gmail')
        interest = request.form.getlist('SelectTech')  # Corrected to get a list of selected values
        # creating user
        create_user = reachbox().create_user(gmail, username, interest)
        if create_user:
            print(f'created user related details are: {create_user}')
            return render_template('Home.html')
        else:
            print('not been able to create user')


# endpoint for creating the post
@app.route('/CreatePost', methods=["GET", "POST"])
def CreatePost():
    # define the post methof request
    if request.method == 'POST':
        # get data from the form
        Gmail = request.form.get('Gmail')
        Heading = request.form.get('Heading')
        Description = request.form.get('Description')
        tech_involved = request.form.getlist('SelectTech')
        create_post = reachbox().create_post(Gmail, Heading, Description, tech_involved)
        if create_post:
            return redirect('/')
        else:
            print('post is not created')
    return render_template('CreatePost.html')

if __name__ == '__main__':
    app.run(debug=True)
