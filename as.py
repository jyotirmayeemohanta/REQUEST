import requests
import json
def reqe():
    x=requests.get("http://saral.navgurukul.org/api/courses")
    with open("meraki.json","w")as f:
        json.dump((x.json()),f,indent=4)
    b=x.json()
    c=0
    n=[]
    print("no.>>>>::<<<corscs>>>>::<<<<<id")
    for i in b["availableCourses"]:
        print(c,i["name"],i['id'])
        n.append(i["id"])
        c=c+1
    m=int(input("enter your seriyal num--->>"))
    r=requests.get("http://saral.navgurukul.org/api/courses/"+(n[m])+"/exercises")

    x=r.json()
    n1=[]
    c=0
    for i in x['data']:
        print(c,i['slug'])
        n1.append(i["slug"])    
        c+=1
    num=int(input("enter your slug num--->>"))
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(m)+"/exercise/getBySlug?slug="+n1[num])
    v1=req.json()
    print(req)
    print("content",v1["content"])


    print("do you want previous content than type up")
    print("do you want next content than type next")
    print("do you want previous content than type previous")
    print("do you want previous content than type exit")
    i=0
    for i in range(len(n1)):
        num1=input("enter your next step-->>")
        if num1=="up":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(m)+"/exercise/getBySlug?slug="+n1[num-1])
            v1=req.json()
            print(num-1,"content",v1["content"])
        if num1=="next":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(m)+"/exercise/getBySlug?slug="+n1[num+1])
            v1=req.json()
            print(num+1,"content",v1["content"])
        if num1=="previous":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(m)+"/exercise/getBySlug?slug="+n1[num])
            v1=req.json()
            print(num,"content",v1["content"])
        if num1=="exit":
            reqe()
reqe()