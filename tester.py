import speedtest
import time
import threading
import sys

running = False


def spinner():
    while running:
        for c in "|/-\\":
            sys.stdout.write(f"\rMěřím... {c}")
            sys.stdout.flush()
            time.sleep(0.1)


def measure_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    ping = st.results.ping
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    return ping, download, upload


def run_once():
    global running
    running = True

    t = threading.Thread(target=spinner)
    t.start()

    ping, download, upload = measure_speed()

    running = False
    t.join()

    print("\r" + " " * 30, end="\r")  # vyčistí řádek
    print(f"Ping: {ping:.0f} ms")
    print(f"Download: {download:.2f} Mbps")
    print(f"Upload: {upload:.2f} Mbps\n")



# MENU
while True:
    print("1 - Jednorázový test")
    print("2 - Konec")

    choice = input("Vyber: ")

    if choice == "1":
        run_once()
    elif choice == "2":
        break
    else:
        print("Neplatná volba\n")