"""Generate favicon PNG sizes + OG share image for ahmetpayaslioglu.com."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "assets", "img")
BG = (10, 14, 26)         # #0a0e1a
ACCENT = (0, 255, 157)    # #00ff9d
TEXT = (229, 231, 235)    # #e5e7eb
MUTED = (156, 163, 175)   # #9ca3af
DIM = (107, 114, 128)     # #6b7280


def load_font(candidates, size):
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


MONO = [
    r"C:\Windows\Fonts\consola.ttf",
    r"C:\Windows\Fonts\consolab.ttf",
]
MONO_BOLD = [
    r"C:\Windows\Fonts\consolab.ttf",
    r"C:\Windows\Fonts\consola.ttf",
]
SANS = [
    r"C:\Windows\Fonts\segoeui.ttf",
    r"C:\Windows\Fonts\arial.ttf",
]
SANS_BOLD = [
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
]


def make_favicon(size, out_path):
    img = Image.new("RGBA", (size, size), BG + (255,))
    draw = ImageDraw.Draw(img)
    radius = int(size * 0.18)
    # Rounded corners by masking
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size, size), radius=radius, fill=255)
    bg_img = Image.new("RGBA", (size, size), BG + (255,))
    out = Image.composite(bg_img, Image.new("RGBA", (size, size), (0, 0, 0, 0)), mask)
    draw = ImageDraw.Draw(out)
    # Inner border
    inset = max(3, size // 24)
    border = max(1, size // 50)
    inner_radius = max(2, radius - inset // 2)
    draw.rounded_rectangle(
        (inset, inset, size - inset, size - inset),
        radius=inner_radius,
        outline=ACCENT,
        width=border,
    )
    # AP text
    font_size = int(size * 0.50)
    font = load_font(MONO_BOLD, font_size)
    text = "AP"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = (size - th) // 2 - bbox[1]
    draw.text((tx, ty), text, font=font, fill=ACCENT)
    out.save(out_path, "PNG")
    print(f"  written {out_path} ({size}x{size})")


def make_og_image(out_path):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Subtle accent glow top-left
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((-200, -200, 600, 600), fill=(0, 255, 157, 24))
    od.ellipse((800, 400, 1400, 1000), fill=(56, 189, 248, 20))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Left monogram box
    box_size = 380
    box_x = 80
    box_y = (H - box_size) // 2
    radius = 56
    draw.rounded_rectangle(
        (box_x, box_y, box_x + box_size, box_y + box_size),
        radius=radius,
        outline=ACCENT,
        width=4,
    )
    # AP text inside box
    font_size = 200
    font = load_font(MONO_BOLD, font_size)
    text = "AP"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = box_x + (box_size - tw) // 2 - bbox[0]
    ty = box_y + (box_size - th) // 2 - bbox[1]
    draw.text((tx, ty), text, font=font, fill=ACCENT)

    # Right text column
    rx = box_x + box_size + 60

    # Prompt line
    prompt_font = load_font(MONO, 26)
    draw.text((rx, box_y + 18), "~/whoami", font=prompt_font, fill=ACCENT)

    # Name
    name_font = load_font(SANS_BOLD, 64)
    draw.text((rx, box_y + 70), "Ahmet", font=name_font, fill=TEXT)
    draw.text((rx, box_y + 140), "Payaslıoğlu", font=name_font, fill=TEXT)

    # Role lines (monospace)
    role_font = load_font(MONO, 22)
    draw.text(
        (rx, box_y + 232),
        "Senior Incident Responder (L3)",
        font=role_font,
        fill=MUTED,
    )
    draw.text(
        (rx, box_y + 262),
        "Threat Hunter · DFIR · Detection Engineering",
        font=role_font,
        fill=MUTED,
    )

    # Domain line
    url_font = load_font(MONO, 24)
    draw.text((rx, box_y + 330), "ahmetpayaslioglu.com", font=url_font, fill=ACCENT)

    img.save(out_path, "PNG", optimize=True)
    print(f"  written {out_path} ({W}x{H})")


def main():
    os.makedirs(OUT, exist_ok=True)
    print("Favicons:")
    make_favicon(32, os.path.join(OUT, "favicon-32.png"))
    make_favicon(192, os.path.join(OUT, "favicon-192.png"))
    make_favicon(512, os.path.join(OUT, "favicon-512.png"))
    print("OG image:")
    make_og_image(os.path.join(OUT, "og-image.png"))
    print("Done.")


if __name__ == "__main__":
    main()
