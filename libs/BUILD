python_sources()

python_tests(name="tests")

vcs_version(
    name = "_version",
    generate_to="libs/_version.py",
    template='vcs_version = "{version}"',
)

pex_binary(
    name = 'print_version',
    entry_point="version.py",
    dependencies=[":_version"],
    include_tools=True,
)
