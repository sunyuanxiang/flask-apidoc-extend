
# -*-code:utf-8-*-
import platform
import subprocess
import jinja2
from itertools import groupby


def apidoc_cmd():
    apidoc = 'apidoc'
    sys = platform.system()
    if sys == 'Windows':
        p = subprocess.Popen(['where', 'apidoc.cmd'],
                             shell=True,
                             stdout=subprocess.PIPE)
        stdout = p.communicate()[0]
        apidoc = stdout.decode('utf-8').split()[0]
    return apidoc


def render_markdown(name, template_folder, template_file, **data_obj):
    """
    :param name: your application package name
    :param template_folder: your template_folder
    :param template_file
    """
    env = jinja2.Environment(
        loader=jinja2.PackageLoader(name, template_folder))
    template = env.get_template(template_file)
    return template.render(data_obj)


def sort_app_data(data_obj, order: list = None):
    # remove apis that the @apiName you are not set
    start = 1
    data_obj = [data for data in data_obj if data.get('name')]
    data_obj.sort(key=lambda data: data.get('group'))
    priority_dict = {}
    if order:
        priority_dict = {value: key for key, value in enumerate(order, start)}
    p_max = len(priority_dict) + start + 1
    result_sort = sorted(
        data_obj,
        key=lambda e: priority_dict.get(e.get('name')) or p_max)
    data_obj = sorted(
        result_sort,
        key=lambda e: priority_dict.get(e.get('group')) or p_max)
    grouped_result = groupby(data_obj, key=lambda e: e['group'])
    return grouped_result
