#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application de chiffrement de fichiers avec interface graphique Tkinter
Utilise l'algorithme de chiffrement symétrique Fernet (AES 128 en mode CBC)
"""

import base64
import os
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext, ttk

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chiffreur de Fichiers - Encrypt.py")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.selected_files = []
        self.password_var = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configuration de l'interface utilisateur"""
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration du grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Titre
        title_label = ttk.Label(main_frame, text="🔐 Chiffreur de Fichiers", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Section sélection de fichiers
        files_label = ttk.Label(main_frame, text="Fichiers à traiter:", font=("Arial", 10, "bold"))
        files_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # Frame pour les boutons de fichiers
        files_frame = ttk.Frame(main_frame)
        files_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        files_frame.columnconfigure(1, weight=1)
        
        self.select_files_btn = ttk.Button(files_frame, text="📁 Sélectionner fichier(s)", 
                                          command=self.select_files)
        self.select_files_btn.grid(row=0, column=0, padx=(0, 10))
        
        self.clear_files_btn = ttk.Button(files_frame, text="🗑️ Effacer la liste", 
                                         command=self.clear_files)
        self.clear_files_btn.grid(row=0, column=2)
        
        # Liste des fichiers sélectionnés
        self.files_listbox = tk.Listbox(main_frame, height=8, selectmode=tk.EXTENDED)
        self.files_listbox.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Scrollbar pour la liste
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.files_listbox.yview)
        scrollbar.grid(row=3, column=3, sticky=(tk.N, tk.S))
        self.files_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Section mot de passe
        password_label = ttk.Label(main_frame, text="Mot de passe:", font=("Arial", 10, "bold"))
        password_label.grid(row=4, column=0, sticky=tk.W, pady=(10, 5))
        
        self.password_entry = ttk.Entry(main_frame, textvariable=self.password_var, 
                                       show="*", width=40, font=("Arial", 10))
        self.password_entry.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.show_password_var = tk.BooleanVar()
        self.show_password_cb = ttk.Checkbutton(main_frame, text="Afficher le mot de passe", 
                                               variable=self.show_password_var,
                                               command=self.toggle_password_visibility)
        self.show_password_cb.grid(row=5, column=2, padx=(10, 0))
        
        # Section boutons d'action
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        self.encrypt_btn = ttk.Button(action_frame, text="🔒 Chiffrer", 
                                     command=self.encrypt_files, style="Accent.TButton")
        self.encrypt_btn.grid(row=0, column=0, padx=(0, 20))
        
        self.decrypt_btn = ttk.Button(action_frame, text="🔓 Déchiffrer", 
                                     command=self.decrypt_files, style="Accent.TButton")
        self.decrypt_btn.grid(row=0, column=1)
        
        # Barre de progression
        progress_label = ttk.Label(main_frame, text="Progression:")
        progress_label.grid(row=7, column=0, sticky=tk.W, pady=(10, 5))
        
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Zone de log
        log_label = ttk.Label(main_frame, text="Journal d'activité:")
        log_label.grid(row=9, column=0, sticky=tk.W, pady=(10, 5))
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=8, width=70)
        self.log_text.grid(row=10, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Configuration du redimensionnement
        main_frame.rowconfigure(10, weight=1)
        
        # Message de bienvenue
        self.log_message("🚀 Application de chiffrement prête à l'emploi!")
        self.log_message("📋 Instructions:")
        self.log_message("   1. Sélectionnez un ou plusieurs fichiers")
        self.log_message("   2. Entrez un mot de passe sécurisé")
        self.log_message("   3. Choisissez Chiffrer ou Déchiffrer")
        self.log_message("⚠️  ATTENTION: Les fichiers originaux seront remplacés!")
        
    def select_files(self):
        """Sélectionner des fichiers à traiter"""
        files = filedialog.askopenfilenames(
            title="Sélectionner des fichiers à chiffrer/déchiffrer",
            filetypes=[
                ("Tous les fichiers", "*.*"),
                ("Fichiers texte", "*.txt"),
                ("Images", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Documents", "*.pdf *.doc *.docx"),
                ("Fichiers chiffrés", "*.encrypted")
            ]
        )
        
        if files:
            self.selected_files.extend(files)
            self.update_files_listbox()
            self.log_message(f"📁 {len(files)} fichier(s) ajouté(s) à la liste")
    
    def clear_files(self):
        """Effacer la liste des fichiers"""
        self.selected_files.clear()
        self.update_files_listbox()
        self.log_message("🗑️ Liste des fichiers effacée")
    
    def update_files_listbox(self):
        """Mettre à jour l'affichage de la liste des fichiers"""
        self.files_listbox.delete(0, tk.END)
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            self.files_listbox.insert(tk.END, filename)
    
    def toggle_password_visibility(self):
        """Basculer la visibilité du mot de passe"""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
    
    def log_message(self, message):
        """Ajouter un message au journal"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def generate_key(self, password, salt):
        """Générer une clé de chiffrement à partir du mot de passe"""
        password_bytes = password.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
        return key
    
    def encrypt_file(self, file_path, password):
        """Chiffrer un fichier et remplacer l'original"""
        try:
            # Créer un fichier temporaire pour la sauvegarde
            temp_file_path = file_path + '.temp_backup'
            
            # Générer un salt aléatoire
            salt = os.urandom(16)
            
            # Générer la clé
            key = self.generate_key(password, salt)
            fernet = Fernet(key)
            
            # Lire le fichier original
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Créer une sauvegarde temporaire
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(file_data)
            
            # Chiffrer les données
            encrypted_data = fernet.encrypt(file_data)
            
            # Remplacer le fichier original par la version chiffrée
            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(salt + encrypted_data)
            
            # Supprimer la sauvegarde temporaire si tout s'est bien passé
            os.remove(temp_file_path)
            
            return True, file_path
            
        except Exception as e:
            # En cas d'erreur, restaurer le fichier original si possible
            try:
                if os.path.exists(temp_file_path):
                    os.replace(temp_file_path, file_path)
            except:
                pass
            return False, str(e)
    
    def decrypt_file(self, file_path, password):
        """Déchiffrer un fichier et remplacer l'original"""
        try:
            # Créer un fichier temporaire pour la sauvegarde
            temp_file_path = file_path + '.temp_backup'
            
            # Lire le fichier chiffré
            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()
            
            # Créer une sauvegarde temporaire du fichier chiffré
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(encrypted_data)
            
            # Extraire le salt (16 premiers octets)
            salt = encrypted_data[:16]
            encrypted_content = encrypted_data[16:]
            
            # Générer la clé
            key = self.generate_key(password, salt)
            fernet = Fernet(key)
            
            # Déchiffrer les données
            decrypted_data = fernet.decrypt(encrypted_content)
            
            # Remplacer le fichier original par la version déchiffrée
            with open(file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            
            # Supprimer la sauvegarde temporaire si tout s'est bien passé
            os.remove(temp_file_path)
            
            return True, file_path
            
        except Exception as e:
            # En cas d'erreur, restaurer le fichier chiffré si possible
            try:
                if os.path.exists(temp_file_path):
                    os.replace(temp_file_path, file_path)
            except:
                pass
            return False, str(e)
    
    def encrypt_files(self):
        """Chiffrer tous les fichiers sélectionnés"""
        if not self.selected_files:
            messagebox.showwarning("Attention", "Veuillez sélectionner au moins un fichier!")
            return
        
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Attention", "Veuillez entrer un mot de passe!")
            return
        
        if len(password) < 6:
            messagebox.showwarning("Attention", "Le mot de passe doit contenir au moins 6 caractères!")
            return
        
        # Désactiver les boutons pendant le traitement
        self.encrypt_btn.configure(state='disabled')
        self.decrypt_btn.configure(state='disabled')
        
        def encrypt_thread():
            try:
                total_files = len(self.selected_files)
                successful = 0
                
                self.log_message(f"🔒 Début du chiffrement de {total_files} fichier(s)...")
                
                for i, file_path in enumerate(self.selected_files):
                    filename = os.path.basename(file_path)
                    self.log_message(f"🔄 Chiffrement de {filename}...")
                    
                    success, result = self.encrypt_file(file_path, password)
                    
                    if success:
                        self.log_message(f"✅ {filename} chiffré avec succès (fichier original remplacé)")
                        successful += 1
                    else:
                        self.log_message(f"❌ Erreur lors du chiffrement de {filename}: {result}")
                    
                    # Mettre à jour la barre de progression
                    progress = ((i + 1) / total_files) * 100
                    self.progress_var.set(progress)
                
                self.log_message(f"🎉 Chiffrement terminé: {successful}/{total_files} fichiers traités avec succès")
                
                if successful == total_files:
                    messagebox.showinfo("Succès", f"Tous les fichiers ont été chiffrés avec succès!")
                else:
                    messagebox.showwarning("Attention", f"{successful}/{total_files} fichiers chiffrés. Vérifiez le journal pour les erreurs.")
                
            finally:
                # Réactiver les boutons
                self.encrypt_btn.configure(state='normal')
                self.decrypt_btn.configure(state='normal')
                self.progress_var.set(0)
        
        # Lancer le chiffrement dans un thread séparé
        threading.Thread(target=encrypt_thread, daemon=True).start()
    
    def decrypt_files(self):
        """Déchiffrer tous les fichiers sélectionnés"""
        if not self.selected_files:
            messagebox.showwarning("Attention", "Veuillez sélectionner au moins un fichier!")
            return
        
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Attention", "Veuillez entrer un mot de passe!")
            return
        
        # Désactiver les boutons pendant le traitement
        self.encrypt_btn.configure(state='disabled')
        self.decrypt_btn.configure(state='disabled')
        
        def decrypt_thread():
            try:
                total_files = len(self.selected_files)
                successful = 0
                
                self.log_message(f"🔓 Début du déchiffrement de {total_files} fichier(s)...")
                
                for i, file_path in enumerate(self.selected_files):
                    filename = os.path.basename(file_path)
                    self.log_message(f"🔄 Déchiffrement de {filename}...")
                    
                    success, result = self.decrypt_file(file_path, password)
                    
                    if success:
                        self.log_message(f"✅ {filename} déchiffré avec succès (fichier original restauré)")
                        successful += 1
                    else:
                        self.log_message(f"❌ Erreur lors du déchiffrement de {filename}: {result}")
                    
                    # Mettre à jour la barre de progression
                    progress = ((i + 1) / total_files) * 100
                    self.progress_var.set(progress)
                
                self.log_message(f"🎉 Déchiffrement terminé: {successful}/{total_files} fichiers traités avec succès")
                
                if successful == total_files:
                    messagebox.showinfo("Succès", f"Tous les fichiers ont été déchiffrés avec succès!")
                else:
                    messagebox.showwarning("Attention", f"{successful}/{total_files} fichiers déchiffrés. Vérifiez le journal pour les erreurs.")
                
            finally:
                # Réactiver les boutons
                self.encrypt_btn.configure(state='normal')
                self.decrypt_btn.configure(state='normal')
                self.progress_var.set(0)
        
        # Lancer le déchiffrement dans un thread séparé
        threading.Thread(target=decrypt_thread, daemon=True).start()

def main():
    """Fonction principale"""
    root = tk.Tk()
    app = EncryptApp(root)
    
    # Centrer la fenêtre
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
