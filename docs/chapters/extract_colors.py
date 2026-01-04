import re
from collections import defaultdict
from pathlib import Path

chapters_dir = Path(r'd:\C2D\Desktop\Code\Latex\TexStudio\0.njuthesis\NJU_thesis_doctor__xcz\docs\chapters')
colors = ['gray', 'Maroon', 'PineGreen', 'Plum', 'NavyBlue']
color_meanings = {
    'gray': '灰色 gray — 自变量，或对应的散度分量 / 微分算子',
    'Maroon': '褐红 Maroon — 基础·通用概念',
    'PineGreen': '松树绿 PineGreen — 进阶·晶体光学',
    'Plum': '李子紫 Plum — 进阶·数学名词',
    'NavyBlue': '海军蓝 NavyBlue — 进阶·物理术语'
}

pattern = re.compile(r'\\textcolor\{(' + '|'.join(colors) + r')\}\{([^}]+)\}')

color_keywords = defaultdict(set)

for i in range(1, 5):
    filepath = chapters_dir / f'chapter{i}.tex'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        matches = pattern.findall(content)
        for color, keyword in matches:
            keyword = keyword.strip()
            if keyword:
                color_keywords[color].add(keyword)

# Generate markdown output
output_lines = ['# 颜色关键字汇总\n']
output_lines.append('本文档汇总了 chapter1.tex ~ chapter4.tex 中使用 `\\textcolor` 标记的所有关键字，按颜色分组。\n\n')

for color in colors:
    keywords = sorted(color_keywords[color])
    output_lines.append(f'## {color_meanings[color]}\n')
    output_lines.append(f'共 {len(keywords)} 个关键字：\n\n')
    for kw in keywords:
        output_lines.append(f'- {kw}\n')
    output_lines.append('\n')

output_path = chapters_dir / 'color_keywords.md'
output_path.write_text(''.join(output_lines), encoding='utf-8')
print(f'已保存至: {output_path}')
print(f'共提取: gray={len(color_keywords["gray"])}, Maroon={len(color_keywords["Maroon"])}, PineGreen={len(color_keywords["PineGreen"])}, Plum={len(color_keywords["Plum"])}, NavyBlue={len(color_keywords["NavyBlue"])}')
