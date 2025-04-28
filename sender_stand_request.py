
import configuration
import requests
import data



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.USERS_PATH,
                         json=body,
                         headers=data.headers)

def get_users():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_PATH, headers=data.headers)

