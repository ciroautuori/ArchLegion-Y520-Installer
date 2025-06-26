#!/bin/bash
# post_install.sh - v0.1 (Installazione Base)
set -e
echo "--- ESECUZIONE SCRIPT POST-INSTALLAZIONE (BASE) ---"

# Abilita servizi essenziali
echo "Abilitazione NetworkManager..."
systemctl enable NetworkManager.service

# Configura il bootloader
echo "Installazione e configurazione di GRUB..."
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=ARCH
grub-mkconfig -o /boot/grub/grub.cfg

echo "--- SCRIPT POST-INSTALLAZIONE (BASE) COMPLETATO ---"
