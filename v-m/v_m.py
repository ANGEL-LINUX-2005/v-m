import ffmpeg
import tkinter as tk
from tkinter import filedialog, messagebox

def reduce_video():
    try:
        # Get user input
        input_file = filedialog.askopenfilename(title="Select Video File")
        if not input_file:
            messagebox.showinfo("Error", "No video file selected.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", title="Save Reduced Video As")
        if not output_file:
            messagebox.showinfo("Error", "No output file selected.")
            return

        bitrate = bitrate_entry.get() or '1M'
        resolution = resolution_entry.get() or '1280x720'

        # Compress video
        ffmpeg.input(input_file).output(output_file, video_bitrate=bitrate, vf=f"scale={resolution}").run()
        messagebox.showinfo("Success", f"Video reduced and saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Video Reducer")
root.geometry("400x200")

# Labels and input fields
tk.Label(root, text="Bitrate (e.g., 1M):").pack(pady=5)
bitrate_entry = tk.Entry(root, width=30)
bitrate_entry.pack(pady=5)

tk.Label(root, text="Resolution (e.g., 1280x720):").pack(pady=5)
resolution_entry = tk.Entry(root, width=30)
resolution_entry.pack(pady=5)

# Button to reduce the video
reduce_button = tk.Button(root, text="Reduce Video", command=reduce_video, bg="blue", fg="white")
reduce_button.pack(pady=20)

# Run the window
root.mainloop()

