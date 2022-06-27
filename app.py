from src import create_app
# from flask_restful import Resource, Api

# app = create_app()
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/hello_world')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)