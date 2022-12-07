import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page

class Home(Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        main = jp.Div(a=container, classes="bg-gray-200 h-screen w-screen p-2")
        jp.Div(a=main, text='Instant Dictionary Web App', classes='text-3xl m-2 w-screen')
        jp.Div(a=main, text='''A web app that lets users type in 
        a term in a text box and returns the English definition
        of that term instantly as soon as the user has finished typing.
        The web app consists of a website with a navigation menu, a 
        Home, Dictionary, and About page.
                ''', classes='text-lg m-2')

        return wp






