from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 300, 525
background_color = (255, 255, 255, 255)
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load fonts
RobotoSlab_Regular = ImageFont.truetype("Assats/RobotoSlab-Bold.ttf", 22)
RobotoSlab_Light = ImageFont.truetype("Assats/RobotoSlab-Regular.ttf", 16)

# Draw background image
background_image = Image.open("Assats/ecardbgfinal.png")
background_image = background_image.resize((width, height))
image.paste(background_image, (0, 0))

# Draw user photo
user_photo = Image.open("photo/743678.jpg")
user_photo = user_photo.resize((145, 145))
image.paste(user_photo, (75, 100))



# Draw name
name_text = "@NAME"
draw.text((100, 260), name_text, fill="rgb(0, 0, 0)", font=RobotoSlab_Regular)

# Draw details
details_text = [
    "Father Name: @Father_name",
    "Mother name: @Mother_name",
    "Tecnologi: @Tecnologi",
    "Seson: @Seson"
]
y_offset = 320
for text in details_text:
    draw.text((15, y_offset), text, fill="rgb(0, 0, 0)", font=RobotoSlab_Light)
    y_offset += 25

# Draw signature
signature_image = Image.open("Assats/pngwing.com.png")
signature_image = signature_image.resize((130, 50))
signature_image = signature_image.convert("RGBA")
image.paste(signature_image, (90, int(height * 0.84)),signature_image)

# Save or show the image
image.save("generated_image.pdf")
# image.show()  # Uncomment this line if you want to display the image
