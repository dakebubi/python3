from jinja2 import Template

template = Template('Hello {{ name }}!')
result = template.render(name='John Doe')
print(result)
