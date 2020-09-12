from flask import Flask,render_template,request

app = Flask(__name__)


html = """
<html>
<body>
<form method='post'>

<textarea type='text' name='content' placeholder='write names here...'></textarea>
<button type='submit'>Go</button>
</form>
</body>
</html>
"""



@app.route("/",methods=["GET"])
def main():
	return html

@app.route("/",methods=["POST"])
def postMain():
	content = request.form["content"]
	print(content)
	with open("list.txt","w") as f:
		f.write(str(content))
	return "DONE"

app.run(debug=True,port=8080,host="192.168.1.5")


