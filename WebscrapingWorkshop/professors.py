import requests
from bs4 import BeautifulSoup

def get_wm_professors():
    url = 'https://www.wm.edu/as/computerscience/people/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    professors = soup.find_all("article", class_="item_listing directory_listing")
    professorsList = []
    for i in range(len(professors)):
        professorsList.append(professors[i].find("p").find("a").string)

    return professorsList

def get_professor_id(professor_name):
    url = f"https://www.ratemyprofessors.com/search/professors/269?q={professor_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    professor_links = soup.find_all("a", href=True)

    for link in professor_links:
        if "/professor/" in link["href"]:
            prof_id = link["href"].split("/")[-1]
            return prof_id
        
def get_all_professor_ids():
    professor_names = get_wm_professors()
    professor_ids = [get_professor_id(name) for name in professor_names if get_professor_id(name) is not None]
    return professor_ids

def save_professor_ids_to_file(filename="professor_ids.txt"):
    professor_ids = get_all_professor_ids()
    with open(filename, "w") as file:
        for prof_id in professor_ids:
            file.write(prof_id + "\n")

save_professor_ids_to_file()
