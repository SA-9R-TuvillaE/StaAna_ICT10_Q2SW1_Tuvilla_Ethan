from pyscript import document, when

CLUB_MEMBERS = [
    "Allison Burgers",
    "Ladis Washerum",
    "Max Imumoccupancy120",
    "Bucky Barnes",
    "Steve Rogers",
    "Tony Stark",
    "Clark Kent",
    "Bruce Wayne",
    "Dick Grayson",
    "Jason Todd",
    "Tim Drake",
    "Peter Quill",
    "Xander Espinosa",
    "Doctor Doom",
    "Peter Parker",
]


@when("click", "#submit-btn")
def check_candidate(event):
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()
    candidate = f"{first_name} {last_name}".title()

    is_member = candidate in CLUB_MEMBERS

    messages = (
        f"Alas, {candidate}, thy name is not inscribed upon the scroll.",
        f"Huzzah, {candidate}! Thou art now sworn into the Order of Holy Knights.",
    )
    document.getElementById("output").textContent = messages[is_member]