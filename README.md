# Counter-Flask-CodingDojo
### Python - Flask - Fundamentals
### Install packages
* ```pipenv install -r requirements.txt```
* ```pipenv shell```
* ```pipenv server.py```
### project structure flask
| routs                | Funtions        | return                        | methods |
|----------------------|-----------------|-------------------------------|---------|
| Localhost:5000/      | counter_get()   | render_template("index.html") | GET     |
| Localhost:5000/reset | counter_reset() | return redirect('/')          | GET     |
| Localhost:5000/two   | count_two()     | return redirect("/")          | GET     |
| Localhost:5000/add   | count_add()     | return redirect("/")          | POST    |
### Sessions
* "visit_count"        
* "count2" 
### Sessions decoded
![alt text](https://github.com/HenryCodeT/FileSizePOC/blob/main/decode_session.png?raw=true)
