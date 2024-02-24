import pyfiglet
import Font_side
import Backsid
import hashr
import Pymarg
import csv

print('''╔╗╔╗╔╗    ╔╗                     ╔════╗          ╔═══╗             ╔═══╗                      ╔╗        ╔╗
║║║║║║    ║║                     ║╔╗╔╗║          ╚╗╔╗║             ║╔═╗║                     ╔╝╚╗       ║║
║║║║║║╔══╗║║ ╔══╗╔══╗╔╗╔╗╔══╗    ╚╝║║╚╝╔══╗    ╔╗ ║║║║             ║║ ╚╝╔══╗ ╔═╗ ╔══╗ ╔═╗╔══╗╚╗╔╝╔══╗╔═╗║║
║╚╝╚╝║║╔╗║║║ ║╔═╝║╔╗║║╚╝║║╔╗║      ║║  ║╔╗║    ╠╣ ║║║║    ╔═══╗    ║║╔═╗╚ ╗║ ║╔╗╗╚ ╗║ ║╔╝║╔╗║ ║║ ║╔╗║║╔╝╚╝
╚╗╔╗╔╝║║═╣║╚╗║╚═╗║╚╝║║║║║║║═╣     ╔╝╚╗ ║╚╝║    ║║╔╝╚╝║    ╚═══╝    ║╚╩═║║╚╝╚╗║║║║║╚╝╚╗║║ ║║═╣ ║╚╗║╚╝║║║ ╔╗
 ╚╝╚╝ ╚══╝╚═╝╚══╝╚══╝╚╩╩╝╚══╝     ╚══╝ ╚══╝    ╚╝╚═══╝             ╚═══╝╚═══╝╚╝╚╝╚═══╝╚╝ ╚══╝ ╚═╝╚══╝╚╝ ╚╝                                                                                          
''')


# Function to save data to CSV
def save_to_csv(Name, Father_name, Mother_name, Seson, Tecnologi, ClassRoll, Bord_roll, Rag_num, Photo):
    with open('student_data.csv', 'w', newline='', encoding='utf-8') as file:  # Use 'w' mode to overwrite the file
        fieldnames = ['Name', 'Father Name', 'Mother Name', 'Session', 'Tecnologi', 'Class roll',
                      'Bord Roll', 'Rag Number', 'Photo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        writer.writerow({
            'Bord Roll': Bord_roll, 'Name': Name, 'Father Name': Father_name,
            'Mother Name': Mother_name, 'Session': Seson, 'Tecnologi': Tecnologi,
            'Class roll': ClassRoll, 'Rag Number': Rag_num, 'Photo': Photo
        })
def Bangla():
    get_data = input("1.Creat ID card"
                     "\n2.Marg ID in One PDF file"
                     "\nEnter your choice (1-2):")
    if get_data == "1":
        print("Please write all in Bengali")
        # Name = input("Enter your Name:")
        # Father_name = input("Enter your Father Name :")
        # Mother_name = input("Enter your Mother Name :")
        # Seson = input("Seson:")
        # Tecnologi = input("Tecnologi:")
        # ClassRoll = int(input("ClassRoll:"))
        # Bord_roll = int(input("Bord_roll:"))
        # Rag_num = int(input("Rag Number:"))
        # _Photo = input("Entar your Bord roll [In English]")
        # image = f"photo/{_Photo}.jpg"
        # Photo = hashr.image_to_url(image)
        # Font_side.make_png_id_bangla(Name, Father_name, Mother_name, Seson, Tecnologi, Bord_roll, Photo)
        # Backsid.make_png_id_bangla(ClassRoll, Bord_roll, Rag_num)
        # print("Congratulations! your id generated successfully!")

        # # init value for testing

        Name = "মোঃ মেহেদী"
        Father_name = "মোঃ মোয়াজ্জেম বিশ্বাস"
        Mother_name = "মোসাঃ কাজল রেখা"
        Seson = "২২-২৩"
        Tecnologi = "কম্পিউটার"
        ClassRoll = "২২৩৬৭৮"
        Bord_roll = "৭৪৩৬৭৮"
        Rag_num = "১৫০২২৬৮৬৭৪"
        _Photo = "743678"
        image = f"photo/{_Photo}.jpg"
        Photo = hashr.image_to_url(image)
        Font_side.make_png_id_bangla(Name, Father_name, Mother_name, Seson, Tecnologi, Bord_roll, Photo)
        Backsid.make_png_id_bangla(ClassRoll, Bord_roll, Rag_num)
        print("Congratulations! your id generated successfully!")
    elif get_data == "2":
        Bord_roll = input("Your Bord Roll [in Bangla]: ")
        Pymarg.marge(f"Id Card/font_{Bord_roll}.pdf", f"Id Card/back_{Bord_roll}.pdf", Bord_roll)
def English():
    get_data = input("1.Creat ID card"
                     "\n2.Marg ID in One PDF file"
                     "\nEnter your choice (1-2):")
    if get_data == "1":
        print("Please write all in English")
        # Name = input("Name:")
        # Father_name = input("Father Name :")
        # Mother_name = input("Mother Name :")
        # Seson = input("Seson:")
        # Tecnologi = input("Tecnologi:")
        # ClassRoll = int(input("ClassRoll:"))
        # Bord_roll = int(input("Bord_roll:"))
        # Rag_num = int(input("Rag Number:"))
        # image = f"photo/{Bord_roll}.jpg"
        # Photo = hashr.image_to_url(image)
        # Font_side.make_png_id_english(Name, Father_name, Mother_name, Seson, Tecnologi, Bord_roll, Photo)
        # Backsid.make_png_id_english(ClassRoll, Bord_roll, Rag_num)
        # save_to_csv(Name, Father_name, Mother_name, Seson, Tecnologi, ClassRoll, Bord_roll, Rag_num, Photo)
        # print(f"Congratulations! your id generated successfully! check {image}")

        # # init value for testing
        Name = "M.Mahadi"
        Father_name = "M.Mozzem Bissas"
        Mother_name = "MST.Kazol Rekha"
        Seson = "2022-23"
        Tecnologi = "CST"
        ClassRoll = "2285133"
        Bord_roll = "743678"
        Rag_num = "1532982354"
        image = f"photo/{Bord_roll}.jpg"
        Photo = hashr.image_to_url(image)
        Font_side.make_png_id_english(Name, Father_name, Mother_name, Seson, Tecnologi, Bord_roll, Photo)
        Backsid.make_png_id_english(ClassRoll, Bord_roll, Rag_num)
        save_to_csv(Name, Father_name, Mother_name, Seson, Tecnologi, ClassRoll, Bord_roll, Rag_num, Photo)
        print("Congratulations! your id generated successfully!")
    elif get_data == "2":
        Bord_roll = input("Your Bord Roll [in Bangla]: ")
        Pymarg.marge(f"Id Card/font_{Bord_roll}.pdf", f"Id Card/back_{Bord_roll}.pdf", Bord_roll)

def main():
    while True:
        Choise = input("\n1.Bangla ID Card"
                       "\n2.English ID Card"
                       "\n3.Both ID Card"
                       "\n4.Exit:"
                       "\nEnter your choice (1-4):")
        if Choise == "1":
            banar = pyfiglet.figlet_format("BANGLA ID")
            print(banar)
            Bangla()

        elif Choise == "2":
            banar = pyfiglet.figlet_format("ENGLISH ID")
            print(banar)
            English()
        elif Choise == "3":
            banar = pyfiglet.figlet_format("Comming!")
            print(banar)
        elif Choise == "4":
            Choise = input("Do you want to exit? [Y/N]:")
            if Choise == "Y" or Choise == "y":
                break
            else:
                main()


if __name__ == "__main__":
    main()
