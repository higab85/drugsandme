from django.shortcuts import redirect
from django.utils import translation

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



def english():
    return redirect("/en")
