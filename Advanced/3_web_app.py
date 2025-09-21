from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'This is my home page'

def about():
    return 'This is my second page'


if __name__ == "__main__":
    app.run(debug=True)
    
# today on friday of june 2025 i bought my new egonomic office chair @6000 kenyan shillings # and it is very comfortable to use while working for long hours, hope 