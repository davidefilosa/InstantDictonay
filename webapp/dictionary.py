import justpy as jp
from definition import Definition
from webapp.layout import DefaultLayout
from webapp.page import Page



class Dictionary(Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        main = jp.Div(a=container, classes="bg-gray-200 h-screen w-screen")
        jp.Div(a=main, text='Instant English Dictionary', classes='text-3xl m-3 w-screen')
        jp.Div(a=main, text='Get the definition of any English word as you type', classes='text-lg m-3')
        input_div = jp.Div(a=main, classes='grid grid-cols-2')
        output_div = jp.Div(a=main, text='Definition... ', classes='py-4 px-2 m-2')
        input_value = jp.Input(a=input_div, placeholder='Type any word...',
                 classes='bg-gray-100 m-2 border-2 border-gray-300 rounded w-64'
                         ' focus:outline-none focus:border-green-600 py-4 px-2 focus:bg-white', outputdiv=output_div)
        input_value.on('input', cls.get_definition)
        return wp
    @staticmethod
    def get_definition(widget, msg):
        term = widget.value
        definition = Definition(term).get()
        widget.outputdiv.text = " ".join(definition)
