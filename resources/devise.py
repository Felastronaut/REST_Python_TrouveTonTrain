from flask_restful import Resource

devise = [
  {
    "EUR":1,
    "USD":1.08,
    "CHF":1.05,
    "GBD":0.87,
  }
]

class Devise(Resource):
  def get(self, id):
    for devise in devises:
      if(id == devise["id"]):
        return devise, 200
    return "Item not found for the id: {}".format(id), 404

    def put(self, id):
      for devise in devises:
        if(id == devise["id"]):
          devise["item"] = request.form["data"]
          devise["status"] = "Open"
          return devise, 200
      return "Item not found for the id: {}".format(id), 404
