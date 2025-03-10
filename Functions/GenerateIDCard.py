from PIL import Image, ImageDraw, ImageFont

card_background = Image.open('./Assets/CardTemplate.png')

draw = ImageDraw.Draw(card_background)

registration_date = "06082023"
registration_date_position = (1340, 130)
registration_date_font = ImageFont.truetype('./Assets/framd.ttf', size=80)

rank = "OVERSEER"
rank_position = (1390, 260)
rank_font = ImageFont.truetype('./Assets/framd.ttf', size=55)

paygrade = "O1"
paygrade_position = (1320, 385)
paygrade_font = ImageFont.truetype('./Assets/framd.ttf', size=80)

platoon = "1COY"
platoon_position = (1570, 385)
platoon_font = ImageFont.truetype('./Assets/framd.ttf', size=80)

identification_number = "0608-0-017"
identification_number_position = (1320, 520)
identification_number_font = ImageFont.truetype('./Assets/framd.ttf', size=80)

callsign = "Fox"
callsign_position = (250, 615)
callsign_font = ImageFont.truetype('./Assets/framd.ttf', size=80)

user_id = "730108671228510269"
user_id_position = (1110, 630)
user_id_font = ImageFont.truetype('./Assets/framd.ttf', size=55)

username = "developer_x"
username_position = (280, 720)
username_font = ImageFont.truetype('./Assets/framd.ttf', size=55)

roblox_username = "TomClancy247"
roblox_username_position = (1250, 725)
roblox_username_font = ImageFont.truetype('./Assets/framd.ttf', size=55)

signature = callsign
signature_position = (1100, 810)
signature_font = ImageFont.truetype('./Assets/signature_collection.ttf', size=110)

draw.text(registration_date_position, registration_date, fill=(0, 0, 0), font=registration_date_font, align='center')
draw.text(rank_position, rank, fill=(0, 0, 0), font=rank_font, align='center')
draw.text(paygrade_position, paygrade, fill=(0, 0, 0), font=paygrade_font, align='center')
draw.text(platoon_position, platoon, fill=(0, 0, 0), font=platoon_font, align='center')
draw.text(identification_number_position, identification_number, fill=(0, 0, 0), font=identification_number_font, align='center')
draw.text(callsign_position, callsign, fill=(0, 0, 0), font=callsign_font, align='center')
draw.text(user_id_position, user_id, fill=(0, 0, 0), font=user_id_font, align='center')
draw.text(username_position, username, fill=(0, 0, 0), font=username_font, align='center')
draw.text(roblox_username_position, roblox_username, fill=(0, 0, 0), font=roblox_username_font, align='center')
draw.text(signature_position, signature, fill=(0, 0, 0), font=signature_font, align='center')

def text_wrap(text,font,writing,max_width,max_height):
    lines = [[]]
    words = text.split()
    for word in words:
        # try putting this word in last line then measure
        lines[-1].append(word)
        (w,h) = writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]), font=font)
        if w > max_width: # too wide
            # take it back out, put it on the next line, then measure again
            lines.append([lines[-1].pop()])
            (w,h) = writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]), font=font)
            if h > max_height: # too high now, cannot fit this word in, so take out - add ellipses
                lines.pop()
                # try adding ellipses to last word fitting (i.e. without a space)
                lines[-1][-1] += '...'
                # keep checking that this doesn't make the textbox too wide, 
                # if so, cycle through previous words until the ellipses can fit
                while writing.multiline_textsize('\n'.join([' '.join(line) for line in lines]),font=font)[0] > max_width:
                    lines[-1].pop()
                    if lines[-1]:
                        lines[-1][-1] += '...'
                    else:
                        lines[-1].append('...')
                break
    return '\n'.join([' '.join(line) for line in lines])

desc_font = ImageFont.truetype('./Assets/framd.ttf', size=40)
desc = 'Fox, the TFC manager, adeptly enforces rules despite occasional deployment gaps. Proficient in BRM5 Marksmanship, they effortlessly hit 1500+ feet targets. Fox also stands as the creative mind behind the Conquerors Assistant bot, showcasing their multifaceted expertise.'
desc_wrapped = text_wrap(desc, desc_font, draw, 570, 447)
draw.text((626, 145), desc_wrapped, font=desc_font, fill=(0, 0, 0))

card_background.save('./Assets/card.png')