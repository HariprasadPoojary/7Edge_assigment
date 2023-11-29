from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app)


def save_order_to_db(order_data: dict):
    ...


def send_email(order_data: dict):
    ...


def save_user_to_db(user_data: dict):
    ...


def update_order_in_db(order_data: dict):
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

                return {"error": "Amount is missing in the request!"}, 406

            case "new_user":
                if user_type := request_data.get("user_type"):
                    if user_type == "premium":
                        save_user_to_db(request_data)

                        return {"success": "User has been processed!"}, 200
                elif condition := request_data.get("conditions"):
                    if user_type := condition.get("user_type"):
                        if user_type == "premium":
                            jobs_to_execute = request_data.get("jobs")
                            for job in jobs_to_execute:
                                if "Database" in job:
                                    save_user_to_db(request_data)
                                if "Email" in job:
                                    send_email(request_data)

                        return {"success": "User has been processed!"}, 200

                return {"error": "user_type is missing in the request!"}, 406

            case "order_shipped":
                send_email(request_data)

                return {
                    "success": f"Order info sent to the User to email: {request_data['customer_email']}"
                }, 200

            case "order_delivered":
                if status := request_data.get("status"):
                    if status == "delivered":
                        update_order_in_db(request_data)

                return {"error": "status is missing in the request!"}, 406

        return {"hello": "world"}


# APP Routings/URL
api.add_resource(API, "/api")

# starting point
if __name__ == "__main__":
    app.run(debug=True)
