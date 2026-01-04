import re
import os

def is_valid_keyword(line):
    """
    判断一行是否为有效的、有意义的文本关键字
    """
    text = line.strip()
    if not text:
        return False

    # 1. 过滤数学公式和 LaTeX 语法
    # 如果包含反斜杠、美元符号、上下标、大括号、等号等，视为数学/代码相关
    math_indicators = ['\\', '$', '^', '_', '{', '}', '=', '<', '>']
    if any(char in text for char in math_indicators):
        return False

    # 2. 过滤无意义内容（纯数字、纯标点）
    # 必须包含至少一个汉字或英文字母
    if not re.search(r'[\u4e00-\u9fa5a-zA-Z]', text):
        return False

    # 3. 过滤特定噪声词（章节、页码引用）
    text_lower = text.lower()
    if 'chapter' in text_lower:  # 如 "of chapter 3"
        return False
    if re.match(r'^p\s?\d+$', text_lower):  # 如 "p 116"
        return False
    if re.match(r'^\(.*\)$', text): # 如 "(1)", "(i)"
        return False

    # 4. 过滤极短关键字
    # 统计有效字符长度：汉字算 1，英文字母算 1，数字忽略
    # 目的：保留 "2D 倒" (长度2)，去除 "x" (长度1), "3" (长度0)
    zh_count = len(re.findall(r'[\u4e00-\u9fa5]', text))
    en_count = len(re.findall(r'[a-zA-Z]', text))
    effective_length = zh_count + en_count

    # 设定阈值：有效长度必须 >= 2
    # 这将过滤掉单个字母 "f", "x" 和单个汉字 "光" (通常单个字作为关键字太泛)
    # 但保留 "CD", "LD", "THz", "光场" 等
    if effective_length < 2:
        return False

    return True

def process_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"错误：找不到文件 {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    current_keywords = []
    processing_list = False # 标记是否正在处理关键字列表

    # 用于临时存储一个 Section 的结构
    # 逻辑：遇到新标题时，结算上一个标题下的关键字

    for line in lines:
        stripped = line.strip()

        # 1. 识别标题 (## ...)
        if stripped.startswith('##'):
            # 结算上一段落（如果有）
            if processing_list and current_keywords:
                output_lines.append(f"共 {len(current_keywords)} 个关键字：\n\n")
                output_lines.extend(current_keywords)
                output_lines.append("\n") # 段后空行

            # 重置状态
            current_keywords = []
            output_lines.append(line) # 写入标题行
            processing_list = False

        # 2. 识别计数行 (共 ... 个关键字) -> 标志着列表开始
        elif stripped.startswith('共') and '个关键字' in stripped:
            processing_list = True
            # 注意：我们不直接写入这一行，而是等处理完该段落后，生成新的计数行

        # 3. 处理内容行
        else:
            if processing_list:
                # 处于列表区域，进行过滤
                if is_valid_keyword(line):
                    current_keywords.append(line)
            else:
                # 处于非列表区域（如文档开头的介绍），直接保留
                # 避免保留过多的连续空行
                if stripped or (output_lines and output_lines[-1].strip()):
                    output_lines.append(line)

    # 4. 结算文件末尾的最后一段
    if processing_list and current_keywords:
        output_lines.append(f"共 {len(current_keywords)} 个关键字：\n\n")
        output_lines.extend(current_keywords)

    # 写入结果
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"处理完成！已生成文件：{output_path}")

if __name__ == "__main__":
    # 请确保同目录下有 color_keywords.md 文件
    process_file("color_keywords.md", "color_keywords_cleaned.md")
