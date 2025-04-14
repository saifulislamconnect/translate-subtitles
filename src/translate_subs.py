import argparse
import os
import re
from deep_translator import GoogleTranslator
from tqdm import tqdm

def translate_text(text, source_lang='auto', target_lang='bn'):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        return text

def split_lines(text, original_line_count):
    sentences = re.split(r'(?<=[।!?])\s+', text)
    if len(sentences) < original_line_count:
        sentences += [''] * (original_line_count - len(sentences))
    return sentences[:original_line_count]

def process_block(block):
    lines = block.strip().splitlines()
    if len(lines) < 3:
        return block

    index, time_range, *text_lines = lines
    original_text = " ".join(text_lines)
    translated_text = translate_text(original_text)
    final_lines = split_lines(translated_text, len(text_lines))

    return "\n".join([index, time_range] + final_lines)

def get_output_filename(input_file):
    base, _ = os.path.splitext(input_file)
    return f"{base}.bn.srt"

def main():
    parser = argparse.ArgumentParser(description="Translate an SRT file to Bangla.")
    parser.add_argument("input_file", help="Path to the input .srt file")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = get_output_filename(input_file)

    if not os.path.isfile(input_file):
        print(f"❌ File not found: {input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()

    blocks = content.strip().split("\n\n")

    translated_blocks = []
    for block in tqdm(blocks, desc="🔄 Translating subtitles", unit="block"):
        translated_blocks.append(process_block(block))

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("\n\n".join(translated_blocks))

    print(f"\n✅ Translation complete! File saved as: {output_file}")

if __name__ == "__main__":
    main()
