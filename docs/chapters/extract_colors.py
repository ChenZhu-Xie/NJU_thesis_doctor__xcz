import re
from collections import defaultdict
from pathlib import Path

# Configuration
chapters_dir = Path(r'd:\C2D\Desktop\Code\Latex\TexStudio\0.njuthesis\NJU_thesis_doctor__xcz\docs\chapters')
chapters = ['chapter1.tex', 'chapter2.tex', 'chapter3.tex', 'chapter4.tex']
colors = ['gray', 'Maroon', 'PineGreen', 'Plum', 'NavyBlue']
color_meanings = {
    'gray': '灰色 gray — 自变量，或对应的散度分量 / 微分算子',
    'Maroon': '褐红 Maroon — 基础·通用概念',
    'PineGreen': '松树绿 PineGreen — 进阶·晶体光学',
    'Plum': '李子紫 Plum — 进阶·数学名词',
    'NavyBlue': '海军蓝 NavyBlue — 进阶·物理术语'
}

def extract_balanced_keywords(content, color_list):
    """
    Extracts keywords for each color using balanced brace matching.
    Supports \textcolor and \mathcolor.
    """
    # Pattern to find the start of \textcolor{color}{ or \mathcolor{color}{
    cmd_pattern = re.compile(r'\\(text|math)color\{(' + '|'.join(color_list) + r')\}\{')
    
    results = defaultdict(set)
    
    for match in cmd_pattern.finditer(content):
        color = match.group(2)
        start_pos = match.end()
        
        # Balanced brace counting
        brace_count = 1
        pos = start_pos
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    break
            pos += 1
            
        if brace_count == 0:
            keyword = content[start_pos:pos].strip()
            if keyword:
                results[color].add(keyword)
                
    return results

# Process files
combined_keywords = defaultdict(set)

for chapter_name in chapters:
    filepath = chapters_dir / chapter_name
    if filepath.exists():
        text = filepath.read_text(encoding='utf-8')
        file_keywords = extract_balanced_keywords(text, colors)
        for color, kws in file_keywords.items():
            combined_keywords[color].update(kws)

# Generate markdown output
output_lines = ['# 颜色关键字汇总\n']
output_lines.append(f'本文档汇总了 {", ".join(chapters)} 中使用 `\\textcolor` 和 `\\mathcolor` 标记的所有关键字，按颜色分组。\n\n')

for color in colors:
    keywords = sorted(list(combined_keywords[color]))
    output_lines.append(f'## {color_meanings[color]}\n')
    output_lines.append(f'共 {len(keywords)} 个关键字：\n\n')
    for kw in keywords:
        output_lines.append(f'{kw}\n')
    output_lines.append('\n')

output_path = chapters_dir / 'color_keywords.md'
output_path.write_text(''.join(output_lines), encoding='utf-8')

print(f'已成功更新汇总表: {output_path}')
stats = [f'{c}={len(combined_keywords[c])}' for c in colors]
print(f'统计数据: {", ".join(stats)}')
