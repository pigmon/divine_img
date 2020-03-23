import urllib.request
import catch

def get_id_list(_file):
    f = open(_file, "r")
    list_id = f.readlines()
    
    for i in range(0, len(list_id)):
        id = list_id[i].strip('\n')
        list_id[i] = id

    return list_id 


if __name__ == '__main__':
    missing_id_list = get_id_list("D:\\DivineCatch\\missing_page.log")

    for id in missing_id_list:
        print("Begin ID: " + id + ":")
        list_icon= catch.get_img_url(id)

        for idx_icon in range(0, len(list_icon)):
            catch.save_icon(list_icon[idx_icon], id + "-" + str(idx_icon))

