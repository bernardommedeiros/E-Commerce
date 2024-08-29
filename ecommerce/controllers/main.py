from ecommerce import app

@app.route("/")
def index():
    return "Hello world!"

@app.route("/admin/", methods=['GET', 'POST'])
def test():
    return "oi"