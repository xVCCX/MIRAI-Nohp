import random
import os
from tabulate import tabulate

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("Colorama tidak terinstal. Warna tidak akan tersedia.")
    class Dummy:
        def __getattr__(self, name):
            return ''
    Fore = Back = Style = Dummy()

BANNER_WIDTH = 50
TABLE_WIDTH = BANNER_WIDTH - 4

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.CYAN + Style.BRIGHT}{'=' * BANNER_WIDTH}
{Fore.YELLOW + Style.BRIGHT}{'M I R A I - Auto Generate Phone Number'.center(BANNER_WIDTH)}
{Fore.MAGENTA + Style.BRIGHT}{'Versi 1.0 - Automation Project'.center(BANNER_WIDTH)}
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⣼⡿⠟⠛⠉⠉⠉⠁⠄⠄⠄⠁⠈⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⠄⠈⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠁⠄⠛⠻⠿⢿⣿⣿⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⠿⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠿⣿
{Fore.CYAN}⣿⣿⠋⠄⠄⠄⣀⣤⡤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈
{Fore.CYAN}⣿⣿⣧⠄⠄⢊⣵⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣶⣶⣶⣶⣶⣶⣶⣤⣤⡀
{Fore.CYAN}⣿⣿⣿⣷⣄⠞⢡⡟⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣟⠻
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⡌⠄⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣷
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⣿⠆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡟⣿⡿⡏⠻⣇⠈⠙
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠐⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⢻⠃⠄⠄⠈⠄⠄
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⣾⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠄⠄⠄⠄⠄⢀⣠
{Fore.CYAN}⣿⣿⣿⣿⣿⡏⢀⠄⠄⠄⠄⠄⠄⣸⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿⣿⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣘⣻⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⠁⡜⠄⠄⠄⠄⠄⠠⠿⠿⠭⢽⣧⣀⠄⠄⠄⢀⡤⠄⠄⠄⠙⠛⠿⠷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⢀⡇⠄⠄⠄⠄⠄⣀⠤⡄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⠶⠦⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⡇⢸⡇⠄⠄⠄⠄⢀⣻⣧⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⣿⡿⣷⣳⣷⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣷⣼⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⢟⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠈⢿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠙⢿⡿⠄⠄⡀⠄⠄⠄⣠⣾⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⡇⠄⡄⠄⠄⣀⡴⣖⣶⣴⣶⡆⠄⠄⠄⠄⣾⠿⠿⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⣿⠄⢧⣤⣾⣫⣾⣿⣿⠟⠛⣾⡦⠄⢰⣶⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠻⣿⣿⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⣿⣫⣾⡿⣫⣾⣿⣿⣿⢽⣿⡶⣿⡧⢀⣷⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⢠⠄⠄⠄⠄⡀⠄⣰⣶⣶⣦⣄⠄⠄⠈⠻⣿⣿⣿
{Fore.CYAN}⣿⣿⣿⣿⣿⢿⣿⣿⣾⣿⣿⣿⣿⣾⣿⣷⣇⣿⡇⢸⣾⣿⣻⠃⢀⠄⠄⠄⠄⢀⣀⣸⠄⠄⢰⠄⡇⠄⣿⣿⣿⣿⣿⣷⣄⠄⠄⠈⢿⣿
{Fore.CYAN}⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⢹⢯⣱⣟⣯⠁⣷⣿⣿⣿⠠⣿⣿⣿⣿⣿⡿⢫⣷⡆⠄⣿⢀⠇⠄⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠹
{Fore.CYAN}⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣐⠿⢿⣿⡷⣾⣿⣿⣿⢿⢳⣿⣿⣿⣿⣿⣶⢻⣽⣷⣸⣿⢸⠄⣼⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄
{Fore.CYAN + Style.BRIGHT}{'=' * BANNER_WIDTH}
    """
    print(banner)

def print_menu(options):
    table = [[f"{Fore.GREEN}{i}", f"{Fore.YELLOW}{option}"] for i, option in enumerate(options, 1)]
    table.append([f"{Fore.RED}0", f"{Fore.RED}Kembali"])
    table_string = tabulate(table, headers=[f"{Fore.CYAN}No.", f"{Fore.CYAN}Pilihan"], tablefmt="fancy_grid")
    
    formatted_table = '\n'.join([line[:TABLE_WIDTH] for line in table_string.split('\n')])
    padding = ' ' * 2
    formatted_table = '\n'.join([f"{padding}{line}{padding}" for line in formatted_table.split('\n')])
    
    print(formatted_table)

def get_user_choice(prompt, options):
    while True:
        try:
            choice = get_numeric_input(prompt)
            if 0 <= choice <= len(options):
                return choice
            print(Fore.RED + f"Error: Pilihan harus antara 0 dan {len(options)}.")
        except ValueError as e:
            print(Fore.RED + f"Error: {str(e)}")

def get_numeric_input(prompt):
    while True:
        try:
            value = input(Fore.CYAN + prompt)
            if not value.strip():
                raise ValueError("Input tidak boleh kosong.")
            return int(value)
        except ValueError:
            raise ValueError("Mohon masukkan angka yang valid.")

providers = {
    "Telkomsel": ["0811", "0812", "0813", "0821", "0822", "0823", "0851", "0852", "0853"],
    "Indosat Ooredoo": ["0814", "0815", "0816", "0855", "0856", "0857", "0858"],
    "XL Axiata": ["0817", "0818", "0819", "0859", "0877", "0878"],
    "Tri": ["0895", "0896", "0897", "0898", "0899"],
    "Smartfren": ["0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"],
    "by.U": ["0851", "0852", "0853"],
    "Axis": ["0838", "0831", "0832", "0833"]
}

hlr_codes = {
    "Jabodetabek": list(range(10, 15)),
    "Jawa Barat": list(range(15, 33)),
    "Jawa Tengah": list(range(33, 39)),
    "Jawa Timur": list(range(39, 44)),
    "Bali": list(range(44, 48)),
    "Kalimantan": list(range(48, 60)),
    "Sumatera bagian utara": list(range(60, 69)),
    "Sumatera bagian tengah": list(range(69, 75)),
    "Sumatera bagian selatan": list(range(75, 87)),
    "Sulawesi": list(range(87, 97)),
    "Papua dan Maluku": list(range(97, 100))
}

def generate_phone_numbers(prefix, hlr_area, count):
    numbers = set()
    while len(numbers) < count:
        hlr = str(random.choice(hlr_codes[hlr_area])).zfill(2)
        random_digits = ''.join(random.choices('0123456789', k=6))
        number = f"{prefix}{hlr}{random_digits}"
        numbers.add(number)
    return list(numbers)

def save_to_file(numbers, filename):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu(["Generate nomor telepon", "Lihat daftar provider", "Lihat daftar area HLR"])
        choice = get_user_choice("Masukkan pilihan Anda: ", ["Generate", "Provider", "HLR"])

        if choice == 0:
            print(Fore.YELLOW + "Terima kasih telah menggunakan Generator Nomor Telepon. Sampai jumpa!")
            break
        elif choice == 1:
            clear_screen()
            print_banner()
            print_menu(list(providers.keys()))
            provider_choice = get_user_choice("Pilih provider: ", list(providers.keys()))
            if provider_choice == 0:
                continue

            provider = list(providers.keys())[provider_choice-1]
            
            clear_screen()
            print_banner()
            print_menu(providers[provider])
            prefix_choice = get_user_choice("Pilih awalan: ", providers[provider])
            if prefix_choice == 0:
                continue

            prefix = providers[provider][prefix_choice-1]

            clear_screen()
            print_banner()
            print_menu(list(hlr_codes.keys()))
            hlr_choice = get_user_choice("Pilih area HLR: ", list(hlr_codes.keys()))
            if hlr_choice == 0:
                continue

            hlr_area = list(hlr_codes.keys())[hlr_choice-1]

            while True:
                try:
                    count = get_numeric_input("Masukkan jumlah nomor telepon yang ingin di-generate: ")
                    if count <= 0:
                        raise ValueError("Jumlah harus lebih besar dari 0.")
                    break
                except ValueError as e:
                    print(Fore.RED + f"Error: {str(e)}")

            generated_numbers = generate_phone_numbers(prefix, hlr_area, count)
            filename = f"{provider.lower().replace(' ', '_')}_{prefix}_numbers.txt"
            save_to_file(generated_numbers, filename)

            print(Fore.GREEN + f"{count} nomor telepon untuk {provider} dengan awalan {prefix} di area {hlr_area} telah di-generate dan disimpan ke {filename}")
            input(Fore.YELLOW + "Tekan Enter untuk melanjutkan...")
        elif choice == 2:
            clear_screen()
            print_banner()
            print(Fore.YELLOW + "Provider dan Awalan yang Tersedia:".center(BANNER_WIDTH))
            table = [[Fore.GREEN + provider, Fore.CYAN + ', '.join(prefixes)] for provider, prefixes in providers.items()]
            print(tabulate(table, headers=[f"{Fore.MAGENTA}Provider", f"{Fore.MAGENTA}Awalan"], tablefmt="fancy_grid", maxcolwidths=[20, TABLE_WIDTH-25]))
            input(Fore.YELLOW + "Tekan Enter untuk melanjutkan...".center(BANNER_WIDTH))
        elif choice == 3:
            clear_screen()
            print_banner()
            print(Fore.YELLOW + "Area HLR yang Tersedia:".center(BANNER_WIDTH))
            table = [[Fore.GREEN + area, Fore.CYAN + f"{min(codes)}-{max(codes)}"] for area, codes in hlr_codes.items()]
            print(tabulate(table, headers=[f"{Fore.MAGENTA}Area", f"{Fore.MAGENTA}Kode HLR"], tablefmt="fancy_grid", maxcolwidths=[30, TABLE_WIDTH-35]))
            input(Fore.YELLOW + "Tekan Enter untuk melanjutkan...".center(BANNER_WIDTH))

if __name__ == "__main__":
    main()