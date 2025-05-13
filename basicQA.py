import tkinter as tk
from tkinter import ttk, messagebox
import tkinter


# --- Student class ---
class Student:
    def __init__(self):
        self.interest = ""
        self.fav_sub = ""
        self.first_goal = ""
        self.second_goal = ""
        self.academic_performance = ""

# --- Forward Chaining Advisor class ---
class Advisor:
    def __init__(self, student):
        self.student = student
        self.facts = set()
        self.advice = ""

    def gather_facts(self):
        # interest
        if self.student.interest == "3D modeling/animation":
            self.facts.add("3D artist")
        
        if self.student.interest == "Active sport":
            self.facts.add("Athletic")
                            
        if self.student.interest == "Coding":
            self.facts.add("interested in programming")

        if self.student.interest == "Drawing/Painting":
            self.facts.add("aritistic")
        
        if self.student.interest == "Digital Editing":
            self.facts.add("Content editor")

        if self.student.interest == "Fashion Design":
            self.facts.add("Fashionist")

        if self.student.interest == "Fixing gadgets":
            self.facts.add("interested in hardware")
        
        if self.student.interest == "Graphic Design":
            self.facts.add("Graphic artist")

        if self.student.interest == "Journaling":
            self.facts.add("Journal writer")

        if self.student.interest == "Learning new language":
            self.facts.add("linguphiles")

        if self.student.interest == "Photography":
            self.facts.add("Visual artist")

        if self.student.interest == "Programming":
            self.facts.add("programmer")
        
        if self.student.interest == "Reading novels":
            self.facts.add("bookworm")
        
        if self.student.interest == "Science experiments":
            self.facts.add("explorer")

        if self.student.interest == "Singing":
            self.facts.add("singerist")

        if self.student.interest == "Solving puzzles":
            self.facts.add("Logical thinker")

        if self.student.interest == "Thrifting/Online Selling":
            self.facts.add("E-commerce seller")

        if self.student.interest == "Traveling":
            self.facts.add("Adventurer")
        
        if self.student.interest == "Video Gaming":
            self.facts.add("gamer")

        if self.student.interest == "Vlogging":
            self.facts.add("Conteent Creator")

        if self.student.interest == "Writing stories":
            self.facts.add("writer")
            

        # favorite subject
        if self.student.fav_sub == "Computer":
            self.facts.add("tech-savvy")

        if self.student.fav_sub == "English":
            self.facts.add("wordsmith")

        if self.student.fav_sub == "Mathematics":
            self.facts.add("Analytical Thinker")
        
        if self.student.fav_sub == "Filipino":
            self.facts.add("Native language Advocate")

        if self.student.fav_sub == "MAPEH":
            self.facts.add("creative individual")

        if self.student.fav_sub == "Science":
            self.facts.add("Aspiring Scientist")
            
        # Academic performance
        if self.student.academic_performance == "good":
            self.facts.add("academically strong")
        elif self.student.academic_performance == "bad":
            self.facts.add("needs improvement")
            
        # first goal
        if self.student.first_goal == "Undecided":
            self.facts.add("aims for Undecided")
        if self.student.first_goal == "Accounting":
            self.facts.add("aims for Accounting")

        if self.student.first_goal == "Architecture":
            self.facts.add("aims for Architecture")

        if self.student.first_goal == "Biology":
            self.facts.add("aims for Biology")

        if self.student.first_goal == "Business Administration":
            self.facts.add("aims for Business Administration")

        if self.student.first_goal == "Chemical Engineering":
            self.facts.add("aims for Chemical Engineering")

        if self.student.first_goal == "Civil Engineering":
            self.facts.add("aims for Civil Engineering")

        if self.student.first_goal == "Communication":
            self.facts.add("aims for Communication")

        if self.student.first_goal == "Computer Science":
            self.facts.add("aims for Computer Science")

        if self.student.first_goal == "Criminology":
            self.facts.add("aims for Criminology")

        if self.student.first_goal == "Economics":
            self.facts.add("aims for Economics")

        if self.student.first_goal == "Education":
            self.facts.add("aims for Education")

        if self.student.first_goal == "Electrical Engineering":
            self.facts.add("aims for Electrical Engineering")

        if self.student.first_goal == "Environmental Science":
            self.facts.add("aims for Environmental Science")

        if self.student.first_goal == "Finance":
            self.facts.add("aims for Finance")

        if self.student.first_goal == "Fine Arts":
            self.facts.add("aims for Fine Arts")

        if self.student.first_goal == "Hospitality Management":
            self.facts.add("aims for Hospitality Management")

        if self.student.first_goal == "Information Technology":
            self.facts.add("aims for Information Technology")

        if self.student.first_goal == "Journalism":
            self.facts.add("aims for Journalism")

        if self.student.first_goal == "Law":
            self.facts.add("aims for Law")

        if self.student.first_goal == "Marketing":
            self.facts.add("aims for Marketing")

        if self.student.first_goal == "Mechanical Engineering":
            self.facts.add("aims for Mechanical Engineering")

        if self.student.first_goal == "Medicine":
            self.facts.add("aims for Medicine")

        if self.student.first_goal == "Nursing":
            self.facts.add("aims for Nursing")

        if self.student.first_goal == "Pharmacy":
            self.facts.add("aims for Pharmacy")

        if self.student.first_goal == "Political Science":
            self.facts.add("aims for Political Science")

        if self.student.first_goal == "Psychology":
            self.facts.add("aims for Psychology")

        if self.student.first_goal == "Public Administration":
            self.facts.add("aims for Public Administration")

        if self.student.first_goal == "Social Work":
            self.facts.add("aims for Social Work")

        if self.student.first_goal == "Sociology":
            self.facts.add("aims for Sociology")

        if self.student.first_goal == "Theater Arts":
            self.facts.add("aims for Theater Arts")
        #second goal
        if self.student.second_goal == "Undecided":
            self.facts.add("also aims for Undecided")

        if self.student.second_goal == "Accounting":
            self.facts.add("also aims for Accounting")

        if self.student.second_goal == "Architecture":
            self.facts.add("also aims for Architecture")

        if self.student.second_goal == "Biology":
            self.facts.add("also aims for Biology")

        if self.student.second_goal == "Business Administration":
            self.facts.add("also aims for Business Administration")

        if self.student.second_goal == "Chemical Engineering":
            self.facts.add("also aims for Chemical Engineering")

        if self.student.second_goal == "Civil Engineering":
            self.facts.add("also aims for Civil Engineering")

        if self.student.second_goal == "Communication":
            self.facts.add("also aims for Communication")

        if self.student.second_goal == "Computer Science":
            self.facts.add("also aims for Computer Science")

        if self.student.second_goal == "Criminology":
            self.facts.add("also aims for Criminology")

        if self.student.second_goal == "Economics":
            self.facts.add("also aims for Economics")

        if self.student.second_goal == "Education":
            self.facts.add("also aims for Education")

        if self.student.second_goal == "Electrical Engineering":
            self.facts.add("also aims for Electrical Engineering")

        if self.student.second_goal == "Environmental Science":
            self.facts.add("also aims for Environmental Science")

        if self.student.second_goal == "Finance":
            self.facts.add("also aims for Finance")

        if self.student.second_goal == "Fine Arts":
            self.facts.add("also aims for Fine Arts")

        if self.student.second_goal == "Hospitality Management":
            self.facts.add("also aims for Hospitality Management")

        if self.student.second_goal == "Information Technology":
            self.facts.add("also aims for Information Technology")

        if self.student.second_goal == "Journalism":
            self.facts.add("also aims for Journalism")

        if self.student.second_goal == "Law":
            self.facts.add("also aims for Law")

        if self.student.second_goal == "Marketing":
            self.facts.add("also aims for Marketing")

        if self.student.second_goal == "Mechanical Engineering":
            self.facts.add("also aims for Mechanical Engineering")

        if self.student.second_goal == "Medicine":
            self.facts.add("also aims for Medicine")

        if self.student.second_goal == "Nursing":
            self.facts.add("also aims for Nursing")

        if self.student.second_goal == "Pharmacy":
            self.facts.add("also aims for Pharmacy")

        if self.student.second_goal == "Political Science":
            self.facts.add("also aims for Political Science")

        if self.student.second_goal == "Psychology":
            self.facts.add("also aims for Psychology")

        if self.student.second_goal == "Public Administration":
            self.facts.add("also aims for Public Administration")

        if self.student.second_goal == "Social Work":
            self.facts.add("also aims for Social Work")

        if self.student.second_goal == "Sociology":
            self.facts.add("also aims for Sociology")

        if self.student.second_goal == "Theater Arts":
            self.facts.add("also aims for Theater Arts")
    
    def match_goal_pair(self, goal1, goal2):
        return (
        {f"aims for {goal1}", f"also aims for {goal2}"}.issubset(self.facts) or
        {f"aims for {goal2}", f"also aims for {goal1}"}.issubset(self.facts)
    )



    def apply_rules(self):
        if "needs improvement" in self.facts:
            self.advice = "Advice: Get to know yourself deeply before making a major decision."
            return

        elif {
            "3D artist",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Fine Arts", "Architecture"):
            self.advice = (
                "Recommendations: Your skills in 3D modeling and creativity can lead to careers like:\n"
                "- 3D Animator\n"
                "- Game Designer\n"
                "- Visual Effects Artist\n\n"
                "Recommended Courses:\n"
                "- Fine Arts\n"
                "- Architecture\n"
                "- Multimedia Arts"
            )

        elif {
            "Athletic",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Physical Education", "Sports Science"):
            self.advice = (
                "Recommendations: Your passion for active sports and creativity can lead to careers like:\n"
                "- Physical Education Teacher\n"
                "- Sports Coach\n"
                "- Athletic Trainer\n\n"
                "Recommended Courses:\n"
                "- Physical Education\n"
                "- Sports Science\n"
                "- Kinesiology"
            )

        elif {
            "interested in programming",
            "Analytical Thinker",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Computer Science", "Undecided"):
            self.advice = (
                "Recommendations: If you like programming and are good at mathematics, you might enjoy careers like:\n"
                "- Data Analyst\n"
                "- Machine Learning Engineer\n"
                "- Data Scientist\n"
                "- Robotics Engineer\n\n"
                "Recommended Courses:\n"
                "- Computer Engineering\n"
                "- Computer Science\n"
                "- Software Engineering"
            )

        elif {
            "aritistic",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Fine Arts", "Architecture"):
            self.advice = (
                "Recommendations: Your talent in drawing and painting can lead to careers like:\n"
                "- Illustrator\n"
                "- Art Director\n"
                "- Gallery Curator\n\n"
                "Recommended Courses:\n"
                "- Fine Arts\n"
                "- Visual Arts\n"
                "- Art History"
            )

        elif {
            "Fashionist",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Fashion Design", "Marketing"):
            self.advice = (
                "Recommendations: Your interest in fashion design and creativity can lead to careers like:\n"
                "- Fashion Designer\n"
                "- Brand Manager\n"
                "- Fashion Merchandiser\n\n"
                "Recommended Courses:\n"
                "- Fashion Design\n"
                "- Marketing\n"
                "- Textile Design"
            )

        elif {
            "Content editor",
            "tech-savvy",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Digital Media", "Communication"):
            self.advice = (
                "Recommendations: Your skills in digital editing and technology can lead to careers like:\n"
                "- Video Editor\n"
                "- Content Creator\n"
                "- Multimedia Specialist\n\n"
                "Recommended Courses:\n"
                "- Digital Media\n"
                "- Communication Arts\n"
                "- Film Production"
            )

        elif {
            "interested in hardware",
            "Analytical Thinker",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Electrical Engineering", "Computer Engineering"):
            self.advice = (
                "Recommendations: Your interest in fixing gadgets and analytical skills can lead to careers like:\n"
                "- Hardware Engineer\n"
                "- Electronics Technician\n"
                "- Systems Engineer\n\n"
                "Recommended Courses:\n"
                "- Electrical Engineering\n"
                "- Computer Engineering\n"
                "- Mechatronics"
            )

        elif {
            "Graphic artist",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Graphic Design", "Marketing"):
            self.advice = (
                "Recommendations: Your talent in graphic design and creativity can lead to careers like:\n"
                "- Graphic Designer\n"
                "- Art Director\n"
                "- UX/UI Designer\n\n"
                "Recommended Courses:\n"
                "- Graphic Design\n"
                "- Visual Communication\n"
                "- Marketing"
            )

        elif {
            "Journal writer",
            "wordsmith",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Journalism", "Communication"):
            self.advice = (
                "Recommendations: Your passion for journaling and writing can lead to careers like:\n"
                "- Journalist\n"
                "- Editor\n"
                "- Content Writer\n\n"
                "Recommended Courses:\n"
                "- Journalism\n"
                "- Communication Arts\n"
                "- English Literature"
            )

        elif {
            "linguphiles",
            "wordsmith",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Linguistics", "Education"):
            self.advice = (
                "Recommendations: Your interest in learning new languages can lead to careers like:\n"
                "- Translator\n"
                "- Language Teacher\n"
                "- Linguist\n\n"
                "Recommended Courses:\n"
                "- Linguistics\n"
                "- Education\n"
                "- Foreign Languages"
            )

        elif {
            "Visual artist",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Photography", "Fine Arts"):
            self.advice = (
                "Recommendations: Your passion for photography and creativity can lead to careers like:\n"
                "- Photographer\n"
                "- Photojournalist\n"
                "- Visual Artist\n\n"
                "Recommended Courses:\n"
                "- Photography\n"
                "- Fine Arts\n"
                "- Visual Communication"
            )

        elif {
            "programmer",
            "Analytical Thinker",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Software Engineering", "Computer Science"):
            self.advice = (
                "Recommendations: Your skills in programming and analytical thinking can lead to careers like:\n"
                "- Software Developer\n"
                "- Systems Analyst\n"
                "- Application Developer\n\n"
                "Recommended Courses:\n"
                "- Software Engineering\n"
                "- Computer Science\n"
                "- Information Technology"
            )

        elif {
            "bookworm",
            "wordsmith",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Literature", "Education"):
            self.advice = (
                "Recommendations: Your love for reading novels and writing can lead to careers like:\n"
                "- Author\n"
                "- Editor\n"
                "- Literature Professor\n\n"
                "Recommended Courses:\n"
                "- English Literature\n"
                "- Creative Writing\n"
                "- Education"
            )

        elif {
            "explorer",
            "Aspiring Scientist",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Biology", "Chemistry"):
            self.advice = (
                "Recommendations: Your interest in science experiments can lead to careers like:\n"
                "- Research Scientist\n"
                "- Lab Technician\n"
                "- Biochemist\n\n"
                "Recommended Courses:\n"
                "- Biology\n"
                "- Chemistry\n"
                "- Biochemistry"
            )

        elif {
            "singerist",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Music", "Performing Arts"):
            self.advice = (
                "Recommendations: Your talent in singing and creativity can lead to careers like:\n"
                "- Singer\n"
                "- Music Teacher\n"
                "- Vocal Coach\n\n"
                "Recommended Courses:\n"
                "- Music\n"
                "- Performing Arts\n"
                "- Music Education"
            )

        elif {
            "Logical thinker",
            "Analytical Thinker",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Mathematics", "Computer Science"):
            self.advice = (
                "Recommendations: Your skill in solving puzzles and analytical thinking can lead to careers like:\n"
                "- Mathematician\n"
                "- Data Analyst\n"
                "- Cryptographer\n\n"
                "Recommended Courses:\n"
                "- Mathematics\n"
                "- Computer Science\n"
                "- Statistics"
            )

        elif {
            "E-commerce seller",
            "Entrepreneurial",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Business Administration", "Marketing"):
            self.advice = (
                "Recommendations: Your experience in online selling and entrepreneurship can lead to careers like:\n"
                "- Business Owner\n"
                "- Marketing Specialist\n"
                "- E-commerce Manager\n\n"
                "Recommended Courses:\n"
                "- Business Administration\n"
                "- Marketing\n"
                "- Entrepreneurship"
            )

        elif {
            "Adventurer",
            "culturally aware",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Tourism", "Hospitality Management"):
            self.advice = (
                "Recommendations: Your love for traveling and cultural awareness can lead to careers like:\n"
                "- Travel Agent\n"
                "- Tour Guide\n"
                "- Hospitality Manager\n\n"
                "Recommended Courses:\n"
                "- Tourism\n"
                "- Hospitality Management\n"
                "- International Relations"
            )

        elif {
            "gamer",
            "tech-savvy",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Undecided", "Computer Science"):
            self.advice = (
                "Recommendations: Your passion for video gaming and technology can lead to careers like:\n"
                "- Game Developer\n"
                "- Game Designer\n"
                "- QA Tester\n\n"
                "Recommended Courses:\n"
                "- Game Development\n"
                "- Computer Science\n"
                "- Interactive Media"
            )

        elif {
            "Conteent Creator",
            "creative individual",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Communication", "Digital Media"):
            self.advice = (
                "Recommendations: Your skills in vlogging and creativity can lead to careers like:\n"
                "- Content Creator\n"
                "- Social Media Manager\n"
                "- Digital Marketer\n\n"
                "Recommended Courses:\n"
                "- Communication\n"
                "- Digital Media\n"
                "- Marketing"
            )

        elif {
            "writer",
            "wordsmith",
            "academically strong"
        }.issubset(self.facts) and self.match_goal_pair("Journalism", "Undecided"):
            self.advice = (
                "Recommendations: Your passion for writing and strength in language arts can lead to fulfilling careers such as:\n"
                "- Author or Novelist\n"
                "- Screenwriter\n"
                "- Content Writer\n"
                "- Editor\n\n"
                "Recommended Courses:\n"
                "- Creative Writing\n"
                "- Journalism\n"
                "- English Literature\n"
                "- Communication Arts"
            )
        



        else:
            self.advice = "General advice: Keep exploring your interests and goals, and consult mentors."

    def advise(self):
        self.gather_facts()
        self.apply_rules()
        return self.advice

# --- GUI class ---
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AdvisorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Career Advisor")
        self.geometry("600x600")
        self.configure(bg="#f7f7fa")

        self.student = Student()

        # --- Input Frame ---
        self.input_frame = ttk.LabelFrame(self, text="Student Information", padding=15)
        self.input_frame.pack(fill="x", padx=20, pady=10)

        # Interest
        ttk.Label(self.input_frame, text="Interest:").grid(row=0, column=0, sticky="w")
        self.interest_cb = ttk.Combobox(self.input_frame, values=[ 
            "3D modeling/animation", "Active sport", "Coding", "Drawing/Painting", "Digital Editing",
            "Fashion Design", "Fixing gadgets", "Graphic Design", "Journaling", "Learning new language",
            "Photography", "Programming", "Reading novels", "Science experiments", "Singing",
            "Solving puzzles", "Thrifting/Online Selling", "Traveling", "Video Gaming", "Vlogging", "Writing stories"
        ])
        self.interest_cb.grid(row=0, column=1, sticky="ew")

        # Favorite Subject
        ttk.Label(self.input_frame, text="Favorite Subject:").grid(row=1, column=0, sticky="w")
        self.fav_sub_cb = ttk.Combobox(self.input_frame, values=[
            "Computer", "English", "Mathematics", "Filipino", "MAPEH", "Science"
        ])
        self.fav_sub_cb.grid(row=1, column=1, sticky="ew")

        # Academic Performance
        ttk.Label(self.input_frame, text="Academic Performance:").grid(row=2, column=0, sticky="w")
        self.academic_cb = ttk.Combobox(self.input_frame, values=["good", "bad"])
        self.academic_cb.grid(row=2, column=1, sticky="ew")

        # First Goal
        ttk.Label(self.input_frame, text="First Goal:").grid(row=3, column=0, sticky="w")
        self.first_goal_cb = ttk.Combobox(self.input_frame, values=[
            "Undecided", "Accounting", "Architecture", "Biology", "Business Administration",
            "Chemical Engineering", "Civil Engineering", "Communication", "Computer Science", "Criminology",
            "Economics", "Education", "Electrical Engineering", "Environmental Science", "Finance",
            "Fine Arts", "Hospitality Management", "Information Technology", "Journalism", "Law",
            "Marketing", "Mechanical Engineering", "Medicine", "Nursing", "Pharmacy",
            "Political Science", "Psychology", "Public Administration", "Social Work", "Sociology", "Theater Arts"
        ])
        self.first_goal_cb.grid(row=3, column=1, sticky="ew")

        # Second Goal
        ttk.Label(self.input_frame, text="Second Goal:").grid(row=4, column=0, sticky="w")
        self.second_goal_cb = ttk.Combobox(self.input_frame, values=self.first_goal_cb["values"])
        self.second_goal_cb.grid(row=4, column=1, sticky="ew")

        # --- Submit Button ---
        self.submit_btn = ttk.Button(self, text="Get Advice", command=self.get_advice)
        self.submit_btn.pack(pady=10)

        restart_button = ttk.Button(self, text="Restart", command=self.restart_app)
        restart_button.pack(pady=5)

        # --- Output ---
        self.output_text = tk.Text(self, wrap="word", height=12, width=70, bg="#f0f0f0")
        self.output_text.pack(padx=20, pady=10)

    def restart_app(self):
        # Reset all input fields
        self.interest_cb.set('')
        self.fav_sub_cb.set('')
        self.academic_cb.set('')
        self.first_goal_cb.set('')
        self.second_goal_cb.set('')

        # Clear result text
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')

    def get_advice(self):
        # Get values from GUI and assign to Student instance
        self.student.interest = self.interest_cb.get()
        self.student.fav_sub = self.fav_sub_cb.get()
        self.student.academic_performance = self.academic_cb.get()
        self.student.first_goal = self.first_goal_cb.get()
        self.student.second_goal = self.second_goal_cb.get()

        # Validate input
        if not all([self.student.interest, self.student.fav_sub, self.student.academic_performance,
                    self.student.first_goal, self.student.second_goal]):
            messagebox.showwarning("Missing Information", "Please fill out all fields.")
            return

        # Get advice
        advisor = Advisor(self.student)
        advice = advisor.advise()

        # Display result
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, advice)


# --- Run the App ---
if __name__ == "__main__":
    app = AdvisorApp()
    app.mainloop()
