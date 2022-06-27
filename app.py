from src import create_app

app = create_app()

app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)