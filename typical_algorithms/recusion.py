from ..data_structure.stack_rightside import StackRightSide

rStack = StackRightSide()

def toStr(n, base):
    convert_str = '0123456789ABCDEF'
    if n < base:
        rStack.push(convert_str[n])
    else:
        rStack.push(convert_str[n//base])
        return toStr(n//base, base)

def main():
    #int to binary
    sample_num = 769
    toStr(sample_num, 2)

if __name__ == "__main__":
    main()


