import pysnooper

def transmute(input):
    result = []
    for i, char in enumerate(input):
        if char == '?':
            result.extend(transmute(input[:i] + '1' + input[i+1:]))
            result.extend(transmute(input[:i] + '0' + input[i+1:]))
            return result
    return [input]



if __name__ == '__main__':
    result = transmute('?')
    print(result)