from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the form
html_template = """
   <!doctype html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Nincompoop Test</title>
   </head>
   <body>
       <h1>Are you a nincompoop? Take the test NOW!</h1>
       <form method="post" action="/result">
           <label>Are you a nincompoop? (y/n):</label><br>
           <input type="text" name="user_input"><br><br>
           <input type="submit" value="Submit">
       </form>
   </body>
   </html>
   """


# Route to display the test form
@app.route('/')
def index():
    return render_template_string(html_template)


# Route to handle form submission
@app.route('/result', methods=['POST'])
def result():
    user = request.form['user_input'].lower()

    if user == "y":
        response = "Calculating answer... you are a nincompoop!"
    elif user == "n":
        response = """Error code 4: Are you sure? 
            <form method='post' action='/confirm'>
                <input type='hidden' name='initial_input' value='n'>
                <input type='submit' name='confirmation' value='Yes' id='yes'>
                <input type='submit' name='confirmation' value='No' id='no'>
            </form>"""
        return response
    else:
        response = "Type y or n you nincompoop"

    return f"<h2>{response}</h2><br><a href='/'>Try Again</a>"


# Route to handle confirmation logic
@app.route('/confirm', methods=['POST'])
def confirm():
    confirmation = request.form['confirmation'].lower()

    if confirmation == "yes":
        response = "Alright then, if you insist... you are a nincompoop indeed!"
    elif confirmation == "no":
        response = "Exactly! Changing answer to 'y'... calculating... you are a nincompoop indeed!"
    else:
        response = "Dude, type yes or no. You nincompoop!"

    return f"<h2>{response}</h2><br><a href='/'>Try Again</a>"


if __name__ == "__main__":
    app.run(debug=True)
