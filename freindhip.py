import os
import qrcode
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

# Config
CERT_WIDTH, CERT_HEIGHT = 1000, 700
BG_COLOR = "#f9f4ef"
FONT_PATH = "arial.ttf"
FONT_BOLD = "arialbd.ttf"
OUTPUT_FOLDER = "certificates"
QR_SECRET = "Happy Friendship Day! 💖 You’re the real one."

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Function to generate QR
def generate_qr(name):
    qr_data = f"{QR_SECRET}\n\nFrom: Your Best Friend\nTo: {name}"
    qr = qrcode.make(qr_data)
    qr = qr.resize((120, 120))
    return qr

# Generate certificate
def generate_certificate(name):
    # Background
    cert = Image.new("RGB", (CERT_WIDTH, CERT_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(cert)

    # Fonts
    try:
        title_font = ImageFont.truetype(FONT_BOLD, 60)
        name_font = ImageFont.truetype(FONT_PATH, 48)
        body_font = ImageFont.truetype(FONT_PATH, 28)
        footer_font = ImageFont.truetype(FONT_PATH, 22)
    except:
        title_font = name_font = body_font = footer_font = ImageFont.load_default()

    # Border
    draw.rectangle([(10, 10), (CERT_WIDTH - 10, CERT_HEIGHT - 10)], outline="black", width=6)

    # Title
    draw.text((CERT_WIDTH // 2 - 300, 80), "Certificate of Friendship", fill="darkblue", font=title_font)

    # Name
    draw.text((CERT_WIDTH // 2 - 250, 220), "Awarded to:", fill="black", font=body_font)
    draw.text((CERT_WIDTH // 2 - 150, 270), name, fill="#c0392b", font=name_font)

    # Body
    msg = "In recognition of your amazing friendship,\nkindness, and constant support.\nYou are truly irreplaceable."
    draw.multiline_text((CERT_WIDTH // 2 - 300, 380), msg, fill="black", font=body_font)

    # Footer
    draw.text((70, CERT_HEIGHT - 80), "Presented with love 💖", fill="gray", font=footer_font)
    draw.text((CERT_WIDTH - 250, CERT_HEIGHT - 80), "Friendship Day 2025", fill="gray", font=footer_font)

    # QR Code
    qr_img = generate_qr(name)
    cert.paste(qr_img, (CERT_WIDTH - 160, CERT_HEIGHT - 160))

    # Save
    filename = os.path.join(OUTPUT_FOLDER, f"{name.replace(' ', '_')}_Certificate.png")
    cert.save(filename)
    print(f"✅ Saved: {filename}")

# Read from file
def process_file(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]
        if not names:
            messagebox.showwarning("Empty File", "No names found in the file.")
            return
        for name in names:
            generate_certificate(name)
        messagebox.showinfo("Done", f"Certificates generated in '{OUTPUT_FOLDER}'")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
def select_file():
    path = filedialog.askopenfilename(title="Select a text file with friend names",
                                      filetypes=[("Text Files", "*.txt")])
    if path:
        process_file(path)

def build_gui():
    root = Tk()
    root.title("Friendship Day Certificate Generator")
    root.geometry("500x200")
    root.resizable(False, False)

    Label(root, text="🎉 Friendship Certificate Generator 🎉", font=("Arial", 16)).pack(pady=10)
    Label(root, text="Click below to select a .txt file with friend names", font=("Arial", 12)).pack(pady=5)
    Button(root, text="Select File", command=select_file, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

    root.mainloop()

# Run GUI
if __name__ == "__main__":
    build_gui()
