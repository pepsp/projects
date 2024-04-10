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
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist"
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
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        title_exist = util.get_entry(title)
        if title_exist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "This entry already exists"})
        else:
            util.save_entry(title, content)
            entry_html = markdown.markdown(title)
            return redirect("wiki", title=title)
    return render(request, "encyclopedia/create.html")

def random_entry(request):
    random_entry = random.choice(util.list_entries())
    entry_html = markdown.markdown(util.get_entry(random_entry))
    return render(request, "encyclopedia/show_entry.html", {
            "entry": entry_html,
            "title": random_entry
        })


def edit(request):
    if request.method == "POST":
        title = request.POST["entry_title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
            })
    

def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("wiki", title=title)
