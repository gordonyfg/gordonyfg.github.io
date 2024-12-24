```yaml
---
title: "Automating Google Test on Windows with MSYS2, MinGW-w64, vcpkg, and GitHub Actions"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - MSYS2
  - MinGW-w64
  - vcpkg
  - Google Test
  - GitHub Actions
---
```
Below is a blog post focused on **Continuous Integration (CI)** for our **GTest Hello World** project using **GitHub Actions** on Windows, leveraging MSYS2, MinGW-w64, and vcpkg. This builds on the project from [our previous blog post](https://gordonyfg.github.io/blog/post-gtest_mingw64_vscode_win/) (the one titled “Setting up a GTest Hello World Project on Windows with MSYS2, MinGW-w64, and vcpkg”). In this new post, we’ll show how to **automate** your project’s builds and test runs with a custom GitHub Actions workflow.

<!--more-->

## Why Automate?

1. **Consistency**: Each push or pull request triggers an automated build, preventing “it works on my machine” surprises.  
2. **Early Bug Detection**: If your code introduces a regression, you’ll catch it right away because your tests will fail in CI.  
3. **Confidence**: Team members can merge new features with assurance that the code passes a clean build on Windows.

## 1. Project Recap

From our [previous tutorial](#), you should have a structure like:

```
gtest_MinGW64_vscode_win_helloworld/
├── CMakeLists.txt
├── src/
│   └── main.cpp
└── tests/
    └── test_helloworld.cpp
```

And your `CMakeLists.txt` references Google Test via **vcpkg**:

```cmake
cmake_minimum_required(VERSION 3.10)
project(GTestHelloWorld CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(helloworld src/main.cpp)

find_package(GTest CONFIG REQUIRED)

add_executable(tests tests/test_helloworld.cpp)
target_link_libraries(tests PRIVATE GTest::gtest GTest::gtest_main)

enable_testing()
add_test(NAME MyHelloWorldTest COMMAND tests)
```

## 2. Add a GitHub Actions Workflow

Inside your repository, create a folder named `.github/workflows` (if it doesn’t exist) and add a file named `cmake-gtest.yml`. Here’s an example that uses:

1. **MSYS2** to install the MinGW compiler toolchain and CMake.  
2. **vcpkg** to fetch Google Test and other libraries.  
3. **CMake** to configure the build with “MinGW Makefiles.”  
4. **CTest** to run the Google Test binary and report results.

### `.github/workflows/cmake-gtest.yml`

```yaml
name: "CMake GTest CI"

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
      # 1. Check out the repository
      - uses: actions/checkout@v3

      # 2. Install MSYS2 (which includes MinGW and CMake if specified)
      - name: Setup MSYS2
        uses: msys2/setup-msys2@v2
        with:
          msystem: MINGW64
          update: true
          install: >-
            mingw-w64-x86_64-gcc
            mingw-w64-x86_64-cmake
            mingw-w64-x86_64-make

      # 3. (Optional) Cache vcpkg to speed up builds
      - name: Cache vcpkg
        uses: actions/cache@v3
        with:
          path: |
            ${{ github.workspace }}/vcpkg
            ${{ github.workspace }}/vcpkg_cache
          key: vcpkg-${{ runner.os }}-${{ hashFiles('**/vcpkg.json') }}

      # 4. Install vcpkg locally if it's not cached
      - name: Install vcpkg
        run: |
          git clone https://github.com/Microsoft/vcpkg.git
          .\vcpkg\bootstrap-vcpkg.bat

      # 5. Configure with CMake using the MSYS2 shell
      - name: Configure with CMake (MSYS2 shell)
        shell: msys2 {0}
        run: |
          mkdir build
          cd build

          # Point CMake to the vcpkg toolchain file and specify x64-mingw-dynamic
          cmake -G "MinGW Makefiles" \
            -DCMAKE_TOOLCHAIN_FILE="${GITHUB_WORKSPACE}/vcpkg/scripts/buildsystems/vcpkg.cmake" \
            -DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic \
            -DCMAKE_PREFIX_PATH="${GITHUB_WORKSPACE}/vcpkg/installed/x64-mingw-dynamic" \
            ../gtest_MinGW64_vscode_win_helloworld

      # 6. Build your code
      - name: Build
        shell: msys2 {0}
        run: |
          cd build
          cmake --build . --config ${{ env.BUILD_TYPE }}

      # 7. Run your tests with ctest
      - name: Test
        shell: msys2 {0}
        run: |
          cd build
          ctest -C ${{ env.BUILD_TYPE }} --output-on-failure
```

### Explanation

1. **`msys2/setup-msys2@v2`**: Installs MSYS2 plus the MinGW-w64 tools (`mingw-w64-x86_64-gcc`, `mingw-w64-x86_64-cmake`, etc.) and sets up the PATH for us.  
2. **Caching vcpkg**: We store the `vcpkg` folder so that subsequent workflow runs won’t have to re-download everything.  
3. **Bootstrap vcpkg**: Clones vcpkg and runs `bootstrap-vcpkg.bat`, giving us `vcpkg.exe`.  
4. **CMake Configuration**:  
   - **`shell: msys2 {0}`** runs these commands inside the MSYS2 environment, so “MinGW Makefiles” can be used.  
   - **`-DCMAKE_TOOLCHAIN_FILE`** points to `vcpkg.cmake`, letting CMake use libraries installed via vcpkg.  
   - **`-DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic`** ensures GTest is installed for MinGW rather than Windows+MSVC.  
5. **Build & Test**: Uses `cmake --build .` and then `ctest`.

## 3. Verify the CI Results

Whenever you push or open a pull request, GitHub Actions will:

1. Check out your code.  
2. Install MSYS2, including the MinGW compiler.  
3. Install vcpkg and GTest (if not cached).  
4. Build your “Hello World” project.  
5. Run the GTest-based tests.  

In your GitHub repository’s “Actions” tab, you should see something like:

```
1/1 Test #1: MyHelloWorldTest .................   Passed    0.01 sec
100% tests passed, 0 tests failed out of 1
```

## 4. Dealing with Common Issues

- **`CMAKE_MAKE_PROGRAM is not set`**: Ensure you use `shell: msys2 {0}` so the MinGW `make` is on the PATH.  
- **`Could not find a package configuration file provided by "GTest"`**: Make sure GTest is installed for the same triplet (`x64-mingw-dynamic`) you configure in CMake.  
- **“Visual Studio instance” errors**: This happens if you forget the MinGW triplet. By default, vcpkg tries `x64-windows`, looking for MSVC.

## 5. Extending the Workflow

- **Multiple Platforms**: Add more jobs for Linux/macOS if you want cross-platform CI.  
- **Matrix Builds**: Test different compilers or build types by using a matrix strategy.  
- **Coverage Reports**: Integrate coverage tools (e.g., `gcov` + Codecov) for deeper insights into test coverage.

## Conclusion

That’s it! You now have a GitHub Actions workflow that automatically compiles your Google Test “Hello World” project in an MSYS2 + MinGW-w64 environment on Windows and runs tests every time you push or open a PR. This automated pipeline gives you **confidence** in your code changes by quickly detecting breakages or regressions.

Feel free to customize your `.github/workflows/cmake-gtest.yml` to include additional steps, run different configurations, or generate artifact uploads. Once you’ve mastered these basics, you’ll have a robust, professional CI system for your C++ projects. Good luck, and happy coding!