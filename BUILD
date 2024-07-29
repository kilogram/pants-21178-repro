__defaults__({
  pex_binary: dict(environment="linux"),
  docker_image: dict(build_platform=["linux/amd64"]),
})

local_environment(
  name="local_linux",
  compatible_platforms=["linux_x86_64"],
  fallback_environment="docker",
)

local_environment(
  name="local_osx",
  compatible_platforms=["macos_arm64"],
)

docker_environment(
  name="docker",
  platform="linux_x86_64",
  image="python:3.9.14-slim-bullseye",
)
