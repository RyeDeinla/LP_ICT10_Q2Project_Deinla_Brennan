from pyscript import document, display


def general_weighted_average(e):
    # Get input values
    sci = float(document.getElementById("science").value)
    eng = float(document.getElementById("english").value)
    ict = float(document.getElementById("ict").value)
    math = float(document.getElementById("math").value)
    fil = float(document.getElementById("filipino").value)
    pe = float(document.getElementById("physicaleducation").value)

    customer_firstname = document.getElementById("firstname").value
    customer_lastname = document.getElementById("lastname").value
    
    # Calculate total and divide by 2 to get the GWA
    generalweightedaverage = (sci + eng + ict + math + fil + pe)/6
    
    # Display the GWA
    display(f"Good day, {customer_firstname} {customer_lastname}!", target="fullname")
    display(f"Your General Weighted Average is: {generalweightedaverage:.2f} ", target="gwa")