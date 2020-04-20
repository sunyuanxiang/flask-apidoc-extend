{% from 'parse.md' import data_parse%}
# {{project_obj.name|default('Your project name is undefined',True)}}
### **{{project_obj.description}}**
*version{{project_obj.version}}*

{% for group,list in data_obj-%}
{{ data_parse(group,list) }}
{%- endfor %}