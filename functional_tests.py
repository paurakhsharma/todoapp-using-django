from selenium import webdriver
browser = webdriver.Firefox()


# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')


# She notices the page title and header mention to-do list
assert 'To-Do' in browser.title


# She is invited to enter a to-do tiem straight away

# She type "Buy peacock feathers" into a text box (Edith's hobby
# is typing fly-fishing lures)


browser.quit()
