from django.shortcuts import render
from django.shortcuts import redirect
from miaTest.reptile import source_data as data


# 将请求定位到index.html文件中
def index(request):
    return render(request, 'index.html')


def show(request):
    # dict_keys = ['Python开发（接受实习）', 'Python开发讲师', 'python/java开发工程师', 'python大数据开发工程师', 'Python开发工程师', 'Python+Django开发工程师', 'Python后台Web开发工程师', 'Python开发工程师（外派）', 'Python开发工程师Web方向', 'Python中高级开发工程师', '高级Python开发工程师', '某银行大数据中心招聘Python开发工程师（外包）', 'python安全开发工程师', '软件开发工程师（js/Python）', '实习+Python开发工程师', '中级python开发工程师', 'Python开发/测试', 'Python开发实习生', 'Python高级开发工程师', 'Python开发工程师实习生/人工智能实习生', 'python开发工程师', 'Python软件开发工程师', 'Python开发工程师 (MJ000163)', 'python后台开发', 'Python/JS开发工程师', '虚拟化平台软件开发工程师', 'Java开发工程师', '大数据开发工程师', '前端高级开发', 'Linux 开发工程师']
    # dict_values = [1, 1, 1, 1, 20, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dict_keys = data.get_keys()
    dict_values = data.get_values()
    print(dict_keys)
    print(dict_values)
    # list_x = []
    # list_y = []
    # for i in range(len(dict_keys)):
    #     list_x.append(dict_keys[i])
    # for i in range(len(dict_values)):
    #     list_y.append(dict_values[i])
    # print(list_x)
    # print(list_y)
    return render(request, 'show.html', {"list_x": dict_keys, "list_y": dict_values})


def echart(request):
    # x轴需要的信息
    listx = ['java', '嵌入式', '前端', 'python']
    # y轴需要的信息
    listy = [300, 150, 100, 256]

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
