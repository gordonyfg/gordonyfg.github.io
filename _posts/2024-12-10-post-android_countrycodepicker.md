---
title: "Enhancing an Open-Source Android Library: CountryCodePicker"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Android
  - Open Source
  - GitHub
  - CI/CD
  - Jitpack
---

In this post, I want to share my experience contributing to an open-source Android library, [CountryCodePicker](https://github.com/Ajinkrishnak/CountryCodePicker). From discovering a bug to fixing it, making a pull request, and eventually distributing the library via Jitpack, this journey highlights my problem-solving skills and commitment to the developer community.

## The Problem

While integrating the CountryCodePicker library into my project, I encountered a bug that disrupted its functionality. After debugging the issue, I identified the root cause and resolved it in a local branch. Upon further investigation, I realized that other users had reported the same issue on GitHub ([Issue #5](https://github.com/Ajinkrishnak/CountryCodePicker/issues/5)). This indicated that my fix could benefit others who relied on this library.

## Forking and Fixing the Library

To share my solution, I forked the original repository and applied the bug fix. My changes included:

1. **Bug Identification and Resolution**: I carefully analyzed the reported issue, replicated it, and made targeted changes to the source code to eliminate the problem.
2. **Testing**: I ensured that the fix was thoroughly tested across different scenarios to confirm its effectiveness.
3. **Documentation**: I updated relevant documentation to inform users of the fix and how it addressed the issue.

The updated version of the library can be found in my GitHub repository: [gordonyfg/CountryCodePicker](https://github.com/gordonyfg/CountryCodePicker).

## Making a Pull Request

After committing and pushing my changes to the forked repository, I created a pull request to the original repository, proposing the fix for inclusion. However, it appeared that the original maintainer was too busy to review and merge the changes.

## Distributing the Library with Jitpack

To ensure that other developers could benefit from the fix, I decided to distribute the library independently. Using [Jitpack](https://jitpack.io/), a platform that simplifies the process of publishing Java and Android libraries, I went through the CI/CD process to make the updated library available for public use. Here’s how developers can integrate it:

```groovy
dependencies {
    implementation 'com.github.gordonyfg:CountryCodePicker:v1.0.1'
}
```

### Key Steps in CI/CD with Jitpack

1. **Repository Preparation**:
   - Ensured the forked repository included the required Jitpack configuration, such as a valid `build.gradle` file.
   - Tagged the release version (`v1.0.1`) to align with semantic versioning standards.

2. **Testing the Build**:
   - Verified that the build succeeded on Jitpack by checking the logs and resolving any dependency issues.

3. **Documentation**:
   - Updated the README to guide users on integrating the library into their projects.

## Lessons Learned

This experience provided valuable insights into:

- **Open Source Collaboration**: Engaging with the developer community by contributing code and documentation.
- **Bug Fixing and Testing**: Diagnosing and resolving issues in a structured and efficient manner.
- **CI/CD Pipelines**: Leveraging Jitpack for seamless library distribution.
- **Communication**: Documenting my work clearly to help other developers adopt the fix.

## Conclusion

Contributing to an open-source project like CountryCodePicker was a rewarding experience. It allowed me to solve a real-world problem, enhance my technical skills, and give back to the community. By distributing the updated library via Jitpack, I ensured that developers could continue to rely on this tool without disruption.

I’m excited to take on similar challenges in future projects and look forward to contributing more to the open-source ecosystem. If you have any questions or feedback, feel free to reach out via [GitHub](https://github.com/gordonyfg) or [LinkedIn](https://www.linkedin.com/in/gordon-yeung-349b66133/).

