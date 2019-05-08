from flask import Flask, redirect,render_template,request, url_for
import os
app = Flask(__name__)



@app.route('/')
def search():
    resultnum = []
    pagecount = 0
    count = range(1,32)
    if len(count) < 10:
        for c in count:
            resultnum.append(c)
    else:
        #Determine the number of result pages
        pages = int(len(count) / 10);
        if pages == 0:
            pagecount = pages
            for c in count:
                resultnum.append(c)
        else:
            pagecount = pages + 1
            for c in count:
                resultnum.append(c)


       
    return render_template('search.html', results=resultnum, pc=pagecount, pages=pages)


if '__name__' == __name__:
    app.run(host=os.getenv("IP",'0.0.0.0'),port=int(os.getenv("PORT")), debug="True")