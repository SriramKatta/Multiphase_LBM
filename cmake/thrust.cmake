include(FetchContent)

FetchContent_Declare(
  Thrust
  GIT_REPOSITORY https://github.com/NVIDIA/thrust.git
  GIT_TAG 3cd5684
)
FetchContent_MakeAvailable(Thrust)

find_package(Thrust REQUIRED CONFIG)
thrust_create_target(Thrust)