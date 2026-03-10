import speedtest
import tkinter

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

def create_gui():
    global result_label
    root = tkinter.Tk()
    root.title("Internet Speed Tester")

    test_button = tkinter.Button(root, text="Test Speed", command=test_speed)
    test_button.pack(pady=20)

    result_label = tkinter.Label(root, text="")
    result_label.pack(pady=20)

    root.mainloop()

create_gui()
