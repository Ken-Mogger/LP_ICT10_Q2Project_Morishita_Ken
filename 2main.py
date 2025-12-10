from pyscript import document

def generate_description(event=None):
    club = document.getElementById("clubOption").value
    info_box = document.getElementById("see_club")

    if club == "Arts Club":
        info_text = (
            "A creative club exploring drawing, painting, and digital art."
        )


    elif club == "Robotics Club":
        info_text = (
            "Members design and build robots while learning basic programming."
        )

    elif club == "Band Club":
        info_text = (
            "Students practice instruments and perform musical pieces together."
        )

    else:
        info_text = "No information available."
    

    info_box.innerHTML = f"Description: {info_text}"