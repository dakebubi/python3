from jinja2 import Template


class Jinja2Test(object):

    def do_render(self):
        template = Template('Hello {{ name }}!')
        result = template.render(name='John Doe')
        print(result)


test = Jinja2Test()
test.do_render()
