from dataclasses import dataclass, field



@dataclass(order=True)
class Videogame:
    # add sort index, so that we can tell our class HOW to sort (step 1)
    # and tell the dataclass not to use in instantiation nor print (step 3)
    sort_index: int = field(init=False, repr=False)
    title: str
    developer: str
    release: int
    protagonist: str = "N/A"

    # use the post_init method to tell the class WHAT to use for sorting (step 2)
    def __post_init__(self):
        self.sort_index = self.release




smw = Videogame("Super Mario World", "Nintendo", 1990)
mgs = Videogame("Metal Gear Solid", "Sony", 1998, "Solid Snake")
halo = Videogame("Halo", "Microsoft", 2001, "Master Chief")
halo_again = Videogame("Halo", "Microsoft", 2001)

# Let's print a few things and see how this looks
print(smw)
print(mgs)
print(halo)
print(halo_again)

print(f"Is halo the same as halo_again? {halo == halo_again}")
print(f"Did Halo come out after Super Mario World? {halo > smw}")
print(f"Did Metal Gear Solid come out after Halo? {mgs > halo}")