import os


# def install_dependencies():
#     os.system("pip install prettytable")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# def check_role(role):
#     if role == "admin":
#         return True

#     return False


def enter_kembali():
    input("\nTekan enter untuk kembali...")


def enter_lanjut():
    input("\nTekan enter untuk lanjut...")
