---
title: "Setting up a GTest Hello World Project on Windows with MSYS2, MinGW-w64, and vcpkg"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - MSYS2
  - MinGW-w64
  - vcpkg
  - Google Test
  - Setup Guide
---


Welcome to my updated demo of a **Google Test** “Hello, World!” project on Windows using **MSYS2**, **MinGW-w64**, and **vcpkg**. In this guide, we’ll walk through:

1. Adjusting environment variable priority in Windows so the correct `g++` is picked up.  
2. Installing and configuring MSYS2, MinGW-w64, and vcpkg.  
3. Dealing with common issues such as “Unable to find a valid Visual Studio instance” and how to ensure we’re using the `x64-mingw-dynamic` triplet.  
4. Building and running a minimal Google Test example.

<!--more-->

## 1. Prioritize the Correct Compiler in Windows

When you have multiple versions of `g++` on your system (from MSYS2, Cygwin, or elsewhere), it’s important that **MSYS2’s MinGW-w64** compiler is picked up first. You can check which ones are visible in `PATH` by opening **Command Prompt** (not MSYS2) and running:

```
C:\Users\Gordon> where g++
```

![Screenshot showing multiple g++ paths in Windows environment](/assets/images/gtest-demo/where-g++.png)

If you see multiple paths, reorder your Windows environment variables so that:

```
C:\msys64\mingw64\bin
```

appears **before** any others in the PATH. This ensures that when you run `g++`, Windows uses the MinGW-w64 version first.

1. **Open** “System Properties” → “Advanced” → “Environment Variables.”
2. **Edit** the `Path` variable and move `C:\msys64\mingw64\bin` to the top.
3. **Apply** changes and **restart** any open terminals so the updated PATH is recognized.

## 2. Installing MSYS2 and MinGW-w64

1. **Install MSYS2**  
   [Download MSYS2](https://www.msys2.org/) and run through the official installer.

2. **Open MSYS2** and **update** packages with:
   ```bash
   pacman -Syuu
   ```
   (Follow on-screen prompts, then reopen MSYS2 if necessary.)

3. **Install Required Tools** (in MSYS2 MingW64 shell):
   ```bash
   pacman -S --needed git base-devel mingw-w64-x86_64-toolchain \
     mingw-w64-x86_64-clang mingw-w64-x86_64-cmake
   ```

4. **Create a Symlink for `make`**  
   By default, MinGW’s make is named `mingw32-make.exe`. To ease usage:
   ```bash
   cd /mingw64/bin
   ln -s mingw32-make.exe make.exe
   ```

## 3. Bootstrapping vcpkg in MSYS2

### 3.1 Clone vcpkg

In the **MingW64** terminal:

```bash
cd /mingw64/bin
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
```

### 3.2 Run the Bootstrap Script

```bash
./bootstrap-vcpkg.bat
```

![Screenshot showing successful vcpkg bootstrap](/assets/images/gtest-demo/bootstrap-done.png)

## 4. Common Installation Pitfall

If you try installing GTest **before** specifying your triplet, you may see:

```
error: in triplet x64-windows: Unable to find a valid Visual Studio instance
Could not locate a complete Visual Studio instance
```

![Screenshot showing the error when installing gtest without setting the correct triplet](/assets/images/gtest-demo/install-error.png)

This happens because vcpkg defaults to the `x64-windows` triplet, expecting Visual Studio.

## 5. Setting the Correct Triplet

To use MinGW-w64, **export** these environment variables first:

```bash
export VCPKG_DEFAULT_TRIPLET=x64-mingw-dynamic
export VCPKG_DEFAULT_HOST_TRIPLET=x64-mingw-dynamic
```

Then install GTest again:

```bash
./vcpkg install gtest
```

![Screenshot showing successful gtest install with x64-mingw-dynamic](/assets/images/gtest-demo/install-gtest-mingw.png)

## 6. Integrate vcpkg (Optional)

Run:

```bash
./vcpkg integrate install
```

![Screenshot of successful vcpkg integrate install](/assets/images/gtest-demo/vcpkg-integrate.png)

This instructs you to use:

```
-DCMAKE_TOOLCHAIN_FILE=C:/msys64/mingw64/bin/vcpkg/scripts/buildsystems/vcpkg.cmake
```

in your CMake commands.

## 7. Verifying Installed Packages

Check what’s installed with:

```bash
./vcpkg list
```

![Screenshot of `vcpkg list` showing gtest installed](/assets/images/gtest-demo/gtest-installed.png)

You should see `gtest:x64-mingw-dynamic` listed.

## 8. Creating a Minimal GTest Project

Here’s a simple folder structure for a “Hello, World!” project:

```
gtest_MinGW64_vscode_win_helloworld/
├── CMakeLists.txt
├── src/
│   └── main.cpp
└── tests/
    └── test_helloworld.cpp
```

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10)
project(GTestHelloWorld CXX)

# Option A: Hard-code the vcpkg toolchain file here
#set(CMAKE_TOOLCHAIN_FILE "C:/msys64/mingw64/bin/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "" FORCE)

# Option B: Omit the line above and specify via command line

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(helloworld src/main.cpp)

find_package(GTest CONFIG REQUIRED)

add_executable(tests tests/test_helloworld.cpp)
target_link_libraries(tests PRIVATE GTest::gtest GTest::gtest_main)

enable_testing()
add_test(NAME MyHelloWorldTest COMMAND tests)
```

### `src/main.cpp`

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### `tests/test_helloworld.cpp`

```cpp
#include <gtest/gtest.h>

// Sample function to test
int add(int a, int b) {
    return a + b;
}

TEST(HelloWorldTest, TestAdd) {
    EXPECT_EQ(add(2, 2), 4);
    EXPECT_EQ(add(-1, 1), 0);
}

TEST(HelloWorldTest, AnotherTest) {
    EXPECT_TRUE(true);
}
```

## 9. Building and Running Tests

1. **Create a `build` directory** and go inside it:
   ```bash
   cd gtest_MinGW64_vscode_win_helloworld
   mkdir build && cd build
   ```

2. **Invoke CMake** using the MinGW Makefiles generator and the vcpkg toolchain:
   ```bash
   cmake -G "MinGW Makefiles" \
     -DCMAKE_TOOLCHAIN_FILE=C:/msys64/mingw64/bin/vcpkg/scripts/buildsystems/vcpkg.cmake \
     -DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic \
     ..
   ```

3. **Build** the project:
   ```bash
   cmake --build .
   ```
   This produces `helloworld.exe` and `tests.exe`.

4. **Run the tests**:
   ```bash
   ./tests
   ```
   You should see Google Test’s output indicating 2 passing tests.

## Conclusion

By prioritizing the correct `g++` in your Windows PATH and setting the `x64-mingw-dynamic` triplet, you can avoid the Visual Studio dependency and run GTest projects with MSYS2 + MinGW-w64. The **vcpkg** package manager simplifies installing libraries like GTest, and you’re free to expand this skeleton into a more advanced project.

If you have any questions or run into issues, feel free to reach out. Happy coding!
