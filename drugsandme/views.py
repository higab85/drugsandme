from django.shortcuts import redirect, render
from django.utils import translation
from django.template.loader import get_template

default_language="en"

# def drugs(page, slug=None, language=default_language):
#     # TODO: this should redirect to a search of the slug
#     return redirect("/" + language + "/drugs/" + slug)

def cannabis(page):
    return redirect("/" + translation.get_language() + "/drugs/cannabis")

def cocaine(page):
    return redirect("/" + translation.get_language() + "/drugs/cocaine")

def ketamine(page):
    return redirect("/" + translation.get_language() + "/drugs/ketamine")

def lsd(page):
    return redirect("/" + translation.get_language() + "/drugs/lsd")

def mdma(page):
    return redirect("/" + translation.get_language() + "/drugs/mdma")

def modafinil(page):
    return redirect("/" + translation.get_language() + "/drugs/modafinil")

def alcohol(page):
    return redirect("/" + translation.get_language() + "/drugs/alcohol")



def english():
    return redirect("/en")


def error_404_view(request, exception):
    response = None
    if (exception.args[0] == "Not implemented yet!"):
      response = render(request, exception.args[1] + '-not_implemented-404.html')
    else:
      response = render(request,'404.html')
    response.status_code = 404
    return response

