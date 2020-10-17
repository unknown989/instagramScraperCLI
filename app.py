from flask import Flask,request

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html>
<head>
	<title>Moving List From Phone to PC</title>
</head>
<body>
	<form method='POST'>
		<textarea name="area"></textarea><br>
		<button type="submit">Go</button>
	</form>
</body>
</html>
"""

@app.route("/",methods=["GET","POST"])
def main():
	if request.method == "GET":
		return html
	elif request.method == "POST":
		print("REACHED HERE")
		postdata = request.form["area"]
		print(postdata)
		with open("list.txt","w") as f:
			f.write(postdata)
		return "Done"
	else:
		return 'Method not allowed'


app.run(host="192.168.1.5",port=8080,debug=True)