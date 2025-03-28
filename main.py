from flask import Flask 
from flask import render_template 
from flask import request
from flask import redirect 
from flask import session
import pymysql

app = Flask(__name__,template_folder="templates",static_folder = 'static')
app.secret_key = 'your_secret_key' #1，启用session，不这么做，将无法使用session，最好要放在现在这个位置，保持全局启用。2，给session在客户端加密，避免在客服端可以直接看到session的原文，而在服务端可以用print（）打印出原文。


@app.route('/') 
def index_page():
    db=pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor=db.cursor(cursor=pymysql.cursors.DictCursor) #cursor=db.cursor()创建此次连接的游标，(cursor=pymysql.cursors.DictCursor)把游标执行命令得到的结果转化为字典
    sql="""select id,tittle,date from articles"""
    sql2= """select*from links"""

    cursor.execute(sql)
    db.commit()
    list=cursor.fetchall()

    cursor.execute(sql2)
    db.commit()
    listtwo=cursor.fetchall()

    cursor.close()
    db.close()
    print(list)
    print(listtwo)
    return render_template("/index.html",datalist=list, datalisttwo=listtwo)
    


@app.route('/articlesdetail/<int:number>') #该路由匹配‘/articlesdetail/任何数字’的url
def articlesdetail_page(number):
    db=pymysql.connect(host='localhost',
                     user='root',
                     password='lele87654321',
                     database='day1')
    cursor=db.cursor(cursor=pymysql.cursors.DictCursor)
    sql="""select*from articles where id=%s"""
    cursor.execute(sql,[number]) #这两行的语法规则：[number]就是‘articlesdetail/任何数字’中传入的数字参数，用来带入上一行sql中的%s
    db.commit()
    list=cursor.fetchall()
    cursor.close()
    db.close()
    print(list)
    return render_template("/textdetail.html",datalist=list)

@app.route('/login',methods=['GET','POST']) 
def login_page():
    if request.method =='GET':
        return render_template("/login.html") 

    mima=request.form.get("password") #通过前端input的name属性拿到前端给的数据。
    db=pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor) 
    sql= """select * from pwd"""
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()  #.fetchall()获取上一次命令的返回结果
    print(data)
    password=data[0]['password']
    print(password)
    cursor.close()
    db.close()
    if mima == password :
        session["id"]=mima #给客户端计算机创建一个session，名字叫做id，值为mima，存储在浏览器上，浏览器关闭后自动删除客户端本次回话的session。
        print(session["id"])
        return redirect('http://127.0.0.1:5000/edit')
    return '密码错误'

@app.route('/logout') 
def logout_page():
    del session["id"]
    return 'logout'

@app.route('/edit') 
def edit_page():
    if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
        
        return render_template("/edit.html")
    return redirect('http://127.0.0.1:5000/login')

@app.route('/edit-addarticle',methods=['GET','POST']) 
def editaddarticle_page():
    if request.method =='GET':
        if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
            return render_template("/edit-addarticle.html")
        return redirect('http://127.0.0.1:5000/login')
    
    tittle=request.form.get('tittle')
    text=request.form.get('text')
    date=request.form.get('date')
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor() 
    sql = """INSERT INTO articles(tittle,text,date) VALUES (%s, %s, %s)"""
    try:
        cursor.execute(sql,[tittle,text,date])
        db.commit()
    except:
        return '提交的数据录入数据库失败'
    else:
        return '提交的数据录入数据库成功'
   

    #这里必需使用try语句，因为经过本人测试在，如果没有try鱼块，前端提交的数据如果不符合数据库中数据表的数据格式要求，导致数据库中sql语句报错，进而导致后续代码无法运行。
    #可能是cursor.execute(sql,[tittle,text,date])和db.commit()其中一个报错吧，反正可以看着是“前端提交的数据如果不符合数据库中数据表的数据格式要求，这两个代码就会报错”
    #这样的话，直接删除原本本鱼块后面的代码，就可以利用except和else来判断前端提交的数据是否录入数据库成功，并且返回提示。

@app.route('/edit-addflink',methods=['GET','POST']) 
def editaddflink_page():
    if request.method =='GET':
        if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
            db=pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
            cursor=db.cursor(cursor=pymysql.cursors.DictCursor) #cursor=db.cursor()创建此次连接的游标，(cursor=pymysql.cursors.DictCursor)把游标执行命令得到的结果转化为字典
           
            sql2= """select*from links"""

          

            cursor.execute(sql2)
            db.commit()
            list=cursor.fetchall()

            cursor.close()
            db.close()
            print(list)
           
            
            
            return render_template("/edit-addflink.html",datalist=list)
        return redirect('http://127.0.0.1:5000/login')
    name=request.form.get('name')
    link=request.form.get('link')
    description=request.form.get('description')
    src=request.form.get('src')
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor() 
    sql = """INSERT INTO links(name,link,description,src) VALUES (%s, %s, %s, %s)"""
    try:
        cursor.execute(sql,[name,link,description,src])
        db.commit()
    except:
        return '提交的友链相关数据录入数据库失败'
    else:
        return '提交的友链相关数据录入数据库成功'

@app.route('/edit-delarticle',methods=['GET','POST']) 
def delarticle_page():
    if request.method =='GET':
        if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
            db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')

            cursor = db.cursor(cursor=pymysql.cursors.DictCursor) #创建此次连接的游标，并把游标执行命令得到的结果转化为字典

            sql = """ select tittle,date from articles;"""
            cursor.execute(sql)
            db.commit()
            list=cursor.fetchall()  #.fetchall()获取上一次命令的返回结果
            
           
            cursor.close()
            db.close()

            print(list)
            return render_template("/edit-delarticle.html",datalist=list)
        return redirect('http://127.0.0.1:5000/login')
    deltittle=request.form.get('deltittle')
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor() 
    sql = """ delete from articles where tittle = %s """
    cursor.execute(sql,[deltittle])
    db.commit()
    return '题目为：《'+ deltittle +'》的文章已经充数据库在删除。'

@app.route('/edit-delflink',methods=['GET','POST']) 
def delflink_page():
    if request.method =='GET':
        if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
            db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')

            cursor = db.cursor(cursor=pymysql.cursors.DictCursor) #创建此次连接的游标，并把游标执行命令得到的结果转化为字典

            sql = """ select name,link from links;"""
            cursor.execute(sql)
            db.commit()
            list=cursor.fetchall()  #.fetchall()获取上一次命令的返回结果
            cursor.close()
            db.close()

            print(list)
            return render_template("/edit-delflink.html",datalist=list)
        return redirect('http://127.0.0.1:5000/login')
    dellink=request.form.get('dellink')
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor() 
    sql = """ delete from links where link = %s """
    cursor.execute(sql,[dellink])
    db.commit()
    return '链接为：“ '+ dellink +' ”的友链已经充数据库在删除。'

@app.route('/edit-changepwd',methods=['GET','POST']) 
def changepwd_page():
    if request.method =='GET':
        if session["id"]:   #验证客户端计算机在该会话中是否有session或者说验证该回话的session是否为空，有的话才可以直觉通过url/edit访问，获取session的方法只有登陆成功
            return render_template("/edit-changepwd.html")
        return redirect('http://127.0.0.1:5000/login')
    pwd=request.form.get('pwd')
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='lele87654321',
                        database='day1')
    cursor = db.cursor() 
    sql = """ UPDATE pwd SET password = %s """
    try:
        cursor.execute(sql,[pwd])
        db.commit()
    except:  
        return '密码修改失败'  
    else:
        return '密码已更改，新的密码为：“ '+ pwd +' ” '

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5000)
