def wish_dish(d):
    """wash dish"""
    if (int(str(d)[8:10]) % 3 == 0) or str(d)[8:9] == "3" or str(d)[9:10] == "3":
        print(f"今天该徐婉丽洗碗 ，日期为{d}")
    else:
        print(f"今天该夏世勇洗碗 ，日期为{d}")


if __name__ == "__main__":
    """yyyy-MM-dd"""
    wish_dish("2021-02-08")
