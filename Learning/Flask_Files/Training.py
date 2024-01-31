from flask import Flask, render_template

skills_app = Flask(__name__) # Giving a Name to Our Web App
skills_app = Flask(__name__, template_folder='/Users/Ahmed/Desktop/Flask_Files') # Setting the Template Folder Where You App Files 

# Skills List
my_skills = [("HTML", 80), ("CSS", 75), ("Python", 95), ("JavaScript", 60)]


# Settign up routing (Homepage, About, Contact, ... Etc.)
@skills_app.route("/")  # Main Route Like elzero.or/
def homepage(): 

    return render_template("homepage.html", pagetitle="Homepage", custom_css="home")

@skills_app.route("/about")
def about(): # about Route Like elzero.or/about

    return render_template("about.html", pagetitle="About", custom_css="about")

@skills_app.route("/skills")
def skills():

    return render_template("skills.html", pagetitle="My Skills", custom_css="skills", 
                           page_head="My Skills", description="This is my Skills Page", 
                           skills=my_skills)




if __name__ == "__main__": 

    skills_app.run(debug=True, port=7000)
