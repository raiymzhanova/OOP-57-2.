from colorama import init, Fore, Style

init()


print(Fore.RED + "Это красный текст." + Style.RESET_ALL)
print(Fore.GREEN + "Это зелёный текст." + Style.RESET_ALL)
print(Fore.YELLOW + "Это жёлтый текст." + Style.RESET_ALL)
print(Fore.BLUE + "Это синий текст.")

print(Style.RESET_ALL)
print("Это обычный текст без цвета.")