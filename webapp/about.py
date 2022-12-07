import justpy as jp

class About:
    path = '/about'
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main = jp.Div(a=wp, classes="bg-gray-200 h-screen w-screen")
        jp.Div(a=main, text='This is the about page', classes='text-3xl m-3 text-align-center w-screen')
        jp.Div(a=main, text='''Lorem ipsum dolor sit amet, consectetur adipiscing 
        elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
        occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
        anim id est laborum.
        ''', classes='text-lg m-2')
        return wp

jp.Route(About.path, About.serve)
jp.justpy()



