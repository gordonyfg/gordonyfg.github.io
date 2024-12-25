---
title: "Extending GTest CI with Structured Tests and Execution Insights"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - MSYS2
  - MinGW-w64
  - vcpkg
  - Google Test
  - GitHub Actions
  - Continuous Integration
---

## Extending GTest CI with Structured Tests and Execution Insights

In my previous posts, I covered how to set up a basic **Google Test** (GTest) project on Windows using **MSYS2**, **MinGW-w64**, and **vcpkg**, and subsequently integrated it with **GitHub Actions** for Continuous Integration (CI). In this post, I’ll demonstrate how I extended the CI workflow to include structured test execution and detailed output insights, making it easier to understand test results both locally and in CI environments.

<!--more-->

---

### Motivation
After setting up the basic CI workflow, I noticed discrepancies between local test execution and CI output. Local tests provided detailed insights about individual test cases, while CI only displayed high-level summaries via `ctest`. To bridge this gap, I:
1. Structured my tests into meaningful test suites.
2. Enhanced the CI configuration to include detailed test outputs and per-test execution times.

---

### Enhancing the Project Structure
To ensure my tests are modular and maintainable, I grouped related functionality into separate test suites. For example, here’s how I structured tests for **LeetCode Problem 167** (LC167):

#### Updated Project Structure
```
C:/Users/Gordon/Documents/Developer/2024_embedded_c++/
├── src/
│   ├── AccessLog.cpp
│   ├── LRU.cpp
│   ├── Merge_SLL.cpp
│   ├── leetcode/
│   │   └── LC167.cpp
├── tests/
│   ├── gtest_helpers/
│   │   └── gtest_main.cpp
│   ├── test_LC167.cpp
│   └── test_helpers.h
├── build/ (Generated after running CMake)
```

#### Example Test Suite (`test_LC167.cpp`)
```cpp
#include <gtest/gtest.h>
#include "LC167.cpp" // Include the solution implementation

TEST(LC167, ExampleTest) {
    std::vector<int> input = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> expected = {1, 2};
    EXPECT_EQ(twoSum(input, target), expected);
}

TEST(LC167, EdgeCaseTest) {
    std::vector<int> input = {1, 2};
    int target = 3;
    std::vector<int> expected = {1, 2};
    EXPECT_EQ(twoSum(input, target), expected);
}
```

---

### Updated CI Workflow with Test Insights
To align CI output with local execution details, I enhanced the `ctest` configuration and included options for verbose logging and direct binary execution.

#### Updated GitHub Actions YAML
Here’s the complete GitHub Actions YAML configuration, updated to include structured tests and execution insights:

```yaml
---
name: CMake GTest CI with Detailed Insights

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  BUILD_TYPE: Release

jobs:
  build:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v3

    - name: Setup MSYS2
      uses: msys2/setup-msys2@v2
      with:
        msystem: MINGW64
        update: true
        install: >
          mingw-w64-x86_64-gcc
          mingw-w64-x86_64-cmake
          mingw-w64-x86_64-make

    - name: Cache vcpkg
      uses: actions/cache@v3
      with:
        path: |
          ${{github.workspace}}/vcpkg
          ${{github.workspace}}/vcpkg_cache
        key: vcpkg-${{ runner.os }}-${{ hashFiles('**/vcpkg.json') }}

    - name: Install vcpkg
      run: |
        git clone https://github.com/Microsoft/vcpkg.git
        .\vcpkg\bootstrap-vcpkg.bat
        .\vcpkg\vcpkg.exe install gtest:x64-mingw-dynamic

    - name: Configure with CMake
      shell: msys2 {0}
      run: |
        mkdir build
        cd build
        cmake -G "MinGW Makefiles" \
          -DCMAKE_TOOLCHAIN_FILE="${GITHUB_WORKSPACE}/vcpkg/scripts/buildsystems/vcpkg.cmake" \
          -DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic \
          -DCMAKE_PREFIX_PATH="${GITHUB_WORKSPACE}/vcpkg/installed/x64-mingw-dynamic" \
          ..

    - name: Build
      shell: msys2 {0}
      run: |
        cd build
        cmake --build . --config ${{env.BUILD_TYPE}}

    - name: Test with CTest
      shell: msys2 {0}
      run: |
        cd build
        ctest -C ${{env.BUILD_TYPE}} --output-on-failure --verbose

    - name: Run Test Binary for Detailed Insights
      shell: msys2 {0}
      run: |
        cd build
        ./tests.exe
```

---

### Benefits of the Updates
1. **Structured Tests**: Organized tests make it easier to identify issues and add new cases.
2. **Execution Insights**: Using `ctest --verbose` and directly running the test binary provides both high-level summaries and detailed execution logs.
3. **Debugging**: Clearer outputs make it easier to debug failures in both local and CI environments.

---

### Conclusion
These updates significantly enhance the testing workflow, making it robust and developer-friendly. Whether you're solving algorithmic problems or writing production code, having a structured and insightful CI setup ensures your work is reliable and maintainable.

Stay tuned for more posts as I continue improving the CI pipeline and explore advanced topics like code coverage and performance benchmarking in GTest!

--- 
