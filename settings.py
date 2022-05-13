from os import environ


SESSION_CONFIGS = [
    dict(
        name="bonus_game",
        display_name="The Bonus Game",
        num_demo_participants=10,
        # app_sequence=["bonus_game", "bret", "debrief", "thanks"],
        app_sequence=["introduction", "bonus_game", "bret", "debrief", "thanks"],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.005,
    participation_fee=1.20,
    deception=False,
    simulated_play_time=5,
    doc=""
)

SESSION_FIELDS = ["prolific_completion_url"]

PARTICIPANT_FIELDS = ["finished"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "GBP"
USE_POINTS = True

ROOMS = [
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    # ),
    dict(name="live_demo", display_name="Room for live demo (no participant labels)"),
]

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# OTREE_PRODUCTION = 1


SECRET_KEY = "%c(+094mz4$hp4gud-&*hs*s$-)ejkbz5sw7$d@526uj$i$nuw"

INSTALLED_APPS = ["otree"]

# DATABASE_URL  = postgres://postgres@localhost/django_db
