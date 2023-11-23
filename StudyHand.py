
#Import StudyHand_func.py into this program
from StudyHand_func import display_question
from StudyHand_func import analyze_study_habits
from StudyHand_func import run_study_habits_quiz


print("Welcome to Study Bee! Let's get you started")
print("Let's learn about who you are")

name = input("Enter your first Name: ")

print("Hello " + name + "! Let's start by taking a quiz!")

# Defines a list of questions about learning styles
questions = [
    # Visual learning style questions
    'Do you learn best through images, charts, or diagrams? (Yes/No/Sometimes): ',
    'Are you more likely to remember information if it is presented visually? (Yes/No/Sometimes): ',
    'Do you find mind mapping or color-coding helpful when learning? (Yes/No/Sometimes): ',

    # Auditory learning style questions
    'Do you prefer learning through discussions and group activities? (Yes/No/Sometimes): ',
    'Do you remember information better when you hear it rather than reading or seeing it? (Yes/No/Sometimes): ',
    'Do you enjoy learning through lectures or audio materials? (Yes/No/Sometimes): ',

    # Kinesthetic learning style questions
    'Do you learn best by doing hands-on activities? (Yes/No/Sometimes): ',
    'Do you prefer studying while moving or being physically active? (Yes/No/Sometimes): ',
    'Do you find it helpful to take breaks and engage in physical activities during study sessions? (Yes/No/Sometimes): '
]

# Maps responses to numerical values
response_values = {'Yes': 1, 'No': 0, 'Sometimes': 0.5}

# Store scores for each learning style
learning_style_scores = {
    'Visual': 0,
    'Auditory': 0,
    'Kinesthetic': 0
}

# Asks the questions and calculates scores for each learning style
for index, question in enumerate(questions):
    answer = input(question)
    response = answer.capitalize()  # Capitalize the response for uniformity
    if response in response_values:
        response_score = response_values[response]
        # Determine the learning style based on question grouping
        if index < 3:
            learning_style_scores['Visual'] += response_score
        elif 3 <= index < 6:
            learning_style_scores['Auditory'] += response_score
        else:
            learning_style_scores['Kinesthetic'] += response_score

# Display scores for each learning style
print("\nThank you for completing the quiz! Let's see the results!\n")
for style, score in learning_style_scores.items():
    print(f"Your score for {style} learning style is: {score}")

# Determine the dominant learning style based on the highest score
dominant_style = max(learning_style_scores, key=learning_style_scores.get)
print(f"\nYour dominant learning style is: {dominant_style}")

if dominant_style == "Visual":
    print("\nBased on your results, you should consider learning through visual materials.")
    print("\nVisual materials include sketching diagrams abd color-coding your notes to organize information.")
    print("It would also be helpful to study with flashcards while using images or watching educational videos.")
    
elif dominant_style == "Auditory":
    print("\nBased on your results, you should consider learning through audio materials.")
    print("\nAudio materials include lectures and audio materials such as podcasts and podcast episodes.")
    print("It would also be helpful to study with flashcards while using audio materials.")
    
elif dominant_style == "Kinesthetic":
    print("\nBased on your results, you should consider learning through hands-on activities.")
    print("\nHands-on activities include physical activities such as walking, jogging, and running.")
    print("It would also be helpful to study with flashcards while using physical activities.")
    
print("\Redirecting to the main menu...")

# Redirect to the main menu
main_menu = input("\nPress Enter to return to the main menu...")
main_menu()

def study_methods():
    print("\nPopular Study Methods:")
    print("1. Pomodoro Technique")
    print("2. Feynman Technique")
    print("3. Cornell Method")
    print("4. Mind Mapping")
    print("5. SQ3R Method")

    method_choice = input("Choose a study method (1-5): ")
    # Add code here to implement functionality for each study method

def main_menu():
    print("\nMain Menu:")
    print("1. Study")
    print("2. Edit Profile")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        study_methods()
    elif choice == '2':
        print("Profile editing functionality will be implemented here.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main_menu()

# Existing code for login function and quiz functionality remains unchanged...

def study_methods():
    print("\nPopular Study Methods:")
    print("1. Pomodoro Technique")
    print("2. Feynman Technique")
    print("3. Cornell Method")
    print("4. Mind Mapping")
    print("5. SQ3R Method")

    method_choice = input("Choose a study method (1-5): ")
    # Add code here to implement functionality for each study method

def study_tab():
    print("\nWelcome to the Study Tab!")
    print("You have entered the study area.")
    study_methods()

def main_menu():
    print("\nMain Menu:")
    print("1. Study")
    print("2. Edit Profile")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        study_tab()
    elif choice == '2':
        print("Profile editing functionality will be implemented here.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main_menu()

# Existing code for other functionalities remains unchanged...
