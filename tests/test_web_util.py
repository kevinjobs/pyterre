from terre.web.util.render_static import render_static


def test_render():
    tpl = "<p>hello, {{ name }}!</p>"
    assert render_static(tpl, name="world") == '<p>hello, world!</p>'
