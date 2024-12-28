---
title: "Setting up a GTest Hello World Project on Linux with GCC and CMake"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - GCC
  - Google Test
  - CMake
  - Setup Guide
---

In this guide, I will walk you through setting up a "Hello World" project using Google Test (GTest) on a Linux system with GCC and CMake. This tutorial is an adaptation of my earlier Windows-based setup, tailored for Ubuntu and other Linux environments. <!--more-->

### Prerequisites
Before starting, ensure you have the following installed:
- **GCC**: Install via `sudo apt install gcc g++ -y`.
- **CMake**: Install via `sudo apt install cmake -y`.
- **Google Test (GTest)**: Pre-installed as part of the `libgtest-dev` package on Ubuntu.

### Step 1: Install and Build Google Test
1. Install the `libgtest-dev` package:
   ```bash
   sudo apt update
   sudo apt install libgtest-dev -y
   ```

2. Navigate to the GTest source directory and build the libraries:
   ```bash
   cd /usr/src/gtest
   sudo cmake .
   sudo make
   ```

3. Copy the built libraries to `/usr/lib` for easier linking:
   ```bash
   sudo cp libgtest.a libgtest_main.a /usr/lib
   ```

### Step 2: Project Setup
#### Directory Structure
Organize your project as follows:
```
my_project/
├── src/
│   └── main.cpp
├── tests/
│   └── test_helloworld.cpp
├── CMakeLists.txt
```

### Step 3: Example Code
#### Main Application (src/main.cpp)
```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Hello, World! 5 + 3 = " << add(5, 3) << std::endl;
    return 0;
}
```

#### Test File (tests/test_helloworld.cpp)
```cpp
#include <gtest/gtest.h>
#include "../src/main.cpp"

TEST(HelloWorldTest, TestAdd) {
    EXPECT_EQ(add(5, 3), 8);
}

TEST(HelloWorldTest, AnotherTest) {
    EXPECT_EQ(add(-2, 2), 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```

### Step 4: Configure CMake
#### Top-Level `CMakeLists.txt`
```cmake
cmake_minimum_required(VERSION 3.10)
project(GTestHelloWorld CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Create an executable from main.cpp
add_executable(helloworld src/main.cpp)

# Find Google Test
find_package(GTest REQUIRED)

# Create a test executable
add_executable(run_tests tests/test_helloworld.cpp)

# Link Google Test to the test executable
target_link_libraries(run_tests PRIVATE GTest::gtest GTest::gtest_main pthread)

# Enable CTest
enable_testing()
add_test(NAME MyHelloWorldTest COMMAND run_tests)

# Custom target to run tests
add_custom_target(tests_run ALL
    COMMAND run_tests
    DEPENDS run_tests
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)
```

### Step 5: Build and Run
1. Create a build directory and configure the project:
   ```bash
   mkdir build && cd build
   cmake ..
   ```

2. Build the project:
   ```bash
   make
   ```

3. Run the tests:
   ```bash
   ./run_tests
   ```

### Example Output
```
Running main() from ./googletest/src/gtest_main.cc
[==========] Running 2 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 2 tests from HelloWorldTest
[ RUN      ] HelloWorldTest.TestAdd
[       OK ] HelloWorldTest.TestAdd (0 ms)
[ RUN      ] HelloWorldTest.AnotherTest
[       OK ] HelloWorldTest.AnotherTest (0 ms)
[----------] 2 tests from HelloWorldTest (0 ms total)

[==========] 2 tests from 1 test suite ran. (0 ms total)
[  PASSED  ] 2 tests.
```

### Conclusion
You have successfully set up a "Hello World" project using Google Test on Linux with GCC and CMake. This process demonstrates the power of CMake and GTest for cross-platform testing.

Let me know if you have any questions or improvements for this guide!

