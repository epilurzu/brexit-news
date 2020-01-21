import src.daily_mirror as daily_mirror
import src.daily_star as daily_star
import src.the_guardian as the_guardian
import src.the_sun as the_sun
import src.the_telegraph as the_telegraph


def start(newspaper):
    print()

    return {
        "0": the_guardian.start,
        "1": the_sun.start,
        "2": daily_star.start,
        "3": the_telegraph.start,
        "4": daily_mirror.start
    }[newspaper]()


print("""
[0] The Guardian
[1] The Sun
[2] Daily Star
[3] The Telegraph
[4] Daily Mirror

Choose the newspaper to scrape: """, end="")

start(input())
