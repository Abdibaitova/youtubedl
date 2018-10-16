from django.views.generic import TemplateView
import youtube_dl

class HomeView(TemplateView):
    template_name = 'index.html'

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': 'result.html',
    'noplaylist' : True,
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=NAPkvgefEgc'])