import os
from prosopygnosia.instagram_functions import instagram_download
from prosopygnosia.artificial_intelligence import ai_with_cv

if __name__ == '__main__':
    def menu():
        os.system('clear')
        print("Welcome to ProsoPygnosia, please select an option")
        print("\t1 - Download and train Instagram Dataset")
        print("\t2 - Select your own dataset")
        print("\t3 - Open Webcam Recognition")
        print("\t8 - Help")
        print("\t9 - Exit")


    while True:
        menu()
        optionMenu = input("Please, insert your option >> ")
        if optionMenu == "1":
            print("")
            os.system('clear')
            instagram_download.main()
        elif optionMenu == "2":
            print("")
            # Not implemented yet
            os.system('clear')
            session_name = '_' + input("Please, select a name for identify the session relationed with this dataset: ")
            path = input("Please introduce the path of the dataset or drop it here: ")
            dest = './profiledata' + session_name
            if os.path.isdir(dest):
                print("Not implemented yet")
                # cargar sesión iniciada
            else:
                instagram_download.copy_images_from_path(path, dest)
                instagram_download.clean_and_crop(os.path.abspath(dest))
        elif optionMenu == "3":
            print("")
            os.system('clear')
            ai_with_cv.cam_recognition()
        elif optionMenu == "8":
            os.system('clear')
            input("Welcome to the help section. \n You must teach this program which of your friends is relationed with"
                  " which of the photos. For this you have two options (option 1 and 2 on the program).\n\n\n"
                  "1. With your Instagram account the app will do this automatically.\n\n"
                  "2. With a path of the dataset you could improve the accurate of this program, this dataset must"
                  " follow this folder tree: dataset >> *username1* *username2* *username3* .... >> *jpg\n\n"
                  "3. Once that the program has learnt from the dataset you could choose this option for recognize "
                  "people from the cam.\n"
                  "IMPORTANT. When you select this option you must press the \"q\" key for exit the WHOLE program."
                  "8. This help menu.\n\n"
                  "9. For quitting the program and go back to your prompt.\n\n\n"
                  "Please, press return to go back to the main menu.")
        elif optionMenu == "9":
            os.system('clear')
            break
        else:
            print("")
            input("Please, choose one of the options showed below. Press return to continue.")
