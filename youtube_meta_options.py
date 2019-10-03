from __future__ import unicode_literals
import youtube_dl
url=input('enter a valid url')
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(url, download=True) 
print 'upload date : %s' %(meta['upload_date'])
print 'uploader    : %s' %(meta['uploader'])
print 'views       : %d' %(meta['view_count'])
print 'likes       : %s' %(meta['like_count'])
print 'dislikes    : %s' %(meta['dislike_count'])
print 'id          : %s' %(meta['id'])
print 'format      : %s' %(meta['format'])
print 'duration    : %s' %(meta['duration'])
print 'title       : %s' %(meta['title'])
print 'description : %s' %(meta['description'])
