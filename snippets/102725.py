
class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs


if __name__ == "__main__":
    spider = Animal(4,5)
    total_limbs = spider.limbs()
    print(total_limbs)


