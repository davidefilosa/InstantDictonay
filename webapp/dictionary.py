import justpy as jp

class Dictionary:
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main = jp.Div(a=wp, classes="bg-gray-200 h-screen w-screen")
        jp.Div(a=main, text='Instant English Dictionary', classes='text-3xl m-3 w-screen')
        jp.Div(a=main, text='Get the definition of any English word as you type', classes='text-lg m-3')
        jp.Input(a=main, placeholder='Type any word...',
                 classes='bg-gray-100 m-2 border-2 border-gray-300 rounded w-48'
                         ' focus:outline-none focus:border-green-600 py-4 px-2 focus:bg-white')
        jp.Div(a=main, text='Definition... ', classes='py-4 px-2 m-2')
        return wp
