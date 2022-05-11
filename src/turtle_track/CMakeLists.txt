cmake_minimum_required(VERSION 3.5)
project(turtle_track)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(FastRTPS_INCLUDE_DIR /opt/ros/foxy/include)
set(FastRTPS_LIBRARY_RELEASE /opt/ros/foxy/lib/libfastrtps.so)

# find dependencies

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

#添加执行文件
aux_source_directory(./src SRC_LIST)

set(SRC_LIST_WITHOUTE)
#file(READ "src/*.cpp" SRC_LIST)
#去掉扩展名
foreach(SRC_FILE ${SRC_LIST})
  get_filename_component(SRC_FILE_WITHOUTE ${SRC_FILE} NAME_WLE)
  set(SRC_LIST_WITHOUTE ${SRC_LIST_WITHOUTE} ${SRC_FILE_WITHOUTE} )
endforeach()
message(STATUS "${SRC_LIST_WITHOUTE}")
foreach(SRC_FILE ${SRC_LIST_WITHOUTE})
  add_executable(${SRC_FILE} src/${SRC_FILE}.cpp)
endforeach()
#add_executable(ObjectRecognizer src/ObjectRecognizer.cpp)
#add_executable(PhotoCapture src/PhotoCapture.cpp)
#基础库
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

foreach(TARGET_NAME ${SRC_LIST_WITHOUTE})
  target_include_directories(${TARGET_NAME} PUBLIC
          $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
          $<INSTALL_INTERFACE:include>)
endforeach()
set(AMENT_DEPENDENCIES ${AMENT_DEPENDENCIES} rclcpp std_msgs )



#tf2 库
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(turtlesim REQUIRED)
find_package(geometry_msgs REQUIRED)
include_directories(
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)
set(AMENT_DEPENDENCIES ${AMENT_DEPENDENCIES}
        nav_msgs
        tf2
        tf2_ros
        geometry_msgs
        rclcpp
        turtlesim
)


# 依赖库链接安装等
install(
        DIRECTORY include/
        DESTINATION include
)
install(
        DIRECTORY launch/
        DESTINATION share/${PROJECT_NAME}/launch
)
message(STATUS "${SRC_LIST_WITHOUTE}")
foreach(TARGET_NAME ${SRC_LIST_WITHOUTE})
  ament_target_dependencies(${TARGET_NAME} ${AMENT_DEPENDENCIES})
  install(TARGETS ${TARGET_NAME}
          DESTINATION lib/${PROJECT_NAME})
endforeach()



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()