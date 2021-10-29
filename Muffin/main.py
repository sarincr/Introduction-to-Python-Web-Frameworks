import muffin


app = muffin.Application()


@app.route('/', '/hello/{name}')
async def hello(request):
    name = request.path_params.get('name', 'world')
    return f'Hello {name.title()}!'

