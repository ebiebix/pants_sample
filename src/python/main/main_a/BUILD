pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        ":lib",
    ],
    complete_platforms=[
        "src/python/pantsbuild/complete_platforms:python_38_slim_buster"
    ],
    shebang="/usr/bin/env python3.8"
)

python_sources(
    name="lib",
    dependencies=["src/python/lib/lib_a"],
    )

docker_image(name="image", dependencies=[":main"])
