import speedtest
import threading
import time
from colorama import init, Fore, Style

init(autoreset=True)

loading = False


def spinner():
    chars = "|/-\\"
    i = 0
    while loading:
        print(f"\r {Fore.CYAN}Measuring speed... {chars[i % len(chars)]}", end="", flush=True)
        time.sleep(0.1)
        i += 1


def color_speed(speed):
    if speed < 20:
        return Fore.RED
    elif speed < 100:
        return Fore.YELLOW
    return Fore.GREEN


try:
    loading = True
    thread = threading.Thread(target=spinner)
    thread.start()

    st = speedtest.Speedtest()
    st.get_best_server()

    ping = st.results.ping
    server = st.results.server

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    loading = False
    thread.join()

    print(f"\r{Fore.CYAN}{' ' * 50}\r", end="")

    print(f"{Fore.CYAN}{Style.BRIGHT}=== INTERNET SPEED TEST ===\n")

    print(f"{Fore.WHITE}Server: {Fore.GREEN}{server['sponsor']} ({server['name']}, {server['country']})")

    print(f"{Fore.WHITE}Ping: {color_speed(100 - min(ping, 100))}{ping:.0f} ms")

    print(f"{Fore.WHITE}Download: {color_speed(download)}{download:.2f} Mbps")

    print(f"{Fore.WHITE}Upload: {color_speed(upload)}{upload:.2f} Mbps")

    print(f"\n{Fore.CYAN}Completed.")

except Exception as e:
    loading = False
    print(f"\n {Fore.RED}Error: {str(e)}")

input("\nPress Enter to exit...")