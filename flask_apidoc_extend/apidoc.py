# -*- coding: UTF-8 -*-
import subprocess
import sys

from flask import Blueprint, make_response, helpers, json
from werkzeug.exceptions import NotFound
import click

from .utils import apidoc_cmd as _apidoc, render_markdown, sort_app_data


class ApiDoc:
    """
    class ApiDoc adds command apidoc to Flask to generate the apidoc
    files.
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

         :param input_path:   source dirname. Location of your project
         files.
         :param output_path:  Output dirname. Location where to put to 
         generated documentation.default is 'static/docs'
         :param template_path:Use template for output files. You can
         create and use your own template.
         :param app:  your flask instence
         :param mount:  register blueprint of the apidoc files to your
         flask application.then you can access
         :param url_path: The url path for the apidoc files.default is
         'apidoc'
         :param private: Include private APIs in output.
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
        """
        if self.mount is True ,apidoc files folder will be under the
        same folder with your app,else it will be under your project
        root.
        """
        if self.mount:
            root_path = helpers.get_root_path(app.import_name)
            self.output_path = '/'.join([root_path, self.output_path])
            self.mount_to_app(app)
        self.register_command(app)

    def register_command(self, app):
        @app.cli.command(with_appcontext=False, help='generates apidoc files')
        @click.option('--export',
                      is_flag=True,
                      help='export to MarkDown files')
        def apidoc(export):
            apidoc_cmd = [_apidoc()]
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
            popen = subprocess.Popen(apidoc_cmd)
            popen.communicate()
            if export:
                result = self.__export2markdown()
                sys.stdout.write('Export success\n') \
                    if result else sys.stdout.write(
                    'No data can be exported\n')
            sys.stdout.write('apidoc files has been generated into {}'
                             .format(self.output_path))
            return popen.returncode

    def mount_to_app(self, app):
        """
         register apidoc url to flask app
        """

        if not self.url_path.startswith('/'):
            self.url_path = '/' + self.url_path
        # 不加static_url_path和url_prefix,就获取不到静态文件
        __apidoc_bp = Blueprint('apidoc',
                                app.import_name,
                                static_folder=self.output_path,
                                static_url_path='',
                                url_prefix=self.url_path)

        @__apidoc_bp.route('/')
        def __apidoc():
            try:
                rp = make_response(__apidoc_bp.send_static_file('index.html'))
            except NotFound:
                return '<h2>Maybe you should run \
                        \'$ flask apidoc\'  command first</h2>'
            return rp

        app.register_blueprint(__apidoc_bp)

    def __export2markdown(self):
        with open(self.output_path + '/api_data.json',
                  encoding='UTF-8') as file:
            data_obj = json.loads(file.read())
        if data_obj is not None:
            with open(self.output_path + '/api_project.json',
                      encoding='UTF-8') as file:
                project_obj = json.loads(file.read())
            data_obj = sort_app_data(data_obj, project_obj.get('order'))
            text = render_markdown(__name__,
                                   'templates',
                                   'template.md',
                                   project_obj=project_obj,
                                   data_obj=data_obj)
            with open(self.output_path + '/apidoc.md',
                      'w',
                      encoding='UTF-8') as file:
                file.write(text)
            return True
        return False
