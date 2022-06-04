mean_cattle = {
    "Argentina": 6_466_331_862_068.97,
    "Brazil": 16_240_605_428_571.40,
    "China": 15_912_008_607_142.90,
    "Germany": 4_305_389_241_379.31,
}

mean_chicken = {
    "Argentina": 1_480_375_068_965.52,
    "Brazil": 11_264_992_250_000.00,
    "China": 16_923_007_172_413.80,
    "Germany": 1_050_709_137_931.03,
}

mean_pig = {
    "Argentina": 397_042_241_379.31,
    "Brazil": 3_423_033_965_517.24,
    "China": 89_464_032_137_931.00,
    "Germany": 7_871_536_310_344.83,
}


class MeatValues():
    def __init__(self) -> None:
        self.mean_gado = mean_cattle
        self.mean_frango = mean_chicken
        self.mean_porco = mean_pig
