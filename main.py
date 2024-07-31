import time
import streamlit as st
from PIL import Image
with st.spinner('Wait for it...'):
    
    my_bar = st.progress(0, text='')
    
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f'{percent_complete}%')
    time.sleep(0.0000000001)

st.balloons()

my_bar.empty()
magicEnabled = True
a,b,c,d = st.tabs(['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('abc.jpeg')
    st.write(':red[-----------------------------------------------------我推荐的网站-----------------------------------------------------]')
    st.link_button("python教程", "https://www.bilibili.com/video/BV1c4411e77t?p=1&vd_source=c012977f737febe696254cbbaee446d3")
    st.link_button("Github", "https://github.com/")
    
    
    st.write(':orange[-----------------------------------------------------我推荐的书-----------------------------------------------------]')
    st.link_button('玛蒂尔达','https://detail.tmall.com/item.htm?id=15165191262&ali_trackid=2:mm_24308344_3112850231_115732950017:1722075497_050_96845343&union_lens=lensId:TAPI@1722075497@212abcc5_1282_190f3b2c2e9_e5f4@01;recoveryid:050_451380364@1722075497867&ak=25016850&bxsign=tbk7wMKuQGP61wfNtLNrl7jBLU13CR0FGc_IAqrSgo3A-7CIeKkmS0tdcvSC9_0QyG5XsSrQGHmEyrKADOk9V_mVPqj1tcKDtXNFlhyITV-wotfl6JWW9nkX95x84822CEPkboGl883r_N3hBFwpImtuwnMr4UDoJb_w1Z7Npa5oBtvO496xmC3VeXdRKZ4GOnO')
    st.link_button('哈利波特系列','https://detail.tmall.com/item.htm?id=794004069338&spm=a21n57.sem.item.1.cb9f6000eRv7Ie&priceTId=214781d717220755814918600e7798&utparam=%7B%22aplus_abtest%22%3A%225ba20e3f5af0a81bf9e42e00bddcdfff%22%7D&&xxc=ad_ztc')
    st.write(':yellow[-----------------------------------------------------我推荐的游戏-----------------------------------------------------]')
    st.link_button('Stick with it!','https://www.9game.cn/xiazai/1216060/')
    code = '''
# 自制小游戏（其实是搜的）
print('Hi,欢迎进入大黄鸡的飞行空间！')
print('准备好出发冒险了吗？')
print('1、准备好了，继续！')
print('2、并没有，我要傲娇地再等等~')
start = input('请输入数字选项：')
while start != '1':
    start = input('现在准备好了吗？请输入数字选项：')
print('糟糕，大黄鸡的发动机坏了，你能帮它找一个新的发动机吗？')
print('1. 好，包在我身上！')
print('2. 不，我懒得找~')
start_1 = input('请输入数字选项：')
if (start_1 == '2') :
    print('懒惰是没有办法在冒险中生存下来的，很遗憾，你没有通过考验。')
elif (start_1 == '1') :
    print('据说在这两个地方找到发动机的几率比较大，你想去哪里找呢？。')
    print('1. 飞机工厂（这里应该会有发动机吧）。')
    print('2. 科学走廊。（感觉不会有发动机）')
    place = input('请输入数字选项：')
    if (place == '1') :
        print('你来到了飞机工厂...')
        print('发现这里竟然一片狼藉！你没有找到发动机~')
        print('1. 这是遭小偷了？算了，去科学走廊看看！')
        print('2. 什么破工厂，哪有什么发动机啊！骗人的吧！')
        place_1 = input('请输入数字选项：')
        if (place_1 == '1') :
            print('你来到了科学走廊...')
            print('发现飞电鼠正在科学走廊搞破坏！刚刚飞机工厂肯定也是它干的')
            print('1. 抓住飞电鼠再说。')
            print('2. 再大的事也不能阻挡我找发动机。')
            place_2 = input('请输入数字选项：')
            if (place_2 == '1') :
                print('成功抓住飞电鼠！还发现藏在它身上的发动机一枚。')
                print('任务完成！')
            elif (place_2 == '2') :
                print("一点正义感都没有，大黄鸡才不要带你去冒险呢！游戏结束！")
            else :
                print("随便行动是找不到发动机的...你在源码世界里迷路了...")
        elif (place_1 == '2') :
            print("鉴于你对游戏产生了质疑，不跟你玩啦~游戏结束，再见！")
        else :
            print("随便行动是找不到发动机的...你在源码世界里迷路了...")
    elif (place == '2') :
        print('糟糕！你发现飞电鼠正在破坏科学走廊！')
        print('1. 抓住飞电鼠再说。')
        print('2. 再大的事也不能阻挡我找发动机。')
        place_2 = input('请输入数字选项：')
        if (place_2 == '1') :
            print('恭喜你抓到飞电鼠，成功保护了科学走廊。')
            print('飞电鼠藏起了大黄鸡发动机，你找到了！恭喜你完成任务！')
        elif (place_2 == '2') :
            print("一点正义感都没有，大黄鸡才不要带你去冒险呢！游戏结束！")
        else :
            print("随便行动是找不到发动机的...你在源码世界里迷路了...")
    else :
        print("看来你和发动机没有缘分啊，游戏结束")
else :
    print("随便行动是找不到发动机的...你在源码世界里迷路了...")
'''
    st.code(code, language="python")
def page_2():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4= st.tabs(['原色','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
def page_3():
    '''我的智能词典'''
    st.write('智慧词典')

    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for l in words_list:
        words_dict[l[1]] = [int(l[0]),l[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    
    
    
        
    
    word = st.text_input('word')
    if word:
        st.chat_message("user").write(word)
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        
        try:
            word_ = words_dict[word][1]
            st.chat_message("assistant").write(f" {word_}")
            if word == 'python':
                st.chat_message("assistant").write(f"我就是用python做的！")
                st.chat_message("assistant").code('print("我就是用python做的！")',language="python")
                st.balloons()
            if word == 'brithday':
                st.chat_message("assistant").write("祝你生日快乐！")
                st.balloons()
            if word == 'snow':
                st.chat_message("assistant").write("下雪了！")
                st.snow()
                
        except:
            st.chat_message("assistant").write("Error")
    
        
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    
    name = st.selectbox('我是……', ['阿短','编程猫','梁壹'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    messages_list.reverse()
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '梁壹':
            with st.chat_message('哈'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
            
    return img
with a:
    page_1()
with b:
    page_2()
with c:
    page_3()
with d:
    page_4()
    