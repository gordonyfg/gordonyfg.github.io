---
title: "Setting Up Google Test (GTest) on Linux: A Complete Workflow"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Linux
  - Google Test
  - CMake
  - Setup Guide
  - CI/CD
---

In this post, I will guide you through setting up a **Google Test (GTest)** workflow on Linux, ensuring seamless integration of building, testing, and debugging for C++ projects. This guide complements my earlier post, [Extending GTest CI with Structured Tests and Execution Insights](https://gordonyfg.github.io/blog/post-gtest_structured_test/), with a focus on Linux-based development. <!--more-->

### Prerequisites
Ensure the following tools are installed on your Linux system:
- **GCC**:
  ```bash
  sudo apt install gcc g++ -y
  ```
- **CMake**:
  ```bash
  sudo apt install cmake -y
  ```
- **Google Test**:
  ```bash
  sudo apt install libgtest-dev -y
  ```

---

### Step 1: Build Google Test Libraries
Google Test libraries need to be built manually as they are not precompiled:

1. Navigate to the GTest source directory:
   ```bash
   cd /usr/src/gtest
   ```

2. Build the libraries:
   ```bash
   sudo cmake .
   sudo make
   ```

3. Copy the built libraries to a system-wide directory:
   ```bash
   sudo cp libgtest.a libgtest_main.a /usr/lib
   ```

---

### Step 2: Project Setup
#### Directory Structure
Organize your project as follows:
```
Embedded-Cpp/
├── src/                # Source files
│   ├── AccessLog.cpp
│   ├── heap_stack.cpp
│   ├── leetcode/
│   │   └── src/
│   │       ├── LC167.cpp
│   │       ├── LC653.cpp
│   │       └── Solution.h
│   ├── LRU.cpp
│   └── Merge_SLL.cpp
├── tests/              # Test files
│   ├── gtest_helpers/
│   │   └── gtest_main.cpp
│   ├── test_LC167.cpp
│   └── test_LC653.cpp
├── CMakeLists.txt      # Top-level CMake file
├── build_and_test.sh   # Build and test script for Linux
```

#### Example Test File: `tests/test_LC167.cpp`
```cpp
#include <gtest/gtest.h>
#include "../../src/leetcode/src/LC167.cpp"

TEST(LC167, ExampleTest) {
    std::vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    Solution solution;
    EXPECT_EQ(solution.twoSum(numbers, target), (std::vector<int>{1, 2}));
}

TEST(LC167, EdgeCaseTest) {
    std::vector<int> numbers = {1, 3, 5, 7};
    int target = 10;
    Solution solution;
    EXPECT_EQ(solution.twoSum(numbers, target), (std::vector<int>{2, 3}));
}
```

---

### Step 3: Configure CMake
#### Top-Level `CMakeLists.txt`
```cmake
cmake_minimum_required(VERSION 3.16)

project(embedded_cpp)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add main leetcode solutions library
file(GLOB LEETCODE_SOURCES
    "src/*.cpp"
    "src/leetcode/src/*.cpp"
)

add_library(leetcode_solutions STATIC
    ${LEETCODE_SOURCES}
)

# Include directories for leetcode solutions
target_include_directories(leetcode_solutions PUBLIC
    ${CMAKE_SOURCE_DIR}/src
)

# Find and link GoogleTest
find_package(GTest REQUIRED)

# Add tests executable
file(GLOB TEST_SOURCES
    "tests/gtest_helpers/*.cpp"
    "tests/*.cpp"
)

add_executable(tests
    ${TEST_SOURCES}
)

# Include directories for tests
target_include_directories(tests PRIVATE
    ${CMAKE_SOURCE_DIR}/tests
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/leetcode/src
)

# Link libraries for tests
target_link_libraries(tests PRIVATE
    GTest::gtest
    GTest::gtest_main
    leetcode_solutions
)

# Enable testing
enable_testing()
add_test(NAME AllTests COMMAND tests)
```

---

### Step 4: Build and Test Locally
#### Build and Test Script: `build_and_test.sh`
```bash
#!/bin/bash

# Set variables
PROJECT_DIR=$(pwd)
BUILD_DIR="$PROJECT_DIR/build"

# Clean up the build directory if it exists
if [ -d "$BUILD_DIR" ]; then
    echo "Cleaning up the build directory..."
    rm -rf "$BUILD_DIR"
fi

# Create a new build directory
mkdir "$BUILD_DIR"
cd "$BUILD_DIR" || exit

# Configure the project with CMake
echo "Configuring the project..."
cmake "$PROJECT_DIR" -DCMAKE_BUILD_TYPE=Release
if [ $? -ne 0 ]; then
    echo "CMake configuration failed!"
    exit 1
fi

# Build the project
echo "Building the project..."
cmake --build .
if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

# Run tests using CTest
echo "Running tests..."
ctest --output-on-failure
if [ $? -ne 0 ]; then
    echo "Tests failed!"
    exit 1
fi

# Optional: Run the test binary directly
echo "Running test binary..."
if [ -f tests ]; then
    ./tests
fi

echo "Build and tests completed successfully!"
```

#### Example Output:
```
Cleaning up the build directory...
Configuring the project...
-- Configuring done (0.4s)
-- Generating done (0.0s)
-- Build files have been written to: /home/gordon-yeung/projects/Embedded-Cpp/build
Building the project...
[100%] Built target tests
Running tests...
Test project /home/gordon-yeung/projects/Embedded-Cpp/build
    Start 1: AllTests
1/1 Test #1: AllTests .........................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =   0.00 sec
Running test binary...
[==========] Running 7 tests from 2 test suites.
[----------] Global test environment set-up.
[----------] 2 tests from LC167
[ RUN      ] LC167.ExampleTest
[       OK ] LC167.ExampleTest (0 ms)
[ RUN      ] LC167.EdgeCaseTest
[       OK ] LC167.EdgeCaseTest (0 ms)
[----------] 2 tests from LC167 (0 ms total)

[----------] 5 tests from LC653Test
[ RUN      ] LC653Test.Example1
[       OK ] LC653Test.Example1 (0 ms)
[ RUN      ] LC653Test.Example2
[       OK ] LC653Test.Example2 (0 ms)
[ RUN      ] LC653Test.EmptyTree
[       OK ] LC653Test.EmptyTree (0 ms)
[ RUN      ] LC653Test.SingleNode
[       OK ] LC653Test.SingleNode (0 ms)
[ RUN      ] LC653Test.LargerTree
[       OK ] LC653Test.LargerTree (0 ms)
[----------] 5 tests from LC653Test (0 ms total)

[----------] Global test environment tear-down
[==========] 7 tests from 2 test suites ran. (0 ms total)
[  PASSED  ] 7 tests.
Build and tests completed successfully!
```

---

### Conclusion
You’ve successfully set up a GTest workflow for Linux, including building, testing, and debugging. This guide demonstrates how to maintain a robust local development process while leveraging the power of GTest and CMake. For advanced CI integration, refer to my earlier post: [Extending GTest CI with Structured Tests and Execution Insights](https://gordonyfg.github.io/blog/post-gtest_structured_test/).

Let me know your thoughts or questions in the comments below!

