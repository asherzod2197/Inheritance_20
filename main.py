# 20. Mashq rejalashtiruvchisi

class Workout:
    def __init__(self, workout_type, duration_minutes):
        self.workout_type = workout_type    # "Yugurish", "Yoga", "Kuch mashqlari" va h.k.
        self.duration = duration_minutes    # daqiqa

    def total_time(self):
        """Mashqning davomiyligi (daqiqa)"""
        return self.duration

    def __str__(self):
        return f"{self.workout_type:12} | {self.duration:4} daqiqa"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class Cardio(Workout):
    def __str__(self):
        return f"🏃‍♂️ {self.workout_type:10} → {self.duration:3} daqiqa"


class Yoga(Workout):
    def __str__(self):
        return f"🧘 {self.workout_type:10} → {self.duration:3} daqiqa"


# Qo‘shimcha mashq turi misoli (foydali bo‘lishi mumkin)
class Strength(Workout):
    def __str__(self):
        return f"🏋️ {self.workout_type:10} → {self.duration:3} daqiqa"


# --------------------------------------------------
# Haftalik reja va umumiy vaqtni chiqarish
# --------------------------------------------------

def show_weekly_workout_plan(workouts):
    print("\n" + "═" * 60)
    print("     HAFTALIK MASHQ REJASI — UMUMIY VAQT HISOBI     ".center(60))
    print("═" * 60)
    print("Mashq turi           Davomiyligi")
    print("─" * 60)

    total_minutes = 0

    for w in workouts:
        print(w)
        total_minutes += w.total_time()

    hours = total_minutes // 60
    minutes_left = total_minutes % 60

    print("─" * 60)
    print(f"Jami mashq vaqti:   {total_minutes:4} daqiqa "
          f"({hours} soat {minutes_left:02d} daqiqa)")
    print("═" * 60 + "\n")


# Test ma'lumotlari (haftalik reja misoli)
mashqlar = [
    Cardio("Yugurish", 60),
    Yoga("Yoga sessiyasi", 45),
    Cardio("Velosiped", 50),
    Strength("Kuch mashqlari", 40),
    Yoga("Yin yoga", 30),
    Cardio("Interval yugurish", 35),
]

show_weekly_workout_plan(mashqlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol rejangiz:\n")
misol_mashqlar = [
    Cardio("Yugurish", 60),
    Yoga("Yoga", 45),
]

show_weekly_workout_plan(misol_mashqlar)
