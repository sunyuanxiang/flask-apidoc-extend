from flask import Flask
from flask_apidoc_extend import ApiDoc

app = Flask(__name__)
ApiDoc(app=app, mount=True)

@app.route('/user/<id>',methods=['GET'])
def user(id):
    """
    @api {get} /user/<id> Read data of a User
    @apiVersion 1.0.0
    @apiName GetUser
    @apiGroup User
    @apiPermission admin
   
    @apiDescription get user's information
   
    @apiHeader {String} Authorization The token can be generated from your user profile.
    @apiHeaderExample {Header} Header-Example
        "Authorization: token 5f048fe"
    @apiParam {Number} id The Users-ID.
   
    @apiExample {curl} Curl example
    curl -H "Authorization: token 5f048fe" -i https://localhost:5000/user/1
    @apiExample {js} Javascript example
    const client = AcmeCorpApi('5f048fe');
    const user = client.getUser(42);
    @apiExample {python} Python example
    client = AcmeCorpApi.Client(token="5f048fe")
    user = client.get_user(42)
   
    @apiSuccess {Number}   id            The Users-ID.
    @apiSuccess {Date}     registered    Registration Date.
    @apiSuccess {Date}     name          Fullname of the User.
    @apiSuccess {String[]} nicknames     List of Users nicknames (Array of Strings).
    @apiSuccess {Object}   profile       Profile data (example for an Object)
    @apiSuccess {Number}   profile.age   Users age.
    @apiSuccess {String}   profile.image Avatar-Image.
    @apiSuccess {Object[]} options       List of Users options (Array of Objects).
    @apiSuccess {String}   options.name  Option Name.
    @apiSuccess {String}   options.value Option Value.
   
    @apiError NoAccessRight Only authenticated Admins can access the data.
    @apiError UserNotFound   The <code>id</code> of the User was not found.
    @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
   
    @apiErrorExample Response (example):
        HTTP/1.1 401 Not Authenticated
        {
          "error": "NoAccessRight"
        }
    """
    return id,200
if __name__ == "__main__":
     app.run()