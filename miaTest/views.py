from django.shortcuts import render
from django.shortcuts import redirect


# 将请求定位到index.html文件中
def index(request):
    return render(request, 'index.html')


def echart(request):
    # x轴需要的信息
    listx = ["java", "嵌入式", "前端"]
    # y轴需要的信息
    listy = [300, 200, 100]

    return render(request, "echart.html", {"listx": listx, "listy": listy})


# 创建url对应的函数映射
def login(request):
    msg = ''
    # 判断是否是POST 返回
    if request.method == 'POST':
        # 接受 html name 是user和pwd的标签
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == '123' and pwd == '123':
            return redirect('https://www.baidu.com')
        else:
            msg = '用户名密码错'
            return render(request, 'login.html', {'msg': msg})

    # 去读index.html
    return render(request, 'index.html', {'msg': msg})
