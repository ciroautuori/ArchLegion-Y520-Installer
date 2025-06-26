# legion_profile/profile.py
from archinstall import Profile

# Definisci il percorso assoluto del profilo
# Questo è necessario perché archinstall cambia directory
__profile_dir__ = __file__[0:__file__.rfind('/')]

# Definisci il profilo
class LegionProfile(Profile):
    def __init__(self):
        super().__init__(
            'Legion-Y520',
            'Profilo personalizzato per Lenovo Legion Y520',
            '/usr/share/archinstall/profiles/minimal.py' # Eredita dal profilo minimo
        )

    @property
    def packages(self):
        # Legge i pacchetti dal nostro file
        with open(f"{__profile_dir__}/packages.x86_64", "r") as pkg_file:
            return [pkg.strip() for pkg in pkg_file.readlines() if pkg.strip() and not pkg.strip().startswith('#')]

# Esponi il profilo ad archinstall
profile = LegionProfile()
