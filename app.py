from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app)


def save_order_to_db(order_data: dict):
    ...


def send_email(order_data: dict):
    ...


# APP Views
class API(Resource):
    def post(self):
        request_data = request.get_json()
        event = request_data.get("event")
        match event:
            case "new_order":
                if amount := request_data.get("total_amount"):
                    if amount > 50:
                        save_order_to_db(request_data)
                        send_email(request_data)

                        return {"success": "Order has been processed!"}, 200
                else:
                    return {"error": "Amount is missing in the request!"}, 406

            case "new_user":
                ...

        return {"hello": "world"}


# APP Routings/URL
api.add_resource(API, "/api")

# starting point
if __name__ == "__main__":
    app.run(debug=True)
