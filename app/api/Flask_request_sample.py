from flask import Flask
from flask_restful import Api, Resource, reqparse
from app.loggingHelper import getLogger

logger = getLogger('test')

parser = reqparse.RequestParser(trim=True)
parser.add_argument('name', location=['json', 'args'])
# parser.add_argument('post_data', location=['json', 'args'], type=list)
parser.add_argument('post_data', type=dict, location=['json', 'args'])

parser2 = reqparse.RequestParser()
parser2.add_argument('age', location=['json', 'args'])

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        args = parser.parse_args()
        args2 = parser2.parse_args()
        logger.info('wellcome to the helloworld get method')
        print  args['post_data']
        return {'name': args['name'], 'age': args2['age'], 'post_data': args['post_data']}

    def post(self):
        args = parser.parse_args()
        print  args['post_data']['age']
        return {'post_data': args['post_data']}


api.add_resource(HelloWorld, '/p')

if __name__ == '__main__':
    app.run(debug=True)
