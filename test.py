from pprint import pprint
import toml

a = toml.load("./config.toml")
pprint(a)

