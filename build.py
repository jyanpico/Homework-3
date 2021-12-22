print("Combining Files")

def replace_content(template, replacment_content):
    return template.replace("{{content}}", replacment_content)

def replace_title(template, replacement_title):
    return template.replace("{{title}}", replacement_title)

def tada():
    print("TADA!!!!!")

def main():
    pages = [
        {
            "filename": "./content/index.html",
            "output": "docs/index.html",
            "title": "About me",
        },
        {
            "filename": "./content/resume.html",
            "output": "docs/resume.html",
            "title": "My Resume",
        },
        {
            "filename": "./content/projects.html",
            "output": "docs/projects.html",
            "title": "My Projects",
        },
    ]
    #Base Template variable
   
    for page in pages:
        template = open('./templates/base.html').read()
        new_page = open(page['filename']).read()
        new_page_with_replacements = replace_content(template, new_page)
        new_page_with_replacements = replace_title(new_page_with_replacements, page['title'])
        new_template = open(page['output'], 'w').write(new_page_with_replacements)
    tada()
    
main()





    
