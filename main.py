# 在此文件处编辑代码
def analyze_text(text):
    """  
分析文本中字符频率并按频率降序排列

参数：
text - 输入的字符串

返回：
list - 按字符频率降序排列的字符列表
"""  
    # 在此处增加代码
    # 创建字典来存储字符频率（不区分大小写）
    char_count = {}
    
    # 统计每个字符的出现次数（不区分大小写）
    for char in text:
        # 只统计字母字符（包括中文）
        if char.isalpha():
            # 将英文字母转换为小写，中文字符保持不变
            if char.isascii() and char.isalpha():
                char_key = char.lower()
            else:
                char_key = char
            char_count[char_key] = char_count.get(char_key, 0) + 1
    
    # 如果没有找到任何字母字符
    if not char_count:
        return []
    
    # 按频率降序排序，频率相同则按字符升序排列
    # 使用元组排序：先按频率降序(-count)，再按字符升序(char)
    sorted_chars = sorted(char_count.items(), 
                         key=lambda x: (-x[1], x[0]))
    
    # 返回字符列表（只返回字符，不包含频率）
    return [char for char, count in sorted_chars]


# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("=========================")
    print("请输入一段文本（输入空行结束）：")

    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    # 合并输入文本
    text = "\n".join(lines)

    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        if sorted_chars:
            print("\n字符频率降序排列:")
            print(",".join(sorted_chars))
            
            # 额外显示详细信息
            print("\n详细分析:")
            print("=" * 30)
            
            # 重新统计以显示频率（不区分大小写）
            char_count = {}
            for char in text:
                if char.isalpha():
                    if char.isascii() and char.isalpha():
                        char_key = char.lower()
                    else:
                        char_key = char
                    char_count[char_key] = char_count.get(char_key, 0) + 1
            
            # 按频率降序显示，频率相同按字符升序
            sorted_details = sorted(char_count.items(), 
                                   key=lambda x: (-x[1], x[0]))
            
            for char, count in sorted_details:
                print(f"'{char}': {count}次")
        else:
            print("文本中没有找到字母字符！")

    # 提示用户比较不同语言
    print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
