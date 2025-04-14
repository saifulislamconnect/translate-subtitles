from deep_translator import GoogleTranslator
import re

# File paths
input_file = "The.Queen.Of.Black.Magic.2019.720p.WEBRip.x264.AAC-[YTS.MX].srt"
output_file = "The.Queen.Of.Black.Magic.2019.Full.Bangla.srt"

def translate_text(text, source_lang='auto', target_lang='bn'):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        return text  # Fallback to original

def split_lines(text, original_line_count):
    # Try to preserve line count and readability
    sentences = re.split(r'(?<=[।!?])\s+', text)
    if len(sentences) < original_line_count:
        sentences += [''] * (original_line_count - len(sentences))
    return sentences[:original_line_count]

def process_block(block):
    lines = block.strip().splitlines()
    if len(lines) < 3:
        return block  # Leave untouched if not standard block

    index, time_range, *text_lines = lines
    original_text = " ".join(text_lines)
    translated_text = translate_text(original_text)

    final_lines = split_lines(translated_text, len(text_lines))
    return "\n".join([index, time_range] + final_lines)

def main():
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()

    blocks = content.strip().split("\n\n")
    translated_blocks = [process_block(block) for block in blocks]

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("\n\n".join(translated_blocks))

    print(f"✅ Translation complete! File saved as: {output_file}")

if __name__ == "__main__":
    main()
