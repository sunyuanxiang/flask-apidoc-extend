{% macro fields(fields_obj)-%}
    {%- for name,fields in fields_obj.items() -%}
###  **{{ name }}**
fields|optional|type|description
- | - | - | -
{% for field in fields -%}
{{field.field}}|{{field.optional}}|{{field.type}}|{{field.description}}
{%endfor%}
    {%-endfor -%}          
{%- endmacro %}


{% macro examples(example_obj) -%}
    {% for example in example_obj %}
### **{{ example.title }}**
```
{{ example.content }}
```
    {%- endfor %}
{%- endmacro %}


{% macro data_parse(grouper,data_obj)-%}
## **{{ grouper }}**
{% for data in data_obj -%}

## *{{grouper}} -- {{ data.title }}* 
version: {{data.version}}
{{data.description}}

### Methods: <code>{{ data.type|upper }}</code>  {% if data.permission%}permission: {{data.permission|map(attribute='name')|join(',') }} {%endif%}
```
 {{ data.url}}
```
{%if data.examples-%}
{{ examples(data.examples) }}
{%endif%}
{% for status in ['header','parameter','success','error'] -%}
{%if data[status]-%}
{%for field in ['fields','examples'] -%}
{{ {'examples':examples,'fields':fields}[field](data[status][field])}}
{%endfor%}
{%-endif%}
{%-endfor%}
{%- endfor %}
{%-endmacro%}