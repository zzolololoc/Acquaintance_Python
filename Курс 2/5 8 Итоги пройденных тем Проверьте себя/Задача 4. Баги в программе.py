def check_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def check_name(names):
    forbidden_start_chars = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
    valid_files = []
    # В names передаётся список с одним элементом-строкой, разбиваем на слова
    file_list = names[0].split()
    for filename in file_list:
        if not filename.startswith(forbidden_start_chars) and filename.endswith(('.txt', '.docx')):
            valid_files.append(filename)
    return valid_files

def combine(data):
    result = []
    for ip, names in data:
        if check_ip(ip):
            valid_files = check_name(names)
            if valid_files:
                result.append([ip, [' '.join(valid_files)]])
    return result


data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]


filtered_data = combine(data)
for combine_result in filtered_data:
    print(combine_result)


# for record in data:
#     ip,name = record
#     print(ip)
#     sort_ip(ip)