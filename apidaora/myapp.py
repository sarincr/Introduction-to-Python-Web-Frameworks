from apidaora import appdaora, route


@route.get('/')
def hello_controller(name: str) -> str:
    return f'Hello  World!'


app = appdaora(hello_controller)
