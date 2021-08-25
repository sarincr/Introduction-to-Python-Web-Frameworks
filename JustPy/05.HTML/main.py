import justpy as jp

def html_comps():
    wp = jp.WebPage()
    jp.I(text='Text in Italic', a=wp)
    jp.Br(a=wp)
    jp.Strong(text='Text in the Strong element', a=wp)
    return wp

jp.justpy(html_comps)
