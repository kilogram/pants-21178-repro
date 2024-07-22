__defaults__({
  pex_binary: dict(environment="linux"),
  docker_image: dict(build_platform=["linux/amd64"]),
})

local_environment(
  name="local_linux",
  compatible_platforms=["linux_x86_64"],
  fallback_environment="docker",
  docker_env_vars=["AWS_PROFILE=apricot"]
)

local_environment(
  name="local_osx",
  compatible_platforms=["macos_arm64"],
)

docker_environment(
  name="docker",
  platform="linux_x86_64",
  image="203469039017.dkr.ecr.us-east-1.amazonaws.com/dev:0.1-5c3759b5c29c6754d817d4162cc38e9ed391f118d1859f5aac8d964d35ef2aca",
  docker_env_vars=["AWS_PROFILE=apricot"]
)
