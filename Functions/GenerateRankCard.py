import discord

from easy_pil import Canvas, Editor, Font, Text, font, load_image

def generate_rank_card(user: discord.Member):

    background = Editor(Canvas((900, 270)))
    # profile = Editor("assets/pfp.png").resize((200, 200)).circle_image()

    # For profile to use users profile picture load it from url using the load_image/load_image_async function
    profile_image = load_image(str(user.avatar.url))
    profile = Editor(profile_image).resize((200, 200)).circle_image()


    # Fonts to use with different size
    poppins_big = Font.poppins(variant="bold", size=50)
    poppins_mediam = Font.poppins(variant="bold", size=40)
    poppins_regular = Font.poppins(variant="regular", size=30)
    poppins_thin = Font.poppins(variant="light", size=18)

    card_left_shape = [(0, 0), (0, 270), (330, 270), (260, 0)]

    background.rectangle((0,0), width=900, height=270, color="#23272a")
    background.polygon(card_left_shape, "#2C2F33")
    background.paste(profile, (40, 35))
    background.ellipse((40, 35), 200, 200, outline="#d7b369", stroke_width=3)
    background.text((600, 30), "WELCOME", font=poppins_big, color="#d7b369", align="center")
    background.text(
        (600, 80), user.name, font=poppins_regular, color="white", align="center"
    )
    background.text(
        (600, 130), "YOU ARE MEMBER", font=poppins_mediam, color="#d7b369", align="center"
    )
    background.text(
        (600, 170), f"NO. {user.guild.member_count}", font=poppins_regular, color="white", align="center"
    )
    background.text(
        (620, 235),
        "THANK YOU FOR JOINING. HOPE YOU WILL ENJOY YOUR STAY",
        font=poppins_thin,
        color="white",
        align="center",
    )

    background.save(fp="./Functions/pfp.png")
    return discord.File(fp="./Functions/pfp.png")