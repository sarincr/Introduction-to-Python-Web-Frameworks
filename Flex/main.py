from flexx import flx

class Example(flx.Widget):
    def init(self):
        flx.Label(text='hello world')

app = flx.App(Example)
app.export('example.html', link=0)
app.launch('browser')   
flx.run()  
