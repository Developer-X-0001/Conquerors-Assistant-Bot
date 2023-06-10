import discord

from easy_pil import Editor, Font, load_image

def generate_rank_card(member: discord.Member):
    background = Editor("Assets/wlcbg.jpg")
    profile = Editor("Assets/pfp.png").resize((150, 150)).circle_image()

    # To use users profile picture load it from url
    # using the load_image/load_image_async function
    profile_image = load_image(str(member.display_icon.url))
    profile = Editor(profile_image).resize((150, 150)).circle_image()


    # Fonts
    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=25, variant="regular")
    poppins_light = Font.poppins(size=20, variant="light")

    background.paste(profile, (325, 90))
    background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)
    background.text(
        (400, 260),
        "WELCOME",
        color="white",
        font=poppins,
        align="center",
        stroke_width=2,
    )
    background.text(
        (400, 325),
        "Shahriyar#9770",
        color="white",
        font=poppins_small,
        align="center",
    )
    background.text(
        (400, 360),
        "You are the 457th Member",
        color="#0BE7F5",
        font=poppins_small,
        align="center",
    )

    background.save(fp="./Functions/pfp.png")
    return discord.File(fp="./Functions/pfp.png")