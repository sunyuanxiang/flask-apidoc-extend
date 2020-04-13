import subprocess

from flask import Blueprint, make_response
from werkzeug.exceptions import NotFound
import click
import warnings

class ApiDoc:
    """
    class ApiDoc adds command apidoc to Flask to generate the apidoc files.
    """

    def __init__(self, 
                 input_path=None, 
                 output_path=None, 
                 template_path=None, 
                 app=None, 
                 mount=True, 
                 url_path=None,
                 private=False):
        """
        Initializes a new instance of ApiDoc.

         :param Input_path:   source dirname. Location of your project files.
         :param output_path:  Output dirname. Location where to put to generated documentation.default is 'static/docs'
         :param template_path:Use template for output files. You can create and use your own template.
         :param app:          your flask instence         
         :param mount:        register blueprint of the apidoc files to your flask application.then you can access 
         :param url_path:     The url path for the apidoc files.default is 'apidoc'
         :param private       Include private APIs in output.
        """
        self.input_path = input_path 
        self.output_path = output_path or 'static/docs'
        self.template_path = template_path
        self.mount = mount
        self.url_path = url_path or 'apidoc'
        self.private = private
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.register_command(app)
        if self.mount:       
            self.mount_to_app(app)  
                 

    def register_command(self, app):
        @app.cli.command(with_appcontext=False)    
        def apidoc():
            apidoc_cmd = ['apidoc']     
            if self.input_path:
                apidoc_cmd.append('-i')
                apidoc_cmd.append(self.input_path)
         
            if self.output_path:
                apidoc_cmd.append('-o')
                apidoc_cmd.append(self.output_path)
         
            if self.template_path:
                apidoc_cmd.append('-t')
                apidoc_cmd.append(self.template_path)
            if self.private:
                apidoc_cmd.append('-p')
                apidoc_cmd.append(self.private)   
            popen = subprocess.Popen(apidoc_cmd, shell=True)
            popen.communicate()
            return popen.returncode


    def mount_to_app(self,app):

        """
         register apidoc url to flask app
        """

        if not self.url_path.startswith('/'):
            self.url_path = '/'+self.url_path
        __apidoc_bp = Blueprint('apidoc',
                                 app.import_name,
                                 static_folder=self.output_path ,
                                 static_url_path='', 
                                 url_prefix=self.url_path)# 不加static_url_path和url_prefix,就获取不到静态文件，不明所以.

        @__apidoc_bp.route('/')
        def __apidoc():  
            try:         
                rp = make_response(__apidoc_bp.send_static_file('index.html'))
            except NotFound:
                return 'Maybe you should run \'flask apidoc\' command first'
            return rp
        app.register_blueprint(__apidoc_bp)
    


