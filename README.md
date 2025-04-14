# 🎬 SRT Subtitle Translator CLI - ( Its FREE! No API Key required! )

A simple yet powerful CLI tool to translate `.srt` subtitle files into any supported language using Google Translate via `deep-translator`.  
Perfect for creating multilingual subtitle files from any source language.

✅ No API key required — just install and run!

---
## Description

This Python script translates subtitles in `.srt` format from any language to a target language. It uses the **Deep Translator** library to perform the translation and **TQDM** for progress tracking. You can specify the source and target languages, and it will automatically handle line-by-line translation while trying to preserve the original subtitle structure.

## ✨ Features

- Translates `.srt` files from **any language** to **your chosen target language**
- Automatically **preserves subtitle format**, keeping time codes and indices intact.
- Auto-detects source language
- CLI-based with a progress bar using `tqdm`
- Supports **100+ languages**
- Provides readable fallback if translation fails
- Provides a **progress bar** to track translation status.

---
## 👨‍💻 Author & Credits

This CLI tool was **developed by [Saiful Islam](https://www.linkedin.com/in/saifulislam-connect/)**.  
The idea, structure, and several optimization suggestions were shaped by Saiful to make subtitle translation efficient, scalable, and CLI-friendly.

> Thanks to `deep-translator` for translation helper

---
## Prerequisites

Before running the script, ensure you have Python 3.x installed along with the following dependencies:

- **deep-translator**: Used to access the translation services.
- **tqdm**: Used for showing a progress bar.
- **argparse**: For handling command-line arguments.

## 🛠 Installation

1. Install Python 3.x from [python.org](https://www.python.org/) if it's not already installed.
2. Install the required dependencies using `pip`:

   ```bash
   pip install deep-translator tqdm
   ```

## 🚀 Usage

### Command Format

```bash
python translate_srt.py <input_file> [--lang <language_code>]
```

### Arguments

- **`input_file`** (required): Path to the input `.srt` file that contains the subtitles to be translated.
- **`--lang`** (optional): Target language code. If no language is provided, it defaults to **Bengali** (`bn`).

### ✅ Example Commands

1. **Default translation to Bengali**:
   ```bash
   python translate_srt.py movie.srt
   ```

2. **Translation to Hindi**:
   ```bash
   python translate_srt.py movie.srt --lang hi
   ```

3. **Translation to Japanese**:
   ```bash
   python translate_srt.py movie.srt --lang ja
   ```

4. **Translation to an unsupported language** (e.g., `xx`):
   ```bash
   python translate_srt.py movie.srt --lang xx
   ```

   The script will output an error message and show a **list of supported languages**.

## 📌 Default Behavior

- **If no `--lang` argument is passed**, the script defaults to translating the subtitles into **Bengali** (`bn`).
- If an invalid language code is provided, the script will show a list of **supported languages** with their corresponding codes.

## 🌍 Supported Languages

Below is a list of supported languages and their corresponding language codes. You can translate subtitles to any of these languages by specifying the appropriate language code.
You can choose from 100+ languages including:

```
Afrikaans (af)
Albanian (sq)
Amharic (am)
Arabic (ar)
Armenian (hy)
Assamese (as)
Aymara (ay)
Azerbaijani (az)
Bambara (bm)
Basque (eu)
Belarusian (be)
Bengali (bn)
Bhojpuri (bho)
Bosnian (bs)
Bulgarian (bg)
Catalan (ca)
Cebuano (ceb)
Chichewa (ny)
Chinese (simplified) (zh-CN)
Chinese (traditional) (zh-TW)
Corsican (co)
Croatian (hr)
Czech (cs)
Danish (da)
Dhivehi (dv)
Dogri (doi)
Dutch (nl)
English (en)
Esperanto (eo)
Estonian (et)
Ewe (ee)
Filipino (tl)
Finnish (fi)
French (fr)
Frisian (fy)
Galician (gl)
Georgian (ka)
German (de)
Greek (el)
Guarani (gn)
Gujarati (gu)
Haitian Creole (ht)
Hausa (ha)
Hawaiian (haw)
Hebrew (iw)
Hindi (hi)
Hmong (hmn)
Hungarian (hu)
Icelandic (is)
Igbo (ig)
Ilocano (ilo)
Indonesian (id)
Irish (ga)
Italian (it)
Japanese (ja)
Javanese (jw)
Kannada (kn)
Kazakh (kk)
Khmer (km)
Kinyarwanda (rw)
Konkani (gom)
Korean (ko)
Krio (kri)
Kurdish (kurmanji) (ku)
Kurdish (sorani) (ckb)
Kyrgyz (ky)
Lao (lo)
Latin (la)
Latvian (lv)
Lingala (ln)
Lithuanian (lt)
Luganda (lg)
Luxembourgish (lb)
Macedonian (mk)
Maithili (mai)
Malagasy (mg)
Malay (ms)
Malayalam (ml)
Maltese (mt)
Maori (mi)
Marathi (mr)
Meiteilon (manipuri) (mni-Mtei)
Mizo (lus)
Mongolian (mn)
Myanmar (my)
Nepali (ne)
Norwegian (no)
Odia (oriya) (or)
Oromo (om)
Pashto (ps)
Persian (fa)
Polish (pl)
Portuguese (pt)
Punjabi (pa)
Quechua (qu)
Romanian (ro)
Russian (ru)
Samoan (sm)
Sanskrit (sa)
Scots Gaelic (gd)
Sepedi (nso)
Serbian (sr)
Sesotho (st)
Shona (sn)
Sindhi (sd)
Sinhala (si)
Slovak (sk)
Slovenian (sl)
Somali (so)
Spanish (es)
Sundanese (su)
Swahili (sw)
Swedish (sv)
Tajik (tg)
Tamil (ta)
Tatar (tt)
Telugu (te)
Thai (th)
Tigrinya (ti)
Tsonga (ts)
Turkish (tr)
Turkmen (tk)
Twi (ak)
Ukrainian (uk)
Urdu (ur)
Uyghur (ug)
Uzbek (uz)
Vietnamese (vi)
Welsh (cy)
Xhosa (xh)
Yiddish (yi)
Yoruba (yo)
Zulu (zu)
```

## Troubleshooting

- **File not found**: If the provided `.srt` file doesn't exist, the script will show a message saying the file was not found.
- **Invalid language code**: If the provided language code is not supported, the script will show an error and print the list of valid language codes.

---

## 📜 License

This project is open source and available under the MIT License.

MIT — feel free to use and modify.

---
