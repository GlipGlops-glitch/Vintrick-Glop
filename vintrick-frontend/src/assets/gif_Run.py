# File: BuildV20_Main/assets/gif_Run.py


def generate_grape_squish_frames(frame_count=8, size=96):
    from PIL import ImageDraw, Image as PILImage, ImageTk
    frames = []
    for i in range(frame_count):
        im = PILImage.new("RGBA", (size, size), (0,0,0,0))
        draw = ImageDraw.Draw(im)
        top = size//4 + int((i/frame_count)*size//6)
        bottom = size - size//8 - int((i/frame_count)*size//12)
        width = size//2 + int((i/frame_count)*size//4)
        x0 = (size - width)//2
        x1 = x0 + width
        draw.ellipse([x0, top, x1, bottom], fill="#6a2673", outline="#46204d", width=4)
        draw.ellipse([x0+width//5, top+width//5, x0+width//3, top+width//2], fill="#fff7", outline=None)
        juice_height = int((i/frame_count)*size//6)
        if juice_height:
            draw.ellipse([size//3, bottom-juice_height, 2*size//3, bottom+juice_height], fill="#bb357d", outline="#7b1948", width=2)
            for dx in [-16, 0, 16]:
                draw.ellipse([size//2+dx-6, bottom+juice_height//2, size//2+dx+6, bottom+juice_height], fill="#bb357d77", outline=None)
        frames.append(ImageTk.PhotoImage(im))
    return frames
