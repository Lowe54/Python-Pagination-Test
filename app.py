from flask import Flask, redirect,render_template,request, url_for
import os
app = Flask(__name__)



@app.route('/')
@app.route('/search')
def search():
    resultnum = []
    pagecount = 0
    count = range(1,32)
    if len(count) < 10:
        for c in count:
            resultnum.append(c)
    else:
        #Determine the number of result pages
        pages = int(len(count) / 10)
        if pages == 0:
            pagecount = pages
            for c in count:
                resultnum.append(c)
        else:
            pagecount = pages + 1
            for c in count:
                resultnum.append(c)


       
    return render_template('search.html', results=resultnum, pc=pagecount, pages=pages, sr=0, nh=10)
@app.route('/search/')
def search_paginated():
    page = int(request.args.get('page'))
    sr = int(request.args.get('sr'))
    nh = 10
    resultnum = []
    currentpagenum = int(page)
    pagecount = 0
    count = range(1,32)
    if len(count) < 10:
        for c in count:
            resultnum.append(c)
    else:
        #Determine the number of result pages
        pages = int(len(count) / 10)
        if pages == 0:
            pagecount = pages
            
        else:
            pagecount = pages + 1
            
        #add the number of results to the result list

        for c, i in enumerate(count):
            print("I is {}".format(i))
            print(i <= sr)
            if i <= sr:
                resultnum.append(i)

       
    return render_template('search.html', results=resultnum, c_page=currentpagenum, pc=pagecount, pages=pages, sr=sr, nh=10)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)