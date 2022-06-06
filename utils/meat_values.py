mean_cattle = {
    "Argentina": 6_466_331.86,
    "Brazil": 16_240_605.43,
    "China": 15_912_008.61,
    "Germany": 4_305_389.24,
}

mean_chicken = {
    "Argentina": 1_480_375.07,
    "Brazil": 11_264_992.25,
    "China": 16_923_007.17,
    "Germany": 1_050_709.14,
}

mean_pig = {
    "Argentina": 320_329.32,
    "Brazil": 3_454_392.18,
    "China": 89_464_032.14,
    "Germany": 7_871_536.31,
}


class MeatValues():
    def __init__(self) -> None:
        self.mean_gado = mean_cattle
        self.mean_frango = mean_chicken
        self.mean_porco = mean_pig
