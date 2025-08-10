import customtkinter as ctk
from Cripter import encrypt, decrypt


class EncryptPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.message = ctk.CTkEntry(self, placeholder_text="Message")
        self.message.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.key = ctk.CTkEntry(self, placeholder_text="Key")
        self.key.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.output = ctk.CTkTextbox(self, height=100, )
        self.output.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.output.configure(state="disabled")

        ctk.CTkButton(self, text="Encrypt", command=self.encrypt_callback).grid(
            row=3, column=0, padx=20, pady=20, sticky="ew"
        )

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def encrypt_callback(self):
        self.output.delete("0.0", "end")
        txt = encrypt(self.message.get(), self.key.get().lower())
        self.output.insert("0.0", txt)

class DecryptPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.message = ctk.CTkEntry(self, placeholder_text="Encrypted Message")
        self.message.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.key = ctk.CTkEntry(self, placeholder_text="Key")
        self.key.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.output = ctk.CTkTextbox(self, height=100)
        self.output.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.output.configure(state="disabled")

        ctk.CTkButton(self, text="Decrypt", command=self.decrypt_callback).grid(
            row=3, column=0, padx=20, pady=20, sticky="ew"
        )

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def decrypt_callback(self):
        self.output.delete("0.0", "end")
        txt = decrypt(self.message.get(), self.key.get().lower())
        self.output.insert("0.0", txt)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cripter!")
        self.geometry("600x400")

        self.grid_rowconfigure(0, weight=0)  # switch row
        self.grid_rowconfigure(1, weight=1)  # page row
        self.grid_columnconfigure(0, weight=1)

        # ---------- switch ----------
        self.mode_var = ctk.StringVar(value="Encrypt")
        switch = ctk.CTkSegmentedButton(
            self,
            values=["Encrypt", "Decrypt"],
            variable=self.mode_var,
            command=self.change_frame
        )
        switch.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # ---------- container for pages ----------
        container = ctk.CTkFrame(self)
        container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # ---------- create pages ----------
        self.frames = {
            "Encrypt": EncryptPage(container),
            "Decrypt": DecryptPage(container)
        }

        for f in self.frames.values():
            f.grid(row=0, column=0, sticky="nsew")

        self.change_frame("Encrypt")  # default page

    def change_frame(self, mode):
        self.frames[mode].tkraise()

if __name__ == "__main__":
    App().mainloop()