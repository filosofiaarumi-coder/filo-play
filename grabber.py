import requests

# Daftar saluran TV kamu (bisa berisi M3U8 maupun MPD)
channels = [
    {
        "name": "RCTI HD (M3U8)",
        "tvg_id": "RCTI.id",
        "logo": "https://example.com/logo/rcti.png",
        "group": "Lokal Indonesia",
        "url": "https://rpluz.ben45mcc.workers.dev/index.m3u8?ch=rcti",
        "user_agent": "android-R+",
        "referrer": "https://www.rctiplus.com/"
    },
    {
        "name": "RCTI HD (MPD)",
        "tvg_id": "RCTI.id",
        "logo": "https://example.com/logo/rcti.png",
        "group": "Lokal Indonesia",
        "url": "https://d3b0v7fggu5zwm.cloudfront.net/out/v1/9e9aba7068ca4c7f8a73381bef5f8742/index.mpd",
        "manifest_type": "mpd",
        "license_type": "clearkey",
        "license_key": "3404792cb4c804902acdc6ca65c1a298:d386001215594043a8995db796ad9e9c",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "referrer": "https://www.visionplus.id/"
    }
]

def generate_m3u():
    m3u_text = "#EXTM3U\n\n"
    
    for item in channels:
        # Tambahkan KODIPROP jika saluran menggunakan DRM (seperti MPD)
        if "license_type" in item:
            m3u_text += '#KODIPROP:inputstreamaddon=inputstream.adaptive\n'
            m3u_text += f'#KODIPROP:inputstream.adaptive.manifest_type={item.get("manifest_type", "mpd")}\n'
            m3u_text += f'#KODIPROP:inputstream.adaptive.license_type={item["license_type"]}\n'
            m3u_text += f'#KODIPROP:inputstream.adaptive.license_key={item["license_key"]}\n'
        
        # Tambahkan User-Agent & Referrer jika ada
        if "user_agent" in item:
            m3u_text += f'#EXTVLCOPT:http-user-agent={item["user_agent"]}\n'
        if "referrer" in item:
            m3u_text += f'#EXTVLCOPT:http-referrer={item["referrer"]}\n'
            
        # Format dasar M3U (#EXTINF dan URL)
        m3u_text += f'#EXTINF:-1 tvg-id="{item["tvg_id"]}" tvg-logo="{item["logo"]}" group-title="{item["group"]}", {item["name"]}\n'
        m3u_text += f'{item["url"]}\n\n'
        
    return m3u_text

if __name__ == "__main__":
    content = generate_m3u()
    with open("playlist.m3u", "w", encoding="utf-8") as file:
        file.write(content)
    print("File playlist.m3u berhasil diperbarui!")
