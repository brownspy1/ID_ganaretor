import pyfiglet
import imgkit
import cv2

# confrigrations
path_wkthmltoimage = r'.\kit\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)

options = {'dpi': 365, 'margin-top': '0in', 'margin-bottom': '0in', 'margin-right': '0in', 'margin-left': '0in',
           'page-size': 'A8', "orientation": "Portrait", 'disable-smart-shrinking': ''}

options = {'enable-local-file-access': None, "--quality": 100}


class Bpi_Id_ganaretor:
    print('''╔╗╔╗╔╗    ╔╗                     ╔════╗          ╔═══╗             ╔═══╗                      ╔╗        ╔╗
║║║║║║    ║║                     ║╔╗╔╗║          ╚╗╔╗║             ║╔═╗║                     ╔╝╚╗       ║║
║║║║║║╔══╗║║ ╔══╗╔══╗╔╗╔╗╔══╗    ╚╝║║╚╝╔══╗    ╔╗ ║║║║             ║║ ╚╝╔══╗ ╔═╗ ╔══╗ ╔═╗╔══╗╚╗╔╝╔══╗╔═╗║║
║╚╝╚╝║║╔╗║║║ ║╔═╝║╔╗║║╚╝║║╔╗║      ║║  ║╔╗║    ╠╣ ║║║║    ╔═══╗    ║║╔═╗╚ ╗║ ║╔╗╗╚ ╗║ ║╔╝║╔╗║ ║║ ║╔╗║║╔╝╚╝
╚╗╔╗╔╝║║═╣║╚╗║╚═╗║╚╝║║║║║║║═╣     ╔╝╚╗ ║╚╝║    ║║╔╝╚╝║    ╚═══╝    ║╚╩═║║╚╝╚╗║║║║║╚╝╚╗║║ ║║═╣ ║╚╗║╚╝║║║ ╔╗
 ╚╝╚╝ ╚══╝╚═╝╚══╝╚══╝╚╩╩╝╚══╝     ╚══╝ ╚══╝    ╚╝╚═══╝             ╚═══╝╚═══╝╚╝╚╝╚═══╝╚╝ ╚══╝ ╚═╝╚══╝╚╝ ╚╝
                                                                                                          
                                                                                                          
''')

    def __init__(self, name, father_name, mother_name, seson, tecnologi, class_roll, bord_roll, rag_num):
        self.Name = name
        self.Father_name = father_name
        self.Mother_name = mother_name
        self.Seson = seson
        self.Tecnologi = tecnologi
        self.ClassRoll = class_roll
        self.Bord_roll = bord_roll
        self.Rag_num = rag_num

    def Ganaret_id_simpal(self):
        html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @font-face {
            font-family: nildoriah;
            src: url('LiNiladriRongtuliUnicode-Regular.ttf');
        }
        @font-face {
            font-family: kalpurus;
            src: url('kalpurush.ttf');
        }
        *
        {
            margin: 0;
            padding: 0;
        }
        .container
        {
            height: 100vh;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-around;
            flex-wrap: wrap;
            box-sizing: border-box;
            flex-direction: row;
        }
        .font
        {
            height: 375px;
            width: 225px;
            position: relative;
            border-radius: 10px;
            background-image: url('ecardbgfinal.png');
            background-size: 225px 375px;
            background-repeat: no-repeat;
        }
        .edetails{
            position: absolute;
            top: 240px;
            line-height: 15px;
            left: 15px;
            text-transform: capitalize;
            font-family: kalpurus;
            font-size: 12px;
            text-emphasis: spacing;
            margin-left: 5px;
        }
        .top img
        {
            height: 90px;
            width: 90px;
            background-color: #d3760c;
            border-radius: 99px;
            position: absolute;
            top: 70px;
            left: 65px;
            object-fit: content;
            border: 4px solid rgba(255 , 255 , 255 , .2);
        }
        .ename{
            position: absolute;
            font-family: nildoriah;
            top: 170px;
            left: 65px;
            color: rgb(0, 0, 0);
            font-size: 22px;
        }
        .signature{
            position: absolute;
            top: 78%;
            height: 80px;
            width: 160px;
        }
        .signature img{
            height: 30px;
            width: 90px;
            margin: 30px 0 0 65px;
            border-radius: 7px;
        }
    </style>
</head>
<body>
    <!-- font id design -->
    <div class="container">
        <div class="padding">
            <div class="font">
                <div class="top">
                    <img src="./photo/@Bord_roll.jpg" alt="user_photo">
                </div>
                <div class="">
                    <div class="ename">
                        <p class="p1"><b>@NAME</b></p>
                    </div>
                    <div class="edetails">
                        <p><b>পিতার নাম : @Father_name</b></p>
                        <p><b>মাতার নাম : @Mother_name</b></p>
                        <p><b>টেকনোলজি : @Tecnologi</b></p>
                        <p><b>সেশন : @Seson</b></p>
                    </div>
                    <div class="signature">
                        <img src="./Assats/pngwing.com.png" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
        html = html.replace("@NAME", self.Name)
        html = html.replace("@Father_name", self.Father_name)
        html = html.replace("@Mother_name", self.Mother_name)
        html = html.replace("@Seson", self.Seson)
        html = html.replace("@Tecnologi", self.Tecnologi)
        html = html.replace("@ClassRoll", str(self.ClassRoll))
        html = html.replace("@Bord_roll", str(self.Bord_roll))
        html = html.replace("@Rag_num", str(self.Rag_num))
        img_file = f'{self.Name}_{self.Bord_roll}.jpg'
        imgkit.from_string(html, img_file, config=config, options=options)
        image = cv2.imread(img_file)
        print("Congratulations! Your id is save to your storge!")


def main():
    while True:

        Choise = input("\n1.V1[Simpal]"
                       "\n2.V2[Modarn + Qr code]"
                       "\n3.V3[With online profile]"
                       "\nEnter your choice (1-3):")
        if Choise == "1":
            # Name = input("Enter your Name:")
            # Father_name = input("Enter your Father Name :")
            # Mother_name = input("Enter your Mother Name :")
            # Seson = input("Seson:")
            # Tecnologi = input("Tecnologi:")
            # ClassRoll = int(input("ClassRoll:"))
            # Bord_roll = int(input("Bord_roll:"))
            # Rag_num = int(input("Rag Number:"))
            #constant valu for testing
            Name = "মোঃ মেহেদী"
            Father_name = "মোঃ মোয়াজ্জেম বিশ্বাস"
            Mother_name = "মোসাঃ কাজল রেখা"
            Seson = "২২-২৩"
            Tecnologi = "কম্পিউটার"
            ClassRoll = "২২৩৬৭৮"
            Bord_roll = "৭৪৩৬৭৮"
            Rag_num = "১৫০২২৬৮৬৭৪"

            detail = Bpi_Id_ganaretor(Name,
                                      Father_name,
                                      Mother_name,
                                      Seson,
                                      Tecnologi,
                                      ClassRoll,
                                      Bord_roll,
                                      Rag_num)

            detail.Ganaret_id_simpal()

        elif Choise == "2":
            banar = pyfiglet.figlet_format("Undar constracson!")
            print(banar)
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
