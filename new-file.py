from flask import request

@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index2():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index3():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\