from django.shortcuts import render,HttpResponse
import getpass
import re
import subprocess as sp
from datetime import date, datetime
from tabulate import tabulate
import mysql.connector as c

m='''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <title>Python Webbrowser</title>
    </head>
    <style>
        .d2{
            position:relative;
            bottom:23px;
        }
    </style>
    <body>
    <div class="d1">
    <nav  class="navbar bg-dark" data-bs-theme="dark">
    
    <div class="container">
    <span style="color:white text-align:center">Content of the table is </span>
  </div>
</nav>
    <div class="d2">
    <table class="table" >
        %s
    </table>
    </div>
    </div>
    </body>
    </html>
    '''
con=c.connect(host='localhost',user='root',passwd='',db='incubator')
cur = con.cursor()
# Create your views here.
def index(request):
    return render(request,"index.html")
def inser_6(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        query = "insert into STARTUP_FOUNDERS(StartupID, Founder) values (%d, '%s')" % (int(t1),t2)
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e)   
def services(request):
    return HttpResponse("this is homepage")
def show(request):
    return render(request,"show.html")
def insert(request):
    return render(request,"insert.html")
def update(request):
    return render(request,"update.html")
def delete(request):
    return render(request,"delete.html")
def show1(request):
    query = "SELECT * FROM EMPLOYEE"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>EmployeeID</td><td>Name</td><td>Dept</td><td>Salary</td><td>Gender</td><td>ResourceId</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
        e = "<td>%s</td>"%row[4]
        p.append(e)
        f = "<td>%s</td>"%row[5]
        p.append(f)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show2(request):
    query = "SELECT * FROM RESOURCE"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>ResourceID</td><td>Resource Type</td><td>Resource Value</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show3(request):
    query = "SELECT * FROM INDUSTRY"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Industry ID</td><td>Industry Type</td><td>Industry name</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show4(request):
    query = "SELECT * FROM LOCATION"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Pincode</td><td>City</td><td>Country</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def sh4(request):
    return render(request,"sh4.html")
def show5(request):
    query = "SELECT * FROM INVESTOR"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Investor ID</td><td>DOB</td><td>Gender</td><td>First Name</td><td>Second Name</td><td>Location ID</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
        e = "<td>%s</td>"%row[4]
        p.append(e)
        f = "<td>%s</td>"%row[5]
        p.append(f)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show6(request):
    query = "SELECT * FROM STARTUP_FOUNDERS"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Startup ID</td><td>Founder</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show7(request):
    query = "SELECT * FROM INVESTS"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Industry ID</td><td>Investor ID</td><td>Startup ID</td><td>Resource ID</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show8(request):
    query = "SELECT * FROM DIRECTOR"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Name</td><td>Startup ID</td><td>Gender</td><td>Experience</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show9(request):
    query = "SELECT * FROM PROJECT"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Project Name</td><td>Startup ID</td><td>Timeframe</td><td>Start Date</td><td>NO of Employees</td></tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
        e = "<td>%s</td>"%row[4]
        p.append(e)
    contents = m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def show10(request):
    query = "SELECT * FROM STARTUP"
    cur.execute(query)
    rec2=cur.fetchall()
    p=[]
    tbl = "<tr><td>Startup ID</td><td>Startup Name</td><td>No of employees</td><td>Networth</td><td>Resource Id</td</tr>"
    p.append(tbl)
    for row in rec2:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td>"%row[3]
        p.append(d)
        e = "<td>%s</td>"%row[4]
        p.append(e)
    contents =m%(p)
    filename='templates/sh4.html'
    output = open(filename,"w")
    output.write(contents)
    return render(request,"show4.html")
def inser_16(request):
    return render(request,"inser_16.html")
def inser_15(request):
    return render(request,"inser_15.html")
def inser_14(request):
    return render(request,"inser_14.html")
def inser_13(request):
    return render(request,"inser_13.html")
def inser_12(request):
    return render(request,"inser_12.html")
def inser_11(request):
    return render(request,"inser_11.html")
def inser_10(request):
    return render(request,"inser_10.html")
def inser_5(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        t4=request.POST.get('t4')
        t5=request.POST.get('t5')
        query = "insert into PROJECT(ProjectName, StartupID, TimeFrame, StartDate, NoofEmployees) values  \
    ('%s', %d, %d, '%s', %d)" % (t1, int(t2), int(t3), t4,int(t5))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def inser_4(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        query = "insert into LOCATION(Pincode, City, Country) values(%d, '%s', '%s')" % (int(t1),t2, t3)
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def inser_3(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        query = "insert into RESOURCE(ResourceID, ResourceValue, ResourceType) values(%d, %d, '%s' )" % (
        int(t1), int(t2), t3)
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def inser_2(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        query = "insert into INDUSTRY(IndustryID,IndustryName,IndustryType) values(%d,'%s','%s')" % (
        int(t1),t2,t3)
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def inser_1(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        t4=request.POST.get('t4')
        t5=request.POST.get('t5')
        t6=request.POST.get('t6')
        query = "insert into EMPLOYEE(EmployeeID,EmployeeName,EmployeeDept,EmployeeSalary,EmployeeSex,ResourceID) values(%d,'%s','%s',%d,'%s',%d)" % (
        int(t1),t2,t3, int(t4), t5, int(t6))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def inser_0(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        t4=request.POST.get('t4')
        t5=request.POST.get('t5')
        t6=request.POST.get('t6')
        query = "insert into INVESTOR(InvestorId,DOB,Sex,FirstName,LastName,LocationId) values(%d,'%s','%s','%s','%s',%d)" % (
        int(t1), t2, t3, t4, t5, int(t6))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data inserted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def update_12(request):
    return render(request,"update_12.html")
def update_11(request):
    return render(request,"update_11.html")
def update_10(request):
    return render(request,"update_10.html") 
def update_0(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        t3=request.POST.get('t3')
        t4=request.POST.get('t4')
        t5=request.POST.get('t5')
        t6=request.POST.get('t6')
        query ="update INVESTOR set DOB ='%s',Sex='%s',FirstName='%s',LastName='%s',LocationId =%d where InvestorID=%d" % (
        t2, t3, t4, t5, int(t6),int(t1))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data updated successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def update_1(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        query = "UPDATE STARTUP set Networth=%d where StartupID=%d" % (
        int(t2), int(t1))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data updated successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def update_2(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        query = "UPDATE EMPLOYEE set EmployeeSalary=%d where EmployeeID=%d" % (
        int(t2), int(t1))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data updated successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 

def delete_12(request):
    return render(request,"delete_12.html")
def delete_11(request):
    return render(request,"delete_11.html")
def delete_10(request):
    return render(request,"delete_10.html") 


def delete_0(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        query = "DELETE FROM INVESTOR WHERE InvestorID=%d" % (int(t1))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data deleted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def delete_1(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        query = "DELETE FROM EMPLOYEE WHERE EmployeeID=%d"% (int(t1))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data deleted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 
def delete_2(request):
    if(request.method=="POST"):
        t1=request.POST.get('t1')
        t2=request.POST.get('t2')
        query = "DELETE FROM DIRECTOR WHERE StartupID=%d AND Name='%s'" % (
        int(t1), str(t2))
        try:
            cur.execute(query)
            con.commit()
            return HttpResponse("Data deleted successfully")
        except Exception as e:
            con.rollback()   
            return HttpResponse(e) 