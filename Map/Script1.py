import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import math
import base64

# Constants
TILE_SIZE = 256
ZOOM_LEVEL = 4
CENTER_TILE = {"x": 8, "y": 5}

TILE_SERVER_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
NOMINATIM_SERVER_URL = "https://nominatim.openstreetmap.org/search"

# Globals
drag_start_x = 0
drag_start_y = 0
tile_offset_x = 0
tile_offset_y = 0
map_tiles = {}


# Base64 decoding function
def decode_email_base64(encoded_email):
    """
    Decode the given Base64-encoded email back to the original.
    """
    return base64.b64decode(encoded_email).decode("utf-8")


# Your Base64-encoded email (replace with your encoded email)
encoded_email = "dGltb24uYmxhY2suZ2FtaWdAZ21haWwuY29t"  # Replace with Base64-encoded email
decoded_email = decode_email_base64(encoded_email)  # Decode the email at runtime

# Tkinter GUI setup
window = tk.Tk()
window.title("OpenStreetMap Viewer with Search and Zoom")

# Setting up a canvas for the map
canvas = tk.Canvas(window, width=3 * TILE_SIZE, height=3 * TILE_SIZE, bg="gray")
canvas.pack()

# Search box, zoom buttons, and other UI elements
controls_frame = tk.Frame(window)
controls_frame.pack(side=tk.BOTTOM, fill=tk.X)

search_entry = tk.Entry(controls_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=10, pady=10)

search_button = tk.Button(controls_frame, text="Search", command=lambda: search_location(search_entry.get()))
search_button.pack(side=tk.LEFT, padx=5, pady=10)

zoom_in_button = tk.Button(controls_frame, text="+", command=lambda: zoom_map(1))  # Zoom in
zoom_in_button.pack(side=tk.RIGHT, padx=5, pady=10)

zoom_out_button = tk.Button(controls_frame, text="-", command=lambda: zoom_map(-1))  # Zoom out
zoom_out_button.pack(side=tk.RIGHT, padx=5, pady=10)


def fetch_tile(x, y, z):
    """
    Fetch a map tile from the OpenStreetMap server.

    Args:
        x (int): Tile x-coordinate.
        y (int): Tile y-coordinate.
        z (int): Zoom level.

    Returns:
        ImageTk.PhotoImage: The tile as a PIL ImageTk.PhotoImage object.
    """
    try:
        url = TILE_SERVER_URL.format(x=x, y=y, z=z)
        headers = {
            "User-Agent": f"OpenStreetMapViewer/1.0 ({decoded_email})"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
    except Exception as e:
        print(f"Error fetching tile {z}/{x}/{y}: {e}")
        return ImageTk.PhotoImage(Image.new("RGB", (TILE_SIZE, TILE_SIZE), "gray"))


def update_map(center_tile_x, center_tile_y, zoom):
    global map_tiles, tile_offset_x, tile_offset_y
    map_tiles.clear()
    canvas.delete("all")

    # Display tiles in a 3x3 grid
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            tile_x = center_tile_x + dx
            tile_y = center_tile_y + dy

            tile_image = fetch_tile(tile_x, tile_y, zoom)
            map_tiles[(tile_x, tile_y)] = tile_image

            canvas_x = (dx + 1) * TILE_SIZE + tile_offset_x
            canvas_y = (dy + 1) * TILE_SIZE + tile_offset_y
            canvas.create_image(canvas_x, canvas_y, image=tile_image)


def start_drag(event):
    global drag_start_x, drag_start_y
    drag_start_x = event.x
    drag_start_y = event.y


def drag_map(event):
    global drag_start_x, drag_start_y, tile_offset_x, tile_offset_y

    dx = event.x - drag_start_x
    dy = event.y - drag_start_y

    tile_offset_x += dx
    tile_offset_y += dy

    if abs(tile_offset_x) >= TILE_SIZE:
        CENTER_TILE["x"] += -1 if tile_offset_x > 0 else 1
        tile_offset_x %= TILE_SIZE

    if abs(tile_offset_y) >= TILE_SIZE:
        CENTER_TILE["y"] += -1 if tile_offset_y > 0 else 1
        tile_offset_y %= TILE_SIZE

    drag_start_x = event.x
    drag_start_y = event.y

    update_map(CENTER_TILE["x"], CENTER_TILE["y"], ZOOM_LEVEL)


def search_location(query):
    """
    Search for a location using the Nominatim API and update the map.

    Args:
        query (str): Query string (e.g., a city or address).
    """
    global CENTER_TILE, ZOOM_LEVEL
    try:
        params = {"q": query, "format": "json"}
        headers = {
            "User-Agent": f"OpenStreetMapViewer/1.0 ({decoded_email})"
        }
        response = requests.get(NOMINATIM_SERVER_URL, params=params, headers=headers)
        response.raise_for_status()

        results = response.json()
        if results:
            lat = float(results[0]["lat"])
            lon = float(results[0]["lon"])

            # Convert latitude and longitude to tile_x and tile_y
            tile_x = int((lon + 180) / 360 * (2 ** ZOOM_LEVEL))
            tile_y = int(
                (1 - (math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi)) / 2 * (
                        2 ** ZOOM_LEVEL))

            CENTER_TILE["x"] = tile_x
            CENTER_TILE["y"] = tile_y
            tile_offset_x = tile_offset_y = 0  # Reset offsets
            update_map(CENTER_TILE["x"], CENTER_TILE["y"], ZOOM_LEVEL)
        else:
            print("No results found for:", query)
    except Exception as e:
        print(f"Error searching for location: {e}")


def zoom_map(direction):
    global ZOOM_LEVEL
    new_zoom = ZOOM_LEVEL + direction
    if 0 <= new_zoom <= 19:
        ZOOM_LEVEL = new_zoom
        update_map(CENTER_TILE["x"], CENTER_TILE["y"], ZOOM_LEVEL)


canvas.bind("<ButtonPress-1>", start_drag)
canvas.bind("<B1-Motion>", drag_map)
window.bind("<MouseWheel>", lambda event: zoom_map(1 if event.delta > 0 else -1))

update_map(CENTER_TILE["x"], CENTER_TILE["y"], ZOOM_LEVEL)
window.mainloop()