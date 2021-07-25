class Videogame:
    def __init__(self, title, developer, release):
        self.title = title
        self.developer = developer
        self.release = release




smw = Videogame("Super Mario World", "Nintendo", 1990)
mgs = Videogame("Metal Gear Solid", "Sony", 1998)
halo = Videogame("Halo", "Microsoft", 2001)
halo_again = Videogame("Halo", "Microsoft", 2001)

# Let's print a few things and see how this looks
print(smw)
print(mgs)
print(halo)
print(halo_again)

print(f"Is halo the same as halo_again? {halo == halo_again}")