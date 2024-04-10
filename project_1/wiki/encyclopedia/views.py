from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util
import markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    entry = util.get_entry(title) 
    if entry:
         entry_html = markdown.markdown(entry)
         return render(request, "encyclopedia/show_entry.html", {
             "entry": entry_html,
            "title": title
        })
    
    else:
        # Si la entrada no existe, devolver un mensaje de error
        return render(request, "encyclopedia/error_notfound.html", {
            "title": title
            })

def search(request):
    if request.method == "GET":
        query = request.GET.get("q", "")
        entries = util.list_entries()
        check_query=None
        for entry in entries:
            if query.lower() == entry.lower():
                check_query = util.get_entry(entry)
                query=entry
                break
        if check_query:
            return redirect("wiki", title=query)
        else:
            matching_entries = [entry for entry in entries if query in entry.lower()]
            return render(request, "encyclopedia/search_results.html", {"entries": matching_entries, "query": query})
        

def create(request):
    return render(request, "encyclopedia/create.html")

def random_entry(request):
    random_entry = random.choice(util.list_entries())
    entry_html = markdown.markdown(util.get_entry(random_entry))
    return render(request, "encyclopedia/show_entry.html", {
            "entry": entry_html,
            "title": random_entry
        })



