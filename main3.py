from pyscript import document, display

def generate_info(event):
    selected_club = document.querySelector("select").value

    club_info = {
    "Social Sciences Club": """
    Social Science Club!
    Description: Study the Social Sciences and join competitions related to such!
    Meeting Time: 4:00 PM
    Location: Room 607
    Advisor: Mr. Teddy
    Number of Members: 30
    Category: Academic
    """,
    
    "Journalism Club": """
    Journalism Club!
    Description: Join the school newspaper and write!
     Meeting Time: 4:00 PM
    Location: Room 609
    Advisor: Ms. Batty
    Number of Members: 25
    Category: Academic
    """,
    
    "Sports Varsity": """
    Sports Varsity!
    Description: Become part of one of our prestigious teams in volleyball, basketball, and badminton! 
     Meeting Time: 4:00 PM
    Location: Room 611
    Advisor: Mr. Taurus
    Number of Members: 30
    Category: Academic
    """,
    
    "STEM Club": """
    STEM Club!
    Description: Learn more about the world around us, while employing the use of technology!
    Meeting Time: 4:00 PM
    Location: Room 613
    Advisor: Ms. Tap
    Number of Members: 30
    Category: Academic
    """
    }

    info_text = club_info.get(selected_club, "Club not found.")
    document.getElementById("info").innerText = info_text

