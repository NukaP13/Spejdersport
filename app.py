from flask import Flask, request, render_template, url_for, redirect
from os import listdir
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('spejdersport.html')

@app.route('/', methods=['POST'])
def index_post():  # put application's code here
    input_spejderk = "Dine informationer er:", "Navn:", request.form['name'], "Tlf.nummer:" ,request.form['number'],"Email:" ,request.form['email'], "Adresse:" ,request.form['address']
    if request.method == 'POST':
        with open('spejderk.txt', 'a') as f:
            f.writelines(str(input_spejderk))
            f.write("\n")
    return render_template('spejdersport.html', spejderk=input_spejderk)

#f = open("spejderk.txt", "r")
#print(f.readlines())
#print("Output of Read function is ")
if __name__ == '__main__':
    app.debug = True
    app.run()
