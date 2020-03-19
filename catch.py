import urllib.request
import re

def get_img_url(_id):
    url = 'http://zh.divine-gate.wikia.com/wiki/' + _id
    ret = []

    try:
        req = urllib.request.urlopen(url, timeout = 60)
        print('Url opened, now begin to read : ' + url)
        buf = req.read()
        print('Reding is done, now decoding...')

    except:
        print('socket timed out - URL %s', url)
        save_url_to_file(_id, "D:\\DivineCatch\\err.log")
        return ret
    else:
        buf = buf.decode('UTF-8')
        print('Begin to find pattern...')

        pattern_icon = re.compile(r"https://vignette.wikia.nocookie.net/divine-gate/images/[/\w]+?" + _id + "-icon.png/[\w\W]+?path-prefix=zh")
        #pattern_big =  re.compile(r"https://vignette.wikia.nocookie.net/divine-gate/images/[/\w]+?" + _id + ".png")

        list_icon = re.findall(pattern_icon, buf)
        #list_big = re.findall(pattern_big, buf)

        print('Access successful.')
        ret = list(set(list_icon))

        #print(ret)

        return ret #, list_big




def save_icon(_url, _id):
    file_name = _id + "-icon.png"
    print("Saving " + _url + " as file " + "[" + file_name + "].")
    f = open("D:\\DivineCatch\\Icon\\" + file_name, 'wb')

    try:
        req = urllib.request.urlopen(_url, timeout = 120)
        buf = req.read()
    except:
        print('socket timed out - URL %s', _url)
        save_url_to_file(_url, "D:\\DivineCatch\\missing.log")
        f.close()
        return
    else:
        f.write(buf)
        print("Done.")

    f.close()
    

def save_big(_url, _id):
    file_name = _id + "-icon.png"
    print("Saving " + _url + " as file " + "[" + file_name + "].")
    f = open("D:\\DivineCatch\\Big\\" + file_name, 'wb')
    req = urllib.request.urlopen(_url)
    buf = req.read()
    f.write(buf)
    f.close()
    print("Done.")

def save_url_to_file(_url, _file):
    f = open(_file, 'a')
    f.write(_url + "\n")
    f.close()

if __name__ == '__main__':
    for i in range(145, 227):
        str_id = str(i).zfill(3)
        print("Begin ID: " + str_id + ":")
        list_icon= get_img_url(str_id)

        for idx_icon in range(0, len(list_icon)):
            save_icon(list_icon[idx_icon], str_id + "-" + str(idx_icon))

        """
        for idx_big in range(0, len(list_big)):
            save_big(list_big[idx_big], str_id + "_" + str(idx_big))
        """