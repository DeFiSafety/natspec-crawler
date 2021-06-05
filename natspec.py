from utils import count_occurences


def score(filename):
    if count_occurences(filename, "@inheritdoc") > 0:
        return None

    tags = count_tags(filename)
    required_tags = count_required_tags(filename)
    try:
        return min(100, int(tags/required_tags * 100))
    except:
        return f"Failed {filename}"


def count_tags(filename) -> (int):
    title_cnt = count_occurences(filename, "@title")
    author_cnt = count_occurences(filename, "@author")
    notice_cnt = count_occurences(filename, "@notice")
    param_cnt = count_occurences(filename, "@param")
    return_cnt = count_occurences(filename, "@return")
    
    return title_cnt + author_cnt + notice_cnt + param_cnt + return_cnt


def count_required_tags(filename) -> int:

    with open(filename, 'r') as myfile:
        lines = [''.join(line.split()) for line in myfile]
    
    cnt = 0

    for a, line in enumerate(lines):
        start = line[:8]

        if start.find('event') == 0 or start.find('interface') == 0:
            # NOTE: count for a @notice
            cnt += 1
            continue
        elif start.find('contract') == 0:
            # NOTE: count for a @title, @author, @notice
            cnt += 3
            continue

        if start.find('function') != 0:
            continue
        
        # NOTE: count for a @notice on a function
        cnt += 1

        if line.find(')') - line.find('(') == 1:
            continue

        func_dec = ''
        b = a

        while b < len(lines):
            nextline = lines[b]
            func_dec += nextline
            if "{" in nextline:
                break
            b += 1
        
        if 'private' in func_dec or 'internal' in func_dec:
            continue

        # Count params 
        func_args = func_dec[func_dec.find('('):func_dec.find(')')]
        if ',' not in func_args:
            cnt += 1
        else:
            cnt += len(func_args.split(','))

        # Count returns
        returns_pos = func_dec.find('returns')
        if returns_pos > 0:
            func_dec = func_dec[returns_pos:]
            returns_args = func_dec[func_dec.find('('):func_dec.find(')')]
            if ',' not in returns_args:
                cnt += 1
            else:
                cnt += len(returns_args.split(','))

    return cnt
