import customtkinter as ctk
from downloader import download_engine
from converter import convert_engine
import os

# Modern Renk Paleti
COLOR_THEME = {
    "bg": "#1a1a1a",
    "primary": "#3d5afe",   # Canlı Mavi
    "secondary": "#263238", # Koyu Gri
    "success": "#00c853",   # Yeşil
    "warning": "#ffab00"    # Turuncu
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DLX Studio - Media Hub")
        self.geometry("800x650")
        
        # Grid Yapılandırması
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Ana Arka Plan Çerçevesi
        self.main_container = ctk.CTkFrame(self, corner_radius=15, fg_color=COLOR_THEME["bg"])
        self.main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_columnconfigure(0, weight=1)

        # Üst Başlık ve Always on Top
        self.header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=20, pady=15)
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="DLX MEDIA", font=("Inter", 24, "bold"), text_color=COLOR_THEME["primary"])
        self.title_label.pack(side="left")

        self.always_top_check = ctk.CTkCheckBox(self.header_frame, text="Üstte Tut", font=("Inter", 12),
                                                command=self.toggle_always_on_top, checkbox_width=18, checkbox_height=18)
        self.always_top_check.pack(side="right")

        # Sekme Yapısı
        self.tabview = ctk.CTkTabview(self.main_container, fg_color=COLOR_THEME["secondary"], segmented_button_selected_color=COLOR_THEME["primary"])
        self.tabview.pack(expand=True, fill="both", padx=20, pady=10)
        self.tabview.add("İNDİRİCİ")
        self.tabview.add("DÖNÜŞTÜRÜCÜ")

        self.setup_modern_downloader()
        self.setup_modern_converter()

    def setup_modern_downloader(self):
        tab = self.tabview.tab("İNDİRİCİ")
        
        # URL Giriş Alanı - Daha şık bir kutu
        self.url_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.url_frame.pack(pady=30, padx=40, fill="x")
        
        self.url_entry = ctk.CTkEntry(self.url_frame, placeholder_text="Video linkini buraya yapıştırın...", 
                                      height=45, corner_radius=10, border_color=COLOR_THEME["primary"])
        self.url_entry.pack(fill="x")

        # Seçenekler Alanı
        self.opt_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.opt_frame.pack(pady=10)

        self.quality_menu = ctk.CTkOptionMenu(self.opt_frame, values=["En Yüksek", "1080p", "720p", "MP3"], 
                                              button_color=COLOR_THEME["primary"], corner_radius=8)
        self.quality_menu.pack(side="left", padx=10)

        self.path_btn = ctk.CTkButton(self.opt_frame, text="Klasör Seç", fg_color="transparent", border_width=1, width=100)
        self.path_btn.pack(side="left", padx=10)

        # Ana Buton
        self.dl_btn = ctk.CTkButton(tab, text="DOWLOAD NOW", font=("Inter", 16, "bold"), 
                                    fg_color=COLOR_THEME["primary"], hover_color="#304ffe", height=50, corner_radius=12)
        self.dl_btn.pack(pady=40, padx=100, fill="x")

    def setup_modern_converter(self):
        tab = self.tabview.tab("DÖNÜŞTÜRÜCÜ")
        ctk.CTkLabel(tab, text="Yakında Gelecek...").pack(pady=20)

    def toggle_always_on_top(self):
        self.attributes("-topmost", self.always_top_check.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()