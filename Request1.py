import requests
import json
def reqe():
    x=requests.get("http://saral.navgurukul.org/api/courses")
    with open("meraki.json","w") as f:
        json.dump(x.json(),f,indent=4)
        print(x)
    b=x.json()
    c=0
    n=[]
    print("no.>>>>::<<<corscs>>>::<<<<<id")
    for i in b["availableCourses"]:
        print(c,i["name"],i['id'])
        n.append(i["id"])
        c=c+1
    m=int(input("enter your Serial no"))
    r=requests.get("http://saral.navgurukul.org/api/courses/"+(n[m]+"/exercises"))
    x=r.json()
    n1=[]
    c=0
    for i in x['data']:
        print(c,i['slug'])
        n1.append(i["slug"])
        c+=1
    num=int(input("enter your slug num---->>"))
    req=requests.get("http://saral.navgurukul.org/api/courses"+str(m)+"/exercises/getBySlug?slug= ")
    print("Do you want next content then type next up")
    print("Do you want previous content then type previous")
    print("Do you want previous content then type exit")
    i=0
    for i in range(len(n1)):
        # print(i)
        num1=input("Enter your next step :--")
        if num1=="up":
            req=requests.get("http://saral.navgurukul.org/api/courses"+str(m)+"/exercise/getBySlug?slug = "+n1[num-1])
            v1=req.json()
            print(num-1,"content",v1["content"])
        if num1=="next":
            req=requests.get("http://saral.navgurukul.org/api/courses"+str(m)+"/exercise/getBy slug ? slug="+n1[num+1])
            v1=req.json()
            print(num+1,"conten",v1["content"])
        if num1=="previous":
            req=requests.get("http://saral.navgurukul.org/api/courses")
            v1=req.json()
            print(num,"content",v1["content"])
        if num1=="exit":
            reqe()
reqe()
