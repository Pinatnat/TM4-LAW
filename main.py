from flask import Flask, request, jsonify

class Profile :
    def __init__(self,nama,npm) :
        self.nama = nama
        self.npm = npm
    
    def get_nama(self):
        return self.nama

mine = Profile("Nadya Aprillia", "1906398566")

dict_prof = {"1906398566":mine}

app = Flask(__name__)
@app.route("/")
def home():
    return "Nginx"

@app.route("/update")
def update():
    data = request.get_json()
    dict_prof.clear()
    dict_prof[data["npm"]]= Profile(data["nama"],data["npm"])
    return jsonify({"status": "OK"})


@app.route("/read/<npm>")
def read(npm):
    response = "None"
    if (dict_prof[npm]!=None):
        response = {
            "status": "OK",
            "npm": npm,
            "name" : dict_prof[npm].get_nama() 
        }
    return jsonify(response)

@app.route("/read/<npm>/<int:trans>")
def read_cache(npm,trans):
    print(trans)
    response = "None"
    if (dict_prof[npm]!=None):
        response = {
            "status": "OK",
            "npm": npm,
            "name" : dict_prof[npm].get_nama() 
        }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8566)