from bs4 import BeautifulSoup
import requests

def fetch_data(url , path):
    r = requests.get(url , path )
    with open(path , "w") as f:
        f.write(r.text)
url = "https://www.temu.com/pk-en/1pc-mens---steel-silvery-------popular-jewelry---g-601099521154377.html?_oak_mp_inf=EMm6u5um1ogBGiA1YWM0NDhjNzRhMzU0MDRkYjUxYjFjMzNlM2M1NjAxNCC83aqGsjI%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F8f985c8713e75d9d1eb78bef36113994.jpg&spec_gallery_id=4016895285&refer_page_sn=10005&refer_source=0&freesia_scene=1&_oak_freesia_scene=1&_oak_rec_ext_1=MjYxMDA&_oak_gallery_order=1259580797%2C1997213293%2C941512362%2C1440771372%2C1624286411&refer_page_el_sn=200024&refer_page_name=home&refer_page_id=10005_1731421966006_mdu6e6tjzw&_x_sessn_id=rm848utf5y"

fetch_data(url , "data/temu.html")
with open("data/temu.html" , 'r') as f:
    data = f.read()

soup = BeautifulSoup(data , 'html.parser')
