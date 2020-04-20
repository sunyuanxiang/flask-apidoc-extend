
# Flask ApiDoc Extend
Flask ApiDoc Extend is a Flask extension which adds support for the ApiDoc.

## Features

- Host apidoc's files, by default they are hosted in http://localhost:5000/apidoc
- Export apidoc's files to Markdown. *apidoc.md* will be generated into output folder.Bydefault it's under ```/static/docs```.

## Installation
You need to install apidoc first.

```$ npm install apidoc -g```

Then you can install flask-apidoc via Python Package Index (PyPI)

```$ pip install flask-apidoc-extend```
## Usage
- Creates a apidoc.json file under your project.

*yourproject/apidoc.json*

like this:
```
{
  "name": "Flask REST API Doc",
  "version": "1.0.0",
  "description": "A Flask REST API Doc example",
  "title": "A Flask REST API Doc example",
  "url" : "http://localhost:5000"

}
```

- Initalizes Apidoc and pass your flask app to it.

ApiDoc param.
```
:param Input_path:   source dirname. Location of your project files.
:param output_path:  Output dirname. Location where to put to generated documentation.default is 'static/docs'
:param template_path:Use template for output files. You can create and use your own template.
:param app:          your flask instence         
:param mount:        register blueprint of the apidoc files to your flask application.then you can access 
:param url_path:     The url path for the apidoc files.default is 'apidoc'
:param private       Include private APIs in output.
```
example:
```
from flask_apidoc_extend import ApiDoc

app = Flask(__name__)
ApiDoc(app=app)
```
- Add some apidoc comments anywhere in your source code:
```
"""
@api {get} /user/:id Request User information
@apiName GetUser
@apiGroup User
     
@apiParam {Number} id User's unique ID.
     
@apiSuccess {String} firstname Firstname of the User.
@apiSuccess {String} lastname  Lastname of the User.
"""
```
- generate apidoc files

```$ cd yourproject/```

```$ flask apidoc``` 

 ```$ flask run```

 Now you can access your apidoc files by http://127.0.0.1:5000/apipdoc

- Export to Markdown (version>=0.1.6)

This command will export apidoc files to markdown(*apidoc.md*).

```$flask apidoc --export ```

Bydefault,you can find markdown file under ```/static/docs```.


**note** : your apidoc.json file must be set under *yourproject/* and you should run command at the same path.

## Feedback
apidocer@163.com
