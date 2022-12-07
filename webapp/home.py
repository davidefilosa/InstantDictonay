import justpy as jp

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left', border=True)
        scrollarea = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scrollarea, classes='m-4')
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/home', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')
        container = jp.QPageContainer(a=layout)
        main = jp.Div(a=container, classes="bg-gray-200 h-screen w-screen p-2")
        jp.Div(a=main, text='Instant Dictionary Web App', classes='text-3xl m-2 w-screen')
        jp.Div(a=main, text='''A web app that lets users type in 
        a term in a text box and returns the English definition
        of that term instantly as soon as the user has finished typing.
        The web app consists of a website with a navigation menu, a 
        Home, Dictionary, and About page.
                ''', classes='text-lg m-2')

        return wp
    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True





