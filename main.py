from package1 import package1

def main():
    """main関数
    """
    test_package = package1.package1("test", 4, 5)
    test_package.print_pac_msg()

if __name__=="__main__":
    main()