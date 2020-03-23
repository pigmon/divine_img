import urllib.request
import catch

def get_url_list(_file):
    f = open(_file, "r")
    list_url = f.readlines()
    f.close()

    return list_url 

if __name__ == '__main__':
    missing_img_list = get_url_list("D:\\DivineCatch\\missing_img.log")

    for id in missing_img_list:
        print("Begin ID: " + id + ":")
        list_icon = catch.get_img_url(id)

        for idx_icon in range(0, len(list_icon)):
            catch.save_icon(list_icon[idx_icon], id + "-" + str(idx_icon))