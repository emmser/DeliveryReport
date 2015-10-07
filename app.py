from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    samples = [{'sample_id': 'sample1'}, {'sample_id': 'sample2'}]
    return render_template('index.html', samples=samples)

@app.route("/report/<sample_id>")
def report(sample_id):
    samples = [{'sample_id': 'sample1'}, {'sample_id': 'sample2'}]
    return render_template('report.html', samples=samples)
    return "Emma " + sample_id

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
