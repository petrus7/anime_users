from flask import Blueprint
from flask.json import jsonify
from flask_restful import Api, Resource
from flask import request
from api import db
from api.api_exception import BadParamsException
from model.user_storage import UserStorage
from repository.mongo_user_repository import MongoDBUserRepository

user_api = Blueprint('user_api', __name__)

api = Api(user_api)



class GetUser(Resource):

    def get(self):
        query_params = dict(request.args)
        if len(query_params) == 0:
            raise BadParamsException(message="No username provided")
        elif 'username' not in query_params:
            raise BadParamsException(message="No username provided")
        repo = MongoDBUserRepository(db)
        return UserStorage(repo.get_users(request.args.getlist('username'))).get_json_obj()






# @user_api.errorhandler(DBException)
@user_api.errorhandler(BadParamsException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


api.add_resource(GetUser, '/get_user')
# api.add_resource(GetUsersById, '/get_anime_by_id')