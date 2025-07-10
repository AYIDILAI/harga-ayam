from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class HargaAyamApp(App):
    def build(self):
        self.title = "Aplikasi Harga Ayam"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.input_berat = TextInput(hint_text="Berat Ayam (kg)", multiline=False, input_filter='float', size_hint_y=None, height=50)
        self.input_harga = TextInput(hint_text="Harga per kg", multiline=False, input_filter='float', size_hint_y=None, height=50)
        layout.add_widget(self.input_berat)
        layout.add_widget(self.input_harga)

        self.label_hasil = Label(text="Harga Total: -", font_size=20, color=(0, 0.5, 0, 1), size_hint_y=None, height=50)
        layout.add_widget(self.label_hasil)

        btn_hitung = Button(text="Hitung", background_color=(0, 0.48, 1, 1), color=(1,1,1,1), size_hint_y=None, height=50)
        btn_hitung.bind(on_press=self.hitung_harga_ayam)
        layout.add_widget(btn_hitung)

        btn_reset = Button(text="Reset", background_color=(0.91, 0.92, 0.94, 1), color=(0,0,0,1), size_hint_y=None, height=50)
        btn_reset.bind(on_press=self.reset_input)
        layout.add_widget(btn_reset)

        btn_print = Button(text="Print", background_color=(0.09, 0.64, 0.72, 1), color=(1,1,1,1), size_hint_y=None, height=50)
        btn_print.bind(on_press=self.print_hasil)
        layout.add_widget(btn_print)

        return layout

    def hitung_harga_ayam(self, instance):
        try:
            berat_ayam = float(self.input_berat.text.replace(',', '.'))
            harga_per_kg = float(self.input_harga.text.replace(',', '.'))
            harga_total = berat_ayam * harga_per_kg
            hasil = f"Harga Total: Rp {harga_total:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
            self.label_hasil.text = hasil
            self.show_popup("Berhasil", hasil)
        except ValueError:
            self.show_popup("Error", "Input tidak valid. Pastikan Berat Ayam dan Harga per kg adalah angka.")

    def reset_input(self, instance):
        self.input_berat.text = ""
        self.input_harga.text = ""
        self.label_hasil.text = "Harga Total: -"
        self.show_popup("Reset", "Input telah direset.")

    def print_hasil(self, instance):
        if self.label_hasil.text == "Harga Total: -" or not self.input_berat.text or not self.input_harga.text:
            self.show_popup("Peringatan", "Belum ada hasil yang dihitung atau input tidak lengkap untuk dicetak.")
            return
        pesan_cetak = f"""------ ANUGRAH JAYA BROILER------\nBerat Ayam  : {self.input_berat.text} kg\nHarga per kg: Rp {self.input_harga.text}\n{self.label_hasil.text}\n-----------------------------\nTerima Kasih!\n"""
        try:
            with open("nota_harga_ayam.txt", "w", encoding="utf-8") as f:
                f.write(pesan_cetak)
            self.show_popup("Cetak", "Nota disimpan sebagai 'nota_harga_ayam.txt'.\nUntuk print, buka file ini di aplikasi lain.")
        except Exception as e:
            self.show_popup("Cetak Error", f"Gagal menyimpan nota: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(350, 200))
        popup.open()

if __name__ == '__main__':
    HargaAyamApp().run()
