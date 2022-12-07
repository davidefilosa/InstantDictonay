import justpy as jp

class Home:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main = jp.Div(a=wp, classes="bg-gray-200 h-screen w-screen")
        jp.Div(a=main, text='Instant Dictionary Web App', classes='text-3xl m-3 w-screen')
        jp.Div(a=main, text='''A web app that lets users type in 
        a term in a text box and returns the English definition
        of that term instantly as soon as the user has finished typing.
        The web app consists of a website with a navigation menu, a 
        Home, Dictionary, and About page.
                ''', classes='text-lg m-2')
        return wp


