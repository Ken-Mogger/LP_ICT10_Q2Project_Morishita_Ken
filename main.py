from pyscript import document

def generate_score(event=None):
    name = document.getElementById("name").value
    grad_year = document.getElementById("grad_year").value

    quarter_one = float(document.getElementById("quarter_one").value)

    quarter_two = float(document.getElementById("quarter_two").value)
    quarter_three = float(document.getElementById("quarter_three").value)

    quarter_four = float(document.getElementById("quarter_four").value)

    final_score = (quarter_one + quarter_two + quarter_four + quarter_three) / 4

    gwaresult = f"""
    Student: {name}
    Year of Graduation: {grad_year}
    GWA of the Year: {round(final_score)}
    """

    

    document.getElementById("gwaresult").innerText = gwaresult