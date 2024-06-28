# -*- coding =uft-8 -*-
# @TIME ： 2020/11/7 12:01
# @Author ： lkl
# @File ： demo2.py
# @Software: PyCharm
import webbrowser
import time

w1 = True
w2 = True
w3 = True
w4 = True
w5 = True
# 《总之就是非常可爱》
one = 'http://quan.qq.com/video/1098_46f94b993c53d17f89f5727375caa6a8'  # 第一集
two = 'http://quan.qq.com/video/1098_03e5edbd8911bbed6e3634d0e373a94a'  # 第二集
three = 'http://quan.qq.com/video/1098_c37f8f8fd43cb4a95b6f406cca6a06dc'  # 第三集
four = 'http://quan.qq.com/video/1098_e410686c0a5d2fdf1e56a0b5f467056d'  # 第四集
five = 'http://quan.qq.com/video/1098_36fd9833bc833c7b1cf6f21e65430f89'  # 第五集
six = 'http://quan.qq.com/video/1098_79ee77515c999260f727df13da0d28bd'  # 第六集
seven = 'http://1251316161.vod2.myqcloud.com/29fe1275vodbj1251316161/af8263365285890809877964020/EOVEEvvmAUkA.mp4'  # 第七集
eight = 'http://1251316161.vod2.myqcloud.com/29fe1275vodbj1251316161/7f4d0dd45285890810098144986/LaWEOhy2hEQA.mp4'  # 第八集
nine = 'http://quan.qq.com/video/1098_7dbce874666d638013c183d7b747b64b'  # 第九集
ten = 'http://quan.qq.com/video/1098_d5ef5c3f269a84ae32c8f64a13fab235'  # 第十集
eleven = 'http://quan.qq.com/video/1098_206cff014e062aa12d150c008abb18d9'  # 第十一集
twelve = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/1fa8c3b45285890811500696688/UIkjoLdZWboA.mp4'  # 第十二集
# 《平凡职业造就世界最强》
thirteen = 'http://quan.qq.com/video/1098_cdfc657ef791668f6bbfa14a864b8840'  # 第一集
fourteen = 'http://quan.qq.com/video/1098_f8a62a5f46ad6fb353d5c777bfefb79a'  # 第二集
fifteen = 'http://quan.qq.com/video/1098_956675ec90e24222044dd6c2512f8d04'  # 第三集
sixteen = 'http://quan.qq.com/video/1098_68640c4a6216d3106cc1d6d0ba1f5044'  # 第四集
seventeen = 'http://quan.qq.com/video/1098_6adc81dccbb14bc257c11ad820a7dc99'  # 第五集
eighteen = 'http://quan.qq.com/video/1098_dff670b8e7d8b72995bfeeffa26496b6'  # 第六集
nineteen = 'http://quan.qq.com/video/1098_b34dd99f1249a943d4a983d96be6a9b9'  # 第七集
twenty = 'http://quan.qq.com/video/1098_85307351739c980bb9306c2fafdde89d'  # 第八集
twenty_one = 'http://quan.qq.com/video/1098_5e5f43613843ccee1bd743d549f3a1a2'  # 第九集
twenty_two = 'http://quan.qq.com/video/1098_64218bb8c133c6c4d12eb5b6cbc9b138'  # 第十集
twenty_three = 'http://quan.qq.com/video/1098_11ba23290881b175e6b734089f8f9f38'  # 第十一集
twenty_four = 'http://quan.qq.com/video/1098_e3f9562f2fc5e5aa5bb9ea2d47b78818'  # 第十二集
twenty_five = 'http://quan.qq.com/video/1098_bbd341f386a83f15b69e08a9b617884a'  # 第十三集
twenty_six = 'http://quan.qq.com/video/1098_cc1526740e363664fb48d20db53073b4'  # 第五点五集
twenty_seven = 'http://quan.qq.com/video/1098_69670777b8383ef433fe25d3a9b7a267'  # OVA1
twenty_eight = 'http://quan.qq.com/video/1098_33b8b82fa6ddc59d3ff7958e64786fe5'  # OVA2
# 《魔王学院的不适者》
twenty_nine = 'http://quan.qq.com/video/1098_f4bc8119b7e46e5f537b9085d6dd36e7'  # 第一集
thirty = 'http://quan.qq.com/video/1098_8397936a9fcf05f8d07b795e648e0719'  # 第二集
thirty_one = 'http://quan.qq.com/video/1098_bb05dd0eb17ce02d4583fc816e05617f'  # 第三集
thirty_two = 'http://quan.qq.com/video/1098_701842d15a6ec13ce7aa7fef5bf7934e'  # 第四集
thirty_three = 'http://quan.qq.com/video/1098_bf9f29804a9da6b257648fb559fc9644'  # 第五集
thirty_four = 'http://quan.qq.com/video/1098_df5b03daf4366ac07ae03da5719974b5'  # 第六集
thirty_five = 'http://quan.qq.com/video/1098_9d8e725b87547da28f007c8690b14990'  # 第七集
thirty_six = 'http://quan.qq.com/video/1098_947022a11fb5ce5ab41a7c61833d27b7'  # 第八集
thirty_seven = 'http://quan.qq.com/video/1098_7a08b0d7faf1dc2d2a12958eac71fa4d'  # 第九集
thirty_eight = 'http://quan.qq.com/video/1098_2450d94762d65614061ea5841d4ddef5'  # 第十集
thirty_nine = 'http://quan.qq.com/video/1098_ab39982eb7941c3d04b07aa39b3e4679'  # 第十一集
forty = 'http://quan.qq.com/video/1098_b816bd4a596aaf5673f39ac8128c1752'  # 第十二集
fortyone = 'http://quan.qq.com/video/1098_0b4889cf0b8b4c3936535376a2c1f06c'  # 第十三集
# 《棍》
fortytwo = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c841de715285890814995493210/ALat0G5iwIQA.mp4'  # 第一集
fortythree = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c7b1c5185285890814995414953/UUxngYQhGd0A.mp4'  # 第二集
fortyfour = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c7d5e1365285890814995434481/PgYxhWbwvMoA.mp4'  # 第三集
fortyfive = ' http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c7d5e5775285890814995434581/E416c3vp89sA.mp4'  # 第四集
fortysix = 'http://50069.gzc.svp.tencent-cloud.com/gzc_1000035_0b53tudc6aagquabwqdk3nqjhhodf6oqml2a.f0.mp4'  # 第五集
fortyseven = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c7d65bb15285890814995435016/PhqO8taL4akA.mp4'  # 第六集
fortyeight = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/c7d67e7a5285890814995435871/iSbadbD8UvgA.mp4'  # 第七集
fortynine = 'http://1251316161.vod2.myqcloud.com/5f6ddb64vodsh1251316161/8cb1c6205285890814984395469/VJ5NCHpAS7EA.mp4'  # 第八集
fifty = ''  # 第九集
fiftyone = ''  # 第十集
fiftytwo = ''  # 第十一集
fiftythree = ''  # 第十二集

print('欢迎来到选集系统')
print('注意：在使用前请确保已联网，并已经下载了谷歌浏览器或Microsoft Edge，并设置为默认浏览器，否则视频可能无法正常播放')
print('     第一次加载可能会慢一点，请耐心等待')
print('目录：[总之就是非常可爱] [平凡职业造就世界最强][魔王学院的不适者] [敬请期待]')
while w1:
    name = input('您想看的番是（输入F退出）：')
    if name == '总之就是非常可爱':
        print('欢迎来到《总之就是非常可爱》选集系统')
        while w2:
            number = input('请输入集数编码（如：1）（输入F返回上一级）：')
            if number == '1':
                webbrowser.open(one)
                print('正在加载，请稍等')
                time.sleep(0.8)
                a = input('是否继续观看（T/F）')
                match a:
                    case 'F' 'f':
                        print('返回上一级')
                        break
                    case '_':
                        print('请继续观看')
            elif number == '2':
                webbrowser.open(two)
                print('正在加载，请稍等')
                time.sleep(0.8)
                b = input('是否继续观看（T/F）')
                if b == 'F' or b == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '3':
                webbrowser.open(three)
                print('正在加载，请稍等')
                time.sleep(0.8)
                c = input('是否继续观看（T/F）')
                if c == 'F' or c == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '4':
                webbrowser.open(four)
                print('正在加载，请稍等')
                time.sleep(0.8)
                d = input('是否继续观看（T/F）')
                if d == 'F' or d == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '5':
                webbrowser.open(five)
                print('正在加载，请稍等')
                time.sleep(0.8)
                e = input('是否继续观看（T/F）')
                if e == 'F' or e == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '6':
                webbrowser.open(six)
                print('正在加载，请稍等')
                time.sleep(0.8)
                f = input('是否继续观看（T/F）')
                if f == 'F' or f == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '7':
                webbrowser.open(seven)
                print('正在加载，请稍等')
                time.sleep(0.8)
                g = input('是否继续观看（T/F）')
                if g == 'F' or g == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '8':
                webbrowser.open(eight)
                print('正在加载，请稍等')
                time.sleep(0.8)
                h = input('是否继续观看（T/F）')
                if h == 'F' or h == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '9':
                webbrowser.open(nine)
                print('正在加载，请稍等')
                time.sleep(0.8)
                i = input('是否继续观看（T/F）')
                if i == 'F' or i == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '10':
                webbrowser.open(ten)
                print('正在加载，请稍等')
                time.sleep(0.8)
                j = input('是否继续观看（T/F）')
                if j == 'F' or j == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '11':
                webbrowser.open(eleven)
                print('正在加载，请稍等')
                time.sleep(0.8)
                k = input('是否继续观看（T/F）')
                if k == 'F' or k == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '12':
                webbrowser.open(twelve)
                print('正在加载，请稍等')
                time.sleep(0.8)
                l = input('全番结束，是否继续回看（T/F）')
                if l == 'F' or l == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == 'F' or number == 'f':
                print('返回上一级')
                break
            else:
                print('没有这个集数，请重新输入')
    elif name == '平凡职业造就世界最强':
        print('欢迎来到《平凡职业造就世界最强》选集系统')
        while True:
            number = input('请输入集数编码（如：1）（输入F返回上一级）（看五点五集输入14）（看OVA1输入15）（看OVA2输入16）：')
            if number == '1':
                print('请稍等')
                webbrowser.open(thirteen)
                a = input('是否继续观看（T/F）')
                if a == 'F' or a == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '2':
                print('请稍等')
                webbrowser.open(fourteen)
                b = input('是否继续观看（T/F）')
                if b == 'F' or b == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '3':
                print('请稍等')
                webbrowser.open(fifteen)
                c = input('是否继续观看（T/F）')
                if c == 'F' or c == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '4':
                print('请稍等')
                webbrowser.open(sixteen)
                d = input('是否继续观看（T/F）')
                if d == 'F' or d == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '5':
                print('请稍等')
                webbrowser.open(seventeen)
                e = input('是否继续观看（T/F）')
                if e == 'F' or e == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '6':
                print('请稍等')
                webbrowser.open(eighteen)
                f = input('是否继续观看（T/F）')
                if f == 'F' or f == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '7':
                print('请稍等')
                webbrowser.open(nineteen)
                g = input('是否继续观看（T/F）')
                if g == 'F' or g == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '8':
                print('请稍等')
                webbrowser.open(twenty)
                h = input('是否继续观看（T/F）')
                if h == 'F' or h == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '9':
                print('请稍等')
                webbrowser.open(twenty_one)
                i = input('是否继续观看（T/F）')
                if i == 'F' or i == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '10':
                print('请稍等')
                webbrowser.open(twenty_two)
                j = input('是否继续观看（T/F）')
                if j == 'F' or j == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '11':
                print('请稍等')
                webbrowser.open(twenty_three)
                k = input('是否继续观看（T/F）')
                if k == 'F' or k == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '12':
                print('请稍等')
                webbrowser.open(twenty_four)
                l = input('是否继续观看（T/F）')
                if l == 'F' or l == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '13':
                print('请稍等')
                webbrowser.open(twenty_five)
                m = input('全番结束，是否继续回看（T/F）')
                if m == 'F' or m == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '14':
                print('请稍等')
                webbrowser.open(twenty_six)
                n = input('是否继续观看（T/F）')
                if n == 'F' or n == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '15':
                print('请稍等')
                webbrowser.open(twenty_seven)
                o = input('是否继续观看（T/F）')
                if o == 'F' or o == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '16':
                print('请稍等')
                webbrowser.open(twenty_eight)
                p = input('是否继续观看（T/F）')
                if p == 'F' or p == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == 'F' or number == 'f':
                print('返回上一级')
            else:
                print('没有这个集数，请重新输入')
    elif name == '魔王学院的不适者':
        print('欢迎来到《魔王学院的不适者》选集系统')
        while True:
            number = input('请输入集数编码（如：1）（输入F返回上一级）：')
            if number == '1':
                print('请稍等')
                webbrowser.open(twenty_nine)
                a = input('是否继续观看（T/F）')
                if a == 'F' or a == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '2':
                print('请稍等')
                webbrowser.open(thirty)
                b = input('是否继续观看（T/F）')
                if b == 'F' or b == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '3':
                print('请稍等')
                webbrowser.open(thirty_one)
                c = input('是否继续观看（T/F）')
                if c == 'F' or c == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '4':
                print('请稍等')
                webbrowser.open(thirty_two)
                d = input('是否继续观看（T/F）')
                if d == 'F' or d == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '5':
                print('请稍等')
                webbrowser.open(thirty_three)
                e = input('是否继续观看（T/F）')
                if e == 'F' or e == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '6':
                print('请稍等')
                webbrowser.open(thirty_four)
                f = input('是否继续观看（T/F）')
                if f == 'F' or f == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '7':
                print('请稍等')
                webbrowser.open(thirty_five)
                g = input('是否继续观看（T/F）')
                if g == 'F' or g == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '8':
                print('请稍等')
                webbrowser.open(thirty_six)
                h = input('是否继续观看（T/F）')
                if h == 'F' or h == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '9':
                print('请稍等')
                webbrowser.open(thirty_seven)
                i = input('是否继续观看（T/F）')
                if i == 'F' or i == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '10':
                print('请稍等')
                webbrowser.open(thirty_eight)
                j = input('是否继续观看（T/F）')
                if j == 'F' or j == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '11':
                print('请稍等')
                webbrowser.open(thirty_nine)
                k = input('是否继续观看（T/F）')
                if k == 'F' or k == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '12':
                print('请稍等')
                webbrowser.open(forty)
                l = input('是否继续观看（T/F）')
                if l == 'F' or l == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == '13':
                print('请稍等')
                webbrowser.open(fortyone)
                m = input('全番结束，是否继续回看（T/F）')
                if m == 'F' or m == 'f':
                    print('返回上一级')
                    break
                else:
                    print('请继续观看')
            elif number == 'F' or number == 'f':
                print('返回上一级')
            else:
                print('没有这个集数，请重新输入')
    elif name == 'NPVDSNWYWW-eyJsaWNlbnNlSWQiOi':
        print('账号正确')
        time.sleep(2)
        print('亏得你可以找到这里')
        while w4:
            a = input('请输入密码（返回请输入F）：')
            if a == 'ghkfkHFHKFfffjkfHKyireFDJWSJflogfO*U^%*UGdyier7fyidiyr7':
                print('密码正确')
                while w5:
                    number = input('《回复术士》你想看第几集（输入F返回）(9,10,11,12集因技术原因无法播放)：')
                    if number == '1':
                        webbrowser.open(fortytwo)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        a = input('是否继续观看（T/F）')
                        if a == 'F' or a == 'f':
                            print('返回上一级')
                            w4 = False
                            break
                        else:
                            print('请继续观看')
                    elif number == '2':
                        webbrowser.open(fortythree)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        b = input('是否继续观看（T/F）')
                        if b == 'F' or b == 'f':
                            print('返回上一级')
                            w4 = False
                            break
                        else:
                            print('请继续观看')
                    elif number == '3':
                        webbrowser.open(fortyfour)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        c = input('是否继续观看（T/F）')
                        if c == 'F' or c == 'f':
                            print('返回上一级')
                            w4 = False
                            break
                        else:
                            print('请继续观看')
                    elif number == '4':
                        webbrowser.open(fortyfive)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        d = input('是否继续观看（T/F）')
                        if d == 'F' or d == 'f':
                            print('返回上一级')
                            w4 = False
                            break
                        else:
                            print('请继续观看')
                    elif number == '5':
                        webbrowser.open(fortysix)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        e = input('是否继续观看（T/F）')
                        if e == 'F' or e == 'f':
                            print('返回上一级')
                            w4 = False
                            break
                        else:
                            print('请继续观看')
                    elif number == '6':
                        webbrowser.open(fortyseven)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        f = input('是否继续观看（T/F）')
                        if f == 'F' or f == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '7':
                        webbrowser.open(fortyeight)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        g = input('是否继续观看（T/F）')
                        if g == 'F' or g == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '8':
                        webbrowser.open(fortynine)
                        print('正在加载，请稍等')
                        time.sleep(0.8)
                        h = input('是否继续观看（T/F）')
                        if h == 'F' or h == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '9':
                        print('暂时没有片源，请见谅')
                        i = input('是否继续观看（T/F）')
                        if i == 'F' or i == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '10':
                        print('暂时没有片源，请见谅')
                        j = input('是否继续观看（T/F）')
                        if j == 'F' or j == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '11':
                        print('暂时没有片源，请见谅')
                        k = input('是否继续观看（T/F）')
                        if k == 'F' or k == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == '12':
                        print('暂时没有片源，请见谅')
                        l = input('全番结束，是否继续回看（T/F）')
                        if l == 'F' or l == 'f':
                            print('返回上一级')
                            break
                        else:
                            print('请继续观看')
                    elif number == 'F' or number == 'f':
                        print('返回上一级')
                        break
                    else:
                        print('没有这个集数，请重新输入')
            elif a == 'f' or a == 'F':
                print('返回上一级')
                break
            else:
                print('密码错误，重新输入')
    elif name == 'F' or name == 'f':
        print('正在关闭')
        time.sleep(2)
        print('感谢使用本系统，期待下次再见')
        time.sleep(1)
        break
    else:
        print('很抱歉，暂时没有收录这个番')
