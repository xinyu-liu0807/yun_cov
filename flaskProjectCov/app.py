import flask
from flask import Flask
from flask import render_template
from flask import jsonify
import utils
import time
import string
from jieba.analyse import extract_tags

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template("index.html")

# 获取当前系统时间
@app.route('/get_sys_time',methods=["get","post"])
def get_sys_time():
    dt = utils.get_sys_time()
    return dt
# 获取中间的
@app.route('/get_center1',methods=["get","post"])
def get_center1():
    # 获取数据库中想要的数据
    res = utils.get_center1()
    # 把数据转换成json字符串
    return jsonify({"confirm":str(res[0]),"suspect":str(res[1]),"heal":str(res[2]),"dead":str(res[3])})

# 获取中国地图
@app.route('/get_center2',methods=["get","post"])
def get_center2():
    datas = []
    res = utils.get_center2()
    for item in res:
        datas.append({"name":item[0],"value":str(item[1])})
    return jsonify({"data":datas})

# 获取左边第一个
@app.route('/get_left1',methods=["get","post"])
def get_left1():
    day,confirm,suspect,heal,deal = [], [], [], [], []
    res = utils.get_left1()
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        deal.append(tup[4])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"deal":deal})

# 获取左边第二个
@app.route('/get_left2',methods=["get","post"])
def get_left2():
    res = utils.get_left2()
    day,confirm,suspect = [],[],[]
    for item in res:
        day.append(item[0].strftime("%m-%d"))
        confirm.append(item[1])
        suspect.append(item[2])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect})


@app.route('/get_right1',methods=["get","post"])
def get_right1():
    res = utils.get_right1()
    city,confirm = [],[]
    for item in res:
        city.append(item[0])
        confirm.append(str(item[1]))
    return jsonify({"city":city,"confirm":confirm})

@app.route('/get_right2',methods=["get","post"])
def get_right2():
    res = utils.get_right2()
    content = []
    for item in res:
        str = item[0].rstrip(string.digits)
        num = item[0][len(str):]
        # 从字符串中提取关键字
        str = extract_tags(str)
        for data in str:
            if not data.isdigit():
                content.append({"name":data,"value":num})
    return jsonify({"data":content})



if __name__ == '__main__':
    app.run()
