from flask_restful import Resource

devises = [
  {
    "id": 1,
    "EUR":1,
    "USD":1.08,
    "CHF":1.05,
    "GBD":0.87
  },
  {
    "id": 2,
    "USD":1.08
  },
  {
    "id": 3,
    "CHF":1.05
  },
  {
    "id": 4,
    "GBD":0.87
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
