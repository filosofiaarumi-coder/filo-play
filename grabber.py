import requests

# Daftar saluran TV kamu
channels = [
    {
        "name": "RCTI HD",
        "tvg_id": "RCTI",
        "logo": "https://example.com/logo/rcti.png",
        "group": "Lokal Indonesia",
        "url": "https://sumber-stream.com/live/rcti.m3u8"
    },
    {
        "name": "SCTV HD",
        "tvg_id": "SCTV",
        "logo": "https://example.com/logo/sctv.png",
        "group": "Lokal Indonesia",
        "url": "https://sumber-stream.com/live/sctv.m3u8"
    }
]

def generate_m3u():
    m3u_text = "#EXTM3U\n"
    for item in channels:
        m3u_text += f'#EXTINF:-1 tvg-id="{item["tvg_id"]}" tvg-logo="{item["logo"]}" group-title="{item["group"]}", {item["name"]}\n'
        m3u_text += f'{item["url"]}\n\n'
    return m3u_text

if __name__ == "__main__":
    content = generate_m3u()
    with open("playlist.m3u", "w", encoding="utf-8") as file:
        file.write(content)
    print("Playlist filo-play berhasil dibuat!")
