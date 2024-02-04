import requests
from bs4 import BeautifulSoup

def get_wikipedia_page_content(url):
    """Obtenir le contenu HTML d'une page Wikipedia."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"La requête a échoué avec le code : {response.status_code}")
        return None
    

def extract_title(html_content):
    """Extraire le titre de la page depuis le contenu HTML."""
    soup = BeautifulSoup(html_content,'html.parser')
    title = soup.title.string
    return title


def extract_sections_with_paragraphs(html_content,title_tag='h2',paragraph_tag='p'):
    """Extraire les sections avec leurs paragraphes depuis le contenu HTML."""
    soup = BeautifulSoup(html_content,'html.parser')
    page_dict = {}


    #Extraire les titres des paragraphes
    for heading in soup.find_all(title_tag):
        title = heading.text.strip()
        paragraphs = []

        #Récupérer tous les paragraphes sous le titre actuel
        for sibling in heading.find_next_siblings():
            if sibling.name and sibling.name ==title_tag:
                break
            elif sibling.name == paragraph_tag:
                paragraphs.append(sibling.text.strip())

        page_dict[title] = paragraphs

    return page_dict


def extract_links(html_content, link_tag='a',link_attribute='href'):
    """Extraire les liens depuis le contenu HTML."""
    soup = BeautifulSoup(html_content,'html.parser')
    links = []


    for link in soup.find_all(link_tag,{link_attribute: True}):
        href = link.get(link_attribute)
        links.append(href)

    return links


def analyse_page(url, title_tag='h1', paragraph_tag='p',link_tag='a',link_attribute='href'):
    """Intégrer toutes les fonctions précédentes dans une seule fonction."""
    html_content = get_wikipedia_page_content(url)


    if html_content:
        #extraire le titre de la page
        title = extract_title(html_content)
        print(f"Titre de la page:{title}\n")

        #extraire les sections avec leurs paragraphes
        page_dict = extract_sections_with_paragraphs(html_content,title_tag,paragraph_tag)
        for section_title, paragraphs in page_dict_items():
            print(f"{section_title} :")
            for paragraph in paragraphs:
                print(paragraph)
            print()

        
        #estraire les liens de la page
        links = extract_links(html_content,link_tag,link_attribute)
        print("\nLiens de la page:")
        for link in links:
            print(link)