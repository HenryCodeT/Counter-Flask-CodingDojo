from flask import Flask, redirect, render_template, request,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/',methods=['GET'])
def counter_get():
    if "visit_count" and "count2" not in session:
        session["visit_count"]=0
        session["count2"]=0
    else:
        session['visit_count'] += 1

    return render_template("index.html")

@app.route('/reset',methods=['GET'])
def counter_reset():
    session.clear()
    return redirect('/')

@app.route('/two',methods=['GET'])
def count_two():
    session['count2'] += 1
    print(request.cookies['session'])
    return redirect("/")

if __name__=="__main__":    
    app.run(debug=True)
