book={}
book['tom']={
    'name':'Jyoti',
    'address':'Odisha',
    'phone':8660175105
}
book['bob']={
    'name':'Jyoti',
    'address':'Odisha',
    'phone':8660175105
}
import json
s=json.dumps(book)
with open("book.txt","w")as f:
    f.write(s)