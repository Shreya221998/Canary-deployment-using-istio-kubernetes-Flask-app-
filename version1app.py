from flask import Flask
app= Flask(__name__)
@app.route('/', methods=["POST","GET"])
def test():
 print("from version1")
 return "from version1"
if __name__=='__main__':
 app.run(debug=True, host="0.0.0.0", port=8080)