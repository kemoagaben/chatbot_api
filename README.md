# Nurten Satılmış QR Business Card

This repository contains a simple Python script to generate a digital business card for **Av. Nurten Satılmış**. The script produces both a `.vcf` contact file and a QR code image. When the QR code is scanned or the VCF file is opened (e.g., shared via WhatsApp), the contact details can be saved directly to a phone's address book.

## Usage

1. Install dependencies:
   ```bash
   pip install qrcode[pil]
   ```
2. Run the generator:
   ```bash
   python generate_vcard_qr.py
   ```
   This creates:
   - `nurten_vcard.vcf`
   - `nurten_vcard_qr.png`

3. Share the `nurten_vcard.vcf` file or the QR image. When recipients scan or open it, they will be prompted to save the contact automatically.

## Contact Data
- Name: Av. Nurten Satılmış
- Organization: Örnek Hukuk Bürosu
- Title: Avukat
- Phone: +90 555 555 5555
- Email: nurten@example.com
- Website: https://yrzdmcyy.manus.space/

Feel free to modify `generate_vcard_qr.py` to update any of these details.
