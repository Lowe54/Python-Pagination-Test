from flask import Flask, redirect,render_template,request, url_for
import random
import os
app = Flask(__name__)



@app.route('/')
@app.route('/search/')
def search():
    if request.args.get('page') != "":
        page = int(request.args.get('page'))
        sr = int(request.args.get('sr'))
        currentpagenum = int(page)
    resultnum = ['Joseph Allen', 'Autumn Welch', 'Valerie Fields', 'Margaret Mccarty', 'Patricia Yu', 'Kelsey Burton', 'Charles Chandler', 'Michelle Washington', 'Wendy Morris', 'Sherri Perez', 'Holly Campbell', 'Karen Cisneros MD', 'Jessica Perry', 'Kimberly Miranda', 'Michael Lawrence']
    pagecount = 0

    if len(resultnum) < 11:
        for c in count:
            print("No need for extra pages here")
    else:
        #Determine the number of result pages
        pages = int(len(resultnum) / 11)
        if pages == 0:
            pagecount = pages
            
        else:
            pagecount = pages + 1
            
      
    return render_template('search.html', results=resultnum, c_page=currentpagenum, pc=pagecount, pages=pages, sr=sr, nh=10)

   
# @app.route('/search/')
# def search_paginated():
#     page = int(request.args.get('page'))
#     sr = int(request.args.get('sr'))
#     print("sr param is {}".format(sr))
#     nh = 10
    
#     currentpagenum = int(page)
#     pagecount = 0
   
#     if len(resultnum) < 10:
#         for c in count:
#             resultnum.append(c)
#     else:
#         #Determine the number of result pages
#         pages = int(len(count) / 10)
#         if pages == 0:
#             pagecount = pages
            
#         else:
#             pagecount = pages + 1
            
#         #add the number of results to the result list
        
#         for c in range(sr,sr+11):
#             print(c)
        

       
#     return render_template('search.html', results=resultnum, c_page=currentpagenum, pc=pagecount, pages=pages, sr=sr, nh=10)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)