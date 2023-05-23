from core.Common import Common, waste_some_time

#Xpath
#absolute /html/body/div[x]/div[y]
#relative //tagname[attribute="value"]
#Xpath=//h2[id="name"]
#//input[@id='Password']/parent::div/following-sibling::input
#no hace el recorrido detodo el camino
# dom pagina con html elememtos dentro de la pagina codigo fuente
#//p[text()='First name cannot be empty']/parent::div/following-sibling::div/following-sibling::div/following-sibling::div/input
#//p[text()='First name cannot be empty'] busqueda por texto

# Test data
TEST_URL = "file:///Users/LauraJCurtidorH/Downloads/SelectorsLocatorsPractice.html"
BROWSER = "chrome"

# Test Elements
XPATH_FIRST_NAME = "XPATH://input[@id='first-name']"
XPATH_LAST_NAME = "XPATH://input[@name='last-name']"
XPATH_EMAIL = "XPATH://input[@type='email']"
XPATH_PASSWORD = "XPATH://input[@id='Password']"
XPATH_SUBMIT = "XPATH://input[@id='Password']/parent::div/following-sibling::input]"

# Test Actions

letsAutomate = Common(BROWSER)
letsAutomate.launch_site(TEST_URL, XPATH_FIRST_NAME)

def do_search(input1, input2, input3, input4):
    letsAutomate.fill_input_text(XPATH_FIRST_NAME, input1)
    letsAutomate.fill_input_text(XPATH_LAST_NAME, input2)
    letsAutomate.fill_input_text(XPATH_EMAIL, input3)
    letsAutomate.fill_input_text(XPATH_PASSWORD, input4)
    waste_some_time(2)
    letsAutomate.do_click(XPATH_SUBMIT)
    letsAutomate.page_back()

do_search("Laura","Curtidor", "laura@epam.com", "Dom12345")

#def do_searches(list_of_texts_to_search):
#    for text_to_search in list_of_texts_to_search:
#        do_search(text_to_search)


# Let's see how to do our three searches in a single line

#do_searches(["First Second", "Second Search", "Third Search"])

# Impressed? no? wait I know what the heck is that weird angular parenthesis? Python is cool, and let us
# create a list just list this:

#my_list_of_texts_to_search = ["Why", "Learning", "backwards", "it is", "so cool", "etc..."]

# so, now you can use your list in our do_searches test action.

#do_searches(my_list_of_texts_to_search)hes(["First Second", "Second Search", "Third Search"])