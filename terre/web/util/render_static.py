from jinja2 import Template


def render_static(tpl: str, **kw):
    template = Template(tpl)
    return template.render(**kw)
