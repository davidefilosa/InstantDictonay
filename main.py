import inspect

import justpy as jp
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp.page import Page
import inspect


imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)


jp.justpy()
